.. _api-reference:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

API Reference
~~~~~~~~~~~~~

=======
 Audit 
=======

--------
 Client
--------

.. autoclass:: oci.audit.audit_client.AuditClient
    :members:

--------
 Models
--------

.. automodule:: oci.audit.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:

===============
 Core Services
===============

---------
 Clients
---------


Block Storage
=============

.. autoclass:: oci.core.blockstorage_client.BlockstorageClient
    :members:

Compute
=======

.. autoclass:: oci.core.compute_client.ComputeClient
    :members:


Virtual Network
===============

.. autoclass:: oci.core.virtual_network_client.VirtualNetworkClient
    :members:

--------
 Models
--------

.. automodule:: oci.core.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:

==========
 Database
==========

--------
 Client
--------

.. autoclass:: oci.database.database_client.DatabaseClient
    :members:

--------
 Models
--------

.. automodule:: oci.database.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:

==========
 Identity
==========

--------
 Client
--------

.. autoclass:: oci.identity.identity_client.IdentityClient
    :members:

--------
 Models
--------

.. automodule:: oci.identity.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:

==============
Load Balancer
==============

--------
 Client
--------

.. autoclass:: oci.load_balancer.load_balancer_client.LoadBalancerClient
    :members:

--------
 Models
--------

.. automodule:: oci.load_balancer.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:

================
 Object Storage
================

--------
 Client
--------

.. autoclass:: oci.object_storage.object_storage_client.ObjectStorageClient
    :members:

--------
 Models
--------

.. automodule:: oci.object_storage.models
    :special-members: __init__
    :members:
    :undoc-members:
    :imported-members:
    :inherited-members:

================
 Upload Manager
================

.. module:: oci.object_storage

.. autoclass:: UploadManager
      :special-members: __init__
      :members:

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

.. autofunction:: from_file

.. autofunction:: validate_config

.. module:: oci.regions

.. autofunction:: is_region

.. autofunction:: endpoint_for


============
 Exceptions
============

.. automodule:: oci.exceptions
    :members:

=========
 Signing
=========

.. module:: oci.signer

.. autofunction:: load_private_key_from_file

.. autofunction:: load_private_key

.. autoclass:: Signer

=====================
 Additional Signers
=====================

.. module:: oci.auth.signers

.. autoclass:: SecurityTokenSigner
      :special-members: __init__
      :members:

.. autoclass:: X509FederationClientBasedSecurityTokenSigner
      :special-members: __init__
      :members:

.. autoclass:: InstancePrincipalsSecurityTokenSigner
      :special-members: __init__
      :members:

============================
X509 Certificate Retrievers
============================

.. module:: oci.auth.certificate_retriever

.. autoclass:: UrlBasedCertificateRetriever
      :special-members: __init__
      :members:

.. autoclass:: PEMStringCertificateRetriever
      :special-members: __init__
      :members:

.. autoclass:: FileBasedCertificateRetriever
      :special-members: __init__
      :members:

====================================
X509 Certificate Federation Client
====================================

.. module:: oci.auth.federation_client

.. autoclass:: X509FederationClient
      :special-members: __init__
      :members:

.. module:: oci.auth.session_key_supplier

.. autoclass:: SessionKeySupplier
      :special-members: __init__
      :members:

===========
 Utilities
===========

.. module:: oci.util

.. autofunction:: to_dict

.. autoclass:: Sentinel

===========
 Waiters
===========

.. module:: oci

.. autofunction:: wait_until

===========
 Pagination
===========

.. module:: oci.pagination

.. autofunction:: list_call_get_all_results
.. autofunction:: list_call_get_up_to_limit
.. autofunction:: list_call_get_all_results_generator
.. autofunction:: list_call_get_up_to_limit_generator

=========
Request
=========
.. module:: oci.request

.. autoclass:: Request
    :members:
    :undoc-members:

=========
Response
=========
.. module:: oci.response

.. autoclass:: Response
    :members:
    :undoc-members:

