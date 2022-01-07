# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbSystemSourceDetails(object):
    """
    Parameters detailing how to provision the initial data of the system.
    """

    #: A constant which can be used with the source_type property of a CreateDbSystemSourceDetails.
    #: This constant has a value of "NONE"
    SOURCE_TYPE_NONE = "NONE"

    #: A constant which can be used with the source_type property of a CreateDbSystemSourceDetails.
    #: This constant has a value of "BACKUP"
    SOURCE_TYPE_BACKUP = "BACKUP"

    #: A constant which can be used with the source_type property of a CreateDbSystemSourceDetails.
    #: This constant has a value of "IMPORTURL"
    SOURCE_TYPE_IMPORTURL = "IMPORTURL"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbSystemSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.mysql.models.CreateDbSystemSourceFromBackupDetails`
        * :class:`~oci.mysql.models.CreateDbSystemSourceFromNoneDetails`
        * :class:`~oci.mysql.models.CreateDbSystemSourceImportFromUrlDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this CreateDbSystemSourceDetails.
            Allowed values for this property are: "NONE", "BACKUP", "IMPORTURL"
        :type source_type: str

        """
        self.swagger_types = {
            'source_type': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType'
        }

        self._source_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['sourceType']

        if type == 'BACKUP':
            return 'CreateDbSystemSourceFromBackupDetails'

        if type == 'NONE':
            return 'CreateDbSystemSourceFromNoneDetails'

        if type == 'IMPORTURL':
            return 'CreateDbSystemSourceImportFromUrlDetails'
        else:
            return 'CreateDbSystemSourceDetails'

    @property
    def source_type(self):
        """
        **[Required]** Gets the source_type of this CreateDbSystemSourceDetails.
        The specific source identifier.

        Allowed values for this property are: "NONE", "BACKUP", "IMPORTURL"


        :return: The source_type of this CreateDbSystemSourceDetails.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this CreateDbSystemSourceDetails.
        The specific source identifier.


        :param source_type: The source_type of this CreateDbSystemSourceDetails.
        :type: str
        """
        allowed_values = ["NONE", "BACKUP", "IMPORTURL"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            raise ValueError(
                "Invalid value for `source_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._source_type = source_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
