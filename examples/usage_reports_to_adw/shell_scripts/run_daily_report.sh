#!/bin/sh
#############################################################################################################################
# Author - Adi Zohar, Jul 7th 2020
#
# daily_report for crontab use
#
# Amend variables below and database connectivity
#
# Crontab set:
# 0 7 * * * timeout 6h /home/opc/oci-python-sdk/examples/usage_reports_to_adw/shell_scripts > /home/opc/oci-python-sdk/examples/usage_reports_to_adw/shell_scripts/run_daily_report_crontab_run.txt 2>&1
#############################################################################################################################
# Env Variables based on yum instant client
export CLIENT_HOME=/usr/lib/oracle/19.6/client64
export LD_LIBRARY_PATH=$CLIENT_HOME/lib
export PATH=$PATH:$CLIENT_HOME/bin

# App dir
export TNS_ADMIN=$HOME/ADWCUSG
export APPDIR=$HOME/oci-python-sdk/examples/usage_reports_to_adw

# Mail Info
export DATE_PRINT="`date '+%d-%b-%Y'`"
export MAIL_FROM_NAME="Cost.Report"
export MAIL_FROM_EMAIL="report@oracleemaildelivery.com"
export MAIL_TO="oci.user@oracle.com"
export MAIL_SUBJECT="Cost Usage Report $DATE_PRINT"

# database info
export DATABASE_USER=usage
export DATABASE_PASS=<password>
export DATABASE_NAME=adwcusg_low

# Fixed variables
export DATE=`date '+%Y%m%d_%H%M'`
export REPORT_DIR=${APPDIR}/report/daily
export OUTPUT_FILE=${REPORT_DIR}/daily_${DATE}.txt
mkdir -p ${REPORT_DIR}

##################################
# run report     
##################################
echo "
set pages 0 head off feed off lines 799 trimsp on echo off verify off 
set define @
col line for a1000

