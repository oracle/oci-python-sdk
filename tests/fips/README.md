Link to FIPS page for Python:
https://confluence.oci.oraclecorp.com/display/SEC/OpenSSL+with+FIPS+for+Python

Docs for using the CLI:
https://confluence.oci.oraclecorp.com/display/SEC/Use+FIPS+140-2-Validated+Encryption+Libraries+for+the+CLI

Docker Commands
---------------

Build the docker image

  docker build -t fips_testing:latest -f "$(pwd)"/tests/fips/ol7.5-python-fips-Dockerfile "$(pwd)"/tests/fips

Run the testing scripts using the docker image.  This assumes your working directory
contains a clone of the Python SDK repository.

  docker run -e PYTHON_TESTS_ADMIN_PASS_PHRASE --name oraclelinux -v "$(pwd)":/oci fips_testing:latest /bin/bash -l /oci/tests/fips/python_sdk_fips_testing.sh

Interactive access to the docker container.  This assumes your working directory
contains a clone of the Python SDK repository.

  docker run -e PYTHON_TESTS_ADMIN_PASS_PHRASE --name oraclelinux -v "$(pwd)":/oci -it fips_testing:latest bash

Other potentially useful docker commands

  docker ps -a
  docker inspect oraclelinux
  docker container stop oraclelinux
  docker container rm oraclelinux
  docker images
  docker rmi fips_testing:latest


Openssl and libcrypto
---------------------

The docker image containes the following version of openssl

```
# openssl version
OpenSSL 1.0.2k-fips  26 Jan 2017
```

This is the path to libcrypto in the docker container
FIPS_LIBCRYPTO_PATH=/usr/lib64/libcrypto.so.1.0.2k


Sample Python program
---------------------

This Python program which fails when used in FIPS complicant environment
This is from [confluence](https://confluence.oci.oraclecorp.com/display/SEC/OpenSSL+with+FIPS+for+Python)
with additions from the [CLI](https://bitbucket.oci.oraclecorp.com/projects/SDK/repos/python-cli/browse/src/oci_cli/fips.py)

```
import ctypes
_bs_crypto = ctypes.CDLL('/usr/lib64/libcrypto.so.1.0.2k')
_bs_crypto.FIPS_mode_set(ctypes.c_int(1))
_bs_crypto.FIPS_mode()
import ssl  # noqa: E402
if not hasattr(ssl, 'FIPS_mode'):
    ssl.FIPS_mode = _bs_crypto.FIPS_mode
import hashlib
hashlib.md5(b"Hello World\n").hexdigest()
````

Output using Python 2.7.5

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: error:060800A3:digital envelope routines:EVP_DigestInit_ex:disabled for fips
```

Output with Python 3.6.5

```
'e59ff97941044f85df5297e1c302d260'
```

This indicates that Python 3.6.5 is not using lybcrypto for it's md5 implementation
