# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserExtSupportAccounts(object):
    """
    A list of Support Accounts corresponding to user.

    **Added In:** 2103141444

    **SCIM++ Properties:**
    - idcsCompositeKey: [value]
    - idcsSearchable: true
    - multiValued: true
    - mutability: readOnly
    - required: false
    - returned: request
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UserExtSupportAccounts object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this UserExtSupportAccounts.
        :type value: str

        :param provider:
            The value to assign to the provider property of this UserExtSupportAccounts.
        :type provider: str

        :param user_id:
            The value to assign to the user_id property of this UserExtSupportAccounts.
        :type user_id: str

        :param ocid:
            The value to assign to the ocid property of this UserExtSupportAccounts.
        :type ocid: str

        :param ref:
            The value to assign to the ref property of this UserExtSupportAccounts.
        :type ref: str

        """
        self.swagger_types = {
            'value': 'str',
            'provider': 'str',
            'user_id': 'str',
            'ocid': 'str',
            'ref': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'provider': 'provider',
            'user_id': 'userId',
            'ocid': 'ocid',
            'ref': '$ref'
        }

        self._value = None
        self._provider = None
        self._user_id = None
        self._ocid = None
        self._ref = None

    @property
    def value(self):
        """
        Gets the value of this UserExtSupportAccounts.
        The identifier of the User's support Account.

        **Added In:** 2103141444

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this UserExtSupportAccounts.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserExtSupportAccounts.
        The identifier of the User's support Account.

        **Added In:** 2103141444

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this UserExtSupportAccounts.
        :type: str
        """
        self._value = value

    @property
    def provider(self):
        """
        Gets the provider of this UserExtSupportAccounts.
        User Support Account Provider

        **Added In:** 2103141444

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The provider of this UserExtSupportAccounts.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this UserExtSupportAccounts.
        User Support Account Provider

        **Added In:** 2103141444

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param provider: The provider of this UserExtSupportAccounts.
        :type: str
        """
        self._provider = provider

    @property
    def user_id(self):
        """
        Gets the user_id of this UserExtSupportAccounts.
        User Support User Id

        **Added In:** 2103141444

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The user_id of this UserExtSupportAccounts.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UserExtSupportAccounts.
        User Support User Id

        **Added In:** 2103141444

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param user_id: The user_id of this UserExtSupportAccounts.
        :type: str
        """
        self._user_id = user_id

    @property
    def ocid(self):
        """
        Gets the ocid of this UserExtSupportAccounts.
        Ocid of the User's Support Account.

        **Added In:** 2103141444

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The ocid of this UserExtSupportAccounts.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this UserExtSupportAccounts.
        Ocid of the User's Support Account.

        **Added In:** 2103141444

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param ocid: The ocid of this UserExtSupportAccounts.
        :type: str
        """
        self._ocid = ocid

    @property
    def ref(self):
        """
        Gets the ref of this UserExtSupportAccounts.
        The URI of the corresponding Support Account resource to which the user belongs

        **Added In:** 2103141444

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this UserExtSupportAccounts.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this UserExtSupportAccounts.
        The URI of the corresponding Support Account resource to which the user belongs

        **Added In:** 2103141444

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this UserExtSupportAccounts.
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
