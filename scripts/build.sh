#!/usr/bin/env bash

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

# Set up python3 pyenv(v3.6.5)
echo "Setup python environment"
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
export PYTHON_3_VERSION=3.6.5
pyenv install $PYTHON_3_VERSION -s
pyenv shell $PYTHON_3_VERSION

echo "Python Version"
python --version

# Disable Lazy imports for docs generation
export OCI_PYTHON_SDK_LAZY_IMPORTS_DISABLED=TRUE

pip install -U pip
pip install -e .

SDK_VERSION=$(tail -1 src/oci/version.py | cut -d '"' -f2)
DEV_VERSION=$SDK_VERSION+$BUILD_NUMBER
echo SDK Version Number $SDK_VERSION
echo Build Version Number $DEV_VERSION

if [ $IS_SNAPSHOT = "true" ]; then
  echo Rewriting version from $SDK_VERSION to $DEV_VERSION
  # Replace the version with the DEV_VERSION (SDK_VERSION + Build Number) so that we can make
  # referencing and declaring dependencies on more explicit
  sed -i "s/$SDK_VERSION/$DEV_VERSION/g" src/oci/version.py
else
  echo "No rewriting of version required"
fi

# Echo out the version to confirm
cat src/oci/version.py

# Disable expect 100 continue feature for integ tests.
export OCI_PYSDK_USING_EXPECT_HEADER=FALSE

echo Building Docs
pip install -r docs/requirements.txt
find . -name \*.py |xargs sed -i "s#https://docs\.cloud\.oracle\.com/en-us/iaas/tools/python-sdk-examples/latest/#https://docs\.cloud\.oracle\.com/en-us/iaas/tools/python-sdk-examples/$SDK_VERSION/#g"

# Redirect STDOUT and STDERR to a file to avoid resource unavailable error in TeamCity jobs.
make docs >> doc_build_output.txt 2>&1

# a hyperlinks mismatch will cause all of the links on readthedocs to break
if cat doc_build_output.txt | grep -q "ERROR: Anonymous hyperlink mismatch";  then
    echo "Failing due to error building docs with sphinx.";
    exit 1;
else
    echo "No critical errors found during sphinx build.";
fi

mkdir -p dist/oci-python-sdk-docs-$SDK_VERSION/
cp -r docs/_build/html/* dist/oci-python-sdk-docs-$SDK_VERSION/

echo Running Tests

if [ $TEST_ENABLE = "false" ]; then
  echo "TESTS HAVE BEEN DISABLED."
else
  pip install -r requirements.txt
  tox -e flake8,py36 -- --vcr-record-mode=none
fi

echo installing Wheel
pip install wheel

echo Building Wheel
# Redirect STDOUT and STDERR to a file to avoid resource unavailable error in TeamCity jobs.
make build >> doc_build_output.txt 2>&1

# Delete doc_build_output.txt
rm doc_build_output.txt

# Create a dev directory that will contain versions of the whl, zip, and docs meant for
# the dev pypi artifactory. Each artifact includes the build number in the version to avoid
# conflicts.
mkdir -p dist/dev/
if [ $IS_SNAPSHOT = "true" ]; then
  cp dist/oci-$DEV_VERSION-py3-none-any.whl dist/dev/oci-$DEV_VERSION-py3-none-any.whl
  cp dist/oci-python-sdk-$DEV_VERSION.zip dist/dev/oci-python-sdk-$DEV_VERSION.zip
else
  cp dist/oci-$SDK_VERSION-py3-none-any.whl dist/dev/oci-$DEV_VERSION-py3-none-any.whl
  cp dist/oci-python-sdk-$SDK_VERSION.zip dist/dev/oci-python-sdk-$DEV_VERSION.zip
fi

pushd dist/oci-python-sdk-docs-$SDK_VERSION
zip -r ../oci-python-sdk-docs-$SDK_VERSION.zip .
popd
cp dist/oci-python-sdk-docs-$SDK_VERSION.zip dist/dev/oci-python-sdk-docs-$DEV_VERSION.zip


echo Contents of dist folder
ls -la dist
