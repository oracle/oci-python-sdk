# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RuleCondition(object):
    """
    A condition to apply to an access control rule.
    """

    #: A constant which can be used with the attribute_name property of a RuleCondition.
    #: This constant has a value of "SOURCE_IP_ADDRESS"
    ATTRIBUTE_NAME_SOURCE_IP_ADDRESS = "SOURCE_IP_ADDRESS"

    #: A constant which can be used with the attribute_name property of a RuleCondition.
    #: This constant has a value of "SOURCE_VCN_ID"
    ATTRIBUTE_NAME_SOURCE_VCN_ID = "SOURCE_VCN_ID"

    #: A constant which can be used with the attribute_name property of a RuleCondition.
    #: This constant has a value of "SOURCE_VCN_IP_ADDRESS"
    ATTRIBUTE_NAME_SOURCE_VCN_IP_ADDRESS = "SOURCE_VCN_IP_ADDRESS"

    #: A constant which can be used with the attribute_name property of a RuleCondition.
    #: This constant has a value of "PATH"
    ATTRIBUTE_NAME_PATH = "PATH"

    def __init__(self, **kwargs):
        """
        Initializes a new RuleCondition object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.load_balancer.models.SourceVcnIdCondition`
        * :class:`~oci.load_balancer.models.SourceIpAddressCondition`
        * :class:`~oci.load_balancer.models.PathMatchCondition`
        * :class:`~oci.load_balancer.models.SourceVcnIpAddressCondition`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_name:
            The value to assign to the attribute_name property of this RuleCondition.
            Allowed values for this property are: "SOURCE_IP_ADDRESS", "SOURCE_VCN_ID", "SOURCE_VCN_IP_ADDRESS", "PATH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type attribute_name: str

        """
        self.swagger_types = {
            'attribute_name': 'str'
        }

        self.attribute_map = {
            'attribute_name': 'attributeName'
        }

        self._attribute_name = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['attributeName']

        if type == 'SOURCE_VCN_ID':
            return 'SourceVcnIdCondition'

        if type == 'SOURCE_IP_ADDRESS':
            return 'SourceIpAddressCondition'

        if type == 'PATH':
            return 'PathMatchCondition'

        if type == 'SOURCE_VCN_IP_ADDRESS':
            return 'SourceVcnIpAddressCondition'
        else:
            return 'RuleCondition'

    @property
    def attribute_name(self):
        """
        **[Required]** Gets the attribute_name of this RuleCondition.
        Allowed values for this property are: "SOURCE_IP_ADDRESS", "SOURCE_VCN_ID", "SOURCE_VCN_IP_ADDRESS", "PATH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The attribute_name of this RuleCondition.
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """
        Sets the attribute_name of this RuleCondition.

        :param attribute_name: The attribute_name of this RuleCondition.
        :type: str
        """
        allowed_values = ["SOURCE_IP_ADDRESS", "SOURCE_VCN_ID", "SOURCE_VCN_IP_ADDRESS", "PATH"]
        if not value_allowed_none_or_none_sentinel(attribute_name, allowed_values):
            attribute_name = 'UNKNOWN_ENUM_VALUE'
        self._attribute_name = attribute_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
