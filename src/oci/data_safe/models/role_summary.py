# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoleSummary(object):
    """
    Details of a role fetched from the database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RoleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param role_name:
            The value to assign to the role_name property of this RoleSummary.
        :type role_name: str

        :param authentication_type:
            The value to assign to the authentication_type property of this RoleSummary.
        :type authentication_type: str

        :param is_password_required:
            The value to assign to the is_password_required property of this RoleSummary.
        :type is_password_required: bool

        :param is_common:
            The value to assign to the is_common property of this RoleSummary.
        :type is_common: bool

        :param is_oracle_maintained:
            The value to assign to the is_oracle_maintained property of this RoleSummary.
        :type is_oracle_maintained: bool

        :param is_inherited:
            The value to assign to the is_inherited property of this RoleSummary.
        :type is_inherited: bool

        :param is_implicit:
            The value to assign to the is_implicit property of this RoleSummary.
        :type is_implicit: bool

        """
        self.swagger_types = {
            'role_name': 'str',
            'authentication_type': 'str',
            'is_password_required': 'bool',
            'is_common': 'bool',
            'is_oracle_maintained': 'bool',
            'is_inherited': 'bool',
            'is_implicit': 'bool'
        }

        self.attribute_map = {
            'role_name': 'roleName',
            'authentication_type': 'authenticationType',
            'is_password_required': 'isPasswordRequired',
            'is_common': 'isCommon',
            'is_oracle_maintained': 'isOracleMaintained',
            'is_inherited': 'isInherited',
            'is_implicit': 'isImplicit'
        }

        self._role_name = None
        self._authentication_type = None
        self._is_password_required = None
        self._is_common = None
        self._is_oracle_maintained = None
        self._is_inherited = None
        self._is_implicit = None

    @property
    def role_name(self):
        """
        **[Required]** Gets the role_name of this RoleSummary.
        Name of the role.


        :return: The role_name of this RoleSummary.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """
        Sets the role_name of this RoleSummary.
        Name of the role.


        :param role_name: The role_name of this RoleSummary.
        :type: str
        """
        self._role_name = role_name

    @property
    def authentication_type(self):
        """
        **[Required]** Gets the authentication_type of this RoleSummary.
        Type of authentication.


        :return: The authentication_type of this RoleSummary.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """
        Sets the authentication_type of this RoleSummary.
        Type of authentication.


        :param authentication_type: The authentication_type of this RoleSummary.
        :type: str
        """
        self._authentication_type = authentication_type

    @property
    def is_password_required(self):
        """
        Gets the is_password_required of this RoleSummary.
        Is password required.


        :return: The is_password_required of this RoleSummary.
        :rtype: bool
        """
        return self._is_password_required

    @is_password_required.setter
    def is_password_required(self, is_password_required):
        """
        Sets the is_password_required of this RoleSummary.
        Is password required.


        :param is_password_required: The is_password_required of this RoleSummary.
        :type: bool
        """
        self._is_password_required = is_password_required

    @property
    def is_common(self):
        """
        Gets the is_common of this RoleSummary.
        Is the role common.


        :return: The is_common of this RoleSummary.
        :rtype: bool
        """
        return self._is_common

    @is_common.setter
    def is_common(self, is_common):
        """
        Sets the is_common of this RoleSummary.
        Is the role common.


        :param is_common: The is_common of this RoleSummary.
        :type: bool
        """
        self._is_common = is_common

    @property
    def is_oracle_maintained(self):
        """
        Gets the is_oracle_maintained of this RoleSummary.
        Is the role oracle maintained.


        :return: The is_oracle_maintained of this RoleSummary.
        :rtype: bool
        """
        return self._is_oracle_maintained

    @is_oracle_maintained.setter
    def is_oracle_maintained(self, is_oracle_maintained):
        """
        Sets the is_oracle_maintained of this RoleSummary.
        Is the role oracle maintained.


        :param is_oracle_maintained: The is_oracle_maintained of this RoleSummary.
        :type: bool
        """
        self._is_oracle_maintained = is_oracle_maintained

    @property
    def is_inherited(self):
        """
        Gets the is_inherited of this RoleSummary.
        Is the role inherited.


        :return: The is_inherited of this RoleSummary.
        :rtype: bool
        """
        return self._is_inherited

    @is_inherited.setter
    def is_inherited(self, is_inherited):
        """
        Sets the is_inherited of this RoleSummary.
        Is the role inherited.


        :param is_inherited: The is_inherited of this RoleSummary.
        :type: bool
        """
        self._is_inherited = is_inherited

    @property
    def is_implicit(self):
        """
        Gets the is_implicit of this RoleSummary.
        Is the role implicit.


        :return: The is_implicit of this RoleSummary.
        :rtype: bool
        """
        return self._is_implicit

    @is_implicit.setter
    def is_implicit(self, is_implicit):
        """
        Sets the is_implicit of this RoleSummary.
        Is the role implicit.


        :param is_implicit: The is_implicit of this RoleSummary.
        :type: bool
        """
        self._is_implicit = is_implicit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
