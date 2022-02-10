# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAttribution(object):
    """
    The confidence, source information, and visibility for a particular sighting or observation of some data associated with an indicator such as threat type, attribute or relationship.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataAttribution object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param confidence:
            The value to assign to the confidence property of this DataAttribution.
        :type confidence: int

        :param source:
            The value to assign to the source property of this DataAttribution.
        :type source: oci.threat_intelligence.models.IndicatorSourceSummary

        :param visibility:
            The value to assign to the visibility property of this DataAttribution.
        :type visibility: oci.threat_intelligence.models.DataVisibility

        :param time_first_seen:
            The value to assign to the time_first_seen property of this DataAttribution.
        :type time_first_seen: datetime

        :param time_last_seen:
            The value to assign to the time_last_seen property of this DataAttribution.
        :type time_last_seen: datetime

        """
        self.swagger_types = {
            'confidence': 'int',
            'source': 'IndicatorSourceSummary',
            'visibility': 'DataVisibility',
            'time_first_seen': 'datetime',
            'time_last_seen': 'datetime'
        }

        self.attribute_map = {
            'confidence': 'confidence',
            'source': 'source',
            'visibility': 'visibility',
            'time_first_seen': 'timeFirstSeen',
            'time_last_seen': 'timeLastSeen'
        }

        self._confidence = None
        self._source = None
        self._visibility = None
        self._time_first_seen = None
        self._time_last_seen = None

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this DataAttribution.
        Confidence is an integer from 0 to 100 that provides a measure of our certainty in the maliciousness of data attributed to an indicator.  For example, if the source of the data being attributed is the Tor Project, our confidence that the associated indicator is a tor exit node would be 100.


        :return: The confidence of this DataAttribution.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this DataAttribution.
        Confidence is an integer from 0 to 100 that provides a measure of our certainty in the maliciousness of data attributed to an indicator.  For example, if the source of the data being attributed is the Tor Project, our confidence that the associated indicator is a tor exit node would be 100.


        :param confidence: The confidence of this DataAttribution.
        :type: int
        """
        self._confidence = confidence

    @property
    def source(self):
        """
        **[Required]** Gets the source of this DataAttribution.

        :return: The source of this DataAttribution.
        :rtype: oci.threat_intelligence.models.IndicatorSourceSummary
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this DataAttribution.

        :param source: The source of this DataAttribution.
        :type: oci.threat_intelligence.models.IndicatorSourceSummary
        """
        self._source = source

    @property
    def visibility(self):
        """
        **[Required]** Gets the visibility of this DataAttribution.

        :return: The visibility of this DataAttribution.
        :rtype: oci.threat_intelligence.models.DataVisibility
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """
        Sets the visibility of this DataAttribution.

        :param visibility: The visibility of this DataAttribution.
        :type: oci.threat_intelligence.models.DataVisibility
        """
        self._visibility = visibility

    @property
    def time_first_seen(self):
        """
        Gets the time_first_seen of this DataAttribution.
        The time the data was first seen for this entity. Defaults to time last seen if no time first seen is provided from the data source. An RFC3339 formatted datetime string


        :return: The time_first_seen of this DataAttribution.
        :rtype: datetime
        """
        return self._time_first_seen

    @time_first_seen.setter
    def time_first_seen(self, time_first_seen):
        """
        Sets the time_first_seen of this DataAttribution.
        The time the data was first seen for this entity. Defaults to time last seen if no time first seen is provided from the data source. An RFC3339 formatted datetime string


        :param time_first_seen: The time_first_seen of this DataAttribution.
        :type: datetime
        """
        self._time_first_seen = time_first_seen

    @property
    def time_last_seen(self):
        """
        **[Required]** Gets the time_last_seen of this DataAttribution.
        The last time this data was seen for this entity. An RFC3339 formatted datetime string


        :return: The time_last_seen of this DataAttribution.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this DataAttribution.
        The last time this data was seen for this entity. An RFC3339 formatted datetime string


        :param time_last_seen: The time_last_seen of this DataAttribution.
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
