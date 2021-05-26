# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_db_home_base import CreateDbHomeBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbHomeWithDbSystemIdFromDatabaseDetails(CreateDbHomeBase):
    """
    Note that a valid `dbSystemId` value must be supplied for the `CreateDbHomeWithDbSystemIdFromDatabase` API operation to successfully complete.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbHomeWithDbSystemIdFromDatabaseDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateDbHomeWithDbSystemIdFromDatabaseDetails.source` attribute
        of this class is ``DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        :type display_name: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        :type kms_key_id: str

        :param kms_key_version_id:
            The value to assign to the kms_key_version_id property of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        :type kms_key_version_id: str

        :param database_software_image_id:
            The value to assign to the database_software_image_id property of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        :type database_software_image_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param source:
            The value to assign to the source property of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
            Allowed values for this property are: "NONE", "DB_BACKUP", "DATABASE", "VM_CLUSTER_BACKUP", "VM_CLUSTER_NEW"
        :type source: str

        :param is_desupported_version:
            The value to assign to the is_desupported_version property of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        :type is_desupported_version: bool

        :param db_system_id:
            The value to assign to the db_system_id property of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        :type db_system_id: str

        :param database:
            The value to assign to the database property of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        :type database: oci.database.models.CreateDatabaseFromAnotherDatabaseDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'kms_key_id': 'str',
            'kms_key_version_id': 'str',
            'database_software_image_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'source': 'str',
            'is_desupported_version': 'bool',
            'db_system_id': 'str',
            'database': 'CreateDatabaseFromAnotherDatabaseDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'kms_key_id': 'kmsKeyId',
            'kms_key_version_id': 'kmsKeyVersionId',
            'database_software_image_id': 'databaseSoftwareImageId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'source': 'source',
            'is_desupported_version': 'isDesupportedVersion',
            'db_system_id': 'dbSystemId',
            'database': 'database'
        }

        self._display_name = None
        self._kms_key_id = None
        self._kms_key_version_id = None
        self._database_software_image_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._source = None
        self._is_desupported_version = None
        self._db_system_id = None
        self._database = None
        self._source = 'DATABASE'

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        The `OCID`__ of the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_system_id of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        The `OCID`__ of the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_system_id: The db_system_id of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def database(self):
        """
        **[Required]** Gets the database of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.

        :return: The database of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        :rtype: oci.database.models.CreateDatabaseFromAnotherDatabaseDetails
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.

        :param database: The database of this CreateDbHomeWithDbSystemIdFromDatabaseDetails.
        :type: oci.database.models.CreateDatabaseFromAnotherDatabaseDetails
        """
        self._database = database

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
