set echo on time on timing on
spool drop_tables.log

prompt Dropping  usage2adw Application Tables
prompt Version 2022/8/12

select to_char(sysdate,'YYYY-MM-DD HH24:MI') current_date from dual;

drop table usage.OCI_USAGE ;
drop table usage.OCI_USAGE_STATS ;
drop table usage.OCI_USAGE_TAG_KEYS ;
drop table usage.OCI_COST;
drop table usage.OCI_COST_STATS;
drop table usage.OCI_COST_TAG_KEYS ;
drop table usage.OCI_COST_REFERENCE;
drop table usage.OCI_PRICE_LIST;

spool off
