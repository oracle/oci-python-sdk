# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogSavedSearchSummary(object):
    """
    A summary of a log saved search that can be used to save and share a given search result.
    """

    #: A constant which can be used with the lifecycle_state property of a LogSavedSearchSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a LogSavedSearchSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LogSavedSearchSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a LogSavedSearchSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LogSavedSearchSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a LogSavedSearchSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new LogSavedSearchSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this LogSavedSearchSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LogSavedSearchSummary.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this LogSavedSearchSummary.
        :type name: str

        :param time_created:
            The value to assign to the time_created property of this LogSavedSearchSummary.
        :type time_created: datetime

        :param time_last_modified:
            The value to assign to the time_last_modified property of this LogSavedSearchSummary.
        :type time_last_modified: datetime

        :param description:
            The value to assign to the description property of this LogSavedSearchSummary.
        :type description: str

        :param query:
            The value to assign to the query property of this LogSavedSearchSummary.
        :type query: str

        :param defined_tags:
            The value to assign to the defined_tags property of this LogSavedSearchSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LogSavedSearchSummary.
        :type freeform_tags: dict(str, str)

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LogSavedSearchSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "INACTIVE", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'time_created': 'datetime',
            'time_last_modified': 'datetime',
            'description': 'str',
            'query': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'time_created': 'timeCreated',
            'time_last_modified': 'timeLastModified',
            'description': 'description',
            'query': 'query',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._time_created = None
        self._time_last_modified = None
        self._description = None
        self._query = None
        self._defined_tags = None
        self._freeform_tags = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this LogSavedSearchSummary.
        The OCID of the resource.


        :return: The id of this LogSavedSearchSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LogSavedSearchSummary.
        The OCID of the resource.


        :param id: The id of this LogSavedSearchSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LogSavedSearchSummary.
        The OCID of the compartment that the resource belongs to.


        :return: The compartment_id of this LogSavedSearchSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LogSavedSearchSummary.
        The OCID of the compartment that the resource belongs to.


        :param compartment_id: The compartment_id of this LogSavedSearchSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this LogSavedSearchSummary.
        The user-friendly display name. This must be unique within the enclosing resource,
        and it's changeable. Avoid entering confidential information.


        :return: The name of this LogSavedSearchSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogSavedSearchSummary.
        The user-friendly display name. This must be unique within the enclosing resource,
        and it's changeable. Avoid entering confidential information.


        :param name: The name of this LogSavedSearchSummary.
        :type: str
        """
        self._name = name

    @property
    def time_created(self):
        """
        Gets the time_created of this LogSavedSearchSummary.
        Time the resource was created.


        :return: The time_created of this LogSavedSearchSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LogSavedSearchSummary.
        Time the resource was created.


        :param time_created: The time_created of this LogSavedSearchSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_last_modified(self):
        """
        Gets the time_last_modified of this LogSavedSearchSummary.
        Time the resource was last modified.


        :return: The time_last_modified of this LogSavedSearchSummary.
        :rtype: datetime
        """
        return self._time_last_modified

    @time_last_modified.setter
    def time_last_modified(self, time_last_modified):
        """
        Sets the time_last_modified of this LogSavedSearchSummary.
        Time the resource was last modified.


        :param time_last_modified: The time_last_modified of this LogSavedSearchSummary.
        :type: datetime
        """
        self._time_last_modified = time_last_modified

    @property
    def description(self):
        """
        Gets the description of this LogSavedSearchSummary.
        Description for this resource.


        :return: The description of this LogSavedSearchSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogSavedSearchSummary.
        Description for this resource.


        :param description: The description of this LogSavedSearchSummary.
        :type: str
        """
        self._description = description

    @property
    def query(self):
        """
        Gets the query of this LogSavedSearchSummary.
        The search query that is saved.


        :return: The query of this LogSavedSearchSummary.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this LogSavedSearchSummary.
        The search query that is saved.


        :param query: The query of this LogSavedSearchSummary.
        :type: str
        """
        self._query = query

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this LogSavedSearchSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this LogSavedSearchSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this LogSavedSearchSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this LogSavedSearchSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this LogSavedSearchSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this LogSavedSearchSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this LogSavedSearchSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this LogSavedSearchSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this LogSavedSearchSummary.
        The state of the LogSavedSearch

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "INACTIVE", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LogSavedSearchSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LogSavedSearchSummary.
        The state of the LogSavedSearch


        :param lifecycle_state: The lifecycle_state of this LogSavedSearchSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "INACTIVE", "DELETING", "FAILED"]
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
