# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .location_details import LocationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectListDataset(LocationDetails):
    """
    Data source details for object storage
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectListDataset object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_language.models.ObjectListDataset.location_type` attribute
        of this class is ``OBJECT_LIST`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param location_type:
            The value to assign to the location_type property of this ObjectListDataset.
            Allowed values for this property are: "OBJECT_LIST"
        :type location_type: str

        :param namespace_name:
            The value to assign to the namespace_name property of this ObjectListDataset.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ObjectListDataset.
        :type bucket_name: str

        :param object_names:
            The value to assign to the object_names property of this ObjectListDataset.
        :type object_names: list[str]

        """
        self.swagger_types = {
            'location_type': 'str',
            'namespace_name': 'str',
            'bucket_name': 'str',
            'object_names': 'list[str]'
        }

        self.attribute_map = {
            'location_type': 'locationType',
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName',
            'object_names': 'objectNames'
        }

        self._location_type = None
        self._namespace_name = None
        self._bucket_name = None
        self._object_names = None
        self._location_type = 'OBJECT_LIST'

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this ObjectListDataset.
        Object storage namespace


        :return: The namespace_name of this ObjectListDataset.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this ObjectListDataset.
        Object storage namespace


        :param namespace_name: The namespace_name of this ObjectListDataset.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this ObjectListDataset.
        Object storage bucket name


        :return: The bucket_name of this ObjectListDataset.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ObjectListDataset.
        Object storage bucket name


        :param bucket_name: The bucket_name of this ObjectListDataset.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_names(self):
        """
        **[Required]** Gets the object_names of this ObjectListDataset.
        Array of files which need to be processed in the bucket


        :return: The object_names of this ObjectListDataset.
        :rtype: list[str]
        """
        return self._object_names

    @object_names.setter
    def object_names(self, object_names):
        """
        Sets the object_names of this ObjectListDataset.
        Array of files which need to be processed in the bucket


        :param object_names: The object_names of this ObjectListDataset.
        :type: list[str]
        """
        self._object_names = object_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
