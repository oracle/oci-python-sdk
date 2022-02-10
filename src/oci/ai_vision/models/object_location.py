# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectLocation(object):
    """
    A location in Object Storage that is uniquely identified by namespace name, bucket name and object name.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectLocation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace_name:
            The value to assign to the namespace_name property of this ObjectLocation.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ObjectLocation.
        :type bucket_name: str

        :param object_name:
            The value to assign to the object_name property of this ObjectLocation.
        :type object_name: str

        """
        self.swagger_types = {
            'namespace_name': 'str',
            'bucket_name': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName',
            'object_name': 'objectName'
        }

        self._namespace_name = None
        self._bucket_name = None
        self._object_name = None

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this ObjectLocation.
        Object Storage namespace name.


        :return: The namespace_name of this ObjectLocation.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this ObjectLocation.
        Object Storage namespace name.


        :param namespace_name: The namespace_name of this ObjectLocation.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this ObjectLocation.
        Object Storage bucket name.


        :return: The bucket_name of this ObjectLocation.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ObjectLocation.
        Object Storage bucket name.


        :param bucket_name: The bucket_name of this ObjectLocation.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this ObjectLocation.
        Object Storage object name.


        :return: The object_name of this ObjectLocation.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this ObjectLocation.
        Object Storage object name.


        :param object_name: The object_name of this ObjectLocation.
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
