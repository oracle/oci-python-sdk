# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConsoleHistory(object):

    def __init__(self, **kwargs):
        """
        Initializes a new ConsoleHistory object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this ConsoleHistory.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ConsoleHistory.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this ConsoleHistory.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this ConsoleHistory.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ConsoleHistory.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this ConsoleHistory.
        :type id: str

        :param instance_id:
            The value to assign to the instance_id property of this ConsoleHistory.
        :type instance_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ConsoleHistory.
            Allowed values for this property are: "REQUESTED", "GETTING-HISTORY", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ConsoleHistory.
        :type time_created: datetime

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'instance_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'instance_id': 'instanceId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._instance_id = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this ConsoleHistory.
        The Availability Domain of an instance.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this ConsoleHistory.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ConsoleHistory.
        The Availability Domain of an instance.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this ConsoleHistory.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ConsoleHistory.
        The OCID of the compartment.


        :return: The compartment_id of this ConsoleHistory.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ConsoleHistory.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this ConsoleHistory.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ConsoleHistory.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ConsoleHistory.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ConsoleHistory.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ConsoleHistory.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this ConsoleHistory.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My console history metadata`


        :return: The display_name of this ConsoleHistory.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ConsoleHistory.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My console history metadata`


        :param display_name: The display_name of this ConsoleHistory.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ConsoleHistory.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ConsoleHistory.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ConsoleHistory.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ConsoleHistory.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ConsoleHistory.
        The OCID of the console history metadata object.


        :return: The id of this ConsoleHistory.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConsoleHistory.
        The OCID of the console history metadata object.


        :param id: The id of this ConsoleHistory.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this ConsoleHistory.
        The OCID of the instance this console history was fetched from.


        :return: The instance_id of this ConsoleHistory.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this ConsoleHistory.
        The OCID of the instance this console history was fetched from.


        :param instance_id: The instance_id of this ConsoleHistory.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ConsoleHistory.
        The current state of the console history.

        Allowed values for this property are: "REQUESTED", "GETTING-HISTORY", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ConsoleHistory.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ConsoleHistory.
        The current state of the console history.


        :param lifecycle_state: The lifecycle_state of this ConsoleHistory.
        :type: str
        """
        allowed_values = ["REQUESTED", "GETTING-HISTORY", "SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ConsoleHistory.
        The date and time the history was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this ConsoleHistory.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ConsoleHistory.
        The date and time the history was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this ConsoleHistory.
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
