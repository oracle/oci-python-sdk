# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTablespaceDetails(object):
    """
    The details required to update a tablespace.
    """

    #: A constant which can be used with the type property of a UpdateTablespaceDetails.
    #: This constant has a value of "PERMANENT"
    TYPE_PERMANENT = "PERMANENT"

    #: A constant which can be used with the type property of a UpdateTablespaceDetails.
    #: This constant has a value of "TEMPORARY"
    TYPE_TEMPORARY = "TEMPORARY"

    #: A constant which can be used with the status property of a UpdateTablespaceDetails.
    #: This constant has a value of "READ_ONLY"
    STATUS_READ_ONLY = "READ_ONLY"

    #: A constant which can be used with the status property of a UpdateTablespaceDetails.
    #: This constant has a value of "READ_WRITE"
    STATUS_READ_WRITE = "READ_WRITE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTablespaceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_details:
            The value to assign to the credential_details property of this UpdateTablespaceDetails.
        :type credential_details: oci.database_management.models.TablespaceAdminCredentialDetails

        :param name:
            The value to assign to the name property of this UpdateTablespaceDetails.
        :type name: str

        :param type:
            The value to assign to the type property of this UpdateTablespaceDetails.
            Allowed values for this property are: "PERMANENT", "TEMPORARY"
        :type type: str

        :param file_size:
            The value to assign to the file_size property of this UpdateTablespaceDetails.
        :type file_size: oci.database_management.models.TablespaceStorageSize

        :param status:
            The value to assign to the status property of this UpdateTablespaceDetails.
            Allowed values for this property are: "READ_ONLY", "READ_WRITE"
        :type status: str

        :param is_auto_extensible:
            The value to assign to the is_auto_extensible property of this UpdateTablespaceDetails.
        :type is_auto_extensible: bool

        :param auto_extend_next_size:
            The value to assign to the auto_extend_next_size property of this UpdateTablespaceDetails.
        :type auto_extend_next_size: oci.database_management.models.TablespaceStorageSize

        :param auto_extend_max_size:
            The value to assign to the auto_extend_max_size property of this UpdateTablespaceDetails.
        :type auto_extend_max_size: oci.database_management.models.TablespaceStorageSize

        :param is_max_size_unlimited:
            The value to assign to the is_max_size_unlimited property of this UpdateTablespaceDetails.
        :type is_max_size_unlimited: bool

        :param is_default:
            The value to assign to the is_default property of this UpdateTablespaceDetails.
        :type is_default: bool

        """
        self.swagger_types = {
            'credential_details': 'TablespaceAdminCredentialDetails',
            'name': 'str',
            'type': 'str',
            'file_size': 'TablespaceStorageSize',
            'status': 'str',
            'is_auto_extensible': 'bool',
            'auto_extend_next_size': 'TablespaceStorageSize',
            'auto_extend_max_size': 'TablespaceStorageSize',
            'is_max_size_unlimited': 'bool',
            'is_default': 'bool'
        }

        self.attribute_map = {
            'credential_details': 'credentialDetails',
            'name': 'name',
            'type': 'type',
            'file_size': 'fileSize',
            'status': 'status',
            'is_auto_extensible': 'isAutoExtensible',
            'auto_extend_next_size': 'autoExtendNextSize',
            'auto_extend_max_size': 'autoExtendMaxSize',
            'is_max_size_unlimited': 'isMaxSizeUnlimited',
            'is_default': 'isDefault'
        }

        self._credential_details = None
        self._name = None
        self._type = None
        self._file_size = None
        self._status = None
        self._is_auto_extensible = None
        self._auto_extend_next_size = None
        self._auto_extend_max_size = None
        self._is_max_size_unlimited = None
        self._is_default = None

    @property
    def credential_details(self):
        """
        **[Required]** Gets the credential_details of this UpdateTablespaceDetails.

        :return: The credential_details of this UpdateTablespaceDetails.
        :rtype: oci.database_management.models.TablespaceAdminCredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this UpdateTablespaceDetails.

        :param credential_details: The credential_details of this UpdateTablespaceDetails.
        :type: oci.database_management.models.TablespaceAdminCredentialDetails
        """
        self._credential_details = credential_details

    @property
    def name(self):
        """
        Gets the name of this UpdateTablespaceDetails.
        The name of the tablespace. It must be unique within a database.


        :return: The name of this UpdateTablespaceDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateTablespaceDetails.
        The name of the tablespace. It must be unique within a database.


        :param name: The name of this UpdateTablespaceDetails.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this UpdateTablespaceDetails.
        The type of tablespace.

        Allowed values for this property are: "PERMANENT", "TEMPORARY"


        :return: The type of this UpdateTablespaceDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UpdateTablespaceDetails.
        The type of tablespace.


        :param type: The type of this UpdateTablespaceDetails.
        :type: str
        """
        allowed_values = ["PERMANENT", "TEMPORARY"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def file_size(self):
        """
        Gets the file_size of this UpdateTablespaceDetails.
        The size of each data file or temp file.


        :return: The file_size of this UpdateTablespaceDetails.
        :rtype: oci.database_management.models.TablespaceStorageSize
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """
        Sets the file_size of this UpdateTablespaceDetails.
        The size of each data file or temp file.


        :param file_size: The file_size of this UpdateTablespaceDetails.
        :type: oci.database_management.models.TablespaceStorageSize
        """
        self._file_size = file_size

    @property
    def status(self):
        """
        Gets the status of this UpdateTablespaceDetails.
        The status of the tablespace.

        Allowed values for this property are: "READ_ONLY", "READ_WRITE"


        :return: The status of this UpdateTablespaceDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateTablespaceDetails.
        The status of the tablespace.


        :param status: The status of this UpdateTablespaceDetails.
        :type: str
        """
        allowed_values = ["READ_ONLY", "READ_WRITE"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def is_auto_extensible(self):
        """
        Gets the is_auto_extensible of this UpdateTablespaceDetails.
        Specifies whether the data file or temp file can be extended automatically.


        :return: The is_auto_extensible of this UpdateTablespaceDetails.
        :rtype: bool
        """
        return self._is_auto_extensible

    @is_auto_extensible.setter
    def is_auto_extensible(self, is_auto_extensible):
        """
        Sets the is_auto_extensible of this UpdateTablespaceDetails.
        Specifies whether the data file or temp file can be extended automatically.


        :param is_auto_extensible: The is_auto_extensible of this UpdateTablespaceDetails.
        :type: bool
        """
        self._is_auto_extensible = is_auto_extensible

    @property
    def auto_extend_next_size(self):
        """
        Gets the auto_extend_next_size of this UpdateTablespaceDetails.
        The size of the next increment of disk space to be allocated automatically when more extents are required.


        :return: The auto_extend_next_size of this UpdateTablespaceDetails.
        :rtype: oci.database_management.models.TablespaceStorageSize
        """
        return self._auto_extend_next_size

    @auto_extend_next_size.setter
    def auto_extend_next_size(self, auto_extend_next_size):
        """
        Sets the auto_extend_next_size of this UpdateTablespaceDetails.
        The size of the next increment of disk space to be allocated automatically when more extents are required.


        :param auto_extend_next_size: The auto_extend_next_size of this UpdateTablespaceDetails.
        :type: oci.database_management.models.TablespaceStorageSize
        """
        self._auto_extend_next_size = auto_extend_next_size

    @property
    def auto_extend_max_size(self):
        """
        Gets the auto_extend_max_size of this UpdateTablespaceDetails.
        The maximum disk space allowed for automatic extension of the data files or temp files.


        :return: The auto_extend_max_size of this UpdateTablespaceDetails.
        :rtype: oci.database_management.models.TablespaceStorageSize
        """
        return self._auto_extend_max_size

    @auto_extend_max_size.setter
    def auto_extend_max_size(self, auto_extend_max_size):
        """
        Sets the auto_extend_max_size of this UpdateTablespaceDetails.
        The maximum disk space allowed for automatic extension of the data files or temp files.


        :param auto_extend_max_size: The auto_extend_max_size of this UpdateTablespaceDetails.
        :type: oci.database_management.models.TablespaceStorageSize
        """
        self._auto_extend_max_size = auto_extend_max_size

    @property
    def is_max_size_unlimited(self):
        """
        Gets the is_max_size_unlimited of this UpdateTablespaceDetails.
        Specifies whether the disk space of the data file or temp file can be limited.


        :return: The is_max_size_unlimited of this UpdateTablespaceDetails.
        :rtype: bool
        """
        return self._is_max_size_unlimited

    @is_max_size_unlimited.setter
    def is_max_size_unlimited(self, is_max_size_unlimited):
        """
        Sets the is_max_size_unlimited of this UpdateTablespaceDetails.
        Specifies whether the disk space of the data file or temp file can be limited.


        :param is_max_size_unlimited: The is_max_size_unlimited of this UpdateTablespaceDetails.
        :type: bool
        """
        self._is_max_size_unlimited = is_max_size_unlimited

    @property
    def is_default(self):
        """
        Gets the is_default of this UpdateTablespaceDetails.
        Specifies whether the tablespace is the default tablespace.


        :return: The is_default of this UpdateTablespaceDetails.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this UpdateTablespaceDetails.
        Specifies whether the tablespace is the default tablespace.


        :param is_default: The is_default of this UpdateTablespaceDetails.
        :type: bool
        """
        self._is_default = is_default

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
