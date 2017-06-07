# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import io
import hashlib
import base64
from multiprocessing.dummy import Pool
from os import stat
from ..constants import DEFAULT_PART_SIZE
from ..constants import MEBIBYTE
from .buffered_part_reader import BufferedPartReader
from ... import models
from ....exceptions import ServiceError
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
import six

READ_BUFFER_SIZE = 8 * 1024
DEFAULT_PARALLEL_PROCESS_COUNT = 3
DEFAULT_MAX_RETRIES = 3


class MultipartObjectAssembler:
    def __init__(self,
                 object_storage_client,
                 namespace_name,
                 bucket_name,
                 object_name,
                 **kwargs
                 ):
        """
        MultipartObjectAssembler provides a simplified interaction when uploading large
        objects using multi-part uploads.

        An assembler can be used to begin a new upload, or resume a previous one.

        :param ObjectStorageClient object_storage_client:
            A configured Object Storage client.

        :param str namespace_name:
            The namespace containing the bucket in which to store the object.

        :param str bucket_name:
            The name of the bucket in which to store the object.

        :param str object_name:
            The name to use for the object in Object Storage, or existing object name if resuming.

        :param int part_size (optional):
            Override the default part size of 128 MiB, value is in bytes.

        :param str if_match (optional):
            The entity tag of the object to match.

        :param str if_none_match (optional):
            The entity tag of the object to avoid matching. The only valid value is ‘*’,
            which indicates that the request should fail if the object
             already exists.

        :param str content_type (optional):
            The content type of the object to upload.

        :param str content_language (optional):
            The content language of the object to upload.

        :param str content_encoding (optional):
            The content encoding of the object to upload.

        :param dict metadata (optional):
            A dictionary of string to string values to associate with the object to upload

        :param bool allow_parallel_uploads (optional):
            Whether or not this MultipartObjectAssembler supports uploading parts in parallel. Defaults to True.

        :param int parallel_process_count (optional):
            The number of worker processes to use in parallel for performing a multipart upload. Default is 3.
        """
        self.object_storage_client = object_storage_client

        self.part_size = DEFAULT_PART_SIZE
        if 'part_size' in kwargs:
            self.part_size = kwargs['part_size']
        self.if_match = None
        if 'if_match' in kwargs:
            self.if_match = kwargs['if_match']
        self.if_none_match = None
        if 'if_none_match' in kwargs:
            self.if_none_match = kwargs['if_none_match']
        self.content_type = None
        if 'content_type' in kwargs:
            self.content_type = kwargs['content_type']
        self.content_language = None
        if 'content_language' in kwargs:
            self.content_language = kwargs['content_language']
        self.content_encoding = None
        if 'content_encoding' in kwargs:
            self.content_encoding = kwargs['content_encoding']
        self.metadata = None
        if 'metadata' in kwargs:
            self.metadata = kwargs['metadata']

        self.parallel_process_count = DEFAULT_PARALLEL_PROCESS_COUNT
        if 'parallel_process_count' in kwargs:
            if kwargs['parallel_process_count'] == 0:
                raise ValueError('parallel_process_count must be at least one.')

            self.parallel_process_count = kwargs['parallel_process_count']

        if 'allow_parallel_uploads' in kwargs and kwargs['allow_parallel_uploads'] is False:
            # if parallel uploads are disabled, use only a single process
            self.parallel_process_count = 1

        self.max_retries = DEFAULT_MAX_RETRIES
        self.manifest = {"uploadId": None,
                         "namespace": namespace_name,
                         "bucketName": bucket_name,
                         "objectName": object_name,
                         "parts": []}

    @staticmethod
    def calculate_md5(file_path, offset, chunk):
        """
        Calculate the base64 encoded MD5 hash for a part of a file.

        :param str file_path: Path to the file
        :param int offset: Offset where the part starts in the file
        :param int chunk: Number of bytes in the part
        :return: Base64 encoded MD5 hash
        :rtype: str
        """
        m = hashlib.md5()
        with io.open(file_path, mode='rb') as f:
            bpr = BufferedPartReader(f, offset, chunk)
            while True:
                part = bpr.read(READ_BUFFER_SIZE)
                if part == b'':
                    break
                m.update(part)
        return base64.b64encode(m.digest()).decode("utf-8")

    @staticmethod
    def _is_exception_retryable(e):
        """
        Determines if the service should attempt to retry an operation based
         on the type of exception

        retry if
           timeout
           Connection error
           unknown client exception: status == -1
           server exception: status >= 500
           Potential edge case: status == 409

        :param e: Exception
        :return: Boolean
        """
        retryable = False
        if isinstance(e, Timeout):
            retryable = True
        elif isinstance(e, ConnectionError):
            retryable = True
        elif isinstance(e, ServiceError):
            if e.status >= 500 or e.status == -1 or (e.status == 409 and e.code == "ConcurrentObjectUpdate"):
                retryable = True

        return retryable

    def add_parts_from_file(self, file_path):
        """
        Splits a file into parts and adds all parts to an internal list of parts to upload.  The parts will not be uploaded to the server until upload is called.

        :param string file_path: Path of file to upload in parts
        """
        with io.open(file_path, mode='rb') as file_object:
            file_object.seek(0, io.SEEK_END)
            end = file_object.tell()
            file_object.seek(0, io.SEEK_SET)
            offset = 0
            while file_object.tell() < end:
                self.add_part_from_file(file_path, offset=offset, size=self.part_size)
                offset += self.part_size
                file_object.seek(offset, io.SEEK_SET)

    def add_part_from_file(self,
                           file_path,
                           offset=0,
                           size=None,
                           part_hash=None):
        """
        Add a part to internal list of parts to upload.  The part will not be uploaded to the server until upload is called.

        :param str file_path: Path to file
        :param offset: Offset of part in file
        :param size: Size of the part in bytes
        :param part_hash: Base64 encoded MD5 hash of the part
        """
        if size is None:
            size = stat(file_path).st_size

        self.manifest["parts"].append({"file_path": file_path,
                                       "offset": offset,
                                       "size": size,
                                       "hash": part_hash})

    def abort(self, **kwargs):
        """
        Abort the multipart upload

        :param str upload_id (optional): The upload id to abort. If not provided, will attempt to abort the upload created internally by new_upload.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing
        """
        if 'upload_id' in kwargs:
            self.manifest["uploadId"] = kwargs['upload_id']
            kwargs.pop('upload_id')

        if not self.manifest["uploadId"]:
            raise ValueError("Cannot abort without an upload id.")

        self.object_storage_client.abort_multipart_upload(self.manifest["namespace"],
                                                          self.manifest["bucketName"],
                                                          self.manifest["objectName"],
                                                          self.manifest["uploadId"],
                                                          **kwargs)

    def resume(self, **kwargs):
        """
       Resume uploading a multipart object to Object Storage

       :param str upload_id (optional): The upload id to resume. If not provided, will attempt to resume the upload created internally by new_upload.

       :param function progress_callback (optional):
            Callback function to receive the number of bytes uploaded since
            the last call to the callback function.

       :param str opc_client_request_id: (optional)
            The client request ID for tracing
       """
        if 'upload_id' in kwargs:
            self.manifest["uploadId"] = kwargs['upload_id']
            kwargs.pop('upload_id')

        # Verify that the upload id is valid
        if self.manifest["uploadId"] is None:
            raise ValueError("Cannot resume without an upload id.")

        upload_kwargs = {}
        if 'progress_callback' in kwargs:
            upload_kwargs['progress_callback'] = kwargs['progress_callback']
            kwargs.pop('progress_callback')

        # Get parts details from object storage to see which parts didn't complete
        has_next_page = True
        while has_next_page:
            response = self.object_storage_client.list_multipart_upload_parts(self.manifest["namespace"],
                                                                              self.manifest["bucketName"],
                                                                              self.manifest["objectName"],
                                                                              self.manifest["uploadId"],
                                                                              **kwargs)
            # Update manifest with information from object storage
            parts = self.manifest["parts"]
            for part in response.data:
                part_index = part.part_number - 1
                if -1 < part_index < len(parts):
                    manifest_part = parts[part_index]
                    if manifest_part["size"] != part.size:
                        raise ValueError('Cannot resume upload with different part size. Parts were uploaded with a part size of {} MiB'.format(part.size / MEBIBYTE))
                    manifest_part["etag"] = part.etag
                    manifest_part["opc_md5"] = part.md5
                elif part_index >= len(parts):
                    raise ValueError('There are more parts on the server than parts to resume, please check the upload ID.')
            has_next_page = response.has_next_page
            kwargs['page'] = response.next_page

        # Upload parts that are missing or incomplete
        self.upload(**upload_kwargs)

    def new_upload(self, **kwargs):
        """
        Create a new multipart upload in Object Storage and add the upload
        id to the manifest

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.
        """
        if self.manifest['uploadId']:
            raise RuntimeError('Cannot call new_upload again once an upload has already been created.')

        request = models.CreateMultipartUploadDetails()
        request.object = self.manifest["objectName"]
        if self.content_type:
            request.content_type = self.content_type
        if self.content_language:
            request.content_language = self.content_language
        if self.content_encoding:
            request.content_encoding = self.content_encoding
        if self.metadata:
            # TODO: look into moving this into codegen for create_multipart_upload like it is for put_object
            processed_metadata = {}
            for key, value in six.iteritems(self.metadata):
                if not key.startswith('opc-meta-'):
                    processed_metadata["opc-meta-" + key] = value
                else:
                    processed_metadata[key] = value
            self.metadata = processed_metadata

            request.metadata = self.metadata

        client_request_id = None
        if 'opc_client_request_id' in kwargs:
            client_request_id = kwargs['opc_client_request_id']

        kwargs = {}
        if client_request_id:
            kwargs['opc_client_request_id'] = client_request_id
        if self.if_match:
            kwargs['if_match'] = self.if_match
        if self.if_none_match:
            kwargs['if_none_match'] = self.if_none_match

        response = self.object_storage_client.create_multipart_upload(self.manifest["namespace"],
                                                                      self.manifest["bucketName"],
                                                                      request,
                                                                      **kwargs)

        self.manifest["uploadId"] = response.data.upload_id

    def _upload_part(self, part_num, part, **kwargs):
        """
        Upload a part to Object Storage

        :param int part_num: Sequence number for where this part belongs in the
                             multipart object.
        :param dict part: Part dictionary containing the following keys: "file_path" (str), "hash" (str), "offset" (int), and "size" (int)
        :param str opc_client_request_id: (optional)
            The client request ID for tracing.
        :param function progress_callback (optional):
            Callback function to receive the number of bytes uploaded since
            the last call to the callback function.
        """
        new_kwargs = {'content_md5': part["hash"]}
        if 'opc_client_request_id' in kwargs:
            new_kwargs['opc_client_request_id'] = kwargs['opc_client_request_id']

        # TODO: Calculate the hash without needing to read the file chunk twice.
        # Calculate the hash before uploading.  The hash will be used
        # to determine if the part needs to be uploaded.  It will also
        # be used to determine if there is a conflict between parts that
        # have previously been uploaded.
        if part["hash"] is None:
            part["hash"] = self.calculate_md5(part["file_path"], part["offset"], part["size"])

        if "opc_md5" not in part:
            remaining_tries = self.max_retries
            while remaining_tries > 0:
                with io.open(part["file_path"], mode='rb') as file_object:
                    bpr = BufferedPartReader(file_object, part["offset"], part["size"])
                    try:
                        response = self.object_storage_client.upload_part(self.manifest["namespace"],
                                                                          self.manifest["bucketName"],
                                                                          self.manifest["objectName"],
                                                                          self.manifest["uploadId"],
                                                                          part_num,
                                                                          bpr,
                                                                          **new_kwargs)
                    except Exception as e:
                        if self._is_exception_retryable(e) and remaining_tries > 1:
                            remaining_tries -= 1
                        else:
                            raise
                    else:
                        break

            if response.status == 200:
                part["etag"] = response.headers['etag']
                part["opc_md5"] = str(response.headers['opc-content-md5'])

        if 'progress_callback' in kwargs:
            kwargs['progress_callback'](part["size"])

    def upload(self, **kwargs):
        """
        Upload an object to Object Storage

        :param function progress_callback (optional):
            Callback function to receive the number of bytes uploaded since
            the last call to the callback function.
        :param str opc_client_request_id: (optional)
            The client request ID for tracing.
        """
        if self.manifest["uploadId"] is None:
            raise RuntimeError('Cannot call upload before initializing an upload using new_upload.')

        pool = Pool(processes=self.parallel_process_count)
        pool.map(lambda part_tuple: self._upload_part(part_num=part_tuple[0] + 1, part=part_tuple[1], **kwargs),
                 enumerate(self.manifest["parts"]))

    def commit(self, **kwargs):
        """
        Commit the multipart upload.

        :return: A Response object with data of type None
        :rtype: None
        """
        if self.manifest["uploadId"] is None:
            raise RuntimeError('Cannot call commit before initializing an upload using new_upload or resuming an upload using resume.')

        client_request_id = None
        if 'opc_client_request_id' in kwargs:
            client_request_id = kwargs['opc_client_request_id']

        commit_details = models.CommitMultipartUploadDetails()

        # Determine which parts to commit and which parts to exclude.
        parts_to_commit = []
        parts_to_exclude = []
        for partNum, part in enumerate(self.manifest["parts"]):
            detail = models.CommitMultipartUploadPartDetails()
            detail.part_num = partNum + 1
            if "etag" in part:
                detail.etag = part["etag"]
                parts_to_commit.append(detail)
            else:
                parts_to_exclude.append(partNum + 1)

        commit_details.parts_to_commit = parts_to_commit
        commit_details.parts_to_exclude = parts_to_exclude

        kwargs = {}
        if client_request_id:
            kwargs['opc_client_request_id'] = client_request_id

        # Commit the multipart upload
        response = self.object_storage_client.commit_multipart_upload(self.manifest["namespace"],
                                                                      self.manifest["bucketName"],
                                                                      self.manifest["objectName"],
                                                                      self.manifest["uploadId"],
                                                                      commit_details,
                                                                      **kwargs)
        return response
