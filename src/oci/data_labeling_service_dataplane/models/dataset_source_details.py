# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatasetSourceDetails(object):
    """
    This allows the customer to specify the source of the dataset.
    """

    #: A constant which can be used with the source_type property of a DatasetSourceDetails.
    #: This constant has a value of "OBJECT_STORAGE"
    SOURCE_TYPE_OBJECT_STORAGE = "OBJECT_STORAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new DatasetSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_labeling_service_dataplane.models.ObjectStorageDatasetSourceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this DatasetSourceDetails.
            Allowed values for this property are: "OBJECT_STORAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_type: str

        """
        self.swagger_types = {
            'source_type': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType'
        }

        self._source_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['sourceType']

        if type == 'OBJECT_STORAGE':
            return 'ObjectStorageDatasetSourceDetails'
        else:
            return 'DatasetSourceDetails'

    @property
    def source_type(self):
        """
        **[Required]** Gets the source_type of this DatasetSourceDetails.
        The source type. OBJECT_STORAGE allows the user to describe where in object storage the dataset is.

        Allowed values for this property are: "OBJECT_STORAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_type of this DatasetSourceDetails.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this DatasetSourceDetails.
        The source type. OBJECT_STORAGE allows the user to describe where in object storage the dataset is.


        :param source_type: The source_type of this DatasetSourceDetails.
        :type: str
        """
        allowed_values = ["OBJECT_STORAGE"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            source_type = 'UNKNOWN_ENUM_VALUE'
        self._source_type = source_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
