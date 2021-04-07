# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateGoldenGateDetails(object):
    """
    Details about Oracle GoldenGate Microservices. Required for online logical migration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateGoldenGateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hub:
            The value to assign to the hub property of this CreateGoldenGateDetails.
        :type hub: oci.database_migration.models.CreateGoldenGateHub

        :param settings:
            The value to assign to the settings property of this CreateGoldenGateDetails.
        :type settings: oci.database_migration.models.CreateGoldenGateSettings

        """
        self.swagger_types = {
            'hub': 'CreateGoldenGateHub',
            'settings': 'CreateGoldenGateSettings'
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
        **[Required]** Gets the hub of this CreateGoldenGateDetails.

        :return: The hub of this CreateGoldenGateDetails.
        :rtype: oci.database_migration.models.CreateGoldenGateHub
        """
        return self._hub

    @hub.setter
    def hub(self, hub):
        """
        Sets the hub of this CreateGoldenGateDetails.

        :param hub: The hub of this CreateGoldenGateDetails.
        :type: oci.database_migration.models.CreateGoldenGateHub
        """
        self._hub = hub

    @property
    def settings(self):
        """
        Gets the settings of this CreateGoldenGateDetails.

        :return: The settings of this CreateGoldenGateDetails.
        :rtype: oci.database_migration.models.CreateGoldenGateSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """
        Sets the settings of this CreateGoldenGateDetails.

        :param settings: The settings of this CreateGoldenGateDetails.
        :type: oci.database_migration.models.CreateGoldenGateSettings
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
