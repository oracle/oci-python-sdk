.. _dual-stack-endpoints:

Dual-stack Endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some Oracle Cloud Infrastructure (OCI) services are designed to support connectivity using both Internet Protocol version 6 (IPv6) and Internet Protocol version 4 (IPv4). This means that users can access OCI resources over either protocol, ensuring compatibility with modern and legacy network environments. OCI services that support dual-stack endpoints facilitate seamless communication and accessibility for clients utilizing IPv6, IPv4, or both.

OCI Python SDK allows you to enable the use of these dual-stack endpoints application level and at client level. The value set at client level takes precedence over the value set at the application level. This feature is disabled by default.

* To opt-in the dual-stack endpoints feature at application level, set the environment variable ``OCI_DUAL_STACK_ENDPOINT_ENABLED``  to ``true``. The boolean value is case-insensitive.
* To opt-in the dual-stack endpoints feature at client level, set the flag in code as shown below

.. code-block:: pycon

   object_storage = oci.object_storage.ObjectStorageClient(config,
                                                           client_level_dualstack_endpoints_enabled=True)


For example, please refer `enable_dual_stack_endpoint_example.py <https://github.com/oracle/oci-python-sdk/blob/master/examples/enable_dual_stack_endpoint_example.py>`__