# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import io
import hashlib
import base64
from os import stat
from .constants import DEFAULT_PART_SIZE
from .constants import MEBIBYTE
from .buffered_part_reader import BufferedPartReader
from .. import models
from ...exceptions import ServiceError
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError

# TODO: Add docstrings to everything.
# TODO: Calculate and verify mulitpart hash.  Currently only checking parts.
# TODO: Add parallel uploads of multipart parts.


class MultipartObjectAssembler:

    def __init__(self,
                 object_storage_client,
                 namespace_name,
                 bucket_name,
                 object_name,
                 **kwargs
                 ):
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
        self.opc_client_request_id = None
        if 'opc_client_request_id' in kwargs:
            self.opc_client_request_id = kwargs['opc_client_request_id']
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
        self.progress = None
        if 'progress' in kwargs:
            self.progress = kwargs['progress']

        self.max_retries = 3
        self.manifest = {"uploadId": None,
                         "namespace": namespace_name,
                         "bucketName": bucket_name,
                         "objectName": object_name,
                         "parts": []}

    @staticmethod
    def calculate_md5(file, offset, chunk):
        m = hashlib.md5()
        with io.open(file, mode='rb') as f:
            bpr = BufferedPartReader(f, offset, chunk)
            while True:
                part = bpr.read(8 * 1024)
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

    def add_parts_from_file(self, filepath):
        with io.open(filepath, mode='rb') as file_object:
            file_object.seek(0, io.SEEK_END)
            end = file_object.tell()
            file_object.seek(0, io.SEEK_SET)
            offset = 0
            while file_object.tell() < end:
                self.add_part(filepath, offset=offset, size=self.part_size)
                offset += self.part_size
                file_object.seek(offset, io.SEEK_SET)

    def add_part(self,
                 file_object,
                 offset=0,
                 size=None,
                 part_hash=None):

        if size is None:
            size = stat(file_object.fileno()).st_size

        self.manifest["parts"].append({"file": file_object,
                                       "offset": offset,
                                       "size": size,
                                       "hash": part_hash})

    def abort(self):
        # TODO: verify that there is an upload ID before trying to abort the upload

        kwargs = {}
        if self.opc_client_request_id:
            kwargs['opc_client_request_id'] = self.opc_client_request_id

        self.object_storage_client.abort_multipart_upload(self.manifest["namespace"],
                                                          self.manifest["bucketName"],
                                                          self.manifest["objectName"],
                                                          self.manifest["uploadId"],
                                                          **kwargs)

    def resume(self, upload_id=None):
        if upload_id:
            self.manifest["uploadId"] = upload_id

        # Verify that the upload id is valid
        if self.manifest["uploadId"] is None:
            raise ValueError("Cannot resume without an upload id.")

        kwargs = {}
        if self.opc_client_request_id:
            kwargs['opc_client_request_id'] = self.opc_client_request_id

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
        self.upload()

    def new_upload(self):
        request = models.CreateMultipartUploadDetails()
        request.object = self.manifest["objectName"]
        if self.content_type:
            request.content_type = self.content_type
        if self.content_language:
            request.content_language = self.content_language
        if self.content_encoding:
            request.content_encoding = self.content_encoding
        if self.metadata:
            request.metadata = self.metadata

        kwargs = {}
        if self.opc_client_request_id:
            kwargs['opc_client_request_id'] = self.opc_client_request_id
        if self.if_match:
            kwargs['if_match'] = self.if_match
        if self.if_none_match:
            kwargs['if_none_match'] = self.if_none_match

        response = self.object_storage_client.create_multipart_upload(self.manifest["namespace"],
                                                                      self.manifest["bucketName"],
                                                                      request,
                                                                      **kwargs)

        self.manifest["uploadId"] = response.data.upload_id

    def upload_part(self, part, part_num):
        kwargs = {'content_md5': part["hash"]}
        if self.opc_client_request_id:
            kwargs['opc_client_request_id'] = self.opc_client_request_id

        remaining_tries = self.max_retries
        while remaining_tries > 0:
            with io.open(part["file"], mode='rb') as file:
                bpr = BufferedPartReader(file, part["offset"], part["size"])
                try:
                    response = self.object_storage_client.upload_part(self.manifest["namespace"],
                                                                      self.manifest["bucketName"],
                                                                      self.manifest["objectName"],
                                                                      self.manifest["uploadId"],
                                                                      part_num,
                                                                      bpr,
                                                                      **kwargs)
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

    def upload(self):
        # TODO: Determine correct action if there is no uploadId in the manifest.
        #       Create the upload or throw exception?
        for part_num, part in enumerate(self.manifest["parts"]):
            # TODO: Determine how to calculate the hash without needing to read the
            #       file chunk twice.

            # Calculate the hash before uploading.  The hash will be used
            # to determine if the part needs to be uploaded.  It will also
            # be used to determine if there is a conflict between parts that
            # have previously been uploaded.
            if part["hash"] is None:
                part["hash"] = self.calculate_md5(part["file"], part["offset"], part["size"])

            if "opc_md5" not in part:
                self.upload_part(part, part_num + 1)

            if self.progress:
                self.progress.update(part["size"])

    def commit(self):
        # Prepare to commit the upload
        commit_details = models.CommitMultipartUploadDetails()

        # Determine which parts to commit and which parts to exclude.
        # TODO: Are there ever parts_to_exclude?
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
        if self.opc_client_request_id:
            kwargs['opc_client_request_id'] = self.opc_client_request_id

        # Commit the multipart upload
        response = self.object_storage_client.commit_multipart_upload(self.manifest["namespace"],
                                                                      self.manifest["bucketName"],
                                                                      self.manifest["objectName"],
                                                                      self.manifest["uploadId"],
                                                                      commit_details,
                                                                      **kwargs)
        return response
