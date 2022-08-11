# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetectorRecipeSummary(object):
    """
    Summary of Detector recipe
    """

    #: A constant which can be used with the owner property of a DetectorRecipeSummary.
    #: This constant has a value of "CUSTOMER"
    OWNER_CUSTOMER = "CUSTOMER"

    #: A constant which can be used with the owner property of a DetectorRecipeSummary.
    #: This constant has a value of "ORACLE"
    OWNER_ORACLE = "ORACLE"

    #: A constant which can be used with the detector property of a DetectorRecipeSummary.
    #: This constant has a value of "IAAS_ACTIVITY_DETECTOR"
    DETECTOR_IAAS_ACTIVITY_DETECTOR = "IAAS_ACTIVITY_DETECTOR"

    #: A constant which can be used with the detector property of a DetectorRecipeSummary.
    #: This constant has a value of "IAAS_CONFIGURATION_DETECTOR"
    DETECTOR_IAAS_CONFIGURATION_DETECTOR = "IAAS_CONFIGURATION_DETECTOR"

    #: A constant which can be used with the detector property of a DetectorRecipeSummary.
    #: This constant has a value of "IAAS_THREAT_DETECTOR"
    DETECTOR_IAAS_THREAT_DETECTOR = "IAAS_THREAT_DETECTOR"

    #: A constant which can be used with the detector property of a DetectorRecipeSummary.
    #: This constant has a value of "IAAS_LOG_INSIGHT_DETECTOR"
    DETECTOR_IAAS_LOG_INSIGHT_DETECTOR = "IAAS_LOG_INSIGHT_DETECTOR"

    #: A constant which can be used with the lifecycle_state property of a DetectorRecipeSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DetectorRecipeSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DetectorRecipeSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DetectorRecipeSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DetectorRecipeSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DetectorRecipeSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DetectorRecipeSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DetectorRecipeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DetectorRecipeSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DetectorRecipeSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DetectorRecipeSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DetectorRecipeSummary.
        :type compartment_id: str

        :param source_detector_recipe_id:
            The value to assign to the source_detector_recipe_id property of this DetectorRecipeSummary.
        :type source_detector_recipe_id: str

        :param owner:
            The value to assign to the owner property of this DetectorRecipeSummary.
            Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type owner: str

        :param detector:
            The value to assign to the detector property of this DetectorRecipeSummary.
            Allowed values for this property are: "IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR", "IAAS_THREAT_DETECTOR", "IAAS_LOG_INSIGHT_DETECTOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type detector: str

        :param detector_rules:
            The value to assign to the detector_rules property of this DetectorRecipeSummary.
        :type detector_rules: list[oci.cloud_guard.models.DetectorRecipeDetectorRule]

        :param time_created:
            The value to assign to the time_created property of this DetectorRecipeSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DetectorRecipeSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DetectorRecipeSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param source_data_retention:
            The value to assign to the source_data_retention property of this DetectorRecipeSummary.
        :type source_data_retention: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DetectorRecipeSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DetectorRecipeSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DetectorRecipeSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'source_detector_recipe_id': 'str',
            'owner': 'str',
            'detector': 'str',
            'detector_rules': 'list[DetectorRecipeDetectorRule]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'source_data_retention': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'source_detector_recipe_id': 'sourceDetectorRecipeId',
            'owner': 'owner',
            'detector': 'detector',
            'detector_rules': 'detectorRules',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'source_data_retention': 'sourceDataRetention',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._source_detector_recipe_id = None
        self._owner = None
        self._detector = None
        self._detector_rules = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._source_data_retention = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DetectorRecipeSummary.
        Ocid for detector recipe


        :return: The id of this DetectorRecipeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DetectorRecipeSummary.
        Ocid for detector recipe


        :param id: The id of this DetectorRecipeSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DetectorRecipeSummary.
        DisplayName of detector recipe


        :return: The display_name of this DetectorRecipeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DetectorRecipeSummary.
        DisplayName of detector recipe


        :param display_name: The display_name of this DetectorRecipeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DetectorRecipeSummary.
        Detector recipe description


        :return: The description of this DetectorRecipeSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DetectorRecipeSummary.
        Detector recipe description


        :param description: The description of this DetectorRecipeSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DetectorRecipeSummary.
        compartmentId of detector recipe


        :return: The compartment_id of this DetectorRecipeSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DetectorRecipeSummary.
        compartmentId of detector recipe


        :param compartment_id: The compartment_id of this DetectorRecipeSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def source_detector_recipe_id(self):
        """
        Gets the source_detector_recipe_id of this DetectorRecipeSummary.
        Recipe Ocid of the Source Recipe to be cloned


        :return: The source_detector_recipe_id of this DetectorRecipeSummary.
        :rtype: str
        """
        return self._source_detector_recipe_id

    @source_detector_recipe_id.setter
    def source_detector_recipe_id(self, source_detector_recipe_id):
        """
        Sets the source_detector_recipe_id of this DetectorRecipeSummary.
        Recipe Ocid of the Source Recipe to be cloned


        :param source_detector_recipe_id: The source_detector_recipe_id of this DetectorRecipeSummary.
        :type: str
        """
        self._source_detector_recipe_id = source_detector_recipe_id

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this DetectorRecipeSummary.
        Owner of detector recipe

        Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The owner of this DetectorRecipeSummary.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this DetectorRecipeSummary.
        Owner of detector recipe


        :param owner: The owner of this DetectorRecipeSummary.
        :type: str
        """
        allowed_values = ["CUSTOMER", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(owner, allowed_values):
            owner = 'UNKNOWN_ENUM_VALUE'
        self._owner = owner

    @property
    def detector(self):
        """
        **[Required]** Gets the detector of this DetectorRecipeSummary.
        Type of detector

        Allowed values for this property are: "IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR", "IAAS_THREAT_DETECTOR", "IAAS_LOG_INSIGHT_DETECTOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The detector of this DetectorRecipeSummary.
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """
        Sets the detector of this DetectorRecipeSummary.
        Type of detector


        :param detector: The detector of this DetectorRecipeSummary.
        :type: str
        """
        allowed_values = ["IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR", "IAAS_THREAT_DETECTOR", "IAAS_LOG_INSIGHT_DETECTOR"]
        if not value_allowed_none_or_none_sentinel(detector, allowed_values):
            detector = 'UNKNOWN_ENUM_VALUE'
        self._detector = detector

    @property
    def detector_rules(self):
        """
        Gets the detector_rules of this DetectorRecipeSummary.
        List of detetor rules for the detector type


        :return: The detector_rules of this DetectorRecipeSummary.
        :rtype: list[oci.cloud_guard.models.DetectorRecipeDetectorRule]
        """
        return self._detector_rules

    @detector_rules.setter
    def detector_rules(self, detector_rules):
        """
        Sets the detector_rules of this DetectorRecipeSummary.
        List of detetor rules for the detector type


        :param detector_rules: The detector_rules of this DetectorRecipeSummary.
        :type: list[oci.cloud_guard.models.DetectorRecipeDetectorRule]
        """
        self._detector_rules = detector_rules

    @property
    def time_created(self):
        """
        Gets the time_created of this DetectorRecipeSummary.
        The date and time the detector recipe was created. Format defined by RFC3339.


        :return: The time_created of this DetectorRecipeSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DetectorRecipeSummary.
        The date and time the detector recipe was created. Format defined by RFC3339.


        :param time_created: The time_created of this DetectorRecipeSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DetectorRecipeSummary.
        The date and time the detector recipe was updated. Format defined by RFC3339.


        :return: The time_updated of this DetectorRecipeSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DetectorRecipeSummary.
        The date and time the detector recipe was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this DetectorRecipeSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DetectorRecipeSummary.
        The current state of the resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DetectorRecipeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DetectorRecipeSummary.
        The current state of the resource.


        :param lifecycle_state: The lifecycle_state of this DetectorRecipeSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def source_data_retention(self):
        """
        Gets the source_data_retention of this DetectorRecipeSummary.
        The number of days for which source data is retained


        :return: The source_data_retention of this DetectorRecipeSummary.
        :rtype: int
        """
        return self._source_data_retention

    @source_data_retention.setter
    def source_data_retention(self, source_data_retention):
        """
        Sets the source_data_retention of this DetectorRecipeSummary.
        The number of days for which source data is retained


        :param source_data_retention: The source_data_retention of this DetectorRecipeSummary.
        :type: int
        """
        self._source_data_retention = source_data_retention

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DetectorRecipeSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this DetectorRecipeSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DetectorRecipeSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this DetectorRecipeSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DetectorRecipeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DetectorRecipeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DetectorRecipeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DetectorRecipeSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DetectorRecipeSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this DetectorRecipeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DetectorRecipeSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this DetectorRecipeSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
