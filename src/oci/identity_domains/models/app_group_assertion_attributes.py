# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppGroupAssertionAttributes(object):
    """
    Each value of this attribute describes an attribute of Group that will be sent in a Security Assertion Markup Language (SAML) assertion.

    **Deprecated Since: 18.2.2**

    **SCIM++ Properties:**
    - caseExact: false
    - idcsCompositeKey: [name]
    - idcsSearchable: false
    - idcsValuePersistedInOtherAttribute: true
    - multiValued: true
    - mutability: readWrite
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppGroupAssertionAttributes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AppGroupAssertionAttributes.
        :type name: str

        :param format:
            The value to assign to the format property of this AppGroupAssertionAttributes.
        :type format: str

        :param condition:
            The value to assign to the condition property of this AppGroupAssertionAttributes.
        :type condition: str

        :param group_name:
            The value to assign to the group_name property of this AppGroupAssertionAttributes.
        :type group_name: str

        """
        self.swagger_types = {
            'name': 'str',
            'format': 'str',
            'condition': 'str',
            'group_name': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'format': 'format',
            'condition': 'condition',
            'group_name': 'groupName'
        }

        self._name = None
        self._format = None
        self._condition = None
        self._group_name = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AppGroupAssertionAttributes.
        The attribute represents the name of the attribute that will be used in the Security Assertion Markup Language (SAML) assertion

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The name of this AppGroupAssertionAttributes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AppGroupAssertionAttributes.
        The attribute represents the name of the attribute that will be used in the Security Assertion Markup Language (SAML) assertion

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param name: The name of this AppGroupAssertionAttributes.
        :type: str
        """
        self._name = name

    @property
    def format(self):
        """
        Gets the format of this AppGroupAssertionAttributes.
        Indicates the format of the assertion attribute.

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The format of this AppGroupAssertionAttributes.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this AppGroupAssertionAttributes.
        Indicates the format of the assertion attribute.

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param format: The format of this AppGroupAssertionAttributes.
        :type: str
        """
        self._format = format

    @property
    def condition(self):
        """
        Gets the condition of this AppGroupAssertionAttributes.
        Indicates the filter types that are supported for the Group assertion attributes.

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The condition of this AppGroupAssertionAttributes.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this AppGroupAssertionAttributes.
        Indicates the filter types that are supported for the Group assertion attributes.

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param condition: The condition of this AppGroupAssertionAttributes.
        :type: str
        """
        self._condition = condition

    @property
    def group_name(self):
        """
        Gets the group_name of this AppGroupAssertionAttributes.
        Indicates the group name that are supported for the group assertion attributes.

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The group_name of this AppGroupAssertionAttributes.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this AppGroupAssertionAttributes.
        Indicates the group name that are supported for the group assertion attributes.

        **Deprecated Since: 18.2.2**

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsValuePersistedInOtherAttribute: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param group_name: The group_name of this AppGroupAssertionAttributes.
        :type: str
        """
        self._group_name = group_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
