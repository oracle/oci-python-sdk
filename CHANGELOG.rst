Change Log
~~~~~~~~~~
All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_.

====================
2.2.0 - 2019-02-21
====================

Added
-----
* Support for government-realm regions
* Support for the Streaming service
* Support for tags in the Key Management service
* Support for regional subnets in the Virtual Networking service

Fixed
-----
* Removed unused Announcements service 'NotificationFollowupDetails' model and 'followups' from Announcement model

====================
2.1.7 - 2019-02-07
====================

Added
-----
* Support for the Web Application Acceleration and Security (WAAS) service
* Support for the Health Checks service
* Support for connection strings on Database resources in the Database service
* Support for traffic management in the DNS service
* Support for tagging in the Email service

====================
2.1.6 - 2019-01-31
====================

Added
-----
* Support for the Announcements service

====================
2.1.5 - 2019-01-24
====================

Added
-----
* Support for renaming databases during restore-from-backup operations in the Database service
* Support for calling Oracle Cloud Infrastructure services in the ca-toronto-1 region

Fixed
-----
* KmsCryptoClient and KmsManagementClient updated to make service_endpoint required
* Explicitly imported path to idna. Addresses `GitHub issue 101 <https://github.com/oracle/oci-python-sdk/issues/101>`__

====================
2.1.4 - 2019-01-10
====================

Added
-----
* Support for device attributes on volume attachments in the Compute service
* Support for custom header rulesets in the Load Balancing service

====================
2.1.3 - 2018-12-13
====================

Added
-----
* Support for Data Guard for VM shapes in the Database service
* Support for sparse disk groups for Exadata shapes in the Database service
* Support for a new field, isLatestForMajorVersion, when listing DB versions in the Database service
* Support for in-transit encryption for paravirtualized boot volume and data volume attachments in the Block Storage service
* Support for tagging DNS Zones in the DNS service
* Support for resetting credentials for SCIM clients associated with an Identity provider and updating user capabilities in the Identity service

Security
-------
* pyOpenSSL pinning was changed to pyOpenSSL>=17.5.0 and cryptography pinning to cryptography>=2.1.4 to address vulnerability `CVE-2018-1000808 <https://nvd.nist.gov/vuln/detail/CVE-2018-1000808>`__

====================
2.1.2 - 2018-11-29
====================

Added
-----
* Support for getting bucket statistics in the Object Storage service
* Support for using FIPS compliant libcrypto library

Fixed
-----
* Block Storage service for copying volume backups across regions is now enabled

====================
2.1.1 - 2018-11-15
====================

Added
-----
* Support for VCN transit routing in the Networking service

Fixed
-----
* Fixed UploadManager to work with unbuffered streams in Python 3

====================
2.1.0 - 2018-11-01
====================

Added
-----
* Support for modifying the route table, DHCP options and security lists associated with a subnet in the Networking service.
* Support for tagging of File Systems, Mount Targets and Snapshots in the File Storage service.
* Support for nested compartments in the Identity service

Breaking
--------
* database_size_in_g_bs field in Backup and BackupSummary models renamed to database_size_in_gbs.

====================
2.0.6 - 2018-10-18
====================

Added
-----
* Support for cost tracking tags in the Identity service
* Support for generating and downloading wallets in the Database service
* Support for creating a standalone backup from an on-premises database in the Database service
* Support for db version and additional connection strings in the Autonomous Transaction Processing and Autonomous Data Warehouse resources of the Database service
* Support for copying volume backups across regions in the Block Storage service
* Support for deleting compartments in the Identity service
* Support for reboot migration for virtual machines in the Compute service
* Support for Instance Pools and Instance Configurations in the Compute service

Changed
-------
* database_edition field in Backup and model changed from a free format string to a validated string. It will only accept one of the following: “STANDARD_EDITION”, “ENTERPRISE_EDITION”, “ENTERPRISE_EDITION_HIGH_PERFORMANCE”, “ENTERPRISE_EDITION_EXTREME_PERFORMANCE”

