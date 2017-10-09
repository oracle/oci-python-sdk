# this script requires having 2 VCS roots checked out at the following directories
#   python-sdk (master) -> oci 
#   python-sdk (oraclebmc) -> oraclebmc

# note we are not publishing this branch to github or RTD so we only care about directories that will end up publicly
# exposed (for example, we dont care about the docs/ folder)

set -x 
set -e

ls -la

# remove all files under oraclebmc/src/oraclebmc to prepare for new files (this will persist deletes made in master)
rm -rf oraclebmc/src/oraclebmc
mkdir oraclebmc/src/oraclebmc

rm -rf oraclebmc/examples
mkdir oraclebmc/examples

rm -rf oraclebmc/tests
mkdir oraclebmc/tests

# first we copy all of the changes from oci/src/oci/* oraclebmc/src/oraclebmc/*
cp -r oci/src/oci/* oraclebmc/src/oraclebmc/

# also copy the examples since we include those in the zip
cp -r oci/examples/* oraclebmc/examples/

# and also copy the tests because we want to make sure we run any new tests against this package
cp -r oci/tests/* oraclebmc/tests/

# now oraclebmc/src/oraclebmc will have a bunch of files that have oci references so fix those with sed
grep -rl 'oci' oraclebmc/ | xargs sed -i 's/oci\./oraclebmc\./g'
grep -rl 'import oci' oraclebmc/ | xargs sed -i 's/import oci/import oraclebmc/g'
grep -rl 'from oci' oraclebmc/ | xargs sed -i 's/from oci/from oraclebmc/g'

# explicitly remove files from source dir that we don't want to copy
# NOTE: change in these files WILL NOT be ported to oraclebmc, so if we need them they must be manually ported
rm oci/CHANGELOG.rst
rm oci/CONTRIBUTING.rst
rm oci/github.whitelist
rm oci/Internal-README.rst
rm oci/pom.xml
rm oci/README.rst
rm oci/setup.py

# copy files from the root directory
cp oci/*.* oraclebmc/

# Inject a warning into the oraclebmc init file
cat << EOF >> src/oraclebmc/__init__.py

import warnings
warnings.warn("The oraclebmc package is deprecated and will no longer be maintained starting March 2018. Please upgrade to the oci package to avoid interruption at that time. More info is available at https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/backward-compatibility.html", DeprecationWarning, stacklevel=2)
EOF

# create PR for oraclebmc/ branch to port changes
cd oraclebmc

UNIQUE_BRANCH_NAME=oci-oraclebmc-sync-$(date +%%Y-%%m-%%d-%%H-%%M-%%S)
git checkout -b $UNIQUE_BRANCH_NAME

# must disable StrictHostKeyChecking so that we don't get an interactive
# prompt later asking to confirm the host key
ls -la ~/.ssh

cat ~/.ssh/config

printf "\n\nHost * \n  StrictHostKeyChecking no\n" >> ~/.ssh/config

cat ~/.ssh/config

# configure git for this commit
git config user.email "$GIT_USER_EMAIL"
git config user.name "$GIT_USER_NAME"

git status
git add --all .
git commit -m "Syncing changes from master branch to oraclebmc branch"
git push -u origin HEAD
echo "Create a pull request from $UNIQUE_BRANCH_NAME to oraclebmc."
cd ..