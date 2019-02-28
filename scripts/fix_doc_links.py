#!/usr/bin/env python

# This script runs at the end of the code generation process and replaces any incorrect
# references to https://ocs.us-phoenix-1.oraclecloud.com with https://docs.cloud.oracle.com

import os
import os.path
import sys

FIND_VALUE = 'docs.us-phoenix-1.oraclecloud.com'
REPLACE_VALUE = 'docs.cloud.oracle.com'
INCLUDED_PATHS = ['examples{}'.format(os.sep),
                  'src{}'.format(os.sep),
                  'tests{}'.format(os.sep)]

base_path = sys.argv[1]


def is_file_in_included_paths(file_path):
    for p in INCLUDED_PATHS:
        if p in file_path:
            return True
    return False


def do_skip_file(file_path):
    # Always skip the '.git' folder in case INCLUDED_PATHS above is contained within
    if '.git' in file_path:
        return True

    if not file_path.endswith('.py'):
        return True

    # Do not process any files not specified in INCLUDED_PATHS
    if not is_file_in_included_paths(file_path):
        return True

    return False


print('Processing directory {}'.format(base_path))
for dir_path, dir_names, file_names in os.walk(base_path):
    for f in file_names:
        file_path = os.path.join(dir_path, f)

        if do_skip_file(file_path):
            continue

        # Input
        print('Processing {}'.format(file_path))
        with open(file_path, 'r') as file:
            content = file.read()

        # Process
        filtered_content = content.replace(FIND_VALUE, REPLACE_VALUE)

        # Output
        with open(file_path, 'w') as file:
            file.write(filtered_content)

print('Link correction complete')
