# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateWebAppAccelerationDetails(object):
    """
    The information to be updated for WebAppAcceleration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateWebAppAccelerationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateWebAppAccelerationDetails.
        :type display_name: str

        :param web_app_acceleration_policy_id:
            The value to assign to the web_app_acceleration_policy_id property of this UpdateWebAppAccelerationDetails.
        :type web_app_acceleration_policy_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateWebAppAccelerationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateWebAppAccelerationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this UpdateWebAppAccelerationDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'web_app_acceleration_policy_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'web_app_acceleration_policy_id': 'webAppAccelerationPolicyId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._display_name = None
        self._web_app_acceleration_policy_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateWebAppAccelerationDetails.
        WebAppAcceleration display name, can be renamed.


        :return: The display_name of this UpdateWebAppAccelerationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateWebAppAccelerationDetails.
        WebAppAcceleration display name, can be renamed.


        :param display_name: The display_name of this UpdateWebAppAccelerationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def web_app_acceleration_policy_id(self):
        """
        Gets the web_app_acceleration_policy_id of this UpdateWebAppAccelerationDetails.
        The `OCID`__ of WebAppAccelerationPolicy, which is attached to the resource.
        This update guarantees that the resource always has WebAppAccelerationPolicy attached at any time.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The web_app_acceleration_policy_id of this UpdateWebAppAccelerationDetails.
        :rtype: str
        """
        return self._web_app_acceleration_policy_id

    @web_app_acceleration_policy_id.setter
    def web_app_acceleration_policy_id(self, web_app_acceleration_policy_id):
        """
        Sets the web_app_acceleration_policy_id of this UpdateWebAppAccelerationDetails.
        The `OCID`__ of WebAppAccelerationPolicy, which is attached to the resource.
        This update guarantees that the resource always has WebAppAccelerationPolicy attached at any time.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param web_app_acceleration_policy_id: The web_app_acceleration_policy_id of this UpdateWebAppAccelerationDetails.
        :type: str
        """
        self._web_app_acceleration_policy_id = web_app_acceleration_policy_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateWebAppAccelerationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateWebAppAccelerationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateWebAppAccelerationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateWebAppAccelerationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateWebAppAccelerationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateWebAppAccelerationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateWebAppAccelerationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateWebAppAccelerationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this UpdateWebAppAccelerationDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this UpdateWebAppAccelerationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this UpdateWebAppAccelerationDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this UpdateWebAppAccelerationDetails.
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
