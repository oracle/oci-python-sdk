.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Logging
~~~~~~~

The Python SDK uses Python's `logging <https://docs.python.org/3.6/library/logging.html>`_ module.

Loggers for the Python SDK are ordered hierarchically, with the top level being ``oci`` (or ``oraclebmc`` if you are using the legacy OracleBMC package).

Logger names are of the form ``<hierarchy>.<id>`` where the ``<hierarchy>`` is similar to ``oci.base_client`` and ``<id>`` is the result of Python's built-in ``id()`` function. The implication of this is that different instances of the same class have different loggers.

Here is an example for adding debug logging at the top level of the oci package.

.. code-block:: python
    import oci
    import logging

    # Enable debug logging
    logging.getLogger('oci').setLevel(logging.DEBUG)

    # Rest of code ...

Request Logging
================
To enable more detailed debugging information request logging can can be turned on.  Request logging will output the requests which the Python SDK sends to Oracle Cloud Infrastructure services.  This option is enabled by setting the configuration attribute ``log_requests`` to ``True``. This could be done in your configuration file, for example:

.. code-block:: text

    [DEFAULT]
    user = <user OCID>
    fingerprint = <fingerprint>
    key_file = <key file>
    tenancy = <tenancy OCID>
    region = us-ashburn-1
    log_requests = True

Or programmatically, for example:

.. code-block:: python

    config = {
        "user": user_ocid,
        "key_file": key_file,
        "fingerprint": calc_fingerprint(key_file),
        "tenancy": testrunner.tenancy,
        "region": testrunner.region,
        "log_requests": True
    }

Request logging turns on debugging information in the Python http module.  This debugging information can be quite verbose and the output will go to standard out.  This http module does not use Python's logging module.

Once you have request logging in your config, you can create the appropriate logging handler(s) for your use case. For example to log to an output stream such as ``stderr`` you could do:

.. code-block:: python

    import oci
    import logging

    config = oci.config.from_file()
    config['log_requests'] = True

    logging.basicConfig()

    client = oci.identity.IdentityClient(config)

    # This call will emit log information to stderr
    client.list_regions()

Note the oci module has logging at the following levels:

* ``INFO``: Request method and request URL
* ``DEBUG``: Request headers and body, and response headers


The raw response body is not logged.
