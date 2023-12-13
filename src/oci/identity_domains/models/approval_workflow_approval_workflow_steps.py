# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApprovalWorkflowApprovalWorkflowSteps(object):
    """
    ApprovalWorkflowSteps applicable for the ApprovalWorkflowInstance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApprovalWorkflowApprovalWorkflowSteps object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this ApprovalWorkflowApprovalWorkflowSteps.
        :type value: str

        :param ocid:
            The value to assign to the ocid property of this ApprovalWorkflowApprovalWorkflowSteps.
        :type ocid: str

        :param type:
            The value to assign to the type property of this ApprovalWorkflowApprovalWorkflowSteps.
        :type type: str

        :param order:
            The value to assign to the order property of this ApprovalWorkflowApprovalWorkflowSteps.
        :type order: int

        :param ref:
            The value to assign to the ref property of this ApprovalWorkflowApprovalWorkflowSteps.
        :type ref: str

        """
        self.swagger_types = {
            'value': 'str',
            'ocid': 'str',
            'type': 'str',
            'order': 'int',
            'ref': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ocid': 'ocid',
            'type': 'type',
            'order': 'order',
            'ref': '$ref'
        }

        self._value = None
        self._ocid = None
        self._type = None
        self._order = None
        self._ref = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this ApprovalWorkflowApprovalWorkflowSteps.
        The unique identifier of the ApprovalWorkflowStep.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this ApprovalWorkflowApprovalWorkflowSteps.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ApprovalWorkflowApprovalWorkflowSteps.
        The unique identifier of the ApprovalWorkflowStep.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this ApprovalWorkflowApprovalWorkflowSteps.
        :type: str
        """
        self._value = value

    @property
    def ocid(self):
        """
        Gets the ocid of this ApprovalWorkflowApprovalWorkflowSteps.
        The unique OCI identifier of the ApprovalWorkflowStep.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The ocid of this ApprovalWorkflowApprovalWorkflowSteps.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this ApprovalWorkflowApprovalWorkflowSteps.
        The unique OCI identifier of the ApprovalWorkflowStep.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param ocid: The ocid of this ApprovalWorkflowApprovalWorkflowSteps.
        :type: str
        """
        self._ocid = ocid

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ApprovalWorkflowApprovalWorkflowSteps.
        The type of the ApprovalWorkflowSteps.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The type of this ApprovalWorkflowApprovalWorkflowSteps.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ApprovalWorkflowApprovalWorkflowSteps.
        The type of the ApprovalWorkflowSteps.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this ApprovalWorkflowApprovalWorkflowSteps.
        :type: str
        """
        self._type = type

    @property
    def order(self):
        """
        Gets the order of this ApprovalWorkflowApprovalWorkflowSteps.
        The order of the ApprovalWorkflowSteps.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The order of this ApprovalWorkflowApprovalWorkflowSteps.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this ApprovalWorkflowApprovalWorkflowSteps.
        The order of the ApprovalWorkflowSteps.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: integer
         - uniqueness: none


        :param order: The order of this ApprovalWorkflowApprovalWorkflowSteps.
        :type: int
        """
        self._order = order

    @property
    def ref(self):
        """
        Gets the ref of this ApprovalWorkflowApprovalWorkflowSteps.
        ApprovalWorkflowSteps URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this ApprovalWorkflowApprovalWorkflowSteps.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this ApprovalWorkflowApprovalWorkflowSteps.
        ApprovalWorkflowSteps URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this ApprovalWorkflowApprovalWorkflowSteps.
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
