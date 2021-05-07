#!/bin/sh

# This script assumes it is running in a docker container with the Python SDK
# repository mounted into the /oci directory and the
# PYTHON_TESTS_ADMIN_PASS_PHRASE set.

set -e
set -x

# Enable pyenv shell integration
eval "$(pyenv init -)"
eval "$(pyenv init --path)"

# TODO: Update the requirements and setup.py so we can use pyOpenSSL > 17.4.0
#       That version is no longer available in the artifactory.
# Setup PIP to use the artifactory
# export PIP_CONFIG_FILE=~/pip.conf
# touch $PIP_CONFIG_FILE
# echo "[global]" > $PIP_CONFIG_FILE
# echo "index-url = https://artifactory.oci.oraclecorp.com/api/pypi/global-dev-pypi/simple" >> $PIP_CONFIG_FILE
# echo "trusted-host = artifactory.oci.oraclecorp.com" >> $PIP_CONFIG_FILE

# Export the path to the fips version of libcrypto
export FIPS_LIBCRYPTO_PATH=/usr/lib64/libcrypto.so.1.0.2k

# Load required environment
source /oci/internal_resources/test_setup.sh

# TODO: Where should the ADMIN_PASS_PHRASE go?  Teamcity?
#       Currently this must be manually set in the enviromnent used for testing

echo "Using python 2.7.5"
pyenv shell 2.7.5

# Update pip to the latest version
pip install -U pip

# Install oci from the clone of the repository
pip install -e /oci
pip install -r /oci/requirements.txt

echo "Python 2.7.5 - Entering fips mode and importing Python SDK"
echo $(pwd)
python /oci/tests/fips/verify_fips_mode.py

pyenv shell --unset

echo "Using Python 3.6.5"
pyenv shell 3.6.5

# Update pip to the latest version
pip install -U pip

# Install oci from the clone of the repository
pip install -e /oci
pip install -r /oci/requirements.txt

echo "Python 3.6.5 - Entering fips mode and importing Python SDK"
python /oci/tests/fips/verify_fips_mode.py

# Run the oci unit tests in FIPS mode to enshure there are no issues.
echo "Running unit tests"
cd /oci
pytest tests/unit
