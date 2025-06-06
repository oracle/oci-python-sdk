# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IdentityPropagationTrustImpersonationServiceUsers(object):
    """
    The Impersonating Principal.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IdentityPropagationTrustImpersonationServiceUsers object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this IdentityPropagationTrustImpersonationServiceUsers.
        :type value: str

        :param ocid:
            The value to assign to the ocid property of this IdentityPropagationTrustImpersonationServiceUsers.
        :type ocid: str

        :param ref:
            The value to assign to the ref property of this IdentityPropagationTrustImpersonationServiceUsers.
        :type ref: str

        :param rule:
            The value to assign to the rule property of this IdentityPropagationTrustImpersonationServiceUsers.
        :type rule: str

        """
        self.swagger_types = {
            'value': 'str',
            'ocid': 'str',
            'ref': 'str',
            'rule': 'str'
        }
        self.attribute_map = {
            'value': 'value',
            'ocid': 'ocid',
            'ref': '$ref',
            'rule': 'rule'
        }
        self._value = None
        self._ocid = None
        self._ref = None
        self._rule = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this IdentityPropagationTrustImpersonationServiceUsers.
        The ID of the Service User.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this IdentityPropagationTrustImpersonationServiceUsers.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this IdentityPropagationTrustImpersonationServiceUsers.
        The ID of the Service User.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this IdentityPropagationTrustImpersonationServiceUsers.
        :type: str
        """
        self._value = value

    @property
    def ocid(self):
        """
        Gets the ocid of this IdentityPropagationTrustImpersonationServiceUsers.
        The OCID of the Service User.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The ocid of this IdentityPropagationTrustImpersonationServiceUsers.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this IdentityPropagationTrustImpersonationServiceUsers.
        The OCID of the Service User.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param ocid: The ocid of this IdentityPropagationTrustImpersonationServiceUsers.
        :type: str
        """
        self._ocid = ocid

    @property
    def ref(self):
        """
        Gets the ref of this IdentityPropagationTrustImpersonationServiceUsers.
        The URI that corresponds to the Service User.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this IdentityPropagationTrustImpersonationServiceUsers.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this IdentityPropagationTrustImpersonationServiceUsers.
        The URI that corresponds to the Service User.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this IdentityPropagationTrustImpersonationServiceUsers.
        :type: str
        """
        self._ref = ref

    @property
    def rule(self):
        """
        **[Required]** Gets the rule of this IdentityPropagationTrustImpersonationServiceUsers.
        The rule expression to be used for matching the inbound token for impersonation.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The rule of this IdentityPropagationTrustImpersonationServiceUsers.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """
        Sets the rule of this IdentityPropagationTrustImpersonationServiceUsers.
        The rule expression to be used for matching the inbound token for impersonation.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param rule: The rule of this IdentityPropagationTrustImpersonationServiceUsers.
        :type: str
        """
        self._rule = rule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
