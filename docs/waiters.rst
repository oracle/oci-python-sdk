.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Composite Operations and Waiters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To wait until an attribute of a resource reaches a certain state, you can use composite operations or waiters. 

Composite Operations
---------------------
You can use the ``CompositeOperation`` classes in the SDK (e.g. :py:class:`~oci.core.ComputeClientCompositeOperations`) 
to perform an action on a resource and wait for it to enter a particular state (or states). The ``CompositeOperation`` classes provide 
convenience methods so that you do not have to invoke an operation and then separately invoke a waiter. 

An example of using ``CompositeOperation`` classes can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/composite_operations_example.py>`__.

Waiters
-------
You can also use the :py:func:`~oci.wait_until` function to wait for a resource to enter a particular state. As an example:

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

Instead of waiting for a single attribute to equal a given value, you can also provide a function reference (either a lambda or a reference to an already defined function) that can be used to evaluate the response received from the service call. This function should return a truthy value if the waiter should stop waiting, and a falsey value if the waiter should continue waiting. 

.. note::
    If the function reference fails to evaluate the service call and return a response, ``wait_until()`` returns an error.

For example, to wait until a volume backup reaches either the "AVAILABLE" or "FAULTY" state :

.. code-block:: python

    oci.wait_until(client, client.get_volume_backup(vol_backup_id), evaluate_response=lambda r: r.data.lifecycle_state in ['AVAILABLE', 'FAULTY'])

Instead of using a lambda, an already defined function can be used:

.. code-block:: python

    def should_stop_waiting_volume_backup(response):
        return response.data.lifecycle_state in ['AVAILABLE', 'FAULTY']

    oci.wait_until(client, client.get_volume_backup(vol_backup_id), evaluate_response=should_stop_waiting_volume_backup)

In addition to these base parameters, ``wait_until()`` can accept optional attributes to control the maximum amount of time it will wait  and the time between calls to the service. For more information on the optional parameters, see the documentation on the :py:func:`~oci.wait_until` function. 

For a more comprehensive sample, please see our `examples <https://github.com/oracle/oci-python-sdk/blob/master/examples/wait_for_resource_in_state.py>`_ on GitHub.
