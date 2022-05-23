Change Log
~~~~~~~~~~
All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_.
====================
2.69.0 - 2022-05-24
====================

Added
-----
* Support for the License Manager service
* Support for usage plans in the API Gateway service
* Support for packaged skill and instance metadata management, role-based access options on instance creation, and assigned ownership in the Digital Assistant service
* Support for compute capacity reservations in the VMWare Solution service
* Support for Oracle Linux 8 application streams in the OS Management service
 
Breaking
--------
* Support for retries by default on operations in the API Gateway service
* The property `specification` is now a required parameter for the deployment model in the API Gateway service
* The property `specification` is now a required parameter for the create_deployment_details model in the API Gateway service
 
Changed
-------
* The vendored dependency `requests` was updgraded from version `2.21.0` to `2.27.1`
* The vendored dependency `urllib3` was updgraded from version `1.24.1` to `1.26.9`
* The vendored dependency `chardet` was updgraded from version `3.0.4` to `4.0.0`
* The vendored dependency `idna` was updgraded from version `2.8` to `2.10`
* The vendored dependency `six` was updgraded from version `1.12.0` to `1.16.0`
 
====================
2.68.0 - 2022-05-17
====================

Added
-----
* Support for information requests in the Operator Access Control service
* Support for Helm charts and repositories on deployments in the DevOps service
* Support for Application Dependency Management service scan results on builds in the DevOps service
* Support for build resources to use Bitbucket Cloud repositories for source code in the DevOps service
* Support for character set selection on autonomous dedicated databases in the Database service
* Support for listing autonomous dedicated database supported character sets in the Database service
* Support for AMD E4 flex shapes on virtual machine database systems in the Database service
* Support for terraform and improvements for cross-region ADGs in the Database service

Breaking
--------
* Support for retries by default on GET and LIST operations in the Visual Builder service

====================
2.67.0 - 2022-05-10
====================

Added
-----
* Support for getting usage information for autonomous databases and Cloud at Customer autonomous databases in the Database service
* Support for the "standby" lifecycle state on autonomous databases in the Database service
* Support for BIP connections and dataflow operators in the Data Integration service
 
Breaking
--------
* The type of parameter `default_connection` was changed from `CreateConnectionFromBICC` to `CreateConnectionDetails` in the create_data_asset_from_fusion_app model in the Data Integration service
* The type of parameter `default_connection` was changed from `ConnectionFromBICCDetails` to `ConnectionDetails` in the data_asset_from_fusion_app model in the Data Integration service
* The type of parameter `default_connection` was changed from `ConnectionSummaryFromBICC` to `ConnectionSummary` in the data_asset_summary_from_fusion_app model in the Data Integration service
* The type of parameter `output_ports` was changed from a list of oci.data_integration.models.OutputPort to oci.data_integration.models.TypedObject in the aggregator model in the Data Integration service
* Support for retries by default on WAF Edge Policy GET / LIST operations in the Web Application Acceleration and Security service
* Support for retries by default on some operations in the Stack Monitoring service
* Support for retries by default on some resource discovery and monitoring operations in the Application Management service
* Support for retries by default on some operations in the MySQL Database service
 
====================
2.66.0 - 2022-05-03
====================

Added
-----
* Support for the Application Dependency Management service
* Support for platform configuration options on some bare metal shapes in the Compute service
* Support for shielded instances for BM.Standard.E4.128 and BM.Standard3.64 shapes in the Compute service
* Support for E4 dense VMs on launch and update instance operations in the Compute service
* Support for reboot migration on DenseIO shapes in the Compute service
* Support for an increased database name maximum length, from 14 to 30 characters, in the Database service
* Support for provisioned concurrency in the Functions service
 
Breaking
--------
* Support for retries by default on operations in the Vault service
* Support for retries by default on operations in the DNS service
* Support for retries by default on operations in the Content Management service
* Support for retries by default on operations in the Console Dashboard service
* Support for retries by default on Web Application Firewall operations in the Web Application Acceleration and Security service
* Support for retries by default on operations in the Data Science service

====================
2.65.0 - 2022-04-26
====================

Added
-----
* Support for the Service Mesh service
* Support for security zones in the Cloud Guard service
* Support for virtual test access points (VTAPs) in the Networking service
* Support for monitoring as a source in the Service Connector Hub service
* Support for creating budgets that target subscriptions and child tenancies in the Budgets service
* Support for listing shapes and specifying a shape during creation of a node in the Roving Edge Infrastructure service
* Support for bringing your own key in the Roving Edge Infrastructure service
* Support for enabling inspection of HTTP request bodies in the Web Application Acceleration and Security
* Support for cost management schedules in the Usage service
* Support for TCPS on external containers as well as non-container and pluggable databases in the Database service
* Support for autoscaling on Open Data Hub (ODH) clusters in the Big Data service
* Support for creating Open Data Hub (ODH) 0.9 clusters in the Big Data service
* Support for Open Data Hub (ODH) patch management in the Big Data service
* Support for customizable Kerberos realm names in the Big Data service
* Support for dedicated vantage points in the Application Performance Monitoring service
* Support for reactivating child tenancies in the Organizations service
* Support for punctuation and the SRT transcription format in the AI Speech service

Breaking
--------
* Support for default retries on some operations in the Networking service
* Support for default retries on all operations in the Data Safe service
* Support for default retries on some additional operations in the Application Performance Monitoring service
* Property `risk_score` is removed from model `Sighting` in the Cloud Guard service
* `subscription_id` is a required parameter for operation `list_subscription_mappings` in the subscription client in Tenant Manager control plane service

====================
2.64.0 - 2022-04-19
====================

Added
-----
* Support for the Stack Monitoring service
* Support for stack monitoring on external databases in the Database service
* Support for upgrading VM database systems in place in the Database service
* Support for viewing supported VMWare software versions when listing host shapes in the VMWare Solution service
* Support for choosing compute shapes when creating SDDCs and ESXi hosts in the VMWare Solution service
* Support for work requests on delete operations in the Vulnerability Scanning service
* Support for additional scan metadata in reports, including CVE descriptions, in the Vulnerability Scanning service
* Support for redemption codes in the Usage service

Breaking
--------
* Param `type` in model `DiscoveryDetails` assumes the value of `UNKNOWN_ENUM_VALUE` if it is assigned a value that is not of the allowed_values. It will not raise a `ValueError`.

====================
2.63.0 - 2022-04-12
====================

Added
-----
* Support for bringing your own IPv6 addresses in the Networking service
* Support for specifying database edition and maximum CPU core count when creating or updating an autonomous database in the Database service
* Support for enabling and disabling data collection options when creating or updating Exadata Cloud at Customer VM clusters in the Database service
 
Breaking
--------
* Support for retries by default on operations in the Identity service
* Support for retries by default on operations in the Operations Insights service
 
====================
2.62.1 - 2022-04-05
====================

Added
-----
* Fixed the lifecycle state values for target databases in the Data Safe service
* Support for content length and content type response headers when downloading PDFs in the Account Management service
* Support for creating Enterprise Manager-based zLinux host targets, creating alarms, and viewing top process analytics in the Operations Insights service
* Support for diagnostic reboots on VM instances in the Compute service

====================
2.62.0 - 2022-03-29
====================

Added
-----
* Support for returning the number of network ports as part of listing shapes in the Compute service
* Support for Java runtime removal and custom logs in the Java Management service
* Support for new parameters for BGP admin state and enabling/disabling BFD in the Networking service
* Support for private OKE clusters and blue-green deployments in the DevOps service
* Support for international customers to consume and launch third-party paid listings in the Marketplace service
* Support for additional fields on entities, attributes, and folders in the Data Catalog service
 
Breaking
--------
* Support for retries by default on operations in the Marketplace service
 
====================
2.61.0 - 2022-03-22
====================

Added
-----
* Support for getting the storage utilization of a deployment on deployment list and get operations in the GoldenGate service
* Support for virtual machines, bare metal machines, and Exadata databases with private endpoints in the Operations Insights service
* Support for setting deletion policies on database systems in the MySQL Database service
 
Breaking
--------
* Support for retries by default on operations in the Data Labeling service (data plane and control plane)
 
====================
2.60.1 - 2022-03-15
====================

Added
-----
* Support for Ubuntu platforms and unlimited installation keys in the Management Agent Cloud service
* Support for shielded instances in the VMWare Solution service
* Support for application resources in the Data Integration service
* Support for multi-AVM on Exadata Cloud at Customer infrastructure in the Database service
* Support for heterogeneous (VM and AVM) clusters on Exadata Cloud at Customer infrastructure in the Database service
* Support for custom maintenance schedules for AVM clusters on Exadata Cloud at Customer infrastructure in the Database service
* Support for listing vulnerabilities, vulnerability-impacted containers, and vulnerability-impacted hosts in the Vulnerability Scanning service
* Support for specifying an image count when creating or updating container scan recipes in the Vulnerability Scanning service

====================
2.60.0 - 2022-03-08
====================

Added
-----
* Support for the Sales Accelerator license option in the Content Management service
* Support for VCN hostname cluster endpoints in the Container Engine for Kubernetes service
* Support for optionally specifying an admin username and password when creating a database system during a restore operation in the MySQL Database service
* Support for automatic tablespace creation on non-autonomous and autonomous database dedicated targets in the Database Migration service
* Support for reporting excluded objects based on static exclusion rules and dynamic exclusion settings in the Database Migration service
* Support for removing, listing, and adding database objects reported by the Cloud Premigration Advisor Tool (CPAT) in the Database Migration service
* Support for migrating Oracle databases from the AWS RDS service to OCI as autonomous databases, using the AWS S3 service and DBLINK for data transfer, in the Database Migration service
* Support for querying additional fields of a resource using return clauses in the Search service
* Support for clusters and station clusters in the Roving Edge Infrastructure service
* Support for creating database systems and database homes using customer-managed keys in the Database service
 
Breaking
--------
* Support for retries enabled by default on operations in the Container Engine for Kubernetes service
* Support for retries enabled by default on operations in the Resource Manager service
* Support for retries enabled by default on operations in the Search service
 
====================
2.59.0 - 2022-03-01
====================

Added
-----
* Support for DRG route distribution statements to be specified with a new match type 'MATCH_ALL' for matching criteria in the Networking service
* Support for VCN route types on DRG attachments for deciding whether to import VCN CIDRs or subnet CIDRs into route rules in the Networking service
* Support for CPS offline reports in the Database service
* Support for infrastructure patching v2 features in the Database service
* Support for auto-scaling the storage of an autonomous database, as well as shrinking an autonomous database, in the Database service
* Support for managed egress via a default networking option on jobs and notebooks in the Data Science service
* Support for more types of saved search enums in the Management Dashboard service

Breaking
--------
* Support for retries enabled by default on some operations in the AI Vision service

====================
2.58.0 - 2022-02-22
====================

Added
-----
* Support for the Data Connectivity Management service
* Support for the AI Speech service
* Support for disabling crash recovery in the MySQL Database service
* Support for detector recipes of type "threat", new detector rule of type "rogue user", and sightings operations in the Cloud Guard service
* Support for more VM shape configurations when listing shapes in the Compute service
* Support for customer-managed encryption keys in the Analytics Cloud service
* Support for FastConnect device information in the Networking service
 
