Change Log
~~~~~~~~~~
All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_.

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
