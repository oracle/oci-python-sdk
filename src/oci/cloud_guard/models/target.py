# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Target(object):
    """
    Description of Target.
    """

    #: A constant which can be used with the target_resource_type property of a Target.
    #: This constant has a value of "COMPARTMENT"
    TARGET_RESOURCE_TYPE_COMPARTMENT = "COMPARTMENT"

    #: A constant which can be used with the target_resource_type property of a Target.
    #: This constant has a value of "ERPCLOUD"
    TARGET_RESOURCE_TYPE_ERPCLOUD = "ERPCLOUD"

    #: A constant which can be used with the target_resource_type property of a Target.
    #: This constant has a value of "HCMCLOUD"
    TARGET_RESOURCE_TYPE_HCMCLOUD = "HCMCLOUD"

    #: A constant which can be used with the target_resource_type property of a Target.
    #: This constant has a value of "SECURITY_ZONE"
    TARGET_RESOURCE_TYPE_SECURITY_ZONE = "SECURITY_ZONE"

    #: A constant which can be used with the lifecycle_state property of a Target.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Target.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Target.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Target.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Target.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Target.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Target.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Target object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Target.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Target.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Target.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this Target.
        :type description: str

        :param target_resource_type:
            The value to assign to the target_resource_type property of this Target.
            Allowed values for this property are: "COMPARTMENT", "ERPCLOUD", "HCMCLOUD", "SECURITY_ZONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type target_resource_type: str

        :param target_resource_id:
            The value to assign to the target_resource_id property of this Target.
        :type target_resource_id: str

        :param recipe_count:
            The value to assign to the recipe_count property of this Target.
        :type recipe_count: int

        :param target_detector_recipes:
            The value to assign to the target_detector_recipes property of this Target.
        :type target_detector_recipes: list[oci.cloud_guard.models.TargetDetectorRecipe]

        :param target_responder_recipes:
            The value to assign to the target_responder_recipes property of this Target.
        :type target_responder_recipes: list[oci.cloud_guard.models.TargetResponderRecipe]

        :param target_details:
            The value to assign to the target_details property of this Target.
        :type target_details: oci.cloud_guard.models.TargetDetails

        :param inherited_by_compartments:
            The value to assign to the inherited_by_compartments property of this Target.
        :type inherited_by_compartments: list[str]

        :param time_created:
            The value to assign to the time_created property of this Target.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Target.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Target.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecyle_details:
            The value to assign to the lifecyle_details property of this Target.
        :type lifecyle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Target.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Target.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Target.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'target_resource_type': 'str',
            'target_resource_id': 'str',
            'recipe_count': 'int',
            'target_detector_recipes': 'list[TargetDetectorRecipe]',
            'target_responder_recipes': 'list[TargetResponderRecipe]',
            'target_details': 'TargetDetails',
            'inherited_by_compartments': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecyle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'target_resource_type': 'targetResourceType',
            'target_resource_id': 'targetResourceId',
            'recipe_count': 'recipeCount',
            'target_detector_recipes': 'targetDetectorRecipes',
            'target_responder_recipes': 'targetResponderRecipes',
            'target_details': 'targetDetails',
            'inherited_by_compartments': 'inheritedByCompartments',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecyle_details': 'lifecyleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._target_resource_type = None
        self._target_resource_id = None
        self._recipe_count = None
        self._target_detector_recipes = None
        self._target_responder_recipes = None
        self._target_details = None
        self._inherited_by_compartments = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecyle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Target.
        Unique identifier that is immutable on creation.


        :return: The id of this Target.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Target.
        Unique identifier that is immutable on creation.


        :param id: The id of this Target.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this Target.
        Target display name, can be renamed.


        :return: The display_name of this Target.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Target.
        Target display name, can be renamed.


        :param display_name: The display_name of this Target.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Target.
        Compartment Identifier where the resource is created


        :return: The compartment_id of this Target.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Target.
        Compartment Identifier where the resource is created


        :param compartment_id: The compartment_id of this Target.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this Target.
        The target description.


        :return: The description of this Target.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Target.
        The target description.


        :param description: The description of this Target.
        :type: str
        """
        self._description = description

    @property
    def target_resource_type(self):
        """
        **[Required]** Gets the target_resource_type of this Target.
        possible type of targets

        Allowed values for this property are: "COMPARTMENT", "ERPCLOUD", "HCMCLOUD", "SECURITY_ZONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The target_resource_type of this Target.
        :rtype: str
        """
        return self._target_resource_type

    @target_resource_type.setter
    def target_resource_type(self, target_resource_type):
        """
        Sets the target_resource_type of this Target.
        possible type of targets


        :param target_resource_type: The target_resource_type of this Target.
        :type: str
        """
        allowed_values = ["COMPARTMENT", "ERPCLOUD", "HCMCLOUD", "SECURITY_ZONE"]
        if not value_allowed_none_or_none_sentinel(target_resource_type, allowed_values):
            target_resource_type = 'UNKNOWN_ENUM_VALUE'
        self._target_resource_type = target_resource_type

    @property
    def target_resource_id(self):
        """
        **[Required]** Gets the target_resource_id of this Target.
        Resource ID which the target uses to monitor


        :return: The target_resource_id of this Target.
        :rtype: str
        """
        return self._target_resource_id

    @target_resource_id.setter
    def target_resource_id(self, target_resource_id):
        """
        Sets the target_resource_id of this Target.
        Resource ID which the target uses to monitor


        :param target_resource_id: The target_resource_id of this Target.
        :type: str
        """
        self._target_resource_id = target_resource_id

    @property
    def recipe_count(self):
        """
        **[Required]** Gets the recipe_count of this Target.
        Total number of recipes attached to target


        :return: The recipe_count of this Target.
        :rtype: int
        """
        return self._recipe_count

    @recipe_count.setter
    def recipe_count(self, recipe_count):
        """
        Sets the recipe_count of this Target.
        Total number of recipes attached to target


        :param recipe_count: The recipe_count of this Target.
        :type: int
        """
        self._recipe_count = recipe_count

    @property
    def target_detector_recipes(self):
        """
        Gets the target_detector_recipes of this Target.
        List of detector recipes associated with target


        :return: The target_detector_recipes of this Target.
        :rtype: list[oci.cloud_guard.models.TargetDetectorRecipe]
        """
        return self._target_detector_recipes

    @target_detector_recipes.setter
    def target_detector_recipes(self, target_detector_recipes):
        """
        Sets the target_detector_recipes of this Target.
        List of detector recipes associated with target


        :param target_detector_recipes: The target_detector_recipes of this Target.
        :type: list[oci.cloud_guard.models.TargetDetectorRecipe]
        """
        self._target_detector_recipes = target_detector_recipes

    @property
    def target_responder_recipes(self):
        """
        Gets the target_responder_recipes of this Target.
        List of responder recipes associated with target


        :return: The target_responder_recipes of this Target.
        :rtype: list[oci.cloud_guard.models.TargetResponderRecipe]
        """
        return self._target_responder_recipes

    @target_responder_recipes.setter
    def target_responder_recipes(self, target_responder_recipes):
        """
        Sets the target_responder_recipes of this Target.
        List of responder recipes associated with target


        :param target_responder_recipes: The target_responder_recipes of this Target.
        :type: list[oci.cloud_guard.models.TargetResponderRecipe]
        """
        self._target_responder_recipes = target_responder_recipes

    @property
    def target_details(self):
        """
        Gets the target_details of this Target.

        :return: The target_details of this Target.
        :rtype: oci.cloud_guard.models.TargetDetails
        """
        return self._target_details

    @target_details.setter
    def target_details(self, target_details):
        """
        Sets the target_details of this Target.

        :param target_details: The target_details of this Target.
        :type: oci.cloud_guard.models.TargetDetails
        """
        self._target_details = target_details

    @property
    def inherited_by_compartments(self):
        """
        Gets the inherited_by_compartments of this Target.
        List of inherited compartments


        :return: The inherited_by_compartments of this Target.
        :rtype: list[str]
        """
        return self._inherited_by_compartments

    @inherited_by_compartments.setter
    def inherited_by_compartments(self, inherited_by_compartments):
        """
        Sets the inherited_by_compartments of this Target.
        List of inherited compartments


        :param inherited_by_compartments: The inherited_by_compartments of this Target.
        :type: list[str]
        """
        self._inherited_by_compartments = inherited_by_compartments

    @property
    def time_created(self):
        """
        Gets the time_created of this Target.
        The date and time the target was created. Format defined by RFC3339.


        :return: The time_created of this Target.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Target.
        The date and time the target was created. Format defined by RFC3339.


        :param time_created: The time_created of this Target.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Target.
        The date and time the target was updated. Format defined by RFC3339.


        :return: The time_updated of this Target.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Target.
        The date and time the target was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this Target.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Target.
        The current state of the Target.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Target.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Target.
        The current state of the Target.


        :param lifecycle_state: The lifecycle_state of this Target.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecyle_details(self):
        """
        Gets the lifecyle_details of this Target.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecyle_details of this Target.
        :rtype: str
        """
        return self._lifecyle_details

    @lifecyle_details.setter
    def lifecyle_details(self, lifecyle_details):
        """
        Sets the lifecyle_details of this Target.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecyle_details: The lifecyle_details of this Target.
        :type: str
        """
        self._lifecyle_details = lifecyle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Target.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this Target.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Target.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this Target.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Target.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Target.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Target.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Target.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Target.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this Target.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Target.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this Target.
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
