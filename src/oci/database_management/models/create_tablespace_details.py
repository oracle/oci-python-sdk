# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTablespaceDetails(object):
    """
    The details required to create a tablespace.
    """

    #: A constant which can be used with the type property of a CreateTablespaceDetails.
    #: This constant has a value of "PERMANENT"
    TYPE_PERMANENT = "PERMANENT"

    #: A constant which can be used with the type property of a CreateTablespaceDetails.
    #: This constant has a value of "TEMPORARY"
    TYPE_TEMPORARY = "TEMPORARY"

    #: A constant which can be used with the default_compress property of a CreateTablespaceDetails.
    #: This constant has a value of "NO_COMPRESS"
    DEFAULT_COMPRESS_NO_COMPRESS = "NO_COMPRESS"

    #: A constant which can be used with the default_compress property of a CreateTablespaceDetails.
    #: This constant has a value of "BASIC_COMPRESS"
    DEFAULT_COMPRESS_BASIC_COMPRESS = "BASIC_COMPRESS"

    #: A constant which can be used with the status property of a CreateTablespaceDetails.
    #: This constant has a value of "READ_ONLY"
    STATUS_READ_ONLY = "READ_ONLY"

    #: A constant which can be used with the status property of a CreateTablespaceDetails.
    #: This constant has a value of "READ_WRITE"
    STATUS_READ_WRITE = "READ_WRITE"

    #: A constant which can be used with the extent_management property of a CreateTablespaceDetails.
    #: This constant has a value of "AUTOALLOCATE"
    EXTENT_MANAGEMENT_AUTOALLOCATE = "AUTOALLOCATE"

    #: A constant which can be used with the extent_management property of a CreateTablespaceDetails.
    #: This constant has a value of "UNIFORM"
    EXTENT_MANAGEMENT_UNIFORM = "UNIFORM"

    #: A constant which can be used with the segment_management property of a CreateTablespaceDetails.
    #: This constant has a value of "AUTO"
    SEGMENT_MANAGEMENT_AUTO = "AUTO"

    #: A constant which can be used with the segment_management property of a CreateTablespaceDetails.
    #: This constant has a value of "MANUAL"
    SEGMENT_MANAGEMENT_MANUAL = "MANUAL"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTablespaceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_details:
            The value to assign to the credential_details property of this CreateTablespaceDetails.
        :type credential_details: oci.database_management.models.TablespaceAdminCredentialDetails

        :param name:
            The value to assign to the name property of this CreateTablespaceDetails.
        :type name: str

        :param type:
            The value to assign to the type property of this CreateTablespaceDetails.
            Allowed values for this property are: "PERMANENT", "TEMPORARY"
        :type type: str

        :param is_bigfile:
            The value to assign to the is_bigfile property of this CreateTablespaceDetails.
        :type is_bigfile: bool

        :param data_files:
            The value to assign to the data_files property of this CreateTablespaceDetails.
        :type data_files: list[str]

        :param file_count:
            The value to assign to the file_count property of this CreateTablespaceDetails.
        :type file_count: int

        :param file_size:
            The value to assign to the file_size property of this CreateTablespaceDetails.
        :type file_size: oci.database_management.models.TablespaceStorageSize

        :param is_reusable:
            The value to assign to the is_reusable property of this CreateTablespaceDetails.
        :type is_reusable: bool

        :param is_auto_extensible:
            The value to assign to the is_auto_extensible property of this CreateTablespaceDetails.
        :type is_auto_extensible: bool

        :param auto_extend_next_size:
            The value to assign to the auto_extend_next_size property of this CreateTablespaceDetails.
        :type auto_extend_next_size: oci.database_management.models.TablespaceStorageSize

        :param auto_extend_max_size:
            The value to assign to the auto_extend_max_size property of this CreateTablespaceDetails.
        :type auto_extend_max_size: oci.database_management.models.TablespaceStorageSize

        :param is_max_size_unlimited:
            The value to assign to the is_max_size_unlimited property of this CreateTablespaceDetails.
        :type is_max_size_unlimited: bool

        :param block_size_in_kilobytes:
            The value to assign to the block_size_in_kilobytes property of this CreateTablespaceDetails.
        :type block_size_in_kilobytes: int

        :param is_encrypted:
            The value to assign to the is_encrypted property of this CreateTablespaceDetails.
        :type is_encrypted: bool

        :param encryption_algorithm:
            The value to assign to the encryption_algorithm property of this CreateTablespaceDetails.
        :type encryption_algorithm: str

        :param default_compress:
            The value to assign to the default_compress property of this CreateTablespaceDetails.
            Allowed values for this property are: "NO_COMPRESS", "BASIC_COMPRESS"
        :type default_compress: str

        :param status:
            The value to assign to the status property of this CreateTablespaceDetails.
            Allowed values for this property are: "READ_ONLY", "READ_WRITE"
        :type status: str

        :param extent_management:
            The value to assign to the extent_management property of this CreateTablespaceDetails.
            Allowed values for this property are: "AUTOALLOCATE", "UNIFORM"
        :type extent_management: str

        :param extent_uniform_size:
            The value to assign to the extent_uniform_size property of this CreateTablespaceDetails.
        :type extent_uniform_size: oci.database_management.models.TablespaceStorageSize

        :param segment_management:
            The value to assign to the segment_management property of this CreateTablespaceDetails.
            Allowed values for this property are: "AUTO", "MANUAL"
        :type segment_management: str

        :param is_default:
            The value to assign to the is_default property of this CreateTablespaceDetails.
        :type is_default: bool

        """
        self.swagger_types = {
            'credential_details': 'TablespaceAdminCredentialDetails',
            'name': 'str',
            'type': 'str',
            'is_bigfile': 'bool',
            'data_files': 'list[str]',
            'file_count': 'int',
            'file_size': 'TablespaceStorageSize',
            'is_reusable': 'bool',
            'is_auto_extensible': 'bool',
            'auto_extend_next_size': 'TablespaceStorageSize',
            'auto_extend_max_size': 'TablespaceStorageSize',
            'is_max_size_unlimited': 'bool',
            'block_size_in_kilobytes': 'int',
            'is_encrypted': 'bool',
            'encryption_algorithm': 'str',
            'default_compress': 'str',
            'status': 'str',
            'extent_management': 'str',
            'extent_uniform_size': 'TablespaceStorageSize',
            'segment_management': 'str',
            'is_default': 'bool'
        }

        self.attribute_map = {
            'credential_details': 'credentialDetails',
            'name': 'name',
            'type': 'type',
            'is_bigfile': 'isBigfile',
            'data_files': 'dataFiles',
            'file_count': 'fileCount',
            'file_size': 'fileSize',
            'is_reusable': 'isReusable',
            'is_auto_extensible': 'isAutoExtensible',
            'auto_extend_next_size': 'autoExtendNextSize',
            'auto_extend_max_size': 'autoExtendMaxSize',
            'is_max_size_unlimited': 'isMaxSizeUnlimited',
            'block_size_in_kilobytes': 'blockSizeInKilobytes',
            'is_encrypted': 'isEncrypted',
            'encryption_algorithm': 'encryptionAlgorithm',
            'default_compress': 'defaultCompress',
            'status': 'status',
            'extent_management': 'extentManagement',
            'extent_uniform_size': 'extentUniformSize',
            'segment_management': 'segmentManagement',
            'is_default': 'isDefault'
        }

        self._credential_details = None
        self._name = None
        self._type = None
        self._is_bigfile = None
        self._data_files = None
        self._file_count = None
        self._file_size = None
        self._is_reusable = None
        self._is_auto_extensible = None
        self._auto_extend_next_size = None
        self._auto_extend_max_size = None
        self._is_max_size_unlimited = None
        self._block_size_in_kilobytes = None
        self._is_encrypted = None
        self._encryption_algorithm = None
        self._default_compress = None
        self._status = None
        self._extent_management = None
        self._extent_uniform_size = None
        self._segment_management = None
        self._is_default = None

    @property
    def credential_details(self):
        """
        **[Required]** Gets the credential_details of this CreateTablespaceDetails.

        :return: The credential_details of this CreateTablespaceDetails.
        :rtype: oci.database_management.models.TablespaceAdminCredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this CreateTablespaceDetails.

        :param credential_details: The credential_details of this CreateTablespaceDetails.
        :type: oci.database_management.models.TablespaceAdminCredentialDetails
        """
        self._credential_details = credential_details

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateTablespaceDetails.
        The name of the tablespace. It must be unique within a database.


        :return: The name of this CreateTablespaceDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateTablespaceDetails.
        The name of the tablespace. It must be unique within a database.


        :param name: The name of this CreateTablespaceDetails.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this CreateTablespaceDetails.
        The type of tablespace.

        Allowed values for this property are: "PERMANENT", "TEMPORARY"


        :return: The type of this CreateTablespaceDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateTablespaceDetails.
        The type of tablespace.


        :param type: The type of this CreateTablespaceDetails.
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
    def is_bigfile(self):
        """
        Gets the is_bigfile of this CreateTablespaceDetails.
        Specifies whether the tablespace is a bigfile or smallfile tablespace.
        A bigfile tablespace contains only one data file or temp file, which can contain up to approximately 4 billion (232) blocks.
        A smallfile tablespace is a traditional Oracle tablespace, which can contain 1022 data files or temp files, each of which can contain up to approximately 4 million (222) blocks.


        :return: The is_bigfile of this CreateTablespaceDetails.
        :rtype: bool
        """
        return self._is_bigfile

    @is_bigfile.setter
    def is_bigfile(self, is_bigfile):
        """
        Sets the is_bigfile of this CreateTablespaceDetails.
        Specifies whether the tablespace is a bigfile or smallfile tablespace.
        A bigfile tablespace contains only one data file or temp file, which can contain up to approximately 4 billion (232) blocks.
        A smallfile tablespace is a traditional Oracle tablespace, which can contain 1022 data files or temp files, each of which can contain up to approximately 4 million (222) blocks.


        :param is_bigfile: The is_bigfile of this CreateTablespaceDetails.
        :type: bool
        """
        self._is_bigfile = is_bigfile

    @property
    def data_files(self):
        """
        Gets the data_files of this CreateTablespaceDetails.
        The list of data files or temp files created for the tablespace.


        :return: The data_files of this CreateTablespaceDetails.
        :rtype: list[str]
        """
        return self._data_files

    @data_files.setter
    def data_files(self, data_files):
        """
        Sets the data_files of this CreateTablespaceDetails.
        The list of data files or temp files created for the tablespace.


        :param data_files: The data_files of this CreateTablespaceDetails.
        :type: list[str]
        """
        self._data_files = data_files

    @property
    def file_count(self):
        """
        Gets the file_count of this CreateTablespaceDetails.
        The number of data files or temp files created for the tablespace. This is for Oracle Managed Files only.


        :return: The file_count of this CreateTablespaceDetails.
        :rtype: int
        """
        return self._file_count

    @file_count.setter
    def file_count(self, file_count):
        """
        Sets the file_count of this CreateTablespaceDetails.
        The number of data files or temp files created for the tablespace. This is for Oracle Managed Files only.


        :param file_count: The file_count of this CreateTablespaceDetails.
        :type: int
        """
        self._file_count = file_count

    @property
    def file_size(self):
        """
        Gets the file_size of this CreateTablespaceDetails.
        The size of each data file or temp file.


        :return: The file_size of this CreateTablespaceDetails.
        :rtype: oci.database_management.models.TablespaceStorageSize
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """
        Sets the file_size of this CreateTablespaceDetails.
        The size of each data file or temp file.


        :param file_size: The file_size of this CreateTablespaceDetails.
        :type: oci.database_management.models.TablespaceStorageSize
        """
        self._file_size = file_size

    @property
    def is_reusable(self):
        """
        Gets the is_reusable of this CreateTablespaceDetails.
        Specifies whether Oracle can reuse the data file or temp file. Reuse is only allowed when the file name is provided.


        :return: The is_reusable of this CreateTablespaceDetails.
        :rtype: bool
        """
        return self._is_reusable

    @is_reusable.setter
    def is_reusable(self, is_reusable):
        """
        Sets the is_reusable of this CreateTablespaceDetails.
        Specifies whether Oracle can reuse the data file or temp file. Reuse is only allowed when the file name is provided.


        :param is_reusable: The is_reusable of this CreateTablespaceDetails.
        :type: bool
        """
        self._is_reusable = is_reusable

    @property
    def is_auto_extensible(self):
        """
        Gets the is_auto_extensible of this CreateTablespaceDetails.
        Specifies whether the data file or temp file can be extended automatically.


        :return: The is_auto_extensible of this CreateTablespaceDetails.
        :rtype: bool
        """
        return self._is_auto_extensible

    @is_auto_extensible.setter
    def is_auto_extensible(self, is_auto_extensible):
        """
        Sets the is_auto_extensible of this CreateTablespaceDetails.
        Specifies whether the data file or temp file can be extended automatically.


        :param is_auto_extensible: The is_auto_extensible of this CreateTablespaceDetails.
        :type: bool
        """
        self._is_auto_extensible = is_auto_extensible

    @property
    def auto_extend_next_size(self):
        """
        Gets the auto_extend_next_size of this CreateTablespaceDetails.
        The size of the next increment of disk space to be allocated automatically when more extents are required.


        :return: The auto_extend_next_size of this CreateTablespaceDetails.
        :rtype: oci.database_management.models.TablespaceStorageSize
        """
        return self._auto_extend_next_size

    @auto_extend_next_size.setter
    def auto_extend_next_size(self, auto_extend_next_size):
        """
        Sets the auto_extend_next_size of this CreateTablespaceDetails.
        The size of the next increment of disk space to be allocated automatically when more extents are required.


        :param auto_extend_next_size: The auto_extend_next_size of this CreateTablespaceDetails.
        :type: oci.database_management.models.TablespaceStorageSize
        """
        self._auto_extend_next_size = auto_extend_next_size

    @property
    def auto_extend_max_size(self):
        """
        Gets the auto_extend_max_size of this CreateTablespaceDetails.
        The maximum disk space allowed for automatic extension of the data files or temp files.


        :return: The auto_extend_max_size of this CreateTablespaceDetails.
        :rtype: oci.database_management.models.TablespaceStorageSize
        """
        return self._auto_extend_max_size

    @auto_extend_max_size.setter
    def auto_extend_max_size(self, auto_extend_max_size):
        """
        Sets the auto_extend_max_size of this CreateTablespaceDetails.
        The maximum disk space allowed for automatic extension of the data files or temp files.


        :param auto_extend_max_size: The auto_extend_max_size of this CreateTablespaceDetails.
        :type: oci.database_management.models.TablespaceStorageSize
        """
        self._auto_extend_max_size = auto_extend_max_size

    @property
    def is_max_size_unlimited(self):
        """
        Gets the is_max_size_unlimited of this CreateTablespaceDetails.
        Specifies whether the disk space of the data file or temp file can be limited.


        :return: The is_max_size_unlimited of this CreateTablespaceDetails.
        :rtype: bool
        """
        return self._is_max_size_unlimited

    @is_max_size_unlimited.setter
    def is_max_size_unlimited(self, is_max_size_unlimited):
        """
        Sets the is_max_size_unlimited of this CreateTablespaceDetails.
        Specifies whether the disk space of the data file or temp file can be limited.


        :param is_max_size_unlimited: The is_max_size_unlimited of this CreateTablespaceDetails.
        :type: bool
        """
        self._is_max_size_unlimited = is_max_size_unlimited

    @property
    def block_size_in_kilobytes(self):
        """
        Gets the block_size_in_kilobytes of this CreateTablespaceDetails.
        Block size for the tablespace.


        :return: The block_size_in_kilobytes of this CreateTablespaceDetails.
        :rtype: int
        """
        return self._block_size_in_kilobytes

    @block_size_in_kilobytes.setter
    def block_size_in_kilobytes(self, block_size_in_kilobytes):
        """
        Sets the block_size_in_kilobytes of this CreateTablespaceDetails.
        Block size for the tablespace.


        :param block_size_in_kilobytes: The block_size_in_kilobytes of this CreateTablespaceDetails.
        :type: int
        """
        self._block_size_in_kilobytes = block_size_in_kilobytes

    @property
    def is_encrypted(self):
        """
        Gets the is_encrypted of this CreateTablespaceDetails.
        Indicates whether the tablespace is encrypted.


        :return: The is_encrypted of this CreateTablespaceDetails.
        :rtype: bool
        """
        return self._is_encrypted

    @is_encrypted.setter
    def is_encrypted(self, is_encrypted):
        """
        Sets the is_encrypted of this CreateTablespaceDetails.
        Indicates whether the tablespace is encrypted.


        :param is_encrypted: The is_encrypted of this CreateTablespaceDetails.
        :type: bool
        """
        self._is_encrypted = is_encrypted

    @property
    def encryption_algorithm(self):
        """
        Gets the encryption_algorithm of this CreateTablespaceDetails.
        The name of the encryption algorithm to be used for tablespace encryption.


        :return: The encryption_algorithm of this CreateTablespaceDetails.
        :rtype: str
        """
        return self._encryption_algorithm

    @encryption_algorithm.setter
    def encryption_algorithm(self, encryption_algorithm):
        """
        Sets the encryption_algorithm of this CreateTablespaceDetails.
        The name of the encryption algorithm to be used for tablespace encryption.


        :param encryption_algorithm: The encryption_algorithm of this CreateTablespaceDetails.
        :type: str
        """
        self._encryption_algorithm = encryption_algorithm

    @property
    def default_compress(self):
        """
        Gets the default_compress of this CreateTablespaceDetails.
        The default compression of data for all tables created in the tablespace.

        Allowed values for this property are: "NO_COMPRESS", "BASIC_COMPRESS"


        :return: The default_compress of this CreateTablespaceDetails.
        :rtype: str
        """
        return self._default_compress

    @default_compress.setter
    def default_compress(self, default_compress):
        """
        Sets the default_compress of this CreateTablespaceDetails.
        The default compression of data for all tables created in the tablespace.


        :param default_compress: The default_compress of this CreateTablespaceDetails.
        :type: str
        """
        allowed_values = ["NO_COMPRESS", "BASIC_COMPRESS"]
        if not value_allowed_none_or_none_sentinel(default_compress, allowed_values):
            raise ValueError(
                "Invalid value for `default_compress`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._default_compress = default_compress

    @property
    def status(self):
        """
        Gets the status of this CreateTablespaceDetails.
        The status of the tablespace.

        Allowed values for this property are: "READ_ONLY", "READ_WRITE"


        :return: The status of this CreateTablespaceDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CreateTablespaceDetails.
        The status of the tablespace.


        :param status: The status of this CreateTablespaceDetails.
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
    def extent_management(self):
        """
        Gets the extent_management of this CreateTablespaceDetails.
        Specifies how the extents of the tablespace should be managed.

        Allowed values for this property are: "AUTOALLOCATE", "UNIFORM"


        :return: The extent_management of this CreateTablespaceDetails.
        :rtype: str
        """
        return self._extent_management

    @extent_management.setter
    def extent_management(self, extent_management):
        """
        Sets the extent_management of this CreateTablespaceDetails.
        Specifies how the extents of the tablespace should be managed.


        :param extent_management: The extent_management of this CreateTablespaceDetails.
        :type: str
        """
        allowed_values = ["AUTOALLOCATE", "UNIFORM"]
        if not value_allowed_none_or_none_sentinel(extent_management, allowed_values):
            raise ValueError(
                "Invalid value for `extent_management`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._extent_management = extent_management

    @property
    def extent_uniform_size(self):
        """
        Gets the extent_uniform_size of this CreateTablespaceDetails.
        The size of the extent when the tablespace is managed with uniform extents of a specific size.


        :return: The extent_uniform_size of this CreateTablespaceDetails.
        :rtype: oci.database_management.models.TablespaceStorageSize
        """
        return self._extent_uniform_size

    @extent_uniform_size.setter
    def extent_uniform_size(self, extent_uniform_size):
        """
        Sets the extent_uniform_size of this CreateTablespaceDetails.
        The size of the extent when the tablespace is managed with uniform extents of a specific size.


        :param extent_uniform_size: The extent_uniform_size of this CreateTablespaceDetails.
        :type: oci.database_management.models.TablespaceStorageSize
        """
        self._extent_uniform_size = extent_uniform_size

    @property
    def segment_management(self):
        """
        Gets the segment_management of this CreateTablespaceDetails.
        Specifies whether tablespace segment management should be automatic or manual.

        Allowed values for this property are: "AUTO", "MANUAL"


        :return: The segment_management of this CreateTablespaceDetails.
        :rtype: str
        """
        return self._segment_management

    @segment_management.setter
    def segment_management(self, segment_management):
        """
        Sets the segment_management of this CreateTablespaceDetails.
        Specifies whether tablespace segment management should be automatic or manual.


        :param segment_management: The segment_management of this CreateTablespaceDetails.
        :type: str
        """
        allowed_values = ["AUTO", "MANUAL"]
        if not value_allowed_none_or_none_sentinel(segment_management, allowed_values):
            raise ValueError(
                "Invalid value for `segment_management`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._segment_management = segment_management

    @property
    def is_default(self):
        """
        Gets the is_default of this CreateTablespaceDetails.
        Specifies whether the tablespace is the default tablespace.


        :return: The is_default of this CreateTablespaceDetails.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this CreateTablespaceDetails.
        Specifies whether the tablespace is the default tablespace.


        :param is_default: The is_default of this CreateTablespaceDetails.
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
