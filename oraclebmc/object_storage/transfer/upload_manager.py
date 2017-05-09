# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import sys
import os
import six
from .multipart_object_assembler import MultipartObjectAssembler
from .constants import DEFAULT_PART_SIZE

# TODO: update docstring for progress, change the value to progress_callback


class UploadManager:
    @staticmethod
    def upload(object_storage_client,
               namespace_name,
               bucket_name,
               object_name,
               file_object,
               **kwargs):

        """
        Uploads an object to Object Storage. Depending on the options provided and the
        size of the object, the object may be uploaded in multiple parts.

        :param object object_storage_client:
            A configured Object Storage client

        :param str namespace_name:
            The namespace containing the bucket and multipart upload

        :param str bucket_name:
            The name of the bucket in which to store the object

        :param str object_name:
            The name of the object in Object Storage

        :param file_object:
            A file like object that has a name attribute

        :param boolean no_multipart (optional):
            Force the object to be uploaded as a single part

        :param int part_size (optional):
            Override the default part size of 128 MiB.

        :param function progress:
            Callback function which will receive the number of bytes transferred.

        :return:
            The response from multipart commit operation or the put operation.
        """
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

            # TODO: make this more generic and ensure it is done the same way
            # on raw put and removed on get.
            # prefix the keys in metadata with 'opc-meta-'
            if 'metadata' in kwargs:
                processed_metadata = {}
                for key, value in six.iteritems(kwargs.get("metadata", {})):
                    if not key.startswith('opc-meta-'):
                        processed_metadata["opc-meta-" + key] = value
                    else:
                        processed_metadata[key] = value
                kwargs['metadata'] = processed_metadata

            # TODO: Provide a better way to warn about the usage of content-md5
            #       with multipart.
            if 'content_md5' in kwargs:
                print('Warning: The --content-md5 option cannot be used with multipart uploads. It will be ignored.',
                      file=sys.stderr)

            ma = MultipartObjectAssembler(object_storage_client,
                                          namespace_name,
                                          bucket_name,
                                          object_name,
                                          **kwargs)
            ma.new_upload()
            # TODO: provide a better way to notify the CLI user of the upload id
            print("Upload ID: {}".format(ma.manifest["uploadId"]), file=sys.stderr)

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

        """
        Resume a multipart upload.

        :param object object_storage_client:
            A configured Object Storage client

        :param str namespace_name:
            The namespace containing the bucket and multipart upload to resume

        :param str bucket_name:
            The name of the bucket that contains the multipart upload to resume

        :param str object_name:
            The name of the object in Object Storage

        :param file_object:
            A file like object that has a name attribute

        :param str upload_id:
            The upload-id for the multipart upload to resume

        :param int part_size (optional):
            Part size, in mebibytes, to use when resuming the transfer. The
            default is 128 mebibytes.  If this value is supplied, it must
            be the same value as the one used when the original upload
            was started.

        :param function progress:
            Callback function which will receive the number of bytes transferred.

        :return:
            The response from the multipart commit operation
        """
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
