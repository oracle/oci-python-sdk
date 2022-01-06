# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTargetDetails(object):
    """
    The information to be updated.
    """

    #: A constant which can be used with the lifecycle_state property of a UpdateTargetDetails.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a UpdateTargetDetails.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a UpdateTargetDetails.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a UpdateTargetDetails.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a UpdateTargetDetails.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a UpdateTargetDetails.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a UpdateTargetDetails.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTargetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateTargetDetails.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this UpdateTargetDetails.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param target_detector_recipes:
            The value to assign to the target_detector_recipes property of this UpdateTargetDetails.
        :type target_detector_recipes: list[oci.cloud_guard.models.UpdateTargetDetectorRecipe]

        :param target_responder_recipes:
            The value to assign to the target_responder_recipes property of this UpdateTargetDetails.
        :type target_responder_recipes: list[oci.cloud_guard.models.UpdateTargetResponderRecipe]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateTargetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateTargetDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'lifecycle_state': 'str',
            'target_detector_recipes': 'list[UpdateTargetDetectorRecipe]',
            'target_responder_recipes': 'list[UpdateTargetResponderRecipe]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'target_detector_recipes': 'targetDetectorRecipes',
            'target_responder_recipes': 'targetResponderRecipes',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._lifecycle_state = None
        self._target_detector_recipes = None
        self._target_responder_recipes = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateTargetDetails.
        DetectorTemplate Identifier


        :return: The display_name of this UpdateTargetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateTargetDetails.
        DetectorTemplate Identifier


        :param display_name: The display_name of this UpdateTargetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this UpdateTargetDetails.
        The current state of the Target.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"


        :return: The lifecycle_state of this UpdateTargetDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this UpdateTargetDetails.
        The current state of the Target.


        :param lifecycle_state: The lifecycle_state of this UpdateTargetDetails.
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
    def target_detector_recipes(self):
        """
        Gets the target_detector_recipes of this UpdateTargetDetails.
        The details of target detector recipes to be updated.


        :return: The target_detector_recipes of this UpdateTargetDetails.
        :rtype: list[oci.cloud_guard.models.UpdateTargetDetectorRecipe]
        """
        return self._target_detector_recipes

    @target_detector_recipes.setter
    def target_detector_recipes(self, target_detector_recipes):
        """
        Sets the target_detector_recipes of this UpdateTargetDetails.
        The details of target detector recipes to be updated.


        :param target_detector_recipes: The target_detector_recipes of this UpdateTargetDetails.
        :type: list[oci.cloud_guard.models.UpdateTargetDetectorRecipe]
        """
        self._target_detector_recipes = target_detector_recipes

    @property
    def target_responder_recipes(self):
        """
        Gets the target_responder_recipes of this UpdateTargetDetails.
        The details of target responder recipes to be updated.


        :return: The target_responder_recipes of this UpdateTargetDetails.
        :rtype: list[oci.cloud_guard.models.UpdateTargetResponderRecipe]
        """
        return self._target_responder_recipes

    @target_responder_recipes.setter
    def target_responder_recipes(self, target_responder_recipes):
        """
        Sets the target_responder_recipes of this UpdateTargetDetails.
        The details of target responder recipes to be updated.


        :param target_responder_recipes: The target_responder_recipes of this UpdateTargetDetails.
        :type: list[oci.cloud_guard.models.UpdateTargetResponderRecipe]
        """
        self._target_responder_recipes = target_responder_recipes

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateTargetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateTargetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateTargetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateTargetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateTargetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateTargetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateTargetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateTargetDetails.
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
