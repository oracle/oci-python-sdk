.. _install:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Installation
~~~~~~~~~~~~

This topic describes how to install, configure, and use the Oracle Cloud Infrastructure Python SDK.

===============
 Prerequisites
===============

The Python SDK requires:

* Python version 2.7.5 or 3.5 or later
* `OpenSSL`_ version 1.0.1 or later. The Python SDK uses the `Cryptography.io`_ library which requires `OpenSSL`_. For details on all Cryptography.io prerequisites, see `Cryptography.io Installation`_.

In addition, all Oracle Cloud Infrastructure SDKs require:

* An Oracle Cloud Infrastructure account
* A user created in that account, in a group with a policy that grants the desired permissions.
  This can be a user for yourself, or another person/system that needs to call the API.
  For an example of how to set up a new user, group, compartment, and policy, see
  `Adding Users`_ in the Getting Started Guide. For a list of other typical
  Oracle Cloud Infrastructure policies, see `Common Policies`_ in the User Guide.
* A keypair used for signing API requests, with the public key uploaded to Oracle. Only the user calling
  the API should be in possession of the private key. (For more information, see `Configuring the SDK`_.)




====================================
 Downloading and Installing the SDK
====================================

You can install the Python SDK through the Python Package Index (PyPI), or alternatively through GitHub.

Set up a virtual environment
-----------------------------

Oracle recommends that you run the SDK in a virtual environment with virtualenv. This allows
you to isolate the dependencies for the SDK and avoids any potential conflicts with other Python packages
which may already be installed (e.g. in your system-wide Python).

With Linux, virtualenv is usually in a separate package from the main Python package.
If you need to install virtualenv, use ``pip install virtualenv``.
To create and activate a virtual environment::

    virtualenv <environment name>
    source <environment name>/bin/activate

For example::

    virtualenv oci_sdk_env
    source oci_sdk_env/bin/activate

PyPi
-----

To install from `PyPI <https://pypi.python.org/pypi/oci>`_ use the following command::

    pip install oci

GitHub
-------

To install from GitHub:

1. Download the SDK from `GitHub <https://github.com/oracle/oci-python-sdk/releases>`_.
   The download is a zip containing a whl file and documentation.
2. Extract the files from the zip.
3. Use the following command to install the SDK::

    pip install oci-*-py2.py3-none-any.whl

  .. note::

      If you're unable to install the whl file, make sure pip is up to date.
      Use ``pip install -U pip`` and then try to install the whl file again.


=====================
 Configuring the SDK
=====================

Before using the SDK, you must set up your config file with the required credentials.
For instructions, see `SDK and Tool Configuration`_ in the User Guide.

.. _SDK and Tool Configuration: https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdkconfig.htm

Verify OpenSSL Version
----------------------

The supported version of OpenSSL for the Python SDK is version 1.0.1 or newer.  Run the following command to find out the version of OpenSSL that you have::

    python -c "import ssl; print(ssl.OPENSSL_VERSION)"

If the version is lower than ``1.0.1``, run the following command to bypass the version issue::

    pip install requests[security]==2.18.4

This command instructs the `requests <https://pypi.python.org/pypi/requests>`_
library used by the Python SDK to use the version of OpenSSL that is bundled with the `cryptography <https://pypi.python.org/pypi/cryptography>`_
library used by the SDK.

If you don't want to use ``requests[security]`` you can update OpenSSL as you normally would. For example, on OS X, use Homebrew to update OpenSSL using the following commands::

 brew update
 brew install openssl
 brew install python

.. note::
    If you need to configure your environment for FIPS-compliance, see :doc:`fips-libraries`

=================
 Troubleshooting
=================

You might encounter issues when installing Python or the SDK, or using the SDK itself.

Service Errors
--------------
Any operation resulting in a service error will cause an exception of type oci.exceptions.ServiceError to be thrown by the SDK. For information about common service errors, see `API Errors <https://docs.us-phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm>`_.


pip 10 Installation Errors
---------------------------
If you are attempting to install the SDK in your system-wide Python using pip 10 then you may encounter conflicts with ``distutils`` installed packages. An example error message is:

.. code-block:: none

    sudo pip install oci
    ...
    ...
    Cannot uninstall 'requests'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.

Resolve by using a virtual environment
***************************************
Installing the SDK in a virtual environment instead of the system-wide Python. See the *Downloading and Installing the SDK* section for more information

Resolve by using the system-wide Python
****************************************
If you wish to still use the system-wide Python, you can resolve this issue by downgrading the version of ``pip`` you are using and then trying to re-install the SDK. ::

    sudo pip install pip==9.0.3
    sudo pip install oci

If you wish to stick with ``pip`` version 10, then you will either have to install the SDK using the ``--user`` switch::

    pip install oci --user

Or you will have to uninstall the distutils installed packages manually. To do this, you will have to:

1. Make a note of what packages cannot be uninstalled. In the example error message, the package is **requests**
2. Find the install location for these packages. You can find this by looking in the directories returned by ``python -m site``
3. One of the directories should contain a sub-directory with the same name as the package (e.g. in the case of the example error message the folder should be called **requests**) and a ``.egg-info`` file which contains the package name and a version
4. Delete the folder and the ``.egg-info`` file
5. Try and re-install the SDK::

    sudo pip install oci

SSL/TLS or Certificate Issues
-----------------------------

When trying to use the SDK, if you get an exception related to SSL/TLS or certificates/certificate validation, see the command for installing requests[security] in `Verify OpenSSL Version`_.


.. _Adding Users: https://docs.us-phoenix-1.oraclecloud.com/Content/GSG/Tasks/addingusers.htm
.. _Common Policies: https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/commonpolicies.htm
.. _Cryptography.io: https://cryptography.io/en/latest/
.. _Cryptography.io Installation: https://cryptography.io/en/latest/installation/
.. _TLS 1.2: https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdks.htm
.. _PyPI link: https://pypi.python.org/pypi
.. _OpenSSL: https://www.openssl.org/
.. _ConfiguringSDK: Configuring the SDK
.. _OSXUsers: Verify OpenSSL Version