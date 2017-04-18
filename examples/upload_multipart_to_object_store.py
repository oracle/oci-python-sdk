import oraclebmc
import sys

bucket_name = "DEX-836_multipart_uploads"
tmp_dir = "/tmp"
config = oraclebmc.config.from_file()
compartment_id = config["tenancy"]
object_storage = oraclebmc.object_storage.ObjectStorageClient(config)
namespace_name = object_storage.get_namespace().data
object_name = "song.mp3"

# TODO: Flesh this out to be a valid example.


def create_bucket():
    # Create bucket
    from oraclebmc.object_storage.models import CreateBucketDetails
    request = CreateBucketDetails()
    request.compartment_id = compartment_id
    request.name = bucket_name
    object_storage.create_bucket(namespace_name, request)


def upload_multipart():
    part_size = 1500000
    test = oraclebmc.MultipartAssembler(object_storage, namespace_name, bucket_name, object_name, part_size=part_size)
    test.new_upload()

    # add parts
    filepath = tmp_dir + '/' + object_name
    test.add_parts_from_file(filepath=filepath)

    try:
        test.upload()
    except Exception:
        test.abort()
    else:
        test.commit()

    print(test.manifest, file=sys.stderr)


def resume_multipart(upload_id):
    part_size = 1500000
    test = oraclebmc.MultipartAssembler(object_storage, namespace_name, bucket_name, object_name, part_size=part_size)
    # add parts
    filepath = tmp_dir + '/' + object_name
    test.add_parts_from_file(filepath=filepath)
    test.resume(upload_id=upload_id)
    test.commit()


if __name__ == "__main__":
    # create_bucket()
    # upload_multipart()
    resume_multipart("97fd0622-0d27-8cac-9f7b-e9a8afdc490a")
