# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .bucket import Bucket
from .bucket_summary import BucketSummary
from .commit_multipart_upload_details import CommitMultipartUploadDetails
from .commit_multipart_upload_part_details import CommitMultipartUploadPartDetails
from .copy_object_details import CopyObjectDetails
from .create_bucket_details import CreateBucketDetails
from .create_multipart_upload_details import CreateMultipartUploadDetails
from .create_preauthenticated_request_details import CreatePreauthenticatedRequestDetails
from .create_replication_policy_details import CreateReplicationPolicyDetails
from .create_retention_rule_details import CreateRetentionRuleDetails
from .duration import Duration
from .list_objects import ListObjects
from .multipart_upload import MultipartUpload
from .multipart_upload_part_summary import MultipartUploadPartSummary
from .namespace_metadata import NamespaceMetadata
from .object_lifecycle_policy import ObjectLifecyclePolicy
from .object_lifecycle_rule import ObjectLifecycleRule
from .object_name_filter import ObjectNameFilter
from .object_summary import ObjectSummary
from .object_version_collection import ObjectVersionCollection
from .object_version_summary import ObjectVersionSummary
from .pattern_details import PatternDetails
from .preauthenticated_request import PreauthenticatedRequest
from .preauthenticated_request_summary import PreauthenticatedRequestSummary
from .put_object_lifecycle_policy_details import PutObjectLifecyclePolicyDetails
from .reencrypt_object_details import ReencryptObjectDetails
from .rename_object_details import RenameObjectDetails
from .replication_policy import ReplicationPolicy
from .replication_policy_summary import ReplicationPolicySummary
from .replication_source import ReplicationSource
from .restore_objects_details import RestoreObjectsDetails
from .retention_rule import RetentionRule
from .retention_rule_collection import RetentionRuleCollection
from .retention_rule_details import RetentionRuleDetails
from .retention_rule_summary import RetentionRuleSummary
from .sse_customer_key_details import SSECustomerKeyDetails
from .update_bucket_details import UpdateBucketDetails
from .update_namespace_metadata_details import UpdateNamespaceMetadataDetails
from .update_retention_rule_details import UpdateRetentionRuleDetails
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
    "CreateReplicationPolicyDetails": CreateReplicationPolicyDetails,
    "CreateRetentionRuleDetails": CreateRetentionRuleDetails,
    "Duration": Duration,
    "ListObjects": ListObjects,
    "MultipartUpload": MultipartUpload,
    "MultipartUploadPartSummary": MultipartUploadPartSummary,
    "NamespaceMetadata": NamespaceMetadata,
    "ObjectLifecyclePolicy": ObjectLifecyclePolicy,
    "ObjectLifecycleRule": ObjectLifecycleRule,
    "ObjectNameFilter": ObjectNameFilter,
    "ObjectSummary": ObjectSummary,
    "ObjectVersionCollection": ObjectVersionCollection,
    "ObjectVersionSummary": ObjectVersionSummary,
    "PatternDetails": PatternDetails,
    "PreauthenticatedRequest": PreauthenticatedRequest,
    "PreauthenticatedRequestSummary": PreauthenticatedRequestSummary,
    "PutObjectLifecyclePolicyDetails": PutObjectLifecyclePolicyDetails,
    "ReencryptObjectDetails": ReencryptObjectDetails,
    "RenameObjectDetails": RenameObjectDetails,
    "ReplicationPolicy": ReplicationPolicy,
    "ReplicationPolicySummary": ReplicationPolicySummary,
    "ReplicationSource": ReplicationSource,
    "RestoreObjectsDetails": RestoreObjectsDetails,
    "RetentionRule": RetentionRule,
    "RetentionRuleCollection": RetentionRuleCollection,
    "RetentionRuleDetails": RetentionRuleDetails,
    "RetentionRuleSummary": RetentionRuleSummary,
    "SSECustomerKeyDetails": SSECustomerKeyDetails,
    "UpdateBucketDetails": UpdateBucketDetails,
    "UpdateNamespaceMetadataDetails": UpdateNamespaceMetadataDetails,
    "UpdateRetentionRuleDetails": UpdateRetentionRuleDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
