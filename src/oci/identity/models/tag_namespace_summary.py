# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TagNamespaceSummary(object):
    """
    A container for defined tags.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TagNamespaceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TagNamespaceSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TagNamespaceSummary.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this TagNamespaceSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this TagNamespaceSummary.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TagNamespaceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TagNamespaceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param is_retired:
            The value to assign to the is_retired property of this TagNamespaceSummary.
        :type is_retired: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TagNamespaceSummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this TagNamespaceSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_retired': 'bool',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_retired': 'isRetired',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_retired = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def id(self):
        """
        Gets the id of this TagNamespaceSummary.
        The OCID of the tag namespace.


        :return: The id of this TagNamespaceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TagNamespaceSummary.
        The OCID of the tag namespace.


        :param id: The id of this TagNamespaceSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this TagNamespaceSummary.
        The OCID of the compartment that contains the tag namespace.


        :return: The compartment_id of this TagNamespaceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TagNamespaceSummary.
        The OCID of the compartment that contains the tag namespace.


        :param compartment_id: The compartment_id of this TagNamespaceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this TagNamespaceSummary.
        The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.


        :return: The name of this TagNamespaceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TagNamespaceSummary.
        The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.


        :param name: The name of this TagNamespaceSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TagNamespaceSummary.
        The description you assign to the tag namespace.


        :return: The description of this TagNamespaceSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TagNamespaceSummary.
        The description you assign to the tag namespace.


        :param description: The description of this TagNamespaceSummary.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this TagNamespaceSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this TagNamespaceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this TagNamespaceSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this TagNamespaceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this TagNamespaceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this TagNamespaceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this TagNamespaceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this TagNamespaceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_retired(self):
        """
        Gets the is_retired of this TagNamespaceSummary.
        Whether the tag namespace is retired.
        For more information, see `Retiring Key Definitions and Namespace Definitions`__.

        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/taggingoverview.htm#Retiring


        :return: The is_retired of this TagNamespaceSummary.
        :rtype: bool
        """
        return self._is_retired

    @is_retired.setter
    def is_retired(self, is_retired):
        """
        Sets the is_retired of this TagNamespaceSummary.
        Whether the tag namespace is retired.
        For more information, see `Retiring Key Definitions and Namespace Definitions`__.

        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/taggingoverview.htm#Retiring


        :param is_retired: The is_retired of this TagNamespaceSummary.
        :type: bool
        """
        self._is_retired = is_retired

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TagNamespaceSummary.
        The tagnamespace's current state. After creating a tagnamespace, make sure its `lifecycleState` is ACTIVE before using it. After retiring a tagnamespace, make sure its `lifecycleState` is INACTIVE before using it.


        :return: The lifecycle_state of this TagNamespaceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TagNamespaceSummary.
        The tagnamespace's current state. After creating a tagnamespace, make sure its `lifecycleState` is ACTIVE before using it. After retiring a tagnamespace, make sure its `lifecycleState` is INACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this TagNamespaceSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this TagNamespaceSummary.
        Date and time the tag namespace was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this TagNamespaceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TagNamespaceSummary.
        Date and time the tag namespace was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this TagNamespaceSummary.
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
