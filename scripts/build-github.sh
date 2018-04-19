#!/usr/bin/env bash

# This script downloads the latest source from bitbucket and github and runs the tests in the bitbucket
# repo against the version of the SDK on github.

set -e ;
set -x ;

echo "Running Github build script"

ls -la

ls -la .python-sdk-bitbucket
ls -la .python-sdk-github

echo Creating venv to install sdk locally
. /opt/odo/tox_sic/venv/bin/activate
virtualenv .sdk-venv
. .sdk-venv/bin/activate

echo Python version
python --version

SDK_VERSION=$(tail -1 .python-sdk-github/src/oci/version.py | cut -d '"' -f2)
echo SDK Version Number $SDK_VERSION

# build wheel to ensure it can be packaged correctly
echo Building Wheel
cd .python-sdk-github/
python setup.py sdist bdist_wheel

# install github version of the SDK from whl using PyPi production index for dependencies
# (by default in TC it will use artifactory)
# pip install pyOpenSSL --upgrade
# pip install -i https://pypi.python.org/simple --trusted-host pypi.python.org dist/*.whl
pip install dist/*.whl

# cd to build docs
cd docs/

echo Building Docs
pip install sphinx --timeout 120
pip install sphinx_rtd_theme

touch warnings.txt
make html

# a hyperlinks mismatch will cause all of the links on readthedocs to break
if cat warnings.txt | grep -q "ERROR: Anonymous hyperlink mismatch";  then
    echo "Failing due to error building docs with sphinx.";
    exit 1;
else
    echo "No critical errors found during sphinx build.";
fi

# back out of github repo
cd ../..

echo Running Tests

if [ $TEST_ENABLE = "false" ]; then
  echo "TESTS HAVE BEEN DISABLED."
else
  # tox runs the tests inside a virtual environment and explicitly installs
  # the current project which we dont want
  # we are using pytest directly so we can run the *bitbucket* tests against the
  # *github* version of the SDK (which was installed above)
  pip install pytest
  pip install mock
  pip install vcrpy

  # run tests from bitbucket repository because not all tests are copied into github
  cd .python-sdk-bitbucket/
  source internal_resources/test_setup.sh
  py.test tests/unit tests/integ -s
fi

exit
