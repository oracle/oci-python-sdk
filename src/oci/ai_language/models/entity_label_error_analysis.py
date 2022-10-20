# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntityLabelErrorAnalysis(object):
    """
    Possible entity error label error details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EntityLabelErrorAnalysis object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this EntityLabelErrorAnalysis.
        :type type: str

        :param offset:
            The value to assign to the offset property of this EntityLabelErrorAnalysis.
        :type offset: int

        :param length:
            The value to assign to the length property of this EntityLabelErrorAnalysis.
        :type length: int

        """
        self.swagger_types = {
            'type': 'str',
            'offset': 'int',
            'length': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'offset': 'offset',
            'length': 'length'
        }

        self._type = None
        self._offset = None
        self._length = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this EntityLabelErrorAnalysis.
        Type of entity text like PER, LOC, GPE, NOPE etc.


        :return: The type of this EntityLabelErrorAnalysis.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this EntityLabelErrorAnalysis.
        Type of entity text like PER, LOC, GPE, NOPE etc.


        :param type: The type of this EntityLabelErrorAnalysis.
        :type: str
        """
        self._type = type

    @property
    def offset(self):
        """
        **[Required]** Gets the offset of this EntityLabelErrorAnalysis.
        Starting index on text.


        :return: The offset of this EntityLabelErrorAnalysis.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this EntityLabelErrorAnalysis.
        Starting index on text.


        :param offset: The offset of this EntityLabelErrorAnalysis.
        :type: int
        """
        self._offset = offset

    @property
    def length(self):
        """
        **[Required]** Gets the length of this EntityLabelErrorAnalysis.
        Length of text


        :return: The length of this EntityLabelErrorAnalysis.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this EntityLabelErrorAnalysis.
        Length of text


        :param length: The length of this EntityLabelErrorAnalysis.
        :type: int
        """
        self._length = length

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
