Change Log
~~~~~~~~~~
All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_.

=====================
25.08.26 - 25.08.26
=====================
* Added security_groups_ids to compute csv
* Added additional parameters for OIC

25.07.15 - 25.07.15
=====================
* Full Stack DR added

=====================
25.06.17 - 25.06.17
=====================
* Added tags for network-security-groups in the csv

=====================
25.05.06 - 25.05.06
=====================
* Moved NSG processing dependencies
* Added Retry to IAM Domain Search
* Fix small bugs
* Fixed IAM Domains IDP Jit
* Added exclude for Bastion, CloudGuard and Logging

=====================
25.04.29 - 25.04.29
=====================
* Added GenAI and GenAI Agents for the enabled regions

=====================
25.04.08 - 25.04.08
=====================
* Added compute additional parameters to the csv

=====================
25.03.18 - 25.03.18
=====================
* Added route table to VNICs

=====================
25.02.10 - 25.02.10
=====================
* Added announcement details including resources for active announcements
* Added CSV for IAM Dynamic Groups (for the -iold flag)

=====================
25.01.13 - 25.01.13
=====================
* Added Cloud Advisor Recommendations - run on root compartment only

=====================
24.12.17 - 24.12.17
=====================
* Change database backup size to source database size
* Added Licensing type for instance

=====================
24.12.10 - 24.12.10
=====================
* Added Vnic information
* Added retry_strategy to vnic call
* Improve the code

=====================
24.11.26 - 24.11.26
=====================
* Added few more variables to databases and fixed the autobck flag

=====================
24.11.12 - 24.11.12
=====================
* Added unique id to Vault CSVs

=====================
24.08.27 - 24.08.27
=====================
* Added support for Exascale databases

=====================
24.08.20 - 24.08.20
=====================
* Added memory for db_system for flex shapes

=====================
24.08.06 - 24.08.06
=====================
* subscription id attribute in Cloud Exadata Infrastructure and Cloud VM Clusters in the Database service and additional parameters

=====================
24.07.09 - 24.07.09
=====================
* Added IAM network sources to the CSV
* Added Tag Namespaces to the CSV
* Added IAM Domains group mapping to csv using old API, flag -iold required
* Added IAM Domains network perimeters

=====================
24.07.02 - 24.07.02
=====================
* Added IAM Domains Policies, Rules and Conditions

=====================
24.06.11 - 24.06.11
=====================
* Added security list and network security group details to the CSVs

=====================
24.06.04 - 24.06.04
=====================
* Added Subnet Name and VCN Name to the DB Base and ExaCS VM Cluster CSVs
* Align the description and security alert in the network security rules and security list.

=====================
24.05.28 - 24.05.28
=====================
* Added logs for IPSEC and Virtual Cirtcuits

=====================
24.05.24 - 24.05.24
=====================
* IAM Domains - Change way members fetched for groups to avoid limit of 10,000 members in one call
* Added option to filter IAM Domain name using ifilter, allowed comma seperated
* Fix ExaCC CSV Extract bug

=====================
24.05.17 - 24.05.17
=====================
* Added pdb csvs
* Added function csvs - functions_apps and functions_fns

=====================
24.04.23 - 24.04.23
=====================
* Added flag -iold to extract identity with old APIs
* Added error handling for domains

=====================
24.04.16 - 24.04.16
=====================
* Added more details to DBNode of database areas

=====================
24.04.09 - 24.04.09
=====================
* Exclude GENAI until the service deployed on all regions to avoid process hung

=====================
24.04.02 - 24.04.02
=====================
* Added is_symmetric_hash_enabled flag for network load balancers

=====================
24.04.02 - 24.04.02
=====================
* Added support for IAM Domains across different compartments

=====================
24.03.19 - 24.03.19
=====================
* Added -excludelist to generate exclude filter flags
* Added certificates, certificate authorities, certificate ca bundle which are part of -sec
* Added Data Safe information including assessments (use -dsa for report), assessments extract to JSON or CSV
* Added description for network security rules and security groups

