# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentCommandOutputDetails(object):
    """
    The output destination for the command.
    """

    #: A constant which can be used with the output_type property of a InstanceAgentCommandOutputDetails.
    #: This constant has a value of "TEXT"
    OUTPUT_TYPE_TEXT = "TEXT"

    #: A constant which can be used with the output_type property of a InstanceAgentCommandOutputDetails.
    #: This constant has a value of "OBJECT_STORAGE_URI"
    OUTPUT_TYPE_OBJECT_STORAGE_URI = "OBJECT_STORAGE_URI"

    #: A constant which can be used with the output_type property of a InstanceAgentCommandOutputDetails.
    #: This constant has a value of "OBJECT_STORAGE_TUPLE"
    OUTPUT_TYPE_OBJECT_STORAGE_TUPLE = "OBJECT_STORAGE_TUPLE"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentCommandOutputDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.compute_instance_agent.models.InstanceAgentCommandOutputViaObjectStorageUriDetails`
        * :class:`~oci.compute_instance_agent.models.InstanceAgentCommandOutputViaObjectStorageTupleDetails`
        * :class:`~oci.compute_instance_agent.models.InstanceAgentCommandOutputViaTextDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param output_type:
            The value to assign to the output_type property of this InstanceAgentCommandOutputDetails.
            Allowed values for this property are: "TEXT", "OBJECT_STORAGE_URI", "OBJECT_STORAGE_TUPLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type output_type: str

        """
        self.swagger_types = {
            'output_type': 'str'
        }

        self.attribute_map = {
            'output_type': 'outputType'
        }

        self._output_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['outputType']

        if type == 'OBJECT_STORAGE_URI':
            return 'InstanceAgentCommandOutputViaObjectStorageUriDetails'

        if type == 'OBJECT_STORAGE_TUPLE':
            return 'InstanceAgentCommandOutputViaObjectStorageTupleDetails'

        if type == 'TEXT':
            return 'InstanceAgentCommandOutputViaTextDetails'
        else:
            return 'InstanceAgentCommandOutputDetails'

    @property
    def output_type(self):
        """
        **[Required]** Gets the output_type of this InstanceAgentCommandOutputDetails.
        The output type for the command. The following values are supported:

        - `TEXT` - the command output is returned as plain text.
        - `OBJECT_STORAGE_URI` - the command output is saved to an Object Storage URL.
        - `OBJECT_STORAGE_TUPLE` - the command output is saved to an Object Storage bucket.

        For background information about Object Storage buckets and URLs, see
        `Overview of Object Storage`__.

        __ https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm

        Allowed values for this property are: "TEXT", "OBJECT_STORAGE_URI", "OBJECT_STORAGE_TUPLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The output_type of this InstanceAgentCommandOutputDetails.
        :rtype: str
        """
        return self._output_type

    @output_type.setter
    def output_type(self, output_type):
        """
        Sets the output_type of this InstanceAgentCommandOutputDetails.
        The output type for the command. The following values are supported:

        - `TEXT` - the command output is returned as plain text.
        - `OBJECT_STORAGE_URI` - the command output is saved to an Object Storage URL.
        - `OBJECT_STORAGE_TUPLE` - the command output is saved to an Object Storage bucket.

        For background information about Object Storage buckets and URLs, see
        `Overview of Object Storage`__.

        __ https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm


        :param output_type: The output_type of this InstanceAgentCommandOutputDetails.
        :type: str
        """
        allowed_values = ["TEXT", "OBJECT_STORAGE_URI", "OBJECT_STORAGE_TUPLE"]
        if not value_allowed_none_or_none_sentinel(output_type, allowed_values):
            output_type = 'UNKNOWN_ENUM_VALUE'
        self._output_type = output_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
