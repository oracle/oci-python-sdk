# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserExtSocialAccounts(object):
    """
    Description:

    **SCIM++ Properties:**
    - idcsCompositeKey: [value]
    - idcsSearchable: true
    - multiValued: true
    - mutability: readOnly
    - required: false
    - returned: request
    - idcsPii: true
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UserExtSocialAccounts object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this UserExtSocialAccounts.
        :type value: str

        :param display:
            The value to assign to the display property of this UserExtSocialAccounts.
        :type display: str

        :param ref:
            The value to assign to the ref property of this UserExtSocialAccounts.
        :type ref: str

        """
        self.swagger_types = {
            'value': 'str',
            'display': 'str',
            'ref': 'str'
        }
        self.attribute_map = {
            'value': 'value',
            'display': 'display',
            'ref': '$ref'
        }
        self._value = None
        self._display = None
        self._ref = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this UserExtSocialAccounts.

        :return: The value of this UserExtSocialAccounts.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserExtSocialAccounts.

        :param value: The value of this UserExtSocialAccounts.
        :type: str
        """
        self._value = value

    @property
    def display(self):
        """
        Gets the display of this UserExtSocialAccounts.
        A human readable name, primarily used for display purposes. READ-ONLY.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this UserExtSocialAccounts.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this UserExtSocialAccounts.
        A human readable name, primarily used for display purposes. READ-ONLY.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this UserExtSocialAccounts.
        :type: str
        """
        self._display = display

    @property
    def ref(self):
        """
        Gets the ref of this UserExtSocialAccounts.
        The URI of the corresponding SocialAccount resource linked with the user

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this UserExtSocialAccounts.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this UserExtSocialAccounts.
        The URI of the corresponding SocialAccount resource linked with the user

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this UserExtSocialAccounts.
        :type: str
        """
        self._ref = ref

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
