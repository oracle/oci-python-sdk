.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Pagination
~~~~~~~~~~~~
When you call a list operation (for example :py:func:`~oci.core.compute_client.ComputeClient.list_instances`) will retrieve a page of results. In order
to retrieve more data, you have to continue to make calls to the list operation, passing in the value of the most recent response's ``next_page`` attribute 
as a parameter to the next list operation call.

As a convenience over manually writing pagination code, you can make use of the functions in the :py:mod:`~oci.pagination` module to:

* Eagerly load all possible results from a list call
* Eagerly load all results from a list call up to a given limit
* Lazily load results (either all results, or up to a given limit) from a list call via a generator. These generators can yield either values/models or the raw response from calling the list operation

The :py:mod:`~oci.pagination` module uses retry with the default retry configuration. For more information, check out the :doc:`Retries </sdk_behaviors/retries>` documentation.
For an example on how to use these functions, please check `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/pagination.py>`_. More details about the API is `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/api/pagination.html>`_.
