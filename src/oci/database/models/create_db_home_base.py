# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


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
    #: This constant has a value of "VM_CLUSTER_NEW"
    SOURCE_VM_CLUSTER_NEW = "VM_CLUSTER_NEW"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbHomeBase object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.CreateDbHomeWithDbSystemIdFromBackupDetails`
        * :class:`~oci.database.models.CreateDbHomeWithDbSystemIdDetails`
        * :class:`~oci.database.models.CreateDbHomeWithVmClusterIdDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDbHomeBase.
        :type display_name: str

        :param source:
            The value to assign to the source property of this CreateDbHomeBase.
            Allowed values for this property are: "NONE", "DB_BACKUP", "VM_CLUSTER_NEW"
        :type source: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'source': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'source': 'source'
        }

        self._display_name = None
        self._source = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['source']

        if type == 'DB_BACKUP':
            return 'CreateDbHomeWithDbSystemIdFromBackupDetails'

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
    def source(self):
        """
        Gets the source of this CreateDbHomeBase.
        The source of database: NONE for creating a new database. DB_BACKUP for creating a new database by restoring from a database backup.

        Allowed values for this property are: "NONE", "DB_BACKUP", "VM_CLUSTER_NEW"


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
        allowed_values = ["NONE", "DB_BACKUP", "VM_CLUSTER_NEW"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            raise ValueError(
                "Invalid value for `source`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._source = source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
