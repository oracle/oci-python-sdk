-- Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
-- This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

---------------------------------------------------------------------
-- Current State - CPU per Service
---------------------------------------------------------------------
with last_date as
(
    select distinct USAGE_INTERVAL_START
    from 
    (
        select USAGE_INTERVAL_START, dense_rank() over (partition by null order by USAGE_INTERVAL_START desc) rn 
        from oci_usage 
        where 
			-- tenant_name=:PARAM_TENANT_NAME and 
			USAGE_INTERVAL_START >= sysdate-14
    ) where rn=2 
)
select 
    to_char(usage_interval_start,'DD-MON-YYYY HH24:MI') DATE_TIME,
    prd_service, 
    sum(
        case when USG_CONSUMED_UNITS like '%MS%' 
        then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000
        else USG_BILLED_QUANTITY
        end 
    ) as USG_BILLED_QUANTITY
from oci_usage
where 
    -- tenant_name = :PARAM_TENANT_NAME and
    -- prd_compartment_name = :PARAM_COMPARTMENT_NAME and
    -- prd_compartment_path like :PARAM_COMPARTMENT_TOP ||'%' and
    -- prd_service = :PARAM_PRODUCT_SERVICE and
    -- prd_region = :PARAM_PRODUCT_REGION and
    USAGE_INTERVAL_START = (select USAGE_INTERVAL_START from last_date) and
    USG_BILLED_QUANTITY>0 and
    USG_CONSUMED_MEASURE='OCPUS'
group by 
    prd_service, to_char(usage_interval_start,'DD-MON-YYYY HH24:MI')
order by 3 desc;

---------------------------------------------------------------------
-- Current State - CPU per Service
---------------------------------------------------------------------
with last_date as
(
    select distinct USAGE_INTERVAL_START
    from 
    (
        select USAGE_INTERVAL_START, dense_rank() over (partition by null order by USAGE_INTERVAL_START desc) rn 
        from oci_usage 
        where 
			-- tenant_name=:PARAM_TENANT_NAME and 
			USAGE_INTERVAL_START >= sysdate-14
    ) where rn=2 
)
select 
    to_char(usage_interval_start,'DD-MON-YYYY HH24:MI') DATE_TIME,
    prd_service,
    round(sum(
        case 
            when USG_CONSUMED_UNITS = 'KB' then USG_BILLED_QUANTITY/1000/1000/1000
            when USG_CONSUMED_UNITS = 'MB' then USG_BILLED_QUANTITY/1000/1000
            when USG_CONSUMED_UNITS = 'GB' then USG_BILLED_QUANTITY/1000
            when USG_CONSUMED_UNITS = 'TB' then USG_BILLED_QUANTITY
        end
    ),2) as USG_BILLED_QUANTITY
from 
(
    select
        usage_interval_start,
        prd_service, 
        sum(
            case when USG_CONSUMED_UNITS like '%MS%' 
            then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000
            else USG_BILLED_QUANTITY
            end 
        ) as USG_BILLED_QUANTITY,
        case when USG_CONSUMED_UNITS like '%MS%' 
            then replace(replace(USG_CONSUMED_UNITS,'MS',''),'_','')
            else USG_CONSUMED_UNITS
        end as USG_CONSUMED_UNITS
    from oci_usage
    where 
        -- tenant_name = :PARAM_TENANT_NAME and
        -- prd_compartment_name = :PARAM_COMPARTMENT_NAME and
        -- prd_compartment_path like :PARAM_COMPARTMENT_TOP ||'%' and
        -- prd_service = :PARAM_PRODUCT_SERVICE and
        -- prd_region = :PARAM_PRODUCT_REGION and
        USAGE_INTERVAL_START = (select USAGE_INTERVAL_START from last_date) and
        USG_BILLED_QUANTITY>0 and
        USG_CONSUMED_MEASURE='STORAGE_SIZE'
    group by 
        prd_service,
        USG_CONSUMED_UNITS,
        usage_interval_start
)
group by prd_service, to_char(usage_interval_start,'DD-MON-YYYY HH24:MI')
order by 3 desc;

---------------------------------------------------------------------
-- Current State - Chart per Compartment
---------------------------------------------------------------------
with last_date as
(
    select distinct USAGE_INTERVAL_START
    from 
    (
        select USAGE_INTERVAL_START, dense_rank() over (partition by null order by USAGE_INTERVAL_START desc) rn 
        from oci_usage 
        where 
			-- tenant_name=:PARAM_TENANT_NAME and 
			USAGE_INTERVAL_START >= sysdate-14
    ) where rn=2 
)
select 
    to_char(usage_interval_start,'DD-MON-YYYY HH24:MI') DATE_TIME,
    prd_compartment_name,
    prd_service, 
    sum(
        case when USG_CONSUMED_UNITS like '%MS%' 
        then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000
        else USG_BILLED_QUANTITY
        end 
    ) as USG_BILLED_QUANTITY
