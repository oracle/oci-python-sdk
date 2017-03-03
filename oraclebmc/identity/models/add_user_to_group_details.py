# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class AddUserToGroupDetails(object):

    def __init__(self):

        self.swagger_types = {
            'user_id': 'str',
            'group_id': 'str'
        }

        self.attribute_map = {
            'user_id': 'userId',
            'group_id': 'groupId'
        }

        self._user_id = None
        self._group_id = None

    @property
    def user_id(self):
        """
        Gets the user_id of this AddUserToGroupDetails.
        The OCID of the user.


        :return: The user_id of this AddUserToGroupDetails.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AddUserToGroupDetails.
        The OCID of the user.


        :param user_id: The user_id of this AddUserToGroupDetails.
        :type: str
        """
        self._user_id = user_id

    @property
    def group_id(self):
        """
        Gets the group_id of this AddUserToGroupDetails.
        The OCID of the group.


        :return: The group_id of this AddUserToGroupDetails.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this AddUserToGroupDetails.
        The OCID of the group.


        :param group_id: The group_id of this AddUserToGroupDetails.
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