prompt   <style>
prompt        td  {font-size:9pt;font-family:arial; text-align:left;}
prompt        th  {font-family: arial, helvetica, sans-serif; font-size: 8pt; font-weight: bold; color: #101010; background-color: #e0e0e0}
prompt        .th1    {font-family: Arial, Helvetica, sans-serif; font-size: 8pt; font-weight: bold; color: #101010; background-color: #d0d0d0}
prompt        .dc1   { font-family: Arial, Helvetica, sans-serif; font-size: 8pt; color: #000000; background-color: white; text-align:left;}
prompt        .dcr   { font-family: Arial, Helvetica, sans-serif; font-size: 8pt; color: #000000; background-color: white; text-align:right;}
prompt        .dcc   { font-family: Arial, Helvetica, sans-serif; font-size: 8pt; color: #000000; background-color: white; text-align:center;}
prompt        .dcbold{ font-family: Arial, Helvetica, sans-serif; font-size: 8pt; color: #000000; background-color: #CCFFCC; text-align:right; font-weight:bold;}
prompt        .tabheader {font-size:12pt; font-family:arial; font-weight:bold; color:purple; text-align:center; background-color: #4fffff}
prompt    </style>

prompt <table border=1 cellpadding=3 cellspacing=0 width=1024 >
prompt     <tr><td colspan=15 class=tabheader>Cost Usage Daily Report - $DATE_PRINT </td></tr>

select
    '<tr>'||
        '<th width=150 nowrap class=th1>Tenant Name</th>'||
        '<th width=80  nowrap class=th1>'||to_char(trunc(sysdate-10),'DD-MON-YYYY')||'</th>'||
        '<th width=80  nowrap class=th1>'||to_char(trunc(sysdate-9),'DD-MON-YYYY')||'</th>'||
        '<th width=80  nowrap class=th1>'||to_char(trunc(sysdate-8),'DD-MON-YYYY')||'</th>'||
        '<th width=80  nowrap class=th1>'||to_char(trunc(sysdate-7),'DD-MON-YYYY')||'</th>'||
        '<th width=80  nowrap class=th1>'||to_char(trunc(sysdate-6),'DD-MON-YYYY')||'</th>'||
        '<th width=80  nowrap class=th1>'||to_char(trunc(sysdate-5),'DD-MON-YYYY')||'</th>'||
        '<th width=80  nowrap class=th1>'||to_char(trunc(sysdate-4),'DD-MON-YYYY')||'</th>'||
        '<th width=80  nowrap class=th1>'||to_char(trunc(sysdate-3),'DD-MON-YYYY')||'</th>'||
        '<th width=80  nowrap class=th1>'||to_char(trunc(sysdate-2),'DD-MON-YYYY')||'</th>'||
        '<th width=80  nowrap class=th1>'||to_char(trunc(sysdate-1),'DD-MON-YYYY')||'</th>'||
        '<th width=80  nowrap class=th1>Month 31 Prediction</th>'||
        '<th width=80  nowrap class=th1>Year Prediction</th>'||
        '<th width=80  nowrap class=th1>Last Load</th>'||
        '<th width=80  nowrap class=th1>Agent Used</th>'||
    '</tr>'
    as line
from dual
union all
select
    '<tr>'||
        '<td nowrap class=dc1> '||tenant_name||'</td> '||
        '<td nowrap class='||day10_class||'> '||to_char(day10,'999,999')||'</td>'||
        '<td nowrap class='||day9_class||'> '||to_char(day9,'999,999')||'</td>'||
        '<td nowrap class='||day8_class||'> '||to_char(day8,'999,999')||'</td>'||
        '<td nowrap class='||day7_class||'> '||to_char(day7,'999,999')||'</td>'||
        '<td nowrap class='||day6_class||'> '||to_char(day6,'999,999')||'</td>'||
        '<td nowrap class='||day5_class||'> '||to_char(day5,'999,999')||'</td>'||
        '<td nowrap class='||day4_class||'> '||to_char(day4,'999,999')||'</td>'||
        '<td nowrap class='||day3_class||'> '||to_char(day3,'999,999')||'</td>'||
        '<td nowrap class='||day2_class||'> '||to_char(day2,'999,999')||'</td>'||
        '<td nowrap class='||day1_class||'> '||to_char(day1,'999,999')||'</td>'||
        '<td nowrap class=dcr> '||to_char(greatest(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10)*31,'999,999,999')||'</td>'||
        '<td nowrap class=dcr> '||to_char(greatest(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10)*365,'999,999,999')||'</td>'||
        '<td nowrap class=dcc> '||to_char(LAST_LOAD,'DD-MON-YYYY HH24:MI')||'</td>'||
        '<td nowrap class=dcc> '||agent||'</td> '||
    '</tr>' as line
from
(
    select
        tenant_name,day1,day2,day3,day4,day5,day6,day7,day8,day9,day10,last_load,agent,
        case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10)) = trunc(day1) then 'dcbold' else 'dcr' END as day1_class,
        case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10)) = trunc(day2) then 'dcbold' else 'dcr' END as day2_class,
        case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10)) = trunc(day3) then 'dcbold' else 'dcr' END as day3_class,
        case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10)) = trunc(day4) then 'dcbold' else 'dcr' END as day4_class,
        case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10)) = trunc(day5) then 'dcbold' else 'dcr' END as day5_class,
        case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10)) = trunc(day6) then 'dcbold' else 'dcr' END as day6_class,
        case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10)) = trunc(day7) then 'dcbold' else 'dcr' END as day7_class,
        case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10)) = trunc(day8) then 'dcbold' else 'dcr' END as day8_class,
        case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10)) = trunc(day9) then 'dcbold' else 'dcr' END as day9_class,
        case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7,day8,day9,day10)) = trunc(day10) then 'dcbold' else 'dcr' END as day10_class
    from
    (
        select 
            tenant_name,
            sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-10) then COST_MY_COST else 0 end) DAY10,
            sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-9 ) then COST_MY_COST else 0 end) DAY9,
            sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-8 ) then COST_MY_COST else 0 end) DAY8,
            sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-7 ) then COST_MY_COST else 0 end) DAY7,
            sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-6 ) then COST_MY_COST else 0 end) DAY6,
            sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-5 ) then COST_MY_COST else 0 end) DAY5,
            sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-4 ) then COST_MY_COST else 0 end) DAY4,
            sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-3 ) then COST_MY_COST else 0 end) DAY3,
            sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-2 ) then COST_MY_COST else 0 end) DAY2,
            sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-1 ) then COST_MY_COST else 0 end) DAY1,
            max(UPDATE_DATE) LAST_LOAD,
            max(agent_version) AGENT
        from oci_cost_stats
        where 
            tenant_name like '%' and
            USAGE_INTERVAL_START >= trunc(sysdate-11)
        group by tenant_name
        order by 1
    )
);
prompt </table>
prompt <br><br>

