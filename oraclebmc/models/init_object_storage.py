from __future__ import absolute_import

from .bucket import Bucket
from .create_bucket_details import CreateBucketDetails
from .error import Error
from .list_objects import ListObjects
from .object_summary import ObjectSummary
from .update_bucket_details import UpdateBucketDetails

# Maps type names to classes for object_storage services.
object_storage_type_mapping = {
    "Bucket": Bucket,
    "CreateBucketDetails": CreateBucketDetails,
    "Error": Error,
    "ListObjects": ListObjects,
    "ObjectSummary": ObjectSummary,
    "UpdateBucketDetails": UpdateBucketDetails
}
