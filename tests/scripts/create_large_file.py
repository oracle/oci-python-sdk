# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from oci.object_storage.transfer.constants import MEBIBYTE

import sys


if len(sys.argv) != 3:
    print('Please provide the path to the file to write content to (first argument) and desired size in MiB (second argument)')
    exit(1)

file_path = sys.argv[1]
size_in_mebibytes = int(sys.argv[2])

sample_content = b'a'
with open(file_path, 'wb') as f:
    f.write(sample_content * MEBIBYTE * size_in_mebibytes)
