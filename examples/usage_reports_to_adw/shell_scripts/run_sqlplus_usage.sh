#!/bin/sh
#############################################################################################################################
# Author - Adi Zohar, Mar 18 2023
#
# run_sqlplus_usage.sh
#
#############################################################################################################################
# Env Variables based on yum instant client
export CLIENT_HOME=/usr/lib/oracle/current/client64
export PATH=$PATH:$CLIENT_HOME/bin

# App dir
export TNS_ADMIN=$HOME/ADWCUSG
export APPDIR=$HOME/usage_reports_to_adw
export CREDFILE=$APPDIR/config.user
cd $APPDIR

# database info
export DATABASE_USER=`grep "^DATABASE_USER" $CREDFILE | awk -F= '{ print $2 }'`
export DATABASE_PASS=`grep "^DATABASE_PASS" $CREDFILE | awk -F= '{ print $2 }'`
export DATABASE_NAME=`grep "^DATABASE_NAME" $CREDFILE | awk -F= '{ print $2 }'`

##################################
# run sqlplus
##################################
sqlplus ${DATABASE_USER}/${DATABASE_PASS}@${DATABASE_NAME}
