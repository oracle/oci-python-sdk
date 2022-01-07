# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbHomeBase(object):
    """
    Details for creating a Database Home.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the source property of a CreateDbHomeBase.
    #: This constant has a value of "NONE"
    SOURCE_NONE = "NONE"

    #: A constant which can be used with the source property of a CreateDbHomeBase.
    #: This constant has a value of "DB_BACKUP"
    SOURCE_DB_BACKUP = "DB_BACKUP"

    #: A constant which can be used with the source property of a CreateDbHomeBase.
    #: This constant has a value of "DATABASE"
    SOURCE_DATABASE = "DATABASE"

    #: A constant which can be used with the source property of a CreateDbHomeBase.
    #: This constant has a value of "VM_CLUSTER_BACKUP"
    SOURCE_VM_CLUSTER_BACKUP = "VM_CLUSTER_BACKUP"

    #: A constant which can be used with the source property of a CreateDbHomeBase.
    #: This constant has a value of "VM_CLUSTER_NEW"
    SOURCE_VM_CLUSTER_NEW = "VM_CLUSTER_NEW"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbHomeBase object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.CreateDbHomeWithDbSystemIdFromDatabaseDetails`
        * :class:`~oci.database.models.CreateDbHomeWithDbSystemIdFromBackupDetails`
        * :class:`~oci.database.models.CreateDbHomeWithVmClusterIdFromBackupDetails`
        * :class:`~oci.database.models.CreateDbHomeWithDbSystemIdDetails`
        * :class:`~oci.database.models.CreateDbHomeWithVmClusterIdDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDbHomeBase.
        :type display_name: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateDbHomeBase.
        :type kms_key_id: str

        :param kms_key_version_id:
            The value to assign to the kms_key_version_id property of this CreateDbHomeBase.
        :type kms_key_version_id: str

        :param database_software_image_id:
            The value to assign to the database_software_image_id property of this CreateDbHomeBase.
        :type database_software_image_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDbHomeBase.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDbHomeBase.
        :type defined_tags: dict(str, dict(str, object))

        :param source:
            The value to assign to the source property of this CreateDbHomeBase.
            Allowed values for this property are: "NONE", "DB_BACKUP", "DATABASE", "VM_CLUSTER_BACKUP", "VM_CLUSTER_NEW"
        :type source: str

        :param is_desupported_version:
            The value to assign to the is_desupported_version property of this CreateDbHomeBase.
        :type is_desupported_version: bool

        """
        self.swagger_types = {
            'display_name': 'str',
            'kms_key_id': 'str',
            'kms_key_version_id': 'str',
            'database_software_image_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'source': 'str',
            'is_desupported_version': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'kms_key_id': 'kmsKeyId',
            'kms_key_version_id': 'kmsKeyVersionId',
            'database_software_image_id': 'databaseSoftwareImageId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'source': 'source',
            'is_desupported_version': 'isDesupportedVersion'
        }

        self._display_name = None
        self._kms_key_id = None
        self._kms_key_version_id = None
        self._database_software_image_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._source = None
        self._is_desupported_version = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['source']

        if type == 'DATABASE':
            return 'CreateDbHomeWithDbSystemIdFromDatabaseDetails'

        if type == 'DB_BACKUP':
            return 'CreateDbHomeWithDbSystemIdFromBackupDetails'

        if type == 'VM_CLUSTER_BACKUP':
            return 'CreateDbHomeWithVmClusterIdFromBackupDetails'

        if type == 'NONE':
            return 'CreateDbHomeWithDbSystemIdDetails'

        if type == 'VM_CLUSTER_NEW':
            return 'CreateDbHomeWithVmClusterIdDetails'
        else:
            return 'CreateDbHomeBase'

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDbHomeBase.
        The user-provided name of the Database Home.


        :return: The display_name of this CreateDbHomeBase.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDbHomeBase.
        The user-provided name of the Database Home.


        :param display_name: The display_name of this CreateDbHomeBase.
        :type: str
        """
        self._display_name = display_name

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this CreateDbHomeBase.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :return: The kms_key_id of this CreateDbHomeBase.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this CreateDbHomeBase.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :param kms_key_id: The kms_key_id of this CreateDbHomeBase.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def kms_key_version_id(self):
        """
        Gets the kms_key_version_id of this CreateDbHomeBase.
        The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.


        :return: The kms_key_version_id of this CreateDbHomeBase.
        :rtype: str
        """
        return self._kms_key_version_id

    @kms_key_version_id.setter
    def kms_key_version_id(self, kms_key_version_id):
        """
        Sets the kms_key_version_id of this CreateDbHomeBase.
        The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.


        :param kms_key_version_id: The kms_key_version_id of this CreateDbHomeBase.
        :type: str
        """
        self._kms_key_version_id = kms_key_version_id

    @property
    def database_software_image_id(self):
        """
        Gets the database_software_image_id of this CreateDbHomeBase.
        The database software image `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_software_image_id of this CreateDbHomeBase.
        :rtype: str
        """
        return self._database_software_image_id

    @database_software_image_id.setter
    def database_software_image_id(self, database_software_image_id):
        """
        Sets the database_software_image_id of this CreateDbHomeBase.
        The database software image `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_software_image_id: The database_software_image_id of this CreateDbHomeBase.
        :type: str
        """
        self._database_software_image_id = database_software_image_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDbHomeBase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDbHomeBase.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDbHomeBase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDbHomeBase.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDbHomeBase.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDbHomeBase.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDbHomeBase.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDbHomeBase.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def source(self):
        """
        Gets the source of this CreateDbHomeBase.
        The source of database: NONE for creating a new database. DB_BACKUP for creating a new database by restoring from a database backup.

        Allowed values for this property are: "NONE", "DB_BACKUP", "DATABASE", "VM_CLUSTER_BACKUP", "VM_CLUSTER_NEW"


        :return: The source of this CreateDbHomeBase.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CreateDbHomeBase.
        The source of database: NONE for creating a new database. DB_BACKUP for creating a new database by restoring from a database backup.


        :param source: The source of this CreateDbHomeBase.
        :type: str
        """
        allowed_values = ["NONE", "DB_BACKUP", "DATABASE", "VM_CLUSTER_BACKUP", "VM_CLUSTER_NEW"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            raise ValueError(
                "Invalid value for `source`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._source = source

    @property
    def is_desupported_version(self):
        """
        Gets the is_desupported_version of this CreateDbHomeBase.
        If true, the customer acknowledges that the specified Oracle Database software is an older release that is not currently supported by OCI.


        :return: The is_desupported_version of this CreateDbHomeBase.
        :rtype: bool
        """
        return self._is_desupported_version

    @is_desupported_version.setter
    def is_desupported_version(self, is_desupported_version):
        """
        Sets the is_desupported_version of this CreateDbHomeBase.
        If true, the customer acknowledges that the specified Oracle Database software is an older release that is not currently supported by OCI.


        :param is_desupported_version: The is_desupported_version of this CreateDbHomeBase.
        :type: bool
        """
        self._is_desupported_version = is_desupported_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
