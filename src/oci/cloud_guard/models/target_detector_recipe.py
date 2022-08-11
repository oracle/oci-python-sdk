# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetDetectorRecipe(object):
    """
    Target Detector recipe
    """

    #: A constant which can be used with the owner property of a TargetDetectorRecipe.
    #: This constant has a value of "CUSTOMER"
    OWNER_CUSTOMER = "CUSTOMER"

    #: A constant which can be used with the owner property of a TargetDetectorRecipe.
    #: This constant has a value of "ORACLE"
    OWNER_ORACLE = "ORACLE"

    #: A constant which can be used with the detector property of a TargetDetectorRecipe.
    #: This constant has a value of "IAAS_ACTIVITY_DETECTOR"
    DETECTOR_IAAS_ACTIVITY_DETECTOR = "IAAS_ACTIVITY_DETECTOR"

    #: A constant which can be used with the detector property of a TargetDetectorRecipe.
    #: This constant has a value of "IAAS_CONFIGURATION_DETECTOR"
    DETECTOR_IAAS_CONFIGURATION_DETECTOR = "IAAS_CONFIGURATION_DETECTOR"

    #: A constant which can be used with the detector property of a TargetDetectorRecipe.
    #: This constant has a value of "IAAS_THREAT_DETECTOR"
    DETECTOR_IAAS_THREAT_DETECTOR = "IAAS_THREAT_DETECTOR"

    #: A constant which can be used with the detector property of a TargetDetectorRecipe.
    #: This constant has a value of "IAAS_LOG_INSIGHT_DETECTOR"
    DETECTOR_IAAS_LOG_INSIGHT_DETECTOR = "IAAS_LOG_INSIGHT_DETECTOR"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipe.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipe.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipe.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipe.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipe.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipe.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TargetDetectorRecipe.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetDetectorRecipe object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TargetDetectorRecipe.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this TargetDetectorRecipe.
        :type display_name: str

        :param description:
            The value to assign to the description property of this TargetDetectorRecipe.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TargetDetectorRecipe.
        :type compartment_id: str

        :param detector_recipe_id:
            The value to assign to the detector_recipe_id property of this TargetDetectorRecipe.
        :type detector_recipe_id: str

        :param owner:
            The value to assign to the owner property of this TargetDetectorRecipe.
            Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type owner: str

        :param detector:
            The value to assign to the detector property of this TargetDetectorRecipe.
            Allowed values for this property are: "IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR", "IAAS_THREAT_DETECTOR", "IAAS_LOG_INSIGHT_DETECTOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type detector: str

        :param detector_rules:
            The value to assign to the detector_rules property of this TargetDetectorRecipe.
        :type detector_rules: list[oci.cloud_guard.models.TargetDetectorRecipeDetectorRule]

        :param effective_detector_rules:
            The value to assign to the effective_detector_rules property of this TargetDetectorRecipe.
        :type effective_detector_rules: list[oci.cloud_guard.models.TargetDetectorRecipeDetectorRule]

        :param time_created:
            The value to assign to the time_created property of this TargetDetectorRecipe.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TargetDetectorRecipe.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TargetDetectorRecipe.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param source_data_retention:
            The value to assign to the source_data_retention property of this TargetDetectorRecipe.
        :type source_data_retention: int

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'detector_recipe_id': 'str',
            'owner': 'str',
            'detector': 'str',
            'detector_rules': 'list[TargetDetectorRecipeDetectorRule]',
            'effective_detector_rules': 'list[TargetDetectorRecipeDetectorRule]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'source_data_retention': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'detector_recipe_id': 'detectorRecipeId',
            'owner': 'owner',
            'detector': 'detector',
            'detector_rules': 'detectorRules',
            'effective_detector_rules': 'effectiveDetectorRules',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'source_data_retention': 'sourceDataRetention'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._detector_recipe_id = None
        self._owner = None
        self._detector = None
        self._detector_rules = None
        self._effective_detector_rules = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._source_data_retention = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TargetDetectorRecipe.
        Ocid for detector recipe


        :return: The id of this TargetDetectorRecipe.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TargetDetectorRecipe.
        Ocid for detector recipe


        :param id: The id of this TargetDetectorRecipe.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this TargetDetectorRecipe.
        Display name of detector recipe.


        :return: The display_name of this TargetDetectorRecipe.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TargetDetectorRecipe.
        Display name of detector recipe.


        :param display_name: The display_name of this TargetDetectorRecipe.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this TargetDetectorRecipe.
        Detector recipe description.


        :return: The description of this TargetDetectorRecipe.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TargetDetectorRecipe.
        Detector recipe description.


        :param description: The description of this TargetDetectorRecipe.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TargetDetectorRecipe.
        compartmentId of detector recipe


        :return: The compartment_id of this TargetDetectorRecipe.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TargetDetectorRecipe.
        compartmentId of detector recipe


        :param compartment_id: The compartment_id of this TargetDetectorRecipe.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def detector_recipe_id(self):
        """
        **[Required]** Gets the detector_recipe_id of this TargetDetectorRecipe.
        Unique identifier for Detector Recipe of which this is an extension


        :return: The detector_recipe_id of this TargetDetectorRecipe.
        :rtype: str
        """
        return self._detector_recipe_id

    @detector_recipe_id.setter
    def detector_recipe_id(self, detector_recipe_id):
        """
        Sets the detector_recipe_id of this TargetDetectorRecipe.
        Unique identifier for Detector Recipe of which this is an extension


        :param detector_recipe_id: The detector_recipe_id of this TargetDetectorRecipe.
        :type: str
        """
        self._detector_recipe_id = detector_recipe_id

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this TargetDetectorRecipe.
        Owner of detector recipe

        Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The owner of this TargetDetectorRecipe.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this TargetDetectorRecipe.
        Owner of detector recipe


        :param owner: The owner of this TargetDetectorRecipe.
        :type: str
        """
        allowed_values = ["CUSTOMER", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(owner, allowed_values):
            owner = 'UNKNOWN_ENUM_VALUE'
        self._owner = owner

    @property
    def detector(self):
        """
        **[Required]** Gets the detector of this TargetDetectorRecipe.
        Type of detector

        Allowed values for this property are: "IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR", "IAAS_THREAT_DETECTOR", "IAAS_LOG_INSIGHT_DETECTOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The detector of this TargetDetectorRecipe.
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """
        Sets the detector of this TargetDetectorRecipe.
        Type of detector


        :param detector: The detector of this TargetDetectorRecipe.
        :type: str
        """
        allowed_values = ["IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR", "IAAS_THREAT_DETECTOR", "IAAS_LOG_INSIGHT_DETECTOR"]
        if not value_allowed_none_or_none_sentinel(detector, allowed_values):
            detector = 'UNKNOWN_ENUM_VALUE'
        self._detector = detector

    @property
    def detector_rules(self):
        """
        Gets the detector_rules of this TargetDetectorRecipe.
        List of detector rules for the detector type for recipe - user input


        :return: The detector_rules of this TargetDetectorRecipe.
        :rtype: list[oci.cloud_guard.models.TargetDetectorRecipeDetectorRule]
        """
        return self._detector_rules

    @detector_rules.setter
    def detector_rules(self, detector_rules):
        """
        Sets the detector_rules of this TargetDetectorRecipe.
        List of detector rules for the detector type for recipe - user input


        :param detector_rules: The detector_rules of this TargetDetectorRecipe.
        :type: list[oci.cloud_guard.models.TargetDetectorRecipeDetectorRule]
        """
        self._detector_rules = detector_rules

    @property
    def effective_detector_rules(self):
        """
        Gets the effective_detector_rules of this TargetDetectorRecipe.
        List of effective detector rules for the detector type for recipe after applying defaults


        :return: The effective_detector_rules of this TargetDetectorRecipe.
        :rtype: list[oci.cloud_guard.models.TargetDetectorRecipeDetectorRule]
        """
        return self._effective_detector_rules

    @effective_detector_rules.setter
    def effective_detector_rules(self, effective_detector_rules):
        """
        Sets the effective_detector_rules of this TargetDetectorRecipe.
        List of effective detector rules for the detector type for recipe after applying defaults


        :param effective_detector_rules: The effective_detector_rules of this TargetDetectorRecipe.
        :type: list[oci.cloud_guard.models.TargetDetectorRecipeDetectorRule]
        """
        self._effective_detector_rules = effective_detector_rules

    @property
    def time_created(self):
        """
        Gets the time_created of this TargetDetectorRecipe.
        The date and time the target detector recipe was created. Format defined by RFC3339.


        :return: The time_created of this TargetDetectorRecipe.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TargetDetectorRecipe.
        The date and time the target detector recipe was created. Format defined by RFC3339.


        :param time_created: The time_created of this TargetDetectorRecipe.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this TargetDetectorRecipe.
        The date and time the target detector recipe was updated. Format defined by RFC3339.


        :return: The time_updated of this TargetDetectorRecipe.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TargetDetectorRecipe.
        The date and time the target detector recipe was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this TargetDetectorRecipe.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TargetDetectorRecipe.
        The current state of the resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TargetDetectorRecipe.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TargetDetectorRecipe.
        The current state of the resource.


        :param lifecycle_state: The lifecycle_state of this TargetDetectorRecipe.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def source_data_retention(self):
        """
        Gets the source_data_retention of this TargetDetectorRecipe.
        The number of days for which source data is retained


        :return: The source_data_retention of this TargetDetectorRecipe.
        :rtype: int
        """
        return self._source_data_retention

    @source_data_retention.setter
    def source_data_retention(self, source_data_retention):
        """
        Sets the source_data_retention of this TargetDetectorRecipe.
        The number of days for which source data is retained


        :param source_data_retention: The source_data_retention of this TargetDetectorRecipe.
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
