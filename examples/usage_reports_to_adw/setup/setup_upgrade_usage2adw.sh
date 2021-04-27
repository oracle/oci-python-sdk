#!/bin/bash
#############################################################################################################################
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# Setup Upgrade for usage2adw
# Written by Adi Zohar, October 2020
# Git Location = https://github.com/oracle/oci-python-sdk/tree/master/examples/usage_reports_to_adw
#
# If script fail, please add the policies and re-run
#
# Version 2020-10-22
#
#########################################################################################################################

###################################################
# Check file usage2adw.py location
###################################################
echo "##################################################" | tee -a $LOG
echo "# Upgrade usage2adw" | tee -a $LOG
echo "##################################################" | tee -a $LOG
cd /home/opc
echo "Checking file usage2adw.py location before upgrade"
if [ -f "/home/opc/usage_reports_to_adw/usage2adw.py" ]; then
   echo "   File usage2adw.py exist in app - /home/opc/usage_reports_to_adw/usage2adw.py " 
elif [ -f "/home/opc/oci-python-sdk/examples/usage_reports_to_adw/usage2adw.py" ]; then
   echo "   File usage2adw.py exist in oci-python-sdk location, /home/opc/oci-python-sdk/examples/usage_reports_to_adw/usage2adw.py"
   echo "   Creating Symbolic Link: ln -s /home/opc/oci-python-sdk/examples/usage_reports_to_adw ."
   ln -s /home/opc/oci-python-sdk/examples/usage_reports_to_adw .
else
   echo "   File usage2adw.py could not find, cannot upgrade, abort "
   exit 1
fi

###################################################
# Check if to upgrade
###################################################
echo ""
echo "Upgrade usage2adw will upgrade the below:"
echo "1. usage2adw.py"
echo "2. APEX Application - All additional users will be removed"
printf "Do you want to continue (y/n) ? "; read ANSWER

if [ "$ANSWER" = 'y' ]
then
   echo ""
else
   exit 0
fi

###################################################
# Start process
###################################################
source ~/.bashrc >/dev/null

export APPDIR=/home/opc/usage_reports_to_adw
export CREDFILE=$APPDIR/config.user
export LOG=/home/opc/upgrade.log
export LOGDIR=$APPDIR/setup/log
export GIT=https://raw.githubusercontent.com/oracle/oci-python-sdk/master/examples/usage_reports_to_adw

cd $APPDIR
mkdir -p $LOGDIR
rm -f $LOG

echo "##################################################" | tee -a $LOG
echo "# Start process at `date`" | tee -a $LOG
echo "##################################################" | tee -a $LOG
echo "# Log = $LOG "
echo ""
echo "" | tee -a $LOG
echo "1. Check if Credential File Exist - $CREDFILE" | tee -a $LOG

if [ -f "$CREDFILE" ]; then
   echo "   File exists." | tee -a $LOG
else
   echo "   File does not exist, Please provide information below:" tee -a $LOG
   printf "   Please Enter Database Name     : "; read DATABASE_NAME
   printf "   Please Enter ADB Admin Password: "; read DATABASE_ADMIN
   printf "   Please Enter ADB App  Password : "; read DATABASE_PASS
   printf "   Please Enter Tag Key to extract as Special Tag (Oracle-Tags.CreatedBy): "; read TAG_SPECIAL

   if [ -z "$TAG_SPECIAL" ]; then
       TAG_SPECIAL="Oracle-Tags.CreatedBy"
   fi

   echo "DATABASE_USER=USAGE" > $CREDFILE   
   echo "DATABASE_NAME=${DATABASE_NAME}_low" >> $CREDFILE
   echo "DATABASE_PASS=${DATABASE_PASS}" >> $CREDFILE 
   echo "DATABASE_ADMIN=${DATABASE_ADMIN}" >> $CREDFILE
   echo "EXTRACT_DATE=2021-04" >> $CREDFILE
   echo "TAG_SPECIAL=${TAG_SPECIAL}" >> $CREDFILE
   echo "File Created." | tee -a $LOG
