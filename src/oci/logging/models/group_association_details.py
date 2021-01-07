# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GroupAssociationDetails(object):
    """
    Groups using the configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GroupAssociationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param group_list:
            The value to assign to the group_list property of this GroupAssociationDetails.
        :type group_list: list[str]

        """
        self.swagger_types = {
            'group_list': 'list[str]'
        }

        self.attribute_map = {
            'group_list': 'groupList'
        }

        self._group_list = None

    @property
    def group_list(self):
        """
        Gets the group_list of this GroupAssociationDetails.
        list of group/dynamic group ids associated with this configuration.


        :return: The group_list of this GroupAssociationDetails.
        :rtype: list[str]
        """
        return self._group_list

    @group_list.setter
    def group_list(self, group_list):
        """
        Sets the group_list of this GroupAssociationDetails.
        list of group/dynamic group ids associated with this configuration.


        :param group_list: The group_list of this GroupAssociationDetails.
        :type: list[str]
        """
        self._group_list = group_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
