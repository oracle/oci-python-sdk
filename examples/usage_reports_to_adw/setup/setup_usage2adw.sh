#!/bin/bash
#############################################################################################################################
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# Setup for usage2adw
# Written by Adi Zohar, October 2020
# Git Location = https://github.com/oracle/oci-python-sdk/tree/master/examples/usage_reports_to_adw
#
# If script fail, please add the policies and re-run
#
# Version 2020-10-22
#
#########################################################################################################################
# Required Instant Principle Policy which includes the below:
#
#  1. Create new Dynamic Group : UsageDownloadGroup  
#     Obtain Compute OCID and add rule - ALL {instance.id = 'ocid1.instance.oc1.xxxxxxxxxx'}
#     or by compartment
#     Obtain Compartment OCID and add rule - ALL {instance.compartment.id = 'ocid1.compartment.oc1.xxxxxxxxxx'}
#
#  2. Create new Policy: UsageDownloadPolicy with Statements:
#     define tenancy usage-report as ocid1.tenancy.oc1..aaaaaaaaned4fkpkisbwjlr56u7cj63lf3wffbilvqknstgtvzub7vhqkggq
#     endorse dynamic-group UsageDownloadGroup to read objects in tenancy usage-report
#     Allow dynamic-group UsageDownloadGroup to inspect compartments in tenancy
#     Allow dynamic-group UsageDownloadGroup to inspect tenancies in tenancy
#########################################################################################################################

source ~/.bashrc >/dev/null

export APPDIR=/home/opc/usage_reports_to_adw
export CREDFILE=$APPDIR/config.user
export LOG=/home/opc/setup.log
export LOGDIR=$APPDIR/setup/log
export SCRIPT=$APPDIR/setup/setup_usage2adw.sh
export PYTHONUNBUFFERED=TRUE
cd $APPDIR/setup
mkdir -p $LOGDIR
rm -f $LOG
echo "##################################################" | tee -a $LOG
echo "# Start process at `date`" | tee -a $LOG
echo "##################################################" | tee -a $LOG

###########################################
# Create the adw properties file
###########################################
echo "" | tee -a $LOG
echo "1. Read Variables from config.user file." | tee -a $LOG

db_db_name=`grep "^DATABASE_NAME" $CREDFILE | awk -F= '{ print $2 }'`
db_app_password=`grep "^DATABASE_PASS" $CREDFILE | awk -F= '{ print $2 }'`
db_admin_password=`grep "^DATABASE_ADMIN" $CREDFILE| awk -F= '{ print $2 }'`
extract_from_date=`grep "^EXTRACT_DATE" $CREDFILE | awk -F= '{ print $2 }'`
extract_tag_special_key=`grep "^TAG_SPECIAL" $CREDFILE | awk -F= '{ print $2 }'`

###########################################
# Extract Wallet from wallet.zip
###########################################
mkdir -p /home/opc/ADWCUSG
echo "" | tee -a $LOG
echo "2. Extract database wallet." | tee -a $LOG
unzip -o $HOME/wallet.zip -d /home/opc/ADWCUSG
if [ $? -eq 0 ]; then
   echo "   Database Wallet extracted successfully" | tee -a $LOG
else
   echo "   Error Extracting, Abort" | tee -a $LOG
   exit 1
fi
rm -f wallet.zip wallet_file

###########################################
# Fixed sqlnet.ora parameter
###########################################
echo "" | tee -a $LOG
echo "3. Fixing sqlnet.ora directory parameter" | tee -a $LOG
sed -i "s#?/network/admin#$HOME/ADWCUSG#" ~/ADWCUSG/sqlnet.ora
if [ $? -eq 0 ]; then
   echo "   Done." | tee -a $LOG
else
   echo "   Error fixing sqlnet.ora, Abort" | tee -a $LOG
   exit 1
fi

###########################################
# Check Oci Connectivity
###########################################
echo "" | tee -a $LOG
echo "4. Checking OCI Connectivity using instance principles..." | tee -a $LOG
echo "   Executed: python3 check_connectivity.sh" | tee -a $LOG
slog=$LOGDIR/check_connectivity.log
rm -f $slog
python3 $APPDIR/setup/check_connectivity.py | tee -a $slog | tee -a $LOG
if (( `grep Error $slog | wc -l` > 0 )); then
   echo "   Error querying OCI, please check the log $slog" | tee -a $LOG
   echo "   Please check the documentation to have the dynamic group and policy correctted" | tee -a $LOG
   echo "   Once fixed you can rerun the script $SCRIPT" | tee -a $LOG
   echo "   Abort" | tee -a $LOG
   exit 1
