# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GlossaryPermissionsSummary(object):
    """
    Permissions object for glosssaries.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GlossaryPermissionsSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param glossary_key:
            The value to assign to the glossary_key property of this GlossaryPermissionsSummary.
        :type glossary_key: str

        :param user_permissions:
            The value to assign to the user_permissions property of this GlossaryPermissionsSummary.
        :type user_permissions: list[str]

        """
        self.swagger_types = {
            'glossary_key': 'str',
            'user_permissions': 'list[str]'
        }

        self.attribute_map = {
            'glossary_key': 'glossaryKey',
            'user_permissions': 'userPermissions'
        }

        self._glossary_key = None
        self._user_permissions = None

    @property
    def glossary_key(self):
        """
        Gets the glossary_key of this GlossaryPermissionsSummary.
        The unique key of the parent glossary.


        :return: The glossary_key of this GlossaryPermissionsSummary.
        :rtype: str
        """
        return self._glossary_key

    @glossary_key.setter
    def glossary_key(self, glossary_key):
        """
        Sets the glossary_key of this GlossaryPermissionsSummary.
        The unique key of the parent glossary.


        :param glossary_key: The glossary_key of this GlossaryPermissionsSummary.
        :type: str
        """
        self._glossary_key = glossary_key

    @property
    def user_permissions(self):
        """
        Gets the user_permissions of this GlossaryPermissionsSummary.
        An array of permissions.


        :return: The user_permissions of this GlossaryPermissionsSummary.
        :rtype: list[str]
        """
        return self._user_permissions

    @user_permissions.setter
    def user_permissions(self, user_permissions):
        """
        Sets the user_permissions of this GlossaryPermissionsSummary.
        An array of permissions.


        :param user_permissions: The user_permissions of this GlossaryPermissionsSummary.
        :type: list[str]
        """
        self._user_permissions = user_permissions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
