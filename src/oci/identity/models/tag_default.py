# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TagDefault(object):
    """
    A document that specifies a default value for a Tag Definition for all resource types created in a Compartment.

    Tag Defaults are inherited by child compartments. This means that if you set a Tag Default on the root Compartment
    for a tenancy, all resources are guaranteed to be created with the referenced Tag Definition applied.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator.
    """

    #: A constant which can be used with the lifecycle_state property of a TagDefault.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new TagDefault object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TagDefault.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TagDefault.
        :type compartment_id: str

        :param tag_namespace_id:
            The value to assign to the tag_namespace_id property of this TagDefault.
        :type tag_namespace_id: str

        :param tag_definition_id:
            The value to assign to the tag_definition_id property of this TagDefault.
        :type tag_definition_id: str

        :param tag_definition_name:
            The value to assign to the tag_definition_name property of this TagDefault.
        :type tag_definition_name: str

        :param value:
            The value to assign to the value property of this TagDefault.
        :type value: str

        :param time_created:
            The value to assign to the time_created property of this TagDefault.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TagDefault.
            Allowed values for this property are: "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'tag_namespace_id': 'str',
            'tag_definition_id': 'str',
            'tag_definition_name': 'str',
            'value': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'tag_namespace_id': 'tagNamespaceId',
            'tag_definition_id': 'tagDefinitionId',
            'tag_definition_name': 'tagDefinitionName',
            'value': 'value',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._compartment_id = None
        self._tag_namespace_id = None
        self._tag_definition_id = None
        self._tag_definition_name = None
        self._value = None
        self._time_created = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TagDefault.
        The OCID of the Tag Default.


        :return: The id of this TagDefault.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TagDefault.
        The OCID of the Tag Default.


        :param id: The id of this TagDefault.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TagDefault.
        The OCID of the Compartment. The Tag Default will apply to any resource contained in this Compartment.


        :return: The compartment_id of this TagDefault.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TagDefault.
        The OCID of the Compartment. The Tag Default will apply to any resource contained in this Compartment.


        :param compartment_id: The compartment_id of this TagDefault.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tag_namespace_id(self):
        """
        **[Required]** Gets the tag_namespace_id of this TagDefault.
        The OCID of the Tag Namespace that contains the Tag Definition.


        :return: The tag_namespace_id of this TagDefault.
        :rtype: str
        """
        return self._tag_namespace_id

    @tag_namespace_id.setter
    def tag_namespace_id(self, tag_namespace_id):
        """
        Sets the tag_namespace_id of this TagDefault.
        The OCID of the Tag Namespace that contains the Tag Definition.


        :param tag_namespace_id: The tag_namespace_id of this TagDefault.
        :type: str
        """
        self._tag_namespace_id = tag_namespace_id

    @property
    def tag_definition_id(self):
        """
        **[Required]** Gets the tag_definition_id of this TagDefault.
        The OCID of the Tag Definition. The Tag Default will always assign a default value for this Tag Definition.


        :return: The tag_definition_id of this TagDefault.
        :rtype: str
        """
        return self._tag_definition_id

    @tag_definition_id.setter
    def tag_definition_id(self, tag_definition_id):
        """
        Sets the tag_definition_id of this TagDefault.
        The OCID of the Tag Definition. The Tag Default will always assign a default value for this Tag Definition.


        :param tag_definition_id: The tag_definition_id of this TagDefault.
        :type: str
        """
        self._tag_definition_id = tag_definition_id

    @property
    def tag_definition_name(self):
        """
        **[Required]** Gets the tag_definition_name of this TagDefault.
        The name used in the Tag Definition. This field is informational in the context of the Tag Default.


        :return: The tag_definition_name of this TagDefault.
        :rtype: str
        """
        return self._tag_definition_name

    @tag_definition_name.setter
    def tag_definition_name(self, tag_definition_name):
        """
        Sets the tag_definition_name of this TagDefault.
        The name used in the Tag Definition. This field is informational in the context of the Tag Default.


        :param tag_definition_name: The tag_definition_name of this TagDefault.
        :type: str
        """
        self._tag_definition_name = tag_definition_name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this TagDefault.
        The default value for the Tag Definition. This will be applied to all resources created in the Compartment.


        :return: The value of this TagDefault.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this TagDefault.
        The default value for the Tag Definition. This will be applied to all resources created in the Compartment.


        :param value: The value of this TagDefault.
        :type: str
        """
        self._value = value

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this TagDefault.
        Date and time the `TagDefault` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this TagDefault.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TagDefault.
        Date and time the `TagDefault` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this TagDefault.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TagDefault.
        The tag default's current state. After creating a tagdefault, make sure its `lifecycleState` is ACTIVE before using it.

        Allowed values for this property are: "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TagDefault.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TagDefault.
        The tag default's current state. After creating a tagdefault, make sure its `lifecycleState` is ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this TagDefault.
        :type: str
        """
        allowed_values = ["ACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
