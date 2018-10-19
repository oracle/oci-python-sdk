# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationSummary(object):
    """
    Instance Configuration Summary
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this InstanceConfigurationSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this InstanceConfigurationSummary.
        :type display_name: str

        :param id:
            The value to assign to the id property of this InstanceConfigurationSummary.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this InstanceConfigurationSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this InstanceConfigurationSummary.
        The OCID of the compartment containing the instance configuration.


        :return: The compartment_id of this InstanceConfigurationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InstanceConfigurationSummary.
        The OCID of the compartment containing the instance configuration.


        :param compartment_id: The compartment_id of this InstanceConfigurationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this InstanceConfigurationSummary.
        A user-friendly name for the instance configuration


        :return: The display_name of this InstanceConfigurationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstanceConfigurationSummary.
        A user-friendly name for the instance configuration


        :param display_name: The display_name of this InstanceConfigurationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this InstanceConfigurationSummary.
        The OCID of the instance configuration


        :return: The id of this InstanceConfigurationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstanceConfigurationSummary.
        The OCID of the instance configuration


        :param id: The id of this InstanceConfigurationSummary.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this InstanceConfigurationSummary.
        The date and time the instance configuration was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this InstanceConfigurationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InstanceConfigurationSummary.
        The date and time the instance configuration was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this InstanceConfigurationSummary.
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
