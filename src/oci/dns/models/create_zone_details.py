# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateZoneDetails(object):
    """
    The body for defining a new zone.
    """

    #: A constant which can be used with the zone_type property of a CreateZoneDetails.
    #: This constant has a value of "PRIMARY"
    ZONE_TYPE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the zone_type property of a CreateZoneDetails.
    #: This constant has a value of "SECONDARY"
    ZONE_TYPE_SECONDARY = "SECONDARY"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateZoneDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateZoneDetails.
        :type name: str

        :param zone_type:
            The value to assign to the zone_type property of this CreateZoneDetails.
            Allowed values for this property are: "PRIMARY", "SECONDARY"
        :type zone_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateZoneDetails.
        :type compartment_id: str

        :param external_masters:
            The value to assign to the external_masters property of this CreateZoneDetails.
        :type external_masters: list[ExternalMaster]

        """
        self.swagger_types = {
            'name': 'str',
            'zone_type': 'str',
            'compartment_id': 'str',
            'external_masters': 'list[ExternalMaster]'
        }

        self.attribute_map = {
            'name': 'name',
            'zone_type': 'zoneType',
            'compartment_id': 'compartmentId',
            'external_masters': 'externalMasters'
        }

        self._name = None
        self._zone_type = None
        self._compartment_id = None
        self._external_masters = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateZoneDetails.
        The name of the zone.


        :return: The name of this CreateZoneDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateZoneDetails.
        The name of the zone.


        :param name: The name of this CreateZoneDetails.
        :type: str
        """
        self._name = name

    @property
    def zone_type(self):
        """
        **[Required]** Gets the zone_type of this CreateZoneDetails.
        The type of the zone. Must be either `PRIMARY` or `SECONDARY`.

        Allowed values for this property are: "PRIMARY", "SECONDARY"


        :return: The zone_type of this CreateZoneDetails.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        """
        Sets the zone_type of this CreateZoneDetails.
        The type of the zone. Must be either `PRIMARY` or `SECONDARY`.


        :param zone_type: The zone_type of this CreateZoneDetails.
        :type: str
        """
        allowed_values = ["PRIMARY", "SECONDARY"]
        if not value_allowed_none_or_none_sentinel(zone_type, allowed_values):
            raise ValueError(
                "Invalid value for `zone_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._zone_type = zone_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateZoneDetails.
        The OCID of the compartment containing the zone.


        :return: The compartment_id of this CreateZoneDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateZoneDetails.
        The OCID of the compartment containing the zone.


        :param compartment_id: The compartment_id of this CreateZoneDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def external_masters(self):
        """
        Gets the external_masters of this CreateZoneDetails.
        External master servers for the zone.


        :return: The external_masters of this CreateZoneDetails.
        :rtype: list[ExternalMaster]
        """
        return self._external_masters

    @external_masters.setter
    def external_masters(self, external_masters):
        """
        Sets the external_masters of this CreateZoneDetails.
        External master servers for the zone.


        :param external_masters: The external_masters of this CreateZoneDetails.
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