prompt <table border=1 cellpadding=3 cellspacing=0 width=1024 >
prompt     <tr><td colspan=13 class=tabheader>Cost Usage Monthly Report - $DATE_PRINT </td></tr>

select
    '<tr>'||
        '<th width=150 nowrap class=th1>Tenant Name</th>'||
        '<th width=70  nowrap class=th1>'||to_char(add_months(trunc(sysdate,'MM'),-11),'MON-YYYY')||'</th>'||
        '<th width=70  nowrap class=th1>'||to_char(add_months(trunc(sysdate,'MM'),-10),'MON-YYYY')||'</th>'||
        '<th width=70  nowrap class=th1>'||to_char(add_months(trunc(sysdate,'MM'), -9),'MON-YYYY')||'</th>'||
        '<th width=70  nowrap class=th1>'||to_char(add_months(trunc(sysdate,'MM'), -8),'MON-YYYY')||'</th>'||
        '<th width=70  nowrap class=th1>'||to_char(add_months(trunc(sysdate,'MM'), -7),'MON-YYYY')||'</th>'||
        '<th width=70  nowrap class=th1>'||to_char(add_months(trunc(sysdate,'MM'), -6),'MON-YYYY')||'</th>'||
        '<th width=70  nowrap class=th1>'||to_char(add_months(trunc(sysdate,'MM'), -5),'MON-YYYY')||'</th>'||
        '<th width=70  nowrap class=th1>'||to_char(add_months(trunc(sysdate,'MM'), -4),'MON-YYYY')||'</th>'||
        '<th width=70  nowrap class=th1>'||to_char(add_months(trunc(sysdate,'MM'), -3),'MON-YYYY')||'</th>'||
        '<th width=70  nowrap class=th1>'||to_char(add_months(trunc(sysdate,'MM'), -2),'MON-YYYY')||'</th>'||
        '<th width=70  nowrap class=th1>'||to_char(add_months(trunc(sysdate,'MM'), -1),'MON-YYYY')||'</th>'||
        '<th width=70  nowrap class=th1>'||to_char(           trunc(sysdate,'MM')    ,'MON-YYYY')||'</th>'||
    '</tr>'
    as line
from dual
union all
select
    '<tr>'||
        '<td nowrap class=dc1> '||tenant_name||'</td> '||
        '<td nowrap class='||m12_class||'> '||to_char(m12,'999,999,999')||'</td>'||
        '<td nowrap class='||m11_class||'> '||to_char(m11,'999,999,999')||'</td>'||
        '<td nowrap class='||m10_class||'> '||to_char(m10,'999,999,999')||'</td>'||
        '<td nowrap class='|| m9_class||'> '||to_char( m9,'999,999,999')||'</td>'||
        '<td nowrap class='|| m8_class||'> '||to_char( m8,'999,999,999')||'</td>'||
        '<td nowrap class='|| m7_class||'> '||to_char( m7,'999,999,999')||'</td>'||
        '<td nowrap class='|| m6_class||'> '||to_char( m6,'999,999,999')||'</td>'||
        '<td nowrap class='|| m5_class||'> '||to_char( m5,'999,999,999')||'</td>'||
        '<td nowrap class='|| m4_class||'> '||to_char( m4,'999,999,999')||'</td>'||
        '<td nowrap class='|| m3_class||'> '||to_char( m3,'999,999,999')||'</td>'||
        '<td nowrap class='|| m2_class||'> '||to_char( m2,'999,999,999')||'</td>'||
        '<td nowrap class='|| m1_class||'> '||to_char( m1,'999,999,999')||'</td>'||
    '</tr>' as line
