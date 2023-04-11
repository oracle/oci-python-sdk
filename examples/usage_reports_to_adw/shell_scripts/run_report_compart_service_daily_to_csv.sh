#!/bin/sh
#############################################################################################################################
# Author - Adi Zohar, OCt 18 202
#
# run_report_compart_service_daily_to_csv.sh
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

# Fixed variables
export DATE=`date '+%Y%m%d'`
export REPORT_DIR=${APPDIR}/report/daily
export OUTPUT_FILE=${REPORT_DIR}/daily_compartment_service_${DATE}.csv
mkdir -p ${REPORT_DIR}

echo "Running Report to $OUTPUT_FILE ..."

##################################
# run report
##################################
echo "
set pages 0 head off feed off lines 799 trimsp on echo off verify off
set define @
col line for a1000

ALTER SESSION SET OPTIMIZER_IGNORE_HINTS=FALSE;
ALTER SESSION SET OPTIMIZER_IGNORE_PARALLEL_HINTS=FALSE;

prompt tenant,date,compartment,service,total

select tenant_name||','||usage_day||','||prd_compartment_name||','||prd_service||','||TOTAL line
from
(
    select /*+ parallel(oci_cost,8) full(oci_cost) */ 
        TENANT_NAME,
        to_char(USAGE_INTERVAL_START,'YYYY-MM-DD') as USAGE_DAY, 
        prd_compartment_name,
        replace(nvl(prd_service,COST_PRODUCT_SKU),'_',' ') prd_service,
        sum(COST_MY_COST) as TOTAL
    from oci_cost
    group by 
        TENANT_NAME,
        to_char(USAGE_INTERVAL_START,'YYYY-MM-DD'),
        prd_compartment_name,
        replace(nvl(prd_service,COST_PRODUCT_SKU),'_',' ')
    order by 1,2,3
);

" | sqlplus -s ${DATABASE_USER}/${DATABASE_PASS}@${DATABASE_NAME} > $OUTPUT_FILE

# Check for errors
if (( `grep ORA- $OUTPUT_FILE | wc -l` > 0 ))
then
    echo ""
    echo "!!! Error running daily report, check logfile $OUTPUT_FILE"
    echo ""
    grep ORA- $OUTPUT_FILE
    exit 1
fi

echo "File Exctracted to $OUTPUT_FILE"

