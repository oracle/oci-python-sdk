#!/bin/bash
#############################################################################################################################
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# Initial Setup unix Packages
# Written by Adi Zohar, October 2020
# Git Location = https://github.com/oracle/oci-python-sdk/tree/master/examples/usage_reports_to_adw
#
# Version 2020-10-22
#
#########################################################################################################################

export APPDIR=/home/opc/usage_reports_to_adw
export CREDFILE=$APPDIR/config.user
export LOG=/home/opc/setup_packages.log
rm -f $LOG
echo "##################################################" | tee -a $LOG
echo "# Start process at `date`" | tee -a $LOG
echo "##################################################" | tee -a $LOG

###########################################
# Install Python3, git and python packages
###########################################
echo "" | tee -a $LOG
echo "########################################################################" | tee -a $LOG
echo "# 1. Install Python3, Git and Python OCI Packages, Can take a moment." | tee -a $LOG
echo "########################################################################" | tee -a $LOG
sudo yum install -y python3 git | tee -a $LOG
sudo pip3 install oci oci-cli cx_Oracle requests | tee -a $LOG
echo "Completed." | tee -a $LOG

###########################################
# Install Oracle Instant Client
###########################################
echo "" | tee -a $LOG
echo "########################################################################" | tee -a $LOG
echo "# 2. Install Oracle Instant Client." | tee -a $LOG
echo "########################################################################" | tee -a $LOG
sudo yum install -y oracle-release-el7 | tee -a $LOG
sudo yum install -y oracle-instantclient19.8-basic.x86_64 oracle-instantclient19.8-sqlplus.x86_64 | tee -a $LOG
echo "Completed." | tee -a $LOG

###########################################
# Setup .bashrc profile
###########################################
echo "" | tee -a $LOG
echo "########################################################################" | tee -a $LOG
echo "# 3. Setup .bashrc env variables." | tee -a $LOG
echo "########################################################################" | tee -a $LOG
echo "export CLIENT_HOME=/usr/lib/oracle/19.8/client64" >>$HOME/.bashrc
echo "export LD_LIBRARY_PATH=$CLIENT_HOME/lib" >>$HOME/.bashrc
echo "export PATH=$PATH:$CLIENT_HOME/bin" >>$HOME/.bashrc
echo "export TNS_ADMIN=$HOME/ADWCUSG" >>$HOME/.bashrc
echo "export PYTHONUNBUFFERED=TRUE" >>$HOME/.bashrc
echo "Completed." | tee -a $LOG

###########################################
# Clone OCI Python SDK repo
###########################################
echo "" | tee -a $LOG
echo "########################################################################" | tee -a $LOG
echo "# 4. Clone OCI Python SDK Git." | tee -a $LOG
echo "########################################################################" | tee -a $LOG
git clone https://github.com/oracle/oci-python-sdk | tee -a $LOG
ln -s /home/opc/oci-python-sdk/examples/usage_reports_to_adw .
chmod +x /home/opc/usage_reports_to_adw/setup/*.sh
chmod +x /home/opc/usage_reports_to_adw/shell_scripts/*.sh
echo "Completed." | tee -a $LOG

echo "##################################################" | tee -a $LOG
echo "# End process at `date`" | tee -a $LOG
echo "##################################################" | tee -a $LOG
