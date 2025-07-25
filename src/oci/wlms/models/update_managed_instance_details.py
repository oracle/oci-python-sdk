# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateManagedInstanceDetails(object):
    """
    The details to update for a managed instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateManagedInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param configuration:
            The value to assign to the configuration property of this UpdateManagedInstanceDetails.
        :type configuration: oci.wlms.models.UpdateManagedInstanceConfigurationDetails

        """
        self.swagger_types = {
            'configuration': 'UpdateManagedInstanceConfigurationDetails'
        }
        self.attribute_map = {
            'configuration': 'configuration'
        }
        self._configuration = None

    @property
    def configuration(self):
        """
        Gets the configuration of this UpdateManagedInstanceDetails.

        :return: The configuration of this UpdateManagedInstanceDetails.
        :rtype: oci.wlms.models.UpdateManagedInstanceConfigurationDetails
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this UpdateManagedInstanceDetails.

        :param configuration: The configuration of this UpdateManagedInstanceDetails.
        :type: oci.wlms.models.UpdateManagedInstanceConfigurationDetails
        """
        self._configuration = configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
