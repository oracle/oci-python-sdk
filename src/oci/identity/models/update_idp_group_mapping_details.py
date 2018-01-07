# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIdpGroupMappingDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIdpGroupMappingDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param idp_group_name:
            The value to assign to the idp_group_name property of this UpdateIdpGroupMappingDetails.
        :type idp_group_name: str

        :param group_id:
            The value to assign to the group_id property of this UpdateIdpGroupMappingDetails.
        :type group_id: str

        """
        self.swagger_types = {
            'idp_group_name': 'str',
            'group_id': 'str'
        }

        self.attribute_map = {
            'idp_group_name': 'idpGroupName',
            'group_id': 'groupId'
        }

        self._idp_group_name = None
        self._group_id = None

    @property
    def idp_group_name(self):
        """
        Gets the idp_group_name of this UpdateIdpGroupMappingDetails.
        The idp group name.


        :return: The idp_group_name of this UpdateIdpGroupMappingDetails.
        :rtype: str
        """
        return self._idp_group_name

    @idp_group_name.setter
    def idp_group_name(self, idp_group_name):
        """
        Sets the idp_group_name of this UpdateIdpGroupMappingDetails.
        The idp group name.


        :param idp_group_name: The idp_group_name of this UpdateIdpGroupMappingDetails.
        :type: str
        """
        self._idp_group_name = idp_group_name

    @property
    def group_id(self):
        """
        Gets the group_id of this UpdateIdpGroupMappingDetails.
        The OCID of the group.


        :return: The group_id of this UpdateIdpGroupMappingDetails.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this UpdateIdpGroupMappingDetails.
        The OCID of the group.


        :param group_id: The group_id of this UpdateIdpGroupMappingDetails.
        :type: str
        """
        self._group_id = group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
