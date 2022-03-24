# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstallationSite(object):
    """
    Installation site of a Java Runtime.
    An installation site is a Java Runtime installed at a specific path on a managed instance.
    """

    #: A constant which can be used with the lifecycle_state property of a InstallationSite.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a InstallationSite.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a InstallationSite.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a InstallationSite.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a InstallationSite.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a InstallationSite.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a InstallationSite.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the managed_instance_type property of a InstallationSite.
    #: This constant has a value of "ORACLE_MANAGEMENT_AGENT"
    MANAGED_INSTANCE_TYPE_ORACLE_MANAGEMENT_AGENT = "ORACLE_MANAGEMENT_AGENT"

    def __init__(self, **kwargs):
        """
        Initializes a new InstallationSite object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param installation_key:
            The value to assign to the installation_key property of this InstallationSite.
        :type installation_key: str

        :param managed_instance_id:
            The value to assign to the managed_instance_id property of this InstallationSite.
        :type managed_instance_id: str

        :param jre:
            The value to assign to the jre property of this InstallationSite.
        :type jre: oci.jms.models.JavaRuntimeId

        :param path:
            The value to assign to the path property of this InstallationSite.
        :type path: str

        :param operating_system:
            The value to assign to the operating_system property of this InstallationSite.
        :type operating_system: oci.jms.models.OperatingSystem

        :param approximate_application_count:
            The value to assign to the approximate_application_count property of this InstallationSite.
        :type approximate_application_count: int

        :param time_last_seen:
            The value to assign to the time_last_seen property of this InstallationSite.
        :type time_last_seen: datetime

        :param blocklist:
            The value to assign to the blocklist property of this InstallationSite.
        :type blocklist: list[oci.jms.models.BlocklistEntry]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this InstallationSite.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param managed_instance_type:
            The value to assign to the managed_instance_type property of this InstallationSite.
            Allowed values for this property are: "ORACLE_MANAGEMENT_AGENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type managed_instance_type: str

        :param hostname:
            The value to assign to the hostname property of this InstallationSite.
        :type hostname: str

        """
        self.swagger_types = {
            'installation_key': 'str',
            'managed_instance_id': 'str',
            'jre': 'JavaRuntimeId',
            'path': 'str',
            'operating_system': 'OperatingSystem',
            'approximate_application_count': 'int',
            'time_last_seen': 'datetime',
            'blocklist': 'list[BlocklistEntry]',
            'lifecycle_state': 'str',
            'managed_instance_type': 'str',
            'hostname': 'str'
        }

        self.attribute_map = {
            'installation_key': 'installationKey',
            'managed_instance_id': 'managedInstanceId',
            'jre': 'jre',
            'path': 'path',
            'operating_system': 'operatingSystem',
            'approximate_application_count': 'approximateApplicationCount',
            'time_last_seen': 'timeLastSeen',
            'blocklist': 'blocklist',
            'lifecycle_state': 'lifecycleState',
            'managed_instance_type': 'managedInstanceType',
            'hostname': 'hostname'
        }

        self._installation_key = None
        self._managed_instance_id = None
        self._jre = None
        self._path = None
        self._operating_system = None
        self._approximate_application_count = None
        self._time_last_seen = None
        self._blocklist = None
        self._lifecycle_state = None
        self._managed_instance_type = None
        self._hostname = None

    @property
    def installation_key(self):
        """
        **[Required]** Gets the installation_key of this InstallationSite.
        The unique identifier for the installation of a Java Runtime at a specific path on a specific operating system.


        :return: The installation_key of this InstallationSite.
        :rtype: str
        """
        return self._installation_key

    @installation_key.setter
    def installation_key(self, installation_key):
        """
        Sets the installation_key of this InstallationSite.
        The unique identifier for the installation of a Java Runtime at a specific path on a specific operating system.


        :param installation_key: The installation_key of this InstallationSite.
        :type: str
        """
        self._installation_key = installation_key

    @property
    def managed_instance_id(self):
        """
        **[Required]** Gets the managed_instance_id of this InstallationSite.
        The `OCID`__ of the related managed instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_instance_id of this InstallationSite.
        :rtype: str
        """
        return self._managed_instance_id

    @managed_instance_id.setter
    def managed_instance_id(self, managed_instance_id):
        """
        Sets the managed_instance_id of this InstallationSite.
        The `OCID`__ of the related managed instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_instance_id: The managed_instance_id of this InstallationSite.
        :type: str
        """
        self._managed_instance_id = managed_instance_id

    @property
    def jre(self):
        """
        **[Required]** Gets the jre of this InstallationSite.

        :return: The jre of this InstallationSite.
        :rtype: oci.jms.models.JavaRuntimeId
        """
        return self._jre

    @jre.setter
    def jre(self, jre):
        """
        Sets the jre of this InstallationSite.

        :param jre: The jre of this InstallationSite.
        :type: oci.jms.models.JavaRuntimeId
        """
        self._jre = jre

    @property
    def path(self):
        """
        **[Required]** Gets the path of this InstallationSite.
        The file system path of the installation.


        :return: The path of this InstallationSite.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this InstallationSite.
        The file system path of the installation.


        :param path: The path of this InstallationSite.
        :type: str
        """
        self._path = path

    @property
    def operating_system(self):
        """
        **[Required]** Gets the operating_system of this InstallationSite.

        :return: The operating_system of this InstallationSite.
        :rtype: oci.jms.models.OperatingSystem
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this InstallationSite.

        :param operating_system: The operating_system of this InstallationSite.
        :type: oci.jms.models.OperatingSystem
        """
        self._operating_system = operating_system

    @property
    def approximate_application_count(self):
        """
        Gets the approximate_application_count of this InstallationSite.
        The approximate count of applications running on this installation


        :return: The approximate_application_count of this InstallationSite.
        :rtype: int
        """
        return self._approximate_application_count

    @approximate_application_count.setter
    def approximate_application_count(self, approximate_application_count):
        """
        Sets the approximate_application_count of this InstallationSite.
        The approximate count of applications running on this installation


        :param approximate_application_count: The approximate_application_count of this InstallationSite.
        :type: int
        """
        self._approximate_application_count = approximate_application_count

    @property
    def time_last_seen(self):
        """
        Gets the time_last_seen of this InstallationSite.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_last_seen of this InstallationSite.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this InstallationSite.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_last_seen: The time_last_seen of this InstallationSite.
        :type: datetime
        """
        self._time_last_seen = time_last_seen

    @property
    def blocklist(self):
        """
        Gets the blocklist of this InstallationSite.
        The list of operations that are blocklisted.


        :return: The blocklist of this InstallationSite.
        :rtype: list[oci.jms.models.BlocklistEntry]
        """
        return self._blocklist

    @blocklist.setter
    def blocklist(self, blocklist):
        """
        Sets the blocklist of this InstallationSite.
        The list of operations that are blocklisted.


        :param blocklist: The blocklist of this InstallationSite.
        :type: list[oci.jms.models.BlocklistEntry]
        """
        self._blocklist = blocklist

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this InstallationSite.
        The lifecycle state of the installation site.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this InstallationSite.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this InstallationSite.
        The lifecycle state of the installation site.


        :param lifecycle_state: The lifecycle_state of this InstallationSite.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def managed_instance_type(self):
        """
        Gets the managed_instance_type of this InstallationSite.
        The type of the source of events.

        Allowed values for this property are: "ORACLE_MANAGEMENT_AGENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The managed_instance_type of this InstallationSite.
        :rtype: str
        """
        return self._managed_instance_type

    @managed_instance_type.setter
    def managed_instance_type(self, managed_instance_type):
        """
        Sets the managed_instance_type of this InstallationSite.
        The type of the source of events.


        :param managed_instance_type: The managed_instance_type of this InstallationSite.
        :type: str
        """
        allowed_values = ["ORACLE_MANAGEMENT_AGENT"]
        if not value_allowed_none_or_none_sentinel(managed_instance_type, allowed_values):
            managed_instance_type = 'UNKNOWN_ENUM_VALUE'
        self._managed_instance_type = managed_instance_type

    @property
    def hostname(self):
        """
        Gets the hostname of this InstallationSite.
        The hostname of the managed instance (if applicable).


        :return: The hostname of this InstallationSite.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this InstallationSite.
        The hostname of the managed instance (if applicable).


        :param hostname: The hostname of this InstallationSite.
        :type: str
        """
        self._hostname = hostname

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
