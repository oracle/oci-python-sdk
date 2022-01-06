# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateStorageDetails(object):
    """
    This is the input to update storage configuration of a tenancy in Logan Analytics application
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateStorageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param archiving_configuration:
            The value to assign to the archiving_configuration property of this UpdateStorageDetails.
        :type archiving_configuration: oci.log_analytics.models.ArchivingConfiguration

        """
        self.swagger_types = {
            'archiving_configuration': 'ArchivingConfiguration'
        }

        self.attribute_map = {
            'archiving_configuration': 'archivingConfiguration'
        }

        self._archiving_configuration = None

    @property
    def archiving_configuration(self):
        """
        **[Required]** Gets the archiving_configuration of this UpdateStorageDetails.

        :return: The archiving_configuration of this UpdateStorageDetails.
        :rtype: oci.log_analytics.models.ArchivingConfiguration
        """
        return self._archiving_configuration

    @archiving_configuration.setter
    def archiving_configuration(self, archiving_configuration):
        """
        Sets the archiving_configuration of this UpdateStorageDetails.

        :param archiving_configuration: The archiving_configuration of this UpdateStorageDetails.
        :type: oci.log_analytics.models.ArchivingConfiguration
        """
        self._archiving_configuration = archiving_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
