# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Uploads all files from a local directory to an object storage bucket
# using multiple processes so that the uploads are done in parallel.
#
# Assumptions: Object storage bucket already exists. See object_crud.py for
#                an example of creating a bucket.
#              Loads configuration from default profile in the default config
#                file

import oci
import os
import argparse
from multiprocessing import Process
from glob import glob


def upload_to_object_storage(config, namespace, bucket, path):
    """
    upload_to_object_storage will upload a file to an object storage bucket.
    This function is intended to be run as a separate process.  The client is
    created with each invocation so that the separate processes do
    not have a reference to the same client.

    :param config: a configuration dictionary used to create ObjectStorageClient
    :param namespace: Namespace where the bucket resides
    :param bucket: Name of the bucket in which the object will be stored
    :param path: path to file to upload to object storage
    :rtype: None
    """
    with open(path, "rb") as in_file:
        name = os.path.basename(path)
        ostorage = oci.object_storage.ObjectStorageClient(config)
        ostorage.put_object(namespace,
                            bucket,
                            name,
                            in_file)
        print("Finished uploading {}".format(name))


if __name__ == "__main__":
    config = oci.config.from_file()
    object_storage = oci.object_storage.ObjectStorageClient(config)
    namespace = object_storage.get_namespace().data

    description = "\n".join(["This is an example to show how multiple files can be uploaded to in",
                             "parallel. The example uses multiple processes.",
                             "",
                             "All the files in 'directory' will be uploaded to the object storage bucket",
                             "specified by 'bucket_name'  The default profile is used.",
                             "",
                             "The bucket must already exist. See object_crud.py for a bucket creation",
                             "example."])

    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(dest='bucket_name',
                        help="Name of object storage bucket")
    parser.add_argument(dest='directory',
                        help="Path to local directory containing files to upload. Do not include trailing path delimiter.")
    args = parser.parse_args()

    bucket_name = args.bucket_name
    directory = args.directory
    if not os.path.isdir(directory):
        parser.usage()
    else:
        dir = directory + os.path.sep + "*"

    proc_list = []
    for file_path in glob(dir):
        print("Starting upload for {}".format(file_path))
        p = Process(target=upload_to_object_storage, args=(config,
                                                           namespace,
                                                           args.bucket_name,
                                                           file_path))
        p.start()
        proc_list.append(p)

    for job in proc_list:
        job.join()
