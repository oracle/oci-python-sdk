# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoScalingConfigurationSummary(object):
    """
    AutoScalingConfigurationSummary model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutoScalingConfigurationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this AutoScalingConfigurationSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this AutoScalingConfigurationSummary.
        :type display_name: str

        :param id:
            The value to assign to the id property of this AutoScalingConfigurationSummary.
        :type id: str

        :param cool_down_in_seconds:
            The value to assign to the cool_down_in_seconds property of this AutoScalingConfigurationSummary.
        :type cool_down_in_seconds: int

        :param is_enabled:
            The value to assign to the is_enabled property of this AutoScalingConfigurationSummary.
        :type is_enabled: bool

        :param resource:
            The value to assign to the resource property of this AutoScalingConfigurationSummary.
        :type resource: Resource

        :param time_created:
            The value to assign to the time_created property of this AutoScalingConfigurationSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'cool_down_in_seconds': 'int',
            'is_enabled': 'bool',
            'resource': 'Resource',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'cool_down_in_seconds': 'coolDownInSeconds',
            'is_enabled': 'isEnabled',
            'resource': 'resource',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._cool_down_in_seconds = None
        self._is_enabled = None
        self._resource = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AutoScalingConfigurationSummary.
        The OCID of the compartment containing the AutoScalingConfiguration.


        :return: The compartment_id of this AutoScalingConfigurationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AutoScalingConfigurationSummary.
        The OCID of the compartment containing the AutoScalingConfiguration.


        :param compartment_id: The compartment_id of this AutoScalingConfigurationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this AutoScalingConfigurationSummary.
        A user-friendly name for the AutoScalingConfiguration. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this AutoScalingConfigurationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutoScalingConfigurationSummary.
        A user-friendly name for the AutoScalingConfiguration. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this AutoScalingConfigurationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutoScalingConfigurationSummary.
        The OCID of the AutoScalingConfiguration


        :return: The id of this AutoScalingConfigurationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutoScalingConfigurationSummary.
        The OCID of the AutoScalingConfiguration


        :param id: The id of this AutoScalingConfigurationSummary.
        :type: str
        """
        self._id = id

    @property
    def cool_down_in_seconds(self):
        """
        Gets the cool_down_in_seconds of this AutoScalingConfigurationSummary.
        The minimum period of time between scaling actions. The default is 300 seconds.


        :return: The cool_down_in_seconds of this AutoScalingConfigurationSummary.
        :rtype: int
        """
        return self._cool_down_in_seconds

    @cool_down_in_seconds.setter
    def cool_down_in_seconds(self, cool_down_in_seconds):
        """
        Sets the cool_down_in_seconds of this AutoScalingConfigurationSummary.
        The minimum period of time between scaling actions. The default is 300 seconds.


        :param cool_down_in_seconds: The cool_down_in_seconds of this AutoScalingConfigurationSummary.
        :type: int
        """
        self._cool_down_in_seconds = cool_down_in_seconds

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this AutoScalingConfigurationSummary.
        If the AutoScalingConfiguration is enabled


        :return: The is_enabled of this AutoScalingConfigurationSummary.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this AutoScalingConfigurationSummary.
        If the AutoScalingConfiguration is enabled


        :param is_enabled: The is_enabled of this AutoScalingConfigurationSummary.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def resource(self):
        """
        Gets the resource of this AutoScalingConfigurationSummary.

        :return: The resource of this AutoScalingConfigurationSummary.
        :rtype: Resource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this AutoScalingConfigurationSummary.

        :param resource: The resource of this AutoScalingConfigurationSummary.
        :type: Resource
        """
        self._resource = resource

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AutoScalingConfigurationSummary.
        The date and time the AutoScalingConfiguration was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this AutoScalingConfigurationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AutoScalingConfigurationSummary.
        The date and time the AutoScalingConfiguration was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this AutoScalingConfigurationSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
