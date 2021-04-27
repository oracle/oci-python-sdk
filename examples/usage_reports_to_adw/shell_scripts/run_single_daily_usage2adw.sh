#!/bin/bash
#############################################################################################################################
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# Author - Adi Zohar, Feb 28th 2020
#
# Run Single daily usage load for crontab use or manual execution
#
# Crontab set to run every 6 hours
# 0 */6 * * * timeout 6h /home/opc/usage_reports_to_adw/shell_scripts/run_single_daily_usage2adw.sh > /home/opc/usage_reports_to_adw/run_single_daily_usage2adw_crontab_run.txt 2>&1
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

# database info
export DATABASE_USER=`grep "^DATABASE_USER" $CREDFILE | awk -F= '{ print $2 }'`
export DATABASE_PASS=`grep "^DATABASE_PASS" $CREDFILE | awk -F= '{ print $2 }'`
export DATABASE_NAME=`grep "^DATABASE_NAME" $CREDFILE | awk -F= '{ print $2 }'`
export TAG_SPECIAL=`grep "^TAG_SPECIAL" $CREDFILE | awk -F= '{ print $2 }'`
export MIN_DATE=`grep "^EXTRACT_DATE" $CREDFILE | awk -F= '{ print $2 }'`

# Fixed variables
export DATE=`date '+%Y%m%d_%H%M'`
export REPORT_DIR=${APPDIR}/report
mkdir -p ${REPORT_DIR}
export OUTPUT_FILE=${REPORT_DIR}/${DATE}.txt

# execute using instance principles
echo "Running ... to $OUTPUT_FILE and screen"

python3 $APPDIR/usage2adw.py -ip -du $DATABASE_USER -dp $DATABASE_PASS -dn $DATABASE_NAME -d $MIN_DATE -ts "${TAG_SPECIAL}" | tee -a $OUTPUT_FILE

grep -i "Error" $OUTPUT_FILE
echo "Finished at `date`  "


