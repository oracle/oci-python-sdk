#!/bin/bash
#############################################################################################################################
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# Initial Setup credentials
# Written by Adi Zohar, October 2020
# Git Location = https://github.com/oracle/oci-python-sdk/tree/master/examples/usage_reports_to_adw
#
# Version 2021-04-27
#
#########################################################################################################################

export APPDIR=/home/opc/usage_reports_to_adw
export CREDFILE=$APPDIR/config.user
export LOG=/home/opc/setup_credentials.log
rm -f $LOG
echo "##################################################" | tee -a $LOG
echo "# Start process at `date`" | tee -a $LOG
echo "##################################################" | tee -a $LOG

###########################################
# Request Application Credential
###########################################
echo "" | tee -a $LOG
echo "########################################################################" | tee -a $LOG
echo "# 5. Application Credentials, stored at $CREDFILE" | tee -a $LOG
echo "########################################################################" | tee -a $LOG
printf "Please Enter Database Name     : "; read DATABASE_NAME
printf "Please Enter ADB Admin Password: "; read DATABASE_ADMIN
printf "Please Enter ADB Application Password (Min 12 Chars, One Upper, One Lower, One Digits): "; read DATABASE_PASS
printf "Please Enter Extract Start Date (Format YYYY-MM i.e. 2021-04): "; read EXTRACT_DATE
printf "Please Enter Tag Key to extract as Special Tag (Oracle-Tags.CreatedBy): "; read TAG_SPECIAL

if [ -z "$TAG_SPECIAL" ]; then
    TAG_SPECIAL="Oracle-Tags.CreatedBy"
fi

echo "DATABASE_USER=USAGE" > $CREDFILE
echo "DATABASE_NAME=${DATABASE_NAME}_low" >> $CREDFILE
echo "DATABASE_PASS=${DATABASE_PASS}" >> $CREDFILE 
echo "DATABASE_ADMIN=${DATABASE_ADMIN}" >> $CREDFILE
echo "EXTRACT_DATE=${EXTRACT_DATE}" >> $CREDFILE
echo "TAG_SPECIAL=${TAG_SPECIAL}" >> $CREDFILE
echo "" | tee -a $LOG
echo "Below Data written to $CREDFILE:" | tee -a $LOG
cat $CREDFILE | tee -a $LOG
echo "" | tee -a $LOG
echo "Setup Packages Completed." | tee -a $LOG
echo "" | tee -a $LOG
echo "########################################################################" | tee -a $LOG
echo "# Please download the database wallet to /home/opc/wallet.zip "           | tee -a $LOG
echo "# Then execute $APPDIR/setup/setup_usage2adw.sh"                          | tee -a $LOG
echo "########################################################################" | tee -a $LOG
