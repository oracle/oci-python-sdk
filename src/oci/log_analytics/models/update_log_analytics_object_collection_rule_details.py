# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateLogAnalyticsObjectCollectionRuleDetails(object):
    """
    Configuration of the collection rule to be updated.
    """

    #: A constant which can be used with the log_set_key property of a UpdateLogAnalyticsObjectCollectionRuleDetails.
    #: This constant has a value of "OBJECT_PATH"
    LOG_SET_KEY_OBJECT_PATH = "OBJECT_PATH"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateLogAnalyticsObjectCollectionRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type description: str

        :param log_group_id:
            The value to assign to the log_group_id property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type log_group_id: str

        :param log_source_name:
            The value to assign to the log_source_name property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type log_source_name: str

        :param entity_id:
            The value to assign to the entity_id property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type entity_id: str

        :param char_encoding:
            The value to assign to the char_encoding property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type char_encoding: str

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type is_enabled: bool

        :param timezone:
            The value to assign to the timezone property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type timezone: str

        :param log_set:
            The value to assign to the log_set property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type log_set: str

        :param log_set_key:
            The value to assign to the log_set_key property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
            Allowed values for this property are: "OBJECT_PATH"
        :type log_set_key: str

        :param log_set_ext_regex:
            The value to assign to the log_set_ext_regex property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type log_set_ext_regex: str

        :param overrides:
            The value to assign to the overrides property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type overrides: dict(str, list[PropertyOverride])

        :param object_name_filters:
            The value to assign to the object_name_filters property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type object_name_filters: list[str]

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'description': 'str',
            'log_group_id': 'str',
            'log_source_name': 'str',
            'entity_id': 'str',
            'char_encoding': 'str',
            'is_enabled': 'bool',
            'timezone': 'str',
            'log_set': 'str',
            'log_set_key': 'str',
            'log_set_ext_regex': 'str',
            'overrides': 'dict(str, list[PropertyOverride])',
            'object_name_filters': 'list[str]',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'description': 'description',
            'log_group_id': 'logGroupId',
            'log_source_name': 'logSourceName',
            'entity_id': 'entityId',
            'char_encoding': 'charEncoding',
            'is_enabled': 'isEnabled',
            'timezone': 'timezone',
            'log_set': 'logSet',
            'log_set_key': 'logSetKey',
            'log_set_ext_regex': 'logSetExtRegex',
            'overrides': 'overrides',
            'object_name_filters': 'objectNameFilters',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._description = None
        self._log_group_id = None
        self._log_source_name = None
        self._entity_id = None
        self._char_encoding = None
        self._is_enabled = None
        self._timezone = None
        self._log_set = None
        self._log_set_key = None
        self._log_set_ext_regex = None
        self._overrides = None
        self._object_name_filters = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def description(self):
        """
        Gets the description of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        A string that describes the details of the rule.
        Avoid entering confidential information.


        :return: The description of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        A string that describes the details of the rule.
        Avoid entering confidential information.


        :param description: The description of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: str
        """
        self._description = description

    @property
    def log_group_id(self):
        """
        Gets the log_group_id of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Logging Analytics Log group OCID to associate the processed logs with.


        :return: The log_group_id of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """
        Sets the log_group_id of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Logging Analytics Log group OCID to associate the processed logs with.


        :param log_group_id: The log_group_id of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: str
        """
        self._log_group_id = log_group_id

    @property
    def log_source_name(self):
        """
        Gets the log_source_name of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Name of the Logging Analytics Source to use for the processing.


        :return: The log_source_name of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: str
        """
        return self._log_source_name

    @log_source_name.setter
    def log_source_name(self, log_source_name):
        """
        Sets the log_source_name of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Name of the Logging Analytics Source to use for the processing.


        :param log_source_name: The log_source_name of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: str
        """
        self._log_source_name = log_source_name

    @property
    def entity_id(self):
        """
        Gets the entity_id of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Logging Analytics entity OCID. Associates the processed logs with the given entity (optional).


        :return: The entity_id of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Logging Analytics entity OCID. Associates the processed logs with the given entity (optional).


        :param entity_id: The entity_id of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: str
        """
        self._entity_id = entity_id

    @property
    def char_encoding(self):
        """
        Gets the char_encoding of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        An optional character encoding to aid in detecting the character encoding of the contents of the objects while processing.
        It is recommended to set this value as ISO_8859_1 when configuring content of the objects having more numeric characters,
        and very few alphabets.
        For e.g. this applies when configuring VCN Flow Logs.


        :return: The char_encoding of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: str
        """
        return self._char_encoding

    @char_encoding.setter
    def char_encoding(self, char_encoding):
        """
        Sets the char_encoding of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        An optional character encoding to aid in detecting the character encoding of the contents of the objects while processing.
        It is recommended to set this value as ISO_8859_1 when configuring content of the objects having more numeric characters,
        and very few alphabets.
        For e.g. this applies when configuring VCN Flow Logs.


        :param char_encoding: The char_encoding of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: str
        """
        self._char_encoding = char_encoding

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Whether or not this rule is currently enabled.


        :return: The is_enabled of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Whether or not this rule is currently enabled.


        :param is_enabled: The is_enabled of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def timezone(self):
        """
        Gets the timezone of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Timezone to be used when processing log entries whose timestamps do not include an explicit timezone.
        When this property is not specified, the timezone of the entity specified is used.
        If the entity is also not specified or do not have a valid timezone then UTC is used.


        :return: The timezone of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Timezone to be used when processing log entries whose timestamps do not include an explicit timezone.
        When this property is not specified, the timezone of the entity specified is used.
        If the entity is also not specified or do not have a valid timezone then UTC is used.


        :param timezone: The timezone of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: str
        """
        self._timezone = timezone

    @property
    def log_set(self):
        """
        Gets the log_set of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        The logSet to be associated with the processed logs. The logSet feature can be used by customers with high volume of data
        and this feature has to be enabled for a given tenancy prior to its usage.
        When logSetExtRegex value is provided, it will take precedence over this logSet value and logSet will be computed dynamically
        using logSetKey and logSetExtRegex.


        :return: The log_set of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: str
        """
        return self._log_set

    @log_set.setter
    def log_set(self, log_set):
        """
        Sets the log_set of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        The logSet to be associated with the processed logs. The logSet feature can be used by customers with high volume of data
        and this feature has to be enabled for a given tenancy prior to its usage.
        When logSetExtRegex value is provided, it will take precedence over this logSet value and logSet will be computed dynamically
        using logSetKey and logSetExtRegex.


        :param log_set: The log_set of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: str
        """
        self._log_set = log_set

    @property
    def log_set_key(self):
        """
        Gets the log_set_key of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        An optional parameter to indicate from where the logSet to be extracted using logSetExtRegex. Default value is OBJECT_PATH (e.g. /n/<namespace>/b/<bucketname>/o/<objectname>).

        Allowed values for this property are: "OBJECT_PATH"


        :return: The log_set_key of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: str
        """
        return self._log_set_key

    @log_set_key.setter
    def log_set_key(self, log_set_key):
        """
        Sets the log_set_key of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        An optional parameter to indicate from where the logSet to be extracted using logSetExtRegex. Default value is OBJECT_PATH (e.g. /n/<namespace>/b/<bucketname>/o/<objectname>).


        :param log_set_key: The log_set_key of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: str
        """
        allowed_values = ["OBJECT_PATH"]
        if not value_allowed_none_or_none_sentinel(log_set_key, allowed_values):
            raise ValueError(
                "Invalid value for `log_set_key`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._log_set_key = log_set_key

    @property
    def log_set_ext_regex(self):
        """
        Gets the log_set_ext_regex of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        The regex to be applied against given logSetKey. Regex has to be in string escaped format.


        :return: The log_set_ext_regex of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: str
        """
        return self._log_set_ext_regex

    @log_set_ext_regex.setter
    def log_set_ext_regex(self, log_set_ext_regex):
        """
        Sets the log_set_ext_regex of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        The regex to be applied against given logSetKey. Regex has to be in string escaped format.


        :param log_set_ext_regex: The log_set_ext_regex of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: str
        """
        self._log_set_ext_regex = log_set_ext_regex

    @property
    def overrides(self):
        """
        Gets the overrides of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Use this to override some property values which are defined at bucket level to the scope of object.
        Supported propeties for override are: logSourceName, charEncoding, entityId.
        Supported matchType for override are \"contains\".


        :return: The overrides of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: dict(str, list[PropertyOverride])
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """
        Sets the overrides of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Use this to override some property values which are defined at bucket level to the scope of object.
        Supported propeties for override are: logSourceName, charEncoding, entityId.
        Supported matchType for override are \"contains\".


        :param overrides: The overrides of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: dict(str, list[PropertyOverride])
        """
        self._overrides = overrides

    @property
    def object_name_filters(self):
        """
        Gets the object_name_filters of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        When the filters are provided, only the objects matching the filters are picked up for processing.
        The matchType supported is exact match and accommodates wildcard \"*\".
        For more information on filters, see `Event Filters`__.

        __ https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/filterevents.htm


        :return: The object_name_filters of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: list[str]
        """
        return self._object_name_filters

    @object_name_filters.setter
    def object_name_filters(self, object_name_filters):
        """
        Sets the object_name_filters of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        When the filters are provided, only the objects matching the filters are picked up for processing.
        The matchType supported is exact match and accommodates wildcard \"*\".
        For more information on filters, see `Event Filters`__.

        __ https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/filterevents.htm


        :param object_name_filters: The object_name_filters of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: list[str]
        """
        self._object_name_filters = object_name_filters

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateLogAnalyticsObjectCollectionRuleDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
