# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FilterQueryParameterPolicyItem(object):
    """
    A query parameter to drop (with BLOCK) or pass through (with ALLOW).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FilterQueryParameterPolicyItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this FilterQueryParameterPolicyItem.
        :type name: str

        """
        self.swagger_types = {
            'name': 'str'
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this FilterQueryParameterPolicyItem.
        The case-sensitive name of the query parameter.


        :return: The name of this FilterQueryParameterPolicyItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FilterQueryParameterPolicyItem.
        The case-sensitive name of the query parameter.


        :param name: The name of this FilterQueryParameterPolicyItem.
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
