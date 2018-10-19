# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MultipartUpload(object):
    """
    Multipart uploads provide efficient and resilient uploads, especially for large objects. Multipart uploads also accommodate
    objects that are too large for a single upload operation. With multipart uploads, individual parts of an object can be
    uploaded in parallel to reduce the amount of time you spend uploading. Multipart uploads can also minimize the impact
    of network failures by letting you retry a failed part upload instead of requiring you to retry an entire object upload.
    See `Managing Multipart Uploads`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingmultipartuploads.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MultipartUpload object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace:
            The value to assign to the namespace property of this MultipartUpload.
        :type namespace: str

        :param bucket:
            The value to assign to the bucket property of this MultipartUpload.
        :type bucket: str

        :param object:
            The value to assign to the object property of this MultipartUpload.
        :type object: str

        :param upload_id:
            The value to assign to the upload_id property of this MultipartUpload.
        :type upload_id: str

        :param time_created:
            The value to assign to the time_created property of this MultipartUpload.
        :type time_created: datetime

        """
        self.swagger_types = {
            'namespace': 'str',
            'bucket': 'str',
            'object': 'str',
            'upload_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'bucket': 'bucket',
            'object': 'object',
            'upload_id': 'uploadId',
            'time_created': 'timeCreated'
        }

        self._namespace = None
        self._bucket = None
        self._object = None
        self._upload_id = None
        self._time_created = None

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this MultipartUpload.
        The namespace in which the in-progress multipart upload is stored.


        :return: The namespace of this MultipartUpload.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this MultipartUpload.
        The namespace in which the in-progress multipart upload is stored.


        :param namespace: The namespace of this MultipartUpload.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket(self):
        """
        **[Required]** Gets the bucket of this MultipartUpload.
        The bucket in which the in-progress multipart upload is stored.


        :return: The bucket of this MultipartUpload.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """
        Sets the bucket of this MultipartUpload.
        The bucket in which the in-progress multipart upload is stored.


        :param bucket: The bucket of this MultipartUpload.
        :type: str
        """
        self._bucket = bucket

    @property
    def object(self):
        """
        **[Required]** Gets the object of this MultipartUpload.
        The object name of the in-progress multipart upload.


        :return: The object of this MultipartUpload.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this MultipartUpload.
        The object name of the in-progress multipart upload.


        :param object: The object of this MultipartUpload.
        :type: str
        """
        self._object = object

    @property
    def upload_id(self):
        """
        **[Required]** Gets the upload_id of this MultipartUpload.
        The unique identifier for the in-progress multipart upload.


        :return: The upload_id of this MultipartUpload.
        :rtype: str
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """
        Sets the upload_id of this MultipartUpload.
        The unique identifier for the in-progress multipart upload.


        :param upload_id: The upload_id of this MultipartUpload.
        :type: str
        """
        self._upload_id = upload_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MultipartUpload.
        The date and time the upload was created, as described in `RFC 2616`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc2616


        :return: The time_created of this MultipartUpload.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MultipartUpload.
        The date and time the upload was created, as described in `RFC 2616`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc2616


        :param time_created: The time_created of this MultipartUpload.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
