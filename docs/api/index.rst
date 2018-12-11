.. _api-reference:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Single Page Reference
~~~~~~~~~~~~~~~~~~~~~~


=====
Audit
=====

--------
 Client
--------

.. autoclass:: oci.audit.audit_client.AuditClient
    :members:
    :noindex:

--------
 Models
--------

.. automodule:: oci.audit.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:
    :noindex:


================
Container Engine
================

--------
 Client
--------

.. autoclass:: oci.container_engine.container_engine_client.ContainerEngineClient
    :members:
    :noindex:

--------
 Models
--------

.. automodule:: oci.container_engine.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:
    :noindex:


=============
Core Services
=============

---------
 Clients
---------


Block Storage
=============

.. autoclass:: oci.core.blockstorage_client.BlockstorageClient
    :members:
    :noindex:


Compute
=======

.. autoclass:: oci.core.compute_client.ComputeClient
    :members:
    :noindex:


Compute Management
==================

.. autoclass:: oci.core.compute_management_client.ComputeManagementClient
    :members:
    :noindex:


Virtual Network
===============

.. autoclass:: oci.core.virtual_network_client.VirtualNetworkClient
    :members:
    :noindex:


--------
 Models
--------

.. automodule:: oci.core.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:
    :noindex:


========
Database
========

--------
 Client
--------

.. autoclass:: oci.database.database_client.DatabaseClient
    :members:
    :noindex:

--------
 Models
--------

.. automodule:: oci.database.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:
    :noindex:


===
DNS
===

--------
 Client
--------

.. autoclass:: oci.dns.dns_client.DnsClient
    :members:
    :noindex:

--------
 Models
--------

.. automodule:: oci.dns.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:
    :noindex:


=====
Email
=====

--------
 Client
--------

.. autoclass:: oci.email.email_client.EmailClient
    :members:
    :noindex:

--------
 Models
--------

.. automodule:: oci.email.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:
    :noindex:


============
File Storage
============

--------
 Client
--------

.. autoclass:: oci.file_storage.file_storage_client.FileStorageClient
    :members:
    :noindex:

--------
 Models
--------

.. automodule:: oci.file_storage.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:
    :noindex:


========
Identity
========

--------
 Client
--------

.. autoclass:: oci.identity.identity_client.IdentityClient
    :members:
    :noindex:

--------
 Models
--------

.. automodule:: oci.identity.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:
    :noindex:


==============
Key Management
==============

---------
 Clients
---------


Kms Crypto
==========

.. autoclass:: oci.key_management.kms_crypto_client.KmsCryptoClient
    :members:
    :noindex:


Kms Management
==============

.. autoclass:: oci.key_management.kms_management_client.KmsManagementClient
    :members:
    :noindex:


Kms Vault
=========

.. autoclass:: oci.key_management.kms_vault_client.KmsVaultClient
    :members:
    :noindex:


--------
 Models
--------

.. automodule:: oci.key_management.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:
    :noindex:


=============
Load Balancer
=============

--------
 Client
--------

.. autoclass:: oci.load_balancer.load_balancer_client.LoadBalancerClient
    :members:
    :noindex:

--------
 Models
--------

.. automodule:: oci.load_balancer.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:
    :noindex:


==============
Object Storage
==============

--------
 Client
--------

.. autoclass:: oci.object_storage.object_storage_client.ObjectStorageClient
    :members:
    :noindex:

--------
 Models
--------

.. automodule:: oci.object_storage.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:
    :noindex:


===============
Resource Search
===============

--------
 Client
--------

.. autoclass:: oci.resource_search.resource_search_client.ResourceSearchClient
    :members:
    :noindex:

--------
 Models
--------

.. automodule:: oci.resource_search.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:
    :noindex:


================
 Upload Manager
================

.. module:: oci.object_storage
      :noindex:

.. autoclass:: UploadManager
      :special-members: __init__
      :members:
      :noindex:

=============
 Base Client
=============

.. module:: oci.base_client

.. autoclass:: BaseClient
    :members: call_api, request

========
 Config
========

.. module:: oci.config
    :noindex:

.. autofunction:: from_file
    :noindex:

.. autofunction:: validate_config
    :noindex:

.. module:: oci.regions
    :noindex:

.. autofunction:: is_region
    :noindex:

.. autofunction:: endpoint_for
    :noindex:


============
 Exceptions
============

.. automodule:: oci.exceptions
    :members:
    :noindex:

=========
 Signing
=========

.. module:: oci.signer
    :noindex:

.. autofunction:: load_private_key_from_file
    :noindex:

.. autofunction:: load_private_key
    :noindex:

.. autoclass:: Signer
    :noindex:

=====================
 Additional Signers
=====================

.. module:: oci.auth.signers
      :noindex:

.. autoclass:: SecurityTokenSigner
      :special-members: __init__
      :members:
      :noindex:

.. autoclass:: X509FederationClientBasedSecurityTokenSigner
      :special-members: __init__
      :members:
      :noindex:

.. autoclass:: InstancePrincipalsSecurityTokenSigner
      :special-members: __init__
      :members:
      :noindex:

============================
X509 Certificate Retrievers
============================

.. module:: oci.auth.certificate_retriever
      :noindex:

.. autoclass:: UrlBasedCertificateRetriever
      :special-members: __init__
      :members:
      :noindex:

.. autoclass:: PEMStringCertificateRetriever
      :special-members: __init__
      :members:
      :noindex:

.. autoclass:: FileBasedCertificateRetriever
      :special-members: __init__
      :members:
      :noindex:

====================================
X509 Certificate Federation Client
====================================

.. module:: oci.auth.federation_client
      :noindex:

.. autoclass:: X509FederationClient
      :special-members: __init__
      :members:
      :noindex:

.. module:: oci.auth.session_key_supplier
      :noindex:

.. autoclass:: SessionKeySupplier
      :special-members: __init__
      :members:
      :noindex:

===========
 Utilities
===========

.. module:: oci.util
    :noindex:

.. autofunction:: to_dict
    :noindex:

.. autoclass:: Sentinel
    :noindex:

===========
 Waiters
===========

.. module:: oci
    :noindex:

.. autofunction:: wait_until
    :noindex:

===========
 Pagination
===========

.. module:: oci.pagination
    :noindex:

.. autofunction:: list_call_get_all_results
    :noindex:

.. autofunction:: list_call_get_up_to_limit
    :noindex:

.. autofunction:: list_call_get_all_results_generator
    :noindex:

.. autofunction:: list_call_get_up_to_limit_generator
    :noindex:

=========
Request
=========
.. module:: oci.request
    :noindex:

.. autoclass:: Request
    :members:
    :undoc-members:
    :noindex:

=========
Response
=========
.. module:: oci.response
    :noindex:

.. autoclass:: Response
    :members:
    :undoc-members:
    :noindex: