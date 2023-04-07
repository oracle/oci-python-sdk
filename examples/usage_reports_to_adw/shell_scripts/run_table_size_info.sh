#!/bin/sh
#############################################################################################################################
# Author - Adi Zohar, OCt 18 2022
#
# run_table_size_info.sh
#
# Extract Tenant, Compartment, Service and Cost to CSV
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
# run report
##################################
echo "
set pages 1000 lines 700 trimsp on 
col segment_name for a36
col gb for 999,999.99
select segment_name, sum(bytes/1024/1024/1024) GB
from user_segments
group by segment_name
having sum(bytes/1024/1024/1024) > 0.01
order by 2 desc;

" | sqlplus -s ${DATABASE_USER}/${DATABASE_PASS}@${DATABASE_NAME}

