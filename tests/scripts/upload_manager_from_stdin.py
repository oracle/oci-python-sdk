# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import sys

if len(sys.argv) != 7:
    print(
        """
        Please provide a configuration file (first argument), profile name (second argument), key passhrase (third argument),
        Object Storage namespace (fourth argument), bucket (fifth argument) and object name (sixth argument)
        """
    )
    exit(1)

config_file_path = sys.argv[1]
profile_name = sys.argv[2]
pass_phrase = sys.argv[3]
namespace = sys.argv[4]
bucket_name = sys.argv[5]
object_name = sys.argv[6]

config = oci.config.from_file(file_location=config_file_path, profile_name=profile_name)
config['pass_phrase'] = pass_phrase
object_storage_client = oci.object_storage.ObjectStorageClient(config)

upload_manager = oci.object_storage.UploadManager(
    object_storage_client,
    parallel_process_count=10
)

response = upload_manager.upload_stream(
    namespace,
    bucket_name,
    object_name,
    sys.stdin
)