from 
	oci_usage
where 
    -- tenant_name = :PARAM_TENANT_NAME and
    -- prd_compartment_name = :PARAM_COMPARTMENT_NAME and
    -- prd_compartment_path like :PARAM_COMPARTMENT_TOP ||'%' and
    -- prd_service = :PARAM_PRODUCT_SERVICE and
    -- prd_region = :PARAM_PRODUCT_REGION and
    USAGE_INTERVAL_START = (select USAGE_INTERVAL_START from last_date) and
    USG_BILLED_QUANTITY>0 and
    USG_CONSUMED_MEASURE='OCPUS'
group by 
    prd_compartment_name, prd_service, to_char(usage_interval_start,'DD-MON-YYYY HH24:MI')
order by 4 desc;

---------------------------------------------------------------------
-- Current State - Storage Per Service in TB
---------------------------------------------------------------------
with last_date as
(
    select distinct USAGE_INTERVAL_START
    from 
    (
        select USAGE_INTERVAL_START, dense_rank() over (partition by null order by USAGE_INTERVAL_START desc) rn 
        from oci_usage 
        where 
			-- tenant_name=:PARAM_TENANT_NAME and 
			USAGE_INTERVAL_START >= sysdate-14
    ) where rn=2 
)
select 
    to_char(usage_interval_start,'DD-MON-YYYY HH24:MI') DATE_TIME,
    prd_compartment_name,
    prd_service,
    round(sum(
        case 
            when USG_CONSUMED_UNITS = 'KB' then USG_BILLED_QUANTITY/1000/1000/1000
            when USG_CONSUMED_UNITS = 'MB' then USG_BILLED_QUANTITY/1000/1000
            when USG_CONSUMED_UNITS = 'GB' then USG_BILLED_QUANTITY/1000
            when USG_CONSUMED_UNITS = 'TB' then USG_BILLED_QUANTITY
        end
    ),2) as USG_BILLED_QUANTITY
from 
(
    select 
        prd_compartment_name,
        prd_service, 
        usage_interval_start,
        sum(
            case when USG_CONSUMED_UNITS like '%MS%' 
            then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000
            else USG_BILLED_QUANTITY
            end 
        ) as USG_BILLED_QUANTITY,
        case when USG_CONSUMED_UNITS like '%MS%' 
            then replace(replace(USG_CONSUMED_UNITS,'MS',''),'_','')
            else USG_CONSUMED_UNITS
        end as USG_CONSUMED_UNITS
    from 
		oci_usage
    where 
        -- tenant_name = :PARAM_TENANT_NAME and
        -- prd_compartment_name = :PARAM_COMPARTMENT_NAME and
        -- prd_compartment_path like :PARAM_COMPARTMENT_TOP ||'%' and
        -- prd_service = :PARAM_PRODUCT_SERVICE and
        -- prd_region = :PARAM_PRODUCT_REGION and
        USAGE_INTERVAL_START = (select USAGE_INTERVAL_START from last_date) and
        USG_BILLED_QUANTITY>0 and
        USG_CONSUMED_MEASURE='STORAGE_SIZE'
    group by 
        prd_compartment_name,
        prd_service,
        USG_CONSUMED_UNITS,
        usage_interval_start
)
group by prd_compartment_name, prd_service, to_char(usage_interval_start,'DD-MON-YYYY HH24:MI')
order by 4 desc

---------------------------------------------------------------------
-- Current State - list
---------------------------------------------------------------------
with last_date as
(
    select distinct USAGE_INTERVAL_START
    from 
    (
        select USAGE_INTERVAL_START, dense_rank() over (partition by null order by USAGE_INTERVAL_START desc) rn 
        from oci_usage 
        where 
			-- tenant_name=:PARAM_TENANT_NAME and 
			USAGE_INTERVAL_START >= sysdate-14
    ) where rn=2 
)
select 
    to_char(usage_interval_start,'DD-MON-YYYY HH24:MI') DATE_TIME,
    prd_compartment_path, 
    prd_compartment_name, 
    prd_region, 
    prd_service, 
    prd_resource,
    USAGE_INTERVAL_START,
    USAGE_INTERVAL_END,
    sum(
        case when USG_CONSUMED_UNITS like '%MS%' 
        then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000
        else USG_BILLED_QUANTITY
        end 
    ) as USG_BILLED_QUANTITY,
    case when USG_CONSUMED_UNITS like '%MS%' 
        then replace(replace(USG_CONSUMED_UNITS,'MS',''),'_','')
        else USG_CONSUMED_UNITS
    end as USG_CONSUMED_UNITS, 
    USG_CONSUMED_MEASURE
