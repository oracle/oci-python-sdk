# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateGoldenGateDetails(object):
    """
    Details about Oracle GoldenGate Microservices. If an empty object is specified, the stored Golden Gate details will be removed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateGoldenGateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hub:
            The value to assign to the hub property of this UpdateGoldenGateDetails.
        :type hub: oci.database_migration.models.UpdateGoldenGateHub

        :param settings:
            The value to assign to the settings property of this UpdateGoldenGateDetails.
        :type settings: oci.database_migration.models.UpdateGoldenGateSettings

        """
        self.swagger_types = {
            'hub': 'UpdateGoldenGateHub',
            'settings': 'UpdateGoldenGateSettings'
        }

        self.attribute_map = {
            'hub': 'hub',
            'settings': 'settings'
        }

        self._hub = None
        self._settings = None

    @property
    def hub(self):
        """
        Gets the hub of this UpdateGoldenGateDetails.

        :return: The hub of this UpdateGoldenGateDetails.
        :rtype: oci.database_migration.models.UpdateGoldenGateHub
        """
        return self._hub

    @hub.setter
    def hub(self, hub):
        """
        Sets the hub of this UpdateGoldenGateDetails.

        :param hub: The hub of this UpdateGoldenGateDetails.
        :type: oci.database_migration.models.UpdateGoldenGateHub
        """
        self._hub = hub

    @property
    def settings(self):
        """
        Gets the settings of this UpdateGoldenGateDetails.

        :return: The settings of this UpdateGoldenGateDetails.
        :rtype: oci.database_migration.models.UpdateGoldenGateSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """
        Sets the settings of this UpdateGoldenGateDetails.

        :param settings: The settings of this UpdateGoldenGateDetails.
        :type: oci.database_migration.models.UpdateGoldenGateSettings
        """
        self._settings = settings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
