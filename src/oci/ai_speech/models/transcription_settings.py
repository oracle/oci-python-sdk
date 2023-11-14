# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TranscriptionSettings(object):
    """
    Processes to perform on the generated transcription.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TranscriptionSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param diarization:
            The value to assign to the diarization property of this TranscriptionSettings.
        :type diarization: oci.ai_speech.models.Diarization

        """
        self.swagger_types = {
            'diarization': 'Diarization'
        }

        self.attribute_map = {
            'diarization': 'diarization'
        }

        self._diarization = None

    @property
    def diarization(self):
        """
        Gets the diarization of this TranscriptionSettings.

        :return: The diarization of this TranscriptionSettings.
        :rtype: oci.ai_speech.models.Diarization
        """
        return self._diarization

    @diarization.setter
    def diarization(self, diarization):
        """
        Sets the diarization of this TranscriptionSettings.

        :param diarization: The diarization of this TranscriptionSettings.
        :type: oci.ai_speech.models.Diarization
        """
        self._diarization = diarization

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