=====================
24.03.12 - 24.03.12
=====================
* Added exclude for GENAI and OCE
* Factor Client Creation for rest of services

=====================
24.03.03 - 24.03.03
=====================
* Remove max_cpu_core_count from Autonomous Database

=====================
24.03.02 - 24.03.02
=====================
* Added CSV Resources with all resources
* Added Error array to Output CSV
* Factor client creation

=====================
24.02.20 - 24.02.20
=====================
* Added additional parameters to Boot and Block Volumes

=====================
24.02.06 - 24.02.06
=====================
* Added Gen AI
* Fixed cores count for RAC Base database

=====================
23.12.20 - 23.12.20
=====================
* Added CSV for Announcements
* Added -andays flag to extract last XX Days of announcement, default 30
* Amend error control on showoci_service.py
* Added errors csv for service and processing errors and warnings

=====================
23.12.12 - 23.12.12
=====================
* Added PostgreSQL
* Added MYSQL Backups
* Fixed support for OCVS VMWare clusters

=====================
23.12.05 - 23.12.05
=====================
* Remove space from Compute CSV which produce empty column

=====================
23.11.28 - 23.11.28
=====================
* Simmplify the Identity Domains User Extract

=====================
23.10.31 - 23.10.31
=====================
* Added additional information to Big Data Cloud Service
* Extract FAILED status as well.

=====================
23.10.24 - 23.10.24
=====================
* Fix bug with instance configuration and object storage csv

=====================
23.10.17 - 23.10.17
=====================
* Fix bug with resource principle authentication

=====================
23.09.26 - 23.09.26
=====================
* Added network load balancers to the CSV

=====================
23.09.19 - 23.09.19
=====================
* Added resource principle authentication with -rp
* Added log unified agents configuration

=====================
23.09.05 - 23.09.05
=====================
* Added Autonomous database ECPU
* emptied vcn_cidr in csv files, vcn_cidrs should be used

=====================
23.08.15 - 23.08.15
=====================
* Performance improvments using Thread enabled
* Migrating the application to parallel execution using Threads
* Added -noparallel to run serial and -threads for thread numbers
* Combined PaaS Native and Data and AI to one group - Native Data and AI
* Combined Monitoring, Security and Limits to one group
* Combined OKE clusters with Compute
* Combined Load Balanacers and Network to one group
* Combined File Storage and Object Storage to one group
* Added OKE Container Summary
* Added NETWORK,LIMITS,QUOTAS,DNSZONE,VCIRCUITS to the -exclude

=====================
23.07.26 - 23.07.26
=====================
* Added support for identity domain password policies, can be skipped using -isc flag
* Added more information to database service (vault_id) and other areas

=====================
23.07.19 - 23.07.19
=====================
* Added additional attributes for compute csv extract
* reform output of False and True and None 50% completed (up to line 7500)

=====================
23.07.04 - 23.07.04
=====================
* Added flag -exclude with options to exclude Services currently support - NETWORK 

=====================
23.06.06 - 23.06.06
=====================
* Added Load Balancer Cipher Suites and Routing Policies
* fix breaking file system list snapshots

=====================
23.05.23 - 23.05.23
=====================
* Added Instance Parameters - Burstable, Launch options and more
* Removed Data Connectivity per SDK breaking

=====================
23.05.02 - 23.05.02
=====================
* Added live migration flag to compute

=====================
23.04.18 - 23.04.18
=====================
* Removed pause to avoid false positive in security scan

=====================
23.04.11 - 23.04.11
=====================
* Amend scripts and help to point to OCI Python SDK sites

=====================
23.03.28 - 23.03.28
=====================
* Added OCI_RESOURCES table to showoci2adw to load all relevants OCIDs
* Added Identity to summary
* Added Goldengate deployment to CSV
* Added NoSQL to CSV
* Added Network Firewall + Policies
* Added more mysql info + added to CSV
* Added Cloud Guard Recipes
* Added option to filter by region - comma seperated
* Added option to filter "Not" by region with -rgn
* Added Open Search Clusters

