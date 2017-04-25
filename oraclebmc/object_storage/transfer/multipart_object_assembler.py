# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import sys
import io
import hashlib
import base64
from os import stat
from .constants import DEFAULT_PART_SIZE
from .. import models
from ...exceptions import ServiceError

# TODO: Add docstrings to everything.
# TODO: Determine if parts should be overwritten.  Currently keep all parts with a matching hash
# TODO: Calculate and verify mulitpart hash.  Currently only checking parts.
# TODO: Abort abandoned multipart uploads.
# TODO: Add parallel uploads of multipart parts.
# TODO: Automatic retries for failed parts.

# TODO: Replace with correct value for a object storage unit


class MultipartObjectAssembler:

    def __init__(self,
                 object_storage_client,
                 namespace_name,
                 bucket_name,
                 object_name,
                 part_size=None
                 ):
        self.object_storage_client = object_storage_client
        if part_size:
            self.part_size = part_size
        else:
            self.part_size = DEFAULT_PART_SIZE
        self.manifest = {"uploadId": None,
                         "namespace": namespace_name,
                         "bucketName": bucket_name,
                         "objectName": object_name,
                         "parts": []}

    def calculate_md5(self, file, offset, chunk):
        m = hashlib.md5()
        with io.open(file, mode='rb') as f:
            f.seek(offset, io.SEEK_SET)
            m.update(f.read(chunk))
        return base64.b64encode(m.digest()).decode("utf-8")

    def add_parts_from_file(self, filepath):
        with io.open(filepath, mode='rb') as file:
            file.seek(0, io.SEEK_END)
            end = file.tell()
            file.seek(0, io.SEEK_SET)
            offset = 0
            while file.tell() < end:
                self.add_part(filepath, offset=offset, size=self.part_size)
                offset += self.part_size
                file.seek(offset, io.SEEK_SET)

    def add_part(self,
                 file,
                 offset=0,
                 size=None,
                 part_hash=None):

        if size is None:
            size = stat(file.name).st_size

        self.manifest["parts"].append({"file": file,
                                       "offset": offset,
                                       "size": size,
                                       "hash": part_hash})

    def abort(self):
        # TODO: verify that there is an upload ID before trying to abort the upload

        self.object_storage_client.abort_multipart_upload(self.manifest["namespace"],
                                                          self.manifest["bucketName"],
                                                          self.manifest["objectName"],
                                                          self.manifest["uploadId"])

    def resume(self, upload_id=None):
        if upload_id:
            self.manifest["uploadId"] = upload_id

        # Verify that the upload id is valid
        if self.manifest["uploadId"] is None:
            raise RuntimeError("Cannot resume with out an upload id.")

        # Get parts details from object storage to see which parts didn't complete
        try:
            response = self.object_storage_client.list_multipart_upload_parts(self.manifest["namespace"],
                                                                              self.manifest["bucketName"],
                                                                              self.manifest["objectName"],
                                                                              self.manifest["uploadId"])
        except ServiceError as e:
            raise e
        else:
            # Update manifest with information from object storage
            parts = self.manifest["parts"]
            for part in response.data:
                part_index = part.part_number - 1
                if -1 < part_index < len(parts):
                    manifest_part = parts[part_index]
                    manifest_part["etag"] = part.etag
                    manifest_part["opc_md5"] = part.md5

            # Upload parts that are missing or incomplete
            # print("Resuming upload for upload id: {}".format(self.manifest["uploadId"]))
            self.upload_multipart()

    # TODO: Come up with a better name for this method.
    def new_upload(self):
        request = models.CreateMultipartUploadDetails()
        request.object = self.manifest["objectName"]

        try:
            response = self.object_storage_client.create_multipart_upload(self.manifest["namespace"],
                                                                          self.manifest["bucketName"],
                                                                          request)
        except Exception as e:
            raise e
        else:
            self.manifest["uploadId"] = response.data.upload_id
            print("Upload ID: {}".format(self.manifest["uploadId"]), file=sys.stderr)

    def upload_part(self, part, part_num):
        print("uploading part: {}".format(part_num), file=sys.stderr)
        with io.open(part["file"], mode='rb') as file:
            file.seek(part["offset"], io.SEEK_SET)
            response = self.object_storage_client.upload_part(self.manifest["namespace"],
                                                              self.manifest["bucketName"],
                                                              self.manifest["objectName"],
                                                              self.manifest["uploadId"],
                                                              part_num,
                                                              file.read(part["size"]))

        # TODO: Handle any issues if the upload didn't work
        if response.status == 200:
            part["etag"] = response.headers['etag']
            part["opc_md5"] = str(response.headers['opc-content-md5'])
            if part["hash"] != part["opc_md5"]:
                # TODO: throw an error if the hashes do not agree
                print("Upload for part {} failed with hash mismatch".format(part_num), file=sys.stderr)
                print("{} vs {}".format(part["hash"], part["opc_md5"]), file=sys.stderr)
            else:
                print("Part {} uploaded successfully".format(part_num), file=sys.stderr)

    def upload(self):
        # TODO: Determine correct action if there is no uploadId in the manifest.
        #       Create the upload or throw exception?
        for part_num, part in enumerate(self.manifest["parts"]):
            # TODO: Determine how to calculate the hash without needing to read the
            #       file chunk twice.

            # Calculate the hash before uploading.  The hash will be used
            # to determine if the part needs to be uploaded.  It will also
            # be used to determine if there is a conflict between parts that
            # parts that have previously been uploaded.
            if part["hash"] is None:
                part["hash"] = self.calculate_md5(part["file"], part["offset"], part["size"])

            if "opc_md5" not in part:
                self.upload_part(part, part_num + 1)
            elif part["hash"] != part["opc_md5"]:
                raise RuntimeError("The local part does not match the part already uploaded to object storage")

    def commit(self):
        # Prepare to commit the upload
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

        # Commit the multipart upload
        response = self.object_storage_client.commit_multipart_upload(self.manifest["namespace"],
                                                                      self.manifest["bucketName"],
                                                                      self.manifest["objectName"],
                                                                      self.manifest["uploadId"],
                                                                      commit_details)

        if response.status == 200:
            print("Commit successful for upload id {}".format(self.manifest["uploadId"]), file=sys.stderr)