Breaking
--------
* Support for retries enabled by default on all operations in the Application Performance Monitoring control plane service

====================
2.57.0 - 2022-02-15
====================

Added
------
* Support for the AI Vision service
* Support for the Threat Intelligence service
* Support for creation of NoSQL database tables with on-demand throughput capacity in the NoSQL Database Cloud service
* Support for tagging features in the Oracle Container Engine for Kubernetes (OKE) service
* Support for trace snapshots in the Application Performance Monitoring service
* Support for auditing and alerts in the Data Safe service
* Support for data discovery and data masking in the Data Safe service
* Support for customized subscriptions and delivery of announcements by email and SMS in the Announcements service

Breaking
--------
* The API `query_old` was removed from `query_client` in the Application Performance Monitoring service
 
====================
2.56.0 - 2022-02-08
====================

Added
-----
* Support for managing tablespaces in the Database Management service
* Support for upgrading and managing payment for subscriptions in the Account Management service
* Support for listing fast launch job configurations in the Data Science service

Breaking changes
-----
* Support for retries enabled by default on all operations in the Application Performance Monitoring service
* The type for the `bill_to_address` parameter was changed from `Address` to `BillToAddress` in the invoice model of the Account Management service
* `payment_method` was made a required property of the `payment_detail` model of the Account Management service

====================
2.55.1 - 2022-02-01
====================

Added
------
* Support for calling Oracle Cloud Infrastructure services in the ap-dcc-canberra-1 region
* Support for the Console Dashboard service
* Support for capacity reservation in the Container Engine for Kubernetes service
* Support for tagging in the Container Engine for Kubernetes service
* Support for fetching listings by image OCID in the Marketplace service
* Support for underscores and hyphens in project resource names in the DevOps service
* Support for cross-region cloning in the Database service

====================
2.55.0 - 2022-01-25
====================

Added
-----
* Support for OneSubscription services
* Support for specifying if a run or application is streaming or batch in the Data Flow service
* Support for updating the Instance Configuration of an Instance Pool within a Cluster Network in the Compute Management service
* Updated documentation for Cross Region ADG feature for Autonomous Database in the Database service
 
Breaking
--------
* Support for retries enabled by default on all operations in the Object Storage service
====================
2.54.1 - 2022-01-18
====================

Added
------
* Support for calling Oracle Cloud Infrastructure services in the me-dcc-muscat-1 region
* Support for the Visual Builder service
* Support for cross-region replication of volume groups in the Block Storage service
* Support for boot volume encryption in the Container Engine for Kubernetes service
* Support for adding metadata to records when creating and updating records in the Data Labeling service
* Support for global export formats in snapshot datasets in the Data Labeling service
* Support for adding labeling instructions to datasets in the Data Labeling service
* Support for updating autonomous dataguard associations for autonomous container databases in the Database service
* Support for setting up automatic failover when creating autonomous container databases in the Database service
* Support for setting the RECO storage size when updating a database system in the Database service
* Support for reconnecting refreshable clones to source for autonomous databases on shared infrastructure in the Database service
* Support for checking if an autonomous database on shared infrastructure can be reconnected to source, in the Database service

====================
2.54.0 - 2022-01-11
====================

Added
------
* Support for calling Oracle Cloud Infrastructure services in the af-johannesburg-1 region
* Support for multiple protocols on the same listener in the Network Load Balancing service
* IPv6 support in the Network Load Balancing service
* Support for creating Enterprise Manager-based Solaris and SunOS host targets in the Operations Insights service
* Support for choosing Data Guard type (Active Data Guard or regular) on databases in the Database service
* Support for allowing control characters in responses as requested in https://github.com/oracle/oci-python-sdk/issues/404. Please see the github issue for more details
 
Fixed
-----
* The root cause of the issue causing data corruption as mentioned in https://github.com/oracle/oci-python-sdk/issues/410 has been fixed. Please see the github issue for more details
 
Breaking
--------
* Support for retries enabled by default on all operations in the Java Management service

====================
2.53.1 - 2021-12-21
====================

Fixed
-----
* Fixes the potential data corruption issue as described in https://github.com/oracle/oci-python-sdk/issues/410. Customers using FIPS compliant openssl versions are advised to enable FIPS with the ways described in https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/fips-libraries.html.

====================
2.53.0 - 2021-12-14
====================

Added
-----
* Support for node replacement in the VMWare Solution service
* Support for ingestion of SQL stats metrics in the Operations Insights service
* Support for AWR hub integration in the Operations Insights service
* Support for automatically generating logical entities from filename patterns and relationships between business terms across glossaries in the Data Catalog service
* Support for automatic start/stop at scheduled times in the Database service
* Support for cloud VM cluster resources on autonomous dedicated databases in the Database service
* Support for external Hive metastores in the Big Data service
* Support for batch detection/inference in the AI Language service
* Support for dimensions on monitoring targets in the Service Connector Hub service
* Support for invoice operations in the Account Management service
* Support for custom CA trust stores in the API Gateway service
* Support for generating scoped database tokens in the Identity service
* Support for database passwords for users, for logging into database accounts, in the Identity service

Fixed
-----
* Fixed an issue where multipart upload operations to Object Storage service throws SSLError on Oracle Linux instances

Breaking
--------
* Support for retries enabled by default on some operations in the Data Catalog service
* Support for retries enabled by default on all operations in the Ocvp service

====================
2.52.1 - 2021-12-07
====================

Added
-----
* Support for the Application Management service
* Support for getting the inventory of JMS resources and listing Java runtime usage in a specified host in the Java Management service
* Support for categories, entity topology, and verifying scheduled tasks in the Logging Analytics service
* Support for RAC databases in the GoldenGate service
* Support for querying additional fields of a resource using return clauses in the Search service
* Support for key versions and key version OCIDs in the Key Management service

====================
2.52.0 - 2021-11-30
====================

Added
-----
* Support for SQL Tuning Advisor in the Database Management service
* Support for listing users and getting user details in the Database Management service
* Support for autonomous databases in the Database Management service
* Support for enabling and disabling Database Management features on autonomous databases in the Database service
* Support for the Solaris platform in the Management Agent Cloud service
* Support for cross-compartment operations in the Operations Insights service
* Support for listing deployment backups in the GoldenGate service
* Support for standard tags in the Identity service
* Support for viewing problems for deleted targets in the Cloud Guard service
* Support for choosing a platform version while creating a platform instance in the Blockchain Platform service
* Support for custom IPSec connection tunnel internet key exchange phase 1 and phase 2 encryption algorithms in the Networking service
* Support for pagination when listing work requests corresponding to an APM domain in the Application Performance Monitoring service
* Support for the "deleted" lifecycle state on APM domains in the Application Performance Monitoring service
* Support for calling Oracle Cloud Infrastructure services in the eu-milan-1 and me-abudhabi-1 regions

Breaking
--------
* Support for retries enabled by default in all operations of the DevOps, Build, and Source Code Management services

====================
2.51.0 - 2021-11-17
====================

Added
-----
* Support for getting subnet topology in the Networking service
* Support for encrypted FastConnect resources in the Networking service
* Support for performance and high availability, as well as recommendation metrics, in the Optimizer service
* Support for optional TDE wallet passwords in the Database service
* Support for Object Storage service integration in the Big Data service

Breaking
--------
* Support for circuit breakers enabled by default in all services except Streaming and Compute
* Support for retries enabled by default in all operations of the Functions and Roving Edge services, and in some operations of the Streaming service.

====================
2.50.0 - 2021-11-09
====================

Added
-----
* Support for drill down metadata in the Management Dashboard service
* Support for operator access control on dedicated autonomous databases in the Operator Access Control service

Breaking
--------
* Property `resource_type` and `is_enforced_always` from model `CreateOperatorControlAssignmentDetails` changed from optional to required in the Operator Access Control service
* Property `operator_control_name`, `approver_groups_list` and `is_fully_pre_approved` from model `UpdateOperatorControlDetails` changed from optional to required in the Operator Access Control service
* Property `is_enforced_always` from model `UpdateOperatorControlAssignmentDetails` changed from optional to required in the Operator Access Control service
* Property `approver_groups_list` and `is_fully_pre_approved` from model `CreateOperatorControlDetails` changed from optional to required in the Operator Access Control service
* Data type for response of operation `create_operator_control_assignment` changed to `oci.operator_access_control.models.OperatorControlAssignment` in the Operator Access Control service
====================
2.49.1 - 2021-11-02
====================

Added
-----
* Support for the Database Tools service
* Support for scan listener port TCP and TCP SSL on cloud VM clusters in the Database service
* Support for domains in the Identity service
* Support for redeemable users and support rewards in the Usage service
* Support for calling Oracle Cloud Infrastructure services in the ap-singapore-1 and eu-marseille-1 regions
* Support for second level domain fallback via environment variable.

Changed
-------
* Endpoint for Identity service changed to include `.oci` subdomain

====================
2.49.0 - 2021-10-26
====================

Added
-----
* Support for the Source Code Management service
* Support for the Build service
* Support for the Certificates service
* Support to create child tenancies in an organization and manage subscriptions in the Organizations service
* Support for Certificates service integration in the Load Balancing service
* Support for creating hosts in specific availability domains in the VMWare Solution service
* Support for user-defined functions and libraries, as well as scheduling and orchestration, in the Data Integration service
* Support for EM-managed Exadatas and EM-managed hosts in the Operations Insights service

Breaking
--------
* Models `ComputeInstanceGroupBlueGreenDeployStageExecutionProgress`, `ComputeInstanceGroupBlueGreenTrafficShiftDeployStageExecutionProgress`, `ComputeInstanceGroupCanaryApprovalDeployStageExecutionProgress`, `ComputeInstanceGroupCanaryDeployStageExecutionProgress`, `ComputeInstanceGroupCanaryTrafficShiftDeployStageExecutionProgress`, `RunPipelineDeployStageExecutionProgress`and `RunValidationTestOnComputeInstanceDeployStageExecutionProgress` were removed from the DevOps service.

====================
2.48.0 - 2021-10-19
====================

Added
-----
* Support for creating database systems from backups with database software images in the Database service
* Support for optionally providing a SID prefix during Exadata database creation in the Database service
* Support for node subsetting on VM clusters in the Database service
* Support for non-CDB to PDB conversion in the Database service
* Support for default homepages, unprocessed data buckets, and parsing geostats in the Logging Analytics service
* Support for Circuit Breakers. Please refer `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/circuit_breakers.html>`__ to learn more.
* Support for enabling/disabling Retries globally for operations using Default Retry Strategy. Please refer `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html#overriding-the-retry-behavior-at-global-sdk-level>`__ for more info.

Breaking
--------
* Default Retry strategy will now retry operations for max 8 attempts and have a timeout of 600 seconds before failing. The strategy will now use `De-Correlated jitter <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html#de-correlated-jitter>`__ as the default delay strategy.

====================
2.47.1 - 2021-10-12
====================

Added
-----
* Support for the Data Labeling Service
* Support for the Web Application Firewall service
* Support for querying and setting Application Performance Monitoring configurations in the Application Performance Monitoring service
* Support for the run-once monitor feature and network data collection in the Application Performance Monitoring service
* Support for Oracle Enterprise Manager bridges, source auto-association, source event types mapping, and partitioning and searching data by LogSet in the Logging Analytics service
* Support for Log events APIs used by plugins like fluentd, fluentbit, etc. to upload data in the Logging Analytics service
* Support for a new ActionType: FAILED in work requests in the VMware Provisioning service
* Support for calling Oracle Cloud Infrastructure services in the il-jerusalem-1 region

