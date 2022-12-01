# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CryptoEventAnalysis(object):
    """
    CryptoEventAnalysis configuration
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CryptoEventAnalysis object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this CryptoEventAnalysis.
        :type is_enabled: bool

        :param summarized_events_log:
            The value to assign to the summarized_events_log property of this CryptoEventAnalysis.
        :type summarized_events_log: oci.jms.models.SummarizedEventsLog

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'summarized_events_log': 'SummarizedEventsLog'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'summarized_events_log': 'summarizedEventsLog'
        }

        self._is_enabled = None
        self._summarized_events_log = None

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this CryptoEventAnalysis.
        CryptoEventAnalysis flag to store enabled or disabled status


        :return: The is_enabled of this CryptoEventAnalysis.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this CryptoEventAnalysis.
        CryptoEventAnalysis flag to store enabled or disabled status


        :param is_enabled: The is_enabled of this CryptoEventAnalysis.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def summarized_events_log(self):
        """
        Gets the summarized_events_log of this CryptoEventAnalysis.

        :return: The summarized_events_log of this CryptoEventAnalysis.
        :rtype: oci.jms.models.SummarizedEventsLog
        """
        return self._summarized_events_log

    @summarized_events_log.setter
    def summarized_events_log(self, summarized_events_log):
        """
        Sets the summarized_events_log of this CryptoEventAnalysis.

        :param summarized_events_log: The summarized_events_log of this CryptoEventAnalysis.
        :type: oci.jms.models.SummarizedEventsLog
        """
        self._summarized_events_log = summarized_events_log

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
