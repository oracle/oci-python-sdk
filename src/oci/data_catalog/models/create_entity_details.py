# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEntityDetails(object):
    """
    Properties used in data entity create operations.
    """

    #: A constant which can be used with the harvest_status property of a CreateEntityDetails.
    #: This constant has a value of "COMPLETE"
    HARVEST_STATUS_COMPLETE = "COMPLETE"

    #: A constant which can be used with the harvest_status property of a CreateEntityDetails.
    #: This constant has a value of "ERROR"
    HARVEST_STATUS_ERROR = "ERROR"

    #: A constant which can be used with the harvest_status property of a CreateEntityDetails.
    #: This constant has a value of "IN_PROGRESS"
    HARVEST_STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the harvest_status property of a CreateEntityDetails.
    #: This constant has a value of "DEFERRED"
    HARVEST_STATUS_DEFERRED = "DEFERRED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEntityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateEntityDetails.
        :type display_name: str

        :param business_name:
            The value to assign to the business_name property of this CreateEntityDetails.
        :type business_name: str

        :param description:
            The value to assign to the description property of this CreateEntityDetails.
        :type description: str

        :param time_external:
            The value to assign to the time_external property of this CreateEntityDetails.
        :type time_external: datetime

        :param is_logical:
            The value to assign to the is_logical property of this CreateEntityDetails.
        :type is_logical: bool

        :param is_partition:
            The value to assign to the is_partition property of this CreateEntityDetails.
        :type is_partition: bool

        :param folder_key:
            The value to assign to the folder_key property of this CreateEntityDetails.
        :type folder_key: str

        :param pattern_key:
            The value to assign to the pattern_key property of this CreateEntityDetails.
        :type pattern_key: str

        :param realized_expression:
            The value to assign to the realized_expression property of this CreateEntityDetails.
        :type realized_expression: str

        :param harvest_status:
            The value to assign to the harvest_status property of this CreateEntityDetails.
            Allowed values for this property are: "COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED"
        :type harvest_status: str

        :param last_job_key:
            The value to assign to the last_job_key property of this CreateEntityDetails.
        :type last_job_key: str

        :param custom_property_members:
            The value to assign to the custom_property_members property of this CreateEntityDetails.
        :type custom_property_members: list[oci.data_catalog.models.CustomPropertySetUsage]

        :param properties:
            The value to assign to the properties property of this CreateEntityDetails.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'display_name': 'str',
            'business_name': 'str',
            'description': 'str',
            'time_external': 'datetime',
            'is_logical': 'bool',
            'is_partition': 'bool',
            'folder_key': 'str',
            'pattern_key': 'str',
            'realized_expression': 'str',
            'harvest_status': 'str',
            'last_job_key': 'str',
            'custom_property_members': 'list[CustomPropertySetUsage]',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'business_name': 'businessName',
            'description': 'description',
            'time_external': 'timeExternal',
            'is_logical': 'isLogical',
            'is_partition': 'isPartition',
            'folder_key': 'folderKey',
            'pattern_key': 'patternKey',
            'realized_expression': 'realizedExpression',
            'harvest_status': 'harvestStatus',
            'last_job_key': 'lastJobKey',
            'custom_property_members': 'customPropertyMembers',
            'properties': 'properties'
        }

        self._display_name = None
        self._business_name = None
        self._description = None
        self._time_external = None
        self._is_logical = None
        self._is_partition = None
        self._folder_key = None
        self._pattern_key = None
        self._realized_expression = None
        self._harvest_status = None
        self._last_job_key = None
        self._custom_property_members = None
        self._properties = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateEntityDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateEntityDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateEntityDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateEntityDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def business_name(self):
        """
        Gets the business_name of this CreateEntityDetails.
        Optional user friendly business name of the data entity. If set, this supplements the harvested display name of the object.


        :return: The business_name of this CreateEntityDetails.
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """
        Sets the business_name of this CreateEntityDetails.
        Optional user friendly business name of the data entity. If set, this supplements the harvested display name of the object.


        :param business_name: The business_name of this CreateEntityDetails.
        :type: str
        """
        self._business_name = business_name

    @property
    def description(self):
        """
        Gets the description of this CreateEntityDetails.
        Detailed description of a data entity.


        :return: The description of this CreateEntityDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateEntityDetails.
        Detailed description of a data entity.


        :param description: The description of this CreateEntityDetails.
        :type: str
        """
        self._description = description

    @property
    def time_external(self):
        """
        **[Required]** Gets the time_external of this CreateEntityDetails.
        Last modified timestamp of the object in the external system.


        :return: The time_external of this CreateEntityDetails.
        :rtype: datetime
        """
        return self._time_external

    @time_external.setter
    def time_external(self, time_external):
        """
        Sets the time_external of this CreateEntityDetails.
        Last modified timestamp of the object in the external system.


        :param time_external: The time_external of this CreateEntityDetails.
        :type: datetime
        """
        self._time_external = time_external

    @property
    def is_logical(self):
        """
        Gets the is_logical of this CreateEntityDetails.
        Property to indicate if the object is a physical materialized object or virtual. For example, View.


        :return: The is_logical of this CreateEntityDetails.
        :rtype: bool
        """
        return self._is_logical

    @is_logical.setter
    def is_logical(self, is_logical):
        """
        Sets the is_logical of this CreateEntityDetails.
        Property to indicate if the object is a physical materialized object or virtual. For example, View.


        :param is_logical: The is_logical of this CreateEntityDetails.
        :type: bool
        """
        self._is_logical = is_logical

    @property
    def is_partition(self):
        """
        Gets the is_partition of this CreateEntityDetails.
        Property to indicate if the object is a sub object of a parent physical object.


        :return: The is_partition of this CreateEntityDetails.
        :rtype: bool
        """
        return self._is_partition

    @is_partition.setter
    def is_partition(self, is_partition):
        """
        Sets the is_partition of this CreateEntityDetails.
        Property to indicate if the object is a sub object of a parent physical object.


        :param is_partition: The is_partition of this CreateEntityDetails.
        :type: bool
        """
        self._is_partition = is_partition

    @property
    def folder_key(self):
        """
        Gets the folder_key of this CreateEntityDetails.
        Key of the associated folder.


        :return: The folder_key of this CreateEntityDetails.
        :rtype: str
        """
        return self._folder_key

    @folder_key.setter
    def folder_key(self, folder_key):
        """
        Sets the folder_key of this CreateEntityDetails.
        Key of the associated folder.


        :param folder_key: The folder_key of this CreateEntityDetails.
        :type: str
        """
        self._folder_key = folder_key

    @property
    def pattern_key(self):
        """
        Gets the pattern_key of this CreateEntityDetails.
        Key of the associated pattern if this is a logical entity.


        :return: The pattern_key of this CreateEntityDetails.
        :rtype: str
        """
        return self._pattern_key

    @pattern_key.setter
    def pattern_key(self, pattern_key):
        """
        Sets the pattern_key of this CreateEntityDetails.
        Key of the associated pattern if this is a logical entity.


        :param pattern_key: The pattern_key of this CreateEntityDetails.
        :type: str
        """
        self._pattern_key = pattern_key

    @property
    def realized_expression(self):
        """
        Gets the realized_expression of this CreateEntityDetails.
        The expression realized after resolving qualifiers . Used in deriving this logical entity


        :return: The realized_expression of this CreateEntityDetails.
        :rtype: str
        """
        return self._realized_expression

    @realized_expression.setter
    def realized_expression(self, realized_expression):
        """
        Sets the realized_expression of this CreateEntityDetails.
        The expression realized after resolving qualifiers . Used in deriving this logical entity


        :param realized_expression: The realized_expression of this CreateEntityDetails.
        :type: str
        """
        self._realized_expression = realized_expression

    @property
    def harvest_status(self):
        """
        Gets the harvest_status of this CreateEntityDetails.
        Status of the object as updated by the harvest process. When an entity object is created , it's harvest status
        will indicate if the entity's metadata has been fully harvested or not. The harvest process can perform
        shallow harvesting to allow users to browse the metadata and can on-demand deep harvest on any object
        This requires a harvest status indicator for catalog objects.

        Allowed values for this property are: "COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED"


        :return: The harvest_status of this CreateEntityDetails.
        :rtype: str
        """
        return self._harvest_status

    @harvest_status.setter
    def harvest_status(self, harvest_status):
        """
        Sets the harvest_status of this CreateEntityDetails.
        Status of the object as updated by the harvest process. When an entity object is created , it's harvest status
        will indicate if the entity's metadata has been fully harvested or not. The harvest process can perform
        shallow harvesting to allow users to browse the metadata and can on-demand deep harvest on any object
        This requires a harvest status indicator for catalog objects.


        :param harvest_status: The harvest_status of this CreateEntityDetails.
        :type: str
        """
        allowed_values = ["COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED"]
        if not value_allowed_none_or_none_sentinel(harvest_status, allowed_values):
            raise ValueError(
                "Invalid value for `harvest_status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._harvest_status = harvest_status

    @property
    def last_job_key(self):
        """
        Gets the last_job_key of this CreateEntityDetails.
        Key of the last harvest process to update this object.


        :return: The last_job_key of this CreateEntityDetails.
        :rtype: str
        """
        return self._last_job_key

    @last_job_key.setter
    def last_job_key(self, last_job_key):
        """
        Sets the last_job_key of this CreateEntityDetails.
        Key of the last harvest process to update this object.


        :param last_job_key: The last_job_key of this CreateEntityDetails.
        :type: str
        """
        self._last_job_key = last_job_key

    @property
    def custom_property_members(self):
        """
        Gets the custom_property_members of this CreateEntityDetails.
        The list of customized properties along with the values for this object


        :return: The custom_property_members of this CreateEntityDetails.
        :rtype: list[oci.data_catalog.models.CustomPropertySetUsage]
        """
        return self._custom_property_members

    @custom_property_members.setter
    def custom_property_members(self, custom_property_members):
        """
        Sets the custom_property_members of this CreateEntityDetails.
        The list of customized properties along with the values for this object


        :param custom_property_members: The custom_property_members of this CreateEntityDetails.
        :type: list[oci.data_catalog.models.CustomPropertySetUsage]
        """
        self._custom_property_members = custom_property_members

    @property
    def properties(self):
        """
        Gets the properties of this CreateEntityDetails.
        A map of maps that contains the properties which are specific to the entity type. Each entity type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        entities have required properties within the \"default\" category. To determine the set of required and
        optional properties for an entity type, a query can be done on '/types?type=dataEntity' that returns a
        collection of all entity types. The appropriate entity type, which includes definitions of all of
        it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :return: The properties of this CreateEntityDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CreateEntityDetails.
        A map of maps that contains the properties which are specific to the entity type. Each entity type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        entities have required properties within the \"default\" category. To determine the set of required and
        optional properties for an entity type, a query can be done on '/types?type=dataEntity' that returns a
        collection of all entity types. The appropriate entity type, which includes definitions of all of
        it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :param properties: The properties of this CreateEntityDetails.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
