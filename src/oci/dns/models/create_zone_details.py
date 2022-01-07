# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_zone_base_details import CreateZoneBaseDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateZoneDetails(CreateZoneBaseDetails):
    """
    The body for defining a new zone.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the zone_type property of a CreateZoneDetails.
    #: This constant has a value of "PRIMARY"
    ZONE_TYPE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the zone_type property of a CreateZoneDetails.
    #: This constant has a value of "SECONDARY"
    ZONE_TYPE_SECONDARY = "SECONDARY"

    #: A constant which can be used with the scope property of a CreateZoneDetails.
    #: This constant has a value of "GLOBAL"
    SCOPE_GLOBAL = "GLOBAL"

    #: A constant which can be used with the scope property of a CreateZoneDetails.
    #: This constant has a value of "PRIVATE"
    SCOPE_PRIVATE = "PRIVATE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateZoneDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.dns.models.CreateZoneDetails.migration_source` attribute
        of this class is ``NONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param migration_source:
            The value to assign to the migration_source property of this CreateZoneDetails.
            Allowed values for this property are: "NONE", "DYNECT"
        :type migration_source: str

        :param name:
            The value to assign to the name property of this CreateZoneDetails.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateZoneDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateZoneDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateZoneDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param zone_type:
            The value to assign to the zone_type property of this CreateZoneDetails.
            Allowed values for this property are: "PRIMARY", "SECONDARY"
        :type zone_type: str

        :param view_id:
            The value to assign to the view_id property of this CreateZoneDetails.
        :type view_id: str

        :param scope:
            The value to assign to the scope property of this CreateZoneDetails.
            Allowed values for this property are: "GLOBAL", "PRIVATE"
        :type scope: str

        :param external_masters:
            The value to assign to the external_masters property of this CreateZoneDetails.
        :type external_masters: list[oci.dns.models.ExternalMaster]

        """
        self.swagger_types = {
            'migration_source': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'zone_type': 'str',
            'view_id': 'str',
            'scope': 'str',
            'external_masters': 'list[ExternalMaster]'
        }

        self.attribute_map = {
            'migration_source': 'migrationSource',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'zone_type': 'zoneType',
            'view_id': 'viewId',
            'scope': 'scope',
            'external_masters': 'externalMasters'
        }

        self._migration_source = None
        self._name = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._zone_type = None
        self._view_id = None
        self._scope = None
        self._external_masters = None
        self._migration_source = 'NONE'

    @property
    def zone_type(self):
        """
        Gets the zone_type of this CreateZoneDetails.
        The type of the zone. Must be either `PRIMARY` or `SECONDARY`. `SECONDARY` is only supported for GLOBAL
        zones.

        Allowed values for this property are: "PRIMARY", "SECONDARY"


        :return: The zone_type of this CreateZoneDetails.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        """
        Sets the zone_type of this CreateZoneDetails.
        The type of the zone. Must be either `PRIMARY` or `SECONDARY`. `SECONDARY` is only supported for GLOBAL
        zones.


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
    def view_id(self):
        """
        Gets the view_id of this CreateZoneDetails.
        This value will be null for zones in the global DNS.


        :return: The view_id of this CreateZoneDetails.
        :rtype: str
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        """
        Sets the view_id of this CreateZoneDetails.
        This value will be null for zones in the global DNS.


        :param view_id: The view_id of this CreateZoneDetails.
        :type: str
        """
        self._view_id = view_id

    @property
    def scope(self):
        """
        Gets the scope of this CreateZoneDetails.
        The scope of the zone.

        Allowed values for this property are: "GLOBAL", "PRIVATE"


        :return: The scope of this CreateZoneDetails.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this CreateZoneDetails.
        The scope of the zone.


        :param scope: The scope of this CreateZoneDetails.
        :type: str
        """
        allowed_values = ["GLOBAL", "PRIVATE"]
        if not value_allowed_none_or_none_sentinel(scope, allowed_values):
            raise ValueError(
                "Invalid value for `scope`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._scope = scope

    @property
    def external_masters(self):
        """
        Gets the external_masters of this CreateZoneDetails.
        External master servers for the zone. `externalMasters` becomes a
        required parameter when the `zoneType` value is `SECONDARY`.


        :return: The external_masters of this CreateZoneDetails.
        :rtype: list[oci.dns.models.ExternalMaster]
        """
        return self._external_masters

    @external_masters.setter
    def external_masters(self, external_masters):
        """
        Sets the external_masters of this CreateZoneDetails.
        External master servers for the zone. `externalMasters` becomes a
        required parameter when the `zoneType` value is `SECONDARY`.


        :param external_masters: The external_masters of this CreateZoneDetails.
        :type: list[oci.dns.models.ExternalMaster]
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
