.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Waiters
~~~~~~~
Sometimes you may need to wait until an attribute of a resource, such as an instance or a VCN, reaches a certain state. An example of this would be launching an instance and then waiting for the instance to become available, or waiting until a subnet in a VCN has been terminated. This waiting can be accomplished by using the :py:func:`~oci.wait_until` function. As an example:

.. code-block:: python

    import oci
    
    config = oci.config.from_file()
    client = oci.core.ComputeClient(config)

    response = client.launch_instance(...)
    instance_ocid = response.data.id

    # We will get returned the result of the last get_instance call (in this case the one where the lifecycle state has moved to available).
    # We can inspect the .data attribute of this (i.e. get_instance_response.data) to get information about the instance
    #
    # Some items to note about the parameters provided:
    #
    #   - The first parameter is the client we'll use to call the service to retrieve data
    #   - The second parameter is the result of a service call. The wait_until function uses this to determine what service operation needs to be called. In the case below
    #     it will keep calling client.get_instance(instance_ocid) until the instance reaches the desired state
    #   - The third parameter is the name of the attribute we will check. The object we will check against is the result of calling .data on the result of the service call.
    #     Please consult the API reference for available attribute names you can use
    #   - The fourth parameter is the desired value. An equality (==) comparison is done
    get_instance_response = oci.wait_until(client, client.get_instance(instance_ocid), 'lifecycle_state', 'RUNNING')


In addition to the base parameters shown above, the function can accept optional attributes to control the maximum amount of time it will wait for and the time between calls to the service. For more information on the optional parameters, see the documentation on the :py:func:`~oci.wait_until` function. 

For a more comprehensive sample, please see our `examples <https://github.com/oracle/oci-python-sdk/blob/master/examples/wait_for_resource_in_state.py>`_ on GitHub.