from __future__ import absolute_import

# import models into model package
from .bucket import Bucket
from .create_bucket import CreateBucket
from .error import Error
from .list_objects import ListObjects
from .object_summary import ObjectSummary
from .update_bucket import UpdateBucket

# Maps type names to classes for object_storage services.
object_storage_type_mapping = {
    'Bucket': Bucket,
    'CreateBucket': CreateBucket,
    'Error': Error,
    'ListObjects': ListObjects,
    'ObjectSummary': ObjectSummary,
    'UpdateBucket': UpdateBucket,
}