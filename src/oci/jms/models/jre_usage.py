# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JreUsage(object):
    """
    Java Runtime usage during a specified time period. A Java Runtime is identified by its vendor and version.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JreUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vendor:
            The value to assign to the vendor property of this JreUsage.
        :type vendor: str

        :param distribution:
            The value to assign to the distribution property of this JreUsage.
        :type distribution: str

        :param version:
            The value to assign to the version property of this JreUsage.
        :type version: str

        :param approximate_installation_count:
            The value to assign to the approximate_installation_count property of this JreUsage.
        :type approximate_installation_count: int

        :param approximate_application_count:
            The value to assign to the approximate_application_count property of this JreUsage.
        :type approximate_application_count: int

        :param approximate_managed_instance_count:
            The value to assign to the approximate_managed_instance_count property of this JreUsage.
        :type approximate_managed_instance_count: int

        :param time_start:
            The value to assign to the time_start property of this JreUsage.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this JreUsage.
        :type time_end: datetime

        :param time_first_seen:
            The value to assign to the time_first_seen property of this JreUsage.
        :type time_first_seen: datetime

        :param time_last_seen:
            The value to assign to the time_last_seen property of this JreUsage.
        :type time_last_seen: datetime

        """
        self.swagger_types = {
            'vendor': 'str',
            'distribution': 'str',
            'version': 'str',
            'approximate_installation_count': 'int',
            'approximate_application_count': 'int',
            'approximate_managed_instance_count': 'int',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'time_first_seen': 'datetime',
            'time_last_seen': 'datetime'
        }

        self.attribute_map = {
            'vendor': 'vendor',
            'distribution': 'distribution',
            'version': 'version',
            'approximate_installation_count': 'approximateInstallationCount',
            'approximate_application_count': 'approximateApplicationCount',
            'approximate_managed_instance_count': 'approximateManagedInstanceCount',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'time_first_seen': 'timeFirstSeen',
            'time_last_seen': 'timeLastSeen'
        }

        self._vendor = None
        self._distribution = None
        self._version = None
        self._approximate_installation_count = None
        self._approximate_application_count = None
        self._approximate_managed_instance_count = None
        self._time_start = None
        self._time_end = None
        self._time_first_seen = None
        self._time_last_seen = None

    @property
    def vendor(self):
        """
        **[Required]** Gets the vendor of this JreUsage.
        The vendor of the Java Runtime.


        :return: The vendor of this JreUsage.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this JreUsage.
        The vendor of the Java Runtime.


        :param vendor: The vendor of this JreUsage.
        :type: str
        """
        self._vendor = vendor

    @property
    def distribution(self):
        """
        **[Required]** Gets the distribution of this JreUsage.
        The distribution of a Java Runtime is the name of the lineage of product to which it belongs, for example _Java(TM) SE Runtime Environment_.


        :return: The distribution of this JreUsage.
        :rtype: str
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """
        Sets the distribution of this JreUsage.
        The distribution of a Java Runtime is the name of the lineage of product to which it belongs, for example _Java(TM) SE Runtime Environment_.


        :param distribution: The distribution of this JreUsage.
        :type: str
        """
        self._distribution = distribution

    @property
    def version(self):
        """
        **[Required]** Gets the version of this JreUsage.
        The version of the Java Runtime.


        :return: The version of this JreUsage.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this JreUsage.
        The version of the Java Runtime.


        :param version: The version of this JreUsage.
        :type: str
        """
        self._version = version

    @property
    def approximate_installation_count(self):
        """
        Gets the approximate_installation_count of this JreUsage.
        The approximate count of installations that are installations of this Java Runtime.


        :return: The approximate_installation_count of this JreUsage.
        :rtype: int
        """
        return self._approximate_installation_count

    @approximate_installation_count.setter
    def approximate_installation_count(self, approximate_installation_count):
        """
        Sets the approximate_installation_count of this JreUsage.
        The approximate count of installations that are installations of this Java Runtime.


        :param approximate_installation_count: The approximate_installation_count of this JreUsage.
        :type: int
        """
        self._approximate_installation_count = approximate_installation_count

    @property
    def approximate_application_count(self):
        """
        Gets the approximate_application_count of this JreUsage.
        The approximate count of the applications running on this Java Runtime.


        :return: The approximate_application_count of this JreUsage.
        :rtype: int
        """
        return self._approximate_application_count

    @approximate_application_count.setter
    def approximate_application_count(self, approximate_application_count):
        """
        Sets the approximate_application_count of this JreUsage.
        The approximate count of the applications running on this Java Runtime.


        :param approximate_application_count: The approximate_application_count of this JreUsage.
        :type: int
        """
        self._approximate_application_count = approximate_application_count

    @property
    def approximate_managed_instance_count(self):
        """
        Gets the approximate_managed_instance_count of this JreUsage.
        The approximate count of the managed instances that report this Java Runtime.


        :return: The approximate_managed_instance_count of this JreUsage.
        :rtype: int
        """
        return self._approximate_managed_instance_count

    @approximate_managed_instance_count.setter
    def approximate_managed_instance_count(self, approximate_managed_instance_count):
        """
        Sets the approximate_managed_instance_count of this JreUsage.
        The approximate count of the managed instances that report this Java Runtime.


        :param approximate_managed_instance_count: The approximate_managed_instance_count of this JreUsage.
        :type: int
        """
        self._approximate_managed_instance_count = approximate_managed_instance_count

    @property
    def time_start(self):
        """
        Gets the time_start of this JreUsage.
        Lower bound of the specified time period filter.


        :return: The time_start of this JreUsage.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this JreUsage.
        Lower bound of the specified time period filter.


        :param time_start: The time_start of this JreUsage.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this JreUsage.
        Upper bound of the specified time period filter.


        :return: The time_end of this JreUsage.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this JreUsage.
        Upper bound of the specified time period filter.


        :param time_end: The time_end of this JreUsage.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def time_first_seen(self):
        """
        Gets the time_first_seen of this JreUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_first_seen of this JreUsage.
        :rtype: datetime
        """
        return self._time_first_seen

    @time_first_seen.setter
    def time_first_seen(self, time_first_seen):
        """
        Sets the time_first_seen of this JreUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_first_seen: The time_first_seen of this JreUsage.
        :type: datetime
        """
        self._time_first_seen = time_first_seen

    @property
    def time_last_seen(self):
        """
        Gets the time_last_seen of this JreUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_last_seen of this JreUsage.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this JreUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_last_seen: The time_last_seen of this JreUsage.
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
