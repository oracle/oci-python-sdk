# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LibraryUsage(object):
    """
    Library usage during a specified time period.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LibraryUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param library_key:
            The value to assign to the library_key property of this LibraryUsage.
        :type library_key: str

        :param fleet_id:
            The value to assign to the fleet_id property of this LibraryUsage.
        :type fleet_id: str

        :param library_name:
            The value to assign to the library_name property of this LibraryUsage.
        :type library_name: str

        :param library_version:
            The value to assign to the library_version property of this LibraryUsage.
        :type library_version: str

        :param cvss_score:
            The value to assign to the cvss_score property of this LibraryUsage.
        :type cvss_score: float

        :param approximate_application_count:
            The value to assign to the approximate_application_count property of this LibraryUsage.
        :type approximate_application_count: int

        :param approximate_java_server_instance_count:
            The value to assign to the approximate_java_server_instance_count property of this LibraryUsage.
        :type approximate_java_server_instance_count: int

        :param approximate_deployed_application_count:
            The value to assign to the approximate_deployed_application_count property of this LibraryUsage.
        :type approximate_deployed_application_count: int

        :param approximate_managed_instance_count:
            The value to assign to the approximate_managed_instance_count property of this LibraryUsage.
        :type approximate_managed_instance_count: int

        :param time_start:
            The value to assign to the time_start property of this LibraryUsage.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this LibraryUsage.
        :type time_end: datetime

        :param time_first_seen:
            The value to assign to the time_first_seen property of this LibraryUsage.
        :type time_first_seen: datetime

        :param time_last_seen:
            The value to assign to the time_last_seen property of this LibraryUsage.
        :type time_last_seen: datetime

        """
        self.swagger_types = {
            'library_key': 'str',
            'fleet_id': 'str',
            'library_name': 'str',
            'library_version': 'str',
            'cvss_score': 'float',
            'approximate_application_count': 'int',
            'approximate_java_server_instance_count': 'int',
            'approximate_deployed_application_count': 'int',
            'approximate_managed_instance_count': 'int',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'time_first_seen': 'datetime',
            'time_last_seen': 'datetime'
        }

        self.attribute_map = {
            'library_key': 'libraryKey',
            'fleet_id': 'fleetId',
            'library_name': 'libraryName',
            'library_version': 'libraryVersion',
            'cvss_score': 'cvssScore',
            'approximate_application_count': 'approximateApplicationCount',
            'approximate_java_server_instance_count': 'approximateJavaServerInstanceCount',
            'approximate_deployed_application_count': 'approximateDeployedApplicationCount',
            'approximate_managed_instance_count': 'approximateManagedInstanceCount',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'time_first_seen': 'timeFirstSeen',
            'time_last_seen': 'timeLastSeen'
        }

        self._library_key = None
        self._fleet_id = None
        self._library_name = None
        self._library_version = None
        self._cvss_score = None
        self._approximate_application_count = None
        self._approximate_java_server_instance_count = None
        self._approximate_deployed_application_count = None
        self._approximate_managed_instance_count = None
        self._time_start = None
        self._time_end = None
        self._time_first_seen = None
        self._time_last_seen = None

    @property
    def library_key(self):
        """
        **[Required]** Gets the library_key of this LibraryUsage.
        The internal identifier of the library.


        :return: The library_key of this LibraryUsage.
        :rtype: str
        """
        return self._library_key

    @library_key.setter
    def library_key(self, library_key):
        """
        Sets the library_key of this LibraryUsage.
        The internal identifier of the library.


        :param library_key: The library_key of this LibraryUsage.
        :type: str
        """
        self._library_key = library_key

    @property
    def fleet_id(self):
        """
        **[Required]** Gets the fleet_id of this LibraryUsage.
        The `OCID`__ of the related fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The fleet_id of this LibraryUsage.
        :rtype: str
        """
        return self._fleet_id

    @fleet_id.setter
    def fleet_id(self, fleet_id):
        """
        Sets the fleet_id of this LibraryUsage.
        The `OCID`__ of the related fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param fleet_id: The fleet_id of this LibraryUsage.
        :type: str
        """
        self._fleet_id = fleet_id

    @property
    def library_name(self):
        """
        **[Required]** Gets the library_name of this LibraryUsage.
        The name of the library.


        :return: The library_name of this LibraryUsage.
        :rtype: str
        """
        return self._library_name

    @library_name.setter
    def library_name(self, library_name):
        """
        Sets the library_name of this LibraryUsage.
        The name of the library.


        :param library_name: The library_name of this LibraryUsage.
        :type: str
        """
        self._library_name = library_name

    @property
    def library_version(self):
        """
        Gets the library_version of this LibraryUsage.
        The version of the library.


        :return: The library_version of this LibraryUsage.
        :rtype: str
        """
        return self._library_version

    @library_version.setter
    def library_version(self, library_version):
        """
        Sets the library_version of this LibraryUsage.
        The version of the library.


        :param library_version: The library_version of this LibraryUsage.
        :type: str
        """
        self._library_version = library_version

    @property
    def cvss_score(self):
        """
        Gets the cvss_score of this LibraryUsage.
        The Common Vulnerability Scoring System (CVSS) score.


        :return: The cvss_score of this LibraryUsage.
        :rtype: float
        """
        return self._cvss_score

    @cvss_score.setter
    def cvss_score(self, cvss_score):
        """
        Sets the cvss_score of this LibraryUsage.
        The Common Vulnerability Scoring System (CVSS) score.


        :param cvss_score: The cvss_score of this LibraryUsage.
        :type: float
        """
        self._cvss_score = cvss_score

    @property
    def approximate_application_count(self):
        """
        Gets the approximate_application_count of this LibraryUsage.
        The approximate count of applications using the library.


        :return: The approximate_application_count of this LibraryUsage.
        :rtype: int
        """
        return self._approximate_application_count

    @approximate_application_count.setter
    def approximate_application_count(self, approximate_application_count):
        """
        Sets the approximate_application_count of this LibraryUsage.
        The approximate count of applications using the library.


        :param approximate_application_count: The approximate_application_count of this LibraryUsage.
        :type: int
        """
        self._approximate_application_count = approximate_application_count

    @property
    def approximate_java_server_instance_count(self):
        """
        Gets the approximate_java_server_instance_count of this LibraryUsage.
        The approximate count of Java server instances using the library.


        :return: The approximate_java_server_instance_count of this LibraryUsage.
        :rtype: int
        """
        return self._approximate_java_server_instance_count

    @approximate_java_server_instance_count.setter
    def approximate_java_server_instance_count(self, approximate_java_server_instance_count):
        """
        Sets the approximate_java_server_instance_count of this LibraryUsage.
        The approximate count of Java server instances using the library.


        :param approximate_java_server_instance_count: The approximate_java_server_instance_count of this LibraryUsage.
        :type: int
        """
        self._approximate_java_server_instance_count = approximate_java_server_instance_count

    @property
    def approximate_deployed_application_count(self):
        """
        Gets the approximate_deployed_application_count of this LibraryUsage.
        The approximate count of deployed applications using the library.


        :return: The approximate_deployed_application_count of this LibraryUsage.
        :rtype: int
        """
        return self._approximate_deployed_application_count

    @approximate_deployed_application_count.setter
    def approximate_deployed_application_count(self, approximate_deployed_application_count):
        """
        Sets the approximate_deployed_application_count of this LibraryUsage.
        The approximate count of deployed applications using the library.


        :param approximate_deployed_application_count: The approximate_deployed_application_count of this LibraryUsage.
        :type: int
        """
        self._approximate_deployed_application_count = approximate_deployed_application_count

    @property
    def approximate_managed_instance_count(self):
        """
        Gets the approximate_managed_instance_count of this LibraryUsage.
        The approximate count of managed instances using the library.


        :return: The approximate_managed_instance_count of this LibraryUsage.
        :rtype: int
        """
        return self._approximate_managed_instance_count

    @approximate_managed_instance_count.setter
    def approximate_managed_instance_count(self, approximate_managed_instance_count):
        """
        Sets the approximate_managed_instance_count of this LibraryUsage.
        The approximate count of managed instances using the library.


        :param approximate_managed_instance_count: The approximate_managed_instance_count of this LibraryUsage.
        :type: int
        """
        self._approximate_managed_instance_count = approximate_managed_instance_count

    @property
    def time_start(self):
        """
        Gets the time_start of this LibraryUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_start of this LibraryUsage.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this LibraryUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_start: The time_start of this LibraryUsage.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this LibraryUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_end of this LibraryUsage.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this LibraryUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_end: The time_end of this LibraryUsage.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def time_first_seen(self):
        """
        Gets the time_first_seen of this LibraryUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_first_seen of this LibraryUsage.
        :rtype: datetime
        """
        return self._time_first_seen

    @time_first_seen.setter
    def time_first_seen(self, time_first_seen):
        """
        Sets the time_first_seen of this LibraryUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_first_seen: The time_first_seen of this LibraryUsage.
        :type: datetime
        """
        self._time_first_seen = time_first_seen

    @property
    def time_last_seen(self):
        """
        Gets the time_last_seen of this LibraryUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_last_seen of this LibraryUsage.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this LibraryUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_last_seen: The time_last_seen of this LibraryUsage.
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
