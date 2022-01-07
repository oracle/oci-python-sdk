# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementDashboardExportDetails(object):
    """
    Array of dashboards to export.  Response from export must be directly acceptable to import (compartmentIds may have to be changed).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementDashboardExportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dashboards:
            The value to assign to the dashboards property of this ManagementDashboardExportDetails.
        :type dashboards: list[oci.management_dashboard.models.ManagementDashboardForImportExportDetails]

        """
        self.swagger_types = {
            'dashboards': 'list[ManagementDashboardForImportExportDetails]'
        }

        self.attribute_map = {
            'dashboards': 'dashboards'
        }

        self._dashboards = None

    @property
    def dashboards(self):
        """
        **[Required]** Gets the dashboards of this ManagementDashboardExportDetails.
        Array of dashboards.


        :return: The dashboards of this ManagementDashboardExportDetails.
        :rtype: list[oci.management_dashboard.models.ManagementDashboardForImportExportDetails]
        """
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """
        Sets the dashboards of this ManagementDashboardExportDetails.
        Array of dashboards.


        :param dashboards: The dashboards of this ManagementDashboardExportDetails.
        :type: list[oci.management_dashboard.models.ManagementDashboardForImportExportDetails]
        """
        self._dashboards = dashboards

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
