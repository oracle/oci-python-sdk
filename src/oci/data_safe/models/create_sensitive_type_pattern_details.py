# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_sensitive_type_details import CreateSensitiveTypeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSensitiveTypePatternDetails(CreateSensitiveTypeDetails):
    """
    Details to create a new sensitive type with regular expressions.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSensitiveTypePatternDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.CreateSensitiveTypePatternDetails.entity_type` attribute
        of this class is ``SENSITIVE_TYPE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_type:
            The value to assign to the entity_type property of this CreateSensitiveTypePatternDetails.
            Allowed values for this property are: "SENSITIVE_TYPE", "SENSITIVE_CATEGORY"
        :type entity_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateSensitiveTypePatternDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSensitiveTypePatternDetails.
        :type compartment_id: str

        :param short_name:
            The value to assign to the short_name property of this CreateSensitiveTypePatternDetails.
        :type short_name: str

        :param description:
            The value to assign to the description property of this CreateSensitiveTypePatternDetails.
        :type description: str

        :param parent_category_id:
            The value to assign to the parent_category_id property of this CreateSensitiveTypePatternDetails.
        :type parent_category_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSensitiveTypePatternDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSensitiveTypePatternDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param name_pattern:
            The value to assign to the name_pattern property of this CreateSensitiveTypePatternDetails.
        :type name_pattern: str

        :param comment_pattern:
            The value to assign to the comment_pattern property of this CreateSensitiveTypePatternDetails.
        :type comment_pattern: str

        :param data_pattern:
            The value to assign to the data_pattern property of this CreateSensitiveTypePatternDetails.
        :type data_pattern: str

        :param search_type:
            The value to assign to the search_type property of this CreateSensitiveTypePatternDetails.
        :type search_type: str

        :param default_masking_format_id:
            The value to assign to the default_masking_format_id property of this CreateSensitiveTypePatternDetails.
        :type default_masking_format_id: str

        """
        self.swagger_types = {
            'entity_type': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'short_name': 'str',
            'description': 'str',
            'parent_category_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'name_pattern': 'str',
            'comment_pattern': 'str',
            'data_pattern': 'str',
            'search_type': 'str',
            'default_masking_format_id': 'str'
        }

        self.attribute_map = {
            'entity_type': 'entityType',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'short_name': 'shortName',
            'description': 'description',
            'parent_category_id': 'parentCategoryId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'name_pattern': 'namePattern',
            'comment_pattern': 'commentPattern',
            'data_pattern': 'dataPattern',
            'search_type': 'searchType',
            'default_masking_format_id': 'defaultMaskingFormatId'
        }

        self._entity_type = None
        self._display_name = None
        self._compartment_id = None
        self._short_name = None
        self._description = None
        self._parent_category_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._name_pattern = None
        self._comment_pattern = None
        self._data_pattern = None
        self._search_type = None
        self._default_masking_format_id = None
        self._entity_type = 'SENSITIVE_TYPE'

    @property
    def name_pattern(self):
        """
        Gets the name_pattern of this CreateSensitiveTypePatternDetails.
        A regular expression to be used by data discovery for matching column names.


        :return: The name_pattern of this CreateSensitiveTypePatternDetails.
        :rtype: str
        """
        return self._name_pattern

    @name_pattern.setter
    def name_pattern(self, name_pattern):
        """
        Sets the name_pattern of this CreateSensitiveTypePatternDetails.
        A regular expression to be used by data discovery for matching column names.


        :param name_pattern: The name_pattern of this CreateSensitiveTypePatternDetails.
        :type: str
        """
        self._name_pattern = name_pattern

    @property
    def comment_pattern(self):
        """
        Gets the comment_pattern of this CreateSensitiveTypePatternDetails.
        A regular expression to be used by data discovery for matching column comments.


        :return: The comment_pattern of this CreateSensitiveTypePatternDetails.
        :rtype: str
        """
        return self._comment_pattern

    @comment_pattern.setter
    def comment_pattern(self, comment_pattern):
        """
        Sets the comment_pattern of this CreateSensitiveTypePatternDetails.
        A regular expression to be used by data discovery for matching column comments.


        :param comment_pattern: The comment_pattern of this CreateSensitiveTypePatternDetails.
        :type: str
        """
        self._comment_pattern = comment_pattern

    @property
    def data_pattern(self):
        """
        Gets the data_pattern of this CreateSensitiveTypePatternDetails.
        A regular expression to be used by data discovery for matching column data values.


        :return: The data_pattern of this CreateSensitiveTypePatternDetails.
        :rtype: str
        """
        return self._data_pattern

    @data_pattern.setter
    def data_pattern(self, data_pattern):
        """
        Sets the data_pattern of this CreateSensitiveTypePatternDetails.
        A regular expression to be used by data discovery for matching column data values.


        :param data_pattern: The data_pattern of this CreateSensitiveTypePatternDetails.
        :type: str
        """
        self._data_pattern = data_pattern

    @property
    def search_type(self):
        """
        Gets the search_type of this CreateSensitiveTypePatternDetails.
        The search type indicating how the column name, comment and data patterns should be used by data discovery.
        `Learn more`__.

        __ https://docs.oracle.com/en/cloud/paas/data-safe/udscs/sensitive-types.html#GUID-1D1AD98E-B93F-4FF2-80AE-CB7D8A14F6CC


        :return: The search_type of this CreateSensitiveTypePatternDetails.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        """
        Sets the search_type of this CreateSensitiveTypePatternDetails.
        The search type indicating how the column name, comment and data patterns should be used by data discovery.
        `Learn more`__.

        __ https://docs.oracle.com/en/cloud/paas/data-safe/udscs/sensitive-types.html#GUID-1D1AD98E-B93F-4FF2-80AE-CB7D8A14F6CC


        :param search_type: The search_type of this CreateSensitiveTypePatternDetails.
        :type: str
        """
        self._search_type = search_type

    @property
    def default_masking_format_id(self):
        """
        Gets the default_masking_format_id of this CreateSensitiveTypePatternDetails.
        The OCID of the library masking format that should be used to mask the sensitive columns associated with the sensitive type.


        :return: The default_masking_format_id of this CreateSensitiveTypePatternDetails.
        :rtype: str
        """
        return self._default_masking_format_id

    @default_masking_format_id.setter
    def default_masking_format_id(self, default_masking_format_id):
        """
        Sets the default_masking_format_id of this CreateSensitiveTypePatternDetails.
        The OCID of the library masking format that should be used to mask the sensitive columns associated with the sensitive type.


        :param default_masking_format_id: The default_masking_format_id of this CreateSensitiveTypePatternDetails.
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
