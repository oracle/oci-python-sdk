# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestJfrRecordingsDetails(object):
    """
    Details of the request to start JFR recordings.
    When the targets aren't specified, then all managed instances currently in the Fleet are selected.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RequestJfrRecordingsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param targets:
            The value to assign to the targets property of this RequestJfrRecordingsDetails.
        :type targets: list[oci.jms.models.JfrAttachmentTarget]

        :param jfc_profile_name:
            The value to assign to the jfc_profile_name property of this RequestJfrRecordingsDetails.
        :type jfc_profile_name: str

        :param jfc_v1:
            The value to assign to the jfc_v1 property of this RequestJfrRecordingsDetails.
        :type jfc_v1: str

        :param jfc_v2:
            The value to assign to the jfc_v2 property of this RequestJfrRecordingsDetails.
        :type jfc_v2: str

        :param recording_duration_in_minutes:
            The value to assign to the recording_duration_in_minutes property of this RequestJfrRecordingsDetails.
        :type recording_duration_in_minutes: int

        :param recording_size_in_mb:
            The value to assign to the recording_size_in_mb property of this RequestJfrRecordingsDetails.
        :type recording_size_in_mb: int

        :param waiting_period_in_minutes:
            The value to assign to the waiting_period_in_minutes property of this RequestJfrRecordingsDetails.
        :type waiting_period_in_minutes: int

        """
        self.swagger_types = {
            'targets': 'list[JfrAttachmentTarget]',
            'jfc_profile_name': 'str',
            'jfc_v1': 'str',
            'jfc_v2': 'str',
            'recording_duration_in_minutes': 'int',
            'recording_size_in_mb': 'int',
            'waiting_period_in_minutes': 'int'
        }
        self.attribute_map = {
            'targets': 'targets',
            'jfc_profile_name': 'jfcProfileName',
            'jfc_v1': 'jfcV1',
            'jfc_v2': 'jfcV2',
            'recording_duration_in_minutes': 'recordingDurationInMinutes',
            'recording_size_in_mb': 'recordingSizeInMb',
            'waiting_period_in_minutes': 'waitingPeriodInMinutes'
        }
        self._targets = None
        self._jfc_profile_name = None
        self._jfc_v1 = None
        self._jfc_v2 = None
        self._recording_duration_in_minutes = None
        self._recording_size_in_mb = None
        self._waiting_period_in_minutes = None

    @property
    def targets(self):
        """
        Gets the targets of this RequestJfrRecordingsDetails.
        The attachment targets to start JFR.


        :return: The targets of this RequestJfrRecordingsDetails.
        :rtype: list[oci.jms.models.JfrAttachmentTarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this RequestJfrRecordingsDetails.
        The attachment targets to start JFR.


        :param targets: The targets of this RequestJfrRecordingsDetails.
        :type: list[oci.jms.models.JfrAttachmentTarget]
        """
        self._targets = targets

    @property
    def jfc_profile_name(self):
        """
        **[Required]** Gets the jfc_profile_name of this RequestJfrRecordingsDetails.
        The profile used for JFR events selection. If the name isn't recognized, the settings from jfcV1 or jfcV2
        will be used depending on the JVM version.
        Both jfcV2 and jfcV1 should be provided to ensure JFR collection on different JVM versions.


        :return: The jfc_profile_name of this RequestJfrRecordingsDetails.
        :rtype: str
        """
        return self._jfc_profile_name

    @jfc_profile_name.setter
    def jfc_profile_name(self, jfc_profile_name):
        """
        Sets the jfc_profile_name of this RequestJfrRecordingsDetails.
        The profile used for JFR events selection. If the name isn't recognized, the settings from jfcV1 or jfcV2
        will be used depending on the JVM version.
        Both jfcV2 and jfcV1 should be provided to ensure JFR collection on different JVM versions.


        :param jfc_profile_name: The jfc_profile_name of this RequestJfrRecordingsDetails.
        :type: str
        """
        self._jfc_profile_name = jfc_profile_name

    @property
    def jfc_v1(self):
        """
        Gets the jfc_v1 of this RequestJfrRecordingsDetails.
        The BASE64 encoded string of JFR settings XML with schema used by JDK 8.


        :return: The jfc_v1 of this RequestJfrRecordingsDetails.
        :rtype: str
        """
        return self._jfc_v1

    @jfc_v1.setter
    def jfc_v1(self, jfc_v1):
        """
        Sets the jfc_v1 of this RequestJfrRecordingsDetails.
        The BASE64 encoded string of JFR settings XML with schema used by JDK 8.


        :param jfc_v1: The jfc_v1 of this RequestJfrRecordingsDetails.
        :type: str
        """
        self._jfc_v1 = jfc_v1

    @property
    def jfc_v2(self):
        """
        Gets the jfc_v2 of this RequestJfrRecordingsDetails.
        The BASE64 encoded string of JFR settings XML with `schema used by JDK 9 and after`__.

        __ https://raw.githubusercontent.com/openjdk/jdk/master/src/jdk.jfr/share/classes/jdk/jfr/internal/jfc/jfc.xsd


        :return: The jfc_v2 of this RequestJfrRecordingsDetails.
        :rtype: str
        """
        return self._jfc_v2

    @jfc_v2.setter
    def jfc_v2(self, jfc_v2):
        """
        Sets the jfc_v2 of this RequestJfrRecordingsDetails.
        The BASE64 encoded string of JFR settings XML with `schema used by JDK 9 and after`__.

        __ https://raw.githubusercontent.com/openjdk/jdk/master/src/jdk.jfr/share/classes/jdk/jfr/internal/jfc/jfc.xsd


        :param jfc_v2: The jfc_v2 of this RequestJfrRecordingsDetails.
        :type: str
        """
        self._jfc_v2 = jfc_v2

    @property
    def recording_duration_in_minutes(self):
        """
        Gets the recording_duration_in_minutes of this RequestJfrRecordingsDetails.
        Duration of the JFR recording in minutes.


        :return: The recording_duration_in_minutes of this RequestJfrRecordingsDetails.
        :rtype: int
        """
        return self._recording_duration_in_minutes

    @recording_duration_in_minutes.setter
    def recording_duration_in_minutes(self, recording_duration_in_minutes):
        """
        Sets the recording_duration_in_minutes of this RequestJfrRecordingsDetails.
        Duration of the JFR recording in minutes.


        :param recording_duration_in_minutes: The recording_duration_in_minutes of this RequestJfrRecordingsDetails.
        :type: int
        """
        self._recording_duration_in_minutes = recording_duration_in_minutes

    @property
    def recording_size_in_mb(self):
        """
        Gets the recording_size_in_mb of this RequestJfrRecordingsDetails.
        The maximum size limit for the JFR file collected.


        :return: The recording_size_in_mb of this RequestJfrRecordingsDetails.
        :rtype: int
        """
        return self._recording_size_in_mb

    @recording_size_in_mb.setter
    def recording_size_in_mb(self, recording_size_in_mb):
        """
        Sets the recording_size_in_mb of this RequestJfrRecordingsDetails.
        The maximum size limit for the JFR file collected.


        :param recording_size_in_mb: The recording_size_in_mb of this RequestJfrRecordingsDetails.
        :type: int
        """
        self._recording_size_in_mb = recording_size_in_mb

    @property
    def waiting_period_in_minutes(self):
        """
        Gets the waiting_period_in_minutes of this RequestJfrRecordingsDetails.
        Period to looking for JVMs. In addition to attach to running JVMs when given the command,
        JVM started within the waiting period will also be attached for JFR. The value should be
        larger than the agent polling interval setting for the fleet to ensure agent can get the
        instructions. If not specified, the agent polling interval for the fleet is used.


        :return: The waiting_period_in_minutes of this RequestJfrRecordingsDetails.
        :rtype: int
        """
        return self._waiting_period_in_minutes

    @waiting_period_in_minutes.setter
    def waiting_period_in_minutes(self, waiting_period_in_minutes):
        """
        Sets the waiting_period_in_minutes of this RequestJfrRecordingsDetails.
        Period to looking for JVMs. In addition to attach to running JVMs when given the command,
        JVM started within the waiting period will also be attached for JFR. The value should be
        larger than the agent polling interval setting for the fleet to ensure agent can get the
        instructions. If not specified, the agent polling interval for the fleet is used.


        :param waiting_period_in_minutes: The waiting_period_in_minutes of this RequestJfrRecordingsDetails.
        :type: int
        """
        self._waiting_period_in_minutes = waiting_period_in_minutes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
