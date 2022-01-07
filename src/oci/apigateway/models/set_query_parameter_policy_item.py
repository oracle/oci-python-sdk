# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SetQueryParameterPolicyItem(object):
    """
    Set will add a new query parameter if it was not in the original request.  If the parameter already exists on the
    request, you can choose to override, append, or skip it.
    """

    #: A constant which can be used with the if_exists property of a SetQueryParameterPolicyItem.
    #: This constant has a value of "OVERWRITE"
    IF_EXISTS_OVERWRITE = "OVERWRITE"

    #: A constant which can be used with the if_exists property of a SetQueryParameterPolicyItem.
    #: This constant has a value of "APPEND"
    IF_EXISTS_APPEND = "APPEND"

    #: A constant which can be used with the if_exists property of a SetQueryParameterPolicyItem.
    #: This constant has a value of "SKIP"
    IF_EXISTS_SKIP = "SKIP"

    def __init__(self, **kwargs):
        """
        Initializes a new SetQueryParameterPolicyItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SetQueryParameterPolicyItem.
        :type name: str

        :param values:
            The value to assign to the values property of this SetQueryParameterPolicyItem.
        :type values: list[str]

        :param if_exists:
            The value to assign to the if_exists property of this SetQueryParameterPolicyItem.
            Allowed values for this property are: "OVERWRITE", "APPEND", "SKIP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type if_exists: str

        """
        self.swagger_types = {
            'name': 'str',
            'values': 'list[str]',
            'if_exists': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'values': 'values',
            'if_exists': 'ifExists'
        }

        self._name = None
        self._values = None
        self._if_exists = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SetQueryParameterPolicyItem.
        The case-sensitive name of the query parameter.  This name must be unique across transformation policies.


        :return: The name of this SetQueryParameterPolicyItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SetQueryParameterPolicyItem.
        The case-sensitive name of the query parameter.  This name must be unique across transformation policies.


        :param name: The name of this SetQueryParameterPolicyItem.
        :type: str
        """
        self._name = name

    @property
    def values(self):
        """
        **[Required]** Gets the values of this SetQueryParameterPolicyItem.
        A list of new values.  Each value can be a constant or may include one or more expressions enclosed within
        ${} delimiters.


        :return: The values of this SetQueryParameterPolicyItem.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this SetQueryParameterPolicyItem.
        A list of new values.  Each value can be a constant or may include one or more expressions enclosed within
        ${} delimiters.


        :param values: The values of this SetQueryParameterPolicyItem.
        :type: list[str]
        """
        self._values = values

    @property
    def if_exists(self):
        """
        Gets the if_exists of this SetQueryParameterPolicyItem.
        If a query parameter with the same name already exists in the request, OVERWRITE will overwrite the value,
        APPEND will append to the existing value, or SKIP will keep the existing value.

        Allowed values for this property are: "OVERWRITE", "APPEND", "SKIP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The if_exists of this SetQueryParameterPolicyItem.
        :rtype: str
        """
        return self._if_exists

    @if_exists.setter
    def if_exists(self, if_exists):
        """
        Sets the if_exists of this SetQueryParameterPolicyItem.
        If a query parameter with the same name already exists in the request, OVERWRITE will overwrite the value,
        APPEND will append to the existing value, or SKIP will keep the existing value.


        :param if_exists: The if_exists of this SetQueryParameterPolicyItem.
        :type: str
        """
        allowed_values = ["OVERWRITE", "APPEND", "SKIP"]
        if not value_allowed_none_or_none_sentinel(if_exists, allowed_values):
            if_exists = 'UNKNOWN_ENUM_VALUE'
        self._if_exists = if_exists

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
