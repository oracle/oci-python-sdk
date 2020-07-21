Change Log
~~~~~~~~~~
All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_.

=====================
20.07.21 - 2020-07-21
=====================
* Added Full + Parallel scan when retrieving max cost and usage file

=====================
20.07.14 - 2020-07-14
=====================
* Support for Cost column changed - OCI amend the column billingUnitReadable to skuUnitDescription
* Added daily report script with step by step configuration - requires OCI Email setup
* Fixed bug on Apex related to the column change for Cost Report

=====================
20.07.07 - 2020-07-07
=====================
* Added flags to skip usage or skip cost with -sc and -su
* Added buffer size and array size for database multi insert to avoid large transaction failing

=====================
20.06.02 - 2020-06-02
=====================
* Added Hourly cost over time

=====================
20.06.02 - 2020-06-02
=====================
* Added Summary cost per day to the Data Statistics - if you manage many tenants, it is a great view to see them all
* Added Cost by SKU to the Cost Over Time - Daily/Weekly and Monthly

=====================
20.05.18 - 2020-05-18
=====================
* Added Rate Card with OCI_PRICE_LIST and using API to obtain info, Thanks to Fabio for the Idea and the API
* Added discount and public rate to the cost report

=====================
20.05.11 - 2020-05-11
=====================
* Added performance improvements to Cost by adding index OCI_COST_1IX and reference table OCI_COST_REFERENCE
* Added Graph Report Selector to the Cost pages
* Added accumulative Chart to Cost
* Added Manual Descriptions for products that don't have.
* Added More Charts to Cost Over Time
* Added More Charts to Cost Analysis

=====================
20.05.04 - 2020-05-04
=====================
* Added connectivity to the home region where bling bucket exist
* Added performance improvements by adding stats tables OCI_USAGE_STATS and OCI_COST_STATS and indexes OCI_USAGE_1IX, OCI_COST_1IX,
  Please run the load script before importing the APEX app in order to create those tables and index

=====================
20.04.27 - 2020-04-27
=====================
* Added limit, prefix and start to the list_object call
* Added support for special chars
* Added Currency Code to the pages
* Added checks if columns exist in the file to avoid failure
* Added Support for null overage
* Align code to use functions properly

=====================
20.04.20 - 2020-04-20
=====================
* Added table OCI_USAGE_TAG_KEYS for tags
* Added table OCI_COST and OCI_COST_TAG_KEYS for cost usage
* Added support for cost files
* Added Cost Analysis and Cost Overview to the APEX App

=====================
20.04.13 - 2020-04-13
=====================
* Added support for tags - TAGS_DATA columns to the table OCI_USAGE
* Added step by step installation guide for instant principles
* Added APEX Application to query the data

=====================
20.02.01 - 2020-02-01
=====================
* Initial Release
