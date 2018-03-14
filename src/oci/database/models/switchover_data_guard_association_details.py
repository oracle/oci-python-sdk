# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SwitchoverDataGuardAssociationDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new SwitchoverDataGuardAssociationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_admin_password:
            The value to assign to the database_admin_password property of this SwitchoverDataGuardAssociationDetails.
        :type database_admin_password: str

        """
        self.swagger_types = {
            'database_admin_password': 'str'
        }

        self.attribute_map = {
            'database_admin_password': 'databaseAdminPassword'
        }

        self._database_admin_password = None

    @property
    def database_admin_password(self):
        """
        **[Required]** Gets the database_admin_password of this SwitchoverDataGuardAssociationDetails.
        The DB System administrator password.


        :return: The database_admin_password of this SwitchoverDataGuardAssociationDetails.
        :rtype: str
        """
        return self._database_admin_password

    @database_admin_password.setter
    def database_admin_password(self, database_admin_password):
        """
        Sets the database_admin_password of this SwitchoverDataGuardAssociationDetails.
        The DB System administrator password.


        :param database_admin_password: The database_admin_password of this SwitchoverDataGuardAssociationDetails.
        :type: str
        """
        self._database_admin_password = database_admin_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
