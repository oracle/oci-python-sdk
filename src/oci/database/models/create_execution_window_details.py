# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateExecutionWindowDetails(object):
    """
    Request to create an execution window resource under an execution resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateExecutionWindowDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateExecutionWindowDetails.
        :type compartment_id: str

        :param execution_resource_id:
            The value to assign to the execution_resource_id property of this CreateExecutionWindowDetails.
        :type execution_resource_id: str

        :param time_scheduled:
            The value to assign to the time_scheduled property of this CreateExecutionWindowDetails.
        :type time_scheduled: datetime

        :param window_duration_in_mins:
            The value to assign to the window_duration_in_mins property of this CreateExecutionWindowDetails.
        :type window_duration_in_mins: int

        :param is_enforced_duration:
            The value to assign to the is_enforced_duration property of this CreateExecutionWindowDetails.
        :type is_enforced_duration: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateExecutionWindowDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateExecutionWindowDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'execution_resource_id': 'str',
            'time_scheduled': 'datetime',
            'window_duration_in_mins': 'int',
            'is_enforced_duration': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'execution_resource_id': 'executionResourceId',
            'time_scheduled': 'timeScheduled',
            'window_duration_in_mins': 'windowDurationInMins',
            'is_enforced_duration': 'isEnforcedDuration',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._compartment_id = None
        self._execution_resource_id = None
        self._time_scheduled = None
        self._window_duration_in_mins = None
        self._is_enforced_duration = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateExecutionWindowDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateExecutionWindowDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateExecutionWindowDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateExecutionWindowDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def execution_resource_id(self):
        """
        **[Required]** Gets the execution_resource_id of this CreateExecutionWindowDetails.
        The `OCID`__ of the execution resource the execution window belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The execution_resource_id of this CreateExecutionWindowDetails.
        :rtype: str
        """
        return self._execution_resource_id

    @execution_resource_id.setter
    def execution_resource_id(self, execution_resource_id):
        """
        Sets the execution_resource_id of this CreateExecutionWindowDetails.
        The `OCID`__ of the execution resource the execution window belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param execution_resource_id: The execution_resource_id of this CreateExecutionWindowDetails.
        :type: str
        """
        self._execution_resource_id = execution_resource_id

    @property
    def time_scheduled(self):
        """
        **[Required]** Gets the time_scheduled of this CreateExecutionWindowDetails.
        The scheduled start date and time of the execution window.


        :return: The time_scheduled of this CreateExecutionWindowDetails.
        :rtype: datetime
        """
        return self._time_scheduled

    @time_scheduled.setter
    def time_scheduled(self, time_scheduled):
        """
        Sets the time_scheduled of this CreateExecutionWindowDetails.
        The scheduled start date and time of the execution window.


        :param time_scheduled: The time_scheduled of this CreateExecutionWindowDetails.
        :type: datetime
        """
        self._time_scheduled = time_scheduled

    @property
    def window_duration_in_mins(self):
        """
        **[Required]** Gets the window_duration_in_mins of this CreateExecutionWindowDetails.
        Duration window allows user to set a duration they plan to allocate for Scheduling window. The duration is in minutes.


        :return: The window_duration_in_mins of this CreateExecutionWindowDetails.
        :rtype: int
        """
        return self._window_duration_in_mins

    @window_duration_in_mins.setter
    def window_duration_in_mins(self, window_duration_in_mins):
        """
        Sets the window_duration_in_mins of this CreateExecutionWindowDetails.
        Duration window allows user to set a duration they plan to allocate for Scheduling window. The duration is in minutes.


        :param window_duration_in_mins: The window_duration_in_mins of this CreateExecutionWindowDetails.
        :type: int
        """
        self._window_duration_in_mins = window_duration_in_mins

    @property
    def is_enforced_duration(self):
        """
        Gets the is_enforced_duration of this CreateExecutionWindowDetails.
        Indicates if duration the user plans to allocate for scheduling window is strictly enforced. The default value is `FALSE`.


        :return: The is_enforced_duration of this CreateExecutionWindowDetails.
        :rtype: bool
        """
        return self._is_enforced_duration

    @is_enforced_duration.setter
    def is_enforced_duration(self, is_enforced_duration):
        """
        Sets the is_enforced_duration of this CreateExecutionWindowDetails.
        Indicates if duration the user plans to allocate for scheduling window is strictly enforced. The default value is `FALSE`.


        :param is_enforced_duration: The is_enforced_duration of this CreateExecutionWindowDetails.
        :type: bool
        """
        self._is_enforced_duration = is_enforced_duration

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateExecutionWindowDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateExecutionWindowDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateExecutionWindowDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateExecutionWindowDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateExecutionWindowDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateExecutionWindowDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateExecutionWindowDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateExecutionWindowDetails.
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
