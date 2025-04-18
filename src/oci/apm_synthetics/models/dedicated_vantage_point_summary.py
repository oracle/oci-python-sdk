# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DedicatedVantagePointSummary(object):
    """
    Information about dedicated vantage points.
    """

    #: A constant which can be used with the status property of a DedicatedVantagePointSummary.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a DedicatedVantagePointSummary.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new DedicatedVantagePointSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DedicatedVantagePointSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DedicatedVantagePointSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this DedicatedVantagePointSummary.
        :type name: str

        :param status:
            The value to assign to the status property of this DedicatedVantagePointSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param dvp_stack_details:
            The value to assign to the dvp_stack_details property of this DedicatedVantagePointSummary.
        :type dvp_stack_details: oci.apm_synthetics.models.DvpStackDetails

        :param region:
            The value to assign to the region property of this DedicatedVantagePointSummary.
        :type region: str

        :param time_created:
            The value to assign to the time_created property of this DedicatedVantagePointSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DedicatedVantagePointSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DedicatedVantagePointSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DedicatedVantagePointSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param monitor_status_count_map:
            The value to assign to the monitor_status_count_map property of this DedicatedVantagePointSummary.
        :type monitor_status_count_map: oci.apm_synthetics.models.MonitorStatusCountMap

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'name': 'str',
            'status': 'str',
            'dvp_stack_details': 'DvpStackDetails',
            'region': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'monitor_status_count_map': 'MonitorStatusCountMap'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'name': 'name',
            'status': 'status',
            'dvp_stack_details': 'dvpStackDetails',
            'region': 'region',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'monitor_status_count_map': 'monitorStatusCountMap'
        }
        self._id = None
        self._display_name = None
        self._name = None
        self._status = None
        self._dvp_stack_details = None
        self._region = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._monitor_status_count_map = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DedicatedVantagePointSummary.
        The `OCID`__ of the dedicated vantage point.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DedicatedVantagePointSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DedicatedVantagePointSummary.
        The `OCID`__ of the dedicated vantage point.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DedicatedVantagePointSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DedicatedVantagePointSummary.
        Unique dedicated vantage point name that cannot be edited. The name should not contain any confidential information.


        :return: The display_name of this DedicatedVantagePointSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DedicatedVantagePointSummary.
        Unique dedicated vantage point name that cannot be edited. The name should not contain any confidential information.


        :param display_name: The display_name of this DedicatedVantagePointSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DedicatedVantagePointSummary.
        Unique permanent name of the vantage point.


        :return: The name of this DedicatedVantagePointSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DedicatedVantagePointSummary.
        Unique permanent name of the vantage point.


        :param name: The name of this DedicatedVantagePointSummary.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this DedicatedVantagePointSummary.
        Status of the dedicated vantage point.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this DedicatedVantagePointSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DedicatedVantagePointSummary.
        Status of the dedicated vantage point.


        :param status: The status of this DedicatedVantagePointSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def dvp_stack_details(self):
        """
        **[Required]** Gets the dvp_stack_details of this DedicatedVantagePointSummary.

        :return: The dvp_stack_details of this DedicatedVantagePointSummary.
        :rtype: oci.apm_synthetics.models.DvpStackDetails
        """
        return self._dvp_stack_details

    @dvp_stack_details.setter
    def dvp_stack_details(self, dvp_stack_details):
        """
        Sets the dvp_stack_details of this DedicatedVantagePointSummary.

        :param dvp_stack_details: The dvp_stack_details of this DedicatedVantagePointSummary.
        :type: oci.apm_synthetics.models.DvpStackDetails
        """
        self._dvp_stack_details = dvp_stack_details

    @property
    def region(self):
        """
        **[Required]** Gets the region of this DedicatedVantagePointSummary.
        Name of the region.


        :return: The region of this DedicatedVantagePointSummary.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this DedicatedVantagePointSummary.
        Name of the region.


        :param region: The region of this DedicatedVantagePointSummary.
        :type: str
        """
        self._region = region

    @property
    def time_created(self):
        """
        Gets the time_created of this DedicatedVantagePointSummary.
        The time the resource was created, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DedicatedVantagePointSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DedicatedVantagePointSummary.
        The time the resource was created, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DedicatedVantagePointSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DedicatedVantagePointSummary.
        The time the resource was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this DedicatedVantagePointSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DedicatedVantagePointSummary.
        The time the resource was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this DedicatedVantagePointSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DedicatedVantagePointSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DedicatedVantagePointSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DedicatedVantagePointSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DedicatedVantagePointSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DedicatedVantagePointSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DedicatedVantagePointSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DedicatedVantagePointSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DedicatedVantagePointSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def monitor_status_count_map(self):
        """
        **[Required]** Gets the monitor_status_count_map of this DedicatedVantagePointSummary.

        :return: The monitor_status_count_map of this DedicatedVantagePointSummary.
        :rtype: oci.apm_synthetics.models.MonitorStatusCountMap
        """
        return self._monitor_status_count_map

    @monitor_status_count_map.setter
    def monitor_status_count_map(self, monitor_status_count_map):
        """
        Sets the monitor_status_count_map of this DedicatedVantagePointSummary.

        :param monitor_status_count_map: The monitor_status_count_map of this DedicatedVantagePointSummary.
        :type: oci.apm_synthetics.models.MonitorStatusCountMap
        """
        self._monitor_status_count_map = monitor_status_count_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
