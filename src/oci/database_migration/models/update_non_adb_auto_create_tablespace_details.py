# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_target_type_tablespace_details import UpdateTargetTypeTablespaceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNonADBAutoCreateTablespaceDetails(UpdateTargetTypeTablespaceDetails):
    """
    Migration tablespace settings valid for NON-ADB target type using auto create feature.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNonADBAutoCreateTablespaceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.UpdateNonADBAutoCreateTablespaceDetails.target_type` attribute
        of this class is ``NON_ADB_AUTOCREATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_type:
            The value to assign to the target_type property of this UpdateNonADBAutoCreateTablespaceDetails.
            Allowed values for this property are: "ADB_S_REMAP", "ADB_D_REMAP", "ADB_D_AUTOCREATE", "NON_ADB_REMAP", "NON_ADB_AUTOCREATE", "TARGET_DEFAULTS_REMAP", "TARGET_DEFAULTS_AUTOCREATE"
        :type target_type: str

        :param is_auto_create:
            The value to assign to the is_auto_create property of this UpdateNonADBAutoCreateTablespaceDetails.
        :type is_auto_create: bool

        :param is_big_file:
            The value to assign to the is_big_file property of this UpdateNonADBAutoCreateTablespaceDetails.
        :type is_big_file: bool

        :param extend_size_in_mbs:
            The value to assign to the extend_size_in_mbs property of this UpdateNonADBAutoCreateTablespaceDetails.
        :type extend_size_in_mbs: int

        """
        self.swagger_types = {
            'target_type': 'str',
            'is_auto_create': 'bool',
            'is_big_file': 'bool',
            'extend_size_in_mbs': 'int'
        }

        self.attribute_map = {
            'target_type': 'targetType',
            'is_auto_create': 'isAutoCreate',
            'is_big_file': 'isBigFile',
            'extend_size_in_mbs': 'extendSizeInMBs'
        }

        self._target_type = None
        self._is_auto_create = None
        self._is_big_file = None
        self._extend_size_in_mbs = None
        self._target_type = 'NON_ADB_AUTOCREATE'

    @property
    def is_auto_create(self):
        """
        Gets the is_auto_create of this UpdateNonADBAutoCreateTablespaceDetails.
        True to auto-create tablespace in the target Database.


        :return: The is_auto_create of this UpdateNonADBAutoCreateTablespaceDetails.
        :rtype: bool
        """
        return self._is_auto_create

    @is_auto_create.setter
    def is_auto_create(self, is_auto_create):
        """
        Sets the is_auto_create of this UpdateNonADBAutoCreateTablespaceDetails.
        True to auto-create tablespace in the target Database.


        :param is_auto_create: The is_auto_create of this UpdateNonADBAutoCreateTablespaceDetails.
        :type: bool
        """
        self._is_auto_create = is_auto_create

    @property
    def is_big_file(self):
        """
        Gets the is_big_file of this UpdateNonADBAutoCreateTablespaceDetails.
        True set tablespace to big file.


        :return: The is_big_file of this UpdateNonADBAutoCreateTablespaceDetails.
        :rtype: bool
        """
        return self._is_big_file

    @is_big_file.setter
    def is_big_file(self, is_big_file):
        """
        Sets the is_big_file of this UpdateNonADBAutoCreateTablespaceDetails.
        True set tablespace to big file.


        :param is_big_file: The is_big_file of this UpdateNonADBAutoCreateTablespaceDetails.
        :type: bool
        """
        self._is_big_file = is_big_file

    @property
    def extend_size_in_mbs(self):
        """
        Gets the extend_size_in_mbs of this UpdateNonADBAutoCreateTablespaceDetails.
        Size of extend in MB. Can only be specified if 'isBigFile' property is set to true.


        :return: The extend_size_in_mbs of this UpdateNonADBAutoCreateTablespaceDetails.
        :rtype: int
        """
        return self._extend_size_in_mbs

    @extend_size_in_mbs.setter
    def extend_size_in_mbs(self, extend_size_in_mbs):
        """
        Sets the extend_size_in_mbs of this UpdateNonADBAutoCreateTablespaceDetails.
        Size of extend in MB. Can only be specified if 'isBigFile' property is set to true.


        :param extend_size_in_mbs: The extend_size_in_mbs of this UpdateNonADBAutoCreateTablespaceDetails.
        :type: int
        """
        self._extend_size_in_mbs = extend_size_in_mbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
