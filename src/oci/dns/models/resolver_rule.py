# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResolverRule(object):
    """
    A rule for a resolver. Specifying both qnameCoverConditions and clientAddressConditions is not allowed.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the action property of a ResolverRule.
    #: This constant has a value of "FORWARD"
    ACTION_FORWARD = "FORWARD"

    def __init__(self, **kwargs):
        """
        Initializes a new ResolverRule object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.dns.models.ResolverForwardRule`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param client_address_conditions:
            The value to assign to the client_address_conditions property of this ResolverRule.
        :type client_address_conditions: list[str]

        :param qname_cover_conditions:
            The value to assign to the qname_cover_conditions property of this ResolverRule.
        :type qname_cover_conditions: list[str]

        :param action:
            The value to assign to the action property of this ResolverRule.
            Allowed values for this property are: "FORWARD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        """
        self.swagger_types = {
            'client_address_conditions': 'list[str]',
            'qname_cover_conditions': 'list[str]',
            'action': 'str'
        }

        self.attribute_map = {
            'client_address_conditions': 'clientAddressConditions',
            'qname_cover_conditions': 'qnameCoverConditions',
            'action': 'action'
        }

        self._client_address_conditions = None
        self._qname_cover_conditions = None
        self._action = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['action']

        if type == 'FORWARD':
            return 'ResolverForwardRule'
        else:
            return 'ResolverRule'

    @property
    def client_address_conditions(self):
        """
        **[Required]** Gets the client_address_conditions of this ResolverRule.
        A list of CIDR blocks. The query must come from a client within one of the blocks in order for the rule action
        to apply.


        :return: The client_address_conditions of this ResolverRule.
        :rtype: list[str]
        """
        return self._client_address_conditions

    @client_address_conditions.setter
    def client_address_conditions(self, client_address_conditions):
        """
        Sets the client_address_conditions of this ResolverRule.
        A list of CIDR blocks. The query must come from a client within one of the blocks in order for the rule action
        to apply.


        :param client_address_conditions: The client_address_conditions of this ResolverRule.
        :type: list[str]
        """
        self._client_address_conditions = client_address_conditions

    @property
    def qname_cover_conditions(self):
        """
        **[Required]** Gets the qname_cover_conditions of this ResolverRule.
        A list of domain names. The query must be covered by one of the domains in order for the rule action to apply.


        :return: The qname_cover_conditions of this ResolverRule.
        :rtype: list[str]
        """
        return self._qname_cover_conditions

    @qname_cover_conditions.setter
    def qname_cover_conditions(self, qname_cover_conditions):
        """
        Sets the qname_cover_conditions of this ResolverRule.
        A list of domain names. The query must be covered by one of the domains in order for the rule action to apply.


        :param qname_cover_conditions: The qname_cover_conditions of this ResolverRule.
        :type: list[str]
        """
        self._qname_cover_conditions = qname_cover_conditions

    @property
    def action(self):
        """
        **[Required]** Gets the action of this ResolverRule.
        The action determines the behavior of the rule. If a query matches a supplied condition then the action will
        apply. If there are no conditions on the rule then all queries are subject to the specified action.
        * `FORWARD` - Matching requests will be forwarded from the source interface to the destination address.

        Allowed values for this property are: "FORWARD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this ResolverRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ResolverRule.
        The action determines the behavior of the rule. If a query matches a supplied condition then the action will
        apply. If there are no conditions on the rule then all queries are subject to the specified action.
        * `FORWARD` - Matching requests will be forwarded from the source interface to the destination address.


        :param action: The action of this ResolverRule.
        :type: str
        """
        allowed_values = ["FORWARD"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