=====================
23.03.21 - 23.03.21
=====================
* Added Identity Domains including Users, Groups, IDPs, DynGroups, Auth Setting, KMSI Setting

=====================
23.03.14 - 23.03.14
=====================
* Added more info for OKE, APIGW, Databases for JSON and CSV
* Added DevOps and WAF
* Added Quotas to CSV

=====================
23.03.07 - 23.03.07
=====================
* Added Tags to file storage and object storage CSVs

=====================
23.02.28 - 23.02.28
=====================
* Add Information on README.md

=====================
23.02.21 - 23.02.21
=====================
* Added function for lifecycle_state active

=====================
23.02.14 - 23.02.14
=====================
* Added database standalone backups
* Added tenant_name and tenant_id (6 last letters) to CSVs

=====================
23.02.07 - 23.02.07
=====================
* Added version check of showoci classes
* Added Queues
* Added CSV for Streams and Queues
* Fix ADB-D extract on ExaCS and ExaCC
* Convert Tags to Columns in CSV output unless -csv_notagstocols specified

=====================
23.01.31 - 23.01.31
=====================
* Added flag -skipdbhomes to skip database homes and databases
* Added flag -readtimeout and -conntimeout for read and connection timeout, default=(20,150)
* Added Autonomous Dedicated to the CSV file.

=====================
23.01.10 - 23.01.10
=====================
* Added ExaCS DB Servers

=====================
22.12.06 - 22.12.06
=====================
* Added Data Connection Registry

=====================
22.11.15 - 22.11.15
=====================
* Added privte ip addresses to subnet - json and csv

=====================
22.10.18 - 22.10.18
=====================
* Added csv for Monitoring: agents, events, alarm, db management and Notifications
* Added Event Actions
* Added application functions
* Added auto backup flag in database.csv

=====================
22.10.11 - 22.10.11
=====================
* Added boot and volume intransit encryption
* Added logs for subnets

=====================
22.10.04 - 22.10.04
=====================
* Added Compute Instance Plugin Status to the JSON output and CSV

=====================
22.09.20 - 22.09.20
=====================
* Removed list_identity_providers which deprecated from OCI SDK
* Removed list_idp_group_mappings which deprecated from OCI SDK

=====================
22.08.16 - 22.08.16
=====================
* Fix block volume list for oci 2.78.0 breaking

=====================
22.07.26 - 22.07.26
=====================
* Added Certificates indicator to load balancer

=====================
22.06.21 - 22.06.21
=====================
* Added dbservers id to exadata csv

=====================
22.05.31 - 22.05.31
=====================
* Added Compartment Path to every api and csv
* Added Visual Builder
* Added csvcol to extract defined tag to csv columns

=====================
22.05.24 - 22.05.24
=====================
* Added Shape Capacity to Reservation CSV

=====================
22.05.10 - 22.05.10
=====================
* Added CSV of Exa Infrastructure

=====================
22.03.29 - 22.03.29
=====================
* Added CSV of IPSEC Tunnels
* Added CSV of Virtual Circuits

=====================
22.03.22 - 22.03.22
=====================
* Added Security Token with -is
* Added DB Servers for ExaCC

=====================
22.03.15 - 22.03.15
=====================
* Added KMS Vaults
* Added Data Integration Workspaces
* Added gi_version_date and system_version_date based on gi and system versions

=====================
22.03.08 - 22.03.08
=====================
* Added CSV for Block Volume Backups and Boot Volumes Backups
* Added Volume Group Backup
* Added Database PDBs

=====================
22.02.22 - 22.02.22
=====================
* Added Support for ExaCS and ExaCC VMclusters in different compartment
* Added CSV for PaaS OAC
* Added CSV for PaaS OIC
* Added CSV for PaaS OCVS
* Added CSV for PaaS OCE
* Added CSV for PaaS Data Science
* Added CSV for PaaS Data Flow
* Added CSV for PaaS Data Catalog
* Added CSV for Big Data Service
* Added CSV for Digital Assistance

