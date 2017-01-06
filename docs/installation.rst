.. _install:

Installation
~~~~~~~~~~~~

First, download the SDK .whl from the `SDK and Other Tools`__ page.  Then, install with::

    pip install oraclebmc-*-py2.py3-none-any.whl

The SDK is coming to the `PyPI`_ soon, at which point you will be able to use::

    pip install oraclebmc

===============
 Prerequisites
===============

oraclebmc uses the `cryptography.io`_ library, which has its own additional `build requirements`_.

Oracle Bare Metal Cloud requires `TLS 1.2`__, which versions of `openssl`_ before 1.0.1 do not provide.  If your
version of Python was built against an earlier version, you will need to install a new Python that links against a
newer version.

You can check the version of openssl that Python was linked to with::

    python -c "import ssl;print(ssl.OPENSSL_VERSION)"

If you see ``OpenSSL 0.9.x`` then you will need to reinstall Python against a newer version.

.. _cryptography.io: https://cryptography.io/en/latest/
.. _build requirements: https://cryptography.io/en/latest/installation/
__ https://docs.us-az-phoenix-1.oracleiaas.com/Content/API/Concepts/sdks.htm
.. _PyPI: https://pypi.python.org/pypi
__ https://tools.ietf.org/html/rfc5246
.. _openssl: https://www.openssl.org/

====================
 Note for OSX Users
====================

OS X already has Python and OpenSSL preinstalled. However, the preinstalled OpenSSL is probably not version 1.0.x or newer, which is what you need. To check whether you have a supported OpenSSL version, run this command:

::

    python -c "import ssl; print(ssl.OPENSSL_VERSION)"

If the version is ``0.9.x``, you need to reinstall Python and OpenSSL using Homebrew (a package manager for the OS X platform).

If you've never used Homebrew to install Python on the system, follow these instructions:

    1. Download and install `Homebrew <http://brew.sh/>`_.
    2. Use these commands to update Homebrew and then install OpenSSL and Python:

       ::

        brew update
        brew install openssl
        brew install python

  .. note:: If you get a "Permission denied" message when running any brew command, it's probably because the OS X permissions model conflicts with Homebrew's default installation location of ``/usr/local``. You can usually fix this by taking back control of the folder with ``sudo chown -R $(whoami) /usr/local``.

Check the OpenSSL version again. If it's still 0.9, see `Troubleshooting Mac Issues`_.


==========================
Troubleshooting Mac Issues
==========================

There are several general types of issues you might encounter.

OpenSSL Version Still 0.9.x
---------------------------

If the Python installation instructions listed in Mac above still result in OpenSSL version 0.9.x, it might be one of these reasons:

    * Your python command is pointing to the wrong Python installation. To check, use the which python command. The default system Python is at ``/usr/bin/python``, whereas the Homebrew-installed version that you want is typically at ``usr/local/bin``. Edit the ``etc/paths`` file to move the ``usr/local/bin`` line to the top of the list. Don't remove the system Python line.

    * Your virtualenv is pointing to the wrong Python installation. By default, virtualenv uses ``/usr/bin/python``, whereas the Homebrew-installed Python is typically at ``usr/local/bin``. To fix this, use this command:

     ::

            virtualenv -p <path to Homebrew Python>  <directory for the virtualenv>

            For example, if your installation is at /usr/local/bin/python:

     ::

            virtualenv -p /usr/local/bin/python cli_env

To determine the location of your Homebrew-installed Python, try one of these commands:

::

    brew info python
    which -a python (the -a option lists all the Python installations)
    brew doctor

If the above items don't fix the problem, the best strategy is to uninstall and reinstall Python with the following commands. Note that you will need to reinstall any packages you previously installed into Homebrew's Python via pip.

::

    brew uninstall openssl
    brew uninstall python
    brew update
    brew install python

If you're still having problems, you may need slightly different commands depending on the version of Homebrew that was used to install your Python or OpenSSL libraries. Here's a recent post that may be helpful: Updating Python and OpenSSL on OS X.

SSL/TLS or Certificate Exception
--------------------------------

When trying to use the CLI, if you get an exception related to SSL/TLS or certificates/certificate validation, the underlying issue is that OpenSSL is the wrong version (0.9.x). See the solution for uninstalling and reinstalling Python above. Make sure to also reinstall the wheel with this command:

::

    pip install oraclebmc_cli-<VERSION>-py2.py3-none-any.whl.

bmcs Command Not Found
----------------------

When trying to use the CLI, if the bmcs command is not found, it could be that pip installed the package to a different virtual environment than your active one, or you've switched to a different active virtual environment after installing the CLI. You can determine where the CLI is installed by using which pip and which bmcs.
