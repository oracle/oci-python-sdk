import oci
import os.path
import sys

# This script is intended to run as part of the docs Make target
# That target assumes the working package has been installed using
# pip install -e .
#
# Assumptions:
#      working directory contains CHANGELOG.txt
#      The CHANGELOG.rst has the following format:
#          any number of lines
#          a line that starts with "=====" followed by a line with the version number in the following format
#          1.4.0 - 2018-05-17
#


# get the version number of the installed oci package.
oci_version = oci.__version__

# get the changelog
current_directory = "."
changelog = os.path.join(current_directory, "CHANGELOG.rst")
with open(changelog, mode='r') as f:
    for line in f:
        if line.startswith("====="):
            changelog_version = f.readline().split(" ")[0]
            break

if oci_version != changelog_version:
    print("The OCI version is {} and the CHANGELOG.rst version is {}.  Please correct one of them.".format(oci_version, changelog_version))
    sys.exit(1)