=====================
22.02.08 - 22.02.08
=====================
* Added estimate dates for exadata maintenance
* Added system version to the db system / exadata csv
* Split database_db_system csv to database_db_all, database_db_vm_bm, database_db_exacs, database_db_exacc
* Added csv for network drg

=====================
22.02.01 - 22.02.01
=====================
* Added CSV for Object storage buckets
* Added CSV for Security Bastions
* Added CSV for Security Logging
* Added CSV for Security Cloud Guard
* Added CSV for Containers Kubernetes
* Added CSV for Edge Waas Policies
* Added CSV for Edge DNS Steering Policies
* Added CSV for Edge Healthchecks

=====================
22.01.18 - 22.01.18
=====================
* Added database home patch history

=====================
22.01.11 - 22.01.11
=====================
* Fixed database connection for ADB
* Added database edition and license model to the CSV extract
* Added APIGW and Deployment + added to the CSV

=====================
21.11.16 - 21.11.16
=====================
* Added Compute Capacity Reservation
* Added Exadata Cloud at Customer

=====================
21.11.02 - 21.11.02
=====================
* Added local user last login to CSV

=====================
21.10.19 - 21.10.19
=====================
* Added logs to load balancer
* Added logs to compute instances
* Added logs to Object Storage
* Added additional attributes to object storage

=====================
21.10.12 - 21.10.12
=====================
* Database Home patch level to the csv

=====================
21.10.05 - 21.10.05
=====================
* Added Bastions
* Added OAC Vanity URL

=====================
21.08.31 - 21.08.31
=====================
* Added CSV for database backups
* Added Autonomous Database DG and extra properties

=====================
21.06.29 - 21.06.29
=====================
* Added DRG Route Tables for DRGV2
* Added Additional database attributes

=====================
21.06.02 - 21.06.02
=====================
* Support for New DRG
* Added Management Agent
* Added Database Management
* Added External Databases - CDB/PDB and NonPDB

=====================
21.05.25 - 21.05.25
=====================
* Added Autonomous Dedicated

=====================
21.05.11 - 21.05.11
=====================
* Added DNS Resolver, endpoints and rules to VCNs
* Added Flex OCPUS to summary Shapes
* Fixed Stopped OCPUs for VM/BM DB if node is stopped
* Added Windows OCPUs to the summary
* Remove vcn_id requirement from list_vlans
* Added Security Scores under -sec

=====================
21.04.20 - 21.04.20
=====================
* Remove ipv6 from vcn (Breaking)
* Added peername to LPG

=====================
21.03.30 - 21.03.30
=====================
* Added Network load Balancer
* Amended Announcement to show all announcements.

=====================
21.03.23 - 21.03.23
=====================
* Added Golden Gate Service to the database area
* Added network_endpoint_details for OAC

=====================
21.03.09 - 21.03.09
=====================
* Added flag -csv_nodate to remove the extract date from the csv files
* Added scan_dns_name from new API for database/exadata
* Added csv for block/boot volumes

=====================
21.03.02 - 21.03.02
=====================
* Added Created for database componenets
* Added internal fqdn to compute and CSV

=====================
21.01.21 - 21.01.21
=====================
* Added SGW transit route
* Added LPG CIDR Blocks
* Added DRG Attachments

=====================
21.01.07 - 21.01.07
=====================
* Added Network Summary
* Added Flexible load balancers
* Added database software images

=====================
20.12.15 - 20.12.15
=====================
* Added OCVS Support (VMWare) under -paas
* Enable OAC Native under -paas
* Added Network Vlans
* Added Users Capabilities and last login
* Added tag namespace to identity

=====================
20.12.08 - 20.12.08
=====================
* Added retry policy to all pagination calls
* Added job id for resource manager
* Added Exadata Infrastructure and VM Clusters

=====================
20.11.24 - 20.11.24
=====================
* Added multiple VCN CIDR blocks

=====================
20.11.17 - 20.11.17
=====================
* Added secondary IP address to vnic
* Added several ocids to the json files
* Added load balancer rule sets

=====================
20.11.03 - 20.11.03
=====================
* Added metadata and extended metadata for instances using json output
* Added tags to load balancer resource

