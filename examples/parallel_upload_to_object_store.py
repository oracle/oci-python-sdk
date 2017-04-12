# Uploads all files from a local directory to an object store bucket
# using multiple processes so that the uploads are done in parallel.
#
# Assumptions: Local directory is /tmp/bmc_copy.
#              Bucket already exists. See object_crud.py for bucket creation
#                 example.

import oraclebmc
import os
from multiprocessing import Process
from glob import glob

bucket_name = "python-sdk-example-bucket"
tmp_dir = "/tmp/bmc_copy"
config = oraclebmc.config.from_file()
compartment_id = config["tenancy"]
object_storage = oraclebmc.object_storage.ObjectStorageClient(config)
namespace = object_storage.get_namespace().data


def upload_to_object_store(path):
    in_file = open(path, "rb")
    data = in_file.read()
    name = os.path.basename(path)
    ostore = oraclebmc.object_storage.ObjectStorageClient(config)
    ostore.put_object(namespace,
                      bucket_name,
                      name,
                      data)
    print("Finished uploading {}".format(name))

proc_list = []
for file_path in glob(tmp_dir + '/*'):
    print("starting upload for {}".format(file_path))
    p = Process(target=upload_to_object_store, args=(file_path,))
    p.start()
    proc_list.append(p)

for job in proc_list:
    job.join()
