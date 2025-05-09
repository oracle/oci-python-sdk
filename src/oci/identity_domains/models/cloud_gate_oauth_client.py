# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudGateOauthClient(object):
    """
    A reference to the OAuth client App used by this Cloud Gate instance.

    **SCIM++ Properties:**
    - caseExact: false
    - idcsSearchable: true
    - multiValued: false
    - mutability: readOnly
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CloudGateOauthClient object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this CloudGateOauthClient.
        :type value: str

        :param ref:
            The value to assign to the ref property of this CloudGateOauthClient.
        :type ref: str

        :param client_id:
            The value to assign to the client_id property of this CloudGateOauthClient.
        :type client_id: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'client_id': 'str'
        }
        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'client_id': 'clientId'
        }
        self._value = None
        self._ref = None
        self._client_id = None

    @property
    def value(self):
        """
        Gets the value of this CloudGateOauthClient.
        The id of the OAuth app for this CloudGate.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this CloudGateOauthClient.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CloudGateOauthClient.
        The id of the OAuth app for this CloudGate.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this CloudGateOauthClient.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this CloudGateOauthClient.
        The URI of the OAuth app for this CloudGate.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this CloudGateOauthClient.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this CloudGateOauthClient.
        The URI of the OAuth app for this CloudGate.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this CloudGateOauthClient.
        :type: str
        """
        self._ref = ref

    @property
    def client_id(self):
        """
        Gets the client_id of this CloudGateOauthClient.
        The Client ID of the OAuth app for this CloudGate.

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The client_id of this CloudGateOauthClient.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this CloudGateOauthClient.
        The Client ID of the OAuth app for this CloudGate.

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param client_id: The client_id of this CloudGateOauthClient.
        :type: str
        """
        self._client_id = client_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
