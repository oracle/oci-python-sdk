# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaskingFormat(object):
    """
    A masking format defines the logic to mask data in a database column. The condition attribute
    defines the condition that must be true for applying the masking format. It enables you to do
    <a href=\"https://docs.oracle.com/en/cloud/paas/data-safe/udscs/conditional-masking.html\">conditional masking</a>
    so that you can mask the column data values differently using different masking formats and
    the associated conditions. A masking format can have one or more format entries. A format entry
    can be a basic masking format such as Random Number, or it can be a library masking format.The
    combined output of all the format entries is used for masking. It provides the flexibility to
    define a masking format that can generate different parts of a data value separately and then
    combine them to get the final data value for masking.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MaskingFormat object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param condition:
            The value to assign to the condition property of this MaskingFormat.
        :type condition: str

        :param description:
            The value to assign to the description property of this MaskingFormat.
        :type description: str

        :param format_entries:
            The value to assign to the format_entries property of this MaskingFormat.
        :type format_entries: list[oci.data_safe.models.FormatEntry]

        """
        self.swagger_types = {
            'condition': 'str',
            'description': 'str',
            'format_entries': 'list[FormatEntry]'
        }

        self.attribute_map = {
            'condition': 'condition',
            'description': 'description',
            'format_entries': 'formatEntries'
        }

        self._condition = None
        self._description = None
        self._format_entries = None

    @property
    def condition(self):
        """
        Gets the condition of this MaskingFormat.
        A condition that must be true for applying the masking format. It can be any valid
        SQL construct that can be used in a SQL predicate. It enables you to do
        <a href=\"https://docs.oracle.com/en/cloud/paas/data-safe/udscs/conditional-masking.html\">conditional masking</a>
        so that you can mask the column data values differently using different masking
        formats and the associated conditions.


        :return: The condition of this MaskingFormat.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this MaskingFormat.
        A condition that must be true for applying the masking format. It can be any valid
        SQL construct that can be used in a SQL predicate. It enables you to do
        <a href=\"https://docs.oracle.com/en/cloud/paas/data-safe/udscs/conditional-masking.html\">conditional masking</a>
        so that you can mask the column data values differently using different masking
        formats and the associated conditions.


        :param condition: The condition of this MaskingFormat.
        :type: str
        """
        self._condition = condition

    @property
    def description(self):
        """
        Gets the description of this MaskingFormat.
        The description of the masking format.


        :return: The description of this MaskingFormat.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MaskingFormat.
        The description of the masking format.


        :param description: The description of this MaskingFormat.
        :type: str
        """
        self._description = description

    @property
    def format_entries(self):
        """
        **[Required]** Gets the format_entries of this MaskingFormat.
        An array of format entries. The combined output of all the format entries is
        used for masking the column data values.


        :return: The format_entries of this MaskingFormat.
        :rtype: list[oci.data_safe.models.FormatEntry]
        """
        return self._format_entries

    @format_entries.setter
    def format_entries(self, format_entries):
        """
        Sets the format_entries of this MaskingFormat.
        An array of format entries. The combined output of all the format entries is
        used for masking the column data values.


        :param format_entries: The format_entries of this MaskingFormat.
        :type: list[oci.data_safe.models.FormatEntry]
        """
        self._format_entries = format_entries

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