Breaking
--------
* db_data_size_in_mbs field in Backup and BackupSummary models renamed to database_size_in_g_bs. The type changed from int to float.

====================
2.0.5 - 2018-10-04
====================

Added
-----
* Support for trusted partner images through application listings and subscriptions in the Compute service
* Support for object lifecycle policies in the Object Storage service
* Support for copying objects across regions in the Object Storage service
* Support for network address translation (NAT) gateways in the Networking service

====================
2.0.4 - 2018-09-27
====================

Added
-----
* Support for paravirtualized launch mode when importing images in the Compute service
* Support for Key Management service
* Support for encrypting the contents of an Object Storage bucket using a Key Management service key
* Support for specifying a Key Management service key when launching a compute instance in the Compute service
* Support for specifying a Key Management service key when backing up or restoring a block storage volume in the Block Volume service

Fixed
-----
* ObjectStorageClient requires int value for content_length keyword agruement to put_object and upload_part, but the SDK was not converting the type for the Requests library.

====================
2.0.3 - 2018-09-06
====================

Added
-----
* Added support for updating metadata fields on an instance in the Compute service

Fixed
-----
* Fixed example wait_for_resource_in_state.py to use existing response objects.  The updated example can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/wait_for_resource_in_state.py>`__.

====================
2.0.2 - 2018-08-23
====================

Added
-----
* Support for fault domains in the Identity service
* Support for resizing an offline volume in the Block Storage service
* Support for Autonomous Data Warehouse and Autonomous Transaction Processing in the Database service

Changed
-------
* Opened up the dependency pinning on cryptography due to `CVE-2018-10903 <https://nvd.nist.gov/vuln/detail/CVE-2018-10903>`__.  OCI does not call the affected method in cryptography, but upgrading is recommended.

====================
2.0.1 - 2018-08-09
====================

Added
-----
* Support for fault domains in the Compute service
* A sample showing how to use Search service from the SDK is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/search_example.py>`__.

====================
2.0.0 - 2018-07-26
====================

Added
-----
* Support for the OCI Search service
* Support for specifying a backup policy when creating a boot volume in the Block Storage service
* Added retries to the InstancePrincipalsSecurityTokenSigner when trying to refresh security tokens

Changed
-------
* Add six, requests, urllib3, idna, and chardet as vendored packages.

Fixed
-----
* Downloading an object from Object Storage could fail without an exception if the connection was closed while the object was being transmitted.

Breaking
--------
* The base exception from requests, `requests.exceptions.RequestException`, has been wrapped in oci.exceptions.RequestExceptions
* `requests.exceptions.ConnectTimeout` has been wrapped in oci.exceptions.ConnectTimeout

====================
1.4.5 - 2018-07-12
====================

Added
-----
* Support for tagging Load Balancers in the Load Balancing service
* Support for export options in the File Storage service
* Support for retrieving compartment name and user name as part of events in the Audit service

Changed
-------
* Setup.py updated to allow more version of cryptography when installing to an existing environment
* Add PyJWT as a vendored package


====================
1.4.4 - 2018-06-28
====================

Added
-----
* Support for service gateway management in the Networking service
* Support for backup and clone of boot volumes in the Block Storage service

Changed
-------
* Setup.py changed to allow more versions of pytz and python-dateutil packages when installing to an existing environment

====================
1.4.3 - 2018-06-14
====================

Added
-----
* Support for the Container Engine service

  * A sample showing how to use this service from the SDK is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/container_engine.py>`__.

Fixed
-------
* Add dependency to idna >=2.5,<2.7 since cryptography and requests both have a dependency on the library and pip can install a version that is incompatable with requests.

====================
1.4.2 - 2018-06-14
====================

This version was removed from PyPi due to a potential dependency conflict between cryptography and requests.

