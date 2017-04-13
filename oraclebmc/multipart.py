import six
import io
import hashlib
import base64
from threading import Thread
from oraclebmc.object_storage import models


class MultipartAssembler:
    def __init__(self,
                 object_storage,
                 namespace_name,
                 bucket_name,
                 object_name,
                 ):
        self.object_storage = object_storage
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

    def setPart(self,
                part,
                part_number,
                md5=None):
        self.manifest["parts"][part_number] = part

    def abort_upload(self):
        response = self.object_storage.abort_multipart_upload(self.manifest["nameSpace"],
                                                              self.manifest["bucketName"],
                                                              self.manifest["objectName"],
                                                              self.manifest["uploadId"])
        # ToDo: check for errors in response and act on them
        if response.status != 200:
            print(response.status)

    def new_upload(self):
        request = models.CreateMultipartUploadDetails()
        request.object = self.manifest["objectName"]
        response = self.object_storage.create_multipart_upload(self.manifest["nameSpace"],
                                                               self.manifest["bucketName"],
                                                               request)
        if response.status == 200:
            self.manifest["uploadId"] = response.data.upload_id
        else:
            # ToDo: Determine what errors can come back and act on them
            print(response.status)

    def upload_part(self, part, part_num):
        print("uploading part: {}".format(part_num))
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
                print("Upload for part {} failed with hash mismatch".format(part_num))
                print("{} vs {}".format(part["hash"], part["opc_md5"]))
            else:
                print("Part {} uploaded successfully".format(part_num))

    def upload(self):
        # Todo: Determine correct action if there is no uploadId in the manifest.
        #       Create the upload or throw exception?
        threads = []
        for part_num, part in enumerate(self.manifest["parts"]):
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
            print("Commit successful")
        else:
            print("Something went wrong")

