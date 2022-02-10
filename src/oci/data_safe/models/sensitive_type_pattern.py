# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .sensitive_type import SensitiveType
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SensitiveTypePattern(SensitiveType):
    """
    Details of the sensitive type.
    """

    #: A constant which can be used with the search_type property of a SensitiveTypePattern.
    #: This constant has a value of "OR"
    SEARCH_TYPE_OR = "OR"

    #: A constant which can be used with the search_type property of a SensitiveTypePattern.
    #: This constant has a value of "AND"
    SEARCH_TYPE_AND = "AND"

    def __init__(self, **kwargs):
        """
        Initializes a new SensitiveTypePattern object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.SensitiveTypePattern.entity_type` attribute
        of this class is ``SENSITIVE_TYPE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SensitiveTypePattern.
        :type id: str

        :param entity_type:
            The value to assign to the entity_type property of this SensitiveTypePattern.
            Allowed values for this property are: "SENSITIVE_TYPE", "SENSITIVE_CATEGORY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_type: str

        :param display_name:
            The value to assign to the display_name property of this SensitiveTypePattern.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SensitiveTypePattern.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SensitiveTypePattern.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param short_name:
            The value to assign to the short_name property of this SensitiveTypePattern.
        :type short_name: str

        :param source:
            The value to assign to the source property of this SensitiveTypePattern.
            Allowed values for this property are: "ORACLE", "USER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source: str

        :param time_created:
            The value to assign to the time_created property of this SensitiveTypePattern.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SensitiveTypePattern.
        :type time_updated: datetime

        :param description:
            The value to assign to the description property of this SensitiveTypePattern.
        :type description: str

        :param parent_category_id:
            The value to assign to the parent_category_id property of this SensitiveTypePattern.
        :type parent_category_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SensitiveTypePattern.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SensitiveTypePattern.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SensitiveTypePattern.
        :type system_tags: dict(str, dict(str, object))

        :param name_pattern:
            The value to assign to the name_pattern property of this SensitiveTypePattern.
        :type name_pattern: str

        :param comment_pattern:
            The value to assign to the comment_pattern property of this SensitiveTypePattern.
        :type comment_pattern: str

        :param data_pattern:
            The value to assign to the data_pattern property of this SensitiveTypePattern.
        :type data_pattern: str

        :param search_type:
            The value to assign to the search_type property of this SensitiveTypePattern.
            Allowed values for this property are: "OR", "AND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type search_type: str

        :param default_masking_format_id:
            The value to assign to the default_masking_format_id property of this SensitiveTypePattern.
        :type default_masking_format_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'entity_type': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'short_name': 'str',
            'source': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'description': 'str',
            'parent_category_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'name_pattern': 'str',
            'comment_pattern': 'str',
            'data_pattern': 'str',
            'search_type': 'str',
            'default_masking_format_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'entity_type': 'entityType',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'short_name': 'shortName',
            'source': 'source',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'description': 'description',
            'parent_category_id': 'parentCategoryId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'name_pattern': 'namePattern',
            'comment_pattern': 'commentPattern',
            'data_pattern': 'dataPattern',
            'search_type': 'searchType',
            'default_masking_format_id': 'defaultMaskingFormatId'
        }

        self._id = None
        self._entity_type = None
        self._display_name = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._short_name = None
        self._source = None
        self._time_created = None
        self._time_updated = None
        self._description = None
        self._parent_category_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._name_pattern = None
        self._comment_pattern = None
        self._data_pattern = None
        self._search_type = None
        self._default_masking_format_id = None
        self._entity_type = 'SENSITIVE_TYPE'

    @property
    def name_pattern(self):
        """
        Gets the name_pattern of this SensitiveTypePattern.
        A regular expression to be used by data discovery for matching column names.


        :return: The name_pattern of this SensitiveTypePattern.
        :rtype: str
        """
        return self._name_pattern

    @name_pattern.setter
    def name_pattern(self, name_pattern):
        """
        Sets the name_pattern of this SensitiveTypePattern.
        A regular expression to be used by data discovery for matching column names.


        :param name_pattern: The name_pattern of this SensitiveTypePattern.
        :type: str
        """
        self._name_pattern = name_pattern

    @property
    def comment_pattern(self):
        """
        Gets the comment_pattern of this SensitiveTypePattern.
        A regular expression to be used by data discovery for matching column comments.


        :return: The comment_pattern of this SensitiveTypePattern.
        :rtype: str
        """
        return self._comment_pattern

    @comment_pattern.setter
    def comment_pattern(self, comment_pattern):
        """
        Sets the comment_pattern of this SensitiveTypePattern.
        A regular expression to be used by data discovery for matching column comments.


        :param comment_pattern: The comment_pattern of this SensitiveTypePattern.
        :type: str
        """
        self._comment_pattern = comment_pattern

    @property
    def data_pattern(self):
        """
        Gets the data_pattern of this SensitiveTypePattern.
        A regular expression to be used by data discovery for matching column data values.


        :return: The data_pattern of this SensitiveTypePattern.
        :rtype: str
        """
        return self._data_pattern

    @data_pattern.setter
    def data_pattern(self, data_pattern):
        """
        Sets the data_pattern of this SensitiveTypePattern.
        A regular expression to be used by data discovery for matching column data values.


        :param data_pattern: The data_pattern of this SensitiveTypePattern.
        :type: str
        """
        self._data_pattern = data_pattern

    @property
    def search_type(self):
        """
        Gets the search_type of this SensitiveTypePattern.
        The search type indicating how the column name, comment and data patterns should be used by data discovery.
        `Learn more`__.

        __ https://docs.oracle.com/en/cloud/paas/data-safe/udscs/sensitive-types.html#GUID-1D1AD98E-B93F-4FF2-80AE-CB7D8A14F6CC

        Allowed values for this property are: "OR", "AND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The search_type of this SensitiveTypePattern.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        """
        Sets the search_type of this SensitiveTypePattern.
        The search type indicating how the column name, comment and data patterns should be used by data discovery.
        `Learn more`__.

        __ https://docs.oracle.com/en/cloud/paas/data-safe/udscs/sensitive-types.html#GUID-1D1AD98E-B93F-4FF2-80AE-CB7D8A14F6CC


        :param search_type: The search_type of this SensitiveTypePattern.
        :type: str
        """
        allowed_values = ["OR", "AND"]
        if not value_allowed_none_or_none_sentinel(search_type, allowed_values):
            search_type = 'UNKNOWN_ENUM_VALUE'
        self._search_type = search_type

    @property
    def default_masking_format_id(self):
        """
        Gets the default_masking_format_id of this SensitiveTypePattern.
        The OCID of the library masking format that should be used to mask the sensitive columns associated with the sensitive type.


        :return: The default_masking_format_id of this SensitiveTypePattern.
        :rtype: str
        """
        return self._default_masking_format_id

    @default_masking_format_id.setter
    def default_masking_format_id(self, default_masking_format_id):
        """
        Sets the default_masking_format_id of this SensitiveTypePattern.
        The OCID of the library masking format that should be used to mask the sensitive columns associated with the sensitive type.


        :param default_masking_format_id: The default_masking_format_id of this SensitiveTypePattern.
        :type: str
        """
        self._default_masking_format_id = default_masking_format_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
