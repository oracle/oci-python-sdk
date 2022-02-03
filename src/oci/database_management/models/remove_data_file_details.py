# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemoveDataFileDetails(object):
    """
    The details required to remove a data file or temp file from the tablespace.
    """

    #: A constant which can be used with the file_type property of a RemoveDataFileDetails.
    #: This constant has a value of "DATAFILE"
    FILE_TYPE_DATAFILE = "DATAFILE"

    #: A constant which can be used with the file_type property of a RemoveDataFileDetails.
    #: This constant has a value of "TEMPFILE"
    FILE_TYPE_TEMPFILE = "TEMPFILE"

    def __init__(self, **kwargs):
        """
        Initializes a new RemoveDataFileDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_details:
            The value to assign to the credential_details property of this RemoveDataFileDetails.
        :type credential_details: oci.database_management.models.TablespaceAdminCredentialDetails

        :param file_type:
            The value to assign to the file_type property of this RemoveDataFileDetails.
            Allowed values for this property are: "DATAFILE", "TEMPFILE"
        :type file_type: str

        :param data_file:
            The value to assign to the data_file property of this RemoveDataFileDetails.
        :type data_file: str

        """
        self.swagger_types = {
            'credential_details': 'TablespaceAdminCredentialDetails',
            'file_type': 'str',
            'data_file': 'str'
        }

        self.attribute_map = {
            'credential_details': 'credentialDetails',
            'file_type': 'fileType',
            'data_file': 'dataFile'
        }

        self._credential_details = None
        self._file_type = None
        self._data_file = None

    @property
    def credential_details(self):
        """
        **[Required]** Gets the credential_details of this RemoveDataFileDetails.

        :return: The credential_details of this RemoveDataFileDetails.
        :rtype: oci.database_management.models.TablespaceAdminCredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this RemoveDataFileDetails.

        :param credential_details: The credential_details of this RemoveDataFileDetails.
        :type: oci.database_management.models.TablespaceAdminCredentialDetails
        """
        self._credential_details = credential_details

    @property
    def file_type(self):
        """
        **[Required]** Gets the file_type of this RemoveDataFileDetails.
        Specifies whether the file is a data file or temp file.

        Allowed values for this property are: "DATAFILE", "TEMPFILE"


        :return: The file_type of this RemoveDataFileDetails.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """
        Sets the file_type of this RemoveDataFileDetails.
        Specifies whether the file is a data file or temp file.


        :param file_type: The file_type of this RemoveDataFileDetails.
        :type: str
        """
        allowed_values = ["DATAFILE", "TEMPFILE"]
        if not value_allowed_none_or_none_sentinel(file_type, allowed_values):
            raise ValueError(
                "Invalid value for `file_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._file_type = file_type

    @property
    def data_file(self):
        """
        **[Required]** Gets the data_file of this RemoveDataFileDetails.
        Name of the data file or temp file to be removed from the tablespace.


        :return: The data_file of this RemoveDataFileDetails.
        :rtype: str
        """
        return self._data_file

    @data_file.setter
    def data_file(self, data_file):
        """
        Sets the data_file of this RemoveDataFileDetails.
        Name of the data file or temp file to be removed from the tablespace.


        :param data_file: The data_file of this RemoveDataFileDetails.
        :type: str
        """
        self._data_file = data_file

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
