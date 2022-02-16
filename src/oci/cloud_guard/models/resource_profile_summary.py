# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceProfileSummary(object):
    """
    Resource profile summary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceProfileSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sightings_count:
            The value to assign to the sightings_count property of this ResourceProfileSummary.
        :type sightings_count: int

        :param id:
            The value to assign to the id property of this ResourceProfileSummary.
        :type id: str

        :param resource_id:
            The value to assign to the resource_id property of this ResourceProfileSummary.
        :type resource_id: str

        :param display_name:
            The value to assign to the display_name property of this ResourceProfileSummary.
        :type display_name: str

        :param type:
            The value to assign to the type property of this ResourceProfileSummary.
        :type type: str

        :param risk_score:
            The value to assign to the risk_score property of this ResourceProfileSummary.
        :type risk_score: float

        :param tactics:
            The value to assign to the tactics property of this ResourceProfileSummary.
        :type tactics: list[oci.cloud_guard.models.TacticSummary]

        :param time_first_detected:
            The value to assign to the time_first_detected property of this ResourceProfileSummary.
        :type time_first_detected: datetime

        :param time_last_detected:
            The value to assign to the time_last_detected property of this ResourceProfileSummary.
        :type time_last_detected: datetime

        :param problems_count:
            The value to assign to the problems_count property of this ResourceProfileSummary.
        :type problems_count: int

        """
        self.swagger_types = {
            'sightings_count': 'int',
            'id': 'str',
            'resource_id': 'str',
            'display_name': 'str',
            'type': 'str',
            'risk_score': 'float',
            'tactics': 'list[TacticSummary]',
            'time_first_detected': 'datetime',
            'time_last_detected': 'datetime',
            'problems_count': 'int'
        }

        self.attribute_map = {
            'sightings_count': 'sightingsCount',
            'id': 'id',
            'resource_id': 'resourceId',
            'display_name': 'displayName',
            'type': 'type',
            'risk_score': 'riskScore',
            'tactics': 'tactics',
            'time_first_detected': 'timeFirstDetected',
            'time_last_detected': 'timeLastDetected',
            'problems_count': 'problemsCount'
        }

        self._sightings_count = None
        self._id = None
        self._resource_id = None
        self._display_name = None
        self._type = None
        self._risk_score = None
        self._tactics = None
        self._time_first_detected = None
        self._time_last_detected = None
        self._problems_count = None

    @property
    def sightings_count(self):
        """
        Gets the sightings_count of this ResourceProfileSummary.
        Number of sightings associated with this resource profile


        :return: The sightings_count of this ResourceProfileSummary.
        :rtype: int
        """
        return self._sightings_count

    @sightings_count.setter
    def sightings_count(self, sightings_count):
        """
        Sets the sightings_count of this ResourceProfileSummary.
        Number of sightings associated with this resource profile


        :param sightings_count: The sightings_count of this ResourceProfileSummary.
        :type: int
        """
        self._sightings_count = sightings_count

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ResourceProfileSummary.
        Unique identifier for resource profile


        :return: The id of this ResourceProfileSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ResourceProfileSummary.
        Unique identifier for resource profile


        :param id: The id of this ResourceProfileSummary.
        :type: str
        """
        self._id = id

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this ResourceProfileSummary.
        Unique identifier for resource profile


        :return: The resource_id of this ResourceProfileSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this ResourceProfileSummary.
        Unique identifier for resource profile


        :param resource_id: The resource_id of this ResourceProfileSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ResourceProfileSummary.
        Resource name for resource profile


        :return: The display_name of this ResourceProfileSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ResourceProfileSummary.
        Resource name for resource profile


        :param display_name: The display_name of this ResourceProfileSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ResourceProfileSummary.
        Resource type for resource profile


        :return: The type of this ResourceProfileSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ResourceProfileSummary.
        Resource type for resource profile


        :param type: The type of this ResourceProfileSummary.
        :type: str
        """
        self._type = type

    @property
    def risk_score(self):
        """
        **[Required]** Gets the risk_score of this ResourceProfileSummary.
        Risk Score for the resource profile


        :return: The risk_score of this ResourceProfileSummary.
        :rtype: float
        """
        return self._risk_score

    @risk_score.setter
    def risk_score(self, risk_score):
        """
        Sets the risk_score of this ResourceProfileSummary.
        Risk Score for the resource profile


        :param risk_score: The risk_score of this ResourceProfileSummary.
        :type: float
        """
        self._risk_score = risk_score

    @property
    def tactics(self):
        """
        **[Required]** Gets the tactics of this ResourceProfileSummary.
        List of tactic summary associated with the resource profile.


        :return: The tactics of this ResourceProfileSummary.
        :rtype: list[oci.cloud_guard.models.TacticSummary]
        """
        return self._tactics

    @tactics.setter
    def tactics(self, tactics):
        """
        Sets the tactics of this ResourceProfileSummary.
        List of tactic summary associated with the resource profile.


        :param tactics: The tactics of this ResourceProfileSummary.
        :type: list[oci.cloud_guard.models.TacticSummary]
        """
        self._tactics = tactics

    @property
    def time_first_detected(self):
        """
        **[Required]** Gets the time_first_detected of this ResourceProfileSummary.
        The date and time the resource profile was first detected. Format defined by RFC3339.


        :return: The time_first_detected of this ResourceProfileSummary.
        :rtype: datetime
        """
        return self._time_first_detected

    @time_first_detected.setter
    def time_first_detected(self, time_first_detected):
        """
        Sets the time_first_detected of this ResourceProfileSummary.
        The date and time the resource profile was first detected. Format defined by RFC3339.


        :param time_first_detected: The time_first_detected of this ResourceProfileSummary.
        :type: datetime
        """
        self._time_first_detected = time_first_detected

    @property
    def time_last_detected(self):
        """
        **[Required]** Gets the time_last_detected of this ResourceProfileSummary.
        The date and time the resource profile was last detected. Format defined by RFC3339.


        :return: The time_last_detected of this ResourceProfileSummary.
        :rtype: datetime
        """
        return self._time_last_detected

    @time_last_detected.setter
    def time_last_detected(self, time_last_detected):
        """
        Sets the time_last_detected of this ResourceProfileSummary.
        The date and time the resource profile was last detected. Format defined by RFC3339.


        :param time_last_detected: The time_last_detected of this ResourceProfileSummary.
        :type: datetime
        """
        self._time_last_detected = time_last_detected

    @property
    def problems_count(self):
        """
        Gets the problems_count of this ResourceProfileSummary.
        Number of problems associated with this resource profile


        :return: The problems_count of this ResourceProfileSummary.
        :rtype: int
        """
        return self._problems_count

    @problems_count.setter
    def problems_count(self, problems_count):
        """
        Sets the problems_count of this ResourceProfileSummary.
        Number of problems associated with this resource profile


        :param problems_count: The problems_count of this ResourceProfileSummary.
        :type: int
        """
        self._problems_count = problems_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
