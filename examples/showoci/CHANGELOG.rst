Change Log
~~~~~~~~~~
All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_.

====================
19.9.24 - 2019-09-30
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
