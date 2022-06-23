# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .allowed_security_configuration import AllowedSecurityConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StatefulNsgConfiguration(AllowedSecurityConfiguration):
    """
    Defines the stateful network security group configuration that allowed the traffic.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StatefulNsgConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.StatefulNsgConfiguration.type` attribute
        of this class is ``STATEFUL_NSG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this StatefulNsgConfiguration.
            Allowed values for this property are: "NSG", "STATEFUL_NSG", "INGRESS_SECURITY_LIST", "STATEFUL_INGRESS_SECURITY_LIST", "EGRESS_SECURITY_LIST", "STATEFUL_EGRESS_SECURITY_LIST"
        :type type: str

        :param nsg_id:
            The value to assign to the nsg_id property of this StatefulNsgConfiguration.
        :type nsg_id: str

        :param security_rule:
            The value to assign to the security_rule property of this StatefulNsgConfiguration.
        :type security_rule: oci.vn_monitoring.models.SecurityRule

        """
        self.swagger_types = {
            'type': 'str',
            'nsg_id': 'str',
            'security_rule': 'SecurityRule'
        }

        self.attribute_map = {
            'type': 'type',
            'nsg_id': 'nsgId',
            'security_rule': 'securityRule'
        }

        self._type = None
        self._nsg_id = None
        self._security_rule = None
        self._type = 'STATEFUL_NSG'

    @property
    def nsg_id(self):
        """
        **[Required]** Gets the nsg_id of this StatefulNsgConfiguration.
        The `OCID`__ of the network
        security group that allowed the traffic.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsg_id of this StatefulNsgConfiguration.
        :rtype: str
        """
        return self._nsg_id

    @nsg_id.setter
    def nsg_id(self, nsg_id):
        """
        Sets the nsg_id of this StatefulNsgConfiguration.
        The `OCID`__ of the network
        security group that allowed the traffic.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsg_id: The nsg_id of this StatefulNsgConfiguration.
        :type: str
        """
        self._nsg_id = nsg_id

    @property
    def security_rule(self):
        """
        **[Required]** Gets the security_rule of this StatefulNsgConfiguration.

        :return: The security_rule of this StatefulNsgConfiguration.
        :rtype: oci.vn_monitoring.models.SecurityRule
        """
        return self._security_rule

    @security_rule.setter
    def security_rule(self, security_rule):
        """
        Sets the security_rule of this StatefulNsgConfiguration.

        :param security_rule: The security_rule of this StatefulNsgConfiguration.
        :type: oci.vn_monitoring.models.SecurityRule
        """
        self._security_rule = security_rule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
