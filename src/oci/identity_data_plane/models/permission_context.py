# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PermissionContext(object):
    """
    PermissionContext model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PermissionContext object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param permission:
            The value to assign to the permission property of this PermissionContext.
        :type permission: oci.identity_data_plane.models.Permission

        :param variables:
            The value to assign to the variables property of this PermissionContext.
        :type variables: list[oci.identity_data_plane.models.ContextVariable]

        """
        self.swagger_types = {
            'permission': 'Permission',
            'variables': 'list[ContextVariable]'
        }

        self.attribute_map = {
            'permission': 'permission',
            'variables': 'variables'
        }

        self._permission = None
        self._variables = None

    @property
    def permission(self):
        """
        **[Required]** Gets the permission of this PermissionContext.
        The permission context.


        :return: The permission of this PermissionContext.
        :rtype: oci.identity_data_plane.models.Permission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """
        Sets the permission of this PermissionContext.
        The permission context.


        :param permission: The permission of this PermissionContext.
        :type: oci.identity_data_plane.models.Permission
        """
        self._permission = permission

    @property
    def variables(self):
        """
        **[Required]** Gets the variables of this PermissionContext.
        The set of variables in this permission context.


        :return: The variables of this PermissionContext.
        :rtype: list[oci.identity_data_plane.models.ContextVariable]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this PermissionContext.
        The set of variables in this permission context.


        :param variables: The variables of this PermissionContext.
        :type: list[oci.identity_data_plane.models.ContextVariable]
        """
        self._variables = variables

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
