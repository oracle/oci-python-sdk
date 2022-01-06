# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogLocationBucketDetails(object):
    """
    Details to access log file in the specified Object Storage bucket, if any.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogLocationBucketDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bucket_name:
            The value to assign to the bucket_name property of this LogLocationBucketDetails.
        :type bucket_name: str

        :param namespace:
            The value to assign to the namespace property of this LogLocationBucketDetails.
        :type namespace: str

        :param object_name:
            The value to assign to the object_name property of this LogLocationBucketDetails.
        :type object_name: str

        """
        self.swagger_types = {
            'bucket_name': 'str',
            'namespace': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'bucket_name': 'bucketName',
            'namespace': 'namespace',
            'object_name': 'objectName'
        }

        self._bucket_name = None
        self._namespace = None
        self._object_name = None

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this LogLocationBucketDetails.
        Name of the bucket containing the log file.


        :return: The bucket_name of this LogLocationBucketDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this LogLocationBucketDetails.
        Name of the bucket containing the log file.


        :param bucket_name: The bucket_name of this LogLocationBucketDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this LogLocationBucketDetails.
        Object Storage namespace.


        :return: The namespace of this LogLocationBucketDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this LogLocationBucketDetails.
        Object Storage namespace.


        :param namespace: The namespace of this LogLocationBucketDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this LogLocationBucketDetails.
        Log object name.


        :return: The object_name of this LogLocationBucketDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this LogLocationBucketDetails.
        Log object name.


        :param object_name: The object_name of this LogLocationBucketDetails.
        :type: str
        """
        self._object_name = object_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
