# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Replica(object):
    """
    A DB System read replica.
    """

    #: A constant which can be used with the lifecycle_state property of a Replica.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Replica.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Replica.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Replica.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Replica.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Replica.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Replica.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a Replica.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Replica object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Replica.
        :type id: str

        :param db_system_id:
            The value to assign to the db_system_id property of this Replica.
        :type db_system_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Replica.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this Replica.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Replica.
        :type description: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Replica.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Replica.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this Replica.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Replica.
        :type time_updated: datetime

        :param mysql_version:
            The value to assign to the mysql_version property of this Replica.
        :type mysql_version: str

        :param availability_domain:
            The value to assign to the availability_domain property of this Replica.
        :type availability_domain: str

        :param fault_domain:
            The value to assign to the fault_domain property of this Replica.
        :type fault_domain: str

        :param ip_address:
            The value to assign to the ip_address property of this Replica.
        :type ip_address: str

        :param port:
            The value to assign to the port property of this Replica.
        :type port: int

        :param port_x:
            The value to assign to the port_x property of this Replica.
        :type port_x: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Replica.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Replica.
        :type defined_tags: dict(str, dict(str, object))

        :param is_delete_protected:
            The value to assign to the is_delete_protected property of this Replica.
        :type is_delete_protected: bool

        """
        self.swagger_types = {
            'id': 'str',
            'db_system_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'mysql_version': 'str',
            'availability_domain': 'str',
            'fault_domain': 'str',
            'ip_address': 'str',
            'port': 'int',
            'port_x': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_delete_protected': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'db_system_id': 'dbSystemId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'mysql_version': 'mysqlVersion',
            'availability_domain': 'availabilityDomain',
            'fault_domain': 'faultDomain',
            'ip_address': 'ipAddress',
            'port': 'port',
            'port_x': 'portX',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_delete_protected': 'isDeleteProtected'
        }

        self._id = None
        self._db_system_id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._mysql_version = None
        self._availability_domain = None
        self._fault_domain = None
        self._ip_address = None
        self._port = None
        self._port_x = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_delete_protected = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Replica.
        The OCID of the read replica.


        :return: The id of this Replica.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Replica.
        The OCID of the read replica.


        :param id: The id of this Replica.
        :type: str
        """
        self._id = id

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this Replica.
        The OCID of the DB System the read replica is associated with.


        :return: The db_system_id of this Replica.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this Replica.
        The OCID of the DB System the read replica is associated with.


        :param db_system_id: The db_system_id of this Replica.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Replica.
        The OCID of the compartment that contains the read replica.


        :return: The compartment_id of this Replica.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Replica.
        The OCID of the compartment that contains the read replica.


        :param compartment_id: The compartment_id of this Replica.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Replica.
        The user-friendly name for the read replica. It does not have to be unique.


        :return: The display_name of this Replica.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Replica.
        The user-friendly name for the read replica. It does not have to be unique.


        :param display_name: The display_name of this Replica.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Replica.
        User provided description of the read replica.


        :return: The description of this Replica.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Replica.
        User provided description of the read replica.


        :param description: The description of this Replica.
        :type: str
        """
        self._description = description

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Replica.
        The state of the read replica.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Replica.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Replica.
        The state of the read replica.


        :param lifecycle_state: The lifecycle_state of this Replica.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Replica.
        A message describing the state of the read replica.


        :return: The lifecycle_details of this Replica.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Replica.
        A message describing the state of the read replica.


        :param lifecycle_details: The lifecycle_details of this Replica.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Replica.
        The date and time the read replica was created, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this Replica.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Replica.
        The date and time the read replica was created, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this Replica.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Replica.
        The time the read replica was last updated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this Replica.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Replica.
        The time the read replica was last updated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this Replica.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def mysql_version(self):
        """
        **[Required]** Gets the mysql_version of this Replica.
        The MySQL version used by the read replica.


        :return: The mysql_version of this Replica.
        :rtype: str
        """
        return self._mysql_version

    @mysql_version.setter
    def mysql_version(self, mysql_version):
        """
        Sets the mysql_version of this Replica.
        The MySQL version used by the read replica.


        :param mysql_version: The mysql_version of this Replica.
        :type: str
        """
        self._mysql_version = mysql_version

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this Replica.
        The name of the Availability Domain the read replica is located in.


        :return: The availability_domain of this Replica.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Replica.
        The name of the Availability Domain the read replica is located in.


        :param availability_domain: The availability_domain of this Replica.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this Replica.
        The name of the Fault Domain the read replica is located in.


        :return: The fault_domain of this Replica.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this Replica.
        The name of the Fault Domain the read replica is located in.


        :param fault_domain: The fault_domain of this Replica.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this Replica.
        The IP address the read replica is configured to listen on.


        :return: The ip_address of this Replica.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Replica.
        The IP address the read replica is configured to listen on.


        :param ip_address: The ip_address of this Replica.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def port(self):
        """
        **[Required]** Gets the port of this Replica.
        The port the read replica is configured to listen on.


        :return: The port of this Replica.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this Replica.
        The port the read replica is configured to listen on.


        :param port: The port of this Replica.
        :type: int
        """
        self._port = port

    @property
    def port_x(self):
        """
        **[Required]** Gets the port_x of this Replica.
        The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.


        :return: The port_x of this Replica.
        :rtype: int
        """
        return self._port_x

    @port_x.setter
    def port_x(self, port_x):
        """
        Sets the port_x of this Replica.
        The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.


        :param port_x: The port_x of this Replica.
        :type: int
        """
        self._port_x = port_x

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Replica.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Replica.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Replica.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Replica.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Replica.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Replica.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Replica.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Replica.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_delete_protected(self):
        """
        Gets the is_delete_protected of this Replica.
        Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow.
        Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If
        the DB System is delete protected, read replicas can still be deleted individually if they are not delete
        protected themselves.


        :return: The is_delete_protected of this Replica.
        :rtype: bool
        """
        return self._is_delete_protected

    @is_delete_protected.setter
    def is_delete_protected(self, is_delete_protected):
        """
        Sets the is_delete_protected of this Replica.
        Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow.
        Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If
        the DB System is delete protected, read replicas can still be deleted individually if they are not delete
        protected themselves.


        :param is_delete_protected: The is_delete_protected of this Replica.
        :type: bool
        """
        self._is_delete_protected = is_delete_protected

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
