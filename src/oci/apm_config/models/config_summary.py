# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigSummary(object):
    """
    A description of a configuration item. It specifes all the properties that define the configuration item.
    """

    #: A constant which can be used with the config_type property of a ConfigSummary.
    #: This constant has a value of "SPAN_FILTER"
    CONFIG_TYPE_SPAN_FILTER = "SPAN_FILTER"

    #: A constant which can be used with the config_type property of a ConfigSummary.
    #: This constant has a value of "METRIC_GROUP"
    CONFIG_TYPE_METRIC_GROUP = "METRIC_GROUP"

    #: A constant which can be used with the config_type property of a ConfigSummary.
    #: This constant has a value of "APDEX"
    CONFIG_TYPE_APDEX = "APDEX"

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.apm_config.models.MetricGroupSummary`
        * :class:`~oci.apm_config.models.ApdexRulesSummary`
        * :class:`~oci.apm_config.models.SpanFilterSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ConfigSummary.
        :type id: str

        :param config_type:
            The value to assign to the config_type property of this ConfigSummary.
            Allowed values for this property are: "SPAN_FILTER", "METRIC_GROUP", "APDEX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type config_type: str

        :param time_created:
            The value to assign to the time_created property of this ConfigSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ConfigSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ConfigSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ConfigSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'config_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'config_type': 'configType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._config_type = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['configType']

        if type == 'METRIC_GROUP':
            return 'MetricGroupSummary'

        if type == 'APDEX':
            return 'ApdexRulesSummary'

        if type == 'SPAN_FILTER':
            return 'SpanFilterSummary'
        else:
            return 'ConfigSummary'

    @property
    def id(self):
        """
        Gets the id of this ConfigSummary.
        The `OCID`__ of the configuration item. An OCID is generated
        when the item is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ConfigSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConfigSummary.
        The `OCID`__ of the configuration item. An OCID is generated
        when the item is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ConfigSummary.
        :type: str
        """
        self._id = id

    @property
    def config_type(self):
        """
        **[Required]** Gets the config_type of this ConfigSummary.
        The type of configuration item.

        Allowed values for this property are: "SPAN_FILTER", "METRIC_GROUP", "APDEX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The config_type of this ConfigSummary.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """
        Sets the config_type of this ConfigSummary.
        The type of configuration item.


        :param config_type: The config_type of this ConfigSummary.
        :type: str
        """
        allowed_values = ["SPAN_FILTER", "METRIC_GROUP", "APDEX"]
        if not value_allowed_none_or_none_sentinel(config_type, allowed_values):
            config_type = 'UNKNOWN_ENUM_VALUE'
        self._config_type = config_type

    @property
    def time_created(self):
        """
        Gets the time_created of this ConfigSummary.
        The time the resource was created, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ConfigSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ConfigSummary.
        The time the resource was created, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ConfigSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ConfigSummary.
        The time the resource was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ConfigSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ConfigSummary.
        The time the resource was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2020-02-13T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ConfigSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ConfigSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ConfigSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ConfigSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ConfigSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ConfigSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ConfigSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ConfigSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ConfigSummary.
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
