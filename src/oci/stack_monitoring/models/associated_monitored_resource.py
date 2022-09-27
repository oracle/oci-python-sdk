# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociatedMonitoredResource(object):
    """
    The information about monitored resource.
    """

    #: A constant which can be used with the lifecycle_state property of a AssociatedMonitoredResource.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AssociatedMonitoredResource.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AssociatedMonitoredResource.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AssociatedMonitoredResource.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AssociatedMonitoredResource.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AssociatedMonitoredResource.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AssociatedMonitoredResource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AssociatedMonitoredResource.
        :type id: str

        :param name:
            The value to assign to the name property of this AssociatedMonitoredResource.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this AssociatedMonitoredResource.
        :type display_name: str

        :param type:
            The value to assign to the type property of this AssociatedMonitoredResource.
        :type type: str

        :param host_name:
            The value to assign to the host_name property of this AssociatedMonitoredResource.
        :type host_name: str

        :param external_id:
            The value to assign to the external_id property of this AssociatedMonitoredResource.
        :type external_id: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this AssociatedMonitoredResource.
        :type management_agent_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AssociatedMonitoredResource.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param association:
            The value to assign to the association property of this AssociatedMonitoredResource.
        :type association: object

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'display_name': 'str',
            'type': 'str',
            'host_name': 'str',
            'external_id': 'str',
            'management_agent_id': 'str',
            'lifecycle_state': 'str',
            'association': 'object'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'display_name': 'displayName',
            'type': 'type',
            'host_name': 'hostName',
            'external_id': 'externalId',
            'management_agent_id': 'managementAgentId',
            'lifecycle_state': 'lifecycleState',
            'association': 'association'
        }

        self._id = None
        self._name = None
        self._display_name = None
        self._type = None
        self._host_name = None
        self._external_id = None
        self._management_agent_id = None
        self._lifecycle_state = None
        self._association = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AssociatedMonitoredResource.
        The `OCID`__ of monitored resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AssociatedMonitoredResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AssociatedMonitoredResource.
        The `OCID`__ of monitored resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AssociatedMonitoredResource.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this AssociatedMonitoredResource.
        Name of the monitored resource


        :return: The name of this AssociatedMonitoredResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AssociatedMonitoredResource.
        Name of the monitored resource


        :param name: The name of this AssociatedMonitoredResource.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this AssociatedMonitoredResource.
        Monitored resource display name.


        :return: The display_name of this AssociatedMonitoredResource.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AssociatedMonitoredResource.
        Monitored resource display name.


        :param display_name: The display_name of this AssociatedMonitoredResource.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        Gets the type of this AssociatedMonitoredResource.
        Type of the monitored resource


        :return: The type of this AssociatedMonitoredResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AssociatedMonitoredResource.
        Type of the monitored resource


        :param type: The type of this AssociatedMonitoredResource.
        :type: str
        """
        self._type = type

    @property
    def host_name(self):
        """
        Gets the host_name of this AssociatedMonitoredResource.
        Resource Host Name


        :return: The host_name of this AssociatedMonitoredResource.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this AssociatedMonitoredResource.
        Resource Host Name


        :param host_name: The host_name of this AssociatedMonitoredResource.
        :type: str
        """
        self._host_name = host_name

    @property
    def external_id(self):
        """
        Gets the external_id of this AssociatedMonitoredResource.
        External resource is any OCI resource identifier `OCID`__
        which is not a Stack Monitoring service resource.
        Currently supports only following resource type identifiers - externalcontainerdatabase,
        externalnoncontainerdatabase, externalpluggabledatabase and OCI compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_id of this AssociatedMonitoredResource.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this AssociatedMonitoredResource.
        External resource is any OCI resource identifier `OCID`__
        which is not a Stack Monitoring service resource.
        Currently supports only following resource type identifiers - externalcontainerdatabase,
        externalnoncontainerdatabase, externalpluggabledatabase and OCI compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_id: The external_id of this AssociatedMonitoredResource.
        :type: str
        """
        self._external_id = external_id

    @property
    def management_agent_id(self):
        """
        Gets the management_agent_id of this AssociatedMonitoredResource.
        Management Agent Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this AssociatedMonitoredResource.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this AssociatedMonitoredResource.
        Management Agent Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this AssociatedMonitoredResource.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AssociatedMonitoredResource.
        The current state of the monitored resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AssociatedMonitoredResource.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AssociatedMonitoredResource.
        The current state of the monitored resource.


        :param lifecycle_state: The lifecycle_state of this AssociatedMonitoredResource.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def association(self):
        """
        Gets the association of this AssociatedMonitoredResource.
        Association details of the resource


        :return: The association of this AssociatedMonitoredResource.
        :rtype: object
        """
        return self._association

    @association.setter
    def association(self, association):
        """
        Sets the association of this AssociatedMonitoredResource.
        Association details of the resource


        :param association: The association of this AssociatedMonitoredResource.
        :type: object
        """
        self._association = association

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
