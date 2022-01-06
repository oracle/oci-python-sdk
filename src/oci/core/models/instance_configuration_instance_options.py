# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationInstanceOptions(object):
    """
    Optional mutable instance options. As a part of Instance Metadata Service Security Header, This allows user to disable the legacy imds endpoints.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationInstanceOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param are_legacy_imds_endpoints_disabled:
            The value to assign to the are_legacy_imds_endpoints_disabled property of this InstanceConfigurationInstanceOptions.
        :type are_legacy_imds_endpoints_disabled: bool

        """
        self.swagger_types = {
            'are_legacy_imds_endpoints_disabled': 'bool'
        }

        self.attribute_map = {
            'are_legacy_imds_endpoints_disabled': 'areLegacyImdsEndpointsDisabled'
        }

        self._are_legacy_imds_endpoints_disabled = None

    @property
    def are_legacy_imds_endpoints_disabled(self):
        """
        Gets the are_legacy_imds_endpoints_disabled of this InstanceConfigurationInstanceOptions.
        Whether to disable the legacy (/v1) instance metadata service endpoints.
        Customers who have migrated to /v2 should set this to true for added security.
        Default is false.


        :return: The are_legacy_imds_endpoints_disabled of this InstanceConfigurationInstanceOptions.
        :rtype: bool
        """
        return self._are_legacy_imds_endpoints_disabled

    @are_legacy_imds_endpoints_disabled.setter
    def are_legacy_imds_endpoints_disabled(self, are_legacy_imds_endpoints_disabled):
        """
        Sets the are_legacy_imds_endpoints_disabled of this InstanceConfigurationInstanceOptions.
        Whether to disable the legacy (/v1) instance metadata service endpoints.
        Customers who have migrated to /v2 should set this to true for added security.
        Default is false.


        :param are_legacy_imds_endpoints_disabled: The are_legacy_imds_endpoints_disabled of this InstanceConfigurationInstanceOptions.
        :type: bool
        """
        self._are_legacy_imds_endpoints_disabled = are_legacy_imds_endpoints_disabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
