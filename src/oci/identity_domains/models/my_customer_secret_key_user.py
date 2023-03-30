# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MyCustomerSecretKeyUser(object):
    """
    User linked to customer secret key

    **SCIM++ Properties:**
    - caseExact: false
    - idcsSearchable: true
    - multiValued: false
    - mutability: immutable
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MyCustomerSecretKeyUser object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this MyCustomerSecretKeyUser.
        :type value: str

        :param ocid:
            The value to assign to the ocid property of this MyCustomerSecretKeyUser.
        :type ocid: str

        :param ref:
            The value to assign to the ref property of this MyCustomerSecretKeyUser.
        :type ref: str

        :param display:
            The value to assign to the display property of this MyCustomerSecretKeyUser.
        :type display: str

        :param name:
            The value to assign to the name property of this MyCustomerSecretKeyUser.
        :type name: str

        """
        self.swagger_types = {
            'value': 'str',
            'ocid': 'str',
            'ref': 'str',
            'display': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ocid': 'ocid',
            'ref': '$ref',
            'display': 'display',
            'name': 'name'
        }

        self._value = None
        self._ocid = None
        self._ref = None
        self._display = None
        self._name = None

    @property
    def value(self):
        """
        Gets the value of this MyCustomerSecretKeyUser.
        User's id

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this MyCustomerSecretKeyUser.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this MyCustomerSecretKeyUser.
        User's id

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this MyCustomerSecretKeyUser.
        :type: str
        """
        self._value = value

    @property
    def ocid(self):
        """
        Gets the ocid of this MyCustomerSecretKeyUser.
        User's ocid

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The ocid of this MyCustomerSecretKeyUser.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this MyCustomerSecretKeyUser.
        User's ocid

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param ocid: The ocid of this MyCustomerSecretKeyUser.
        :type: str
        """
        self._ocid = ocid

    @property
    def ref(self):
        """
        Gets the ref of this MyCustomerSecretKeyUser.
        The URI that corresponds to the user linked to this credential

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this MyCustomerSecretKeyUser.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this MyCustomerSecretKeyUser.
        The URI that corresponds to the user linked to this credential

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this MyCustomerSecretKeyUser.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this MyCustomerSecretKeyUser.
        User display name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this MyCustomerSecretKeyUser.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this MyCustomerSecretKeyUser.
        User display name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this MyCustomerSecretKeyUser.
        :type: str
        """
        self._display = display

    @property
    def name(self):
        """
        Gets the name of this MyCustomerSecretKeyUser.
        User name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The name of this MyCustomerSecretKeyUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MyCustomerSecretKeyUser.
        User name

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param name: The name of this MyCustomerSecretKeyUser.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other