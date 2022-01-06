# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateExportDetails(object):
    """
    Details for updating the export.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateExportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param export_options:
            The value to assign to the export_options property of this UpdateExportDetails.
        :type export_options: list[oci.file_storage.models.ClientOptions]

        """
        self.swagger_types = {
            'export_options': 'list[ClientOptions]'
        }

        self.attribute_map = {
            'export_options': 'exportOptions'
        }

        self._export_options = None

    @property
    def export_options(self):
        """
        Gets the export_options of this UpdateExportDetails.
        New export options for the export.

        **Setting to the empty array will make the export invisible to all clients.**

        Leaving unset will leave the `exportOptions` unchanged.


        :return: The export_options of this UpdateExportDetails.
        :rtype: list[oci.file_storage.models.ClientOptions]
        """
        return self._export_options

    @export_options.setter
    def export_options(self, export_options):
        """
        Sets the export_options of this UpdateExportDetails.
        New export options for the export.

        **Setting to the empty array will make the export invisible to all clients.**

        Leaving unset will leave the `exportOptions` unchanged.


        :param export_options: The export_options of this UpdateExportDetails.
        :type: list[oci.file_storage.models.ClientOptions]
        """
        self._export_options = export_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
