# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceConnector(object):
    """
    The configuration details of the flow defined by the service connector.
    For more information about flows defined by service connectors, see
    `Service Connector Hub Overview`__.

    __ https://docs.cloud.oracle.com/iaas/Content/service-connector-hub/overview.htm
    """

    #: A constant which can be used with the lifecycle_state property of a ServiceConnector.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ServiceConnector.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ServiceConnector.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ServiceConnector.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ServiceConnector.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ServiceConnector.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ServiceConnector.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceConnector object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ServiceConnector.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ServiceConnector.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ServiceConnector.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ServiceConnector.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this ServiceConnector.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ServiceConnector.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ServiceConnector.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecyle_details:
            The value to assign to the lifecyle_details property of this ServiceConnector.
        :type lifecyle_details: str

        :param source:
            The value to assign to the source property of this ServiceConnector.
        :type source: oci.sch.models.SourceDetails

        :param tasks:
            The value to assign to the tasks property of this ServiceConnector.
        :type tasks: list[oci.sch.models.TaskDetails]

        :param target:
            The value to assign to the target property of this ServiceConnector.
        :type target: oci.sch.models.TargetDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ServiceConnector.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ServiceConnector.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ServiceConnector.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecyle_details': 'str',
            'source': 'SourceDetails',
            'tasks': 'list[TaskDetails]',
            'target': 'TargetDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecyle_details': 'lifecyleDetails',
            'source': 'source',
            'tasks': 'tasks',
            'target': 'target',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecyle_details = None
        self._source = None
        self._tasks = None
        self._target = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ServiceConnector.
        The `OCID`__ of the service connector.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ServiceConnector.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ServiceConnector.
        The `OCID`__ of the service connector.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ServiceConnector.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ServiceConnector.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this ServiceConnector.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ServiceConnector.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this ServiceConnector.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ServiceConnector.
        The description of the resource. Avoid entering confidential information.


        :return: The description of this ServiceConnector.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ServiceConnector.
        The description of the resource. Avoid entering confidential information.


        :param description: The description of this ServiceConnector.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ServiceConnector.
        The `OCID`__ of the compartment containing the service connector.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ServiceConnector.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ServiceConnector.
        The `OCID`__ of the compartment containing the service connector.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ServiceConnector.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ServiceConnector.
        The date and time when the service connector was created.
        Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ServiceConnector.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ServiceConnector.
        The date and time when the service connector was created.
        Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ServiceConnector.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ServiceConnector.
        The date and time when the service connector was updated.
        Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ServiceConnector.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ServiceConnector.
        The date and time when the service connector was updated.
        Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ServiceConnector.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ServiceConnector.
        The current state of the service connector.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ServiceConnector.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ServiceConnector.
        The current state of the service connector.


        :param lifecycle_state: The lifecycle_state of this ServiceConnector.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecyle_details(self):
        """
        Gets the lifecyle_details of this ServiceConnector.
        A message describing the current state in more detail.
        For example, the message might provide actionable
        information for a resource in a `FAILED` state.


        :return: The lifecyle_details of this ServiceConnector.
        :rtype: str
        """
        return self._lifecyle_details

    @lifecyle_details.setter
    def lifecyle_details(self, lifecyle_details):
        """
        Sets the lifecyle_details of this ServiceConnector.
        A message describing the current state in more detail.
        For example, the message might provide actionable
        information for a resource in a `FAILED` state.


        :param lifecyle_details: The lifecyle_details of this ServiceConnector.
        :type: str
        """
        self._lifecyle_details = lifecyle_details

    @property
    def source(self):
        """
        Gets the source of this ServiceConnector.

        :return: The source of this ServiceConnector.
        :rtype: oci.sch.models.SourceDetails
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this ServiceConnector.

        :param source: The source of this ServiceConnector.
        :type: oci.sch.models.SourceDetails
        """
        self._source = source

    @property
    def tasks(self):
        """
        Gets the tasks of this ServiceConnector.
        The list of tasks.


        :return: The tasks of this ServiceConnector.
        :rtype: list[oci.sch.models.TaskDetails]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """
        Sets the tasks of this ServiceConnector.
        The list of tasks.


        :param tasks: The tasks of this ServiceConnector.
        :type: list[oci.sch.models.TaskDetails]
        """
        self._tasks = tasks

    @property
    def target(self):
        """
        Gets the target of this ServiceConnector.

        :return: The target of this ServiceConnector.
        :rtype: oci.sch.models.TargetDetails
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this ServiceConnector.

        :param target: The target of this ServiceConnector.
        :type: oci.sch.models.TargetDetails
        """
        self._target = target

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ServiceConnector.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ServiceConnector.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ServiceConnector.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ServiceConnector.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ServiceConnector.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ServiceConnector.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ServiceConnector.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ServiceConnector.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ServiceConnector.
        The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ServiceConnector.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ServiceConnector.
        The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ServiceConnector.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
