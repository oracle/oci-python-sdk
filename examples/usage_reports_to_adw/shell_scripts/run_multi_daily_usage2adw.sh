#!/bin/bash
#############################################################################################################################
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# Author - Adi Zohar, Feb 28th 2020
#
# Run Multi daily usage load for crontab use
#
# Amend variables below and database connectivity
#
# Crontab set:
# 0 0 * * * timeout 6h /home/opc/oci-python-sdk/examples/usage_reports_to_adw/shell_scripts/run_multi_daily_usage2adw.sh > /home/opc/oci-python-sdk/examples/usage_reports_to_adw/shell_scripts/run_multi_daily_usage2adw_crontab_run.txt 2>&1
#############################################################################################################################

# Env Variables based on yum instant client
export CLIENT_HOME=/usr/lib/oracle/18.3/client64
export LD_LIBRARY_PATH=$CLIENT_HOME/lib
export PATH=$PATH:$CLIENT_HOME/bin

# App dir
export TNS_ADMIN=$HOME/ADWCUSG
export APPDIR=$HOME/oci-python-sdk/examples/usage_reports_to_adw

# database info
export DATABASE_USER=usage
export DATABASE_PASS=PaSsw0rd2#_#
export DATABASE_NAME=adwcusg_low
export MIN_DATE=2020-01-01

# Fixed variables
export DATE=`date '+%Y%m%d_%H%M'`
export REPORT_DIR=${APPDIR}/report
mkdir -p ${REPORT_DIR}

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
    OUTPUT_FILE=${DIR}/${DATE}_${NAME}.txt
    mkdir -p $DIR
    echo "Running $NAME... to $OUTPUT_FILE "
    python3 $APPDIR/usage2adw.py -t $NAME -du $DATABASE_USER -dp $DATABASE_PASS -dn $DATABASE_NAME -d $MIN_DATE > $OUTPUT_FILE
    grep -i "Error" $OUTPUT_FILE

    ERROR=""

    if (( `grep -i Error $OUTPUT_FILE | wc -l` > 0 ))
    then
        ERROR=" with **** Errors ****"
    fi

    echo "Finish `date` - $NAME $ERROR "
}

##################################
# Main
##################################
echo "Start running at `date`..."

run_report tenant_name_1 
run_report tenant_name_2 

echo "Completed at `date`.."