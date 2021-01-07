# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LimitValueSummary(object):
    """
    The value of a specific resource limit.
    """

    #: A constant which can be used with the scope_type property of a LimitValueSummary.
    #: This constant has a value of "GLOBAL"
    SCOPE_TYPE_GLOBAL = "GLOBAL"

    #: A constant which can be used with the scope_type property of a LimitValueSummary.
    #: This constant has a value of "REGION"
    SCOPE_TYPE_REGION = "REGION"

    #: A constant which can be used with the scope_type property of a LimitValueSummary.
    #: This constant has a value of "AD"
    SCOPE_TYPE_AD = "AD"

    def __init__(self, **kwargs):
        """
        Initializes a new LimitValueSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this LimitValueSummary.
        :type name: str

        :param scope_type:
            The value to assign to the scope_type property of this LimitValueSummary.
            Allowed values for this property are: "GLOBAL", "REGION", "AD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scope_type: str

        :param availability_domain:
            The value to assign to the availability_domain property of this LimitValueSummary.
        :type availability_domain: str

        :param value:
            The value to assign to the value property of this LimitValueSummary.
        :type value: int

        """
        self.swagger_types = {
            'name': 'str',
            'scope_type': 'str',
            'availability_domain': 'str',
            'value': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'scope_type': 'scopeType',
            'availability_domain': 'availabilityDomain',
            'value': 'value'
        }

        self._name = None
        self._scope_type = None
        self._availability_domain = None
        self._value = None

    @property
    def name(self):
        """
        Gets the name of this LimitValueSummary.
        The resource limit name. To be used for writing policies (in case of quotas) or other programmatic calls.


        :return: The name of this LimitValueSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LimitValueSummary.
        The resource limit name. To be used for writing policies (in case of quotas) or other programmatic calls.


        :param name: The name of this LimitValueSummary.
        :type: str
        """
        self._name = name

    @property
    def scope_type(self):
        """
        Gets the scope_type of this LimitValueSummary.
        The scope type of the limit.

        Allowed values for this property are: "GLOBAL", "REGION", "AD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The scope_type of this LimitValueSummary.
        :rtype: str
        """
        return self._scope_type

    @scope_type.setter
    def scope_type(self, scope_type):
        """
        Sets the scope_type of this LimitValueSummary.
        The scope type of the limit.


        :param scope_type: The scope_type of this LimitValueSummary.
        :type: str
        """
        allowed_values = ["GLOBAL", "REGION", "AD"]
        if not value_allowed_none_or_none_sentinel(scope_type, allowed_values):
            scope_type = 'UNKNOWN_ENUM_VALUE'
        self._scope_type = scope_type

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this LimitValueSummary.
        If present, the returned value is only specific to this availability domain.


        :return: The availability_domain of this LimitValueSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this LimitValueSummary.
        If present, the returned value is only specific to this availability domain.


        :param availability_domain: The availability_domain of this LimitValueSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def value(self):
        """
        Gets the value of this LimitValueSummary.
        The resource limit value.


        :return: The value of this LimitValueSummary.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this LimitValueSummary.
        The resource limit value.


        :param value: The value of this LimitValueSummary.
        :type: int
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