fi

###########################################
# Read App info from file
###########################################
echo "2. Read App info from file" | tee -a $LOG
db_app_password=`grep "^DATABASE_PASS" $CREDFILE | awk -F= '{ print $2 }'`
db_db_name=`grep "^DATABASE_NAME" $CREDFILE | awk -F= '{ print $2 }'`

###########################################
# Download files from github
###########################################
echo "" | tee -a $LOG
echo "3. Download Files from github - $GIT " | tee -a $LOG
echo "   Download usage2adw.py" | tee -a $LOG
wget ${GIT}/usage2adw.py -O ${APPDIR}/usage2adw.py -o $LOGDIR/usage2adw.py.download.log| tee -a $LOG
if [ $? -eq 0 ]; then
   echo "   usage2adw.py downloaded successfully" | tee -a $LOG
else
   echo "   Error Downloading usage2adw.py, Abort, log=$LOGDIR/usage2adw.py.download.log" | tee -a $LOG
   exit 1
fi

echo "   Download usage.demo.apex.sql" | tee -a $LOG
wget ${GIT}/apex_demo_app/usage.demo.apex.sql -O ${APPDIR}/apex_demo_app/usage.demo.apex.sql -o $LOGDIR/usage.demo.apex.sql.download.log| tee -a $LOG
if [ $? -eq 0 ]; then
   echo "   usage.demo.apex.sql downloaded successfully" | tee -a $LOG
else
   echo "   Error Downloading usage.demo.apex.sql, Abort, log=$LOGDIR/usage.demo.apex.sql.download.log" | tee -a $LOG
   exit 1
fi

echo "   Download enable_apex.sql" | tee -a $LOG
wget ${GIT}/setup/enable_apex.sql -O ${APPDIR}/setup/enable_apex.sql -o $LOGDIR/enable_apex.sql.download.log| tee -a $LOG
if [ $? -eq 0 ]; then
   echo "   enable_apex.sql downloaded successfully" | tee -a $LOG
else
   echo "   Error Downloading enable_apex.sql, Abort, log=$LOGDIR/enable_apex.sql.download.log" | tee -a $LOG
   exit 1
fi

###########################################
# Download files from github
###########################################
echo "" | tee -a $LOG
echo "4. List files." | tee -a $LOG
ls -lrt ${APPDIR}/usage2adw.py ${APPDIR}/apex_demo_app/usage.demo.apex.sql ${APPDIR}/setup/enable_apex.sql | tee -a $LOG

###########################################
# Delete APEX App and import New App
###########################################
echo "" | tee -a $LOG
slog=$LOGDIR/upgrade_apex_application.log
echo "5. Upgrade APEX application" | tee -a $LOG
echo "   sqlplus USAGE/${db_app_password}@${db_db_name} @$APPDIR/setup/enable_apex.sql" | tee -a $LOG
echo "set echo on serveroutput on time on lines 199 trimsp on pages 1000 verify off
spool $slog
define pass=$db_app_password
@${APPDIR}/setup/enable_apex.sql
spool off
" | sqlplus -s USAGE/${db_app_password}@${db_db_name} >> $LOG

if (( `egrep 'ORA-|SP2-' $slog | egrep -v 'ORA-00955|ORA-00001|ORA-06512' | wc -l` > 0 )); then
   egrep 'ORA-|SP2-' $slog | egrep -v 'ORA-00955|ORA-00001|ORA-06512'
   echo "   Error upgrading APEX APP, please check log $slog, aborting."
   exit 1
else
   echo "   Okay." | tee -a $LOG
fi

###########################################
# Completed
###########################################
echo "" | tee -a $LOG
echo "##################################################" | tee -a $LOG
echo "# Upgrade Completed at `date`" | tee -a $LOG
echo "##################################################" | tee -a $LOG
echo "Please run the application to upgrade schema:" | tee -a $LOG
echo "/home/opc/usage_reports_to_adw/shell_scripts/run_single_daily_usage2adw.sh" | tee -a $LOG
echo ""

