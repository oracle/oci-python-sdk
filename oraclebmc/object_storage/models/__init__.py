# coding: utf-8
# Copyright (c) 2017 Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .bucket import Bucket
from .bucket_summary import BucketSummary
from .create_bucket_details import CreateBucketDetails
from .list_objects import ListObjects
from .object_summary import ObjectSummary
from .update_bucket_details import UpdateBucketDetails

# Maps type names to classes for object_storage services.
object_storage_type_mapping = {
    "Bucket": Bucket,
    "BucketSummary": BucketSummary,
    "CreateBucketDetails": CreateBucketDetails,
    "ListObjects": ListObjects,
    "ObjectSummary": ObjectSummary,
    "UpdateBucketDetails": UpdateBucketDetails
}
