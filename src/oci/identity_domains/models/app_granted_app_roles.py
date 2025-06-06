# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppGrantedAppRoles(object):
    """
    A list of AppRoles that are granted to this App (and that are defined by other Apps). Within the Oracle Public Cloud infrastructure, this allows AppID-based association. Such an association allows this App to act as a consumer and thus to access resources of another App that acts as a producer.
    """

    #: A constant which can be used with the type property of a AppGrantedAppRoles.
    #: This constant has a value of "direct"
    TYPE_DIRECT = "direct"

    #: A constant which can be used with the type property of a AppGrantedAppRoles.
    #: This constant has a value of "indirect"
    TYPE_INDIRECT = "indirect"

    def __init__(self, **kwargs):
        """
        Initializes a new AppGrantedAppRoles object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this AppGrantedAppRoles.
        :type value: str

        :param ref:
            The value to assign to the ref property of this AppGrantedAppRoles.
        :type ref: str

        :param type:
            The value to assign to the type property of this AppGrantedAppRoles.
            Allowed values for this property are: "direct", "indirect", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param display:
            The value to assign to the display property of this AppGrantedAppRoles.
        :type display: str

        :param app_id:
            The value to assign to the app_id property of this AppGrantedAppRoles.
        :type app_id: str

        :param app_name:
            The value to assign to the app_name property of this AppGrantedAppRoles.
        :type app_name: str

        :param admin_role:
            The value to assign to the admin_role property of this AppGrantedAppRoles.
        :type admin_role: bool

        :param legacy_group_name:
            The value to assign to the legacy_group_name property of this AppGrantedAppRoles.
        :type legacy_group_name: str

        :param read_only:
            The value to assign to the read_only property of this AppGrantedAppRoles.
        :type read_only: bool

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'type': 'str',
            'display': 'str',
            'app_id': 'str',
            'app_name': 'str',
            'admin_role': 'bool',
            'legacy_group_name': 'str',
            'read_only': 'bool'
        }
        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'type': 'type',
            'display': 'display',
            'app_id': 'appId',
            'app_name': 'appName',
            'admin_role': 'adminRole',
            'legacy_group_name': 'legacyGroupName',
            'read_only': 'readOnly'
        }
        self._value = None
        self._ref = None
        self._type = None
        self._display = None
        self._app_id = None
        self._app_name = None
        self._admin_role = None
        self._legacy_group_name = None
        self._read_only = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this AppGrantedAppRoles.
        The id of an AppRole that is granted to this App.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this AppGrantedAppRoles.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AppGrantedAppRoles.
        The id of an AppRole that is granted to this App.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this AppGrantedAppRoles.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this AppGrantedAppRoles.
        The URI of an AppRole that is granted to this App.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this AppGrantedAppRoles.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this AppGrantedAppRoles.
        The URI of an AppRole that is granted to this App.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this AppGrantedAppRoles.
        :type: str
        """
        self._ref = ref

    @property
    def type(self):
        """
        Gets the type of this AppGrantedAppRoles.
        A label that indicates whether this AppRole was granted directly to the App (or indirectly through a Group). For an App, the value of this attribute will always be 'direct' (because an App cannot be a member of a Group).

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "direct", "indirect", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AppGrantedAppRoles.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AppGrantedAppRoles.
        A label that indicates whether this AppRole was granted directly to the App (or indirectly through a Group). For an App, the value of this attribute will always be 'direct' (because an App cannot be a member of a Group).

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this AppGrantedAppRoles.
        :type: str
        """
        allowed_values = ["direct", "indirect"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def display(self):
        """
        Gets the display of this AppGrantedAppRoles.
        The display-name of an AppRole that is granted to this App.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this AppGrantedAppRoles.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this AppGrantedAppRoles.
        The display-name of an AppRole that is granted to this App.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this AppGrantedAppRoles.
        :type: str
        """
        self._display = display

    @property
    def app_id(self):
        """
        Gets the app_id of this AppGrantedAppRoles.
        The id of the App that defines this AppRole, which is granted to this App. The App that defines the AppRole acts as the producer; the App to which the AppRole is granted acts as a consumer.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The app_id of this AppGrantedAppRoles.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """
        Sets the app_id of this AppGrantedAppRoles.
        The id of the App that defines this AppRole, which is granted to this App. The App that defines the AppRole acts as the producer; the App to which the AppRole is granted acts as a consumer.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param app_id: The app_id of this AppGrantedAppRoles.
        :type: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """
        Gets the app_name of this AppGrantedAppRoles.
        The name of the App that defines this AppRole, which is granted to this App. The App that defines the AppRole acts as the producer; the App to which the AppRole is granted acts as a consumer.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The app_name of this AppGrantedAppRoles.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """
        Sets the app_name of this AppGrantedAppRoles.
        The name of the App that defines this AppRole, which is granted to this App. The App that defines the AppRole acts as the producer; the App to which the AppRole is granted acts as a consumer.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param app_name: The app_name of this AppGrantedAppRoles.
        :type: str
        """
        self._app_name = app_name

    @property
    def admin_role(self):
        """
        Gets the admin_role of this AppGrantedAppRoles.
        If true, then this granted AppRole confers administrative privileges within the App that defines it. Otherwise, the granted AppRole confers only functional privileges.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The admin_role of this AppGrantedAppRoles.
        :rtype: bool
        """
        return self._admin_role

    @admin_role.setter
    def admin_role(self, admin_role):
        """
        Sets the admin_role of this AppGrantedAppRoles.
        If true, then this granted AppRole confers administrative privileges within the App that defines it. Otherwise, the granted AppRole confers only functional privileges.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param admin_role: The admin_role of this AppGrantedAppRoles.
        :type: bool
        """
        self._admin_role = admin_role

    @property
    def legacy_group_name(self):
        """
        Gets the legacy_group_name of this AppGrantedAppRoles.
        The name of the legacy group associated with this AppRole.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The legacy_group_name of this AppGrantedAppRoles.
        :rtype: str
        """
        return self._legacy_group_name

    @legacy_group_name.setter
    def legacy_group_name(self, legacy_group_name):
        """
        Sets the legacy_group_name of this AppGrantedAppRoles.
        The name of the legacy group associated with this AppRole.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param legacy_group_name: The legacy_group_name of this AppGrantedAppRoles.
        :type: str
        """
        self._legacy_group_name = legacy_group_name

    @property
    def read_only(self):
        """
        Gets the read_only of this AppGrantedAppRoles.
        If true, indicates that this value must be protected.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The read_only of this AppGrantedAppRoles.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this AppGrantedAppRoles.
        If true, indicates that this value must be protected.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param read_only: The read_only of this AppGrantedAppRoles.
        :type: bool
        """
        self._read_only = read_only

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
