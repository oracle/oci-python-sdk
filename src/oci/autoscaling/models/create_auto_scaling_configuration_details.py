# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutoScalingConfigurationDetails(object):
    """
    Creation details for an autoscaling configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutoScalingConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAutoScalingConfigurationDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAutoScalingConfigurationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateAutoScalingConfigurationDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAutoScalingConfigurationDetails.
        :type freeform_tags: dict(str, str)

        :param cool_down_in_seconds:
            The value to assign to the cool_down_in_seconds property of this CreateAutoScalingConfigurationDetails.
        :type cool_down_in_seconds: int

        :param is_enabled:
            The value to assign to the is_enabled property of this CreateAutoScalingConfigurationDetails.
        :type is_enabled: bool

        :param policies:
            The value to assign to the policies property of this CreateAutoScalingConfigurationDetails.
        :type policies: list[CreateAutoScalingPolicyDetails]

        :param resource:
            The value to assign to the resource property of this CreateAutoScalingConfigurationDetails.
        :type resource: Resource

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'cool_down_in_seconds': 'int',
            'is_enabled': 'bool',
            'policies': 'list[CreateAutoScalingPolicyDetails]',
            'resource': 'Resource'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'cool_down_in_seconds': 'coolDownInSeconds',
            'is_enabled': 'isEnabled',
            'policies': 'policies',
            'resource': 'resource'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._cool_down_in_seconds = None
        self._is_enabled = None
        self._policies = None
        self._resource = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAutoScalingConfigurationDetails.
        The `OCID`__ of the compartment containing the autoscaling configuration.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateAutoScalingConfigurationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAutoScalingConfigurationDetails.
        The `OCID`__ of the compartment containing the autoscaling configuration.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateAutoScalingConfigurationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAutoScalingConfigurationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateAutoScalingConfigurationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAutoScalingConfigurationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateAutoScalingConfigurationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateAutoScalingConfigurationDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateAutoScalingConfigurationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAutoScalingConfigurationDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateAutoScalingConfigurationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAutoScalingConfigurationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateAutoScalingConfigurationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAutoScalingConfigurationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateAutoScalingConfigurationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def cool_down_in_seconds(self):
        """
        Gets the cool_down_in_seconds of this CreateAutoScalingConfigurationDetails.
        The minimum period of time to wait between scaling actions. The cooldown period gives the system time to stabilize
        before rescaling. The minimum value is 300 seconds, which is also the default.


        :return: The cool_down_in_seconds of this CreateAutoScalingConfigurationDetails.
        :rtype: int
        """
        return self._cool_down_in_seconds

    @cool_down_in_seconds.setter
    def cool_down_in_seconds(self, cool_down_in_seconds):
        """
        Sets the cool_down_in_seconds of this CreateAutoScalingConfigurationDetails.
        The minimum period of time to wait between scaling actions. The cooldown period gives the system time to stabilize
        before rescaling. The minimum value is 300 seconds, which is also the default.


        :param cool_down_in_seconds: The cool_down_in_seconds of this CreateAutoScalingConfigurationDetails.
        :type: int
        """
        self._cool_down_in_seconds = cool_down_in_seconds

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this CreateAutoScalingConfigurationDetails.
        Whether the autoscaling configuration is enabled.


        :return: The is_enabled of this CreateAutoScalingConfigurationDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this CreateAutoScalingConfigurationDetails.
        Whether the autoscaling configuration is enabled.


        :param is_enabled: The is_enabled of this CreateAutoScalingConfigurationDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def policies(self):
        """
        **[Required]** Gets the policies of this CreateAutoScalingConfigurationDetails.

        :return: The policies of this CreateAutoScalingConfigurationDetails.
        :rtype: list[CreateAutoScalingPolicyDetails]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """
        Sets the policies of this CreateAutoScalingConfigurationDetails.

        :param policies: The policies of this CreateAutoScalingConfigurationDetails.
        :type: list[CreateAutoScalingPolicyDetails]
        """
        self._policies = policies

    @property
    def resource(self):
        """
        **[Required]** Gets the resource of this CreateAutoScalingConfigurationDetails.

        :return: The resource of this CreateAutoScalingConfigurationDetails.
        :rtype: Resource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this CreateAutoScalingConfigurationDetails.

        :param resource: The resource of this CreateAutoScalingConfigurationDetails.
        :type: Resource
        """
        self._resource = resource

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
