import oraclebmc
import io
# from oraclebmc.object_storage.models import CreateBucketDetails

bucket_name = "DEX-836_multipart_uploads"
tmp_dir = "/tmp"
config = oraclebmc.config.from_file()
compartment_id = config["tenancy"]
object_storage = oraclebmc.object_storage.ObjectStorageClient(config)
namespace_name = object_storage.get_namespace().data
object_name = "song.mp3"

# Create bucket
# Uncomment this code if the bucket doesn't already exist
# request = CreateBucketDetails()
# request.compartment_id = compartment_id
# request.name = bucket_name
# bucket = object_storage.create_bucket(namespace_name, request)

chunk = 1000000
test = oraclebmc.MultipartAssembler(object_storage, namespace_name, bucket_name, object_name)
test.new_upload()

# add parts
filename = tmp_dir + '/' + object_name
with io.open(filename, mode='rb') as file:
    file.seek(0, io.SEEK_END)
    end = file.tell()
    file.seek(0, io.SEEK_SET)
    offset = 0
    while file.tell() < end:
        test.add_part(filename, offset=offset, chunk=chunk)
        offset += chunk
        file.seek(offset, io.SEEK_SET)

try:
    test.upload()
except Exception:
    test.abort_upload()
else:
    test.commit()

print(test.manifest)

