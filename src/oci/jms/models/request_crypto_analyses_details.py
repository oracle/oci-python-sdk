# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestCryptoAnalysesDetails(object):
    """
    Details of the request to start a JFR analysis.
    When the targets aren't specified, then all managed instances currently in the fleet are selected.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RequestCryptoAnalysesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param targets:
            The value to assign to the targets property of this RequestCryptoAnalysesDetails.
        :type targets: list[oci.jms.models.JfrAttachmentTarget]

        :param recording_duration_in_minutes:
            The value to assign to the recording_duration_in_minutes property of this RequestCryptoAnalysesDetails.
        :type recording_duration_in_minutes: int

        """
        self.swagger_types = {
            'targets': 'list[JfrAttachmentTarget]',
            'recording_duration_in_minutes': 'int'
        }

        self.attribute_map = {
            'targets': 'targets',
            'recording_duration_in_minutes': 'recordingDurationInMinutes'
        }

        self._targets = None
        self._recording_duration_in_minutes = None

    @property
    def targets(self):
        """
        Gets the targets of this RequestCryptoAnalysesDetails.
        The attachment targets to start JFR.


        :return: The targets of this RequestCryptoAnalysesDetails.
        :rtype: list[oci.jms.models.JfrAttachmentTarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this RequestCryptoAnalysesDetails.
        The attachment targets to start JFR.


        :param targets: The targets of this RequestCryptoAnalysesDetails.
        :type: list[oci.jms.models.JfrAttachmentTarget]
        """
        self._targets = targets

    @property
    def recording_duration_in_minutes(self):
        """
        Gets the recording_duration_in_minutes of this RequestCryptoAnalysesDetails.
        Duration of the JFR recording in minutes.


        :return: The recording_duration_in_minutes of this RequestCryptoAnalysesDetails.
        :rtype: int
        """
        return self._recording_duration_in_minutes

    @recording_duration_in_minutes.setter
    def recording_duration_in_minutes(self, recording_duration_in_minutes):
        """
        Sets the recording_duration_in_minutes of this RequestCryptoAnalysesDetails.
        Duration of the JFR recording in minutes.


        :param recording_duration_in_minutes: The recording_duration_in_minutes of this RequestCryptoAnalysesDetails.
        :type: int
        """
        self._recording_duration_in_minutes = recording_duration_in_minutes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
