Change Log
~~~~~~~~~~
All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_.

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
 1.0.8 - 2017-08-01
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
 1.0.0 - 2017-07-26
====================

* Initial Release
