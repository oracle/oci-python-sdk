# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_zone_base_details import CreateZoneBaseDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMigratedDynectZoneDetails(CreateZoneBaseDetails):
    """
    The body for migrating a zone from DynECT.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMigratedDynectZoneDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.dns.models.CreateMigratedDynectZoneDetails.migration_source` attribute
        of this class is ``DYNECT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param migration_source:
            The value to assign to the migration_source property of this CreateMigratedDynectZoneDetails.
            Allowed values for this property are: "NONE", "DYNECT"
        :type migration_source: str

        :param name:
            The value to assign to the name property of this CreateMigratedDynectZoneDetails.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMigratedDynectZoneDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMigratedDynectZoneDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMigratedDynectZoneDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param dynect_migration_details:
            The value to assign to the dynect_migration_details property of this CreateMigratedDynectZoneDetails.
        :type dynect_migration_details: oci.dns.models.DynectMigrationDetails

        """
        self.swagger_types = {
            'migration_source': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'dynect_migration_details': 'DynectMigrationDetails'
        }

        self.attribute_map = {
            'migration_source': 'migrationSource',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'dynect_migration_details': 'dynectMigrationDetails'
        }

        self._migration_source = None
        self._name = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._dynect_migration_details = None
        self._migration_source = 'DYNECT'

    @property
    def dynect_migration_details(self):
        """
        Gets the dynect_migration_details of this CreateMigratedDynectZoneDetails.

        :return: The dynect_migration_details of this CreateMigratedDynectZoneDetails.
        :rtype: oci.dns.models.DynectMigrationDetails
        """
        return self._dynect_migration_details

    @dynect_migration_details.setter
    def dynect_migration_details(self, dynect_migration_details):
        """
        Sets the dynect_migration_details of this CreateMigratedDynectZoneDetails.

        :param dynect_migration_details: The dynect_migration_details of this CreateMigratedDynectZoneDetails.
        :type: oci.dns.models.DynectMigrationDetails
        """
        self._dynect_migration_details = dynect_migration_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
