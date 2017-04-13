# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.
#
# Uploads all files from a local directory to an object store bucket
# using multiple processes so that the uploads are done in parallel.
#
# Assumptions: Object store bucket already exists. See object_crud.py for
# example of creating a bucket.

import oraclebmc
import os
import argparse
from multiprocessing import Process
from glob import glob


def upload_to_object_store(config, namespace, bucket, path):
    """
    upload_to_object_store will upload a file to a object store bucket.
    This function is intended to be run as a separate process.  The client is
    created with each invocation so that the separate processes do
    not have a reference to the same object.
    
    :param config: a configuration dictionary used to create ObjectStorageClient
    :param namespace: Namespace where the bucket resides
    :param bucket: Name of the bucket in which the object will be stored
    :param path: path to file to upload to object store
    :rtype: None
    """
    in_file = open(path, "rb")
    data = in_file.read()
    name = os.path.basename(path)
    ostore = oraclebmc.object_storage.ObjectStorageClient(config)
    ostore.put_object(namespace,
                      bucket,
                      name,
                      data)
    print("Finished uploading {}".format(name))

if __name__ == "__main__":
    config = oraclebmc.config.from_file()
    object_storage = oraclebmc.object_storage.ObjectStorageClient(config)
    namespace = object_storage.get_namespace().data

    description = \
"""This is an example to show how multiple files can be uploaded to in
parallel. The example uses multiple processes.

All the files in 'directory' will be uploaded to the object store bucket
specified by 'bucket_name'  The default profile will is used.
    
The bucket must already exists. See object_crud.py for a bucket creation
example.
"""
    epilog = "Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved."

    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=epilog)
    parser.add_argument(dest='bucket_name',
                        help="Name of object store bucket")
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
        p = Process(target=upload_to_object_store, args=(config,
                                                         namespace,
                                                         args.bucket_name,
                                                         file_path))
        p.start()
        proc_list.append(p)

    for job in proc_list:
        job.join()