=====================
20.10.20 - 20.10.20
=====================
* Added limit check per compartment if only one compartment filtered

=====================
20.09.22 - 20.09.22
=====================
* Added Cloud Guard using -sec flag
* Added Logging using -sec flag

=====================
20.09.01 - 20.09.01
=====================
* Fixed Mysql error while mysql deployed to several regions

=====================
20.08.25 - 2020-08-25
=====================
* Fixed bug searching compartment by OCID
* Fixed OIC information when printout

=====================
20.07.28 - 2020-07-28
=====================
* Added Autonomous database properties for standby database

=====================
20.07.21 - 2020-07-21
=====================
* Remove vcn_id from several network list options to boost the performance - list_dhcp_options, list_local_peering_gateways, list_route_tables, list_security_lists, list_subnets and list_internet_gateways
* Fix database error if DG is in different region

=====================
20.07.14 - 2020-07-14
=====================
* Added retry policy for identity

=====================
20.06.30 - 2020-06-30
=====================
* Added compute agent information
* Added password policy to the tenant json (thanks to Josh)

=====================
20.06.15 - 2020-06-15
=====================
* Added Maintatance for DBSystem including alert if maintenance is less than 14 days
* Added -nobackups flags

=====================
20.06.09 - 2020-06-09
=====================
* Added file storage to the csv file
* Added network sources
* Added pagination call for the list_policies (Thank you Shyam)
* Added more info for the images in the summary

=====================
20.06.02 - 2020-06-02
=====================
* Added image to the summary if it is custom image (from the marketplace)
* Added step by step installation guide

=====================
20.05.18 - 2020-05-18
=====================
* Bug Fixed

=====================
20.05.04 - 2020-05-04
=====================
* Added database_db_system and database_autonomous csv files
* Added support for E3 Flex
* Added CPU type for compute
* Added support for Mysql service under the databases (-d)

=====================
20.04.20 - 2020-04-20
=====================
* Added Maintanance Window for DB Node
* Added User Credential and additional skip flag (-isc) (Thanks to J.Hammer for his Contribution)
* Added security alert flag if security list or security group has 0.0.0.0/0 from ports which not 22,443,3389

=====================
20.04.13 - 2020-04-13
=====================
* Added python version check
* Removed VCN check for compartment in order to extract other components
* Added Summary Total for Region
* Fixed Summary Total to include stopped VMs OCPUs in different category
* Added WAAS Policies to the -edge flag
* Added network security groups to the csv output

=====================
20.04.06 - 2020-04-06
=====================
* Added support for big data service with the -dataai flag
* Fixed limits printout when usage or available was 0 and remove if no usage or available
* Fixed security list dest port range values
* Added CSV Compartment
* Added delegation token for cloud shell with -dt (thanks to Leo)

=====================
20.03.31 - 2020-03-31
=====================
* Added DNS Zones to the -edge flag
* Added DNS Steering Policies to the -edge flag
* Added Events to -m flag
* Added Retry Strategy to all network and load balancers requests
* Added Image count to the summary
* Handle federation exception in identity

=====================
20.03.24 - 2020-03-24
=====================
* Added Identity User to the CSV

=====================
20.03.11 - 2020-03-11
=====================
* Add support for Data Science, Data Flow, Data Catalog using -dataai
* Moved ODA to -dataai flag
* Add support for nosql database
* Add private end point to autonomous database
* Added items to the display of DB System and Autonomous Database
* Added tunnel id to the tunnel info json

=====================
20.02.11 - 2020-02-11
=====================
* Add support for Function Applications (-fun)
* Add support for API gateways (-api)
* Fix limits to use pagination to produce all rows

=====================
20.01.30 - 2020-01-30
=====================
* Add DRG Redundant status

=====================
20.01.29 - 2020-01-29
=====================
* Fix call to list_databases due to OCI change the parameters requirement
* Fix bug listing autonomous databases if no VCN exist

=====================
20.01.15 - 2020-01-15
=====================
* Added recursive compartment with -cpr
* Added -ic to fetch compartments flag if only compartments required

