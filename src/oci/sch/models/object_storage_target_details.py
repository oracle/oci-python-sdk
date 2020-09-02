# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .target_details import TargetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageTargetDetails(TargetDetails):
    """
    The object storage target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageTargetDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.ObjectStorageTargetDetails.kind` attribute
        of this class is ``objectStorage`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this ObjectStorageTargetDetails.
            Allowed values for this property are: "streaming", "objectStorage", "monitoring", "functions", "notifications"
        :type kind: str

        :param namespace:
            The value to assign to the namespace property of this ObjectStorageTargetDetails.
        :type namespace: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ObjectStorageTargetDetails.
        :type bucket_name: str

        :param object_name_prefix:
            The value to assign to the object_name_prefix property of this ObjectStorageTargetDetails.
        :type object_name_prefix: str

        """
        self.swagger_types = {
            'kind': 'str',
            'namespace': 'str',
            'bucket_name': 'str',
            'object_name_prefix': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'namespace': 'namespace',
            'bucket_name': 'bucketName',
            'object_name_prefix': 'objectNamePrefix'
        }

        self._kind = None
        self._namespace = None
        self._bucket_name = None
        self._object_name_prefix = None
        self._kind = 'objectStorage'

    @property
    def namespace(self):
        """
        Gets the namespace of this ObjectStorageTargetDetails.
        The namespace.


        :return: The namespace of this ObjectStorageTargetDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this ObjectStorageTargetDetails.
        The namespace.


        :param namespace: The namespace of this ObjectStorageTargetDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this ObjectStorageTargetDetails.
        The name of the bucket. Avoid entering confidential information.


        :return: The bucket_name of this ObjectStorageTargetDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ObjectStorageTargetDetails.
        The name of the bucket. Avoid entering confidential information.


        :param bucket_name: The bucket_name of this ObjectStorageTargetDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name_prefix(self):
        """
        Gets the object_name_prefix of this ObjectStorageTargetDetails.
        The prefix of the objects. Avoid entering confidential information.


        :return: The object_name_prefix of this ObjectStorageTargetDetails.
        :rtype: str
        """
        return self._object_name_prefix

    @object_name_prefix.setter
    def object_name_prefix(self, object_name_prefix):
        """
        Sets the object_name_prefix of this ObjectStorageTargetDetails.
        The prefix of the objects. Avoid entering confidential information.


        :param object_name_prefix: The object_name_prefix of this ObjectStorageTargetDetails.
        :type: str
        """
        self._object_name_prefix = object_name_prefix

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
