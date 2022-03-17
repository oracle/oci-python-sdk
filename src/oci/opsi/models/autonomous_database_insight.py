# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_insight import DatabaseInsight
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseInsight(DatabaseInsight):
    """
    Database insight resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseInsight object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.AutonomousDatabaseInsight.entity_source` attribute
        of this class is ``AUTONOMOUS_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this AutonomousDatabaseInsight.
            Allowed values for this property are: "AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"
        :type entity_source: str

        :param id:
            The value to assign to the id property of this AutonomousDatabaseInsight.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AutonomousDatabaseInsight.
        :type compartment_id: str

        :param status:
            The value to assign to the status property of this AutonomousDatabaseInsight.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED"
        :type status: str

        :param database_type:
            The value to assign to the database_type property of this AutonomousDatabaseInsight.
        :type database_type: str

        :param database_version:
            The value to assign to the database_version property of this AutonomousDatabaseInsight.
        :type database_version: str

        :param processor_count:
            The value to assign to the processor_count property of this AutonomousDatabaseInsight.
        :type processor_count: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AutonomousDatabaseInsight.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AutonomousDatabaseInsight.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AutonomousDatabaseInsight.
        :type system_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this AutonomousDatabaseInsight.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AutonomousDatabaseInsight.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousDatabaseInsight.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AutonomousDatabaseInsight.
        :type lifecycle_details: str

        :param database_connection_status_details:
            The value to assign to the database_connection_status_details property of this AutonomousDatabaseInsight.
        :type database_connection_status_details: str

        :param database_id:
            The value to assign to the database_id property of this AutonomousDatabaseInsight.
        :type database_id: str

        :param database_name:
            The value to assign to the database_name property of this AutonomousDatabaseInsight.
        :type database_name: str

        :param database_display_name:
            The value to assign to the database_display_name property of this AutonomousDatabaseInsight.
        :type database_display_name: str

        :param database_resource_type:
            The value to assign to the database_resource_type property of this AutonomousDatabaseInsight.
        :type database_resource_type: str

        :param db_additional_details:
            The value to assign to the db_additional_details property of this AutonomousDatabaseInsight.
        :type db_additional_details: object

        """
        self.swagger_types = {
            'entity_source': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'status': 'str',
            'database_type': 'str',
            'database_version': 'str',
            'processor_count': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'database_connection_status_details': 'str',
            'database_id': 'str',
            'database_name': 'str',
            'database_display_name': 'str',
            'database_resource_type': 'str',
            'db_additional_details': 'object'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'status': 'status',
            'database_type': 'databaseType',
            'database_version': 'databaseVersion',
            'processor_count': 'processorCount',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'database_connection_status_details': 'databaseConnectionStatusDetails',
            'database_id': 'databaseId',
            'database_name': 'databaseName',
            'database_display_name': 'databaseDisplayName',
            'database_resource_type': 'databaseResourceType',
            'db_additional_details': 'dbAdditionalDetails'
        }

        self._entity_source = None
        self._id = None
        self._compartment_id = None
        self._status = None
        self._database_type = None
        self._database_version = None
        self._processor_count = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._database_connection_status_details = None
        self._database_id = None
        self._database_name = None
        self._database_display_name = None
        self._database_resource_type = None
        self._db_additional_details = None
        self._entity_source = 'AUTONOMOUS_DATABASE'

    @property
    def database_id(self):
        """
        **[Required]** Gets the database_id of this AutonomousDatabaseInsight.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The database_id of this AutonomousDatabaseInsight.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this AutonomousDatabaseInsight.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this AutonomousDatabaseInsight.
        :type: str
        """
        self._database_id = database_id

    @property
    def database_name(self):
        """
        **[Required]** Gets the database_name of this AutonomousDatabaseInsight.
        Name of database


        :return: The database_name of this AutonomousDatabaseInsight.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this AutonomousDatabaseInsight.
        Name of database


        :param database_name: The database_name of this AutonomousDatabaseInsight.
        :type: str
        """
        self._database_name = database_name

    @property
    def database_display_name(self):
        """
        Gets the database_display_name of this AutonomousDatabaseInsight.
        Display name of database


        :return: The database_display_name of this AutonomousDatabaseInsight.
        :rtype: str
        """
        return self._database_display_name

    @database_display_name.setter
    def database_display_name(self, database_display_name):
        """
        Sets the database_display_name of this AutonomousDatabaseInsight.
        Display name of database


        :param database_display_name: The database_display_name of this AutonomousDatabaseInsight.
        :type: str
        """
        self._database_display_name = database_display_name

    @property
    def database_resource_type(self):
        """
        **[Required]** Gets the database_resource_type of this AutonomousDatabaseInsight.
        OCI database resource type


        :return: The database_resource_type of this AutonomousDatabaseInsight.
        :rtype: str
        """
        return self._database_resource_type

    @database_resource_type.setter
    def database_resource_type(self, database_resource_type):
        """
        Sets the database_resource_type of this AutonomousDatabaseInsight.
        OCI database resource type


        :param database_resource_type: The database_resource_type of this AutonomousDatabaseInsight.
        :type: str
        """
        self._database_resource_type = database_resource_type

    @property
    def db_additional_details(self):
        """
        Gets the db_additional_details of this AutonomousDatabaseInsight.
        Additional details of a database in JSON format. For autonomous databases, this is the AutonomousDatabase object serialized as a JSON string as defined in https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/. For EM, pass in null or an empty string. Note that this string needs to be escaped when specified in the curl command.


        :return: The db_additional_details of this AutonomousDatabaseInsight.
        :rtype: object
        """
        return self._db_additional_details

    @db_additional_details.setter
    def db_additional_details(self, db_additional_details):
        """
        Sets the db_additional_details of this AutonomousDatabaseInsight.
        Additional details of a database in JSON format. For autonomous databases, this is the AutonomousDatabase object serialized as a JSON string as defined in https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/. For EM, pass in null or an empty string. Note that this string needs to be escaped when specified in the curl command.


        :param db_additional_details: The db_additional_details of this AutonomousDatabaseInsight.
        :type: object
        """
        self._db_additional_details = db_additional_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