* Support for the Container Engine service

  * A sample showing how to use this service from the SDK is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/container_engine.py>`__.

====================
1.4.1 - 2018-05-31
====================

Added
-----
* Support for the "soft shutdown" instance action in the Compute service
* Support for Auth Token management in the Identity service

Changed
-------
* Bumped required version of python-dateutil to 2.7.3

====================
1.4.0 - 2018-05-17
====================

Added
-----
* Support for launching a database system from a backup in the Database service
* Support for backup or clone of multiple volumes at once using volume groups in the Block Storage service
* Support for tagging virtual cloud network resources in the Networking service
* Support for specifying the PARAVIRTUALIZED remote volume type when creating a virtual image or launching a new instance in the Compute service
* Example to retrieve network information for an instance which can be found on `Github <https://github.com/oracle/oci-python-sdk/blob/master/examples/get_all_instance_ip_addresses_and_dns_info.py>`__.

Changed
-------
* Added retrieving and setting the home region to the user_crud.py example which can be found on `Github <https://github.com/oracle/oci-python-sdk/blob/master/examples/user_crud.py>`__.

Breaking
--------
* In ``FileStorageClient.list_exports`` the ``compartment_id`` parameter has moved from a positional to a keyword argument.  This requires a code change as a v1.3.x call would look like: ``file_storage_client.list_exports('ocid1....')`` but in v1.4.x+ it would look like ``file_storage_client.list_exports(compartment_id='ocid1....')``

====================
1.3.20 - 2018-05-03
====================

Added
-----
* Support for returning names for events in the Audit service
* Support for multiple hostnames per listener in the Load Balancing service
* Helper function for Base64-ing scripts for user_data in launch instance options

  * An example of Base64-ing scripts for user_data can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/launch_instance_example.py>`__.

Changed
-------
* Add httpsig_cffi as a vendored package

Fixed
-----
* Multipart object put resume to account when final part is less than part size

====================
1.3.19 - 2018-04-19
====================

Added
-----
* Support for tagging ``DbSystem`` and ``Database`` resources in the Database Service
* Support for filtering by ``DbSystemId`` in ``ListDbVersions`` operation in Database Service
* Support for composite operations that provide convenience methods for operations that can be chained together (e.g. launching an instance and waiting for it to enter the RUNNING state)

  * An example on how to perform these operations can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/composite_operations_example.py>`__.


====================
1.3.18 - 2018-04-05
====================

Added
-----
* Added Python 3.6 as a supported Python version

Fixed
------
* Python API reference documentation improvements


====================
1.3.17 - 2018-03-26
====================

Added
------
* Added support for remote VCN peering across regions

  * An example on how to perform these operations can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/remote_peering_connection_example.py>`__.

* Added support for calling Oracle Cloud Infrastructure services in the uk-london-1 (LHR) region


====================
1.3.16 - 2018-03-08
====================

Added
-----
* Added support for the Email Service

  * An example on using the Email Service can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/email_service_example.py>`__.

* Added support for SMTP credentials in the Identity Service

  * An example on managing SMTP credentials can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/email_service_example.py>`__.

* Added support for paravirtualized volume attachments in Core Services

  * An example on using volume attachments can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/volume_attachment_example.py>`__.

* Added support for variable size boot volumes in Core Services

====================
1.3.15 - 2018-02-22
====================

Added
-----
* Support for File Storage Service

  * An example on using the File Storage Service can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/file_storage_example.py>`__.

* Added support for tagging Bucket resources in the Object Storage Service

  * An example on tagging buckets can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/object_storage_bucket_tagging_example.py>`__.

* Added support  for specifying a restore period for archived objects in the ``RestoreObjects`` operation of the Object Storage service.

  * An example on using archive storage can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/object_storage_archive_example.py>`__.

====================
1.3.14 - 2018-02-08
====================

Added
-----
* Support for Domain Name System Service

  * An example on using the Domain Name System Service can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/dns_service_example.py>`_.

