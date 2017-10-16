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
    :members:
    :undoc-members:
    :imported-members:

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
    :members:
    :undoc-members:
    :imported-members:

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
    :members:
    :undoc-members:
    :imported-members:

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
    :members:
    :undoc-members:
    :imported-members:

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
    :members:
    :undoc-members:
    :imported-members:

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

===========
 Utilities
===========

.. module:: oci.util

.. autofunction:: to_dict

.. autoclass:: Sentinel

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

