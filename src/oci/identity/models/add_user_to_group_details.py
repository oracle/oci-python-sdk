# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddUserToGroupDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new AddUserToGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param user_id:
            The value to assign to the user_id property of this AddUserToGroupDetails.
        :type user_id: str

        :param group_id:
            The value to assign to the group_id property of this AddUserToGroupDetails.
        :type group_id: str

        """
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
        **[Required]** Gets the user_id of this AddUserToGroupDetails.
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
        **[Required]** Gets the group_id of this AddUserToGroupDetails.
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
