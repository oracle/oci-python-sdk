Signing
~~~~~~~~

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