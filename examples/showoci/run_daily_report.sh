#!/bin/bash
#############################################################################################################################
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# Author - Adi Zohar, May 15th 2019, Amended Feb 10, 2023
#
# Run daily report for crontab use
# Generates daily report including JSON file and latest CSV files
#
# Amend APPDIR
#
# Crontab set:
# 0 0 * * * timeout 6h /home/opc/showoci/run_daily_report.sh > /home/opc/showoci/run_daily_report_crontab_run.txt 2>&1
#############################################################################################################################
. ~/.bashrc >/dev/null
export DATE=`date '+%Y%m%d'`
export APPDIR=$HOME/showoci
export REPORT_DIR=${APPDIR}/report

##################################
# Report Function
##################################
run_report()
{
	NAME=$1
	if [ -z "$NAME" ]
	then
		exit 1
	fi

	DIR=${REPORT_DIR}/$NAME
	CSV_DIR=${DIR}/csv
	OUTPUT_FILE=${DIR}/${DATE}_${NAME}.txt
	JSON_FILE=${DIR}/${DATE}_${NAME}.json.txt
	CSV_FILE=${CSV_DIR}/${NAME}

    echo "###################################################################################"
    echo "# Start running showoci for $NAME at `date`"
    echo "###################################################################################"
    echo "# Output File = $OUTPUT_FILE"
    echo "# JSON   File = $JSON_FILE"
    echo "###################################################################################"
    echo "Please Wait ..."

	mkdir -p $DIR
    mkdir -p $CSV_DIR
	echo "Running $NAME... to $OUTPUT_FILE "

    # if using instant principle don't add -t
    if [ "$2" = "-ip" ]
    then
	    python3 $APPDIR/showoci.py -ani $2 $3 $4 $5 $6 -sjf $JSON_FILE -csv $CSV_FILE > $OUTPUT_FILE 2>&1
    else
	    python3 $APPDIR/showoci.py -ani -t $NAME $2 $3 $4 $5 $6 -sjf $JSON_FILE -csv $CSV_FILE > $OUTPUT_FILE 2>&1
    fi

    grep -i "Error in" $OUTPUT_FILE |grep -v "LB_Errors"

    # if showoci_csv2excel exist, remove the comment
    # python3 $APPDIR/showoci_csv2excel.py $CSV_FILE >> $OUTPUT_FILE

    ERROR=""
    WARNING=""

    if (( `grep -i "Error in" $OUTPUT_FILE | grep -v "LB_Errors" | wc -l` > 0 ))
    then
        ERROR=" with **** Errors ****"
    fi

    if (( `grep -i "Service Warning" $OUTPUT_FILE | wc -l` > 0 ))
    then
        WARNING=" with **** Warnings ****"
    fi

    echo "Run Cleanup..."

    # Cleanup - Gzip after 7 days, delete after 180
    /usr/bin/find ${DIR} -name "*.txt" -mtime +7  -exec gzip '{}' \;
    /usr/bin/find ${DIR} -name "*.txt" -mtime +180 -exec rm -f '{}' \;

    echo "###################################################################################"
	echo "# Finish `date` - $NAME $ERROR $WARNING "
    echo "###################################################################################"

}

##################################
# Main
##################################

run_report local -ip 
# run_report tenant_name_profile
