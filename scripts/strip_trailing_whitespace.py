#!/usr/bin/env python

# This script runs at the end of the code generation process and strips any trailing
# whitespace (which would otherwise cause Rubocop to complain). This is a bit hacky
# but it's easier than messing around with mustache templates

import os
import os.path

SOURCE_CODE_LOCAITON = 'src/oci'

for dirpath, dirnames, filenames in os.walk(SOURCE_CODE_LOCAITON):
    for f in filenames:
        file_path = os.path.join(dirpath, f)
        print('Stripping whitespace from {}'.format(file_path))
        with open(file_path, 'r') as file:
            content = file.readlines()

        stripped_content = [c.rstrip() for c in content]
        with open(file_path, 'w') as file:
            for c in stripped_content:
                file.write('{}\n'.format(c))

print('Whitespace stripping complete')
