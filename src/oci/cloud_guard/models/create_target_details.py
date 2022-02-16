# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTargetDetails(object):
    """
    The information about new Target.
    """

    #: A constant which can be used with the target_resource_type property of a CreateTargetDetails.
    #: This constant has a value of "COMPARTMENT"
    TARGET_RESOURCE_TYPE_COMPARTMENT = "COMPARTMENT"

    #: A constant which can be used with the target_resource_type property of a CreateTargetDetails.
    #: This constant has a value of "ERPCLOUD"
    TARGET_RESOURCE_TYPE_ERPCLOUD = "ERPCLOUD"

    #: A constant which can be used with the target_resource_type property of a CreateTargetDetails.
    #: This constant has a value of "HCMCLOUD"
    TARGET_RESOURCE_TYPE_HCMCLOUD = "HCMCLOUD"

    #: A constant which can be used with the lifecycle_state property of a CreateTargetDetails.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a CreateTargetDetails.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CreateTargetDetails.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CreateTargetDetails.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CreateTargetDetails.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CreateTargetDetails.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a CreateTargetDetails.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTargetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateTargetDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateTargetDetails.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this CreateTargetDetails.
        :type description: str

        :param target_resource_type:
            The value to assign to the target_resource_type property of this CreateTargetDetails.
            Allowed values for this property are: "COMPARTMENT", "ERPCLOUD", "HCMCLOUD"
        :type target_resource_type: str

        :param target_resource_id:
            The value to assign to the target_resource_id property of this CreateTargetDetails.
        :type target_resource_id: str

        :param target_detector_recipes:
            The value to assign to the target_detector_recipes property of this CreateTargetDetails.
        :type target_detector_recipes: list[oci.cloud_guard.models.CreateTargetDetectorRecipeDetails]

        :param target_responder_recipes:
            The value to assign to the target_responder_recipes property of this CreateTargetDetails.
        :type target_responder_recipes: list[oci.cloud_guard.models.CreateTargetResponderRecipeDetails]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CreateTargetDetails.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateTargetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateTargetDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'target_resource_type': 'str',
            'target_resource_id': 'str',
            'target_detector_recipes': 'list[CreateTargetDetectorRecipeDetails]',
            'target_responder_recipes': 'list[CreateTargetResponderRecipeDetails]',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'target_resource_type': 'targetResourceType',
            'target_resource_id': 'targetResourceId',
            'target_detector_recipes': 'targetDetectorRecipes',
            'target_responder_recipes': 'targetResponderRecipes',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._target_resource_type = None
        self._target_resource_id = None
        self._target_detector_recipes = None
        self._target_responder_recipes = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateTargetDetails.
        DetectorTemplate identifier.

        Avoid entering confidential information.


        :return: The display_name of this CreateTargetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateTargetDetails.
        DetectorTemplate identifier.

        Avoid entering confidential information.


        :param display_name: The display_name of this CreateTargetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateTargetDetails.
        Compartment Identifier where the resource is created


        :return: The compartment_id of this CreateTargetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateTargetDetails.
        Compartment Identifier where the resource is created


        :param compartment_id: The compartment_id of this CreateTargetDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this CreateTargetDetails.
        The target description.

        Avoid entering confidential information.


        :return: The description of this CreateTargetDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateTargetDetails.
        The target description.

        Avoid entering confidential information.


        :param description: The description of this CreateTargetDetails.
        :type: str
        """
        self._description = description

    @property
    def target_resource_type(self):
        """
        **[Required]** Gets the target_resource_type of this CreateTargetDetails.
        possible type of targets(compartment/HCMCloud/ERPCloud)

        Allowed values for this property are: "COMPARTMENT", "ERPCLOUD", "HCMCLOUD"


        :return: The target_resource_type of this CreateTargetDetails.
        :rtype: str
        """
        return self._target_resource_type

    @target_resource_type.setter
    def target_resource_type(self, target_resource_type):
        """
        Sets the target_resource_type of this CreateTargetDetails.
        possible type of targets(compartment/HCMCloud/ERPCloud)


        :param target_resource_type: The target_resource_type of this CreateTargetDetails.
        :type: str
        """
        allowed_values = ["COMPARTMENT", "ERPCLOUD", "HCMCLOUD"]
        if not value_allowed_none_or_none_sentinel(target_resource_type, allowed_values):
            raise ValueError(
                "Invalid value for `target_resource_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._target_resource_type = target_resource_type

    @property
    def target_resource_id(self):
        """
        **[Required]** Gets the target_resource_id of this CreateTargetDetails.
        Resource ID which the target uses to monitor


        :return: The target_resource_id of this CreateTargetDetails.
        :rtype: str
        """
        return self._target_resource_id

    @target_resource_id.setter
    def target_resource_id(self, target_resource_id):
        """
        Sets the target_resource_id of this CreateTargetDetails.
        Resource ID which the target uses to monitor


        :param target_resource_id: The target_resource_id of this CreateTargetDetails.
        :type: str
        """
        self._target_resource_id = target_resource_id

    @property
    def target_detector_recipes(self):
        """
        Gets the target_detector_recipes of this CreateTargetDetails.
        List of detector recipes to associate with target


        :return: The target_detector_recipes of this CreateTargetDetails.
        :rtype: list[oci.cloud_guard.models.CreateTargetDetectorRecipeDetails]
        """
        return self._target_detector_recipes

    @target_detector_recipes.setter
    def target_detector_recipes(self, target_detector_recipes):
        """
        Sets the target_detector_recipes of this CreateTargetDetails.
        List of detector recipes to associate with target


        :param target_detector_recipes: The target_detector_recipes of this CreateTargetDetails.
        :type: list[oci.cloud_guard.models.CreateTargetDetectorRecipeDetails]
        """
        self._target_detector_recipes = target_detector_recipes

    @property
    def target_responder_recipes(self):
        """
        Gets the target_responder_recipes of this CreateTargetDetails.
        List of responder recipes to associate with target


        :return: The target_responder_recipes of this CreateTargetDetails.
        :rtype: list[oci.cloud_guard.models.CreateTargetResponderRecipeDetails]
        """
        return self._target_responder_recipes

    @target_responder_recipes.setter
    def target_responder_recipes(self, target_responder_recipes):
        """
        Sets the target_responder_recipes of this CreateTargetDetails.
        List of responder recipes to associate with target


        :param target_responder_recipes: The target_responder_recipes of this CreateTargetDetails.
        :type: list[oci.cloud_guard.models.CreateTargetResponderRecipeDetails]
        """
        self._target_responder_recipes = target_responder_recipes

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CreateTargetDetails.
        The current state of the DetectorRule.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"


        :return: The lifecycle_state of this CreateTargetDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CreateTargetDetails.
        The current state of the DetectorRule.


        :param lifecycle_state: The lifecycle_state of this CreateTargetDetails.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateTargetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this CreateTargetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateTargetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this CreateTargetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateTargetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateTargetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateTargetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateTargetDetails.
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
