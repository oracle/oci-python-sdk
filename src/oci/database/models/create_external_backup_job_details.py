# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateExternalBackupJobDetails(object):
    """
    CreateExternalBackupJobDetails model.
    """

    #: A constant which can be used with the database_mode property of a CreateExternalBackupJobDetails.
    #: This constant has a value of "SI"
    DATABASE_MODE_SI = "SI"

    #: A constant which can be used with the database_mode property of a CreateExternalBackupJobDetails.
    #: This constant has a value of "RAC"
    DATABASE_MODE_RAC = "RAC"

    #: A constant which can be used with the database_edition property of a CreateExternalBackupJobDetails.
    #: This constant has a value of "STANDARD_EDITION"
    DATABASE_EDITION_STANDARD_EDITION = "STANDARD_EDITION"

    #: A constant which can be used with the database_edition property of a CreateExternalBackupJobDetails.
    #: This constant has a value of "ENTERPRISE_EDITION"
    DATABASE_EDITION_ENTERPRISE_EDITION = "ENTERPRISE_EDITION"

    #: A constant which can be used with the database_edition property of a CreateExternalBackupJobDetails.
    #: This constant has a value of "ENTERPRISE_EDITION_HIGH_PERFORMANCE"
    DATABASE_EDITION_ENTERPRISE_EDITION_HIGH_PERFORMANCE = "ENTERPRISE_EDITION_HIGH_PERFORMANCE"

    #: A constant which can be used with the database_edition property of a CreateExternalBackupJobDetails.
    #: This constant has a value of "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"
    DATABASE_EDITION_ENTERPRISE_EDITION_EXTREME_PERFORMANCE = "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateExternalBackupJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateExternalBackupJobDetails.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateExternalBackupJobDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateExternalBackupJobDetails.
        :type display_name: str

        :param db_version:
            The value to assign to the db_version property of this CreateExternalBackupJobDetails.
        :type db_version: str

        :param db_name:
            The value to assign to the db_name property of this CreateExternalBackupJobDetails.
        :type db_name: str

        :param db_unique_name:
            The value to assign to the db_unique_name property of this CreateExternalBackupJobDetails.
        :type db_unique_name: str

        :param pdb_name:
            The value to assign to the pdb_name property of this CreateExternalBackupJobDetails.
        :type pdb_name: str

        :param external_database_identifier:
            The value to assign to the external_database_identifier property of this CreateExternalBackupJobDetails.
        :type external_database_identifier: int

        :param character_set:
            The value to assign to the character_set property of this CreateExternalBackupJobDetails.
        :type character_set: str

        :param ncharacter_set:
            The value to assign to the ncharacter_set property of this CreateExternalBackupJobDetails.
        :type ncharacter_set: str

        :param database_mode:
            The value to assign to the database_mode property of this CreateExternalBackupJobDetails.
            Allowed values for this property are: "SI", "RAC"
        :type database_mode: str

        :param database_edition:
            The value to assign to the database_edition property of this CreateExternalBackupJobDetails.
            Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"
        :type database_edition: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'db_version': 'str',
            'db_name': 'str',
            'db_unique_name': 'str',
            'pdb_name': 'str',
            'external_database_identifier': 'int',
            'character_set': 'str',
            'ncharacter_set': 'str',
            'database_mode': 'str',
            'database_edition': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'db_version': 'dbVersion',
            'db_name': 'dbName',
            'db_unique_name': 'dbUniqueName',
            'pdb_name': 'pdbName',
            'external_database_identifier': 'externalDatabaseIdentifier',
            'character_set': 'characterSet',
            'ncharacter_set': 'ncharacterSet',
            'database_mode': 'databaseMode',
            'database_edition': 'databaseEdition'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._db_version = None
        self._db_name = None
        self._db_unique_name = None
        self._pdb_name = None
        self._external_database_identifier = None
        self._character_set = None
        self._ncharacter_set = None
        self._database_mode = None
        self._database_edition = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateExternalBackupJobDetails.
        The targeted availability domain for the backup.


        :return: The availability_domain of this CreateExternalBackupJobDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateExternalBackupJobDetails.
        The targeted availability domain for the backup.


        :param availability_domain: The availability_domain of this CreateExternalBackupJobDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateExternalBackupJobDetails.
        The `OCID`__ of the compartment where this backup should be created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateExternalBackupJobDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateExternalBackupJobDetails.
        The `OCID`__ of the compartment where this backup should be created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateExternalBackupJobDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateExternalBackupJobDetails.
        A user-friendly name for the backup. This name does not have to be unique.


        :return: The display_name of this CreateExternalBackupJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateExternalBackupJobDetails.
        A user-friendly name for the backup. This name does not have to be unique.


        :param display_name: The display_name of this CreateExternalBackupJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def db_version(self):
        """
        **[Required]** Gets the db_version of this CreateExternalBackupJobDetails.
        A valid Oracle Database version.


        :return: The db_version of this CreateExternalBackupJobDetails.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this CreateExternalBackupJobDetails.
        A valid Oracle Database version.


        :param db_version: The db_version of this CreateExternalBackupJobDetails.
        :type: str
        """
        self._db_version = db_version

    @property
    def db_name(self):
        """
        **[Required]** Gets the db_name of this CreateExternalBackupJobDetails.
        The name of the database from which the backup is being taken.


        :return: The db_name of this CreateExternalBackupJobDetails.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this CreateExternalBackupJobDetails.
        The name of the database from which the backup is being taken.


        :param db_name: The db_name of this CreateExternalBackupJobDetails.
        :type: str
        """
        self._db_name = db_name

    @property
    def db_unique_name(self):
        """
        Gets the db_unique_name of this CreateExternalBackupJobDetails.
        The `DB_UNIQUE_NAME` of the Oracle Database being backed up.


        :return: The db_unique_name of this CreateExternalBackupJobDetails.
        :rtype: str
        """
        return self._db_unique_name

    @db_unique_name.setter
    def db_unique_name(self, db_unique_name):
        """
        Sets the db_unique_name of this CreateExternalBackupJobDetails.
        The `DB_UNIQUE_NAME` of the Oracle Database being backed up.


        :param db_unique_name: The db_unique_name of this CreateExternalBackupJobDetails.
        :type: str
        """
        self._db_unique_name = db_unique_name

    @property
    def pdb_name(self):
        """
        Gets the pdb_name of this CreateExternalBackupJobDetails.
        The pluggable database name.


        :return: The pdb_name of this CreateExternalBackupJobDetails.
        :rtype: str
        """
        return self._pdb_name

    @pdb_name.setter
    def pdb_name(self, pdb_name):
        """
        Sets the pdb_name of this CreateExternalBackupJobDetails.
        The pluggable database name.


        :param pdb_name: The pdb_name of this CreateExternalBackupJobDetails.
        :type: str
        """
        self._pdb_name = pdb_name

    @property
    def external_database_identifier(self):
        """
        **[Required]** Gets the external_database_identifier of this CreateExternalBackupJobDetails.
        The `DBID` of the Oracle Database being backed up.


        :return: The external_database_identifier of this CreateExternalBackupJobDetails.
        :rtype: int
        """
        return self._external_database_identifier

    @external_database_identifier.setter
    def external_database_identifier(self, external_database_identifier):
        """
        Sets the external_database_identifier of this CreateExternalBackupJobDetails.
        The `DBID` of the Oracle Database being backed up.


        :param external_database_identifier: The external_database_identifier of this CreateExternalBackupJobDetails.
        :type: int
        """
        self._external_database_identifier = external_database_identifier

    @property
    def character_set(self):
        """
        **[Required]** Gets the character_set of this CreateExternalBackupJobDetails.
        The character set for the database.


        :return: The character_set of this CreateExternalBackupJobDetails.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """
        Sets the character_set of this CreateExternalBackupJobDetails.
        The character set for the database.


        :param character_set: The character_set of this CreateExternalBackupJobDetails.
        :type: str
        """
        self._character_set = character_set

    @property
    def ncharacter_set(self):
        """
        **[Required]** Gets the ncharacter_set of this CreateExternalBackupJobDetails.
        The national character set for the database.


        :return: The ncharacter_set of this CreateExternalBackupJobDetails.
        :rtype: str
        """
        return self._ncharacter_set

    @ncharacter_set.setter
    def ncharacter_set(self, ncharacter_set):
        """
        Sets the ncharacter_set of this CreateExternalBackupJobDetails.
        The national character set for the database.


        :param ncharacter_set: The ncharacter_set of this CreateExternalBackupJobDetails.
        :type: str
        """
        self._ncharacter_set = ncharacter_set

    @property
    def database_mode(self):
        """
        **[Required]** Gets the database_mode of this CreateExternalBackupJobDetails.
        The mode (single instance or RAC) of the database being backed up.

        Allowed values for this property are: "SI", "RAC"


        :return: The database_mode of this CreateExternalBackupJobDetails.
        :rtype: str
        """
        return self._database_mode

    @database_mode.setter
    def database_mode(self, database_mode):
        """
        Sets the database_mode of this CreateExternalBackupJobDetails.
        The mode (single instance or RAC) of the database being backed up.


        :param database_mode: The database_mode of this CreateExternalBackupJobDetails.
        :type: str
        """
        allowed_values = ["SI", "RAC"]
        if not value_allowed_none_or_none_sentinel(database_mode, allowed_values):
            raise ValueError(
                "Invalid value for `database_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._database_mode = database_mode

    @property
    def database_edition(self):
        """
        **[Required]** Gets the database_edition of this CreateExternalBackupJobDetails.
        The Oracle Database edition to use for creating a database from this standalone backup.
        Note that 2-node RAC DB systems require Enterprise Edition - Extreme Performance.

        Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"


        :return: The database_edition of this CreateExternalBackupJobDetails.
        :rtype: str
        """
        return self._database_edition

    @database_edition.setter
    def database_edition(self, database_edition):
        """
        Sets the database_edition of this CreateExternalBackupJobDetails.
        The Oracle Database edition to use for creating a database from this standalone backup.
        Note that 2-node RAC DB systems require Enterprise Edition - Extreme Performance.


        :param database_edition: The database_edition of this CreateExternalBackupJobDetails.
        :type: str
        """
        allowed_values = ["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"]
        if not value_allowed_none_or_none_sentinel(database_edition, allowed_values):
            raise ValueError(
                "Invalid value for `database_edition`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._database_edition = database_edition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
