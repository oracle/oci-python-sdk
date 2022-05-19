# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SkillSummary(object):
    """
    Summary of a Skill.
    """

    #: A constant which can be used with the lifecycle_state property of a SkillSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SkillSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SkillSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SkillSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SkillSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SkillSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SkillSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_details property of a SkillSummary.
    #: This constant has a value of "PUBLISHED"
    LIFECYCLE_DETAILS_PUBLISHED = "PUBLISHED"

    #: A constant which can be used with the lifecycle_details property of a SkillSummary.
    #: This constant has a value of "DRAFT"
    LIFECYCLE_DETAILS_DRAFT = "DRAFT"

    def __init__(self, **kwargs):
        """
        Initializes a new SkillSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SkillSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this SkillSummary.
        :type name: str

        :param version:
            The value to assign to the version property of this SkillSummary.
        :type version: str

        :param display_name:
            The value to assign to the display_name property of this SkillSummary.
        :type display_name: str

        :param namespace:
            The value to assign to the namespace property of this SkillSummary.
        :type namespace: str

        :param category:
            The value to assign to the category property of this SkillSummary.
        :type category: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SkillSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SkillSummary.
            Allowed values for this property are: "PUBLISHED", "DRAFT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        :param platform_version:
            The value to assign to the platform_version property of this SkillSummary.
        :type platform_version: str

        :param time_created:
            The value to assign to the time_created property of this SkillSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SkillSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SkillSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SkillSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'version': 'str',
            'display_name': 'str',
            'namespace': 'str',
            'category': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'platform_version': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'version': 'version',
            'display_name': 'displayName',
            'namespace': 'namespace',
            'category': 'category',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'platform_version': 'platformVersion',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._name = None
        self._version = None
        self._display_name = None
        self._namespace = None
        self._category = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._platform_version = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SkillSummary.
        Unique immutable identifier that was assigned when the resource was created.


        :return: The id of this SkillSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SkillSummary.
        Unique immutable identifier that was assigned when the resource was created.


        :param id: The id of this SkillSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SkillSummary.
        The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.


        :return: The name of this SkillSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SkillSummary.
        The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.


        :param name: The name of this SkillSummary.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """
        **[Required]** Gets the version of this SkillSummary.
        The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces.  The version must begin with a letter or a number.


        :return: The version of this SkillSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SkillSummary.
        The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces.  The version must begin with a letter or a number.


        :param version: The version of this SkillSummary.
        :type: str
        """
        self._version = version

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SkillSummary.
        The resource's display name.


        :return: The display_name of this SkillSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SkillSummary.
        The resource's display name.


        :param display_name: The display_name of this SkillSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this SkillSummary.
        The resource's namespace.


        :return: The namespace of this SkillSummary.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this SkillSummary.
        The resource's namespace.


        :param namespace: The namespace of this SkillSummary.
        :type: str
        """
        self._namespace = namespace

    @property
    def category(self):
        """
        **[Required]** Gets the category of this SkillSummary.
        The resource's category.  This is used to group resource's together.


        :return: The category of this SkillSummary.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this SkillSummary.
        The resource's category.  This is used to group resource's together.


        :param category: The category of this SkillSummary.
        :type: str
        """
        self._category = category

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SkillSummary.
        The resource's current state.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SkillSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SkillSummary.
        The resource's current state.


        :param lifecycle_state: The lifecycle_state of this SkillSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        **[Required]** Gets the lifecycle_details of this SkillSummary.
        The resource's publish state.

        Allowed values for this property are: "PUBLISHED", "DRAFT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this SkillSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this SkillSummary.
        The resource's publish state.


        :param lifecycle_details: The lifecycle_details of this SkillSummary.
        :type: str
        """
        allowed_values = ["PUBLISHED", "DRAFT"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    @property
    def platform_version(self):
        """
        **[Required]** Gets the platform_version of this SkillSummary.
        The ODA Platform Version for this resource.


        :return: The platform_version of this SkillSummary.
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """
        Sets the platform_version of this SkillSummary.
        The ODA Platform Version for this resource.


        :param platform_version: The platform_version of this SkillSummary.
        :type: str
        """
        self._platform_version = platform_version

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SkillSummary.
        When the resource was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this SkillSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SkillSummary.
        When the resource was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this SkillSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this SkillSummary.
        When the resource was last updated. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this SkillSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SkillSummary.
        When the resource was last updated. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this SkillSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SkillSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this SkillSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SkillSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this SkillSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SkillSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this SkillSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SkillSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this SkillSummary.
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
