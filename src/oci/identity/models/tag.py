# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Tag(object):
    """
    A tag definition that belongs to a specific tag namespace.  \"Defined tags\" must be set up in your tenancy before
    you can apply them to resources.
    For more information, see `Managing Tags and Tag Namespaces`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/taggingoverview.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Tag object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Tag.
        :type compartment_id: str

        :param tag_namespace_id:
            The value to assign to the tag_namespace_id property of this Tag.
        :type tag_namespace_id: str

        :param tag_namespace_name:
            The value to assign to the tag_namespace_name property of this Tag.
        :type tag_namespace_name: str

        :param id:
            The value to assign to the id property of this Tag.
        :type id: str

        :param name:
            The value to assign to the name property of this Tag.
        :type name: str

        :param description:
            The value to assign to the description property of this Tag.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Tag.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Tag.
        :type defined_tags: dict(str, dict(str, object))

        :param is_retired:
            The value to assign to the is_retired property of this Tag.
        :type is_retired: bool

        :param time_created:
            The value to assign to the time_created property of this Tag.
        :type time_created: datetime

        :param is_cost_tracking:
            The value to assign to the is_cost_tracking property of this Tag.
        :type is_cost_tracking: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'tag_namespace_id': 'str',
            'tag_namespace_name': 'str',
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_retired': 'bool',
            'time_created': 'datetime',
            'is_cost_tracking': 'bool'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'tag_namespace_id': 'tagNamespaceId',
            'tag_namespace_name': 'tagNamespaceName',
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_retired': 'isRetired',
            'time_created': 'timeCreated',
            'is_cost_tracking': 'isCostTracking'
        }

        self._compartment_id = None
        self._tag_namespace_id = None
        self._tag_namespace_name = None
        self._id = None
        self._name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_retired = None
        self._time_created = None
        self._is_cost_tracking = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Tag.
        The OCID of the compartment that contains the tag definition.


        :return: The compartment_id of this Tag.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Tag.
        The OCID of the compartment that contains the tag definition.


        :param compartment_id: The compartment_id of this Tag.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tag_namespace_id(self):
        """
        **[Required]** Gets the tag_namespace_id of this Tag.
        The OCID of the namespace that contains the tag definition.


        :return: The tag_namespace_id of this Tag.
        :rtype: str
        """
        return self._tag_namespace_id

    @tag_namespace_id.setter
    def tag_namespace_id(self, tag_namespace_id):
        """
        Sets the tag_namespace_id of this Tag.
        The OCID of the namespace that contains the tag definition.


        :param tag_namespace_id: The tag_namespace_id of this Tag.
        :type: str
        """
        self._tag_namespace_id = tag_namespace_id

    @property
    def tag_namespace_name(self):
        """
        **[Required]** Gets the tag_namespace_name of this Tag.
        The name of the tag namespace that contains the tag definition.


        :return: The tag_namespace_name of this Tag.
        :rtype: str
        """
        return self._tag_namespace_name

    @tag_namespace_name.setter
    def tag_namespace_name(self, tag_namespace_name):
        """
        Sets the tag_namespace_name of this Tag.
        The name of the tag namespace that contains the tag definition.


        :param tag_namespace_name: The tag_namespace_name of this Tag.
        :type: str
        """
        self._tag_namespace_name = tag_namespace_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Tag.
        The OCID of the tag definition.


        :return: The id of this Tag.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Tag.
        The OCID of the tag definition.


        :param id: The id of this Tag.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Tag.
        The name of the tag. The name must be unique across all tags in the namespace and can't be changed.


        :return: The name of this Tag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Tag.
        The name of the tag. The name must be unique across all tags in the namespace and can't be changed.


        :param name: The name of this Tag.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this Tag.
        The description you assign to the tag.


        :return: The description of this Tag.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Tag.
        The description you assign to the tag.


        :param description: The description of this Tag.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Tag.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Tag.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Tag.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Tag.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Tag.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}``

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Tag.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Tag.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}``

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Tag.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_retired(self):
        """
        **[Required]** Gets the is_retired of this Tag.
        Indicates whether the tag is retired.
        See `Retiring Key Definitions and Namespace Definitions`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/taggingoverview.htm#Retiring


        :return: The is_retired of this Tag.
        :rtype: bool
        """
        return self._is_retired

    @is_retired.setter
    def is_retired(self, is_retired):
        """
        Sets the is_retired of this Tag.
        Indicates whether the tag is retired.
        See `Retiring Key Definitions and Namespace Definitions`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/taggingoverview.htm#Retiring


        :param is_retired: The is_retired of this Tag.
        :type: bool
        """
        self._is_retired = is_retired

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Tag.
        Date and time the tag was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this Tag.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Tag.
        Date and time the tag was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this Tag.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def is_cost_tracking(self):
        """
        Gets the is_cost_tracking of this Tag.
        Indicates whether the tag is enabled for cost tracking.


        :return: The is_cost_tracking of this Tag.
        :rtype: bool
        """
        return self._is_cost_tracking

    @is_cost_tracking.setter
    def is_cost_tracking(self, is_cost_tracking):
        """
        Sets the is_cost_tracking of this Tag.
        Indicates whether the tag is enabled for cost tracking.


        :param is_cost_tracking: The is_cost_tracking of this Tag.
        :type: bool
        """
        self._is_cost_tracking = is_cost_tracking

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
