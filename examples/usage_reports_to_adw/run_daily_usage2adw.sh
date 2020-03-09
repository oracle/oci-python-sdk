#!/bin/ksh
#############################################################################################################################
# Author - Adi Zohar, Feb 28th 2020
#
# Run daily usage load for crontab use
#
# Amend variables below and database connectivity
#
# Crontab set:
# 0 0 * * * timeout 6h /home/opc/usage_adw/run_daily_usage2adw.sh > /home/opc/usage_adw/run_daily_usage2adw_crontab_run.txt 2>&1
#############################################################################################################################
# Update below variables
export ORACLE_HOME=$HOME/instantclient_18_3
export TNS_ADMIN=$ORACLE_HOME/network/admin
export PYTHONPATH=$HOME/python
export APPDIR=$HOME/usage2adw

# database info
export DATABASE_USER=user
export DATABASE_PASS=password#
export DATABASE_NAME=adw_low
export MIN_DATE=2020-02-01

# Fixed variables
export DATE=`date '+%Y%m%d_%H%M'`
export PATH=${PATH}:${ORACLE_HOME}:${PYTHONPATH}/bin
export LD_LIBRARY_PATH=${ORACLE_HOME}
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

run_report tenant_name  &
wait

echo "Completed at `date`.."

