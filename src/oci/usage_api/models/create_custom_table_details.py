# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCustomTableDetails(object):
    """
    New custom table detail.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCustomTableDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCustomTableDetails.
        :type compartment_id: str

        :param saved_report_id:
            The value to assign to the saved_report_id property of this CreateCustomTableDetails.
        :type saved_report_id: str

        :param saved_custom_table:
            The value to assign to the saved_custom_table property of this CreateCustomTableDetails.
        :type saved_custom_table: oci.usage_api.models.SavedCustomTable

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'saved_report_id': 'str',
            'saved_custom_table': 'SavedCustomTable'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'saved_report_id': 'savedReportId',
            'saved_custom_table': 'savedCustomTable'
        }

        self._compartment_id = None
        self._saved_report_id = None
        self._saved_custom_table = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCustomTableDetails.
        The compartment OCID.


        :return: The compartment_id of this CreateCustomTableDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCustomTableDetails.
        The compartment OCID.


        :param compartment_id: The compartment_id of this CreateCustomTableDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def saved_report_id(self):
        """
        **[Required]** Gets the saved_report_id of this CreateCustomTableDetails.
        The associated saved report OCID.


        :return: The saved_report_id of this CreateCustomTableDetails.
        :rtype: str
        """
        return self._saved_report_id

    @saved_report_id.setter
    def saved_report_id(self, saved_report_id):
        """
        Sets the saved_report_id of this CreateCustomTableDetails.
        The associated saved report OCID.


        :param saved_report_id: The saved_report_id of this CreateCustomTableDetails.
        :type: str
        """
        self._saved_report_id = saved_report_id

    @property
    def saved_custom_table(self):
        """
        **[Required]** Gets the saved_custom_table of this CreateCustomTableDetails.

        :return: The saved_custom_table of this CreateCustomTableDetails.
        :rtype: oci.usage_api.models.SavedCustomTable
        """
        return self._saved_custom_table

    @saved_custom_table.setter
    def saved_custom_table(self, saved_custom_table):
        """
        Sets the saved_custom_table of this CreateCustomTableDetails.

        :param saved_custom_table: The saved_custom_table of this CreateCustomTableDetails.
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
