# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserExtTrustedUserAgents(object):
    """
    A list of trusted User Agents owned by this user. Multi-Factored Authentication uses Trusted User Agents to authenticate users.  A User Agent is software application that a user uses to issue requests. For example, a User Agent could be a particular browser (possibly one of several executing on a desktop or laptop) or a particular mobile application (again, oneof several executing on a particular mobile device). A User Agent is trusted once the Multi-Factor Authentication has verified it in some way.

    **Added In:** 18.3.6

    **SCIM++ Properties:**
    - idcsCompositeKey: [value]
    - multiValued: true
    - mutability: readWrite
    - required: false
    - returned: request
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UserExtTrustedUserAgents object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this UserExtTrustedUserAgents.
        :type value: str

        :param ref:
            The value to assign to the ref property of this UserExtTrustedUserAgents.
        :type ref: str

        :param display:
            The value to assign to the display property of this UserExtTrustedUserAgents.
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
        **[Required]** Gets the value of this UserExtTrustedUserAgents.
        The identifier of the User's trusted user agent.

        **Added In:** 18.3.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this UserExtTrustedUserAgents.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserExtTrustedUserAgents.
        The identifier of the User's trusted user agent.

        **Added In:** 18.3.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this UserExtTrustedUserAgents.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this UserExtTrustedUserAgents.
        The URI of the corresponding trusted user agent resource.

        **Added In:** 18.3.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this UserExtTrustedUserAgents.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this UserExtTrustedUserAgents.
        The URI of the corresponding trusted user agent resource.

        **Added In:** 18.3.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this UserExtTrustedUserAgents.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this UserExtTrustedUserAgents.
        A human-readable identifier for this trusted user agent, used primarily for display purposes. READ-ONLY.

        **Added In:** 18.3.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this UserExtTrustedUserAgents.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this UserExtTrustedUserAgents.
        A human-readable identifier for this trusted user agent, used primarily for display purposes. READ-ONLY.

        **Added In:** 18.3.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this UserExtTrustedUserAgents.
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
