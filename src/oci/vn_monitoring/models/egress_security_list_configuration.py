# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .allowed_security_configuration import AllowedSecurityConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EgressSecurityListConfiguration(AllowedSecurityConfiguration):
    """
    Defines the subnet egress security list configuration that allowed the traffic.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EgressSecurityListConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.EgressSecurityListConfiguration.type` attribute
        of this class is ``EGRESS_SECURITY_LIST`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this EgressSecurityListConfiguration.
            Allowed values for this property are: "NSG", "STATEFUL_NSG", "INGRESS_SECURITY_LIST", "STATEFUL_INGRESS_SECURITY_LIST", "EGRESS_SECURITY_LIST", "STATEFUL_EGRESS_SECURITY_LIST"
        :type type: str

        :param security_list_id:
            The value to assign to the security_list_id property of this EgressSecurityListConfiguration.
        :type security_list_id: str

        :param security_rule:
            The value to assign to the security_rule property of this EgressSecurityListConfiguration.
        :type security_rule: oci.vn_monitoring.models.EgressSecurityRule

        """
        self.swagger_types = {
            'type': 'str',
            'security_list_id': 'str',
            'security_rule': 'EgressSecurityRule'
        }

        self.attribute_map = {
            'type': 'type',
            'security_list_id': 'securityListId',
            'security_rule': 'securityRule'
        }

        self._type = None
        self._security_list_id = None
        self._security_rule = None
        self._type = 'EGRESS_SECURITY_LIST'

    @property
    def security_list_id(self):
        """
        **[Required]** Gets the security_list_id of this EgressSecurityListConfiguration.
        The `OCID`__ of the security
        list that allowed the traffic.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The security_list_id of this EgressSecurityListConfiguration.
        :rtype: str
        """
        return self._security_list_id

    @security_list_id.setter
    def security_list_id(self, security_list_id):
        """
        Sets the security_list_id of this EgressSecurityListConfiguration.
        The `OCID`__ of the security
        list that allowed the traffic.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param security_list_id: The security_list_id of this EgressSecurityListConfiguration.
        :type: str
        """
        self._security_list_id = security_list_id

    @property
    def security_rule(self):
        """
        **[Required]** Gets the security_rule of this EgressSecurityListConfiguration.

        :return: The security_rule of this EgressSecurityListConfiguration.
        :rtype: oci.vn_monitoring.models.EgressSecurityRule
        """
        return self._security_rule

    @security_rule.setter
    def security_rule(self, security_rule):
        """
        Sets the security_rule of this EgressSecurityListConfiguration.

        :param security_rule: The security_rule of this EgressSecurityListConfiguration.
        :type: oci.vn_monitoring.models.EgressSecurityRule
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
