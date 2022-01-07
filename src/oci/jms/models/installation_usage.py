# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstallationUsage(object):
    """
    Installation usage during a specified time period.
    An installation is a collection of deployed instances of a specific Java Runtime that share the same install path.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstallationUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param jre_vendor:
            The value to assign to the jre_vendor property of this InstallationUsage.
        :type jre_vendor: str

        :param jre_distribution:
            The value to assign to the jre_distribution property of this InstallationUsage.
        :type jre_distribution: str

        :param jre_version:
            The value to assign to the jre_version property of this InstallationUsage.
        :type jre_version: str

        :param path:
            The value to assign to the path property of this InstallationUsage.
        :type path: str

        :param os:
            The value to assign to the os property of this InstallationUsage.
        :type os: str

        :param architecture:
            The value to assign to the architecture property of this InstallationUsage.
        :type architecture: str

        :param operating_system:
            The value to assign to the operating_system property of this InstallationUsage.
        :type operating_system: oci.jms.models.OperatingSystem

        :param approximate_application_count:
            The value to assign to the approximate_application_count property of this InstallationUsage.
        :type approximate_application_count: int

        :param approximate_managed_instance_count:
            The value to assign to the approximate_managed_instance_count property of this InstallationUsage.
        :type approximate_managed_instance_count: int

        :param time_start:
            The value to assign to the time_start property of this InstallationUsage.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this InstallationUsage.
        :type time_end: datetime

        :param time_first_seen:
            The value to assign to the time_first_seen property of this InstallationUsage.
        :type time_first_seen: datetime

        :param time_last_seen:
            The value to assign to the time_last_seen property of this InstallationUsage.
        :type time_last_seen: datetime

        """
        self.swagger_types = {
            'jre_vendor': 'str',
            'jre_distribution': 'str',
            'jre_version': 'str',
            'path': 'str',
            'os': 'str',
            'architecture': 'str',
            'operating_system': 'OperatingSystem',
            'approximate_application_count': 'int',
            'approximate_managed_instance_count': 'int',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'time_first_seen': 'datetime',
            'time_last_seen': 'datetime'
        }

        self.attribute_map = {
            'jre_vendor': 'jreVendor',
            'jre_distribution': 'jreDistribution',
            'jre_version': 'jreVersion',
            'path': 'path',
            'os': 'os',
            'architecture': 'architecture',
            'operating_system': 'operatingSystem',
            'approximate_application_count': 'approximateApplicationCount',
            'approximate_managed_instance_count': 'approximateManagedInstanceCount',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'time_first_seen': 'timeFirstSeen',
            'time_last_seen': 'timeLastSeen'
        }

        self._jre_vendor = None
        self._jre_distribution = None
        self._jre_version = None
        self._path = None
        self._os = None
        self._architecture = None
        self._operating_system = None
        self._approximate_application_count = None
        self._approximate_managed_instance_count = None
        self._time_start = None
        self._time_end = None
        self._time_first_seen = None
        self._time_last_seen = None

    @property
    def jre_vendor(self):
        """
        **[Required]** Gets the jre_vendor of this InstallationUsage.
        The vendor of the Java Runtime that is deployed with the installation.


        :return: The jre_vendor of this InstallationUsage.
        :rtype: str
        """
        return self._jre_vendor

    @jre_vendor.setter
    def jre_vendor(self, jre_vendor):
        """
        Sets the jre_vendor of this InstallationUsage.
        The vendor of the Java Runtime that is deployed with the installation.


        :param jre_vendor: The jre_vendor of this InstallationUsage.
        :type: str
        """
        self._jre_vendor = jre_vendor

    @property
    def jre_distribution(self):
        """
        **[Required]** Gets the jre_distribution of this InstallationUsage.
        The distribution of the Java Runtime that is deployed with the installation.


        :return: The jre_distribution of this InstallationUsage.
        :rtype: str
        """
        return self._jre_distribution

    @jre_distribution.setter
    def jre_distribution(self, jre_distribution):
        """
        Sets the jre_distribution of this InstallationUsage.
        The distribution of the Java Runtime that is deployed with the installation.


        :param jre_distribution: The jre_distribution of this InstallationUsage.
        :type: str
        """
        self._jre_distribution = jre_distribution

    @property
    def jre_version(self):
        """
        **[Required]** Gets the jre_version of this InstallationUsage.
        The version of the Java Runtime that is deployed with the installation.


        :return: The jre_version of this InstallationUsage.
        :rtype: str
        """
        return self._jre_version

    @jre_version.setter
    def jre_version(self, jre_version):
        """
        Sets the jre_version of this InstallationUsage.
        The version of the Java Runtime that is deployed with the installation.


        :param jre_version: The jre_version of this InstallationUsage.
        :type: str
        """
        self._jre_version = jre_version

    @property
    def path(self):
        """
        **[Required]** Gets the path of this InstallationUsage.
        The file system path of the Java installation.


        :return: The path of this InstallationUsage.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this InstallationUsage.
        The file system path of the Java installation.


        :param path: The path of this InstallationUsage.
        :type: str
        """
        self._path = path

    @property
    def os(self):
        """
        **[Required]** Gets the os of this InstallationUsage.
        The Operating System for the installation. Deprecated, use `operatingSystem` instead.


        :return: The os of this InstallationUsage.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this InstallationUsage.
        The Operating System for the installation. Deprecated, use `operatingSystem` instead.


        :param os: The os of this InstallationUsage.
        :type: str
        """
        self._os = os

    @property
    def architecture(self):
        """
        **[Required]** Gets the architecture of this InstallationUsage.
        The architecture of the operating system for the installation. Deprecated, use `operatingSystem` instead.


        :return: The architecture of this InstallationUsage.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this InstallationUsage.
        The architecture of the operating system for the installation. Deprecated, use `operatingSystem` instead.


        :param architecture: The architecture of this InstallationUsage.
        :type: str
        """
        self._architecture = architecture

    @property
    def operating_system(self):
        """
        Gets the operating_system of this InstallationUsage.

        :return: The operating_system of this InstallationUsage.
        :rtype: oci.jms.models.OperatingSystem
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this InstallationUsage.

        :param operating_system: The operating_system of this InstallationUsage.
        :type: oci.jms.models.OperatingSystem
        """
        self._operating_system = operating_system

    @property
    def approximate_application_count(self):
        """
        Gets the approximate_application_count of this InstallationUsage.
        The approximate count of applications running on this installation


        :return: The approximate_application_count of this InstallationUsage.
        :rtype: int
        """
        return self._approximate_application_count

    @approximate_application_count.setter
    def approximate_application_count(self, approximate_application_count):
        """
        Sets the approximate_application_count of this InstallationUsage.
        The approximate count of applications running on this installation


        :param approximate_application_count: The approximate_application_count of this InstallationUsage.
        :type: int
        """
        self._approximate_application_count = approximate_application_count

    @property
    def approximate_managed_instance_count(self):
        """
        Gets the approximate_managed_instance_count of this InstallationUsage.
        The approximate count of managed instances reporting this installation


        :return: The approximate_managed_instance_count of this InstallationUsage.
        :rtype: int
        """
        return self._approximate_managed_instance_count

    @approximate_managed_instance_count.setter
    def approximate_managed_instance_count(self, approximate_managed_instance_count):
        """
        Sets the approximate_managed_instance_count of this InstallationUsage.
        The approximate count of managed instances reporting this installation


        :param approximate_managed_instance_count: The approximate_managed_instance_count of this InstallationUsage.
        :type: int
        """
        self._approximate_managed_instance_count = approximate_managed_instance_count

    @property
    def time_start(self):
        """
        Gets the time_start of this InstallationUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_start of this InstallationUsage.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this InstallationUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_start: The time_start of this InstallationUsage.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this InstallationUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_end of this InstallationUsage.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this InstallationUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_end: The time_end of this InstallationUsage.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def time_first_seen(self):
        """
        Gets the time_first_seen of this InstallationUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_first_seen of this InstallationUsage.
        :rtype: datetime
        """
        return self._time_first_seen

    @time_first_seen.setter
    def time_first_seen(self, time_first_seen):
        """
        Sets the time_first_seen of this InstallationUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_first_seen: The time_first_seen of this InstallationUsage.
        :type: datetime
        """
        self._time_first_seen = time_first_seen

    @property
    def time_last_seen(self):
        """
        Gets the time_last_seen of this InstallationUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_last_seen of this InstallationUsage.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this InstallationUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_last_seen: The time_last_seen of this InstallationUsage.
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
