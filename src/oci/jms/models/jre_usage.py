# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JreUsage(object):
    """
    Java Runtime usage during a specified time period. A Java Runtime is identified by its vendor and version.
    """

    #: A constant which can be used with the security_status property of a JreUsage.
    #: This constant has a value of "UNKNOWN"
    SECURITY_STATUS_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the security_status property of a JreUsage.
    #: This constant has a value of "UP_TO_DATE"
    SECURITY_STATUS_UP_TO_DATE = "UP_TO_DATE"

    #: A constant which can be used with the security_status property of a JreUsage.
    #: This constant has a value of "UPDATE_REQUIRED"
    SECURITY_STATUS_UPDATE_REQUIRED = "UPDATE_REQUIRED"

    #: A constant which can be used with the security_status property of a JreUsage.
    #: This constant has a value of "UPGRADE_REQUIRED"
    SECURITY_STATUS_UPGRADE_REQUIRED = "UPGRADE_REQUIRED"

    def __init__(self, **kwargs):
        """
        Initializes a new JreUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this JreUsage.
        :type id: str

        :param fleet_id:
            The value to assign to the fleet_id property of this JreUsage.
        :type fleet_id: str

        :param managed_instance_id:
            The value to assign to the managed_instance_id property of this JreUsage.
        :type managed_instance_id: str

        :param security_status:
            The value to assign to the security_status property of this JreUsage.
            Allowed values for this property are: "UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type security_status: str

        :param release_date:
            The value to assign to the release_date property of this JreUsage.
        :type release_date: datetime

        :param end_of_support_life_date:
            The value to assign to the end_of_support_life_date property of this JreUsage.
        :type end_of_support_life_date: datetime

        :param vendor:
            The value to assign to the vendor property of this JreUsage.
        :type vendor: str

        :param distribution:
            The value to assign to the distribution property of this JreUsage.
        :type distribution: str

        :param version:
            The value to assign to the version property of this JreUsage.
        :type version: str

        :param days_under_security_baseline:
            The value to assign to the days_under_security_baseline property of this JreUsage.
        :type days_under_security_baseline: int

        :param operating_systems:
            The value to assign to the operating_systems property of this JreUsage.
        :type operating_systems: list[oci.jms.models.OperatingSystem]

        :param approximate_installation_count:
            The value to assign to the approximate_installation_count property of this JreUsage.
        :type approximate_installation_count: int

        :param approximate_application_count:
            The value to assign to the approximate_application_count property of this JreUsage.
        :type approximate_application_count: int

        :param approximate_managed_instance_count:
            The value to assign to the approximate_managed_instance_count property of this JreUsage.
        :type approximate_managed_instance_count: int

        :param approximate_pending_work_request_count:
            The value to assign to the approximate_pending_work_request_count property of this JreUsage.
        :type approximate_pending_work_request_count: int

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
            'id': 'str',
            'fleet_id': 'str',
            'managed_instance_id': 'str',
            'security_status': 'str',
            'release_date': 'datetime',
            'end_of_support_life_date': 'datetime',
            'vendor': 'str',
            'distribution': 'str',
            'version': 'str',
            'days_under_security_baseline': 'int',
            'operating_systems': 'list[OperatingSystem]',
            'approximate_installation_count': 'int',
            'approximate_application_count': 'int',
            'approximate_managed_instance_count': 'int',
            'approximate_pending_work_request_count': 'int',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'time_first_seen': 'datetime',
            'time_last_seen': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'fleet_id': 'fleetId',
            'managed_instance_id': 'managedInstanceId',
            'security_status': 'securityStatus',
            'release_date': 'releaseDate',
            'end_of_support_life_date': 'endOfSupportLifeDate',
            'vendor': 'vendor',
            'distribution': 'distribution',
            'version': 'version',
            'days_under_security_baseline': 'daysUnderSecurityBaseline',
            'operating_systems': 'operatingSystems',
            'approximate_installation_count': 'approximateInstallationCount',
            'approximate_application_count': 'approximateApplicationCount',
            'approximate_managed_instance_count': 'approximateManagedInstanceCount',
            'approximate_pending_work_request_count': 'approximatePendingWorkRequestCount',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'time_first_seen': 'timeFirstSeen',
            'time_last_seen': 'timeLastSeen'
        }

        self._id = None
        self._fleet_id = None
        self._managed_instance_id = None
        self._security_status = None
        self._release_date = None
        self._end_of_support_life_date = None
        self._vendor = None
        self._distribution = None
        self._version = None
        self._days_under_security_baseline = None
        self._operating_systems = None
        self._approximate_installation_count = None
        self._approximate_application_count = None
        self._approximate_managed_instance_count = None
        self._approximate_pending_work_request_count = None
        self._time_start = None
        self._time_end = None
        self._time_first_seen = None
        self._time_last_seen = None

    @property
    def id(self):
        """
        Gets the id of this JreUsage.
        The internal identifier of the Java Runtime.


        :return: The id of this JreUsage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JreUsage.
        The internal identifier of the Java Runtime.


        :param id: The id of this JreUsage.
        :type: str
        """
        self._id = id

    @property
    def fleet_id(self):
        """
        Gets the fleet_id of this JreUsage.
        The `OCID`__ of the related fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The fleet_id of this JreUsage.
        :rtype: str
        """
        return self._fleet_id

    @fleet_id.setter
    def fleet_id(self, fleet_id):
        """
        Sets the fleet_id of this JreUsage.
        The `OCID`__ of the related fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param fleet_id: The fleet_id of this JreUsage.
        :type: str
        """
        self._fleet_id = fleet_id

    @property
    def managed_instance_id(self):
        """
        Gets the managed_instance_id of this JreUsage.
        The `OCID`__ of the related managed instance. This property value is present only for /listJreUsage.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_instance_id of this JreUsage.
        :rtype: str
        """
        return self._managed_instance_id

    @managed_instance_id.setter
    def managed_instance_id(self, managed_instance_id):
        """
        Sets the managed_instance_id of this JreUsage.
        The `OCID`__ of the related managed instance. This property value is present only for /listJreUsage.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_instance_id: The managed_instance_id of this JreUsage.
        :type: str
        """
        self._managed_instance_id = managed_instance_id

    @property
    def security_status(self):
        """
        Gets the security_status of this JreUsage.
        The security status of the Java Runtime.

        Allowed values for this property are: "UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The security_status of this JreUsage.
        :rtype: str
        """
        return self._security_status

    @security_status.setter
    def security_status(self, security_status):
        """
        Sets the security_status of this JreUsage.
        The security status of the Java Runtime.


        :param security_status: The security_status of this JreUsage.
        :type: str
        """
        allowed_values = ["UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED"]
        if not value_allowed_none_or_none_sentinel(security_status, allowed_values):
            security_status = 'UNKNOWN_ENUM_VALUE'
        self._security_status = security_status

    @property
    def release_date(self):
        """
        Gets the release_date of this JreUsage.
        The release date of the Java Runtime (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The release_date of this JreUsage.
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """
        Sets the release_date of this JreUsage.
        The release date of the Java Runtime (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param release_date: The release_date of this JreUsage.
        :type: datetime
        """
        self._release_date = release_date

    @property
    def end_of_support_life_date(self):
        """
        Gets the end_of_support_life_date of this JreUsage.
        The End of Support Life (EOSL) date of the Java Runtime (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The end_of_support_life_date of this JreUsage.
        :rtype: datetime
        """
        return self._end_of_support_life_date

    @end_of_support_life_date.setter
    def end_of_support_life_date(self, end_of_support_life_date):
        """
        Sets the end_of_support_life_date of this JreUsage.
        The End of Support Life (EOSL) date of the Java Runtime (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param end_of_support_life_date: The end_of_support_life_date of this JreUsage.
        :type: datetime
        """
        self._end_of_support_life_date = end_of_support_life_date

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
    def days_under_security_baseline(self):
        """
        Gets the days_under_security_baseline of this JreUsage.
        The number of days since this release has been under the security baseline.


        :return: The days_under_security_baseline of this JreUsage.
        :rtype: int
        """
        return self._days_under_security_baseline

    @days_under_security_baseline.setter
    def days_under_security_baseline(self, days_under_security_baseline):
        """
        Sets the days_under_security_baseline of this JreUsage.
        The number of days since this release has been under the security baseline.


        :param days_under_security_baseline: The days_under_security_baseline of this JreUsage.
        :type: int
        """
        self._days_under_security_baseline = days_under_security_baseline

    @property
    def operating_systems(self):
        """
        Gets the operating_systems of this JreUsage.
        The operating systems that have this Java Runtime installed.


        :return: The operating_systems of this JreUsage.
        :rtype: list[oci.jms.models.OperatingSystem]
        """
        return self._operating_systems

    @operating_systems.setter
    def operating_systems(self, operating_systems):
        """
        Sets the operating_systems of this JreUsage.
        The operating systems that have this Java Runtime installed.


        :param operating_systems: The operating_systems of this JreUsage.
        :type: list[oci.jms.models.OperatingSystem]
        """
        self._operating_systems = operating_systems

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
    def approximate_pending_work_request_count(self):
        """
        Gets the approximate_pending_work_request_count of this JreUsage.
        The approximate count of work requests working on this Java Runtime.


        :return: The approximate_pending_work_request_count of this JreUsage.
        :rtype: int
        """
        return self._approximate_pending_work_request_count

    @approximate_pending_work_request_count.setter
    def approximate_pending_work_request_count(self, approximate_pending_work_request_count):
        """
        Sets the approximate_pending_work_request_count of this JreUsage.
        The approximate count of work requests working on this Java Runtime.


        :param approximate_pending_work_request_count: The approximate_pending_work_request_count of this JreUsage.
        :type: int
        """
        self._approximate_pending_work_request_count = approximate_pending_work_request_count

    @property
    def time_start(self):
        """
        Gets the time_start of this JreUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_start of this JreUsage.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this JreUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_start: The time_start of this JreUsage.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this JreUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_end of this JreUsage.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this JreUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


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
