# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetDetectorRecipeSummary(object):
    """
    Summary of DetectorRecipe
    """

    #: A constant which can be used with the owner property of a TargetDetectorRecipeSummary.
    #: This constant has a value of "CUSTOMER"
    OWNER_CUSTOMER = "CUSTOMER"

    #: A constant which can be used with the owner property of a TargetDetectorRecipeSummary.
    #: This constant has a value of "ORACLE"
    OWNER_ORACLE = "ORACLE"

    #: A constant which can be used with the detector property of a TargetDetectorRecipeSummary.
    #: This constant has a value of "IAAS_ACTIVITY_DETECTOR"
    DETECTOR_IAAS_ACTIVITY_DETECTOR = "IAAS_ACTIVITY_DETECTOR"

    #: A constant which can be used with the detector property of a TargetDetectorRecipeSummary.
    #: This constant has a value of "IAAS_CONFIGURATION_DETECTOR"
    DETECTOR_IAAS_CONFIGURATION_DETECTOR = "IAAS_CONFIGURATION_DETECTOR"

    #: A constant which can be used with the detector property of a TargetDetectorRecipeSummary.
    #: This constant has a value of "IAAS_THREAT_DETECTOR"
    DETECTOR_IAAS_THREAT_DETECTOR = "IAAS_THREAT_DETECTOR"

    #: A constant which can be used with the detector property of a TargetDetectorRecipeSummary.
    #: This constant has a value of "IAAS_LOG_INSIGHT_DETECTOR"
    DETECTOR_IAAS_LOG_INSIGHT_DETECTOR = "IAAS_LOG_INSIGHT_DETECTOR"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipeSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetDetectorRecipeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TargetDetectorRecipeSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TargetDetectorRecipeSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this TargetDetectorRecipeSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this TargetDetectorRecipeSummary.
        :type description: str

        :param owner:
            The value to assign to the owner property of this TargetDetectorRecipeSummary.
            Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type owner: str

        :param detector_recipe_id:
            The value to assign to the detector_recipe_id property of this TargetDetectorRecipeSummary.
        :type detector_recipe_id: str

        :param detector:
            The value to assign to the detector property of this TargetDetectorRecipeSummary.
            Allowed values for this property are: "IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR", "IAAS_THREAT_DETECTOR", "IAAS_LOG_INSIGHT_DETECTOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type detector: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TargetDetectorRecipeSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this TargetDetectorRecipeSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TargetDetectorRecipeSummary.
        :type time_updated: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this TargetDetectorRecipeSummary.
        :type lifecycle_details: str

        :param source_data_retention:
            The value to assign to the source_data_retention property of this TargetDetectorRecipeSummary.
        :type source_data_retention: int

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'owner': 'str',
            'detector_recipe_id': 'str',
            'detector': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_details': 'str',
            'source_data_retention': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'owner': 'owner',
            'detector_recipe_id': 'detectorRecipeId',
            'detector': 'detector',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_details': 'lifecycleDetails',
            'source_data_retention': 'sourceDataRetention'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._owner = None
        self._detector_recipe_id = None
        self._detector = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_details = None
        self._source_data_retention = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TargetDetectorRecipeSummary.
        Unique identifier that is immutable on creation


        :return: The id of this TargetDetectorRecipeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TargetDetectorRecipeSummary.
        Unique identifier that is immutable on creation


        :param id: The id of this TargetDetectorRecipeSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TargetDetectorRecipeSummary.
        Compartment Identifier


        :return: The compartment_id of this TargetDetectorRecipeSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TargetDetectorRecipeSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this TargetDetectorRecipeSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this TargetDetectorRecipeSummary.
        DetectorRecipe Identifier Name


        :return: The display_name of this TargetDetectorRecipeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TargetDetectorRecipeSummary.
        DetectorRecipe Identifier Name


        :param display_name: The display_name of this TargetDetectorRecipeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this TargetDetectorRecipeSummary.
        DetectorRecipe Description


        :return: The description of this TargetDetectorRecipeSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TargetDetectorRecipeSummary.
        DetectorRecipe Description


        :param description: The description of this TargetDetectorRecipeSummary.
        :type: str
        """
        self._description = description

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this TargetDetectorRecipeSummary.
        Owner of DetectorRecipe

        Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The owner of this TargetDetectorRecipeSummary.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this TargetDetectorRecipeSummary.
        Owner of DetectorRecipe


        :param owner: The owner of this TargetDetectorRecipeSummary.
        :type: str
        """
        allowed_values = ["CUSTOMER", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(owner, allowed_values):
            owner = 'UNKNOWN_ENUM_VALUE'
        self._owner = owner

    @property
    def detector_recipe_id(self):
        """
        **[Required]** Gets the detector_recipe_id of this TargetDetectorRecipeSummary.
        Unique identifier for Detector Recipe of which this is an extension


        :return: The detector_recipe_id of this TargetDetectorRecipeSummary.
        :rtype: str
        """
        return self._detector_recipe_id

    @detector_recipe_id.setter
    def detector_recipe_id(self, detector_recipe_id):
        """
        Sets the detector_recipe_id of this TargetDetectorRecipeSummary.
        Unique identifier for Detector Recipe of which this is an extension


        :param detector_recipe_id: The detector_recipe_id of this TargetDetectorRecipeSummary.
        :type: str
        """
        self._detector_recipe_id = detector_recipe_id

    @property
    def detector(self):
        """
        Gets the detector of this TargetDetectorRecipeSummary.
        Type of detector

        Allowed values for this property are: "IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR", "IAAS_THREAT_DETECTOR", "IAAS_LOG_INSIGHT_DETECTOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The detector of this TargetDetectorRecipeSummary.
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """
        Sets the detector of this TargetDetectorRecipeSummary.
        Type of detector


        :param detector: The detector of this TargetDetectorRecipeSummary.
        :type: str
        """
        allowed_values = ["IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR", "IAAS_THREAT_DETECTOR", "IAAS_LOG_INSIGHT_DETECTOR"]
        if not value_allowed_none_or_none_sentinel(detector, allowed_values):
            detector = 'UNKNOWN_ENUM_VALUE'
        self._detector = detector

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TargetDetectorRecipeSummary.
        The current state of the resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TargetDetectorRecipeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TargetDetectorRecipeSummary.
        The current state of the resource.


        :param lifecycle_state: The lifecycle_state of this TargetDetectorRecipeSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this TargetDetectorRecipeSummary.
        The date and time the target detector recipe was created. Format defined by RFC3339.


        :return: The time_created of this TargetDetectorRecipeSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TargetDetectorRecipeSummary.
        The date and time the target detector recipe was created. Format defined by RFC3339.


        :param time_created: The time_created of this TargetDetectorRecipeSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this TargetDetectorRecipeSummary.
        The date and time the target detector recipe was updated. Format defined by RFC3339.


        :return: The time_updated of this TargetDetectorRecipeSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TargetDetectorRecipeSummary.
        The date and time the target detector recipe was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this TargetDetectorRecipeSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this TargetDetectorRecipeSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this TargetDetectorRecipeSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this TargetDetectorRecipeSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this TargetDetectorRecipeSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def source_data_retention(self):
        """
        Gets the source_data_retention of this TargetDetectorRecipeSummary.
        The number of days for which source data is retained


        :return: The source_data_retention of this TargetDetectorRecipeSummary.
        :rtype: int
        """
        return self._source_data_retention

    @source_data_retention.setter
    def source_data_retention(self, source_data_retention):
        """
        Sets the source_data_retention of this TargetDetectorRecipeSummary.
        The number of days for which source data is retained


        :param source_data_retention: The source_data_retention of this TargetDetectorRecipeSummary.
        :type: int
        """
        self._source_data_retention = source_data_retention

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
