# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetDatabaseSummary(object):
    """
    Summary of a Data Safe target database.
    """

    #: A constant which can be used with the infrastructure_type property of a TargetDatabaseSummary.
    #: This constant has a value of "ORACLE_CLOUD"
    INFRASTRUCTURE_TYPE_ORACLE_CLOUD = "ORACLE_CLOUD"

    #: A constant which can be used with the infrastructure_type property of a TargetDatabaseSummary.
    #: This constant has a value of "CLOUD_AT_CUSTOMER"
    INFRASTRUCTURE_TYPE_CLOUD_AT_CUSTOMER = "CLOUD_AT_CUSTOMER"

    #: A constant which can be used with the infrastructure_type property of a TargetDatabaseSummary.
    #: This constant has a value of "ON_PREMISES"
    INFRASTRUCTURE_TYPE_ON_PREMISES = "ON_PREMISES"

    #: A constant which can be used with the infrastructure_type property of a TargetDatabaseSummary.
    #: This constant has a value of "NON_ORACLE_CLOUD"
    INFRASTRUCTURE_TYPE_NON_ORACLE_CLOUD = "NON_ORACLE_CLOUD"

    #: A constant which can be used with the database_type property of a TargetDatabaseSummary.
    #: This constant has a value of "DATABASE_CLOUD_SERVICE"
    DATABASE_TYPE_DATABASE_CLOUD_SERVICE = "DATABASE_CLOUD_SERVICE"

    #: A constant which can be used with the database_type property of a TargetDatabaseSummary.
    #: This constant has a value of "AUTONOMOUS_DATABASE"
    DATABASE_TYPE_AUTONOMOUS_DATABASE = "AUTONOMOUS_DATABASE"

    #: A constant which can be used with the database_type property of a TargetDatabaseSummary.
    #: This constant has a value of "INSTALLED_DATABASE"
    DATABASE_TYPE_INSTALLED_DATABASE = "INSTALLED_DATABASE"

    #: A constant which can be used with the lifecycle_state property of a TargetDatabaseSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a TargetDatabaseSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a TargetDatabaseSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetDatabaseSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetDatabaseSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a TargetDatabaseSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TargetDatabaseSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a TargetDatabaseSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetDatabaseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this TargetDatabaseSummary.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this TargetDatabaseSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this TargetDatabaseSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this TargetDatabaseSummary.
        :type description: str

        :param infrastructure_type:
            The value to assign to the infrastructure_type property of this TargetDatabaseSummary.
            Allowed values for this property are: "ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type infrastructure_type: str

        :param database_type:
            The value to assign to the database_type property of this TargetDatabaseSummary.
            Allowed values for this property are: "DATABASE_CLOUD_SERVICE", "AUTONOMOUS_DATABASE", "INSTALLED_DATABASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TargetDatabaseSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this TargetDatabaseSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this TargetDatabaseSummary.
        :type time_created: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TargetDatabaseSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TargetDatabaseSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'infrastructure_type': 'str',
            'database_type': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'infrastructure_type': 'infrastructureType',
            'database_type': 'databaseType',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._id = None
        self._display_name = None
        self._description = None
        self._infrastructure_type = None
        self._database_type = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TargetDatabaseSummary.
        The OCID of the compartment that contains the Data Safe target database.


        :return: The compartment_id of this TargetDatabaseSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TargetDatabaseSummary.
        The OCID of the compartment that contains the Data Safe target database.


        :param compartment_id: The compartment_id of this TargetDatabaseSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TargetDatabaseSummary.
        The OCID of the Data Safe target database.


        :return: The id of this TargetDatabaseSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TargetDatabaseSummary.
        The OCID of the Data Safe target database.


        :param id: The id of this TargetDatabaseSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this TargetDatabaseSummary.
        The display name of the target database in Data Safe.


        :return: The display_name of this TargetDatabaseSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TargetDatabaseSummary.
        The display name of the target database in Data Safe.


        :param display_name: The display_name of this TargetDatabaseSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this TargetDatabaseSummary.
        The description of the target database in Data Safe.


        :return: The description of this TargetDatabaseSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TargetDatabaseSummary.
        The description of the target database in Data Safe.


        :param description: The description of this TargetDatabaseSummary.
        :type: str
        """
        self._description = description

    @property
    def infrastructure_type(self):
        """
        **[Required]** Gets the infrastructure_type of this TargetDatabaseSummary.
        The infrastructure type the database is running on.

        Allowed values for this property are: "ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The infrastructure_type of this TargetDatabaseSummary.
        :rtype: str
        """
        return self._infrastructure_type

    @infrastructure_type.setter
    def infrastructure_type(self, infrastructure_type):
        """
        Sets the infrastructure_type of this TargetDatabaseSummary.
        The infrastructure type the database is running on.


        :param infrastructure_type: The infrastructure_type of this TargetDatabaseSummary.
        :type: str
        """
        allowed_values = ["ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD"]
        if not value_allowed_none_or_none_sentinel(infrastructure_type, allowed_values):
            infrastructure_type = 'UNKNOWN_ENUM_VALUE'
        self._infrastructure_type = infrastructure_type

    @property
    def database_type(self):
        """
        **[Required]** Gets the database_type of this TargetDatabaseSummary.
        The database type.

        Allowed values for this property are: "DATABASE_CLOUD_SERVICE", "AUTONOMOUS_DATABASE", "INSTALLED_DATABASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this TargetDatabaseSummary.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this TargetDatabaseSummary.
        The database type.


        :param database_type: The database_type of this TargetDatabaseSummary.
        :type: str
        """
        allowed_values = ["DATABASE_CLOUD_SERVICE", "AUTONOMOUS_DATABASE", "INSTALLED_DATABASE"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this TargetDatabaseSummary.
        The current state of the target database in Data Safe.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TargetDatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TargetDatabaseSummary.
        The current state of the target database in Data Safe.


        :param lifecycle_state: The lifecycle_state of this TargetDatabaseSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this TargetDatabaseSummary.
        Details about the current state of the target database in Data Safe.


        :return: The lifecycle_details of this TargetDatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this TargetDatabaseSummary.
        Details about the current state of the target database in Data Safe.


        :param lifecycle_details: The lifecycle_details of this TargetDatabaseSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this TargetDatabaseSummary.
        The date and time the database was registered in Data Safe and created as a target database in Data Safe.


        :return: The time_created of this TargetDatabaseSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TargetDatabaseSummary.
        The date and time the database was registered in Data Safe and created as a target database in Data Safe.


        :param time_created: The time_created of this TargetDatabaseSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this TargetDatabaseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this TargetDatabaseSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this TargetDatabaseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this TargetDatabaseSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this TargetDatabaseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this TargetDatabaseSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this TargetDatabaseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this TargetDatabaseSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
