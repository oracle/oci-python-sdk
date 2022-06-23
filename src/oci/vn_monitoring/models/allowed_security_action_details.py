# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AllowedSecurityActionDetails(object):
    """
    Defines details for the security action taken on allowed traffic.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AllowedSecurityActionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_restricted_or_partial:
            The value to assign to the is_restricted_or_partial property of this AllowedSecurityActionDetails.
        :type is_restricted_or_partial: bool

        :param allowed_security_configuration:
            The value to assign to the allowed_security_configuration property of this AllowedSecurityActionDetails.
        :type allowed_security_configuration: oci.vn_monitoring.models.AllowedSecurityConfiguration

        """
        self.swagger_types = {
            'is_restricted_or_partial': 'bool',
            'allowed_security_configuration': 'AllowedSecurityConfiguration'
        }

        self.attribute_map = {
            'is_restricted_or_partial': 'isRestrictedOrPartial',
            'allowed_security_configuration': 'allowedSecurityConfiguration'
        }

        self._is_restricted_or_partial = None
        self._allowed_security_configuration = None

    @property
    def is_restricted_or_partial(self):
        """
        **[Required]** Gets the is_restricted_or_partial of this AllowedSecurityActionDetails.
        If true, the allowed security configuration details are incomplete.


        :return: The is_restricted_or_partial of this AllowedSecurityActionDetails.
        :rtype: bool
        """
        return self._is_restricted_or_partial

    @is_restricted_or_partial.setter
    def is_restricted_or_partial(self, is_restricted_or_partial):
        """
        Sets the is_restricted_or_partial of this AllowedSecurityActionDetails.
        If true, the allowed security configuration details are incomplete.


        :param is_restricted_or_partial: The is_restricted_or_partial of this AllowedSecurityActionDetails.
        :type: bool
        """
        self._is_restricted_or_partial = is_restricted_or_partial

    @property
    def allowed_security_configuration(self):
        """
        Gets the allowed_security_configuration of this AllowedSecurityActionDetails.

        :return: The allowed_security_configuration of this AllowedSecurityActionDetails.
        :rtype: oci.vn_monitoring.models.AllowedSecurityConfiguration
        """
        return self._allowed_security_configuration

    @allowed_security_configuration.setter
    def allowed_security_configuration(self, allowed_security_configuration):
        """
        Sets the allowed_security_configuration of this AllowedSecurityActionDetails.

        :param allowed_security_configuration: The allowed_security_configuration of this AllowedSecurityActionDetails.
        :type: oci.vn_monitoring.models.AllowedSecurityConfiguration
        """
        self._allowed_security_configuration = allowed_security_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
