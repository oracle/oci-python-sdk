# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetectionResultItem(object):
    """
    An object to hold detection result for one timestamp/row.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetectionResultItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param timestamp:
            The value to assign to the timestamp property of this DetectionResultItem.
        :type timestamp: datetime

        :param row_index:
            The value to assign to the row_index property of this DetectionResultItem.
        :type row_index: int

        :param score:
            The value to assign to the score property of this DetectionResultItem.
        :type score: float

        :param anomalies:
            The value to assign to the anomalies property of this DetectionResultItem.
        :type anomalies: list[oci.ai_anomaly_detection.models.Anomaly]

        """
        self.swagger_types = {
            'timestamp': 'datetime',
            'row_index': 'int',
            'score': 'float',
            'anomalies': 'list[Anomaly]'
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'row_index': 'rowIndex',
            'score': 'score',
            'anomalies': 'anomalies'
        }

        self._timestamp = None
        self._row_index = None
        self._score = None
        self._anomalies = None

    @property
    def timestamp(self):
        """
        Gets the timestamp of this DetectionResultItem.
        The time stamp associated with a list of anomaly points, format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The timestamp of this DetectionResultItem.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this DetectionResultItem.
        The time stamp associated with a list of anomaly points, format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param timestamp: The timestamp of this DetectionResultItem.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def row_index(self):
        """
        Gets the row_index of this DetectionResultItem.
        The index number to indicate where anomaly points are located among all rows when there are no timestamps provided.


        :return: The row_index of this DetectionResultItem.
        :rtype: int
        """
        return self._row_index

    @row_index.setter
    def row_index(self, row_index):
        """
        Sets the row_index of this DetectionResultItem.
        The index number to indicate where anomaly points are located among all rows when there are no timestamps provided.


        :param row_index: The row_index of this DetectionResultItem.
        :type: int
        """
        self._row_index = row_index

    @property
    def score(self):
        """
        Gets the score of this DetectionResultItem.
        A significant score across multiple signals at timestamp/row level


        :return: The score of this DetectionResultItem.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this DetectionResultItem.
        A significant score across multiple signals at timestamp/row level


        :param score: The score of this DetectionResultItem.
        :type: float
        """
        self._score = score

    @property
    def anomalies(self):
        """
        **[Required]** Gets the anomalies of this DetectionResultItem.
        An array of anomalies associated with a given timestamp/row.


        :return: The anomalies of this DetectionResultItem.
        :rtype: list[oci.ai_anomaly_detection.models.Anomaly]
        """
        return self._anomalies

    @anomalies.setter
    def anomalies(self, anomalies):
        """
        Sets the anomalies of this DetectionResultItem.
        An array of anomalies associated with a given timestamp/row.


        :param anomalies: The anomalies of this DetectionResultItem.
        :type: list[oci.ai_anomaly_detection.models.Anomaly]
        """
        self._anomalies = anomalies

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
