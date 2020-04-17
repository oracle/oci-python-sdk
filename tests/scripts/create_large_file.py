# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
