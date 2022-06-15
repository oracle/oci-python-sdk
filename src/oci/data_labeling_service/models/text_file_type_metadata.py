# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TextFileTypeMetadata(object):
    """
    Metadata for files with text content.
    """

    #: A constant which can be used with the format_type property of a TextFileTypeMetadata.
    #: This constant has a value of "DELIMITED"
    FORMAT_TYPE_DELIMITED = "DELIMITED"

    def __init__(self, **kwargs):
        """
        Initializes a new TextFileTypeMetadata object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_labeling_service.models.DelimitedFileTypeMetadata`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param format_type:
            The value to assign to the format_type property of this TextFileTypeMetadata.
            Allowed values for this property are: "DELIMITED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type format_type: str

        """
        self.swagger_types = {
            'format_type': 'str'
        }

        self.attribute_map = {
            'format_type': 'formatType'
        }

        self._format_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['formatType']

        if type == 'DELIMITED':
            return 'DelimitedFileTypeMetadata'
        else:
            return 'TextFileTypeMetadata'

    @property
    def format_type(self):
        """
        **[Required]** Gets the format_type of this TextFileTypeMetadata.
        It defines the format type of text files.

        Allowed values for this property are: "DELIMITED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The format_type of this TextFileTypeMetadata.
        :rtype: str
        """
        return self._format_type

    @format_type.setter
    def format_type(self, format_type):
        """
        Sets the format_type of this TextFileTypeMetadata.
        It defines the format type of text files.


        :param format_type: The format_type of this TextFileTypeMetadata.
        :type: str
        """
        allowed_values = ["DELIMITED"]
        if not value_allowed_none_or_none_sentinel(format_type, allowed_values):
            format_type = 'UNKNOWN_ENUM_VALUE'
        self._format_type = format_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
