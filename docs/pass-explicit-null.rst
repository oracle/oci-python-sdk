.. _pass-explicit-null:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Passing explicit Null/None values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The SDK does not send fields with a value of ``None`` back to the service. In order to send a ``None`` explicitly back to the service - for example if you are trying to clear metadata on a bucket - you can set a field's value to ``oci.util.NONE_SENTINEL``:

.. code-block:: python

    import oci

    update_bucket_details = oci.object_storage.models.UpdateBucketDetails()
    update_bucket_details.metadata = oci.util.NONE_SENTINEL

    object_storage.update_bucket('my_namespace', 'my_bucket', update_bucket_details)