else
   echo "   Okay." | tee -a $LOG
fi

###########################################
# create application schema and enable APEX
###########################################
echo "" | tee -a $LOG
slog=$LOGDIR/db_creation_user.log
echo "5. Creating USAGE user on ADWC instance and enable APEX Workspace" | tee -a $LOG
echo "   commands executed:" | tee -a $LOG
echo "   sqlplus ADMIN/${db_admin_password}@${db_db_name}" | tee -a $LOG
echo "   create user usage identified by ${db_app_password};" | tee -a $LOG
echo "   grant create dimension, connect, resource, dwrole, unlimited tablespace to usage;" | tee -a $LOG
echo "   exec apex_instance_admin.add_workspace(p_workspace => 'USAGE', p_primary_schema => 'USAGE');" | tee -a $LOG
echo "set lines 199 trimsp on pages 0 feed on
spool $slog
create user usage identified by ${db_app_password};
grant create dimension, connect, resource, dwrole, unlimited tablespace to usage;
exec apex_instance_admin.add_workspace(p_workspace => 'USAGE', p_primary_schema => 'USAGE');
" | sqlplus -s ADMIN/${db_admin_password}@${db_db_name} >> $LOG

if (( `grep ORA- $slog | egrep -v 'ORA-01920|ORA-20987|06512'| wc -l` > 0 )); then
   echo "   Error creating USAGE user, please check log $slog, aborting."
   exit 1
else
   echo "   Okay." | tee -a $LOG
fi

###########################################
# create tables and import APEX App
###########################################
echo "" | tee -a $LOG
slog=$LOGDIR/create_table_enable_apex.log
echo "6. Create USAGE Tables and Import APEX application" | tee -a $LOG
echo "   sqlplus USAGE/${db_app_password}@${db_db_name} @$APPDIR/setup/create_tables.sql" | tee -a $LOG
echo "   sqlplus USAGE/${db_app_password}@${db_db_name} @$APPDIR/setup/enable_apex.sql" | tee -a $LOG
echo "set echo on serveroutput on time on lines 199 trimsp on pages 1000 verify off
spool $slog
define pass=${db_app_password}
@$APPDIR/setup/create_tables
@$APPDIR/setup/enable_apex
spool off
" | sqlplus -s USAGE/${db_app_password}@${db_db_name} >> $LOG

if (( `egrep 'ORA-|SP2-' $slog | egrep -v 'ORA-00955|ORA-00001|ORA-06512' | wc -l` > 0 )); then
   egrep 'ORA-|SP2-' $slog | egrep -v 'ORA-00955|ORA-00001|ORA-06512'
   echo "   Error creating USAGE tables, please check log $slog, aborting."
   exit 1
else
   echo "   Okay." | tee -a $LOG
fi

###########################################
# Setup Crontab
###########################################
echo "" | tee -a $LOG
echo "7. Setup Crontab to run every 3 hours and gather stats every week" | tee -a $LOG
echo "Executed: crontab $APPDIR/setup/setup.crontab.txt" | tee -a $LOG
crontab $APPDIR/setup/setup.crontab.txt

###########################################
# run initial usage2adw
###########################################
echo "" | tee -a $LOG
echo "###############################################################" | tee -a $LOG
echo "# Running Initial usage2adw.py extract" | tee -a $LOG
echo "###############################################################" | tee -a $LOG
echo "   Command line: " | tee -a $LOG
echo "   python3 usage2adw.py -ip -du USAGE -dp ${db_app_password} -dn ${db_db_name} -d ${extract_from_date}" -ts "${extract_tag_special_key}" | tee -a $LOG
echo "" | tee -a $LOG | tee -a $LOG
cd $APPDIR
python3 usage2adw.py -ip -du USAGE -dp ${db_app_password} -dn ${db_db_name} -d ${extract_from_date} -ts "${extract_tag_special_key}" | tee -a $LOG
echo "" | tee -a $LOG

echo "############################################################################################" | tee -a $LOG
echo "# If process complete successfuly, please continue and login to APEX" | tee -a $LOG
echo "############################################################################################" | tee -a $LOG

