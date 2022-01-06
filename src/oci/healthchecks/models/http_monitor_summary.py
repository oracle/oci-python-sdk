# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HttpMonitorSummary(object):
    """
    A summary containing all of the mutable and immutable properties for an HTTP monitor.
    """

    #: A constant which can be used with the protocol property of a HttpMonitorSummary.
    #: This constant has a value of "HTTP"
    PROTOCOL_HTTP = "HTTP"

    #: A constant which can be used with the protocol property of a HttpMonitorSummary.
    #: This constant has a value of "HTTPS"
    PROTOCOL_HTTPS = "HTTPS"

    def __init__(self, **kwargs):
        """
        Initializes a new HttpMonitorSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this HttpMonitorSummary.
        :type id: str

        :param results_url:
            The value to assign to the results_url property of this HttpMonitorSummary.
        :type results_url: str

        :param home_region:
            The value to assign to the home_region property of this HttpMonitorSummary.
        :type home_region: str

        :param time_created:
            The value to assign to the time_created property of this HttpMonitorSummary.
        :type time_created: datetime

        :param compartment_id:
            The value to assign to the compartment_id property of this HttpMonitorSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this HttpMonitorSummary.
        :type display_name: str

        :param interval_in_seconds:
            The value to assign to the interval_in_seconds property of this HttpMonitorSummary.
        :type interval_in_seconds: int

        :param is_enabled:
            The value to assign to the is_enabled property of this HttpMonitorSummary.
        :type is_enabled: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this HttpMonitorSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this HttpMonitorSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param protocol:
            The value to assign to the protocol property of this HttpMonitorSummary.
            Allowed values for this property are: "HTTP", "HTTPS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        """
        self.swagger_types = {
            'id': 'str',
            'results_url': 'str',
            'home_region': 'str',
            'time_created': 'datetime',
            'compartment_id': 'str',
            'display_name': 'str',
            'interval_in_seconds': 'int',
            'is_enabled': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'protocol': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'results_url': 'resultsUrl',
            'home_region': 'homeRegion',
            'time_created': 'timeCreated',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'interval_in_seconds': 'intervalInSeconds',
            'is_enabled': 'isEnabled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'protocol': 'protocol'
        }

        self._id = None
        self._results_url = None
        self._home_region = None
        self._time_created = None
        self._compartment_id = None
        self._display_name = None
        self._interval_in_seconds = None
        self._is_enabled = None
        self._freeform_tags = None
        self._defined_tags = None
        self._protocol = None

    @property
    def id(self):
        """
        Gets the id of this HttpMonitorSummary.
        The OCID of the resource.


        :return: The id of this HttpMonitorSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HttpMonitorSummary.
        The OCID of the resource.


        :param id: The id of this HttpMonitorSummary.
        :type: str
        """
        self._id = id

    @property
    def results_url(self):
        """
        Gets the results_url of this HttpMonitorSummary.
        A URL for fetching the probe results.


        :return: The results_url of this HttpMonitorSummary.
        :rtype: str
        """
        return self._results_url

    @results_url.setter
    def results_url(self, results_url):
        """
        Sets the results_url of this HttpMonitorSummary.
        A URL for fetching the probe results.


        :param results_url: The results_url of this HttpMonitorSummary.
        :type: str
        """
        self._results_url = results_url

    @property
    def home_region(self):
        """
        Gets the home_region of this HttpMonitorSummary.
        The region where updates must be made and where results must be fetched from.


        :return: The home_region of this HttpMonitorSummary.
        :rtype: str
        """
        return self._home_region

    @home_region.setter
    def home_region(self, home_region):
        """
        Sets the home_region of this HttpMonitorSummary.
        The region where updates must be made and where results must be fetched from.


        :param home_region: The home_region of this HttpMonitorSummary.
        :type: str
        """
        self._home_region = home_region

    @property
    def time_created(self):
        """
        Gets the time_created of this HttpMonitorSummary.
        The RFC 3339-formatted creation date and time of the probe.


        :return: The time_created of this HttpMonitorSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this HttpMonitorSummary.
        The RFC 3339-formatted creation date and time of the probe.


        :param time_created: The time_created of this HttpMonitorSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this HttpMonitorSummary.
        The OCID of the compartment.


        :return: The compartment_id of this HttpMonitorSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this HttpMonitorSummary.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this HttpMonitorSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this HttpMonitorSummary.
        A user-friendly and mutable name suitable for display in a user interface.


        :return: The display_name of this HttpMonitorSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this HttpMonitorSummary.
        A user-friendly and mutable name suitable for display in a user interface.


        :param display_name: The display_name of this HttpMonitorSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def interval_in_seconds(self):
        """
        Gets the interval_in_seconds of this HttpMonitorSummary.
        The monitor interval in seconds. Valid values: 10, 30, and 60.


        :return: The interval_in_seconds of this HttpMonitorSummary.
        :rtype: int
        """
        return self._interval_in_seconds

    @interval_in_seconds.setter
    def interval_in_seconds(self, interval_in_seconds):
        """
        Sets the interval_in_seconds of this HttpMonitorSummary.
        The monitor interval in seconds. Valid values: 10, 30, and 60.


        :param interval_in_seconds: The interval_in_seconds of this HttpMonitorSummary.
        :type: int
        """
        self._interval_in_seconds = interval_in_seconds

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this HttpMonitorSummary.
        Enables or disables the monitor. Set to 'true' to launch monitoring.


        :return: The is_enabled of this HttpMonitorSummary.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this HttpMonitorSummary.
        Enables or disables the monitor. Set to 'true' to launch monitoring.


        :param is_enabled: The is_enabled of this HttpMonitorSummary.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this HttpMonitorSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace.  For more information,
        see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this HttpMonitorSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this HttpMonitorSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace.  For more information,
        see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this HttpMonitorSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this HttpMonitorSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this HttpMonitorSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this HttpMonitorSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this HttpMonitorSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def protocol(self):
        """
        Gets the protocol of this HttpMonitorSummary.
        Allowed values for this property are: "HTTP", "HTTPS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this HttpMonitorSummary.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this HttpMonitorSummary.

        :param protocol: The protocol of this HttpMonitorSummary.
        :type: str
        """
        allowed_values = ["HTTP", "HTTPS"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