====================
2.47.0 - 2021-10-05
====================

Added
-----
* Support for configuring Binlog variables in the MySQL Database service.
* Support new response value "OPERATOR" for backup creationType in list and get MDS backup API in the MySQL Database service.
* Support for SetAutoUpgradableConfig and GetAutoUpgradableConfig operations in Management Agent Cloud service.
* Support for additional installType filter for List Management Agents, Images and Count API operations in Management Agent Cloud service.
* Support for list and read DeploymentUpgrade, cancel and restore DeploymentBackup in the Golden Gate service.
* Support for non-autonomous databases targets, executing Pre-Migration advisor, uploading Datapump logs into Object Storage bucket, and filtering Database Objects in the Database Migration service.
* Support for calling Oracle Cloud Infrastructure services in the ap-ibaraki-1 region.

Breaking changes
----
* Param `is_agent_auto_upgradable` is removed from model `UpdateManagementAgentDetails` in the Management Agent Cloud Service
* Param `display_name` is removed from operations `list_work_requests`, `list_work_request_logs` and `list_work_request_errors` in the Database Migration Service Client
* Allowed values for param `sort_order` from operation `list_work_requests` changed to `timeAccepted` in the Database Migration Service Client
* Allowed values for param `sort_order` from operations `list_work_request_errors` and `list_work_request_logs` changed to `timestamp` in the Database Migration Service Client
* Param `time_stamp` renamed to `timestamp` in models `WorkRequestLogEntry`, `WorkRequestError` for the Database Migration Service
* Param `compartment_id` is removed from model `UpdateAgentDetails` for the Database Migration Service

====================
2.46.0 - 2021-09-28
====================

Added
-----
* Support for autonomous databases and clones on shared infrastructure not requiring mTLS in the Database service
* Support for server-side encryption using object-specific KMS keys in the Object Storage service
* Support for Windows in the Java Management service
* Support for using network security groups in the API Gateway service
* Support for network security groups in the Functions service
* Support for signed container images in the Functions service
* Support for setting message format when creating and updating alarms in the Monitoring service
* Support for user and security assessment features in the Data Safe service

Breaking
--------
* Operations `request_summarized_application_usage`, `request_summarized_installation_usage`, `request_summarized_jre_usage`, `request_summarized_managed_instance_usage` were removed from the Java Management Service Client
* Models `RequestSummarizedApplicationUsageDetails`, `RequestSummarizedInstallationUsageDetails`, `RequestSummarizedJreUsageDetails` and `RequestSummarizedManagedInstanceUsageDetails` were removed from Java Management Service

Changed
-------
* Dependency `configparser` will only be installed for Python 2. The built-in configparser will be used for Python 3

====================
2.45.1 - 2021-09-14
====================

Added
-----
* Support for serviceHostKeyFingerprint property for InstanceConsoleConnection in Core service
* Support for Shielded Instances in Core service
* Support for ML Jobs in the Data Science service

====================
2.45.0 - 2021-09-07
====================

Added
-----
* Support for terraform advanced options (detailed log level, refresh, and parallelism) on jobs in the Resource Manager service
* Support for forced cancellation when cancelling jobs in the Resource Manager service
* Support for getting the detailed log content of a job in the Resource Manager service
* Support for provider information in the responses of list operations in the Management Dashboard service
* Support for scheduled jobs in Database Management service
* Support for monitoring and management of OCI virtual machine, bare metal, and ExaCS databases in the Database Management service
* Support for a unified way of managing both external and cloud databases in the Database Management service
* Support for metrics and Performance Hub on virtual machine, bare metal, and ExaCS databases in the Database Management service

Breaking
--------
* Param `oci_splat_generated_ocids` is removed from operation `create_template` in the Resource Manager service

====================
2.44.2 - 2021-08-31
====================

Added
-----
* Support for Oracle Analytics Cloud and OCI Vault integration on connections in the Data Catalog service
* Support for critical event monitoring in the OS Management service

====================
2.44.1 - 2021-08-24
====================

Added
-----
* Support for generating recommended VM cluster networks in the Database service
* Support for creating VM cluster networks with a specified listener port in the Database service

====================
2.44.0 - 2021-08-17
====================

Added
-----
* Support for getting management agent hosts which are eligible to create Operations Insights host resources on, in the Operations Insights service
* Support for getting summarized agent counts and summarized plugin counts in the Management Agent Cloud service

Breaking
--------
* Model `WorkSubmissionKey` was removed from Management Agent Cloud service
* Type for parameter `plugin_name` changed to `list[str]` from `str` in operation `list_management_agent_plugins` in the Management Agent Cloud Service
* Type for parameter `version` changed to `list[str]` from `str` in operation `list_management_agent_plugins` in the Management Agent Cloud Service
* Type for parameter `platform_type` changed to `list[str]` from `str` in operation `list_management_agent_plugins` in the Management Agent Cloud Service

====================
2.43.2 - 2021-08-03
====================

Added
-----
* Support for manually copying volume group backups across regions in the Block Volume service
* Support for work requests for the copy volume backup and copy boot volume backup operations in the Block Volume service
* Support for specifying external Hive metastores during application creation in the Data Flow service
* Support for changing the compartment of a backup in the MySQL Database service
* Support for model catalog features including provenance, metadata, schemas, and artifact introspection in the Data Science service
* Support for Exadata system network bonding in the Database service
* Support for creating autonomous databases with early patching enabled in the Database service

====================
2.43.1 - 2021-07-27
====================

Added
-----
* Support for filtering by tag on capacity planning and SQL warehouse list operations in the Operations Insights service
* Support for creating cross-region autonomous data guards in the Database service
* Support for the customer contacts feature on cloud exadata infrastructure in the Database service
* Support for cost analysis custom tables in the Usage service

====================
2.43.0 - 2021-07-20
====================

Added
-----
* Support for schedules, schedule tasks, REST tasks, operators, S3, and Fusion Apps in the Data Integration service
* Support for getting available updates and update histories for VM clusters in the Database service
* Support for downloading network validation reports for Exadata network resources in the Database service
* Support for patch and upgrade of Grid Infrastructure (GI), and update of DomU OS software for VM clusters in the Database service
* Support for updating data guard associations in the Database service

Changed
-------
* Changed Expect HTTP header to support only Object Storage and Log Analytics services, to mitigate performance degradation issues in the OCI Python SDK v2.38.4 and above. For more information, please see https://github.com/oracle/oci-python-sdk/issues/367

Breaking
--------
* Data Type for param `type` changed from `str` to `object` in model `ShapeField` in the Data Integration Service
* Data Type for param `type` changed from `oci.data_integration.models.BaseType` to `object` in model `Parameter` in the Data Integration Service
* Data Type for param `type` changed from `str` to `object` in model `NativeShapeField` in the Data Integration Service
* Base class for model `OracleWriteAttributes` changed from `object` to `oci.data_integration.models.AbstractWriteAttribute` in the Data Integration Service
* Base class for model `OracleReadAttributes` changed from `object` to `oci.data_integration.models.AbstractReadAttribute` in the Data Integration Service
* Base class for model `OracleAdwcWriteAttributes` changed from `object` to `oci.data_integration.models.AbstractWriteAttribute` in the Data Integration Service
* Base class for model `OracleAtpWriteAttributes` changed from `object` to `oci.data_integration.models.AbstractWriteAttribute` in the Data Integration Service
* Param `bucket_name` was removed from model `OracleAtpWriteAttributes` in the Data Integration Service
* Param `bucket_name` was removed from model `OracleAdwcWriteAttributes` in the Data Integration Service
* Param `bucket_name` was removed from model `OracleAdwcWriteAttributes` in the Data Integration Service
* Param `is_file_pattern` was removed from model `CsvFormatAttribute` in the Data Integration Service
* Constant `MODEL_TYPE_REST_OPERATOR` was removed from model `Operator` in the Data Integration Service

====================
2.42.0 - 2021-07-13
====================

Added
-----
* Support for the AI Anomaly Detection service
* Support for retrieving a DNS zone as a zone file in the DNS service
* Support for querying manual adjustments in the Usage service
* Support for searching Marketplace listings in the Marketplace service
* Support for new cluster type 'ODH' in the Big Data service
* Support for availability domain as an optional parameter when creating VLANs in the Networking service
* Support for search domain type on DHCP options, to support multi-level domain search in the Networking service

Breaking
--------
* Model `TSIG` was removed from the DNS service
* Param `tsig` was removed from model `ExternalMaster` in the DNS service
* Models `CreateCustomTableDetails`, `CreateScheduleReportDetails`, `CustomTable`, `CustomTableCollection`, `CustomTableSummary`, `SavedScheduleReport`, `ScheduleReport`, `ScheduleReportCollection`, `ScheduleReportSummary`, `UpdateCustomTableDetails`, `UpdateScheduleReportDetails` were removed from Usage API service

====================
2.41.1 - 2021-07-06
====================

Added
-----
* Support for order activation in the Organizations service
* Support for resource principal authorization on Enterprise Manager bridge resources in the Operations Insights service
* Support for the starter edition license type in the Content and Experience service
* Support for the Generic Artifacts service's new domain name

====================
2.41.0 - 2021-06-29
====================

Added
-----
* Support for the DevOps service
* Support for configuring network security groups for node pools in the Container Engine for Kubernetes service
* Support for optionally specifying CPU core count and data storage size when creating autonomous databases in the Database service
* Support for metastore and initial data asset import/export in the Data Catalog service
* Support for associating domain names to emails and managing email domain names / DKIM in the Email Delivery service
* Support for email domain names on senders and suppressions in the Email Delivery service
* Support for signing request bodies for PUT/POST/PATCH requests where it is expected by the service. For more information, please see https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/index.html

Breaking
--------
* The property `cpu_core_count` was made optional in model CreateAutonomousDatabaseBase in the Database service
* `DISPLAYNAME` was removed as allowed value for the SortBy property in method `list_job_executions` under the Data Catalog service
* Util function `should_record_body_position_for_retry` was moved from src/oci/retry/retry_utils.py to src/oci/util.py
* Util function `record_body_position_for_retry` was renamed to `record_body_position_for_rewind` and was moved from src/oci/retry/retry_utils.py to src/oci/util.py
* Util function `rewind_body_for_retry` was renamed to `rewind_body` and was moved from src/oci/retry/retry_utils.py to src/oci/util.py

====================
2.40.1 - 2021-06-22
====================

Added
-----
* Support for virtual machine and bare metal pluggable databases in the Database service

Changed
-------
* Changed allowed versions of cryptography package to a range, starting from from 3.2.1 up to 3.4.7

====================
2.40.0 - 2021-06-15
====================

Added
-----
* Support for elastic storage on Exadata Infrastructure resources for Cloud at Customer in the Database service
* Support for registration and management of target databases in the Data Safe service
* Support for config on metadata in the Management Dashboard service
* Support for a new work request operation type for node pool reconciliation events in the Container Engine for Kubernetes service
* Support for migrating clusters with a public Kubernetes API endpoint which are not integrated with a customer's VCN to a VCN-native cluster in the Container Engine for Kubernetes service
* Support for getting the spark version of applications, and filtering applications by spark version, in the Data Flow service

