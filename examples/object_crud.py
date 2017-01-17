import oraclebmc
from oraclebmc.object_storage.models import CreateBucketDetails


config = oraclebmc.config.from_file()
compartment_id = config["tenancy"]
object_storage = oraclebmc.object_storage.ObjectStorageClient(config)

namespace = object_storage.get_namespace().data
bucket_name = "python-sdk-example-bucket"
object_name = "python-sdk-example-object"
my_data = b"Hello, World!"

print("Creating a new bucket {!r} in compartment {!r}".format(
    bucket_name, compartment_id))
request = CreateBucketDetails()
request.compartment_id = compartment_id
request.name = bucket_name
bucket = object_storage.create_bucket(namespace, request)

print("Uploading new object {!r}".format(object_name))
obj = object_storage.put_object(
    namespace,
    bucket_name,
    object_name,
    my_data)

same_obj = object_storage.get_object(
    namespace,
    bucket_name,
    object_name)

print("{!r} == {!r}: {}".format(
    my_data, same_obj.data.content,
    my_data == same_obj.data.content))

print("Deleting object {}".format(object_name))
object_storage.delete_object(namespace, bucket_name, object_name)

print("Deleting bucket {}".format(bucket_name))
object_storage.delete_bucket(namespace, bucket_name)
