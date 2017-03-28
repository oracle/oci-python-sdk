.. _install:

Installation
~~~~~~~~~~~~

This topic describes how to install, configure, and use the Oracle Bare Metal Cloud Services Python SDK.
The Python SDK supports operations for the following services:

* Identity and Access Management Service
* Core Services (Networking Service, Compute Service, and Block Volume Service)
* Object Storage Service

===============
 Prerequisites
===============

* An Oracle Bare Metal Cloud Services account
* A user created in that account, in a group with a policy that grants the desired permissions.
  This can be a user for yourself, or another person/system that needs to call the API.
  For an example of how to set up a new user, group, compartment, and policy, see
  `Adding Users`_ in the Getting Started Guide. For a list of other typical
  Oracle Bare Metal Cloud Services policies, see `Common Policies`_ in the User Guide.
* Python version 2.7.5 or 3.5 or later, running on Mac, Windows, or Linux. 
* The Python SDK uses the `cryptography.io`_ library, which has its own additional `build requirements`_.
* A keypair used for signing API requests, with the public key uploaded to Oracle. Only the user calling
  the API should be in possession of the private key. (For more information, see `Configuring the SDK`_.)


====================================
 Downloading and Installing the SDK
====================================

You can install the Python SDK through the Python Package Index (PyPI), or alternatively through GitHub. 

**PyPi**

To install from `PyPI <https://pypi.python.org/pypi/oraclebmc>`_:

  Use the following command::

      pip install oraclebmc

**GitHub**

To install from GitHub:

1. Download the SDK from `GitHub <https://github.com/oracle/bmcs-python-sdk/releases>`_. 
   The download is a zip containing a whl file and documentation.
2. Extract the files from the zip.
3. Use the following command to install the SDK::

      pip install oraclebmc-*-py2.py3-none-any.whl

  .. note::

      If you're unable to install the whl file, make sure pip is up to date.
      Use ``pip install -U pip`` and then try to install the whl file again.


**Virtual environment (Optional)** 

Although optional, Oracle recommends that you run the SDK in a virtual environment with virtualenv.

    With Linux, it's usually in a separate package from the main Python package.
    If you need to install virtualenv, use pip install virtualenv.
    To create and activate a virtual environment::

        virtualenv <environment name>
        . <environment name>/bin/activate

    For example::

        virtualenv bmcs_sdk_env
        . bmcs_sdk_env/bin/activate



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

    pip install requests[security]

This command instructs the `requests <https://pypi.python.org/pypi/requests>`_
library used by the Python SDK to use the version of OpenSSL that is bundled with the `cryptography <https://pypi.python.org/pypi/cryptography>`_
library used by the SDK.

**Note:**
If you don't want to use ``requests[security]`` you can update OpenSSL as you normally would. For example, on OS X, use Homebrew to update OpenSSL using the following commands::

 brew update
 brew install openssl
 brew install python

=================
 Troubleshooting
=================

You might encounter issues when installing Python or the SDK, or using the SDK itself.

Service Errors
--------------
Any operation resulting in a service error will cause an exception of type oraclebmc.exceptions.ServiceError to be thrown by the SDK. For information about common service errors returned by BMCS, see `API Errors <https://docs.us-phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm>`_
.

Oracle Linux Permission Issues
------------------------------
On Oracle Linux 7.3, if you encounter permission issues when running pip install, you might need to use ``sudo``.

SSL/TLS or Certificate Issues
-----------------------------

When trying to use the SDK, if you get an exception related to SSL/TLS or certificates/certificate validation, see the command for installing requests[security] in `Verify OpenSSL Version`_.


.. _Adding Users: https://docs.us-phoenix-1.oraclecloud.com/Content/GSG/Tasks/addingusers.htm
.. _Common Policies: https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/commonpolicies.htm
.. _cryptography.io: https://cryptography.io/en/latest/
.. _build requirements: https://cryptography.io/en/latest/installation/
.. _TLS 1.2: https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdks.htm
.. _PyPI link: https://pypi.python.org/pypi
.. _openssl: https://www.openssl.org/
.. _ConfiguringSDK: Configuring the SDK
.. _OSXUsers: Verify OpenSSL Version