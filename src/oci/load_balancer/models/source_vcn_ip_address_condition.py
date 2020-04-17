# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .rule_condition import RuleCondition
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SourceVcnIpAddressCondition(RuleCondition):
    """
    An access control rule condition that requires a match on the specified source VCN and IP address range.
    This condition must be used only in conjunction with `SourceVcnIdCondition`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SourceVcnIpAddressCondition object with values from keyword arguments. The default value of the :py:attr:`~oci.load_balancer.models.SourceVcnIpAddressCondition.attribute_name` attribute
        of this class is ``SOURCE_VCN_IP_ADDRESS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_name:
            The value to assign to the attribute_name property of this SourceVcnIpAddressCondition.
            Allowed values for this property are: "SOURCE_IP_ADDRESS", "SOURCE_VCN_ID", "SOURCE_VCN_IP_ADDRESS", "PATH"
        :type attribute_name: str

        :param attribute_value:
            The value to assign to the attribute_value property of this SourceVcnIpAddressCondition.
        :type attribute_value: str

        """
        self.swagger_types = {
            'attribute_name': 'str',
            'attribute_value': 'str'
        }

        self.attribute_map = {
            'attribute_name': 'attributeName',
            'attribute_value': 'attributeValue'
        }

        self._attribute_name = None
        self._attribute_value = None
        self._attribute_name = 'SOURCE_VCN_IP_ADDRESS'

    @property
    def attribute_value(self):
        """
        **[Required]** Gets the attribute_value of this SourceVcnIpAddressCondition.
        An IPv4 address range that the original client IP address (in the context of the specified VCN) of an
        incoming packet must match.

        The service accepts only classless inter-domain routing (CIDR) format (x.x.x.x/y) strings.

        Specify 0.0.0.0/0 to match all incoming traffic in the customer VCN.

        example: \"10.10.1.0/24\"


        :return: The attribute_value of this SourceVcnIpAddressCondition.
        :rtype: str
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        """
        Sets the attribute_value of this SourceVcnIpAddressCondition.
        An IPv4 address range that the original client IP address (in the context of the specified VCN) of an
        incoming packet must match.

        The service accepts only classless inter-domain routing (CIDR) format (x.x.x.x/y) strings.

        Specify 0.0.0.0/0 to match all incoming traffic in the customer VCN.

        example: \"10.10.1.0/24\"


        :param attribute_value: The attribute_value of this SourceVcnIpAddressCondition.
        :type: str
        """
        self._attribute_value = attribute_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
