# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FilterGroupMembershipResult(object):
    """
    FilterGroupMembershipResult model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FilterGroupMembershipResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param principal:
            The value to assign to the principal property of this FilterGroupMembershipResult.
        :type principal: oci.identity_data_plane.models.Principal

        :param group_ids:
            The value to assign to the group_ids property of this FilterGroupMembershipResult.
        :type group_ids: list[str]

        """
        self.swagger_types = {
            'principal': 'Principal',
            'group_ids': 'list[str]'
        }

        self.attribute_map = {
            'principal': 'principal',
            'group_ids': 'groupIds'
        }

        self._principal = None
        self._group_ids = None

    @property
    def principal(self):
        """
        **[Required]** Gets the principal of this FilterGroupMembershipResult.
        Return passed-in resolved principal object


        :return: The principal of this FilterGroupMembershipResult.
        :rtype: oci.identity_data_plane.models.Principal
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """
        Sets the principal of this FilterGroupMembershipResult.
        Return passed-in resolved principal object


        :param principal: The principal of this FilterGroupMembershipResult.
        :type: oci.identity_data_plane.models.Principal
        """
        self._principal = principal

    @property
    def group_ids(self):
        """
        **[Required]** Gets the group_ids of this FilterGroupMembershipResult.
        An array of group or dynamic group Ids which present the intersection between the passed-in group/dynamic-group and the actual group/dynamic-group the resovled principal belongs to.


        :return: The group_ids of this FilterGroupMembershipResult.
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """
        Sets the group_ids of this FilterGroupMembershipResult.
        An array of group or dynamic group Ids which present the intersection between the passed-in group/dynamic-group and the actual group/dynamic-group the resovled principal belongs to.


        :param group_ids: The group_ids of this FilterGroupMembershipResult.
        :type: list[str]
        """
        self._group_ids = group_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
