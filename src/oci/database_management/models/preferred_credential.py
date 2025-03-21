# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PreferredCredential(object):
    """
    The details of the preferred credential.
    """

    #: A constant which can be used with the type property of a PreferredCredential.
    #: This constant has a value of "BASIC"
    TYPE_BASIC = "BASIC"

    #: A constant which can be used with the type property of a PreferredCredential.
    #: This constant has a value of "NAMED_CREDENTIAL"
    TYPE_NAMED_CREDENTIAL = "NAMED_CREDENTIAL"

    #: A constant which can be used with the status property of a PreferredCredential.
    #: This constant has a value of "SET"
    STATUS_SET = "SET"

    #: A constant which can be used with the status property of a PreferredCredential.
    #: This constant has a value of "NOT_SET"
    STATUS_NOT_SET = "NOT_SET"

    def __init__(self, **kwargs):
        """
        Initializes a new PreferredCredential object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.NamedPreferredCredential`
        * :class:`~oci.database_management.models.BasicPreferredCredential`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this PreferredCredential.
            Allowed values for this property are: "BASIC", "NAMED_CREDENTIAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param credential_name:
            The value to assign to the credential_name property of this PreferredCredential.
        :type credential_name: str

        :param status:
            The value to assign to the status property of this PreferredCredential.
            Allowed values for this property are: "SET", "NOT_SET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param is_accessible:
            The value to assign to the is_accessible property of this PreferredCredential.
        :type is_accessible: bool

        """
        self.swagger_types = {
            'type': 'str',
            'credential_name': 'str',
            'status': 'str',
            'is_accessible': 'bool'
        }
        self.attribute_map = {
            'type': 'type',
            'credential_name': 'credentialName',
            'status': 'status',
            'is_accessible': 'isAccessible'
        }
        self._type = None
        self._credential_name = None
        self._status = None
        self._is_accessible = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'NAMED_CREDENTIAL':
            return 'NamedPreferredCredential'

        if type == 'BASIC':
            return 'BasicPreferredCredential'
        else:
            return 'PreferredCredential'

    @property
    def type(self):
        """
        Gets the type of this PreferredCredential.
        The type of preferred credential. Only 'BASIC' is supported currently.

        Allowed values for this property are: "BASIC", "NAMED_CREDENTIAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this PreferredCredential.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PreferredCredential.
        The type of preferred credential. Only 'BASIC' is supported currently.


        :param type: The type of this PreferredCredential.
        :type: str
        """
        allowed_values = ["BASIC", "NAMED_CREDENTIAL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def credential_name(self):
        """
        Gets the credential_name of this PreferredCredential.
        The name of the preferred credential.


        :return: The credential_name of this PreferredCredential.
        :rtype: str
        """
        return self._credential_name

    @credential_name.setter
    def credential_name(self, credential_name):
        """
        Sets the credential_name of this PreferredCredential.
        The name of the preferred credential.


        :param credential_name: The credential_name of this PreferredCredential.
        :type: str
        """
        self._credential_name = credential_name

    @property
    def status(self):
        """
        Gets the status of this PreferredCredential.
        The status of the preferred credential.

        Allowed values for this property are: "SET", "NOT_SET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this PreferredCredential.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PreferredCredential.
        The status of the preferred credential.


        :param status: The status of this PreferredCredential.
        :type: str
        """
        allowed_values = ["SET", "NOT_SET"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def is_accessible(self):
        """
        Gets the is_accessible of this PreferredCredential.
        Indicates whether the preferred credential is accessible.


        :return: The is_accessible of this PreferredCredential.
        :rtype: bool
        """
        return self._is_accessible

    @is_accessible.setter
    def is_accessible(self, is_accessible):
        """
        Sets the is_accessible of this PreferredCredential.
        Indicates whether the preferred credential is accessible.


        :param is_accessible: The is_accessible of this PreferredCredential.
        :type: bool
        """
        self._is_accessible = is_accessible

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
