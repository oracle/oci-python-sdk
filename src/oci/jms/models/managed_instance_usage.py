# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstanceUsage(object):
    """
    Managed instance usage during a specified time period.
    An entity that emits usage events to Java Management Service (JMS) is represented as a managed instance.
    A managed instance has a unique identity which is used by JMS to distinguish it from other managed instances.
    Currently, JMS supports only one kind of managed instance, a Management Agent.
    """

    #: A constant which can be used with the managed_instance_type property of a ManagedInstanceUsage.
    #: This constant has a value of "ORACLE_MANAGEMENT_AGENT"
    MANAGED_INSTANCE_TYPE_ORACLE_MANAGEMENT_AGENT = "ORACLE_MANAGEMENT_AGENT"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstanceUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param managed_instance_id:
            The value to assign to the managed_instance_id property of this ManagedInstanceUsage.
        :type managed_instance_id: str

        :param managed_instance_type:
            The value to assign to the managed_instance_type property of this ManagedInstanceUsage.
            Allowed values for this property are: "ORACLE_MANAGEMENT_AGENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type managed_instance_type: str

        :param hostname:
            The value to assign to the hostname property of this ManagedInstanceUsage.
        :type hostname: str

        :param host_id:
            The value to assign to the host_id property of this ManagedInstanceUsage.
        :type host_id: str

        :param operating_system:
            The value to assign to the operating_system property of this ManagedInstanceUsage.
        :type operating_system: oci.jms.models.OperatingSystem

        :param approximate_application_count:
            The value to assign to the approximate_application_count property of this ManagedInstanceUsage.
        :type approximate_application_count: int

        :param approximate_installation_count:
            The value to assign to the approximate_installation_count property of this ManagedInstanceUsage.
        :type approximate_installation_count: int

        :param approximate_jre_count:
            The value to assign to the approximate_jre_count property of this ManagedInstanceUsage.
        :type approximate_jre_count: int

        :param time_start:
            The value to assign to the time_start property of this ManagedInstanceUsage.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this ManagedInstanceUsage.
        :type time_end: datetime

        :param time_first_seen:
            The value to assign to the time_first_seen property of this ManagedInstanceUsage.
        :type time_first_seen: datetime

        :param time_last_seen:
            The value to assign to the time_last_seen property of this ManagedInstanceUsage.
        :type time_last_seen: datetime

        """
        self.swagger_types = {
            'managed_instance_id': 'str',
            'managed_instance_type': 'str',
            'hostname': 'str',
            'host_id': 'str',
            'operating_system': 'OperatingSystem',
            'approximate_application_count': 'int',
            'approximate_installation_count': 'int',
            'approximate_jre_count': 'int',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'time_first_seen': 'datetime',
            'time_last_seen': 'datetime'
        }

        self.attribute_map = {
            'managed_instance_id': 'managedInstanceId',
            'managed_instance_type': 'managedInstanceType',
            'hostname': 'hostname',
            'host_id': 'hostId',
            'operating_system': 'operatingSystem',
            'approximate_application_count': 'approximateApplicationCount',
            'approximate_installation_count': 'approximateInstallationCount',
            'approximate_jre_count': 'approximateJreCount',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'time_first_seen': 'timeFirstSeen',
            'time_last_seen': 'timeLastSeen'
        }

        self._managed_instance_id = None
        self._managed_instance_type = None
        self._hostname = None
        self._host_id = None
        self._operating_system = None
        self._approximate_application_count = None
        self._approximate_installation_count = None
        self._approximate_jre_count = None
        self._time_start = None
        self._time_end = None
        self._time_first_seen = None
        self._time_last_seen = None

    @property
    def managed_instance_id(self):
        """
        **[Required]** Gets the managed_instance_id of this ManagedInstanceUsage.
        The `OCID`__ of the related managed instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_instance_id of this ManagedInstanceUsage.
        :rtype: str
        """
        return self._managed_instance_id

    @managed_instance_id.setter
    def managed_instance_id(self, managed_instance_id):
        """
        Sets the managed_instance_id of this ManagedInstanceUsage.
        The `OCID`__ of the related managed instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_instance_id: The managed_instance_id of this ManagedInstanceUsage.
        :type: str
        """
        self._managed_instance_id = managed_instance_id

    @property
    def managed_instance_type(self):
        """
        **[Required]** Gets the managed_instance_type of this ManagedInstanceUsage.
        The type of the source of events.

        Allowed values for this property are: "ORACLE_MANAGEMENT_AGENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The managed_instance_type of this ManagedInstanceUsage.
        :rtype: str
        """
        return self._managed_instance_type

    @managed_instance_type.setter
    def managed_instance_type(self, managed_instance_type):
        """
        Sets the managed_instance_type of this ManagedInstanceUsage.
        The type of the source of events.


        :param managed_instance_type: The managed_instance_type of this ManagedInstanceUsage.
        :type: str
        """
        allowed_values = ["ORACLE_MANAGEMENT_AGENT"]
        if not value_allowed_none_or_none_sentinel(managed_instance_type, allowed_values):
            managed_instance_type = 'UNKNOWN_ENUM_VALUE'
        self._managed_instance_type = managed_instance_type

    @property
    def hostname(self):
        """
        Gets the hostname of this ManagedInstanceUsage.
        The hostname of the managed instance (if applicable).


        :return: The hostname of this ManagedInstanceUsage.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this ManagedInstanceUsage.
        The hostname of the managed instance (if applicable).


        :param hostname: The hostname of this ManagedInstanceUsage.
        :type: str
        """
        self._hostname = hostname

    @property
    def host_id(self):
        """
        Gets the host_id of this ManagedInstanceUsage.
        The host `OCID`__ of the related managed instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The host_id of this ManagedInstanceUsage.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """
        Sets the host_id of this ManagedInstanceUsage.
        The host `OCID`__ of the related managed instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param host_id: The host_id of this ManagedInstanceUsage.
        :type: str
        """
        self._host_id = host_id

    @property
    def operating_system(self):
        """
        Gets the operating_system of this ManagedInstanceUsage.

        :return: The operating_system of this ManagedInstanceUsage.
        :rtype: oci.jms.models.OperatingSystem
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this ManagedInstanceUsage.

        :param operating_system: The operating_system of this ManagedInstanceUsage.
        :type: oci.jms.models.OperatingSystem
        """
        self._operating_system = operating_system

    @property
    def approximate_application_count(self):
        """
        Gets the approximate_application_count of this ManagedInstanceUsage.
        The approximate count of applications reported by this managed instance.


        :return: The approximate_application_count of this ManagedInstanceUsage.
        :rtype: int
        """
        return self._approximate_application_count

    @approximate_application_count.setter
    def approximate_application_count(self, approximate_application_count):
        """
        Sets the approximate_application_count of this ManagedInstanceUsage.
        The approximate count of applications reported by this managed instance.


        :param approximate_application_count: The approximate_application_count of this ManagedInstanceUsage.
        :type: int
        """
        self._approximate_application_count = approximate_application_count

    @property
    def approximate_installation_count(self):
        """
        Gets the approximate_installation_count of this ManagedInstanceUsage.
        The approximate count of installations reported by this managed instance.


        :return: The approximate_installation_count of this ManagedInstanceUsage.
        :rtype: int
        """
        return self._approximate_installation_count

    @approximate_installation_count.setter
    def approximate_installation_count(self, approximate_installation_count):
        """
        Sets the approximate_installation_count of this ManagedInstanceUsage.
        The approximate count of installations reported by this managed instance.


        :param approximate_installation_count: The approximate_installation_count of this ManagedInstanceUsage.
        :type: int
        """
        self._approximate_installation_count = approximate_installation_count

    @property
    def approximate_jre_count(self):
        """
        Gets the approximate_jre_count of this ManagedInstanceUsage.
        The approximate count of Java Runtimes reported by this managed instance.


        :return: The approximate_jre_count of this ManagedInstanceUsage.
        :rtype: int
        """
        return self._approximate_jre_count

    @approximate_jre_count.setter
    def approximate_jre_count(self, approximate_jre_count):
        """
        Sets the approximate_jre_count of this ManagedInstanceUsage.
        The approximate count of Java Runtimes reported by this managed instance.


        :param approximate_jre_count: The approximate_jre_count of this ManagedInstanceUsage.
        :type: int
        """
        self._approximate_jre_count = approximate_jre_count

    @property
    def time_start(self):
        """
        Gets the time_start of this ManagedInstanceUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_start of this ManagedInstanceUsage.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this ManagedInstanceUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_start: The time_start of this ManagedInstanceUsage.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this ManagedInstanceUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_end of this ManagedInstanceUsage.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this ManagedInstanceUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_end: The time_end of this ManagedInstanceUsage.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def time_first_seen(self):
        """
        Gets the time_first_seen of this ManagedInstanceUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_first_seen of this ManagedInstanceUsage.
        :rtype: datetime
        """
        return self._time_first_seen

    @time_first_seen.setter
    def time_first_seen(self, time_first_seen):
        """
        Sets the time_first_seen of this ManagedInstanceUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_first_seen: The time_first_seen of this ManagedInstanceUsage.
        :type: datetime
        """
        self._time_first_seen = time_first_seen

    @property
    def time_last_seen(self):
        """
        Gets the time_last_seen of this ManagedInstanceUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_last_seen of this ManagedInstanceUsage.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this ManagedInstanceUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_last_seen: The time_last_seen of this ManagedInstanceUsage.
        :type: datetime
        """
        self._time_last_seen = time_last_seen

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
