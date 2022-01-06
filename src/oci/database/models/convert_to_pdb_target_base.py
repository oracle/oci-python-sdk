# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConvertToPdbTargetBase(object):
    """
    Details of the container database in which the converted pluggable database will be located.
    """

    #: A constant which can be used with the target property of a ConvertToPdbTargetBase.
    #: This constant has a value of "NEW_DATABASE"
    TARGET_NEW_DATABASE = "NEW_DATABASE"

    def __init__(self, **kwargs):
        """
        Initializes a new ConvertToPdbTargetBase object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.PdbConversionToNewDatabaseDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target:
            The value to assign to the target property of this ConvertToPdbTargetBase.
            Allowed values for this property are: "NEW_DATABASE"
        :type target: str

        """
        self.swagger_types = {
            'target': 'str'
        }

        self.attribute_map = {
            'target': 'target'
        }

        self._target = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['target']

        if type == 'NEW_DATABASE':
            return 'PdbConversionToNewDatabaseDetails'
        else:
            return 'ConvertToPdbTargetBase'

    @property
    def target(self):
        """
        Gets the target of this ConvertToPdbTargetBase.
        The target container database of the pluggable database created by the database conversion operation. Currently, the database conversion operation only supports creating the pluggable database in a new container database.
         - Use `NEW_DATABASE` to specify that the pluggable database be created within a new container database in the same database home.

        Allowed values for this property are: "NEW_DATABASE"


        :return: The target of this ConvertToPdbTargetBase.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this ConvertToPdbTargetBase.
        The target container database of the pluggable database created by the database conversion operation. Currently, the database conversion operation only supports creating the pluggable database in a new container database.
         - Use `NEW_DATABASE` to specify that the pluggable database be created within a new container database in the same database home.


        :param target: The target of this ConvertToPdbTargetBase.
        :type: str
        """
        allowed_values = ["NEW_DATABASE"]
        if not value_allowed_none_or_none_sentinel(target, allowed_values):
            raise ValueError(
                "Invalid value for `target`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._target = target

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
