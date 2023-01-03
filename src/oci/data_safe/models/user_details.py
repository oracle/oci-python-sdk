# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserDetails(object):
    """
    The details of a particular user.
    """

    #: A constant which can be used with the authentication_type property of a UserDetails.
    #: This constant has a value of "PASSWORD"
    AUTHENTICATION_TYPE_PASSWORD = "PASSWORD"

    #: A constant which can be used with the authentication_type property of a UserDetails.
    #: This constant has a value of "NONE"
    AUTHENTICATION_TYPE_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new UserDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UserDetails.
        :type name: str

        :param status:
            The value to assign to the status property of this UserDetails.
        :type status: str

        :param profile:
            The value to assign to the profile property of this UserDetails.
        :type profile: str

        :param tablespace:
            The value to assign to the tablespace property of this UserDetails.
        :type tablespace: str

        :param is_user_predefined_by_oracle:
            The value to assign to the is_user_predefined_by_oracle property of this UserDetails.
        :type is_user_predefined_by_oracle: bool

        :param authentication_type:
            The value to assign to the authentication_type property of this UserDetails.
            Allowed values for this property are: "PASSWORD", "NONE"
        :type authentication_type: str

        """
        self.swagger_types = {
            'name': 'str',
            'status': 'str',
            'profile': 'str',
            'tablespace': 'str',
            'is_user_predefined_by_oracle': 'bool',
            'authentication_type': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'status': 'status',
            'profile': 'profile',
            'tablespace': 'tablespace',
            'is_user_predefined_by_oracle': 'isUserPredefinedByOracle',
            'authentication_type': 'authenticationType'
        }

        self._name = None
        self._status = None
        self._profile = None
        self._tablespace = None
        self._is_user_predefined_by_oracle = None
        self._authentication_type = None

    @property
    def name(self):
        """
        Gets the name of this UserDetails.
        The name of the user.


        :return: The name of this UserDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserDetails.
        The name of the user.


        :param name: The name of this UserDetails.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """
        Gets the status of this UserDetails.
        The status of the user account.


        :return: The status of this UserDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UserDetails.
        The status of the user account.


        :param status: The status of this UserDetails.
        :type: str
        """
        self._status = status

    @property
    def profile(self):
        """
        Gets the profile of this UserDetails.
        The name of the profile assigned to the user.


        :return: The profile of this UserDetails.
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """
        Sets the profile of this UserDetails.
        The name of the profile assigned to the user.


        :param profile: The profile of this UserDetails.
        :type: str
        """
        self._profile = profile

    @property
    def tablespace(self):
        """
        Gets the tablespace of this UserDetails.
        The default tablespace of the user.


        :return: The tablespace of this UserDetails.
        :rtype: str
        """
        return self._tablespace

    @tablespace.setter
    def tablespace(self, tablespace):
        """
        Sets the tablespace of this UserDetails.
        The default tablespace of the user.


        :param tablespace: The tablespace of this UserDetails.
        :type: str
        """
        self._tablespace = tablespace

    @property
    def is_user_predefined_by_oracle(self):
        """
        Gets the is_user_predefined_by_oracle of this UserDetails.
        Indicates whether or not the user is predefined by ORACLE.


        :return: The is_user_predefined_by_oracle of this UserDetails.
        :rtype: bool
        """
        return self._is_user_predefined_by_oracle

    @is_user_predefined_by_oracle.setter
    def is_user_predefined_by_oracle(self, is_user_predefined_by_oracle):
        """
        Sets the is_user_predefined_by_oracle of this UserDetails.
        Indicates whether or not the user is predefined by ORACLE.


        :param is_user_predefined_by_oracle: The is_user_predefined_by_oracle of this UserDetails.
        :type: bool
        """
        self._is_user_predefined_by_oracle = is_user_predefined_by_oracle

    @property
    def authentication_type(self):
        """
        Gets the authentication_type of this UserDetails.
        The authentication type of the user.

        Allowed values for this property are: "PASSWORD", "NONE"


        :return: The authentication_type of this UserDetails.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """
        Sets the authentication_type of this UserDetails.
        The authentication type of the user.


        :param authentication_type: The authentication_type of this UserDetails.
        :type: str
        """
        allowed_values = ["PASSWORD", "NONE"]
        if not value_allowed_none_or_none_sentinel(authentication_type, allowed_values):
            raise ValueError(
                "Invalid value for `authentication_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._authentication_type = authentication_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