Breaking
--------
* The properties `freeform_tags` and `defined_tags` were removed from the ManagementDashboardExportDetails model in the Management Dashboard service

====================
2.39.1 - 2021-06-08
====================

Added
-----
* Support for Java Management service
* Support for resource principals for the Enterprise Manager bridge resource in Operations Insights service
* Support for encryptionInTransitType in BootVolumeAttachment and IScsiVolumeAttachment in Core service
* Support for updating iscsiLoginState for VolumeAttachment in Core service
* Support for a new type of Source called Import for use with the Export tool in Application Migration service

Fixed
-----
* Fixed a bug where requests were not retried for a specific case of Upload Manager uploading a file with multipart disabled and callback provided

====================
2.39.0 - 2021-06-01
====================

Added
-----
* Support for configuration of autonomous database KMS keys in the Database service
* Support for creating database software images with any supported RUs in the Database service
* Support for creating database software images from an existing database home in the Database service
* Support for listing all NSGs associated with a given VLAN in the Networking service
* Support for a duration windows, task failure reasons, and next execution times on scheduled tasks in the Logging Analytics service
* Support for calling Oracle Cloud Infrastructure services in the sa-vinhedo-1 region

Breaking
-----
* `compartment_id` is now optional in operation `list_network_security_groups` in the Networking service

====================
2.38.4 - 2021-05-25
====================

Added
-----
* Support for the Generic Artifacts service
* Support for the Bastion service
* Support for reading secrets by name in the Vault service
* Support for the isDynamic field when listing definitions in the Limits service
* Support for getting billable image sizes in the Compute service
* Support for getting Automatic Workload Repository (AWR) data on external databases in the Database Management service
* Support for the VM.Standard.E3.Flex flexible compute shape with customizable OCPUs and memory on notebooks in the Data Science service
* Support for container images and generic artifacts billing in the Registry service
* Support for the HCX Enterprise add-on in the VMware Solution service
* Support for the Expect HTTP header. Expect headers are added by default for all PUT/POST operations

====================
2.38.3 - 2021-05-18
====================

Added
-----
* Support for spark-submit compatible options in the Data Flow service
* Support for Object Storage as a configuration source in the Resource Manager service

====================
2.38.2 - 2021-05-11
====================

Added
-----
* Support for creating notebook sessions with larger block volumes in the Data Science service
* Support for database maintenance run patch modes in the Database service

Fixed
-----
* Fixed a bug where `timeout=None` was not respected when passed to clients. The older versions of the SDK still use the default connection timeout(10s) and read timeout(60s) when initialized with `timeout=None`

Changed
-------
* Improvement in the performance of Upload Manager for parallel uploads. This is achieved by overriding the default read size of Python HTTP client from 8192 bytes to 64 kb.

====================
2.38.1 - 2021-05-04
====================

Added
-----
* Support for the Operator Access Control service
* Support for the Service Catalog service
* Support for the AI Language service
* Support for autonomous database on Exadata Cloud at Customer infrastructure patching in the Database service

====================
2.38.0 - 2021-04-27
====================

Added
-----
* Support for RACs (real application clusters) for external container, non-container, and pluggable databases in the Database service
* Support for data masking in the Cloud Guard service
* Support for opting out of DNS records during instance launch, as well as attaching secondary VNICs, in the Compute service
* Support for mutable sizes on cluster networks in the Autoscaling service
* Support for auto-tiering on buckets in the Object Storage service

Breaking
--------
* VCN id parameters were moved from being required to being optional on all list operations in the Networking service

====================
2.37.0 - 2021-04-20
====================

Added
-----
* Support for opting in/out of live migration on instances in the Compute service
* Support for enabling/disabling Operations Insights on external non-container and external pluggable databases in the Database service
* Support for a GraphStudio URL as a connection URL on databases in the Database service
* Support for adding customer contacts on autonomous databases in the Database service
* Support for name annotations on harvested objects in the Data Catalog service

Changed
-------
* If retries are enabled, the SDK will now retry on status 409/IncorrectState. It will not retry on status 501.

Breaking
--------
* Bumped cryptography version to 3.3.2 to address security vulnerability https://github.com/oracle/oci-python-sdk/pull/322

====================
2.36.0 - 2021-04-13
====================

Added
-----
* Support for the Database Migration service
* Support for the Networking Topology service
* Support for getting the id of peered VCNs on local peering gateways in the Networking service
* Support for burstable instances in the Compute service
* Support for preemptible instances in the Compute service
* Support for fractional resource usage and availability in the Limits service
* Support for streaming analytics in the Service Connector Hub service
* Support for flexible routing inside DRGs to enable packet flow between any two attachments in the Networking service
* Support for routing policy to customize dynamic import/export of routes in the Networking service
* Support for IPv6, including on FastConnect and IPsec resources, in the Networking service
* Support for request validation policies in the API Gateway service
* Support for RESP-compliant (e.g. REDIS) response caches, and for configuring response caching per-route in the API Gateway service
* Support for flexible billing in the VMWare Solution service
* Support for new DNS format for the Web Application Acceleration and Security service
* Support for configuring APM tracing on applications and functions in the Functions service
* Support for Enterprise Manager external databases and Management Agent Service managed external databases and hosts in the Operations Insights service
* Support for getting cluster cache metrics for RAC CDB managed databases in the Database Management service

Breaking changes
----
* Removed response codes `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307` and `444` from attribute `block_response_code` in model `AddressRateLimiting` in the Web Application Acceleration and Security Service
* `VcnId` was made optional in CreateDrgAttachmentDetails model under Core services.
* The property `IsInternetAccessAllowed` was removed from CreateIpv6Details model under Core services.
* The property `Ipv6CidrBlock` was removed from CreateVcnDetails model under Core services.
* The property `PublicIpAddress` and `IsInternetAccessAllowed` were removed from Ipv6 model under Core services.
* Required property `PeerId` was added to LocalPeeringGateway model under Core services.
* The property `Ipv6PublicCidrBlock` was removed from Subnet model under Core services.
* The property `Ipv6PublicCidrBlock` was replaced by `Ipv6CidrBlocks` in Vcn model in Core services.
* Required property `CurrentSku` was added under CreateEsxiHostDetails under Ocvp service.
* Required property `InitialSku` was added under CreateSddcDetails under Ocvp service.
* Required properties `BillingContractEndDate`, `NextSku` & `CurrentSku` were added under EsxiHost under Ocvp service.
* Required properties `BillingContractEndDate`, `NextSku` & `CurrentSku` were added under EsxiHostSummary under Ocvp service.
* Required property `InitialSku` was added under Sddc under Ocvp service.
* Required property `Id` was added under DatabaseDetails under Opsi service.
* `compartment_id` and `database_id` are now optional in operation `ingest_sql_bucket` under Opsi service.
* `compartment_id` and `database_id` are now optional in operation `ingest_sql_plan_lines` under Opsi service.
* `compartment_id` and `database_id` are now optional in operation `ingest_sql_text` under Opsi service.
* `compartment_id` is now optional in operation `list_database_insights` under Opsi service.
* `database_id` is now optional in operation `list_sql_plans` under Opsi service.
* `database_id` is now optional in operation `summarize_sql_response_time_distributions` under Opsi service.
* `database_id` is now optional in operation `summarize_sql_statistics_time_series_by_plan` under Opsi service.
* `database_id` is now optional in operation `summarize_sql_plan_insights` under Opsi service.
* Value of attribute `model_type` in model `ConnectionDetails` in Data Integration service defaults to UNKNOWN_ENUM_VALUE when it receives an invalid value. In the earlier versions, this raises a ValueError

====================
2.35.1 - 2021-04-06
====================

Added
-----
* Support for scheduling the suspension and resumption of compute instance pools based on predefined schedules in the Autoscaling service
* Support for database software images for Cloud@Customer in the Database service
* Support for OCIC IDCS authorization details in the Application Migration service
* Support for cross-region asynchronous volume replication in the Block Storage service
* Support for SDK generation in the API Gateway service
* Support for container image signing in the Registry service
* Support for cluster features as a part of the Container Engine for Kubernetes service
* Support for filtering dedicated virtual machine hosts by remaining memory and OCPUs in the Compute service
* Support for read/write-any object from buckets using pre-authenticated requests in the Object Storage service
* Support for restricting pre-authenticated requests by prefix in the Object Storage service
* Support for route filtering on public virtual circuits in the Virtual Networking service
* Support for calculating content length of a non-resettable stream for binary uploads. A non-resettable stream will be buffered into memory to calculate the content length. A buffer_limit may be passed into the request to provide a buffer limit. The default buffer limit is 100 MiB. More documentation can be found here: https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/index.html

====================
2.35.0 - 2021-03-30
====================

Added
-----
* Support for the Vulnerability Scanning service
* Support for vSphere 7.0 in the VMware Solution service
* Support for forecasting in the Usage service
* Support for viewing, searching, and modifying parameters for on-premise Oracle databases in the Database Management service
* Support for listing tablespaces of managed databases in the Database Management service
* Support for cross-regional replication of keys in the Key Management service
* Support for highly-available database systems in the MySQL Database service
* Support for Oracle Enterprise Manager bridges, source auto-association, source event type mappings, and plugins to upload data in the Logging Analytics service

