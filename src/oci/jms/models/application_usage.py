# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplicationUsage(object):
    """
    Application usage during a specified time period.
    An application is a Java application that can be executed by a Java Runtime installation.
    An application is independent of the Java Runtime or its installation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApplicationUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param application_id:
            The value to assign to the application_id property of this ApplicationUsage.
        :type application_id: str

        :param display_name:
            The value to assign to the display_name property of this ApplicationUsage.
        :type display_name: str

        :param application_type:
            The value to assign to the application_type property of this ApplicationUsage.
        :type application_type: str

        :param operating_systems:
            The value to assign to the operating_systems property of this ApplicationUsage.
        :type operating_systems: list[oci.jms.models.OperatingSystem]

        :param approximate_installation_count:
            The value to assign to the approximate_installation_count property of this ApplicationUsage.
        :type approximate_installation_count: int

        :param approximate_jre_count:
            The value to assign to the approximate_jre_count property of this ApplicationUsage.
        :type approximate_jre_count: int

        :param approximate_managed_instance_count:
            The value to assign to the approximate_managed_instance_count property of this ApplicationUsage.
        :type approximate_managed_instance_count: int

        :param time_start:
            The value to assign to the time_start property of this ApplicationUsage.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this ApplicationUsage.
        :type time_end: datetime

        :param time_first_seen:
            The value to assign to the time_first_seen property of this ApplicationUsage.
        :type time_first_seen: datetime

        :param time_last_seen:
            The value to assign to the time_last_seen property of this ApplicationUsage.
        :type time_last_seen: datetime

        """
        self.swagger_types = {
            'application_id': 'str',
            'display_name': 'str',
            'application_type': 'str',
            'operating_systems': 'list[OperatingSystem]',
            'approximate_installation_count': 'int',
            'approximate_jre_count': 'int',
            'approximate_managed_instance_count': 'int',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'time_first_seen': 'datetime',
            'time_last_seen': 'datetime'
        }

        self.attribute_map = {
            'application_id': 'applicationId',
            'display_name': 'displayName',
            'application_type': 'applicationType',
            'operating_systems': 'operatingSystems',
            'approximate_installation_count': 'approximateInstallationCount',
            'approximate_jre_count': 'approximateJreCount',
            'approximate_managed_instance_count': 'approximateManagedInstanceCount',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'time_first_seen': 'timeFirstSeen',
            'time_last_seen': 'timeLastSeen'
        }

        self._application_id = None
        self._display_name = None
        self._application_type = None
        self._operating_systems = None
        self._approximate_installation_count = None
        self._approximate_jre_count = None
        self._approximate_managed_instance_count = None
        self._time_start = None
        self._time_end = None
        self._time_first_seen = None
        self._time_last_seen = None

    @property
    def application_id(self):
        """
        **[Required]** Gets the application_id of this ApplicationUsage.
        An internal identifier for the application that is unique to a Fleet.


        :return: The application_id of this ApplicationUsage.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """
        Sets the application_id of this ApplicationUsage.
        An internal identifier for the application that is unique to a Fleet.


        :param application_id: The application_id of this ApplicationUsage.
        :type: str
        """
        self._application_id = application_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ApplicationUsage.
        The name of the application.


        :return: The display_name of this ApplicationUsage.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApplicationUsage.
        The name of the application.


        :param display_name: The display_name of this ApplicationUsage.
        :type: str
        """
        self._display_name = display_name

    @property
    def application_type(self):
        """
        **[Required]** Gets the application_type of this ApplicationUsage.
        The type of the application, denoted by how the application was started.


        :return: The application_type of this ApplicationUsage.
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """
        Sets the application_type of this ApplicationUsage.
        The type of the application, denoted by how the application was started.


        :param application_type: The application_type of this ApplicationUsage.
        :type: str
        """
        self._application_type = application_type

    @property
    def operating_systems(self):
        """
        Gets the operating_systems of this ApplicationUsage.
        The operating systems running this application.


        :return: The operating_systems of this ApplicationUsage.
        :rtype: list[oci.jms.models.OperatingSystem]
        """
        return self._operating_systems

    @operating_systems.setter
    def operating_systems(self, operating_systems):
        """
        Sets the operating_systems of this ApplicationUsage.
        The operating systems running this application.


        :param operating_systems: The operating_systems of this ApplicationUsage.
        :type: list[oci.jms.models.OperatingSystem]
        """
        self._operating_systems = operating_systems

    @property
    def approximate_installation_count(self):
        """
        Gets the approximate_installation_count of this ApplicationUsage.
        The approximate count of installations running this application.


        :return: The approximate_installation_count of this ApplicationUsage.
        :rtype: int
        """
        return self._approximate_installation_count

    @approximate_installation_count.setter
    def approximate_installation_count(self, approximate_installation_count):
        """
        Sets the approximate_installation_count of this ApplicationUsage.
        The approximate count of installations running this application.


        :param approximate_installation_count: The approximate_installation_count of this ApplicationUsage.
        :type: int
        """
        self._approximate_installation_count = approximate_installation_count

    @property
    def approximate_jre_count(self):
        """
        Gets the approximate_jre_count of this ApplicationUsage.
        The approximate count of Java Runtimes running this application.


        :return: The approximate_jre_count of this ApplicationUsage.
        :rtype: int
        """
        return self._approximate_jre_count

    @approximate_jre_count.setter
    def approximate_jre_count(self, approximate_jre_count):
        """
        Sets the approximate_jre_count of this ApplicationUsage.
        The approximate count of Java Runtimes running this application.


        :param approximate_jre_count: The approximate_jre_count of this ApplicationUsage.
        :type: int
        """
        self._approximate_jre_count = approximate_jre_count

    @property
    def approximate_managed_instance_count(self):
        """
        Gets the approximate_managed_instance_count of this ApplicationUsage.
        The approximate count of managed instances reporting this application.


        :return: The approximate_managed_instance_count of this ApplicationUsage.
        :rtype: int
        """
        return self._approximate_managed_instance_count

    @approximate_managed_instance_count.setter
    def approximate_managed_instance_count(self, approximate_managed_instance_count):
        """
        Sets the approximate_managed_instance_count of this ApplicationUsage.
        The approximate count of managed instances reporting this application.


        :param approximate_managed_instance_count: The approximate_managed_instance_count of this ApplicationUsage.
        :type: int
        """
        self._approximate_managed_instance_count = approximate_managed_instance_count

    @property
    def time_start(self):
        """
        Gets the time_start of this ApplicationUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_start of this ApplicationUsage.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this ApplicationUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_start: The time_start of this ApplicationUsage.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this ApplicationUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_end of this ApplicationUsage.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this ApplicationUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_end: The time_end of this ApplicationUsage.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def time_first_seen(self):
        """
        Gets the time_first_seen of this ApplicationUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_first_seen of this ApplicationUsage.
        :rtype: datetime
        """
        return self._time_first_seen

    @time_first_seen.setter
    def time_first_seen(self, time_first_seen):
        """
        Sets the time_first_seen of this ApplicationUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_first_seen: The time_first_seen of this ApplicationUsage.
        :type: datetime
        """
        self._time_first_seen = time_first_seen

    @property
    def time_last_seen(self):
        """
        Gets the time_last_seen of this ApplicationUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_last_seen of this ApplicationUsage.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this ApplicationUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_last_seen: The time_last_seen of this ApplicationUsage.
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
