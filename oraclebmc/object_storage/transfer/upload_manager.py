# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import os
from .multipart_object_assembler import MultipartObjectAssembler
from .constants import DEFAULT_PART_SIZE

# TODO: Add docstrings to everything.
# TODO: Warn if the content_md5 is set and the multipart upload is chosen.
#       Replicate JavaSDK behavior for the warning.


class UploadManager:
    @staticmethod
    def upload(object_storage_client,
               namespace_name,
               bucket_name,
               object_name,
               file_object,
               **kwargs):

        progress = None
        if 'progress' in kwargs:
            progress = kwargs['progress']
            kwargs.pop('progress')

        no_multipart = False
        if 'no_multipart' in kwargs:
            no_multipart = kwargs['no_multipart']
            kwargs.pop('no_multipart')

        part_size = DEFAULT_PART_SIZE
        if 'part_size' in kwargs:
            part_size = kwargs['part_size']
            kwargs.pop('part_size')

        file_size = os.fstat(file_object.fileno()).st_size
        if file_size < part_size or no_multipart:
            # put_object expects 'opc_meta' not metadata
            if 'metadata' in kwargs:
                kwargs['opc_meta'] = kwargs['metadata']
                kwargs.pop('metadata')
            if progress:
                wrapped_file = FileReadCallbackStream(file_object, lambda bytes_read: progress.update(bytes_read))
                response = object_storage_client.put_object(namespace_name,
                                                            bucket_name,
                                                            object_name,
                                                            wrapped_file,
                                                            **kwargs)
            else:
                response = object_storage_client.put_object(namespace_name, bucket_name, object_name, file_object, **kwargs)
        else:
            kwargs['part_size'] = part_size
            kwargs['progress'] = progress

            ma = MultipartObjectAssembler(object_storage_client,
                                          namespace_name,
                                          bucket_name,
                                          object_name,
                                          **kwargs)
            ma.new_upload()
            if progress:
                progress.label = "Upload ID: {}".format(ma.manifest["uploadId"])
                progress.update(0)
            # file_object is a buffered reader when coming from CLI, so we need access to the underlying file.
            # TODO: make this more generic for non-CLI uses.
            ma.add_parts_from_file(file_object.name)
            ma.upload()
            response = ma.commit()

        return response

    @staticmethod
    def resume(object_storage_client,
               namespace_name,
               bucket_name,
               object_name,
               file_object,
               upload_id,
               **kwargs):

        ma = MultipartObjectAssembler(object_storage_client,
                                      namespace_name,
                                      bucket_name,
                                      object_name,
                                      **kwargs)
        ma.add_parts_from_file(filepath=file_object.name)
        ma.resume(upload_id=upload_id)
        response = ma.commit()

        return response


class FileReadCallbackStream:
    def __init__(self, file, progress_callback):
        self.progress_callback = progress_callback
        self.file = file
        self.mode = file.mode

    # this is used by 'requests' to determine the Content-Length header using fstat
    def fileno(self):
        return self.file.fileno()

    def read(self, n):
        self.progress_callback(n)
        return self.file.read(n)