Breaking
--------
* Name of Enum attribute "forcast_type" in Usage API service renamed to "forecast_type"
* Value of Enum attribute "forecast_type" in Usage API service defaults to UNKNOWN_ENUM_VALUE when it receives an invalid value. In the earlier versions, this raises a ValueError
* Retries are now enabled in Upload Manager. The SDK used to explicitly override retry configuration on binary upload operations because of potential data corruption issue (https://github.com/oracle/oci-python-sdk/issues/203).

====================
2.34.0 - 2021-03-23
====================

Added
-----
* Support for the Network Load Balancing service
* Support for maintenance runs on autonomous databases in the Database service
* Support for announcement preferences in the Announcements service
* Support for domain claiming in the Organizations service
* Support for saved reports in the Usage service
* Support for the HeatWave in-memory analytics accelerator in the MySQL Database service
* Support for community applications in the Marketplace service
* Support for capacity reservations in the Compute service

Breaking
--------
* Parameter `vnic_id` changed from optional to required in model `CreateIpv6Details` in the core services
* Parameter `vnic_id` changed from optional to required in model `Ipv6` in the core services
* Value of Enum attribute `operator` in Usage API service defaults to `UNKNOWN_ENUM_VALUE` when it receives an invalid value. In the earlier versions, this raises a `ValueError`

====================
2.33.0 - 2021-03-16
====================

Added
-----
* Support for routing policies and HTTP2 listener protocols in the Load Balancing service
* Support for model deployments in the Data Science service
* Support for private clusters in the Container Engine for Kubernetes service
* Support for updating an instance's usage type in the Content and Experience service

Breaking
--------
* Retries are now enabled on all operations performing binary data upload, except upload manager. The SDK used to explicitly override retry configuration on binary upload operations because of potential data corruption issue (https://github.com/oracle/oci-python-sdk/issues/203).

====================
2.32.1 - 2021-03-09
====================

Added
-----
* Support for the Application Performance Monitoring service
* Support for the Golden Gate service
* Support for SMS subscriptions in the Notifications service
* Support for friendly-formatted messages in the Service Connector Hub service
* Support for attaching and detaching instances to instance pools in the Autoscaling service

====================
2.32.0 - 2021-03-02
====================

Added
-----
* Support for pipelines, pipeline tasks, and favorites in the Data Integration service
* Support for publishing tasks to OCI Data Flow in the Data Integration service
* Support for clones in the File Storage service

Breaking
--------
* Changed model `UniqueKey` in the Dataintegration service to not inherit from Key.
* Changed model `PrimaryKey` in the Dataintegration service to inherit from `UniqueKey`.
* Removed enum values `PRIMARY_KEY` and `UNIQUE_KEY` in property `model_type` from model `key` in the Dataintegration service.

====================
2.31.2 - 2021-02-23
====================

Added
-----
* Support for the OCI Registry service
* Support for exporting an existing running VM, or a copy of VM, into a VMDK, QCOW2, VDI, VHD, or OCI formatted image in the Compute service
* Support for platform configurations on instances in the Compute service
* Support for providing target tags and target compartments on profiles in the Optimizer service
* Support for the 'Fix it' feature in the Optimizer service

====================
2.31.1 - 2021-02-16
====================

Added
-----
* Support for scan DNS names and zone ids on database system, cloud VM cluster, and autonomous Exadata infrastructure responses in the Database service
* Support for specifying ACL rules to limit ingress into public load balancers in the Integration service
* Support for Cloud at Customer as a source type in the Application Migration service
* Support for selective migration of specific resources in the Application Migration service

====================
2.31.0 - 2021-02-09
====================

Added
-----
* Support for the Database Management service
* Support for setting an offset for budget processing in the Budgets service
* Support for enabling and disabling Oracle Cloud Agent plugins in the Compute service
* Support for listing available plugins and for getting the status of plugins in the Oracle Cloud Agent service
* Support for one-off patching in autonomous transaction processing - dedicated databases in the Database service
* Support for additional database upgrade options in the Database service
* Support for glossary term recommendations in the Data Catalog service
* Support for listing errata in the OS Management service

Breaking
--------
* Model `InstanceAgentCommandContentInfo` is removed from Compute Instance Agent service

====================
2.30.0 - 2021-02-02
====================

Added
-----
* Support for checking if a contact for Exadata infrastructure is valid in My Oracle Support in the Database service
* Support for checking if Exadata infrastructure is in a degraded state in the Database service
* Support for updating the operating system on a VM cluster in the Database service
* Support for external databases in the Database service
* Support for uploading objects to the infrequent access storage tier in the Object Storage service
* Support for changing the storage tier of existing objects in the Object Storage service
* Support for private templates in the Resource Manager service
* Support for multiple encryption domains on IPSec tunnels in the Networking service

Breaking
--------
* Attribute `vnic_id` in response model `Ipv6` changed from required to optional in the Networking service

====================
2.29.0 - 2021-01-26
====================

Added
-----
* Support for creating, managing, and using asymmetric keys in the Key Management service
* Support for peer ACD unique names in Exadata Cloud at Customer in the Database service
* Support for ACLs on autonomous databases in Exadata Cloud at Customer Data Guard in the Database service
* Support for drift detection on individual resources of a stack in the Resource Manager service
* Support for private access channels and vanity URLs in the Analytics Cloud service
* Support for updating load balancer shapes in the Blockchain Platform service
* Support for assigning volume backup policies to volume groups in the Block Volume service

Breaking
--------
* Parameter `idcs_access_token` in model `CreateBlockchainPlatformDetails` changed from optional to required in the Blockchain service

====================
2.28.0 - 2021-01-19
====================

Added
-----
* Support for Logging Analytics as a target in the Service Connector Hub service
* Support for lookups, agent collection warnings, task commands, and data archive/recall in the Logging Analytics service

Fixed
-----
* Fixed a bug in the endpoint used for the Management Dashboard service

Breaking
--------
* A new required property `kind` is added to the models `UpdateScheduledTaskDetails` and `ScheduledTask` in the Log Analytics service
* The allowed values for parameter `sort_by` are restricted for methods `list_meta_source_types`, `list_parser_functions`, `list_parser_meta_plugins`, `list_source_label_operators`, `list_source_meta_functions` in the Log Analytics service. For more information please see the documentation for `LogAnalyticsClient <https://docs.oracle.com/en-us/iaas/tools/python/latest/api/log_analytics/client/oci.log_analytics.LogAnalyticsClient.html#loganalyticsclient>`_

====================
2.27.0 - 2021-01-12
====================

Added
-----
* Support for auto-scaling in the Big Data service
* Documentation fixes for the Logging Search service

Breaking
--------
* Removed `LIFECYCLE_STATE_UPDATING_INFRA` from model BdsInstance in the Big Data service
* Removed `LIFECYCLE_STATE_STOPPING` and `LIFECYCLE_STATE_STARTING` from model Node in the Big Data Service

====================
2.26.0 - 2020-12-15
====================

Added
-----
* Support for filtering listKeys based on KeyShape in KeyManagement service
* Support for the Oracle Roving Edge Infrastructure service
* Support for flexible ShapeDetails in Load Balancer service
* Support for listing of harvested Rules, additional filtering for Logical Entity list calls in Data Catalog service
* Support second level domain for audit SDK
* Support for listing flex components in Database service
* Support for APEX service for ADBS on OCI console for Database service
* Support for Customer-Managed Key features as a part of the Database service
* Support for Github configuration source provider as part of the Resource Manager service

Breaking
--------
* Removed deprecated create_autonomous_data_warehouse API from Database service
* Removed deprecated create_autonomous_data_warehouse_backup API from Database service
* Removed deprecated delete_autonomous_data_warehouse API from Database service
* Removed deprecated generate_autonomous_data_warehouse_wallet API from Database service
* Removed deprecated get_autonomous_data_warehouse API from Database service
* Removed deprecated get_autonomous_data_warehouse_backup API from Database service
* Removed deprecated list_autonomous_data_warehouse_backups API from Database service
* Removed deprecated list_autonomous_data_warehouses API from Database service
* Removed deprecated restore_autonomous_data_warehouse API from Database service
* Removed deprecated start_autonomous_data_warehouse API from Database service
* Removed deprecated stop_autonomous_data_warehouse API from Database service
* Removed deprecated update_autonomous_data_warehouse API from Database service
* The enum attributes `lifecycle_state` and `license_model` from Model `AutonomousDataWarehouseSummary` in the Database service raise `ValueError` if they receive an invalid value. In the earlier versions, the value defaults to `UNKNOWN_ENUM_VALUE`.
* The enum attributes `lifecycle_state` and `license_model` from Model `AutonomousDataWarehouse` in the Database service raise `ValueError` if they receive an invalid value. In the earlier versions, the value defaults to `UNKNOWN_ENUM_VALUE`.

Fixed
-----
* Fixed an issue in the documentation where model links were incorrect

====================
2.25.1 - 2020-12-08
====================

Added
-----
* Support for Integration Service custom endpoint feature
* Support for metadata field in IdentityProvider Get and List response
* Support for fine-grained data analysis and improved SQL insights
* Support for ADB Dedicated - ORDS and SSL cert rotation at AEI
* Support for Maintenance Schedule feature for Exadata Infrastructure resources for ExaCC

====================
2.25.0 - 2020-12-01
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the sa-santiago-1 region
* Support for peer and OSN resources, as well as retry tokens, in the Blockchain Platform service
* Support for getting the availability status of management agents in the Management Agent service
* Support for the on-prem-connector resource type in the Data Safe service
* Support for service channels in the MySQL Database service
* Support for getting the creation type of backups, and for filtering backups by creation type in the MySQL Database service

Breaking
--------
* Parameter `compartment_id` changed from optional to required for method `list_work_requests` in the Data Safe service
* Return type of method `create_data_safe_private_endpoint` changed from `None` to `oci.data_safe.models.DataSafePrivateEndpoint` in the Data Safe service
* Parameters `freeform_tags` and `defined_tags` are removed from model `EnableDataSafeConfigurationDetails` in the Data Safe service

====================
2.24.1 - 2020-11-24
====================

Added
-----
* Provide example for pagination that creates a *Details object for pagination
* Provide example to turn response and model to JSON

Security
-----
* cryptography pinning to cryptography=3.2.1 to address vulnerability `Github security alerts <https://github.com/oracle/oci-python-sdk/pull/299>`__

====================
2.24.0 - 2020-11-17
====================

Added
-----
* Support for specifying memory for AMD E3 shapes during node pool creation and update in the Container Engine for Kubernetes service
* Support for upgrading a database on a VM database system in the Database service
* Support for listing autonomous database clones in the Database service
* Support for Data Guard with autonomous container databases on Exadata Cloud at Customer in the Database service
* Support for getting the last login time of a user in the Identity service
* Support to bulk editing tags on resources in the Identity service

Breaking
--------
* The models `AgentUpload`, `Attribute`, `CreateNamespaceDetails`, `FieldMap`, `GenerateAgentObjectNameDetails`, `LogAnalytics`, `LogAnalyticsCollectionWarning`, `LogAnalyticsSummary`, `OutOfBoxEntityTypeDetails`, `Query`, `QueryWorkRequestResource`, `RegisterEntityTypesDetails`, `ServiceTenancy`, `StringListDetails` are removed from the Log Analytics service
* The enum `name` removed value `CUSLTER_SPLIT` and added `CLUSTER_SPLIT` in the Log Analytics service
* The value for enum `status` is not validated against allowed values and will not raise `ValueError` in the Container Engine service

====================
2.23.5 - 2020-11-10
====================

Added
-----
* Support for the 21C autonomous database version in the Database service
* Support for creating a Data Guard association with a standby database from a database software image in the Database service
* Support for specifying a TDE wallet password when creating a database or database system in the Database service
* Support for enabling access control lists for autonomous databases on Exadata Cloud At Customer in the Database service
* Support for private DNS resolvers, resolver endpoints, and views in the DNS service
* Support for getting a VCN and resolver association in the Networking service
* Support for additional parameters when updating subnets and VLANs in the Networking service
* Support for analytics clusters (database accelerators) in the MySQL Database service
* Support for migrations to Java Cloud Service and Oracle Weblogic Server instances that use existing databases in the Application Migration service
* Support for specifying reserved IPs when creating load balancers in the Load Balancing service

Changed
-------
* Removed support for Python 3.5, since it is end of life
* Support for Python 3.7, 3.8 and 3.9

====================
2.23.4 - 2020-11-03
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the uk-cardiff-1 region
* Support for the Organizations service
* Support for the Optimizer service
* Support for tenancy ID and name on responses in the Usage service
* Support for object versioning in object lifecycle management in the Object Storage service
* Support for specifying a syslog URL for applications in the Functions service
* Support for creation of always-free NoSQL database tables in the NoSQL Database service

====================
2.23.3 - 2020-10-29
====================

Fixed
-------
* Fixed an issue where `UploadManager.upload_stream()` raised `MultipartUploadError` if the time to upload is greater than the read timeout. Please see `github issue #300 <https://github.com/oracle/oci-python-sdk/issues/300>`_ for more details.

====================
2.23.2 - 2020-10-27
====================

Added
-----
* Support for the Compute Instance Agent service
* Support for key store resources and operations in the Database service
* Support for specifying a key store when creating autonomous container databases in the Database service

Fixed
-------
* Bypassed the use of PyOpenSSL in the vendored requests library only if ssl does not have SNI. This may fix a `known issue <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/known-issues.html#uploadmanager-generates-ssl3-write-pending-error-when-a-read-timeout-is-set-for-the-object-storage-client>`_. depending on your environment. For more information, please see the link to the docs.

====================
2.23.1 - 2020-10-20
====================

Added
-----
* Support for the Operations Insights service
* Support for updating autonomous databases to enable/disable Operations Insights service integration, in the Database service
* Support for the NEEDS_ATTENTION lifecycle state on database systems in the Database service
* Support for HCX in the VMware Solutions service
* Added an example script for Usage API

====================
2.23.0 - 2020-10-13
====================

Added
-----
* Support for API definitions in the API Gateway service
* Support for pattern-based logical entities, namespace-bound custom properties, and faceted search in the Data Catalog service
* Support for autonomous Data Guard on autonomous infrastructure in the Database service
* Support for creating a Data Guard association on an existing standby database home in the Database service
* Support for upgrading cloud VM cluster grid infrastructure in the Database service

Breaking
--------
* Attribute `is_quick_start` in models `CreateLogSavedSearchDetails`, `LogSavedSearchSummary` and `LogSavedSearch` is removed from the Logging Management service
* Lifecycle State `DELETED` is removed from the Logging Management service

====================
2.22.0 - 2020-10-06
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the me-dubai-1 region
* Support for rotating keys on autonomous container databases and autonomous databases in the Database service
* Support for cloud Exadata infrastructure and cloud VM clusters in the Database service
* Support for controlling the display of tax banners in the Marketplace service
* Support for application references, patch changes, generic JDBC and MySQL data asset types, and publishing tasks to OCI Dataflow in the Data Integration service
* Support for disabling the legacy Instance Metadata endpoints v1 in the Compute service
* Support for instance configurations specifying instance options in the Compute Management service

Breaking
--------
* The attribute `model_type` in `TypedObject` model now raises `ValueError` when provided with an invalid value. Please see the `documentation <https://docs.cloud.oracle.com/en-us/iaas/tools/python/2.21.6/api/data_integration/models/oci.data_integration.models.TypedObject.html#oci.data_integration.models.TypedObject.model_type>`_ for a list of allowed values.

====================
2.21.6 - 2020-09-29
====================

Added
-----
* Support for specifying custom content dispositions when downloading objects in the Object Storage service
* Support for the “bring your own IP address” feature in the Virtual Networking service
* Support for updating the tags of instance console connections in the Compute service
* Support for custom SSL certificates on gateways in the API Gateway service

====================
2.21.5 - 2020-09-22
====================

Added
-----
* Support for software keys in the Key Management service
* Support for customer contacts on Exadata Cloud at Customer in the Database service
* Support for updating open modes and permission levels of autonomous databases in the Database service
* Support for flexible memory on VM instances in the Compute and Compute Management services

====================
2.21.4 - 2020-09-15
====================

Added
-----
* Support for the Cloud Guard service
* Support for specifying desired consumption models when creating instances in the Integration service
* Support for dynamic shapes in the Load Balancing service

====================
2.21.3 - 2020-09-08
====================

Added
-----
* Support for Logging Service
* Support for Logging Analytics Service
* Support for Logging Search Service
* Support for Logging Ingestion Service
* Support for Management Agent Cloud Service
* Support for Management Dashboard Service
* Support for Service Connector Hub service
* Support for Policy based Request/Response transformation in the API Gateway Service
* Support for sending diagnostic interrupt to a VM instance in the Compute Service
* Support for custom Database Software Images in the Database Service
* Support for getting and listing container database patches for Autonomous Container Database resources in the Database Service
* Support for updating patch id on maintenance run for Autonomous Container Database resources in the Database Service
* Support for searching Oracle Cloud resources across tenancies in the Search Service
* Documentation update for Logging Policies in the API Gateway service
* Support for Python SDK in Cloud Shell

====================
2.21.1 - 2020-08-18
====================

Added
-----
* Support for custom boot volume size and other node pool updates in the Container Engine for Kubernetes service
* Support for Data Guard on Exadata Cloud at Customer VM clusters in the Database service
* Support for stopping VM instances after scheduled maintenance or hypervisor reboots in the Compute service
* Support for creating and managing private endpoints in the Data Flow service

====================
2.21.1 - 2020-08-18
====================

Added
-----
* Support for custom boot volume size and other node pool updates in the Container Engine for Kubernetes service
* Support for Data Guard on Exadata Cloud at Customer VM clusters in the Database service
* Support for stopping VM instances after scheduled maintenance or hypervisor reboots in the Compute service
* Support for creating and managing private endpoints in the Data Flow service

====================
2.21.0 - 2020-08-11
====================

Added
-----
* Support for autonomous json databases in the Database service
* Support for cleaning up uncommitted multipart uploads in the Object Storage service
* Support for additional list API filters in the Data Catalog service

Breaking
--------
* Some unusable region enums were removed from the Support Management service
* Parameter `opc_retry_token` was removed from the Support Management service

====================
2.20.0 - 2020-08-04
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the uk-gov-cardiff-1 region
* Support for creating and managing private endpoints in the Data Flow service
* Support for changing instance shapes and restarting nodes in the Big Data service
* Support for additional versions (for example CSQL) in the Big Data service
* Support for creating stacks from compartments in the Resource Manager service

Breaking
--------
* Param `life_cycle_details` renamed to `lifecycle_details` in models `BlockchainPlatformByHostname` and `BlockchainPlatformSummary` in the Blockchain service

Changed
-------
* Restricted `pyOpenSSL` dependency to versions between 17.5.0 and 19.1.0, both inclusive. See `#255 <https://github.com/oracle/oci-python-sdk/issues/255>`_ for details.

====================
2.19.0 - 2020-07-28
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the us-sanjose-1 region
* Support for updating the fault domain and launch options of VM instances in the Compute service
* Support for image capability schemas and schema versions in the Compute service
* Support for 'Patch Now' maintenance runs for autonomous Exadata infrastructure and autonomous container database resources in the Database service
* Support for automatic performance and cost tuning on volumes in the Block Storage service

Breaking
--------
* Removed the accessToken field from the GitlabAccessTokenConfigurationSourceProvider model in the Resource Manager service

====================
2.18.1 - 2020-07-21
====================

Added
-----
* Support for license types on instances in the Content and Experience service

Fixed
-----
* Fixed a bug for Resource Principal authentication where RPST token was not getting refreshed correctly.

====================
2.18.0 - 2020-07-14
====================

Added
-----
* Support for the Blockchain service
* Support for failing over an autonomous database that has Data Guard enabled in the Database service
* Support for switching over an autonomous database that has Data Guard enabled in the Database service
* Support for git configuration sources in the Resource Manager service
* Support for optionally specifying a VCN id on list operations of DHCP options, subnets, security lists, route tables, internet gateways, and local peering gateways in the Networking service

Fixed
-----
* Fixed a bug where user-set timeout values were not being passed to base client from service client and remained `None`. This has been fixed in all clients except the upload manager and multipart object assembler.

Breaking
--------
* Parameter `vcn_id` changed from required to optional in methods `list_dhcp_options`, `list_local_peering_gateways`, `list_route_tables`, `list_security_lists`, `list_subnets` and `list_internet_gateways` in the virtual network client. If the VCN ID is not provided, then the list includes information of all VCNs in the specified compartment.
* For upload manager and multipart object assembler, the timeout for the object storage client is overwritten to `None` for all operations which call object storage. For this reason, the operations are NOT thread-safe, and you should provide the class with its own Object Storage client that isn't used elsewhere.

====================
2.17.2 - 2020-07-07
====================

Added
-----
* Support for registering and deregistering autonomous dedicated databases with Data Safe in the Database service
* Support for switching between non-private-endpoints and private endpoints on autonomous databases in the Database service
* Support for returning group names when listing identity provider groups in the Identity service
* Support for server-side object re-encryption in the Object Storage service
* Support for private endpoint (ingress) and public endpoint whitelisting in the Analytics Cloud service

====================
2.17.1 - 2020-06-30
====================

Added
-----
* Support for the Usage service
* Support for the VMware Provisioning service
* Support for applying one-off patches to databases in the Database service
* Support for layer-2 virtualization features on vlans in the Networking service
* Support for all AttachVolumeDetails and ParavirtualizedAttachVolumeDetails properties on instance configurations in the Compute Management service
* Support for setting HTTP header size and allowing invalid characters in HTTP request headers in the Load Balancing service
* Support for enabling/disabling HTTP logging. Please see https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/logging.html

====================
2.17.0 - 2020-06-23
====================

Added
-----
* Support for the Data Integration service
* Support for updating database home IDs on databases in the Database service
* Support for backing up autonomous databases on Cloud at Customer in the Database service
* Support for managing autonomous VM clusters on Cloud at Customer in the Database service
* Support for accessing data assets via private endpoints in the Data Catalog service
* Support for dependency archive zip files to be specified for use by applications in the Data Flow service

Breaking
--------
* Attribute `lifecycle_state` in the Data Catalog service has restricted values to "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"
* Attribute `workflow_status` in the Data Catalog service has restricted values to "NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"
* Attribute `schedule_type` in the Data Catalog service has restricted values to "SCHEDULED", "IMMEDIATE"
* Attribute `job_type` in the Data Catalog service has restricted values to "HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE"
* Attribute `harvest_status` in the Data Catalog service has restricted values to "COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED"

====================
2.16.1 - 2020-06-16
====================

Added
-----
* Support for creating a new database from an existing database based on a given timestamp in the Database service
* Support for enabling archive log backups of databases in the Database service
* Support for returning the database version on autonomous container databases in the Database service
* Support for the new DNS format of the Data Transfer service
* Support for scheduled autoscaling, which allows for scaling actions triggered at particular times based on CRON expressions, in the Compute Autoscaling service
* Support for filtering of list APIs for groups, identity providers, identity provider groups, compartments, dynamic groups, network sources, policies, and users by name or lifecycle state in the Identity Service

====================
2.16.0 - 2020-06-09
====================

Added
-----
* Support for returning the database version of backups in the Database service
* Support for patching on Exadata Cloud at Customer resources in the Database service
* Support for new lifecycle substates on instances in the Digital Assistant service
* Support for file servers in the Integration service
* Support for deleting non-empty tag namespaces and bulk deleting tags in the Identity service
* Support for bulk move and bulk delete of resources by compartment in the Identity service

Breaking
--------
* Data type for paramater `data_storage_size_in_tbs` changed from int to float in the Database service
* Parameter `lifecycle_state` removed state `OFFLINE` and added `DISCONNECTED` in the Database service

====================
2.15.0 - 2020-06-02
====================

Added
-----
* Support for optionally supplying a signature when deleting an agreement in the Marketplace service
* Support for launching paid listings in non-US regions in the Marketplace service
* Support for returning the image id of packages in the Marketplace service
* Support for calling Oracle Cloud Infrastructure services in the ap-chuncheon-1 region
* Support for authenticating via Resource Principals. An example of how to use resource principals is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/resource_principals_example.py>`__

Fixed
-----
* Fixed a bug where `oci.waiter.wait_until()` was not invoking `wait_callback` correctly based on the resource property
* Fixed a bug in `ExponentialBackoffWithFullJitterRetryStrategy.do_sleep()` where it was assuming time in milliseconds but it should be seconds

Breaking
--------
* Field `signature` in `delete_accepted_agreement_id` from Marketplace Service changed from required to optional

====================
2.14.3 - 2020-05-19
====================

Added
-----
* Support for returning the private IP of a private endpoint database in the Database service
* Support for native JWT validation in the API Gateway service

====================
2.14.2 - 2020-05-12
====================

Added
-----
* Support for drift detection in the Resource Manager service

====================
2.14.1 - 2020-05-05
====================

Added
-----
* Support for updating the license type of database systems in the Database service
* Support for updating the version of 19c autonomous databases in the Database service
* Support for backup and restore functionality in the Key Management service
* Support for reports in the Marketplace service
* Support for calling Oracle Cloud Infrastructure services in the ap-hyderabad-1 region
====================
2.14.0 - 2020-04-28
====================

Added
-----
* Support for the MySQL Database service
* Support for updating the database home of a database in the Database service
* Support for government regions in the Marketplace service
* Support for starting and stopping instances in the Integration service
* Support for installing Windows updates in the OS Management service

Breaking
--------
* Deleted models ErrataId, ManagedInstanceUpdateDetails and UpdatablePackageSummary from the os_management service

====================
2.13.0 - 2020-04-21
====================

Added
-----
* Support for the Data Safe service
* Support for the Incident Management service
* Support for showing which database versions support always-free in the Database service
* Support in instance configurations for flex shapes, dedicated VM hosts, encryption in transit, and KMS keys in the Compute Autoscaling service
* Support for server-side object encryption using a customer-provided encryption key in the Object Storage service
* Support for specifying maintenance preferences while launching and updating Exadata Database systems in the Database service
* Support for flexible-shaped VM instances in the Compute service
* Support for scheduled cross-region backups in the Block Volume service
* Support for object versioning in the Object Storage service

Breaking
--------
* Deleted models Archiver, CreateArchiverDetails and UpdateArchiverDetails from the streaming service

====================
2.12.4 - 2020-04-14
====================

Added
-----
* Support for access types on instances in the Content and Experience service
* Support for identity contexts in the Search service
* Support for Client Side Encryption: https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/clientsideencryption.htm
* Support for retries on Python built-in `ConnectionError <https://docs.python.org/3/library/exceptions.html#ConnectionError>`__

====================
2.12.3 - 2020-04-07
====================

Added
-----
* Support for changing compartments of runs and applications in the Data Flow service
* Support for getting usage information in the Key Management Vault service
* Support for custom Key Management service endpoints and private endpoints on stream pools in the Streaming service
* Fixed kms_example and added secrets examples

====================
2.12.2 - 2020-03-31
====================

Added
-----
* Support for the Secrets Management service
* Support for the Big Data service
* Support for updating class name, file URI, language, and spark version of applications in the Data Flow service
* Support for cross-region replication in the Object Storage service
* Support for retention rules in the Object Storage service
* Support for enabling and disabling pod security policy admission controllers in the Container Engine for Kubernetes service

====================
2.12.1 - 2020-03-24
====================

Added
-----
* Support for Web Application Acceleration and Security configurations on instances in the Content and Experience service
* Support for shared database homes on Exadata Cloud at Customer resources in the Database service
* Support for Exadata database creation from backup in the Database service
* Support for conditions on JavaScript challenges, new action types on access rules, new policy configuration settings, exclusions on custom protection rules, and IP address lists on IP whitelists in the Web Application Acceleration and Security service

====================
2.12.0 - 2020-03-17
====================

Added
-----
* Support for serial console connections in the Database service
* Support for preview database versions in the Database service
* Support for node reboot migration maintenance status and maintenance windows in the Database service
* Support for using instance metadata API v2 for instance principals authentication
* Upgraded configparser dependency version

Breaking
--------
* Deleted model autonomous_exadata_infrastructure_maintenance_window.py from the database service

====================
2.11.0 - 2020-03-10
====================

Added
-----
* Support for Events service integration with alerts in the Budgets service

Breaking
--------
* The parameters sort_by and lifecycle_state type from Budget service are changed from str to enum

====================
2.10.7 - 2020-03-03
====================

Added
-----
* Support for updating the shape of a Database System in the Database service
* Support for generating CPE configurations for download in the Networking service
* Support for private IPs and fault domains of cluster nodes in the Container Engine for Kubernetes service
* Support for calling Oracle Cloud Infrastructure services in the ca-montreal-1 region
* Fixed missed parameter when invoking request signing for delegation token

====================
2.10.6 - 2020-02-25
====================

Added
-----
* Support for restarting autonomous databases in the Database service
* Support for private endpoints on autonomous databases in the Database service
* Support for IP-based policies in the Identity service
* Support for management of OAuth 2.0 client credentials in the Identity service
* Support for OCI Functions as a subscription protocol in the Notifications service

====================
2.10.5 - 2020-02-18
====================

Added
-----
* Support for the NoSQL Database service
* Support for filtering database versions by storage management type in the Database service
* Support for specifying paid listing types within pricing models in the Marketplace service
* Support for primary and non-primary instance types in the Content and Experience service

====================
2.10.4 - 2020-02-11
====================

Added
-----
* Support for listing supported database versions for Autonomous Database Serverless, and selecting a version at provisioning time in the Database service
* Support for TCP proxy protocol versions on listener connection configurations in the Load Balancer service
* Support for calling the Notifications service in alternate realms
* Support for calling Oracle Cloud Infrastructure services in the eu-amsterdam-1 and me-jeddah-1 regions

====================
2.10.3 - 2020-02-04
====================

Added
-----
* Support for the Data Science service
* Support for calling Oracle Cloud Infrastructure services in the ap-osaka-1 and ap-melbourne-1 regions

====================
2.10.2 - 2020-01-28
====================

Added
-----
* Support for the Application Migration service
* Support for the Data Flow service
* Support for the Data Catalog service
* Support for cross-shape Data Guard in the Database service
* Support for offline data export in the Data Transfer service

====================
2.10.1 - 2020-01-21
====================

Added
-----
* Support for getting DRG redundancy status in the Networking service
* Support for cloning autonomous databases from backups in the Database service

====================
2.10.0 - 2020-01-14
====================

Added
-----
* Support for a description field on route rules and security rules in the Networking service
* Support for starting and stopping Digital Assistant instances in the Digital Assistant service
* Support for shared database homes on Exadata, bare metal, and virtual machine instances in the Database service
* Support for tracking a number of Database service operations through the Work Requests service

Breaking
--------
* Field `db_home_id` in `list_databases` from database service is changed from required to optional

====================
2.9.0 - 2020-01-07
====================

Added
-----
* Support for optionally specifying the corporate proxy field when creating Exadata infrastructure in the Database service
* Support for maintenance windows, and rescheduling maintenance runs, on autonomous container databases in the Database service
* Provide example on how to use key_content for python SDK configuration

Breaking
--------
* Field `host_name` in `NodeDetails` from database service is changed from optional to required

====================
2.8.0 - 2019-12-17
====================

Added
-----
* Support for the API Gateway service
* Support for the OS Management service
* Support for the Marketplace service
* Support for "default"-type vaults in the Key Management service
* Support for bringing your own keys in the Key Management service
* Support for cross-region backups of boot volumes in the Block Storage service
* Support for top-level TSIG keys in the DNS service
* Support for resizing virtual machine instances to different shapes in the Compute service
* Support for management configuration of cloud agents in the Compute service
* Support for launching node pools using image IDs in the Container Engine for Kubernetes service

Breaking
--------
* Removed support for v1 auth tokens in kubeconfig files in the `CreateClusterKubeconfigContentDetails` class of the Container Engine for Kubernetes service
* Removed the IDCS access token requirement on the delete deleteOceInstance operation in the Content and Experience service, which is why the `DeleteOceInstanceDetails` class was removed
* Set `compartment_id` as a required parameter in `list_stream_pools` for streaming service

====================
2.7.1 - 2019-12-10
====================

Added
-----
* Support for etags on results of the List Objects API in the Object Storage service
* Support for OCIDs on buckets in the Object Storage service
* Support for content-disposition and cache-control headers on objects in the Object Storage service
* Support for recovering deleted compartments in the Identity service
* Support for sharing volumes across multiple instances in the Block Storage service
* Support for connect harnesses and stream pools in the Streaming service
* Support for associating file storage mount targets with network security groups in the File Storage service
* Support for calling Oracle Cloud Infrastructure services in the uk-gov-london-1 region
* Add default connection timeout(10s) and read timeout(60s) for Python SDK client
* Add contents table to client documentation
* Fix the issue of the second style of pagination

====================
2.7.0 - 2019-11-26
====================

Added
-----
* Support for maintenance windows on autonomous databases in the Database service
* Support for getting the compute units (OCPUs) of an Exadata autonomous transaction processing - dedicated resource in the Database service

Breaking changes
----
* Create database home from VM_CLUSTER_BACKUP is removed from Database Service

====================
2.6.5 - 2019-11-19
====================

Added
-----
* Support for four-byte autonomous system numbers (ASNs) on FastConnect resources in the Networking service
* Support for choosing fault domains when creating instance pools in the Compute service
* Support for allowing connections from only specific VCNs to autonomous data warehouse and autonomous transaction processing instances in the Database service
* Support for Streaming Client Non-Regional

====================
2.6.4 - 2019-11-12
====================

Added
-----
* Support for access to APEX and SQL Dev features on autonomous transaction processing and autonomous data warehouse resources in the Database service
* Support for registering / deregistering autonomous transaction processing and autonomous data warehouse resources with Data Safe in the Database service
* Support for redirecting HTTP / HTTPS request URIs to different URIs in the Load Balancing service
* Support for specifying compartments on options APIs in the Container Engine for Kubernetes service
* Support for volume performance units on block volumes in the Block Storage service

====================
2.6.3 - 2019-11-05
====================

Added
-----
* Support for the Analytics Cloud service
* Support for the Integration Cloud service
* Support for IKE versions in IPSec connections in the Virtual Networking service
* Support for getting a stack's Terraform state in the Resource Manager service

====================
2.6.2 - 2019-10-29
====================

Added
-----
* Support for wallet rotation operations on Autonomous Databases in the Database service
* Support for adding and removing image shape compatibility entries in the Compute service
* Support for managing redirects in the Web Application Acceleration and Security service
* Support for migrating zones from the Dyn HTTP Redirect Service to Oracle Cloud Infrastructure in the DNS service

====================
2.6.1 - 2019-10-15
====================

Added
-----
* Support for the Digital Assistant service
* Support for work requests on Instance Pool operations in the Compute service

====================
2.6.0 - 2019-10-08
====================

Added
-----
* Support for the new schema for events in the Audit service
* Support for entitlements in the Data Transfer service
* Support for custom scheduled backup policies on volumes in the Block Storage service
* Support for specifying the network type when launching virtual machine instances in the Compute service
* Support for Monitoring service integration in the Health Checks service

Breaking
--------
* The tenant_id parameter is now id (Id of the Transfer Application Entitlement) for get_transfer_appliance_entitlement in TransferApplianceEntitlementClient
* The topic_attributes_details parameter is now required for update_topic in NotificationControlPlaneClient
* The Audit service version was bumped to 20190901, use older version of Python SDK for Audit service version 20160918

====================
2.5.2 - 2019-10-01
====================

Added
-----
* Support for required tags in the Identity service
* Support for work requests on tagging operations in the Identity service
* Support for enumerated tag values in the Identity service
* Support for moving dynamic routing gateway resources across compartments in the Networking service
* Support for migrating zones from Dyn managed DNS to OCI in the DNS service
* Support for fast provisioning for virtual machine databases in the Database service

====================
2.5.1 - 2019-09-24
====================

Added
-----
* Support for selecting the Terraform version to use in the Resource Manager service
* Support for bucket re-encryption in the Object Storage service
* Support for enabling / disabling bucket-level events in the Object Storage service

====================
2.5.0 - 2019-09-17
====================

Added
-----
* Support for importing state files in the Resource Manager service
* Support for Exadata Cloud at Customer in the Database service
* Support for free tier resources and system tags in the Load Balancing service
* Support for free tier resources and system tags in the Compute service
* Support for free tier resources and system tags in the Block Storage service
* Support for free tier and system tags on autonomous databases in the Database service

Breaking
--------
* The availability_domain parameter is now a kwarg for list_db_system_shapes in DatabaseClient
* The model CreateDbHomeWithDbSystemIdBase was renamed CreateDbHomeBase and the parameter db_system_id was removed
* The parameter create_db_home_with_db_system_id_details for create_db_home in DatabaseClient changed from CreateDbHomeWithDbSystemIdBase to CreateDbHomeBase

====================
2.4.0 - 2019-09-10
====================

Added
-----
* Support for specifying the autoBackupWindow field for scheduling backups in the Database service
* Support for network security groups on autonomous Exadata infrastructure in the Database service
* Support for Kubernetes secrets encryption in customer clusters, regional subnets, and cluster authentication for instance principals in the Container Engine for Kubernetes service
* Support for the Oracle Content and Experience service

Breaking
--------
* The etag header has been removed from the response for NotificationControlPlaneClient.change_topic_compartment and NotificationDataPlaneClient.change_subscription_compartment

====================
2.3.3 - 2019-09-03
====================

Added
-----
* Support for the Sydney (SYD) region
* Support for managing cluster networks in the Compute Autoscaling service
* Support for tracking asynchronous operations via work requests in the Database service

====================
2.3.2 - 2019-08-27
====================

Added
-----
* Support for the Sao Paulo (GRU) region
* Support for dedicated virtual machine hosts in the Compute service
* Support for resource groups in metrics and alarms in the Monitoring service

====================
2.3.1 - 2019-08-20
====================

Added
-----
* Support for the Limits service
* Support for archiving to Object Storage in the Streaming service
* Support for etags on resources in the Streaming service
* Support for Key Management service (KMS) encryption of file systems in the File Storage service
* Support for moving public IP, DHCP, local peering gateway, internet gateway, network security group, and DRG attachment resources across compartments in the Networking service
* Support for multi-origin, basic cache, certificate mapping, and OCI Monitoring service integration in the Web Application Acceleration and Security service

====================
2.3.0 - 2019-08-13
====================

Added
-----
* Support for the Data Transfer service
* Support for the Zurich (ZRH) region

Breaking
--------
* oci.waas.WafLog.timestamp type changed from str to datetime
* oci.waas.models.Certificate.issuer_name type changed from oci.waas.models.CertificateSubjectName to oci.waas.models.CerticateIssuerName
* `"PURGE_WAAS_POLICY"` removed as option for oci.waas.models.WorkRequest.operation_type
* `"PURGE_WAAS_POLICY"` removed as option for oci.waas.models.WorkRequestSummary.operation_type

====================
2.2.21 - 2019-08-06
====================

Added
-----
* Support for IPv6 load balancers in the Load Balancing service
* Support for IPv6 on VCN and FastConnect resources in the Networking service

====================
2.2.20 - 2019-07-30
====================

Added
-----
* Support for the Mumbai (BOM) region
* Support for the Events service
* Support for moving streams across compartments in the Streaming service
* Support for moving FastConnect resources across compartments in the Networking service
* Support for moving policies across compartments in the Web Application Acceleration and Security service
* Support for tagging FastConnect resources in the Networking service

====================
2.2.19 - 2019-07-23
====================

Added
-----
* Support for moving resources across compartments in the Database service
* Support for moving resources across compartments in the Health Checks service
* Support for moving alarms across compartments in the Monitoring service
* Support for creating instance configurations from running instances in the Compute service
* Support for setting up budget alerts for cost tracking tags in the Budgets service

====================
2.2.18 - 2019-07-16
====================

Added
-----
* Support for the Functions service
* Support for the Quotas service
* Support for moving resources across compartments in the DNS service
* Support for moving instances across compartments in the Compute service
* Support for moving keys and vaults across compartments in the Key Management service
* Support for moving topics and subscriptions across compartments in the Notifications service
* Support for moving load balancers across compartments in the Load Balancing service
* Support for specifying permitted REST methods in load balancer rule sets in the Load Balancing service
* Support for configuring cookie session persistence in backend sets in the Load Balancing service
* Support for ACL rules in rule sets in the Load Balancing service
* Support for move compartment tree in the Identity service
* Support for specifying and returning a KMS key in backup operations in the Block Storage service
* Support for transit routing in the Networking service
* Support for authenticating via Resource Principals. An example of how to use resource principals is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/resource_principals_example.py>`__. This authentication method is only supported within the Functions service at this time.

====================
2.2.17 - 2019-07-09
====================

Added
-----
* Support for network security groups in the Load Balancing service
* Support for network security groups in Core Services
* Support for network security groups on database systems in the Database service
* Support for creating autonomous transaction processing and autonomous data warehouse previews in the Database service
* Support for getting the load balancer attachments of instance pools in the Compute service
* Support for moving resources across compartments in the Resource Manager service
* Support for moving VCN resources across compartments in the Networking service

====================
2.2.16 - 2019-07-02
====================

Added
-----
* Support for moving images, instance configurations, and instance pools across compartments in Core Services
* Support for moving autoscaling configurations across compartments in the Compute Autoscaling service

Fixed
-----
* Fixed a bug where the Streaming service's endpoints in Tokyo, Seoul, and future regions were not reachable from the SDK

====================
2.2.15 - 2019-06-25
====================

Added
-----
* Support for moving senders across compartments in the Email service
* Support for moving NAT gateway resources across compartments in Core Services

====================
2.2.14 - 2019-06-18
====================

Added
-----
* Support for moving service gateway resources across compartments in Core Services
* Support for moving block storage resources across compartments in Core Services
* Support for key deletion in the Key Management service

====================
2.2.13 - 2019-06-11
====================

Added
-----
* Support for specifying custom boot volume sizes on instance configurations in the Compute Autoscaling service
* Support for 'Autonomous Transaction Processing - Dedicated' features, as well as maintenance run and backup operations on autonomous databases, autonomous container databases, and autonomous Exadata infrastructure in the Database service

====================
2.2.12 - 2019-06-04
====================

Added
-----
* Support for autoscaling autonomous databases and autonomous data warehouses in the Database service
* Support for specifying fault domains as part of instance configurations in the Compute Autoscaling service
* Support for deleting tag definitions and tag namespaces in the Identity service

Fixed
-----
* Support for regions in realms other than oraclecloud.com in the Load Balancing service

====================
2.2.11 - 2019-05-28
====================

Added
-----
* Support for the Work Requests service, and tracking of a number of Core Services operations through work requests
* Support for emulated volume attachments in Core Services
* Support for changing the compartment of resources in the File Storage service
* Support for tags in list operations in the File Storage service
* Support for returning UI password creation dates in the Identity service

====================
2.2.10 - 2019-05-21
====================

Added
-----
* Support for returning tags when listing instance configurations, instance pools, or autoscaling configurations in the Compute Autoscaling service
* Support for getting the namespace of another tenancy than the caller's tenancy in the Object Storage service
* Support for BGP dynamic routing and providing pre-shared secrets (PSKs) when establishing tunnels in the Networking service

====================
2.2.9 - 2019-05-14
====================

Added
-----
* Support for the Seoul (ICN) region
* Support for logging context fields on data-plane APIs of the Key Management Service
* Support for reverse pagination on list operations of the Email service
* Support for configuring backup retention windows on database backups in the Database service
* Support for subscribed regions in stop_untagged_instances.py on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/stop_untagged_instances.py>`__.
* New services to showoci.py on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/showoci/showoci.py>`__.

====================
2.2.8 - 2019-05-07
====================

Added
-----
* Support for the Tokyo (NRT) region
* A sample demonstrating how to find, stop and report on instances that have been improperly tagged is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/stop_untagged_instances.py>`__.
* A sample demonstrating adding and deleting an API key is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/add_API_key.py>`__.
* New services to showoci.py on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/showoci/showoci.py>`__.

Fixed
-----
* Updated example for Streaming service to address issue with encoding in Python 3 is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/stream_example.py>`__.

====================
2.2.7 - 2019-04-16
====================

Added
-----
* Support for tagging dynamic groups in the Identity service
* Support for updating network ACLs and license types for autonomous databases and autonomous data warehouses in the Database service
* Support for editing static routes and IPSec remote IDs in the Virtual Networking service
* An example for reporting details for multiple Oracle Cloud Infrastructure resources is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/showoci/showoci.py>`__.

====================
2.2.6 - 2019-04-09
====================

Added
-----
* Support for etag and if-match headers (for optimistic concurrency control) in the Email service

====================
2.2.5 - 2019-04-02
====================

Added
-----
* Support for provider service key names on virtual circuits in the FastConnect service
* Support for customer reference names on cross connects and cross connect groups in the FastConnect service
* A sample showing how to use Streaming service from the SDK is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/stream_example.py>`__.

====================
2.2.4 - 2019-03-26
====================

Added
-----
* Support for glob patterns and exclusions for object lifecycle management in the Object Storage service
* Documentation enhancements and corrections for traffic management in the DNS service

====================
2.2.3 - 2019-03-19
====================

Added
-----
* Support for specifying metadata on node pools in the Container Engine for Kubernetes service
* Support for provisioning a new autonomous database or autonomous data warehouse as a clone of another in the Database service

Changed
-------
* Updated vendored packages. idna==2.8, PyJWT==1.7.1, requests==2.21.0, six==1.12.0, urllib3==1.24.1, requests==2.21.0

====================
2.2.2 - 2019-03-12
====================

Added
-----
* Support for the Budgets service
* Support for managing multifactor authentication in the Identity service
* Support for managing default tags in the Identity service
* Support for account recovery in the Identity service
* Support for authentication policies in the Identity service
* Support for specifying the workload type when creating autonomous databases in the Database service
* Support for I/O resource management for Exadata database systems in the Database service
* Support for customer-specified timezones on database systems in the Database service

====================
2.2.1 - 2019-02-28
====================

Added
-----
* Support for the Monitoring service
* Support for the Notification service
* Support for the Resource Manager service
* Support for the Compute Autoscaling service
* Support for changing the compartment of a tag namespace in the Identity service
* Support for specifying fault domains in the Database service
* Support for managing instance monitoring in the Compute service
* Support for attaching/detaching load balancers to instance pools in the Compute service

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
