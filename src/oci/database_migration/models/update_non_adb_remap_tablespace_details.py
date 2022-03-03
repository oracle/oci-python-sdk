# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_target_type_tablespace_details import UpdateTargetTypeTablespaceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNonADBRemapTablespaceDetails(UpdateTargetTypeTablespaceDetails):
    """
    Migration tablespace settings valid for NON-ADB target type using remap feature.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNonADBRemapTablespaceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.UpdateNonADBRemapTablespaceDetails.target_type` attribute
        of this class is ``NON_ADB_REMAP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_type:
            The value to assign to the target_type property of this UpdateNonADBRemapTablespaceDetails.
            Allowed values for this property are: "ADB_S_REMAP", "ADB_D_REMAP", "ADB_D_AUTOCREATE", "NON_ADB_REMAP", "NON_ADB_AUTOCREATE", "TARGET_DEFAULTS_REMAP", "TARGET_DEFAULTS_AUTOCREATE"
        :type target_type: str

        :param remap_target:
            The value to assign to the remap_target property of this UpdateNonADBRemapTablespaceDetails.
        :type remap_target: str

        """
        self.swagger_types = {
            'target_type': 'str',
            'remap_target': 'str'
        }

        self.attribute_map = {
            'target_type': 'targetType',
            'remap_target': 'remapTarget'
        }

        self._target_type = None
        self._remap_target = None
        self._target_type = 'NON_ADB_REMAP'

    @property
    def remap_target(self):
        """
        Gets the remap_target of this UpdateNonADBRemapTablespaceDetails.
        Name of tablespace at target to which the source database tablespace need to be remapped.


        :return: The remap_target of this UpdateNonADBRemapTablespaceDetails.
        :rtype: str
        """
        return self._remap_target

    @remap_target.setter
    def remap_target(self, remap_target):
        """
        Sets the remap_target of this UpdateNonADBRemapTablespaceDetails.
        Name of tablespace at target to which the source database tablespace need to be remapped.


        :param remap_target: The remap_target of this UpdateNonADBRemapTablespaceDetails.
        :type: str
        """
        self._remap_target = remap_target

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
