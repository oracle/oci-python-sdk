# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodeSourceOption(object):
    """
    The source option for the node.
    """

    #: A constant which can be used with the source_type property of a NodeSourceOption.
    #: This constant has a value of "IMAGE"
    SOURCE_TYPE_IMAGE = "IMAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new NodeSourceOption object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.container_engine.models.NodeSourceViaImageOption`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this NodeSourceOption.
            Allowed values for this property are: "IMAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_type: str

        :param source_name:
            The value to assign to the source_name property of this NodeSourceOption.
        :type source_name: str

        """
        self.swagger_types = {
            'source_type': 'str',
            'source_name': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'source_name': 'sourceName'
        }

        self._source_type = None
        self._source_name = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['sourceType']

        if type == 'IMAGE':
            return 'NodeSourceViaImageOption'
        else:
            return 'NodeSourceOption'

    @property
    def source_type(self):
        """
        **[Required]** Gets the source_type of this NodeSourceOption.
        The source type of this option.
        `IMAGE` means the OCID is of an image.

        Allowed values for this property are: "IMAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_type of this NodeSourceOption.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this NodeSourceOption.
        The source type of this option.
        `IMAGE` means the OCID is of an image.


        :param source_type: The source_type of this NodeSourceOption.
        :type: str
        """
        allowed_values = ["IMAGE"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            source_type = 'UNKNOWN_ENUM_VALUE'
        self._source_type = source_type

    @property
    def source_name(self):
        """
        Gets the source_name of this NodeSourceOption.
        The user-friendly name of the entity corresponding to the OCID.


        :return: The source_name of this NodeSourceOption.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this NodeSourceOption.
        The user-friendly name of the entity corresponding to the OCID.


        :param source_name: The source_name of this NodeSourceOption.
        :type: str
        """
        self._source_name = source_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
