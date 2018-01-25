#!/usr/bin/env bash

# This script is used to: 
#   - Run the tests without using VCR to mock responses (by deleting the old mock responses)
#   - Re-record the tests so that we keep our VCR data up to date

set -e ;
set -x ;

echo Check Directory Contents
ls -la

echo "Sourcing test_setup.sh to load env vars"
source internal_resources/test_setup.sh;

echo Creating venv to install sdk locally
. /opt/odo/tox_sic/venv/bin/activate
virtualenv .sdk-venv
. .sdk-venv/bin/activate
pip install -e .

echo Python version
python --version

echo Running Tests

if [ $TEST_ENABLE = "false" ]; then
  echo "TESTS HAVE BEEN DISABLED."
else
  pip install tox

  echo "Removing mocked responses before Python 2.7 test run"
  rm tests/fixtures/cassettes/*.yml

  echo "Running Python 2.7 tests"
  tox -e py27 -- --vcr-record-mode=all

  echo "Removing mocked responses before Python 3.5 test run"
  rm tests/fixtures/cassettes/*.yml

  echo "Running Python 3.5 tests"
  tox -e py35 -- --vcr-record-mode=all
fi