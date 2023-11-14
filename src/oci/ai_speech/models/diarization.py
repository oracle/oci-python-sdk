# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Diarization(object):
    """
    Speaker diarization is a combination of speaker segmentation and speaker clustering. Provide diarization details to enable this feature.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Diarization object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_diarization_enabled:
            The value to assign to the is_diarization_enabled property of this Diarization.
        :type is_diarization_enabled: bool

        :param number_of_speakers:
            The value to assign to the number_of_speakers property of this Diarization.
        :type number_of_speakers: int

        """
        self.swagger_types = {
            'is_diarization_enabled': 'bool',
            'number_of_speakers': 'int'
        }

        self.attribute_map = {
            'is_diarization_enabled': 'isDiarizationEnabled',
            'number_of_speakers': 'numberOfSpeakers'
        }

        self._is_diarization_enabled = None
        self._number_of_speakers = None

    @property
    def is_diarization_enabled(self):
        """
        Gets the is_diarization_enabled of this Diarization.
        Set true to enable Speaker diarization and tag transcription with speaker tags. By default this is disabled.


        :return: The is_diarization_enabled of this Diarization.
        :rtype: bool
        """
        return self._is_diarization_enabled

    @is_diarization_enabled.setter
    def is_diarization_enabled(self, is_diarization_enabled):
        """
        Sets the is_diarization_enabled of this Diarization.
        Set true to enable Speaker diarization and tag transcription with speaker tags. By default this is disabled.


        :param is_diarization_enabled: The is_diarization_enabled of this Diarization.
        :type: bool
        """
        self._is_diarization_enabled = is_diarization_enabled

    @property
    def number_of_speakers(self):
        """
        Gets the number_of_speakers of this Diarization.
        Number of speakers in the audio provided. By default service will auto detect all speakers in audio file


        :return: The number_of_speakers of this Diarization.
        :rtype: int
        """
        return self._number_of_speakers

    @number_of_speakers.setter
    def number_of_speakers(self, number_of_speakers):
        """
        Sets the number_of_speakers of this Diarization.
        Number of speakers in the audio provided. By default service will auto detect all speakers in audio file


        :param number_of_speakers: The number_of_speakers of this Diarization.
        :type: int
        """
        self._number_of_speakers = number_of_speakers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
