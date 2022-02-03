# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AsmPropertySummary(object):
    """
    The summary of ASM properties.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AsmPropertySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param disk_group:
            The value to assign to the disk_group property of this AsmPropertySummary.
        :type disk_group: str

        """
        self.swagger_types = {
            'disk_group': 'str'
        }

        self.attribute_map = {
            'disk_group': 'diskGroup'
        }

        self._disk_group = None

    @property
    def disk_group(self):
        """
        **[Required]** Gets the disk_group of this AsmPropertySummary.
        The name of the disk group.


        :return: The disk_group of this AsmPropertySummary.
        :rtype: str
        """
        return self._disk_group

    @disk_group.setter
    def disk_group(self, disk_group):
        """
        Sets the disk_group of this AsmPropertySummary.
        The name of the disk group.


        :param disk_group: The disk_group of this AsmPropertySummary.
        :type: str
        """
        self._disk_group = disk_group

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
