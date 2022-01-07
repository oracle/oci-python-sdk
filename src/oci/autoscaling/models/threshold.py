# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Threshold(object):
    """
    Threshold model.
    """

    #: A constant which can be used with the operator property of a Threshold.
    #: This constant has a value of "GT"
    OPERATOR_GT = "GT"

    #: A constant which can be used with the operator property of a Threshold.
    #: This constant has a value of "GTE"
    OPERATOR_GTE = "GTE"

    #: A constant which can be used with the operator property of a Threshold.
    #: This constant has a value of "LT"
    OPERATOR_LT = "LT"

    #: A constant which can be used with the operator property of a Threshold.
    #: This constant has a value of "LTE"
    OPERATOR_LTE = "LTE"

    def __init__(self, **kwargs):
        """
        Initializes a new Threshold object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operator:
            The value to assign to the operator property of this Threshold.
            Allowed values for this property are: "GT", "GTE", "LT", "LTE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operator: str

        :param value:
            The value to assign to the value property of this Threshold.
        :type value: int

        """
        self.swagger_types = {
            'operator': 'str',
            'value': 'int'
        }

        self.attribute_map = {
            'operator': 'operator',
            'value': 'value'
        }

        self._operator = None
        self._value = None

    @property
    def operator(self):
        """
        **[Required]** Gets the operator of this Threshold.
        The comparison operator to use. Options are greater than (`GT`), greater than or equal to
        (`GTE`), less than (`LT`), and less than or equal to (`LTE`).

        Allowed values for this property are: "GT", "GTE", "LT", "LTE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operator of this Threshold.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this Threshold.
        The comparison operator to use. Options are greater than (`GT`), greater than or equal to
        (`GTE`), less than (`LT`), and less than or equal to (`LTE`).


        :param operator: The operator of this Threshold.
        :type: str
        """
        allowed_values = ["GT", "GTE", "LT", "LTE"]
        if not value_allowed_none_or_none_sentinel(operator, allowed_values):
            operator = 'UNKNOWN_ENUM_VALUE'
        self._operator = operator

    @property
    def value(self):
        """
        **[Required]** Gets the value of this Threshold.

        :return: The value of this Threshold.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Threshold.

        :param value: The value of this Threshold.
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
