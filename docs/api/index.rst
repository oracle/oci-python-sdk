.. _api-reference:

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

.. autoclass:: oraclebmc.core.blockstorage_client.BlockstorageClient
    :members:

Compute
=======

.. autoclass:: oraclebmc.core.compute_client.ComputeClient
    :members:


Virtual Network
===============

.. autoclass:: oraclebmc.core.virtual_network_client.VirtualNetworkClient

--------
 Models
--------

.. automodule:: oraclebmc.core.models
    :members:
    :undoc-members:
    :imported-members:

==========
 Identity
==========

--------
 Client
--------

.. autoclass:: oraclebmc.identity.identity_client.IdentityClient
    :members:

--------
 Models
--------

.. automodule:: oraclebmc.identity.models
    :members:
    :imported-members:

================
 Object Storage
================

--------
 Client
--------

.. autoclass:: oraclebmc.object_storage.object_storage_client.ObjectStorageClient
    :members:

--------
 Models
--------

.. automodule:: oraclebmc.object_storage.models
    :members:
    :imported-members:


=============
 Base Client
=============

.. module:: oraclebmc.base_client

.. autoclass:: BaseClient
    :members: call_api, request

========
 Config
========

.. module:: oraclebmc.config

.. autofunction:: from_file

.. autofunction:: validate_config

.. module:: oraclebmc.regions

.. autofunction:: is_region

.. autofunction:: endpoint_for


============
 Exceptions
============

.. automodule:: oraclebmc.exceptions
    :members:

=========
 Signing
=========

.. module:: oraclebmc.signer

.. autofunction:: load_private_key_from_file

.. autofunction:: load_private_key

.. autoclass:: Signer

.. autoclass:: ObjectUploadSigner

===========
 Utilities
===========

.. module:: oraclebmc.util

.. autofunction:: to_dict

.. autoclass:: Sentinel
