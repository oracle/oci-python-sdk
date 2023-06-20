.. _realm-specific-endpoint-template:

Realm Specific Endpoint Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dedicated endpoints are the endpoint templates defined by the service for a specific realm at client level. OCI Python SDK allows you to enable the use of these realm-specific endpoint templates feature at application level and at client level. The value set at client level takes precedence over the value set at the application level. This feature is disabled by default.

* To opt-in the realm-specific endpoint templates feature at application level, set the environment variable ``OCI_REALM_SPECIFIC_SERVICE_ENDPOINT_TEMPLATE_ENABLED``  to ``true``. The boolean value is case-insensitive.
* To opt-in the realm-specific endpoint templates feature at client level, set the flag in code as shown below

.. code-block:: python
   object_storage = oci.object_storage.ObjectStorageClient(config)
   object_storage.base_client.client_level_realm_specific_endpoint_template_enabled = True

For example, please refer `enable_realm_specific_endpoint_example.py <https://github.com/oracle/oci-python-sdk/blob/master/examples/enable_realm_specific_endpoint_example.py>`__