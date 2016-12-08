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

MacOS no longer keeps openssl updated.  If you have `brew`_, it is recommended to install Python, which should
build against brew's version of openssl::

    brew update
    brew install python

By default brew installs Python to ``/usr/local/bin``, while the system Python is located in ``/usr/bin``.  If your
``$PATH`` does not have ``/usr/local/bin`` first, invoking python or creating a virtualenv with ``virtualenv my-venv``
will still use the system's python.  You can use ``brew doctor`` to verify that your path is set up correctly, or
``which python`` to see which Python will be used.

.. _brew: http://brew.sh/