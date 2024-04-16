# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OnPremiseVantagePointSummary(object):
    """
    Information about On-premise vantage point.
    """

    #: A constant which can be used with the type property of a OnPremiseVantagePointSummary.
    #: This constant has a value of "ON_PREMISE_DOCKER_VANTAGE_POINT"
    TYPE_ON_PREMISE_DOCKER_VANTAGE_POINT = "ON_PREMISE_DOCKER_VANTAGE_POINT"

    def __init__(self, **kwargs):
        """
        Initializes a new OnPremiseVantagePointSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OnPremiseVantagePointSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this OnPremiseVantagePointSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this OnPremiseVantagePointSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this OnPremiseVantagePointSummary.
            Allowed values for this property are: "ON_PREMISE_DOCKER_VANTAGE_POINT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param description:
            The value to assign to the description property of this OnPremiseVantagePointSummary.
        :type description: str

        :param workers_summary:
            The value to assign to the workers_summary property of this OnPremiseVantagePointSummary.
        :type workers_summary: oci.apm_synthetics.models.WorkersSummary

        :param time_created:
            The value to assign to the time_created property of this OnPremiseVantagePointSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OnPremiseVantagePointSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OnPremiseVantagePointSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OnPremiseVantagePointSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'name': 'str',
            'type': 'str',
            'description': 'str',
            'workers_summary': 'WorkersSummary',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'name': 'name',
            'type': 'type',
            'description': 'description',
            'workers_summary': 'workersSummary',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._name = None
        self._type = None
        self._description = None
        self._workers_summary = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OnPremiseVantagePointSummary.
        The `OCID`__ of the On-premise vantage point.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this OnPremiseVantagePointSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OnPremiseVantagePointSummary.
        The `OCID`__ of the On-premise vantage point.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this OnPremiseVantagePointSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OnPremiseVantagePointSummary.
        Unique permanent name of the On-premise vantage point.


        :return: The display_name of this OnPremiseVantagePointSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OnPremiseVantagePointSummary.
        Unique permanent name of the On-premise vantage point.


        :param display_name: The display_name of this OnPremiseVantagePointSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this OnPremiseVantagePointSummary.
        Unique On-premise vantage point name that cannot be edited. The name should not contain any confidential information.


        :return: The name of this OnPremiseVantagePointSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OnPremiseVantagePointSummary.
        Unique On-premise vantage point name that cannot be edited. The name should not contain any confidential information.


        :param name: The name of this OnPremiseVantagePointSummary.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this OnPremiseVantagePointSummary.
        Type of On-premise vantage point.

        Allowed values for this property are: "ON_PREMISE_DOCKER_VANTAGE_POINT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this OnPremiseVantagePointSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this OnPremiseVantagePointSummary.
        Type of On-premise vantage point.


        :param type: The type of this OnPremiseVantagePointSummary.
        :type: str
        """
        allowed_values = ["ON_PREMISE_DOCKER_VANTAGE_POINT"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def description(self):
        """
        Gets the description of this OnPremiseVantagePointSummary.
        A short description about the On-premise vantage point.


        :return: The description of this OnPremiseVantagePointSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OnPremiseVantagePointSummary.
        A short description about the On-premise vantage point.


        :param description: The description of this OnPremiseVantagePointSummary.
        :type: str
        """
        self._description = description

    @property
    def workers_summary(self):
        """
        **[Required]** Gets the workers_summary of this OnPremiseVantagePointSummary.

        :return: The workers_summary of this OnPremiseVantagePointSummary.
        :rtype: oci.apm_synthetics.models.WorkersSummary
        """
        return self._workers_summary

    @workers_summary.setter
    def workers_summary(self, workers_summary):
        """
        Sets the workers_summary of this OnPremiseVantagePointSummary.

        :param workers_summary: The workers_summary of this OnPremiseVantagePointSummary.
        :type: oci.apm_synthetics.models.WorkersSummary
        """
        self._workers_summary = workers_summary

    @property
    def time_created(self):
        """
        Gets the time_created of this OnPremiseVantagePointSummary.
        The time the resource was created, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this OnPremiseVantagePointSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OnPremiseVantagePointSummary.
        The time the resource was created, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this OnPremiseVantagePointSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OnPremiseVantagePointSummary.
        The time the resource was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this OnPremiseVantagePointSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OnPremiseVantagePointSummary.
        The time the resource was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this OnPremiseVantagePointSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OnPremiseVantagePointSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OnPremiseVantagePointSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OnPremiseVantagePointSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OnPremiseVantagePointSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OnPremiseVantagePointSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OnPremiseVantagePointSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OnPremiseVantagePointSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OnPremiseVantagePointSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other