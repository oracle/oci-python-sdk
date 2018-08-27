#!/usr/bin/env bash

set -e ;
set -x ;

echo Check Directory Contents
ls -la

echo "Sourcing test_setup.sh to load env vars"
source internal_resources/test_setup.sh;


# If the team city venv exists, use that to create a local venv.
# If we are not running on team city, assume that a venv is already in use.
if [ -d "/opt/odo/tox_sic/venv/bin" ]; then
  echo Creating venv to install sdk locally
  . /opt/odo/tox_sic/venv/bin/activate
  virtualenv .sdk-venv
  . .sdk-venv/bin/activate
fi

pip install -U pip
pip install -e .

echo Python version
python --version

SDK_VERSION=$(tail -1 src/oci/version.py | cut -d '"' -f2)
echo SDK Version Number $SDK_VERSION

# echo Building Docs
# pip install sphinx --timeout 120
# pip install sphinx_rtd_theme

# touch warnings.txt
# make docs

# a hyperlinks mismatch will cause all of the links on readthedocs to break
# if cat warnings.txt | grep -q "ERROR: Anonymous hyperlink mismatch";  then
#     echo "Failing due to error building docs with sphinx.";
#     exit 1;
# else
#     echo "No critical errors found during sphinx build.";
# fi

# mkdir -p dist/oci-python-sdk-docs-$SDK_VERSION/
# cp -r docs/_build/html/* dist/oci-python-sdk-docs-$SDK_VERSION/

echo Running Tests

if [ $TEST_ENABLE = "false" ]; then
  echo "Tests Disabled.  Just running flake 8"
  # tox -e flake8
else
  echo "Tests enabled"
  # pip install tox
  # tox -e flake8,py35 -- --vcr-record-mode=none
fi

echo Building Wheel
make build

# Create a dev directory that will contain versions of the whl, zip, and docs meant for
# the dev pypi artifactory. Each artifact includes the build number in the version to avoid
# conflicts.
# DEV_VERSION=$SDK_VERSION+$BUILD_NUMBER
# mkdir -p dist/dev/
# cp dist/oci-$SDK_VERSION-py2.py3-none-any.whl dist/dev/oci-$DEV_VERSION-py2.py3-none-any.whl
# cp dist/oci-python-sdk-$SDK_VERSION.zip dist/dev/oci-python-sdk-$DEV_VERSION.zip

# pushd dist/oci-python-sdk-docs-$SDK_VERSION
# zip -r ../oci-python-sdk-docs-$SDK_VERSION.zip .
# popd
# cp dist/oci-python-sdk-docs-$SDK_VERSION.zip dist/dev/oci-python-sdk-docs-$DEV_VERSION.zip


# echo Contents of dist folder
# ls -la dist
