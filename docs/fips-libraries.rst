.. _fips-libraries:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Using FIPS-validated Libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SDK can be configured to use FIPS-validated libcrypto library. You can set it programmatically on a per session basis or persistently across the environment. Both approaches require the path to the libcrypto library on your system.

Enabling FIPS Mode Programmatically
------------------------------------

To configure the SDK to use a FIPS-validated libcrypto library, execute the following:

.. code-block:: python

    oci.fips.enable_fips_mode('</path/to/libcrypto.x.x.x>')

Setting the Environment Variables
---------------------------------

If you do not want to run ``enable_fips_mode()`` for every session, you can set an environment variable so that the SDK uses the library every time.

Set the one of the following environment variables to the path to the libcrypto library, listed according to priority:

- FIPS_LIBCRYPTO_PATH
- OCI_PYTHON_SDK_FIPS_LIBCRYPTO_PATH

Verifying the Configuration
---------------------------

To verify that the SDK is using the libcrypto library that you specified, execute the following:

.. code-block:: python

    oci.fips.is_fips_mode()

This should return True, indicating that the SDK is using the library specified by the environment variable.
