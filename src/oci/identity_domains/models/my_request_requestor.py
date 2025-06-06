# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MyRequestRequestor(object):
    """
    Requesting User

    **SCIM++ Properties:**
    - idcsSearchable: true
    - multiValued: false
    - mutability: immutable
    - required: false
    - returned: request
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MyRequestRequestor object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this MyRequestRequestor.
        :type value: str

        :param ref:
            The value to assign to the ref property of this MyRequestRequestor.
        :type ref: str

        :param display:
            The value to assign to the display property of this MyRequestRequestor.
        :type display: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'display': 'str'
        }
        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'display': 'display'
        }
        self._value = None
        self._ref = None
        self._display = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this MyRequestRequestor.
        User identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsCsvAttributeName: requestor_id
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this MyRequestRequestor.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this MyRequestRequestor.
        User identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsCsvAttributeName: requestor_id
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this MyRequestRequestor.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this MyRequestRequestor.
        User URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this MyRequestRequestor.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this MyRequestRequestor.
        User URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this MyRequestRequestor.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this MyRequestRequestor.
        User display name

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this MyRequestRequestor.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this MyRequestRequestor.
        User display name

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this MyRequestRequestor.
        :type: str
        """
        self._display = display

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
