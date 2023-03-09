# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MeGroups(object):
    """
    A list of groups that the user belongs to, either thorough direct membership, nested groups, or dynamically calculated
    """

    #: A constant which can be used with the type property of a MeGroups.
    #: This constant has a value of "direct"
    TYPE_DIRECT = "direct"

    #: A constant which can be used with the type property of a MeGroups.
    #: This constant has a value of "indirect"
    TYPE_INDIRECT = "indirect"

    def __init__(self, **kwargs):
        """
        Initializes a new MeGroups object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this MeGroups.
        :type value: str

        :param ocid:
            The value to assign to the ocid property of this MeGroups.
        :type ocid: str

        :param ref:
            The value to assign to the ref property of this MeGroups.
        :type ref: str

        :param display:
            The value to assign to the display property of this MeGroups.
        :type display: str

        :param non_unique_display:
            The value to assign to the non_unique_display property of this MeGroups.
        :type non_unique_display: str

        :param external_id:
            The value to assign to the external_id property of this MeGroups.
        :type external_id: str

        :param type:
            The value to assign to the type property of this MeGroups.
            Allowed values for this property are: "direct", "indirect", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param membership_ocid:
            The value to assign to the membership_ocid property of this MeGroups.
        :type membership_ocid: str

        :param date_added:
            The value to assign to the date_added property of this MeGroups.
        :type date_added: str

        """
        self.swagger_types = {
            'value': 'str',
            'ocid': 'str',
            'ref': 'str',
            'display': 'str',
            'non_unique_display': 'str',
            'external_id': 'str',
            'type': 'str',
            'membership_ocid': 'str',
            'date_added': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ocid': 'ocid',
            'ref': '$ref',
            'display': 'display',
            'non_unique_display': 'nonUniqueDisplay',
            'external_id': 'externalId',
            'type': 'type',
            'membership_ocid': 'membershipOcid',
            'date_added': 'dateAdded'
        }

        self._value = None
        self._ocid = None
        self._ref = None
        self._display = None
        self._non_unique_display = None
        self._external_id = None
        self._type = None
        self._membership_ocid = None
        self._date_added = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this MeGroups.
        The identifier of the User's group.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this MeGroups.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this MeGroups.
        The identifier of the User's group.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this MeGroups.
        :type: str
        """
        self._value = value

    @property
    def ocid(self):
        """
        Gets the ocid of this MeGroups.
        Ocid of the User's group.

        **Added In:** 2102181953

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The ocid of this MeGroups.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this MeGroups.
        Ocid of the User's group.

        **Added In:** 2102181953

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param ocid: The ocid of this MeGroups.
        :type: str
        """
        self._ocid = ocid

    @property
    def ref(self):
        """
        Gets the ref of this MeGroups.
        The URI of the corresponding Group resource to which the user belongs

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this MeGroups.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this MeGroups.
        The URI of the corresponding Group resource to which the user belongs

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this MeGroups.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this MeGroups.
        A human readable name, primarily used for display purposes. READ-ONLY.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this MeGroups.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this MeGroups.
        A human readable name, primarily used for display purposes. READ-ONLY.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this MeGroups.
        :type: str
        """
        self._display = display

    @property
    def non_unique_display(self):
        """
        Gets the non_unique_display of this MeGroups.
        A human readable name for Group as defined by the Service Consumer. READ-ONLY.

        **Added In:** 2011192329

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The non_unique_display of this MeGroups.
        :rtype: str
        """
        return self._non_unique_display

    @non_unique_display.setter
    def non_unique_display(self, non_unique_display):
        """
        Sets the non_unique_display of this MeGroups.
        A human readable name for Group as defined by the Service Consumer. READ-ONLY.

        **Added In:** 2011192329

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param non_unique_display: The non_unique_display of this MeGroups.
        :type: str
        """
        self._non_unique_display = non_unique_display

    @property
    def external_id(self):
        """
        Gets the external_id of this MeGroups.
        An identifier for the Resource as defined by the Service Consumer. READ-ONLY.

        **Added In:** 2011192329

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The external_id of this MeGroups.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this MeGroups.
        An identifier for the Resource as defined by the Service Consumer. READ-ONLY.

        **Added In:** 2011192329

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param external_id: The external_id of this MeGroups.
        :type: str
        """
        self._external_id = external_id

    @property
    def type(self):
        """
        Gets the type of this MeGroups.
        A label indicating the attribute's function; e.g., 'direct' or 'indirect'.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none

        Allowed values for this property are: "direct", "indirect", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this MeGroups.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MeGroups.
        A label indicating the attribute's function; e.g., 'direct' or 'indirect'.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param type: The type of this MeGroups.
        :type: str
        """
        allowed_values = ["direct", "indirect"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def membership_ocid(self):
        """
        Gets the membership_ocid of this MeGroups.
        Membership Ocid

        **Added In:** 2103141444

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The membership_ocid of this MeGroups.
        :rtype: str
        """
        return self._membership_ocid

    @membership_ocid.setter
    def membership_ocid(self, membership_ocid):
        """
        Sets the membership_ocid of this MeGroups.
        Membership Ocid

        **Added In:** 2103141444

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param membership_ocid: The membership_ocid of this MeGroups.
        :type: str
        """
        self._membership_ocid = membership_ocid

    @property
    def date_added(self):
        """
        Gets the date_added of this MeGroups.
        Date when the member is Added to the group

        **Added In:** 2105200541

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :return: The date_added of this MeGroups.
        :rtype: str
        """
        return self._date_added

    @date_added.setter
    def date_added(self, date_added):
        """
        Sets the date_added of this MeGroups.
        Date when the member is Added to the group

        **Added In:** 2105200541

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :param date_added: The date_added of this MeGroups.
        :type: str
        """
        self._date_added = date_added

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
