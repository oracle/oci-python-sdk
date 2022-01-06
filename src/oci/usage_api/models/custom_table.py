# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomTable(object):
    """
    The saved custom table.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomTable object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CustomTable.
        :type id: str

        :param saved_report_id:
            The value to assign to the saved_report_id property of this CustomTable.
        :type saved_report_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CustomTable.
        :type compartment_id: str

        :param saved_custom_table:
            The value to assign to the saved_custom_table property of this CustomTable.
        :type saved_custom_table: oci.usage_api.models.SavedCustomTable

        """
        self.swagger_types = {
            'id': 'str',
            'saved_report_id': 'str',
            'compartment_id': 'str',
            'saved_custom_table': 'SavedCustomTable'
        }

        self.attribute_map = {
            'id': 'id',
            'saved_report_id': 'savedReportId',
            'compartment_id': 'compartmentId',
            'saved_custom_table': 'savedCustomTable'
        }

        self._id = None
        self._saved_report_id = None
        self._compartment_id = None
        self._saved_custom_table = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CustomTable.
        The custom table OCID.


        :return: The id of this CustomTable.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CustomTable.
        The custom table OCID.


        :param id: The id of this CustomTable.
        :type: str
        """
        self._id = id

    @property
    def saved_report_id(self):
        """
        Gets the saved_report_id of this CustomTable.
        The custom table associated saved report OCID.


        :return: The saved_report_id of this CustomTable.
        :rtype: str
        """
        return self._saved_report_id

    @saved_report_id.setter
    def saved_report_id(self, saved_report_id):
        """
        Sets the saved_report_id of this CustomTable.
        The custom table associated saved report OCID.


        :param saved_report_id: The saved_report_id of this CustomTable.
        :type: str
        """
        self._saved_report_id = saved_report_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CustomTable.
        The custom table compartment OCID.


        :return: The compartment_id of this CustomTable.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CustomTable.
        The custom table compartment OCID.


        :param compartment_id: The compartment_id of this CustomTable.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def saved_custom_table(self):
        """
        Gets the saved_custom_table of this CustomTable.

        :return: The saved_custom_table of this CustomTable.
        :rtype: oci.usage_api.models.SavedCustomTable
        """
        return self._saved_custom_table

    @saved_custom_table.setter
    def saved_custom_table(self, saved_custom_table):
        """
        Sets the saved_custom_table of this CustomTable.

        :param saved_custom_table: The saved_custom_table of this CustomTable.
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
