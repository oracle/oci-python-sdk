Signing
~~~~~~~~

.. module:: oci.signer

.. autofunction:: load_private_key_from_file

.. autofunction:: load_private_key

.. autoclass:: Signer

===========================
Resource Principals Signer
===========================

On an instance that has Resource Principals enabled, a signer can be retrieved
using oci.auth.signer.get_resource_principals_signer. The returned resource
principals signer can then be used when initializing a client. If the instance
is not configured for Resource Principals this call will raise an
EnvironmentError exception.

.. code-block:: python

    resource_principals_signer = oci.auth.signer.get_resource_principals_signer()
    # A populated config is not needed when using a Resource Principals signer
    db_client = oci.database.DatabaseClient({}, signer=resource_principals_signer)

===================
Additional Signers
===================

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