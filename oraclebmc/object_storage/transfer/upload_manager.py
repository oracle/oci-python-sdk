from multipart_object_assembler import MultipartObjectAssembler
from constants import DEFAULT_PART_SIZE


class UploadManager:
    @staticmethod
    def upload(object_storage_client,
               namespace_name,
               bucket_name,
               object_name,
               file,
               part_size=DEFAULT_PART_SIZE):

        ma = MultipartObjectAssembler(object_storage_client, namespace_name, bucket_name, object_name, part_size)
        ma.new_upload()

        # add parts
        ma.add_parts_from_file(filepath=file.name)

        try:
            ma.upload()
        except Exception as e:
            raise e
        else:
            ma.commit()

    @staticmethod
    def resume(object_storage_client,
               namespace_name,
               bucket_name,
               object_name,
               file,
               upload_id,
               part_size=DEFAULT_PART_SIZE):

        ma = MultipartObjectAssembler(object_storage_client, namespace_name, bucket_name, object_name, part_size=part_size)
        ma.add_parts_from_file(filepath=file.name)
        ma.resume(upload_id=upload_id)
        ma.commit()