from
(
    select
        tenant_name,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,
        case when trunc(greatest(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)) = trunc(m1)  then 'dcbold' else 'dcr' END as m1_class,
        case when trunc(greatest(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)) = trunc(m2)  then 'dcbold' else 'dcr' END as m2_class,
        case when trunc(greatest(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)) = trunc(m3)  then 'dcbold' else 'dcr' END as m3_class,
        case when trunc(greatest(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)) = trunc(m4)  then 'dcbold' else 'dcr' END as m4_class,
        case when trunc(greatest(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)) = trunc(m5)  then 'dcbold' else 'dcr' END as m5_class,
        case when trunc(greatest(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)) = trunc(m6)  then 'dcbold' else 'dcr' END as m6_class,
        case when trunc(greatest(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)) = trunc(m7)  then 'dcbold' else 'dcr' END as m7_class,
        case when trunc(greatest(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)) = trunc(m8)  then 'dcbold' else 'dcr' END as m8_class,
        case when trunc(greatest(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)) = trunc(m9)  then 'dcbold' else 'dcr' END as m9_class,
        case when trunc(greatest(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)) = trunc(m10) then 'dcbold' else 'dcr' END as m10_class,
        case when trunc(greatest(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)) = trunc(m11) then 'dcbold' else 'dcr' END as m11_class,
        case when trunc(greatest(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)) = trunc(m12) then 'dcbold' else 'dcr' END as m12_class
    from
    (
        select 
            tenant_name,
            sum(case when trunc(USAGE_INTERVAL_START,'MM') = add_months(trunc(sysdate,'MM'),-11) then COST_MY_COST else 0 end) M12,
            sum(case when trunc(USAGE_INTERVAL_START,'MM') = add_months(trunc(sysdate,'MM'),-10) then COST_MY_COST else 0 end) M11,
            sum(case when trunc(USAGE_INTERVAL_START,'MM') = add_months(trunc(sysdate,'MM'), -9) then COST_MY_COST else 0 end) M10,
            sum(case when trunc(USAGE_INTERVAL_START,'MM') = add_months(trunc(sysdate,'MM'), -8) then COST_MY_COST else 0 end) M9,
            sum(case when trunc(USAGE_INTERVAL_START,'MM') = add_months(trunc(sysdate,'MM'), -7) then COST_MY_COST else 0 end) M8,
            sum(case when trunc(USAGE_INTERVAL_START,'MM') = add_months(trunc(sysdate,'MM'), -6) then COST_MY_COST else 0 end) M7,
            sum(case when trunc(USAGE_INTERVAL_START,'MM') = add_months(trunc(sysdate,'MM'), -5) then COST_MY_COST else 0 end) M6,
            sum(case when trunc(USAGE_INTERVAL_START,'MM') = add_months(trunc(sysdate,'MM'), -4) then COST_MY_COST else 0 end) M5,
            sum(case when trunc(USAGE_INTERVAL_START,'MM') = add_months(trunc(sysdate,'MM'), -3) then COST_MY_COST else 0 end) M4,
            sum(case when trunc(USAGE_INTERVAL_START,'MM') = add_months(trunc(sysdate,'MM'), -2) then COST_MY_COST else 0 end) M3,
            sum(case when trunc(USAGE_INTERVAL_START,'MM') = add_months(trunc(sysdate,'MM'), -1) then COST_MY_COST else 0 end) M2,
            sum(case when trunc(USAGE_INTERVAL_START,'MM') =            trunc(sysdate,'MM')      then COST_MY_COST else 0 end) M1
        from oci_cost_stats
        where 
            tenant_name like '%'
        group by tenant_name
        order by 1
    )
);
prompt </table>

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

echo ""
echo "Sending e-mail to $MAIL_TO ..."

####################
# Sending e-mail
####################
cat <<-eomail | /usr/sbin/sendmail -f "$MAIL_FROM_EMAIL" -F "$MAIL_FROM_NAME" -t
To: $MAIL_TO
Subject: $MAIL_SUBJECT
Content-Type: text/html
`cat $OUTPUT_FILE`
eomail
