# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentCommandSourceDetails(object):
    """
    Command content.
    """

    #: A constant which can be used with the source_type property of a InstanceAgentCommandSourceDetails.
    #: This constant has a value of "TEXT"
    SOURCE_TYPE_TEXT = "TEXT"

    #: A constant which can be used with the source_type property of a InstanceAgentCommandSourceDetails.
    #: This constant has a value of "OBJECT_STORAGE_URI"
    SOURCE_TYPE_OBJECT_STORAGE_URI = "OBJECT_STORAGE_URI"

    #: A constant which can be used with the source_type property of a InstanceAgentCommandSourceDetails.
    #: This constant has a value of "OBJECT_STORAGE_TUPLE"
    SOURCE_TYPE_OBJECT_STORAGE_TUPLE = "OBJECT_STORAGE_TUPLE"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentCommandSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.compute_instance_agent.models.InstanceAgentCommandSourceViaObjectStorageTupleDetails`
        * :class:`~oci.compute_instance_agent.models.InstanceAgentCommandSourceViaObjectStorageUriDetails`
        * :class:`~oci.compute_instance_agent.models.InstanceAgentCommandSourceViaTextDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this InstanceAgentCommandSourceDetails.
            Allowed values for this property are: "TEXT", "OBJECT_STORAGE_URI", "OBJECT_STORAGE_TUPLE", 'UNKNOWN_ENUM_VALUE'.
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

        if type == 'OBJECT_STORAGE_TUPLE':
            return 'InstanceAgentCommandSourceViaObjectStorageTupleDetails'

        if type == 'OBJECT_STORAGE_URI':
            return 'InstanceAgentCommandSourceViaObjectStorageUriDetails'

        if type == 'TEXT':
            return 'InstanceAgentCommandSourceViaTextDetails'
        else:
            return 'InstanceAgentCommandSourceDetails'

    @property
    def source_type(self):
        """
        **[Required]** Gets the source_type of this InstanceAgentCommandSourceDetails.
        The source type of the command. Use `TEXT` for inlining the command. Use `OBJECT_STORAGE_TUPLE` when specifying
        the namespace, bucket name, and object name. Use `OBJECT_STORAGE_URI` when specifying the Object Storage URL.

        Allowed values for this property are: "TEXT", "OBJECT_STORAGE_URI", "OBJECT_STORAGE_TUPLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_type of this InstanceAgentCommandSourceDetails.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this InstanceAgentCommandSourceDetails.
        The source type of the command. Use `TEXT` for inlining the command. Use `OBJECT_STORAGE_TUPLE` when specifying
        the namespace, bucket name, and object name. Use `OBJECT_STORAGE_URI` when specifying the Object Storage URL.


        :param source_type: The source_type of this InstanceAgentCommandSourceDetails.
        :type: str
        """
        allowed_values = ["TEXT", "OBJECT_STORAGE_URI", "OBJECT_STORAGE_TUPLE"]
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
