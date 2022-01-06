# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HeaderValidationItem(object):
    """
    Header validation properties.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HeaderValidationItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param required:
            The value to assign to the required property of this HeaderValidationItem.
        :type required: bool

        :param name:
            The value to assign to the name property of this HeaderValidationItem.
        :type name: str

        """
        self.swagger_types = {
            'required': 'bool',
            'name': 'str'
        }

        self.attribute_map = {
            'required': 'required',
            'name': 'name'
        }

        self._required = None
        self._name = None

    @property
    def required(self):
        """
        Gets the required of this HeaderValidationItem.
        Determines if the header is required in the request.


        :return: The required of this HeaderValidationItem.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this HeaderValidationItem.
        Determines if the header is required in the request.


        :param required: The required of this HeaderValidationItem.
        :type: bool
        """
        self._required = required

    @property
    def name(self):
        """
        **[Required]** Gets the name of this HeaderValidationItem.
        Parameter name.


        :return: The name of this HeaderValidationItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HeaderValidationItem.
        Parameter name.


        :param name: The name of this HeaderValidationItem.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