* Support for reserved public IPs in Virtual Networking Service

  * An example on using this functionality can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/reserved_public_ip_example.py>`_.

* Support for path route sets in Load Balancing Service

  * An example on using this functionality can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/load_balancer_path_route_sets_example.py>`_.

* Support for automated and policy-based backups, read-only volume attachments, and incremental backups in Block Storage Service

  * An example on using policy-based backups can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/volume_backup_policy_example.py>`_.

* Support for filtering by ``backupId`` in ``ListDbSystems`` operation in Database Service

====================
1.3.13 - 2018-01-25
====================

Added
-----
* Support for using the ``ObjectReadWithoutList`` public access type when creating and updating buckets
* Support for dynamic groups in Identity Service
* Support for instance principals authentication when calling OCI services. An example of how to use instance principals authentication can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/instance_principals_examples.py>`_.
* Support for configuring idle timeout for listeners in Load Balancer Service
* Support for VNC console connections in Compute Service

====================
1.3.12 - 2018-01-11
====================

Added
-----
* Support for tagging:

  * Support for creating, updating, retrieving and listing tags and tag namespaces (these operations can be found in Identity Service)
  * Support for adding freeform and defined tags to resources in Core Services (Networking, Compute, and Block Volume) and Identity Service
  * An example on using tagging can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/tagging.py>`_.

* Support for bringing your own custom image for emulation mode virtual machines in Compute Service
* Added the ``oci.pagination`` module, which contains convenience functions so that you don't have to manually deal with page tokens when using list operations. See the `documentation <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/pagination.html>`_ for more information

Changed
-------
* Upgraded cryptography dependency to 2.1.3

  * Added dependency on pyOpenSSL <= 17.4.0 as the minimum cryptography version for pyOpenSSL 17.5.0 is 2.1.4

* Upgraded six dependency to 1.11.0
* Ugraded requests dependency to 2.18.4

====================
1.3.11 - 2017-12-11
====================

Added
-----
* Support for public peering for FastConnect
* Support for specifying an authorized entity name in a Letter of Authority
* Support for showing a list of bandwidth shapes for a specific provider (the ``list_fast_connect_provider_virtual_circuit_bandwidth_shapes`` in ``VirtualNetworkClient``)

Changed
-------
* Audit events now have a ``response_payload`` attribute which contains metadata of interest. For example, the OCID of a resource

Deprecated
-----------
* The ``list_virtual_circuit_bandwidth_shapes`` operation in ``VirtualNetworkClient`` has been deprecated. Use the ``list_fast_connect_provider_virtual_circuit_bandwidth_shapes`` operation instead
* When using ``CreateVirtualCircuitDetails``, supplying a ``provider_name`` is deprecated and ``provider_service_id`` should be used instead

====================
1.3.10 - 2017-11-27
====================

Added
-----
* Support for initializing model objects from keyword arguments
* Support for VCN to VCN peering within the same region
* Support for sorting and filtering in list APIs in Load Balancing service
* Support for user managed boot volumes
* Support for using a second physical NIC when attaching VNICs on X7 Bare Metal instances

Fixed
-----
* Model types now check the data types of their attributes prior to data being serialized and sent to the service
* When opc_request_id is specified as a parameter, it is no longer overwritten with a SDK-generated value

====================
1.3.9 - 2017-11-02
====================

Added
-----
* Support for the Audit service
* Support for archive storage tier, object rename and namespace metadata in Object Storage service
* Support for fast clones of volumes in Block Storage service
* Support for backup and restore in Database service
* Support for sorting and filtering in list APIs in Core Services
* Support for passing explicit None values to service operations. Consult the *Passing explicit Null/None values* section of the `docs <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io>`_ for more information.
* Support for supplying private key contents through the 'key_content' config field

Changed
-------
* Upgraded cryptography dependency to 1.9.
* Minimum version of Mac OS supported is now 10.8

====================
1.3.8 - 2017-10-12
====================

Deprecated
----------
* Creating block volumes and specifying the size in MBs is deprecated. Instead, the new size_in_gbs field should be used to specify the volume size in GBs.

Added
-----
* Support for creating block volumes and specifying the size in GBs.
* Support in UploadManager for handling piped input.
* Support for adding and updating display names for captured instance serial console data.
* Support for VNIC source/destination checks.
* Support for new Database service features: VM DBs, Bring Your Own License, and Data Guard.
* Support for the FRA (eu-frankfurt-1) region.

Changed
-------
* The size of block volumes and volume backups is specified in GBs as well as MBs.

====================
1.3.7 - 2017-09-11
====================

Deprecated
----------
* The top level namespace / package name has been changed from oraclebmc to oci. The oraclebmc package is deprecated and will no longer be maintained starting March 2018. Please upgrade to the oci package to avoid interruption at that time. More info is available `here <http://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/backward-compatibility.html>`_.
* The default configuration file location has been changed from ~/.oraclebmc/config to ~/.oci/config. The old location still works if the file at the new location does not exist.

