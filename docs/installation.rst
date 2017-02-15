.. _install:

Installation
~~~~~~~~~~~~

This topic describes how to install, configure, and use the Oracle Bare Metal Cloud Services Python SDK.
The Python SDK supports operations for the following services:

* Identity and Access Management Service
* Object Storage Service
* Core Services (Networking Service, Compute Service, and Block Volume Service)

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
* The Python SDK requires `TLS 1.2`_, which versions of `openssl`_ before 1.0.1 do not provide.
  If your version of Python was built against an earlier version, you will need to install a new
  Python that links against a newer version.
* A keypair used for signing API requests, with the public key uploaded to Oracle. Only the user calling
  the API should be in possession of the private key. See Configuring the SDK below.

.. _Adding Users: https://docs.us-phoenix-1.oraclecloud.com/Content/GSG/Tasks/addingusers.htm
.. _Common Policies: https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/commonpolicies.htm
.. _cryptography.io: https://cryptography.io/en/latest/
.. _build requirements: https://cryptography.io/en/latest/installation/
.. _TLS 1.2: https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdks.htm
.. _PyPI: https://pypi.python.org/pypi
.. _openssl: https://www.openssl.org/

====================================
 Downloading and Installing the SDK
====================================

You can install using a GitHub download or by using the Python Package Index (PyPI).

To install using the SDK download:

1. Download the SDK from `GitHub`__. 
   The download is a zip containing a whl file and documentation.
2. Extract the files from the zip.
3. Use the following command to install the SDK::

      pip install oraclebmc-*-py2.py3-none-any.whl

  .. note::

      If you're unable to install the whl file, make sure pip is up to date.
      Use ``pip install -U pip`` and then try to install the whl file again.

To install from the `Python Package Index <https://pypi/python.org/pypi/oraclebmc/1.1.0>`_
:

   Use the following command::

      pip install oraclebmc


(Optional) 
Oracle recommends that you run the SDK in a virtual environment with virtualenv.

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

====================
 Note for OSX Users
====================

OS X already has Python and OpenSSL preinstalled. However, the preinstalled OpenSSL is probably not version 1.0.x or
newer, which is what you need. To check whether you have a supported OpenSSL version, run this command::

    python -c "import ssl; print(ssl.OPENSSL_VERSION)"

If the version is ``0.9.x``, you need to reinstall Python and OpenSSL using Homebrew
(a package manager for the OS X platform).

If you've never used Homebrew to install Python on the system, follow these instructions:

1. Download and install `Homebrew`_.
2. Use these commands to update Homebrew and then install OpenSSL and Python:
   ::

       brew update
       brew install openssl
       brew install python

  .. note::

    If you get a "Permission denied" message when running any brew command, it's probably because
    the OS X permissions model conflicts with Homebrew's default installation location of ``/usr/local``.
    You can usually fix this by taking back control of the folder with ``sudo chown -R $(whoami) /usr/local``.

Check the OpenSSL version again. If it's still 0.9, see `Troubleshooting Mac Issues`_.

.. _Homebrew: http://brew.sh/

=================
 Troubleshooting
=================

You might encounter issues when installing Python or the SDK, or using the SDK itself.

----------------------------
 Troubleshooting OEL Issues
----------------------------
On OEL 7.3, if you encounter permission issues when running pip install, you might need to use ``sudo``.

----------------------------
 Troubleshooting Mac Issues
----------------------------

There are several general types of issues you might encounter.

OpenSSL Version Still 0.9.x
===========================

If the Python installation instructions listed in Mac above still result in OpenSSL version 0.9.x,
it might be one of these reasons:

* Your python command is pointing to the wrong Python installation. To check, use the which python command.
  The default system Python is at ``/usr/bin/python``, whereas the Homebrew-installed version that you want
  is typically at ``usr/local/bin``. Edit the ``etc/paths`` file to move the ``usr/local/bin`` line to the
  top of the list. Don't remove the system Python line.

* Your virtualenv is pointing to the wrong Python installation. By default, virtualenv uses ``/usr/bin/python``,
  whereas the Homebrew-installed Python is typically at ``usr/local/bin``. To fix this, use this command::

      virtualenv -p <path to Homebrew Python>  <directory for the virtualenv>

  For example, if your installation is at /usr/local/bin/python::

      virtualenv -p /usr/local/bin/python bmcs_sdk_env

To determine the location of your Homebrew-installed Python, try one of these commands::

    brew info python
    which -a python  # (the -a option lists all the Python installations)
    brew doctor

If the above items don't fix the problem, the best strategy is to uninstall and reinstall Python with the following
commands. Note that you will need to reinstall any packages you previously installed into Homebrew's Python via pip.
::

    brew uninstall openssl
    brew uninstall python
    brew update
    brew install python

If you're still having problems, you may need slightly different commands depending on the version of Homebrew
that was used to install your Python or OpenSSL libraries. Here's a recent post that may be helpful:
`Updating Python and OpenSSL on OS X`__.

__ https://community.dev.hpe.com/t5/Blogs/Updating-Python-and-Openssl-on-OS-X/ba-p/237791

SSL/TLS or Certificate Exception
================================

When trying to use the SDK, if you get an exception related to SSL/TLS or certificates/certificate validation,
the underlying issue is that OpenSSL is the wrong version (0.9.x). See the solution for uninstalling and
reinstalling Python above. Make sure to also reinstall the wheel with this command::

    pip install oraclebmc-*-py2.py3-none-any.whl

================
 Contributions
================

Got a fix for a bug, or a new feature you'd like to contribute? The SDK is open source and accepting pull requests on `GitHub`__.

__ https://github.com/oracle/bmcs-python-sdk

================
 Notifications
================

To be notified when a new version of the Python SDK is released, subscribe to the `Atom feed`_.

.. _Atom feed: https://github.com/oracle/bmcs-python-sdk/releases.atom


