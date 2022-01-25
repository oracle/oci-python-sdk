#!/bin/sh
#############################################################################################################################
# Author - Adi Zohar, Jul 7th 2020
#
# run_gather_stats for crontab use weekly run
#
# Amend variables below and database connectivity
#
# Crontab set:
# 30 0 * * 0 timeout 6h /home/opc/usage_reports_to_adw/shell_scripts/run_gather_stats.sh > /home/opc/usage_reports_to_adw/run_gather_stats_run.txt 2>&1
#############################################################################################################################
# Env Variables based on yum instant client
export CLIENT_HOME=/usr/lib/oracle/current/client64
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:$CLIENT_HOME/lib:$CLIENT_HOME
export PATH=$PATH:$CLIENT_HOME/bin:$CLIENT_HOME

# App dir
export TNS_ADMIN=$HOME/ADWCUSG
export APPDIR=$HOME/usage_reports_to_adw
export CREDFILE=$APPDIR/config.user
cd $APPDIR

# Mail Info
export DATE_PRINT="`date '+%d-%b-%Y'`"

# database info
export DATABASE_USER=`grep "^DATABASE_USER" $CREDFILE | awk -F= '{ print $2 }'`
export DATABASE_PASS=`grep "^DATABASE_PASS" $CREDFILE | awk -F= '{ print $2 }'`
export DATABASE_NAME=`grep "^DATABASE_NAME" $CREDFILE | awk -F= '{ print $2 }'`

# Fixed variables
export DATE=`date '+%Y%m%d_%H%M'`
export REPORT_DIR=${APPDIR}/report/daily
export OUTPUT_FILE=${REPORT_DIR}/gather_stats_${DATE}.txt
mkdir -p ${REPORT_DIR}

##################################
# run stats
##################################
echo "Running Gather Stats, Log = $OUTPUT_FILE"
echo "
set pages 0 head off feed off lines 799 trimsp on echo off verify off
set define @
exec dbms_stats.gather_schema_stats(ownname=>'USAGE',DEGREE=>8,estimate_percent=>10,block_sample=>TRUE,stattype=>'DATA',force=>TRUE, method_opt=>'FOR ALL COLUMNS SIZE 1',cascade=>TRUE);
" | sqlplus -s ${DATABASE_USER}/${DATABASE_PASS}@${DATABASE_NAME} | tee -a $OUTPUT_FILE

# Check for errors
if (( `grep ORA- $OUTPUT_FILE | wc -l` > 0 ))
then
    echo ""
    echo "!!! Error running gather stats, check logfile $OUTPUT_FILE"
    echo ""
    grep ORA- $OUTPUT_FILE
    exit 1
fi

