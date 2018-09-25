# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .bucket import Bucket
from .bucket_summary import BucketSummary
from .commit_multipart_upload_details import CommitMultipartUploadDetails
from .commit_multipart_upload_part_details import CommitMultipartUploadPartDetails
from .copy_object_details import CopyObjectDetails
from .create_bucket_details import CreateBucketDetails
from .create_multipart_upload_details import CreateMultipartUploadDetails
from .create_preauthenticated_request_details import CreatePreauthenticatedRequestDetails
from .list_objects import ListObjects
from .multipart_upload import MultipartUpload
from .multipart_upload_part_summary import MultipartUploadPartSummary
from .namespace_metadata import NamespaceMetadata
from .object_lifecycle_policy import ObjectLifecyclePolicy
from .object_lifecycle_rule import ObjectLifecycleRule
from .object_name_filter import ObjectNameFilter
from .object_summary import ObjectSummary
from .preauthenticated_request import PreauthenticatedRequest
from .preauthenticated_request_summary import PreauthenticatedRequestSummary
from .put_object_lifecycle_policy_details import PutObjectLifecyclePolicyDetails
from .rename_object_details import RenameObjectDetails
from .restore_objects_details import RestoreObjectsDetails
from .update_bucket_details import UpdateBucketDetails
from .update_namespace_metadata_details import UpdateNamespaceMetadataDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for object_storage services.
object_storage_type_mapping = {
    "Bucket": Bucket,
    "BucketSummary": BucketSummary,
    "CommitMultipartUploadDetails": CommitMultipartUploadDetails,
    "CommitMultipartUploadPartDetails": CommitMultipartUploadPartDetails,
    "CopyObjectDetails": CopyObjectDetails,
    "CreateBucketDetails": CreateBucketDetails,
    "CreateMultipartUploadDetails": CreateMultipartUploadDetails,
    "CreatePreauthenticatedRequestDetails": CreatePreauthenticatedRequestDetails,
    "ListObjects": ListObjects,
    "MultipartUpload": MultipartUpload,
    "MultipartUploadPartSummary": MultipartUploadPartSummary,
    "NamespaceMetadata": NamespaceMetadata,
    "ObjectLifecyclePolicy": ObjectLifecyclePolicy,
    "ObjectLifecycleRule": ObjectLifecycleRule,
    "ObjectNameFilter": ObjectNameFilter,
    "ObjectSummary": ObjectSummary,
    "PreauthenticatedRequest": PreauthenticatedRequest,
    "PreauthenticatedRequestSummary": PreauthenticatedRequestSummary,
    "PutObjectLifecyclePolicyDetails": PutObjectLifecyclePolicyDetails,
    "RenameObjectDetails": RenameObjectDetails,
    "RestoreObjectsDetails": RestoreObjectsDetails,
    "UpdateBucketDetails": UpdateBucketDetails,
    "UpdateNamespaceMetadataDetails": UpdateNamespaceMetadataDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