Added
-----
* Support for the Database service
* Support for instance console connections
* Support for the Load Balancer Health Status API
* Support for Compartment renaming
* Support for managing customer secret keys

Changed
-------
* The default configuration file location is now ~/.oci/config

====================
1.3.6 - 2017-08-10
====================

Added
-------
* Documentation for UploadManager.

Changed
-------
* Upgraded cryptography dependency to 1.8.2.

====================
1.3.5 - 2017-07-20
====================

Added
-------
* Support for VCN multi-VNIC operations.
* Support for VCN secondary IP operations.
* Support for compute image import/export operations.

====================
 1.3.4 - 2017-06-16
====================

Fixed
-------

* Fixed bug in support for load balancing service.

====================
 1.3.3 - 2017-06-09
====================

Added
-------

* An UploadManager class to better support large object uploads through multipart and parallel operations.
* Support for object storage pre-authenticated requests and public buckets.
* Support for load balancing service.
* Support for nested instance metadata operations.

====================
 1.3.2 - 2017-05-18
====================

Added
-------

* Support for VCN private subnets using the prohibit_public_ip_on_vnic parameter on oci.core.VirtualNetworkClient.create_subnet.
* Support for FastConnect
* Support for list_regions and region subscription operations
* First class support for new IAD region

Fixed
-------

* For manually created configs (not from a file), use default values for optional fields that are not present (`GitHub issue <https://github.com/oracle/bmcs-python-sdk/issues/13>`_)
* Updated parsing of 'region' config value to enable better support for unrecognized regions

====================
 1.3.1 - 2017-04-27
====================

Changed
-------

* No longer throwing exceptions for unrecognized enum values returned by services.  Any unrecognized enum value returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.

====================
 1.3.0 - 2017-04-06
====================

Added
-------

* Support for DHCP Search Domain Option.
* Support for ComputeClient.get_windows_instance_initial_credentials.

====================
 1.2.0 - 2017-03-28
====================

Fixed
-------

* Allow service responses to deserialize to base classes when unknown subtypes are returned. Previously this would result in an exception.

Added
-------

* Support hostnames for instances and DNS labels for VCNs and subnets.

====================
 1.1.2 - 2017-03-16
====================

Changed
-------

* Updated cryptography version to 1.8.1

====================
 1.1.1 - 2017-02-23
====================

Added
-------

* Support for iPXE script parameter to launch_instance operation
* Support for stateless security list rules

====================
 1.1.0 - 2017-02-03
====================

Added
-------

* Support added for Core Services:

  * Block Storage
  * Compute
  * Virtual Network

====================
 1.0.0 - 2017-01-17
====================


Added
-------

* Initial Release
* Support added for Identity Service, Object Storage Service