from 
	oci_usage
where 
    -- tenant_name = :PARAM_TENANT_NAME and
    -- prd_compartment_name = :PARAM_COMPARTMENT_NAME and
    -- prd_compartment_path like :PARAM_COMPARTMENT_TOP ||'%' and
    -- prd_service = :PARAM_PRODUCT_SERVICE and
    -- prd_region = :PARAM_PRODUCT_REGION and
    USAGE_INTERVAL_START = (select USAGE_INTERVAL_START from last_date) and
    USG_BILLED_QUANTITY>0
group by 
    prd_compartment_path, 
    prd_compartment_name, 
    prd_region, 
    prd_service, 
    prd_resource, 
    USG_CONSUMED_UNITS, 
    USG_CONSUMED_MEASURE,
    USAGE_INTERVAL_START,
    USAGE_INTERVAL_END
order by 1,2,3,4,5


---------------------------------------------------------------------
-- CPUs over time
---------------------------------------------------------------------

select 
    to_char(USAGE_INTERVAL_START,'YYYY-MM-DD HH24:MI') USAGE_INTERVAL_START,
    prd_service, 
    sum(
        case when USG_CONSUMED_UNITS like '%MS%' 
        then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000
        else USG_BILLED_QUANTITY
        end 
    ) as USG_BILLED_QUANTITY
from 
	oci_usage
where 
    -- tenant_name=:PARAM_TENANT and
    -- prd_compartment_name = :PARAM_COMPARTMENT_NAME and
    -- prd_compartment_path like :PARAM_COMPARTMENT_TOP ||'%') and
    -- prd_service = :PARAM_PRODUCT_SERVICE and
    -- prd_region = :PARAM_PRODUCT_REGION and
    USAGE_INTERVAL_START >= add_months(sysdate,0-12) and
    USG_BILLED_QUANTITY>0 and
    USG_CONSUMED_MEASURE='OCPUS'
group by 
    to_char(USAGE_INTERVAL_START,'YYYY-MM-DD HH24:MI'),
    prd_service
order by 2 desc;

---------------------------------------------------------------------
-- Usage over Time 
---------------------------------------------------------------------
select 
    USAGE_INTERVAL_START,
    prd_service,
    round(sum(
        case 
            when USG_CONSUMED_UNITS = 'KB' then USG_BILLED_QUANTITY/1000/1000/1000
            when USG_CONSUMED_UNITS = 'MB' then USG_BILLED_QUANTITY/1000/1000
            when USG_CONSUMED_UNITS = 'GB' then USG_BILLED_QUANTITY/1000
            when USG_CONSUMED_UNITS = 'TB' then USG_BILLED_QUANTITY
        end
    ),2) as USG_BILLED_QUANTITY
from 
(
    select 
        to_char(USAGE_INTERVAL_START,'YYYY-MM-DD HH24:MI') USAGE_INTERVAL_START,
        prd_service, 
        sum(
            case when USG_CONSUMED_UNITS like '%MS%' 
            then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000
            else USG_BILLED_QUANTITY
            end 
        ) as USG_BILLED_QUANTITY,
        case when USG_CONSUMED_UNITS like '%MS%' 
            then replace(replace(USG_CONSUMED_UNITS,'MS',''),'_','')
            else USG_CONSUMED_UNITS
        end as USG_CONSUMED_UNITS
    from oci_usage
    where 
        -- tenant_name=:PARAM_TENANT and
        -- prd_compartment_name = :PARAM_COMPARTMENT_NAME and
        -- prd_compartment_path like :PARAM_COMPARTMENT_TOP ||'%') and
        -- prd_service = :PARAM_PRODUCT_SERVICE and
        -- prd_region = :PARAM_PRODUCT_REGION and
        USAGE_INTERVAL_START >= add_months(sysdate,0-12) and
        USG_BILLED_QUANTITY>0 and
        USG_CONSUMED_MEASURE='STORAGE_SIZE'
    group by 
        to_char(USAGE_INTERVAL_START,'YYYY-MM-DD HH24:MI'),
        prd_service,
        USG_CONSUMED_UNITS
)
group by USAGE_INTERVAL_START,prd_service order by 1,2 desc;
