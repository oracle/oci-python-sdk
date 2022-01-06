# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FleetAgentConfiguration(object):
    """
    Management Agent Configuration for a Fleet. Includes JRE scanning frequency and list of include/exclude file system paths.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FleetAgentConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param jre_scan_frequency_in_minutes:
            The value to assign to the jre_scan_frequency_in_minutes property of this FleetAgentConfiguration.
        :type jre_scan_frequency_in_minutes: int

        :param java_usage_tracker_processing_frequency_in_minutes:
            The value to assign to the java_usage_tracker_processing_frequency_in_minutes property of this FleetAgentConfiguration.
        :type java_usage_tracker_processing_frequency_in_minutes: int

        :param linux_configuration:
            The value to assign to the linux_configuration property of this FleetAgentConfiguration.
        :type linux_configuration: oci.jms.models.FleetAgentOsConfiguration

        :param windows_configuration:
            The value to assign to the windows_configuration property of this FleetAgentConfiguration.
        :type windows_configuration: oci.jms.models.FleetAgentOsConfiguration

        :param time_last_modified:
            The value to assign to the time_last_modified property of this FleetAgentConfiguration.
        :type time_last_modified: datetime

        """
        self.swagger_types = {
            'jre_scan_frequency_in_minutes': 'int',
            'java_usage_tracker_processing_frequency_in_minutes': 'int',
            'linux_configuration': 'FleetAgentOsConfiguration',
            'windows_configuration': 'FleetAgentOsConfiguration',
            'time_last_modified': 'datetime'
        }

        self.attribute_map = {
            'jre_scan_frequency_in_minutes': 'jreScanFrequencyInMinutes',
            'java_usage_tracker_processing_frequency_in_minutes': 'javaUsageTrackerProcessingFrequencyInMinutes',
            'linux_configuration': 'linuxConfiguration',
            'windows_configuration': 'windowsConfiguration',
            'time_last_modified': 'timeLastModified'
        }

        self._jre_scan_frequency_in_minutes = None
        self._java_usage_tracker_processing_frequency_in_minutes = None
        self._linux_configuration = None
        self._windows_configuration = None
        self._time_last_modified = None

    @property
    def jre_scan_frequency_in_minutes(self):
        """
        **[Required]** Gets the jre_scan_frequency_in_minutes of this FleetAgentConfiguration.
        The frequency (in minutes) of JRE scanning. (That is, how often should JMS scan for JRE installations.)


        :return: The jre_scan_frequency_in_minutes of this FleetAgentConfiguration.
        :rtype: int
        """
        return self._jre_scan_frequency_in_minutes

    @jre_scan_frequency_in_minutes.setter
    def jre_scan_frequency_in_minutes(self, jre_scan_frequency_in_minutes):
        """
        Sets the jre_scan_frequency_in_minutes of this FleetAgentConfiguration.
        The frequency (in minutes) of JRE scanning. (That is, how often should JMS scan for JRE installations.)


        :param jre_scan_frequency_in_minutes: The jre_scan_frequency_in_minutes of this FleetAgentConfiguration.
        :type: int
        """
        self._jre_scan_frequency_in_minutes = jre_scan_frequency_in_minutes

    @property
    def java_usage_tracker_processing_frequency_in_minutes(self):
        """
        **[Required]** Gets the java_usage_tracker_processing_frequency_in_minutes of this FleetAgentConfiguration.
        The frequency (in minutes) of Java Usage Tracker processing. (That is, how often should JMS process data from the Java Usage Tracker.)


        :return: The java_usage_tracker_processing_frequency_in_minutes of this FleetAgentConfiguration.
        :rtype: int
        """
        return self._java_usage_tracker_processing_frequency_in_minutes

    @java_usage_tracker_processing_frequency_in_minutes.setter
    def java_usage_tracker_processing_frequency_in_minutes(self, java_usage_tracker_processing_frequency_in_minutes):
        """
        Sets the java_usage_tracker_processing_frequency_in_minutes of this FleetAgentConfiguration.
        The frequency (in minutes) of Java Usage Tracker processing. (That is, how often should JMS process data from the Java Usage Tracker.)


        :param java_usage_tracker_processing_frequency_in_minutes: The java_usage_tracker_processing_frequency_in_minutes of this FleetAgentConfiguration.
        :type: int
        """
        self._java_usage_tracker_processing_frequency_in_minutes = java_usage_tracker_processing_frequency_in_minutes

    @property
    def linux_configuration(self):
        """
        **[Required]** Gets the linux_configuration of this FleetAgentConfiguration.

        :return: The linux_configuration of this FleetAgentConfiguration.
        :rtype: oci.jms.models.FleetAgentOsConfiguration
        """
        return self._linux_configuration

    @linux_configuration.setter
    def linux_configuration(self, linux_configuration):
        """
        Sets the linux_configuration of this FleetAgentConfiguration.

        :param linux_configuration: The linux_configuration of this FleetAgentConfiguration.
        :type: oci.jms.models.FleetAgentOsConfiguration
        """
        self._linux_configuration = linux_configuration

    @property
    def windows_configuration(self):
        """
        **[Required]** Gets the windows_configuration of this FleetAgentConfiguration.

        :return: The windows_configuration of this FleetAgentConfiguration.
        :rtype: oci.jms.models.FleetAgentOsConfiguration
        """
        return self._windows_configuration

    @windows_configuration.setter
    def windows_configuration(self, windows_configuration):
        """
        Sets the windows_configuration of this FleetAgentConfiguration.

        :param windows_configuration: The windows_configuration of this FleetAgentConfiguration.
        :type: oci.jms.models.FleetAgentOsConfiguration
        """
        self._windows_configuration = windows_configuration

    @property
    def time_last_modified(self):
        """
        **[Required]** Gets the time_last_modified of this FleetAgentConfiguration.
        The date and time of the last modification to the Fleet Agent Configuration (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_last_modified of this FleetAgentConfiguration.
        :rtype: datetime
        """
        return self._time_last_modified

    @time_last_modified.setter
    def time_last_modified(self, time_last_modified):
        """
        Sets the time_last_modified of this FleetAgentConfiguration.
        The date and time of the last modification to the Fleet Agent Configuration (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_last_modified: The time_last_modified of this FleetAgentConfiguration.
        :type: datetime
        """
        self._time_last_modified = time_last_modified

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
