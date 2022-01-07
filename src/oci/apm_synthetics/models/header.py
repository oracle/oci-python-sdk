# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Header(object):
    """
    Details of the header.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Header object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param header_name:
            The value to assign to the header_name property of this Header.
        :type header_name: str

        :param header_value:
            The value to assign to the header_value property of this Header.
        :type header_value: str

        """
        self.swagger_types = {
            'header_name': 'str',
            'header_value': 'str'
        }

        self.attribute_map = {
            'header_name': 'headerName',
            'header_value': 'headerValue'
        }

        self._header_name = None
        self._header_value = None

    @property
    def header_name(self):
        """
        **[Required]** Gets the header_name of this Header.
        Name of the header.


        :return: The header_name of this Header.
        :rtype: str
        """
        return self._header_name

    @header_name.setter
    def header_name(self, header_name):
        """
        Sets the header_name of this Header.
        Name of the header.


        :param header_name: The header_name of this Header.
        :type: str
        """
        self._header_name = header_name

    @property
    def header_value(self):
        """
        Gets the header_value of this Header.
        Value of the header.


        :return: The header_value of this Header.
        :rtype: str
        """
        return self._header_value

    @header_value.setter
    def header_value(self, header_value):
        """
        Sets the header_value of this Header.
        Value of the header.


        :param header_value: The header_value of this Header.
        :type: str
        """
        self._header_value = header_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
