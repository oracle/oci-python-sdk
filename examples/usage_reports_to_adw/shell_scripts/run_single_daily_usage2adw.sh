#!/bin/bash
#############################################################################################################################
# Author - Adi Zohar, Feb 28th 2020
#
# Run Single daily usage load for crontab use
#
# Amend variables below and database connectivity
#
# Crontab set:
# 0 0 * * * timeout 6h /home/opc/oci-python-sdk/examples/usage_reports_to_adw/shell_scripts/run_single_daily_usage2adw.sh > /home/opc/oci-python-sdk/examples/usage_reports_to_adw/shell_scripts/run_single_daily_usage2adw_crontab_run.txt 2>&1
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
export OUTPUT_FILE=${REPORT_DIR}/${DATE}.txt

# execute using instance principles
echo "Running ... to $OUTPUT_FILE "

python3 $APPDIR/usage2adw.py -ip -du $DATABASE_USER -dp $DATABASE_PASS -dn $DATABASE_NAME -d $MIN_DATE > $OUTPUT_FILE

grep -i "Error" $OUTPUT_FILE
echo "Finished at `date`  "


