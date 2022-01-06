# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScriptSummary(object):
    """
    Information about the script.
    """

    #: A constant which can be used with the content_type property of a ScriptSummary.
    #: This constant has a value of "SIDE"
    CONTENT_TYPE_SIDE = "SIDE"

    #: A constant which can be used with the content_type property of a ScriptSummary.
    #: This constant has a value of "JS"
    CONTENT_TYPE_JS = "JS"

    def __init__(self, **kwargs):
        """
        Initializes a new ScriptSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ScriptSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ScriptSummary.
        :type display_name: str

        :param content_type:
            The value to assign to the content_type property of this ScriptSummary.
            Allowed values for this property are: "SIDE", "JS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type content_type: str

        :param monitor_status_count_map:
            The value to assign to the monitor_status_count_map property of this ScriptSummary.
        :type monitor_status_count_map: oci.apm_synthetics.models.MonitorStatusCountMap

        :param time_created:
            The value to assign to the time_created property of this ScriptSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ScriptSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ScriptSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ScriptSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'content_type': 'str',
            'monitor_status_count_map': 'MonitorStatusCountMap',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'content_type': 'contentType',
            'monitor_status_count_map': 'monitorStatusCountMap',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._content_type = None
        self._monitor_status_count_map = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ScriptSummary.
        The `OCID`__ of the script.
        scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ScriptSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScriptSummary.
        The `OCID`__ of the script.
        scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ScriptSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ScriptSummary.
        Unique name that can be edited. The name should not contain any confidential information.


        :return: The display_name of this ScriptSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ScriptSummary.
        Unique name that can be edited. The name should not contain any confidential information.


        :param display_name: The display_name of this ScriptSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def content_type(self):
        """
        **[Required]** Gets the content_type of this ScriptSummary.
        Content type of the script.

        Allowed values for this property are: "SIDE", "JS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The content_type of this ScriptSummary.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this ScriptSummary.
        Content type of the script.


        :param content_type: The content_type of this ScriptSummary.
        :type: str
        """
        allowed_values = ["SIDE", "JS"]
        if not value_allowed_none_or_none_sentinel(content_type, allowed_values):
            content_type = 'UNKNOWN_ENUM_VALUE'
        self._content_type = content_type

    @property
    def monitor_status_count_map(self):
        """
        **[Required]** Gets the monitor_status_count_map of this ScriptSummary.

        :return: The monitor_status_count_map of this ScriptSummary.
        :rtype: oci.apm_synthetics.models.MonitorStatusCountMap
        """
        return self._monitor_status_count_map

    @monitor_status_count_map.setter
    def monitor_status_count_map(self, monitor_status_count_map):
        """
        Sets the monitor_status_count_map of this ScriptSummary.

        :param monitor_status_count_map: The monitor_status_count_map of this ScriptSummary.
        :type: oci.apm_synthetics.models.MonitorStatusCountMap
        """
        self._monitor_status_count_map = monitor_status_count_map

    @property
    def time_created(self):
        """
        Gets the time_created of this ScriptSummary.
        The time the resource was created, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ScriptSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ScriptSummary.
        The time the resource was created, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ScriptSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ScriptSummary.
        The time the resource was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ScriptSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ScriptSummary.
        The time the resource was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ScriptSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ScriptSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ScriptSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ScriptSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ScriptSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ScriptSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ScriptSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ScriptSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ScriptSummary.
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
