# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .bucket import Bucket
from .bucket_summary import BucketSummary
from .commit_multipart_upload_details import CommitMultipartUploadDetails
from .commit_multipart_upload_part_details import CommitMultipartUploadPartDetails
from .create_bucket_details import CreateBucketDetails
from .create_multipart_upload_details import CreateMultipartUploadDetails
from .create_preauthenticated_request_details import CreatePreauthenticatedRequestDetails
from .list_objects import ListObjects
from .multipart_upload import MultipartUpload
from .multipart_upload_part_summary import MultipartUploadPartSummary
from .object_summary import ObjectSummary
from .preauthenticated_request import PreauthenticatedRequest
from .preauthenticated_request_summary import PreauthenticatedRequestSummary
from .update_bucket_details import UpdateBucketDetails

# Maps type names to classes for object_storage services.
object_storage_type_mapping = {
    "Bucket": Bucket,
    "BucketSummary": BucketSummary,
    "CommitMultipartUploadDetails": CommitMultipartUploadDetails,
    "CommitMultipartUploadPartDetails": CommitMultipartUploadPartDetails,
    "CreateBucketDetails": CreateBucketDetails,
    "CreateMultipartUploadDetails": CreateMultipartUploadDetails,
    "CreatePreauthenticatedRequestDetails": CreatePreauthenticatedRequestDetails,
    "ListObjects": ListObjects,
    "MultipartUpload": MultipartUpload,
    "MultipartUploadPartSummary": MultipartUploadPartSummary,
    "ObjectSummary": ObjectSummary,
    "PreauthenticatedRequest": PreauthenticatedRequest,
    "PreauthenticatedRequestSummary": PreauthenticatedRequestSummary,
    "UpdateBucketDetails": UpdateBucketDetails
}
