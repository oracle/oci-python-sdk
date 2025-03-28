# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppAccounts(object):
    """
    Accounts of App
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppAccounts object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this AppAccounts.
        :type value: str

        :param ref:
            The value to assign to the ref property of this AppAccounts.
        :type ref: str

        :param owner_id:
            The value to assign to the owner_id property of this AppAccounts.
        :type owner_id: str

        :param name:
            The value to assign to the name property of this AppAccounts.
        :type name: str

        :param active:
            The value to assign to the active property of this AppAccounts.
        :type active: bool

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'owner_id': 'str',
            'name': 'str',
            'active': 'bool'
        }
        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'owner_id': 'ownerId',
            'name': 'name',
            'active': 'active'
        }
        self._value = None
        self._ref = None
        self._owner_id = None
        self._name = None
        self._active = None

    @property
    def value(self):
        """
        Gets the value of this AppAccounts.
        Account identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this AppAccounts.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AppAccounts.
        Account identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this AppAccounts.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this AppAccounts.
        AccountMgmtInfo URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this AppAccounts.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this AppAccounts.
        AccountMgmtInfo URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this AppAccounts.
        :type: str
        """
        self._ref = ref

    @property
    def owner_id(self):
        """
        Gets the owner_id of this AppAccounts.
        Owner identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The owner_id of this AppAccounts.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this AppAccounts.
        Owner identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param owner_id: The owner_id of this AppAccounts.
        :type: str
        """
        self._owner_id = owner_id

    @property
    def name(self):
        """
        Gets the name of this AppAccounts.
        Name of the account

        **Added In:** 17.4.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The name of this AppAccounts.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AppAccounts.
        Name of the account

        **Added In:** 17.4.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param name: The name of this AppAccounts.
        :type: str
        """
        self._name = name

    @property
    def active(self):
        """
        Gets the active of this AppAccounts.
        Status of the account

        **Added In:** 17.4.6

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The active of this AppAccounts.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this AppAccounts.
        Status of the account

        **Added In:** 17.4.6

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param active: The active of this AppAccounts.
        :type: bool
        """
        self._active = active

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
