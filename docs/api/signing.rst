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
using `oci.auth.signers.get_resource_principals_signer`. The returned resource
principals signer can then be used when initializing a client. If the instance
is not configured for Resource Principals this call will raise an
EnvironmentError exception.

.. code-block:: python

    resource_principals_signer = oci.auth.signers.get_resource_principals_signer()
    # A populated config is not needed when using a Resource Principals signer
    db_client = oci.database.DatabaseClient({}, signer=resource_principals_signer)

=========================
OKE Workload Auth Signer
=========================

The OKE Workload Auth Signer is a signer that grants an entire workload (an application running on Kubernetes clusters)
access to OCI resources and services using the OKE Workload Identity. It can be retrieved by
`oci.auth.signers.get_oke_workload_identity_resource_principal_signer`. The retrieved signer can then be used when
initializing a client.

The default path for retrieving the kubernetes service account token is `/var/run/secrets/kubernetes.io/serviceaccount/token`.
If you have a different kubernetes service account token path, use the `service_account_token_path` parameter
while retrieving the signer. If you want to directly pass in your kubernetes service account token, use the
`service_account_token` parameter while retrieving the signer.

.. code-block:: python

    oke_workload_signer = oci.auth.signers.get_oke_workload_identity_resource_principal_signer()

    # If you have a kubernetes service account token path different from the default path then:
    # token_path = "path_to_your_token_file"
    # oke_workload_signer = oci.auth.signers.get_oke_workload_identity_resource_principal_signer(service_account_token_path=token_path)

    # If you want to directly pass in the kubernetes service account token then:
    # token_string = "your_token_string"
    # oke_workload_signer = oci.auth.signers.get_oke_workload_identity_resource_principal_signer(service_account_token=token_string)

    # A populated config is not needed when using the OKE Workload Auth signer
    container_engine_client = oci.container_engine.ContainerEngineClient({}, signer=oke_workload_signer)

===================
Additional Signers
===================

.. automodule:: oci.auth.signers

.. autoclass:: SecurityTokenSigner
      :special-members: __init__
      :members:

.. autoclass:: X509FederationClientBasedSecurityTokenSigner
      :special-members: __init__
      :members:

.. autoclass:: InstancePrincipalsSecurityTokenSigner
      :special-members: __init__
      :members:

.. autoclass:: InstancePrincipalsDelegationTokenSigner
      :special-members: __init__
      :members:

.. autoclass:: ResourcePrincipalsFederationSigner
      :special-members: __init__
      :members:

.. autoclass:: EphemeralResourcePrincipalSigner
      :special-members: __init__
      :members:

============================
X509 Certificate Retrievers
============================

.. automodule:: oci.auth.certificate_retriever

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

.. automodule:: oci.auth.federation_client

.. autoclass:: X509FederationClient
      :special-members: __init__
      :members:

.. automodule:: oci.auth.session_key_supplier

.. autoclass:: SessionKeySupplier
      :special-members: __init__
      :members: