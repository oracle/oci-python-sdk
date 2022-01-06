# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiskGroupDetails(object):
    """
    Information about a diskgroup which includes diskgroup name and ASM name.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DiskGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param diskgroup_name:
            The value to assign to the diskgroup_name property of this DiskGroupDetails.
        :type diskgroup_name: str

        :param asm_name:
            The value to assign to the asm_name property of this DiskGroupDetails.
        :type asm_name: str

        """
        self.swagger_types = {
            'diskgroup_name': 'str',
            'asm_name': 'str'
        }

        self.attribute_map = {
            'diskgroup_name': 'diskgroupName',
            'asm_name': 'asmName'
        }

        self._diskgroup_name = None
        self._asm_name = None

    @property
    def diskgroup_name(self):
        """
        **[Required]** Gets the diskgroup_name of this DiskGroupDetails.
        The diskgroup name.


        :return: The diskgroup_name of this DiskGroupDetails.
        :rtype: str
        """
        return self._diskgroup_name

    @diskgroup_name.setter
    def diskgroup_name(self, diskgroup_name):
        """
        Sets the diskgroup_name of this DiskGroupDetails.
        The diskgroup name.


        :param diskgroup_name: The diskgroup_name of this DiskGroupDetails.
        :type: str
        """
        self._diskgroup_name = diskgroup_name

    @property
    def asm_name(self):
        """
        **[Required]** Gets the asm_name of this DiskGroupDetails.
        The ASM name.


        :return: The asm_name of this DiskGroupDetails.
        :rtype: str
        """
        return self._asm_name

    @asm_name.setter
    def asm_name(self, asm_name):
        """
        Sets the asm_name of this DiskGroupDetails.
        The ASM name.


        :param asm_name: The asm_name of this DiskGroupDetails.
        :type: str
        """
        self._asm_name = asm_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
