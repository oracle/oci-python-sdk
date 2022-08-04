# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TranscriptionNormalization(object):
    """
    Information to Normalize generated transcript.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TranscriptionNormalization object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_punctuation_enabled:
            The value to assign to the is_punctuation_enabled property of this TranscriptionNormalization.
        :type is_punctuation_enabled: bool

        :param filters:
            The value to assign to the filters property of this TranscriptionNormalization.
        :type filters: list[oci.ai_speech.models.TranscriptionFilter]

        """
        self.swagger_types = {
            'is_punctuation_enabled': 'bool',
            'filters': 'list[TranscriptionFilter]'
        }

        self.attribute_map = {
            'is_punctuation_enabled': 'isPunctuationEnabled',
            'filters': 'filters'
        }

        self._is_punctuation_enabled = None
        self._filters = None

    @property
    def is_punctuation_enabled(self):
        """
        Gets the is_punctuation_enabled of this TranscriptionNormalization.
        Whether to add punctuation in the generated transcription. Enabled by default.


        :return: The is_punctuation_enabled of this TranscriptionNormalization.
        :rtype: bool
        """
        return self._is_punctuation_enabled

    @is_punctuation_enabled.setter
    def is_punctuation_enabled(self, is_punctuation_enabled):
        """
        Sets the is_punctuation_enabled of this TranscriptionNormalization.
        Whether to add punctuation in the generated transcription. Enabled by default.


        :param is_punctuation_enabled: The is_punctuation_enabled of this TranscriptionNormalization.
        :type: bool
        """
        self._is_punctuation_enabled = is_punctuation_enabled

    @property
    def filters(self):
        """
        Gets the filters of this TranscriptionNormalization.
        List of filters.


        :return: The filters of this TranscriptionNormalization.
        :rtype: list[oci.ai_speech.models.TranscriptionFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this TranscriptionNormalization.
        List of filters.


        :param filters: The filters of this TranscriptionNormalization.
        :type: list[oci.ai_speech.models.TranscriptionFilter]
        """
        self._filters = filters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
