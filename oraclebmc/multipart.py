import six
import sys
import io
import hashlib
import base64
from threading import Thread
from oraclebmc.object_storage import models
from oraclebmc.exceptions import ServiceError


class MultipartAssembler:
    PART_SIZE = 1000000

    def __init__(self,
                 object_storage,
                 namespace_name,
                 bucket_name,
                 object_name,
                 part_size=None
                 ):
        self.object_storage = object_storage
        if part_size:
            self.part_size = part_size
        else:
            self.part_size = self.PART_SIZE
        self.manifest = {"uploadId": 0,
                         "nameSpace": namespace_name,
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
                self.add_part(filepath, offset=offset, chunk=self.part_size)
                offset += self.part_size
                file.seek(offset, io.SEEK_SET)

    def add_part(self,
                 file,
                 offset,
                 chunk,
                 part_hash=None):
        if part_hash is None:
            part_hash = self.calculate_md5(file, offset, chunk)

        self.manifest["parts"].append({"file": file,
                                       "offset": offset,
                                       "chunk": chunk,
                                       "hash": part_hash})

    def set_part(self,
                part,
                part_number,
                md5=None):
        self.manifest["parts"][part_number] = part

    def abort(self):
        # ToDo: verify that there is an upload ID before trying to abort the upload
        response = self.object_storage.abort_multipart_upload(self.manifest["nameSpace"],
                                                              self.manifest["bucketName"],
                                                              self.manifest["objectName"],
                                                              self.manifest["uploadId"])
        # ToDo: check for errors in response and act on them
        if response.status != 200:
            print(response.status)

    def resume(self, upload_id=None):
        if not upload_id == None:
            self.manifest["uploadId"] = upload_id

        # Verify that the upload id is valid
        if not self.manifest["uploadId"] or self.manifest["uploadId"] == 0:
            print("Cannot resume upload for upload id {}. The id is invalid".format(upload_id), file=sys.stderr)
        else:
            if not self.manifest["parts"]:
                # ToDo: rebuild parts, need filepath
                pass

        # Get parts details from object storage to see which parts didn't complete
        try:
            response = self.object_storage.list_multipart_upload_parts(self.manifest["nameSpace"],
                                                                       self.manifest["bucketName"],
                                                                       self.manifest["objectName"],
                                                                       self.manifest["uploadId"])
        except ServiceError as e:
            if e.status == 404:
                print("Upload id {} not found".format(self.manifest["uploadId"]), file=sys.stderr)

            raise e
        else:
            # Determine which parts need to be uploaded
            parts = self.manifest["parts"]
            for part in response.data:
                part_index = part.part_number - 1
                if part_index > -1 and part_index < len(parts):
                    manifest_part = parts[part_index]
                    if manifest_part["hash"] == part.md5:
                        manifest_part["etag"] = part.etag
                        manifest_part["opc_md5"] = part.md5

            # Upload parts that are missing or incomplete
            self.upload()

    def new_upload(self):
        request = models.CreateMultipartUploadDetails()
        request.object = self.manifest["objectName"]
        response = self.object_storage.create_multipart_upload(self.manifest["nameSpace"],
                                                               self.manifest["bucketName"],
                                                               request)
        if response.status == 200:
            self.manifest["uploadId"] = response.data.upload_id
            print("Upload ID: {}".format(self.manifest["uploadId"]), file=sys.stderr)
        else:
            # ToDo: Determine what errors can come back and act on them
            print(response.status, file=sys.stderr)

    def upload_part(self, part, part_num):
        print("uploading part: {}".format(part_num), file=sys.stderr)
        with io.open(part["file"], mode='rb') as file:
            file.seek(part["offset"], io.SEEK_SET)
            response = self.object_storage.upload_part(self.manifest["nameSpace"],
                                                       self.manifest["bucketName"],
                                                       self.manifest["objectName"],
                                                       self.manifest["uploadId"],
                                                       part_num,
                                                       file.read(part["chunk"]))

        # ToDo: Handle any issues if the upload didn't work
        if response.status == 200:
            part["etag"] = response.headers['etag']
            part["opc_md5"] = str(response.headers['opc-content-md5'])
            if part["hash"] != part["opc_md5"]:
                # ToDo: throw an error if the hashes do not agree
                print("Upload for part {} failed with hash mismatch".format(part_num), file=sys.stderr)
                print("{} vs {}".format(part["hash"], part["opc_md5"]), file=sys.stderr)
            else:
                print("Part {} uploaded successfully".format(part_num), file=sys.stderr)

    def upload(self):
        # Todo: Determine correct action if there is no uploadId in the manifest.
        #       Create the upload or throw exception?
        threads = []
        for part_num, part in enumerate(self.manifest["parts"]):
            if "opc_md5" not in part or part["hash"] != part["opc_md5"]:
                t = Thread(target=self.upload_part, args=(part, part_num + 1))
                t.start()
                threads.append(t)

        for t in threads:
            t.join()

    def commit(self):
        # Prepare to commit the upload
        commitDetails = models.CommitMultipartUploadDetails()

        # Parts to commit and parts to exclude
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

        commitDetails.parts_to_commit = parts_to_commit
        commitDetails.parts_to_exclude = parts_to_exclude

        # Commit the multipart upload
        response = self.object_storage.commit_multipart_upload(self.manifest["nameSpace"],
                                                               self.manifest["bucketName"],
                                                               self.manifest["objectName"],
                                                               self.manifest["uploadId"],
                                                               commitDetails)

        # ToDo determine how to clean up if there is a failure.
        if response.status == 200:
            print("Commit successful for upload id {}".format(self.manifest["uploadId"]), file=sys.stderr)
        else:
            print("Something went wrong", file=sys.stderr)

