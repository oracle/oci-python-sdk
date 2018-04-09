# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateZoneDetails(object):
    """
    The body for updating a zone.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateZoneDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param external_masters:
            The value to assign to the external_masters property of this UpdateZoneDetails.
        :type external_masters: list[ExternalMaster]

        """
        self.swagger_types = {
            'external_masters': 'list[ExternalMaster]'
        }

        self.attribute_map = {
            'external_masters': 'externalMasters'
        }

        self._external_masters = None

    @property
    def external_masters(self):
        """
        Gets the external_masters of this UpdateZoneDetails.
        External master servers for the zone.


        :return: The external_masters of this UpdateZoneDetails.
        :rtype: list[ExternalMaster]
        """
        return self._external_masters

    @external_masters.setter
    def external_masters(self, external_masters):
        """
        Sets the external_masters of this UpdateZoneDetails.
        External master servers for the zone.


        :param external_masters: The external_masters of this UpdateZoneDetails.
        :type: list[ExternalMaster]
        """
        self._external_masters = external_masters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
