# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTargetTypeTablespaceDetails(object):
    """
    Migration tablespace settings.
    """

    #: A constant which can be used with the target_type property of a CreateTargetTypeTablespaceDetails.
    #: This constant has a value of "ADB_S_REMAP"
    TARGET_TYPE_ADB_S_REMAP = "ADB_S_REMAP"

    #: A constant which can be used with the target_type property of a CreateTargetTypeTablespaceDetails.
    #: This constant has a value of "ADB_D_REMAP"
    TARGET_TYPE_ADB_D_REMAP = "ADB_D_REMAP"

    #: A constant which can be used with the target_type property of a CreateTargetTypeTablespaceDetails.
    #: This constant has a value of "ADB_D_AUTOCREATE"
    TARGET_TYPE_ADB_D_AUTOCREATE = "ADB_D_AUTOCREATE"

    #: A constant which can be used with the target_type property of a CreateTargetTypeTablespaceDetails.
    #: This constant has a value of "NON_ADB_REMAP"
    TARGET_TYPE_NON_ADB_REMAP = "NON_ADB_REMAP"

    #: A constant which can be used with the target_type property of a CreateTargetTypeTablespaceDetails.
    #: This constant has a value of "NON_ADB_AUTOCREATE"
    TARGET_TYPE_NON_ADB_AUTOCREATE = "NON_ADB_AUTOCREATE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTargetTypeTablespaceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_migration.models.CreateNonADBAutoCreateTablespaceDetails`
        * :class:`~oci.database_migration.models.CreateNonADBRemapTablespaceDetails`
        * :class:`~oci.database_migration.models.CreateADBDedicatedRemapTargetTablespaceDetails`
        * :class:`~oci.database_migration.models.CreateADBServerlesTablespaceDetails`
        * :class:`~oci.database_migration.models.CreateADBDedicatedAutoCreateTablespaceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_type:
            The value to assign to the target_type property of this CreateTargetTypeTablespaceDetails.
            Allowed values for this property are: "ADB_S_REMAP", "ADB_D_REMAP", "ADB_D_AUTOCREATE", "NON_ADB_REMAP", "NON_ADB_AUTOCREATE"
        :type target_type: str

        """
        self.swagger_types = {
            'target_type': 'str'
        }

        self.attribute_map = {
            'target_type': 'targetType'
        }

        self._target_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['targetType']

        if type == 'NON_ADB_AUTOCREATE':
            return 'CreateNonADBAutoCreateTablespaceDetails'

        if type == 'NON_ADB_REMAP':
            return 'CreateNonADBRemapTablespaceDetails'

        if type == 'ADB_D_REMAP':
            return 'CreateADBDedicatedRemapTargetTablespaceDetails'

        if type == 'ADB_S_REMAP':
            return 'CreateADBServerlesTablespaceDetails'

        if type == 'ADB_D_AUTOCREATE':
            return 'CreateADBDedicatedAutoCreateTablespaceDetails'
        else:
            return 'CreateTargetTypeTablespaceDetails'

    @property
    def target_type(self):
        """
        **[Required]** Gets the target_type of this CreateTargetTypeTablespaceDetails.
        Type of Database Base Migration Target.

        Allowed values for this property are: "ADB_S_REMAP", "ADB_D_REMAP", "ADB_D_AUTOCREATE", "NON_ADB_REMAP", "NON_ADB_AUTOCREATE"


        :return: The target_type of this CreateTargetTypeTablespaceDetails.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """
        Sets the target_type of this CreateTargetTypeTablespaceDetails.
        Type of Database Base Migration Target.


        :param target_type: The target_type of this CreateTargetTypeTablespaceDetails.
        :type: str
        """
        allowed_values = ["ADB_S_REMAP", "ADB_D_REMAP", "ADB_D_AUTOCREATE", "NON_ADB_REMAP", "NON_ADB_AUTOCREATE"]
        if not value_allowed_none_or_none_sentinel(target_type, allowed_values):
            raise ValueError(
                "Invalid value for `target_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._target_type = target_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
