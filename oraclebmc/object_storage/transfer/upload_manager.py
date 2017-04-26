# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import os
from .multipart_object_assembler import MultipartObjectAssembler
from .constants import DEFAULT_PART_SIZE
from .constants import OBJECT_USE_MULTIPART_SIZE


class UploadManager:
    @staticmethod
    def upload(object_storage_client,
               namespace_name,
               bucket_name,
               object_name,
               file,
               part_size=DEFAULT_PART_SIZE):

        if part_size < OBJECT_USE_MULTIPART_SIZE or \
                        os.fstat(file.fileno()).st_size >= OBJECT_USE_MULTIPART_SIZE:

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
        else:
            # TODO: Add single part upload
            pass

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