=====================
20.01.14 - 2020-01-14
=====================
* Added users extract to CVS (thank you Josh)
* Fixed route extract when previous route is empty
* Added Native PaaS - OIC/ODA/OCE with -paas flag (Prepared as well OAC)
* Added filter by compartment ocid if specified with -cp
* Added -tenantid to overide it over the profile

=====================
19.11.19 - 2019-11-19
=====================
* Added total block volume in CSV export per instance
* Added compartment_id to all JSON resources
* Changed JSON 'compartment' to 'compartment_name' to be aligned across the application
* Added VPUs to the block and boot volumes

=====================
19.10.31 - 2019-10-31
=====================
* Added Storage Management for dbsystem
* Change output - gb to GB and tb to TB
* Added compartment_id, compartment_name, region_name to several areas for json
* Added more functionality to showoci_to_se.py to align with showoci JSON

====================
19.9.30 - 2019-09-30
====================
* Fix few bugs and added free compute shape

====================
19.9.11 - 2019-09-11
====================
* Fix instance configuration error when block volumes or vnic exist
* Added 0.5 seconds sleep for every 10 backendsets call to avoid TooManyRequestErrors if customer has many load balancers
* Added extract_date to each CSV
* Added support for X6 Shapes (Standard.B1)
* Added compute time for Region processing
* Changed processing time to HH:MM:DD

====================
19.9.4 - 2019-09-04
====================
* Added usage and available to the limits
* Added CSV extract for limits
* Fix few error handling

====================
19.9.3 - 2019-09-03
====================
* Support limits and quota with -lq flag
* Added request exception to handle service not found for new regions
* Added Total OCPUs in Summary for Database and Compute

====================
19.8.6 - 2019-08-06
====================
* Support Mumbai

====================
19.7.24 - 2019-07-24
====================

* Added support for load balancer cookie session persistence (LB cookie stickiness)
* Added load balancer backendset fields in the json format
* Added option to search compartment by path with -cpath flag, example -cpath "Adi Main / Adi Sub"

====================
19.7.17 - 2019-07-17
====================

* Added support with network security groups for compute, databases and load balancers
* In order to read security group rules, use permission is required - Allow Group ReadOnlyUsers to use network-security-groups in tenancy
* seperate security list components to individual fields

====================
19.7.10 - 2019-07-10
====================

* Added subnet_ids and vcn_id to json resources 
* If region do not have VCNs do not fetch resources that base on VCNS like compute, load balancer, database, ..
* Removed preauthenticated URL for object storage to avoid service errors on permission
* Fixed several bugs
* Added showoci_to_se.py - convert showoci JSON file to simple JSON format for easier processing.
* Added OCID for csv extracts

====================
19.6.24 - 2019-06-24
====================
Added
-----
* Added Freeform Tags and Defined Tages to the Compute and Database CSVs extract

====================
19.6.17 - 2019-06-17
====================
Added
-----
* Support to extract to CSV using -csv, currently supported IAM Groups and Policies, Network, Load Balancers and Databases
* Added subnet IP for the database node
* Added Shape base OCPU, Memory and local storage to instances and databases
* Added host+rules+path for load balancer listeners
* Added Support for Exadata.Base.48

Fixed
-----
* Several Bugs
* Fix Instances + db_node VNIC information
* Fix All ports display at network security list

====================
19.6.10 - 2019-06-10
====================

Added
-----
* Added support for autoscale Autonomous Database
* Added Workload Type for the Autonomous Database Summary

====================
19.6.3 - 2019-06-03
====================

Added
-----
* Added support for ipsec dynamic routing (bgp)

====================
19.5.27 - 2019-05-27
====================

Added
-----
* Added support for instance principals using -ip flag

====================
19.5.20 - 2019-05-20
====================

Added
-----
* Added Array check for service availability to support Seoul
* Added run_daily_report.sh for daily crontab use

====================
19.5.13 - 2019-05-13
====================

