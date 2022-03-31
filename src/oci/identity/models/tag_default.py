# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TagDefault(object):
    """
    Tag defaults let you specify a default tag (tagnamespace.tag=\"value\") to apply to all resource types
    in a specified compartment. The tag default is applied at the time the resource is created. Resources
    that exist in the compartment before you create the tag default are not tagged. The `TagDefault` object
    specifies the tag and compartment details.

    Tag defaults are inherited by child compartments. This means that if you set a tag default on the root compartment
    for a tenancy, all resources that are created in the tenancy are tagged. For more information about
    using tag defaults, see `Managing Tag Defaults`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator.

    __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagdefaults.htm
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

        :param is_required:
            The value to assign to the is_required property of this TagDefault.
        :type is_required: bool

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
            'is_required': 'bool'
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
            'is_required': 'isRequired'
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

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TagDefault.
        The OCID of the tag default.


        :return: The id of this TagDefault.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TagDefault.
        The OCID of the tag default.


        :param id: The id of this TagDefault.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TagDefault.
        The OCID of the compartment. The tag default applies to all new resources that get created in the
        compartment. Resources that existed before the tag default was created are not tagged.


        :return: The compartment_id of this TagDefault.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TagDefault.
        The OCID of the compartment. The tag default applies to all new resources that get created in the
        compartment. Resources that existed before the tag default was created are not tagged.


        :param compartment_id: The compartment_id of this TagDefault.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tag_namespace_id(self):
        """
        **[Required]** Gets the tag_namespace_id of this TagDefault.
        The OCID of the tag namespace that contains the tag definition.


        :return: The tag_namespace_id of this TagDefault.
        :rtype: str
        """
        return self._tag_namespace_id

    @tag_namespace_id.setter
    def tag_namespace_id(self, tag_namespace_id):
        """
        Sets the tag_namespace_id of this TagDefault.
        The OCID of the tag namespace that contains the tag definition.


        :param tag_namespace_id: The tag_namespace_id of this TagDefault.
        :type: str
        """
        self._tag_namespace_id = tag_namespace_id

    @property
    def tag_definition_id(self):
        """
        **[Required]** Gets the tag_definition_id of this TagDefault.
        The OCID of the tag definition. The tag default will always assign a default value for this tag definition.


        :return: The tag_definition_id of this TagDefault.
        :rtype: str
        """
        return self._tag_definition_id

    @tag_definition_id.setter
    def tag_definition_id(self, tag_definition_id):
        """
        Sets the tag_definition_id of this TagDefault.
        The OCID of the tag definition. The tag default will always assign a default value for this tag definition.


        :param tag_definition_id: The tag_definition_id of this TagDefault.
        :type: str
        """
        self._tag_definition_id = tag_definition_id

    @property
    def tag_definition_name(self):
        """
        **[Required]** Gets the tag_definition_name of this TagDefault.
        The name used in the tag definition. This field is informational in the context of the tag default.


        :return: The tag_definition_name of this TagDefault.
        :rtype: str
        """
        return self._tag_definition_name

    @tag_definition_name.setter
    def tag_definition_name(self, tag_definition_name):
        """
        Sets the tag_definition_name of this TagDefault.
        The name used in the tag definition. This field is informational in the context of the tag default.


        :param tag_definition_name: The tag_definition_name of this TagDefault.
        :type: str
        """
        self._tag_definition_name = tag_definition_name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this TagDefault.
        The default value for the tag definition. This will be applied to all resources created in the compartment.


        :return: The value of this TagDefault.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this TagDefault.
        The default value for the tag definition. This will be applied to all resources created in the compartment.


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
        The tag default's current state. After creating a `TagDefault`, make sure its `lifecycleState` is ACTIVE before using it.

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
        The tag default's current state. After creating a `TagDefault`, make sure its `lifecycleState` is ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this TagDefault.
        :type: str
        """
        allowed_values = ["ACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def is_required(self):
        """
        **[Required]** Gets the is_required of this TagDefault.
        If you specify that a value is required, a value is set during resource creation (either by the
        user creating the resource or another tag defualt). If no value is set, resource creation is
        blocked.

        * If the `isRequired` flag is set to \"true\", the value is set during resource creation.
        * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation.

        Example: `false`


        :return: The is_required of this TagDefault.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """
        Sets the is_required of this TagDefault.
        If you specify that a value is required, a value is set during resource creation (either by the
        user creating the resource or another tag defualt). If no value is set, resource creation is
        blocked.

        * If the `isRequired` flag is set to \"true\", the value is set during resource creation.
        * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation.

        Example: `false`


        :param is_required: The is_required of this TagDefault.
        :type: bool
        """
        self._is_required = is_required

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
