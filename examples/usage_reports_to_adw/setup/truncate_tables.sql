set echo on time on timing on
spool truncate_tables.log

prompt Truncating usage2adw Application Tables
prompt Version 2022/8/12

select to_char(sysdate,'YYYY-MM-DD HH24:MI') current_date from dual;

truncate table usage.OCI_USAGE ;
truncate table usage.OCI_USAGE_STATS ;
truncate table usage.OCI_USAGE_TAG_KEYS ;
truncate table usage.OCI_COST;
truncate table usage.OCI_COST_STATS;
truncate table usage.OCI_COST_TAG_KEYS ;
truncate table usage.OCI_COST_REFERENCE;
truncate table usage.OCI_PRICE_LIST;

spool off
