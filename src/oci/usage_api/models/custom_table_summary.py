# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomTableSummary(object):
    """
    Custom table in list request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomTableSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CustomTableSummary.
        :type id: str

        :param saved_custom_table:
            The value to assign to the saved_custom_table property of this CustomTableSummary.
        :type saved_custom_table: oci.usage_api.models.SavedCustomTable

        """
        self.swagger_types = {
            'id': 'str',
            'saved_custom_table': 'SavedCustomTable'
        }

        self.attribute_map = {
            'id': 'id',
            'saved_custom_table': 'savedCustomTable'
        }

        self._id = None
        self._saved_custom_table = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CustomTableSummary.
        The custom table OCID.


        :return: The id of this CustomTableSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CustomTableSummary.
        The custom table OCID.


        :param id: The id of this CustomTableSummary.
        :type: str
        """
        self._id = id

    @property
    def saved_custom_table(self):
        """
        **[Required]** Gets the saved_custom_table of this CustomTableSummary.

        :return: The saved_custom_table of this CustomTableSummary.
        :rtype: oci.usage_api.models.SavedCustomTable
        """
        return self._saved_custom_table

    @saved_custom_table.setter
    def saved_custom_table(self, saved_custom_table):
        """
        Sets the saved_custom_table of this CustomTableSummary.

        :param saved_custom_table: The saved_custom_table of this CustomTableSummary.
        :type: oci.usage_api.models.SavedCustomTable
        """
        self._saved_custom_table = saved_custom_table

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
