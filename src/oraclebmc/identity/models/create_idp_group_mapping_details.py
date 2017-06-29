# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateIdpGroupMappingDetails(object):

    def __init__(self):

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
        Gets the idp_group_name of this CreateIdpGroupMappingDetails.
        The name of the IdP group you want to map.


        :return: The idp_group_name of this CreateIdpGroupMappingDetails.
        :rtype: str
        """
        return self._idp_group_name

    @idp_group_name.setter
    def idp_group_name(self, idp_group_name):
        """
        Sets the idp_group_name of this CreateIdpGroupMappingDetails.
        The name of the IdP group you want to map.


        :param idp_group_name: The idp_group_name of this CreateIdpGroupMappingDetails.
        :type: str
        """
        self._idp_group_name = idp_group_name

    @property
    def group_id(self):
        """
        Gets the group_id of this CreateIdpGroupMappingDetails.
        The OCID of the IAM Service :class:`Group`
        you want to map to the IdP group.


        :return: The group_id of this CreateIdpGroupMappingDetails.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this CreateIdpGroupMappingDetails.
        The OCID of the IAM Service :class:`Group`
        you want to map to the IdP group.


        :param group_id: The group_id of this CreateIdpGroupMappingDetails.
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
