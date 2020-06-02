#!/usr/bin/env bash

# This script downloads the latest source from bitbucket and github and runs the tests in the bitbucket
# repo against the version of the SDK on github.

set -e ;
set -x ;

echo "Running Github build script"

ls -la

ls -la .python-sdk-bitbucket

# must disable StrictHostKeyChecking so that we don't get an interactive
# prompt later asking to confirm the host key
set +e
ssh -o StrictHostKeyChecking=no github.com
ssh -o StrictHostKeyChecking=no git@bitbucket.oci.oraclecorp.com -p 7999
set -e

# Put in the clone from GitHub
git clone $GITHUB_CLONE_TARGET .python-sdk-github

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

# Redirect STDOUT and STDERR to a file to avoid resource unavailable error in TeamCity jobs.
python setup.py sdist bdist_wheel >> build_output.txt 2>&1

# install github version of the SDK from whl using PyPi production index for dependencies
# (by default in TC it will use artifactory)
# pip install pyOpenSSL --upgrade
# pip install -i https://pypi.python.org/simple --trusted-host pypi.python.org dist/*.whl
pip install dist/*.whl >> build_output.txt 2>&1

rm build_output.txt

# back out of github repo
cd ..

echo Running Tests

if [ $TEST_ENABLE = "false" ]; then
  echo "TESTS HAVE BEEN DISABLED."
else
  # we are using pytest directly so we can run the *bitbucket* tests against the
  # *github* version of the SDK (which was installed above)
  # tox runs the tests inside a virtual environment and explicitly installs
  # the current project which we dont want
  pip install pytest==3.2.3
  pip install mock==2.0.0
  pip install vcrpy==1.11.1

  # run tests from bitbucket repository because not all tests are copied into github
  # skip the long running integration tests
  cd .python-sdk-bitbucket/
  source internal_resources/test_setup.sh
  py.test --vcr-record-mode=none \
          --ignore=tests/integ/test_large_file_transfer.py \
          --ignore=tests/integ/test_object_storage.py \
          --ignore=tests/integ/test_composite_operations.py \
          --ignore=tests/integ/test_virtualnetwork.py \
          --ignore=tests/integ/test_launch_instance_tutorial.py \
          tests/unit tests/integ -s
fi

exit