Added
-----
* Option to print nice to screen + JSON file using -sjf switch
* Added summary to JSON output file or screen
* Added Monitoring Service
* Added Notifications Service
* Added Edge Services (Healthcheck)
* Added Announcement
* Added Array check for service availability to support Tokyo

====================
19.4.23 - 2019-04-23
====================

Added
-----
* Added Autonomous Database Whitelist IPs
* Added Identity - Cost Tracking Tags
* Added Budgets
* Added Compute Autoscaling
* Add OS Version to the compute summary
* Add Reboot migration alert

Fixed / Changed
---------------
* Display Volume Backups with 1 line instead of 3 lines
* Fix load balancer pathroute error when output to JSON

====================
19.4.14 - 2019-04-14
====================

Added
-----
* Added Database Dataguard Association
* Added Tenancy information for filtered result
* Added Streams

Fixed
-----
* Fixed summary width 
* Fixed summary to print only when have data

====================
19.4.6 - 2019-04-06
====================

Added
-----
* Added Containers
* Added Database Edition to the Summary

====================
19.4.2 - 2019-04-02
====================

Added
-----
* Split application to classes and modules
* Added Tags inside Json output
* Added Cache components and print the cache
* Added autonomouns database backups
* uploaded to github

====================
3.0.7 - 2019-03-14
====================

Added
-----
* Add execution date/time 
* Add command line

Fixed
-----
* Use OCI constants for DBSystem and Config

====================
3.0.6 - 2019-03-13
====================

Added
-----
* includes OCID in the JSON file for most of objects
* includes local peering gateway name and IP in the route list
* Includes Service Gateway info in the route table and vcn
* Includes DRG name in the route table 
* Add no data found incase no data extracted

====================
3.0.5 - 2019-03-12
====================

Added
-----
* Support for Resource Management, Stacks and Jobs
* Include License type for databases @ summary page

====================
3.0.2 - 2019-03-03
====================

Fixed
-----
* Added Exceptions to handle service errors

====================
3.0.1 - 2018-02-27
====================

Added
-----
* Support for regional subnets in the Virtual Networking service

====================
3.0.0 - 2019-02-14
====================

Added
-----
* Summary pages 
* Summary Only flag -so 

====================
2.3.1 - 2019-02-04
====================

Added
-----
* Support for Maintenance Reboot

====================
2.3.0 - 2018-12-28
====================

Added
-----
* KMS support with flag -k

====================
2.2.5 - 2018-11-28
====================

Fixed
-----
* Use bucket statistics instead for size instead of reading bucket objects

====================
2.2.4 - 2018-11-16
====================

Added
-----
* Profile Support using flag -t
* Support Nested Compartments
* Support Transit VCN route
* Support Instance Pool Configuration
* Boot and Block Volume Backups 
* Added db backups + db system patches + DB home patches
* Added LB Certificate to the Load Balancer Section
* Added Limits to the File System Export_Set

====================
2.1.1 - 2018-10-18
====================

Added
-----
* Support VCN resources from different compartments
* Support Compute resources from different compartments
* Added Flag -nr for no root compartment extract

====================
2.0.8 - 2018-10-08
====================

Added
-----
* Added Remote Peering
* Added Autonomous DB + Filter by Compartment as cp
* Added Fastconnect
* Added NATGW + Object Lifecycle + Filter by region using -rg

Fixed
-----
* Fixed issue with ADWC at London which not yet supported
* Fixed Groups and Pagniation to retrieve all rows

====================
2.0.0 - 2018-08-06
====================

Added
-----
* Convert the application to build JSON variable first and option to JSON file or JSON screen
* Added option to include OCID in the JSON file
* Added subnet to the VNIC of instance/DB
* Added Fault Domain and OCI Version check

Fixed
-----
* fix Lb pathroute + listener

====================
 1.0.8 - 2018-08-01
====================

Added
-----
* Added menus with flags
* Added Security List and Route Table
* Added DHCP Options + Fix VNIC to display public only if exists, 
* Added flag to include ManagementCompartment and fix few bugs

Fixed
-----
* fixed exceptions, added proxy parameter and add git

====================
 1.0.0 - 2018-07-26
====================

* Initial Release
