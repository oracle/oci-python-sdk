# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParserAction(object):
    """
    A parser action. Typically refers to an operation to be performed while fetching or parsing the logs. Example: Unzip.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ParserAction object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ParserAction.
        :type name: str

        :param order:
            The value to assign to the order property of this ParserAction.
        :type order: int

        """
        self.swagger_types = {
            'name': 'str',
            'order': 'int'
        }
        self.attribute_map = {
            'name': 'name',
            'order': 'order'
        }
        self._name = None
        self._order = None

    @property
    def name(self):
        """
        Gets the name of this ParserAction.
        Parser action name.


        :return: The name of this ParserAction.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ParserAction.
        Parser action name.


        :param name: The name of this ParserAction.
        :type: str
        """
        self._name = name

    @property
    def order(self):
        """
        Gets the order of this ParserAction.
        Parser action order.


        :return: The order of this ParserAction.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this ParserAction.
        Parser action order.


        :param order: The order of this ParserAction.
        :type: int
        """
        self._order = order

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
