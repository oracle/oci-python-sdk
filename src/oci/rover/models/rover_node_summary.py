# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverNodeSummary(object):
    """
    Summary of the RoverNode.
    """

    #: A constant which can be used with the lifecycle_state property of a RoverNodeSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a RoverNodeSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a RoverNodeSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RoverNodeSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a RoverNodeSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a RoverNodeSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new RoverNodeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RoverNodeSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RoverNodeSummary.
        :type compartment_id: str

        :param cluster_id:
            The value to assign to the cluster_id property of this RoverNodeSummary.
        :type cluster_id: str

        :param serial_number:
            The value to assign to the serial_number property of this RoverNodeSummary.
        :type serial_number: str

        :param display_name:
            The value to assign to the display_name property of this RoverNodeSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this RoverNodeSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RoverNodeSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this RoverNodeSummary.
        :type lifecycle_state_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RoverNodeSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RoverNodeSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this RoverNodeSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'cluster_id': 'str',
            'serial_number': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'cluster_id': 'clusterId',
            'serial_number': 'serialNumber',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._cluster_id = None
        self._serial_number = None
        self._display_name = None
        self._time_created = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RoverNodeSummary.
        The OCID of the RoverNode.


        :return: The id of this RoverNodeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RoverNodeSummary.
        The OCID of the RoverNode.


        :param id: The id of this RoverNodeSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RoverNodeSummary.
        The OCID of the compartment containing the RoverNode.


        :return: The compartment_id of this RoverNodeSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RoverNodeSummary.
        The OCID of the compartment containing the RoverNode.


        :param compartment_id: The compartment_id of this RoverNodeSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cluster_id(self):
        """
        Gets the cluster_id of this RoverNodeSummary.
        The cluster ID if the node is part of a cluster.


        :return: The cluster_id of this RoverNodeSummary.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this RoverNodeSummary.
        The cluster ID if the node is part of a cluster.


        :param cluster_id: The cluster_id of this RoverNodeSummary.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def serial_number(self):
        """
        Gets the serial_number of this RoverNodeSummary.
        Serial number of the node.


        :return: The serial_number of this RoverNodeSummary.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this RoverNodeSummary.
        Serial number of the node.


        :param serial_number: The serial_number of this RoverNodeSummary.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def display_name(self):
        """
        Gets the display_name of this RoverNodeSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this RoverNodeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RoverNodeSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this RoverNodeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this RoverNodeSummary.
        The time the the RoverNode was created. An RFC3339 formatted datetime string


        :return: The time_created of this RoverNodeSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RoverNodeSummary.
        The time the the RoverNode was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this RoverNodeSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this RoverNodeSummary.
        The current state of the RoverNode.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RoverNodeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RoverNodeSummary.
        The current state of the RoverNode.


        :param lifecycle_state: The lifecycle_state of this RoverNodeSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_state_details(self):
        """
        Gets the lifecycle_state_details of this RoverNodeSummary.
        A property that can contain details on the lifecycle.


        :return: The lifecycle_state_details of this RoverNodeSummary.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this RoverNodeSummary.
        A property that can contain details on the lifecycle.


        :param lifecycle_state_details: The lifecycle_state_details of this RoverNodeSummary.
        :type: str
        """
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this RoverNodeSummary.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this RoverNodeSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RoverNodeSummary.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this RoverNodeSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this RoverNodeSummary.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this RoverNodeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RoverNodeSummary.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this RoverNodeSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this RoverNodeSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this RoverNodeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this RoverNodeSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this RoverNodeSummary.
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
