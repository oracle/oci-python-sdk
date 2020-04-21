# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateExportDetails(object):
    """
    Details for creating the export.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateExportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param export_options:
            The value to assign to the export_options property of this CreateExportDetails.
        :type export_options: list[ClientOptions]

        :param export_set_id:
            The value to assign to the export_set_id property of this CreateExportDetails.
        :type export_set_id: str

        :param file_system_id:
            The value to assign to the file_system_id property of this CreateExportDetails.
        :type file_system_id: str

        :param path:
            The value to assign to the path property of this CreateExportDetails.
        :type path: str

        """
        self.swagger_types = {
            'export_options': 'list[ClientOptions]',
            'export_set_id': 'str',
            'file_system_id': 'str',
            'path': 'str'
        }

        self.attribute_map = {
            'export_options': 'exportOptions',
            'export_set_id': 'exportSetId',
            'file_system_id': 'fileSystemId',
            'path': 'path'
        }

        self._export_options = None
        self._export_set_id = None
        self._file_system_id = None
        self._path = None

    @property
    def export_options(self):
        """
        Gets the export_options of this CreateExportDetails.
        Export options for the new export. If left unspecified,
        defaults to:

               [
                 {
                    \"source\" : \"0.0.0.0/0\",
                    \"requirePrivilegedSourcePort\" : false,
                    \"access\" : \"READ_WRITE\",
                    \"identitySquash\" : \"NONE\"
                  }
               ]

          **Note:** Mount targets do not have Internet-routable IP
          addresses.  Therefore they will not be reachable from the
          Internet, even if an associated `ClientOptions` item has
          a source of `0.0.0.0/0`.

          **If set to the empty array then the export will not be
          visible to any clients.**

          The export's `exportOptions` can be changed after creation
          using the `UpdateExport` operation.


        :return: The export_options of this CreateExportDetails.
        :rtype: list[ClientOptions]
        """
        return self._export_options

    @export_options.setter
    def export_options(self, export_options):
        """
        Sets the export_options of this CreateExportDetails.
        Export options for the new export. If left unspecified,
        defaults to:

               [
                 {
                    \"source\" : \"0.0.0.0/0\",
                    \"requirePrivilegedSourcePort\" : false,
                    \"access\" : \"READ_WRITE\",
                    \"identitySquash\" : \"NONE\"
                  }
               ]

          **Note:** Mount targets do not have Internet-routable IP
          addresses.  Therefore they will not be reachable from the
          Internet, even if an associated `ClientOptions` item has
          a source of `0.0.0.0/0`.

          **If set to the empty array then the export will not be
          visible to any clients.**

          The export's `exportOptions` can be changed after creation
          using the `UpdateExport` operation.


        :param export_options: The export_options of this CreateExportDetails.
        :type: list[ClientOptions]
        """
        self._export_options = export_options

    @property
    def export_set_id(self):
        """
        **[Required]** Gets the export_set_id of this CreateExportDetails.
        The OCID of this export's export set.


        :return: The export_set_id of this CreateExportDetails.
        :rtype: str
        """
        return self._export_set_id

    @export_set_id.setter
    def export_set_id(self, export_set_id):
        """
        Sets the export_set_id of this CreateExportDetails.
        The OCID of this export's export set.


        :param export_set_id: The export_set_id of this CreateExportDetails.
        :type: str
        """
        self._export_set_id = export_set_id

    @property
    def file_system_id(self):
        """
        **[Required]** Gets the file_system_id of this CreateExportDetails.
        The OCID of this export's file system.


        :return: The file_system_id of this CreateExportDetails.
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """
        Sets the file_system_id of this CreateExportDetails.
        The OCID of this export's file system.


        :param file_system_id: The file_system_id of this CreateExportDetails.
        :type: str
        """
        self._file_system_id = file_system_id

    @property
    def path(self):
        """
        **[Required]** Gets the path of this CreateExportDetails.
        Path used to access the associated file system.

        Avoid entering confidential information.

        Example: `/mediafiles`


        :return: The path of this CreateExportDetails.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this CreateExportDetails.
        Path used to access the associated file system.

        Avoid entering confidential information.

        Example: `/mediafiles`


        :param path: The path of this CreateExportDetails.
        :type: str
        """
        self._path = path

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
