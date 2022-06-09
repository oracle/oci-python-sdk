# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TagDefaultSummary(object):
    """
    Summary information for the specified tag default.
    """

    #: A constant which can be used with the lifecycle_state property of a TagDefaultSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new TagDefaultSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TagDefaultSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TagDefaultSummary.
        :type compartment_id: str

        :param tag_namespace_id:
            The value to assign to the tag_namespace_id property of this TagDefaultSummary.
        :type tag_namespace_id: str

        :param tag_definition_id:
            The value to assign to the tag_definition_id property of this TagDefaultSummary.
        :type tag_definition_id: str

        :param tag_definition_name:
            The value to assign to the tag_definition_name property of this TagDefaultSummary.
        :type tag_definition_name: str

        :param value:
            The value to assign to the value property of this TagDefaultSummary.
        :type value: str

        :param time_created:
            The value to assign to the time_created property of this TagDefaultSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TagDefaultSummary.
            Allowed values for this property are: "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param is_required:
            The value to assign to the is_required property of this TagDefaultSummary.
        :type is_required: bool

        :param locks:
            The value to assign to the locks property of this TagDefaultSummary.
        :type locks: list[oci.identity.models.ResourceLock]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'tag_namespace_id': 'str',
            'tag_definition_id': 'str',
            'tag_definition_name': 'str',
            'value': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'is_required': 'bool',
            'locks': 'list[ResourceLock]'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'tag_namespace_id': 'tagNamespaceId',
            'tag_definition_id': 'tagDefinitionId',
            'tag_definition_name': 'tagDefinitionName',
            'value': 'value',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'is_required': 'isRequired',
            'locks': 'locks'
        }

        self._id = None
        self._compartment_id = None
        self._tag_namespace_id = None
        self._tag_definition_id = None
        self._tag_definition_name = None
        self._value = None
        self._time_created = None
        self._lifecycle_state = None
        self._is_required = None
        self._locks = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TagDefaultSummary.
        The OCID of the tag default.


        :return: The id of this TagDefaultSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TagDefaultSummary.
        The OCID of the tag default.


        :param id: The id of this TagDefaultSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TagDefaultSummary.
        The OCID of the compartment. The tag default will apply to all new resources that are created in the compartment.


        :return: The compartment_id of this TagDefaultSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TagDefaultSummary.
        The OCID of the compartment. The tag default will apply to all new resources that are created in the compartment.


        :param compartment_id: The compartment_id of this TagDefaultSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tag_namespace_id(self):
        """
        **[Required]** Gets the tag_namespace_id of this TagDefaultSummary.
        The OCID of the tag namespace that contains the tag definition.


        :return: The tag_namespace_id of this TagDefaultSummary.
        :rtype: str
        """
        return self._tag_namespace_id

    @tag_namespace_id.setter
    def tag_namespace_id(self, tag_namespace_id):
        """
        Sets the tag_namespace_id of this TagDefaultSummary.
        The OCID of the tag namespace that contains the tag definition.


        :param tag_namespace_id: The tag_namespace_id of this TagDefaultSummary.
        :type: str
        """
        self._tag_namespace_id = tag_namespace_id

    @property
    def tag_definition_id(self):
        """
        **[Required]** Gets the tag_definition_id of this TagDefaultSummary.
        The OCID of the tag definition. The tag default will always assign a default value for this tag definition.


        :return: The tag_definition_id of this TagDefaultSummary.
        :rtype: str
        """
        return self._tag_definition_id

    @tag_definition_id.setter
    def tag_definition_id(self, tag_definition_id):
        """
        Sets the tag_definition_id of this TagDefaultSummary.
        The OCID of the tag definition. The tag default will always assign a default value for this tag definition.


        :param tag_definition_id: The tag_definition_id of this TagDefaultSummary.
        :type: str
        """
        self._tag_definition_id = tag_definition_id

    @property
    def tag_definition_name(self):
        """
        **[Required]** Gets the tag_definition_name of this TagDefaultSummary.
        The name used in the tag definition. This field is informational in the context of the tag default.


        :return: The tag_definition_name of this TagDefaultSummary.
        :rtype: str
        """
        return self._tag_definition_name

    @tag_definition_name.setter
    def tag_definition_name(self, tag_definition_name):
        """
        Sets the tag_definition_name of this TagDefaultSummary.
        The name used in the tag definition. This field is informational in the context of the tag default.


        :param tag_definition_name: The tag_definition_name of this TagDefaultSummary.
        :type: str
        """
        self._tag_definition_name = tag_definition_name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this TagDefaultSummary.
        The default value for the tag definition. This will be applied to all new resources created in the compartment.


        :return: The value of this TagDefaultSummary.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this TagDefaultSummary.
        The default value for the tag definition. This will be applied to all new resources created in the compartment.


        :param value: The value of this TagDefaultSummary.
        :type: str
        """
        self._value = value

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this TagDefaultSummary.
        Date and time the `TagDefault` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this TagDefaultSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TagDefaultSummary.
        Date and time the `TagDefault` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this TagDefaultSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TagDefaultSummary.
        The tag default's current state. After creating a `TagDefault`, make sure its `lifecycleState` is ACTIVE before using it.

        Allowed values for this property are: "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TagDefaultSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TagDefaultSummary.
        The tag default's current state. After creating a `TagDefault`, make sure its `lifecycleState` is ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this TagDefaultSummary.
        :type: str
        """
        allowed_values = ["ACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def is_required(self):
        """
        **[Required]** Gets the is_required of this TagDefaultSummary.
        If you specify that a value is required, a value is set during resource creation (either by
        the user creating the resource or another tag defualt). If no value is set, resource
        creation is blocked.

        * If the `isRequired` flag is set to \"true\", the value is set during resource creation.
        * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation.

        Example: `false`


        :return: The is_required of this TagDefaultSummary.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """
        Sets the is_required of this TagDefaultSummary.
        If you specify that a value is required, a value is set during resource creation (either by
        the user creating the resource or another tag defualt). If no value is set, resource
        creation is blocked.

        * If the `isRequired` flag is set to \"true\", the value is set during resource creation.
        * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation.

        Example: `false`


        :param is_required: The is_required of this TagDefaultSummary.
        :type: bool
        """
        self._is_required = is_required

    @property
    def locks(self):
        """
        Gets the locks of this TagDefaultSummary.
        Locks associated with this resource.


        :return: The locks of this TagDefaultSummary.
        :rtype: list[oci.identity.models.ResourceLock]
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """
        Sets the locks of this TagDefaultSummary.
        Locks associated with this resource.


        :param locks: The locks of this TagDefaultSummary.
        :type: list[oci.identity.models.ResourceLock]
        """
        self._locks = locks

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
