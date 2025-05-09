# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TestPreferredCredentialDetails(object):
    """
    The status of the preferred credential test. The status is 'SUCCEEDED' if the preferred credential is working else the status is 'FAILED'.
    """

    #: A constant which can be used with the type property of a TestPreferredCredentialDetails.
    #: This constant has a value of "BASIC"
    TYPE_BASIC = "BASIC"

    #: A constant which can be used with the type property of a TestPreferredCredentialDetails.
    #: This constant has a value of "NAMED_CREDENTIAL"
    TYPE_NAMED_CREDENTIAL = "NAMED_CREDENTIAL"

    def __init__(self, **kwargs):
        """
        Initializes a new TestPreferredCredentialDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.TestNamedPreferredCredentialDetails`
        * :class:`~oci.database_management.models.TestBasicPreferredCredentialDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TestPreferredCredentialDetails.
            Allowed values for this property are: "BASIC", "NAMED_CREDENTIAL"
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }
        self.attribute_map = {
            'type': 'type'
        }
        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'NAMED_CREDENTIAL':
            return 'TestNamedPreferredCredentialDetails'

        if type == 'BASIC':
            return 'TestBasicPreferredCredentialDetails'
        else:
            return 'TestPreferredCredentialDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this TestPreferredCredentialDetails.
        The type of preferred credential. Only 'BASIC' is supported currently.

        Allowed values for this property are: "BASIC", "NAMED_CREDENTIAL"


        :return: The type of this TestPreferredCredentialDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TestPreferredCredentialDetails.
        The type of preferred credential. Only 'BASIC' is supported currently.


        :param type: The type of this TestPreferredCredentialDetails.
        :type: str
        """
        allowed_values = ["BASIC", "NAMED_CREDENTIAL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
