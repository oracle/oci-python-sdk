# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstancePoolSummary(object):
    """
    Summary information for an instance pool.
    """

    #: A constant which can be used with the lifecycle_state property of a InstancePoolSummary.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a InstancePoolSummary.
    #: This constant has a value of "SCALING"
    LIFECYCLE_STATE_SCALING = "SCALING"

    #: A constant which can be used with the lifecycle_state property of a InstancePoolSummary.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_state property of a InstancePoolSummary.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a InstancePoolSummary.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a InstancePoolSummary.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the lifecycle_state property of a InstancePoolSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a InstancePoolSummary.
    #: This constant has a value of "RUNNING"
    LIFECYCLE_STATE_RUNNING = "RUNNING"

    def __init__(self, **kwargs):
        """
        Initializes a new InstancePoolSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this InstancePoolSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this InstancePoolSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this InstancePoolSummary.
        :type display_name: str

        :param instance_configuration_id:
            The value to assign to the instance_configuration_id property of this InstancePoolSummary.
        :type instance_configuration_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this InstancePoolSummary.
            Allowed values for this property are: "PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param availability_domains:
            The value to assign to the availability_domains property of this InstancePoolSummary.
        :type availability_domains: list[str]

        :param size:
            The value to assign to the size property of this InstancePoolSummary.
        :type size: int

        :param time_created:
            The value to assign to the time_created property of this InstancePoolSummary.
        :type time_created: datetime

        :param defined_tags:
            The value to assign to the defined_tags property of this InstancePoolSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this InstancePoolSummary.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'instance_configuration_id': 'str',
            'lifecycle_state': 'str',
            'availability_domains': 'list[str]',
            'size': 'int',
            'time_created': 'datetime',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'instance_configuration_id': 'instanceConfigurationId',
            'lifecycle_state': 'lifecycleState',
            'availability_domains': 'availabilityDomains',
            'size': 'size',
            'time_created': 'timeCreated',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._instance_configuration_id = None
        self._lifecycle_state = None
        self._availability_domains = None
        self._size = None
        self._time_created = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this InstancePoolSummary.
        The OCID of the instance pool.


        :return: The id of this InstancePoolSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstancePoolSummary.
        The OCID of the instance pool.


        :param id: The id of this InstancePoolSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this InstancePoolSummary.
        The OCID of the compartment containing the instance pool.


        :return: The compartment_id of this InstancePoolSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InstancePoolSummary.
        The OCID of the compartment containing the instance pool.


        :param compartment_id: The compartment_id of this InstancePoolSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this InstancePoolSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this InstancePoolSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstancePoolSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this InstancePoolSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def instance_configuration_id(self):
        """
        **[Required]** Gets the instance_configuration_id of this InstancePoolSummary.
        The OCID of the instance configuration associated with the instance pool.


        :return: The instance_configuration_id of this InstancePoolSummary.
        :rtype: str
        """
        return self._instance_configuration_id

    @instance_configuration_id.setter
    def instance_configuration_id(self, instance_configuration_id):
        """
        Sets the instance_configuration_id of this InstancePoolSummary.
        The OCID of the instance configuration associated with the instance pool.


        :param instance_configuration_id: The instance_configuration_id of this InstancePoolSummary.
        :type: str
        """
        self._instance_configuration_id = instance_configuration_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this InstancePoolSummary.
        The current state of the instance pool.

        Allowed values for this property are: "PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this InstancePoolSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this InstancePoolSummary.
        The current state of the instance pool.


        :param lifecycle_state: The lifecycle_state of this InstancePoolSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def availability_domains(self):
        """
        **[Required]** Gets the availability_domains of this InstancePoolSummary.
        The availability domains for the instance pool.


        :return: The availability_domains of this InstancePoolSummary.
        :rtype: list[str]
        """
        return self._availability_domains

    @availability_domains.setter
    def availability_domains(self, availability_domains):
        """
        Sets the availability_domains of this InstancePoolSummary.
        The availability domains for the instance pool.


        :param availability_domains: The availability_domains of this InstancePoolSummary.
        :type: list[str]
        """
        self._availability_domains = availability_domains

    @property
    def size(self):
        """
        **[Required]** Gets the size of this InstancePoolSummary.
        The number of instances that should be in the instance pool.


        :return: The size of this InstancePoolSummary.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this InstancePoolSummary.
        The number of instances that should be in the instance pool.


        :param size: The size of this InstancePoolSummary.
        :type: int
        """
        self._size = size

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this InstancePoolSummary.
        The date and time the instance pool was created, in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this InstancePoolSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InstancePoolSummary.
        The date and time the instance pool was created, in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this InstancePoolSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this InstancePoolSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this InstancePoolSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this InstancePoolSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this InstancePoolSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this InstancePoolSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this InstancePoolSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this InstancePoolSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this InstancePoolSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
