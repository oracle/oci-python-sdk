# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DynamicResourceGroupDynamicGroupAppRoles(object):
    """
    A list of appRoles that are currently granted to this Dynamic Resource Group.  The Identity service will assert these AppRoles for any resource that satisfies the matching-rule of this DynamicResourceGroup.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DynamicResourceGroupDynamicGroupAppRoles object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this DynamicResourceGroupDynamicGroupAppRoles.
        :type value: str

        :param ref:
            The value to assign to the ref property of this DynamicResourceGroupDynamicGroupAppRoles.
        :type ref: str

        :param display:
            The value to assign to the display property of this DynamicResourceGroupDynamicGroupAppRoles.
        :type display: str

        :param app_id:
            The value to assign to the app_id property of this DynamicResourceGroupDynamicGroupAppRoles.
        :type app_id: str

        :param app_name:
            The value to assign to the app_name property of this DynamicResourceGroupDynamicGroupAppRoles.
        :type app_name: str

        :param admin_role:
            The value to assign to the admin_role property of this DynamicResourceGroupDynamicGroupAppRoles.
        :type admin_role: bool

        :param legacy_group_name:
            The value to assign to the legacy_group_name property of this DynamicResourceGroupDynamicGroupAppRoles.
        :type legacy_group_name: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'display': 'str',
            'app_id': 'str',
            'app_name': 'str',
            'admin_role': 'bool',
            'legacy_group_name': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'display': 'display',
            'app_id': 'appId',
            'app_name': 'appName',
            'admin_role': 'adminRole',
            'legacy_group_name': 'legacyGroupName'
        }

        self._value = None
        self._ref = None
        self._display = None
        self._app_id = None
        self._app_name = None
        self._admin_role = None
        self._legacy_group_name = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this DynamicResourceGroupDynamicGroupAppRoles.
        The identifier of the appRole

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this DynamicResourceGroupDynamicGroupAppRoles.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this DynamicResourceGroupDynamicGroupAppRoles.
        The identifier of the appRole

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this DynamicResourceGroupDynamicGroupAppRoles.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this DynamicResourceGroupDynamicGroupAppRoles.
        The URI of the corresponding appRole resource to which the user belongs

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: reference
         - uniqueness: none


        :return: The ref of this DynamicResourceGroupDynamicGroupAppRoles.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this DynamicResourceGroupDynamicGroupAppRoles.
        The URI of the corresponding appRole resource to which the user belongs

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: reference
         - uniqueness: none


        :param ref: The ref of this DynamicResourceGroupDynamicGroupAppRoles.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this DynamicResourceGroupDynamicGroupAppRoles.
        A human readable name, primarily used for display purposes. READ-ONLY.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The display of this DynamicResourceGroupDynamicGroupAppRoles.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this DynamicResourceGroupDynamicGroupAppRoles.
        A human readable name, primarily used for display purposes. READ-ONLY.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param display: The display of this DynamicResourceGroupDynamicGroupAppRoles.
        :type: str
        """
        self._display = display

    @property
    def app_id(self):
        """
        Gets the app_id of this DynamicResourceGroupDynamicGroupAppRoles.
        ID of parent App. READ-ONLY.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The app_id of this DynamicResourceGroupDynamicGroupAppRoles.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """
        Sets the app_id of this DynamicResourceGroupDynamicGroupAppRoles.
        ID of parent App. READ-ONLY.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param app_id: The app_id of this DynamicResourceGroupDynamicGroupAppRoles.
        :type: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """
        Gets the app_name of this DynamicResourceGroupDynamicGroupAppRoles.
        Name of parent App. READ-ONLY.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The app_name of this DynamicResourceGroupDynamicGroupAppRoles.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """
        Sets the app_name of this DynamicResourceGroupDynamicGroupAppRoles.
        Name of parent App. READ-ONLY.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param app_name: The app_name of this DynamicResourceGroupDynamicGroupAppRoles.
        :type: str
        """
        self._app_name = app_name

    @property
    def admin_role(self):
        """
        Gets the admin_role of this DynamicResourceGroupDynamicGroupAppRoles.
        If true, then the role provides administrative access privileges. READ-ONLY.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The admin_role of this DynamicResourceGroupDynamicGroupAppRoles.
        :rtype: bool
        """
        return self._admin_role

    @admin_role.setter
    def admin_role(self, admin_role):
        """
        Sets the admin_role of this DynamicResourceGroupDynamicGroupAppRoles.
        If true, then the role provides administrative access privileges. READ-ONLY.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param admin_role: The admin_role of this DynamicResourceGroupDynamicGroupAppRoles.
        :type: bool
        """
        self._admin_role = admin_role

    @property
    def legacy_group_name(self):
        """
        Gets the legacy_group_name of this DynamicResourceGroupDynamicGroupAppRoles.
        The name of the legacy group associated with this AppRole.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The legacy_group_name of this DynamicResourceGroupDynamicGroupAppRoles.
        :rtype: str
        """
        return self._legacy_group_name

    @legacy_group_name.setter
    def legacy_group_name(self, legacy_group_name):
        """
        Sets the legacy_group_name of this DynamicResourceGroupDynamicGroupAppRoles.
        The name of the legacy group associated with this AppRole.

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param legacy_group_name: The legacy_group_name of this DynamicResourceGroupDynamicGroupAppRoles.
        :type: str
        """
        self._legacy_group_name = legacy_group_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
