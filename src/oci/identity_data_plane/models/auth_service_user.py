# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthServiceUser(object):
    """
    AuthServiceUser model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AuthServiceUser object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this AuthServiceUser.
        :type compartment_id: str

        :param tenant_id:
            The value to assign to the tenant_id property of this AuthServiceUser.
        :type tenant_id: str

        :param id:
            The value to assign to the id property of this AuthServiceUser.
        :type id: str

        :param name:
            The value to assign to the name property of this AuthServiceUser.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this AuthServiceUser.
        :type display_name: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'tenant_id': 'str',
            'id': 'str',
            'name': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'tenant_id': 'tenantId',
            'id': 'id',
            'name': 'name',
            'display_name': 'displayName'
        }

        self._compartment_id = None
        self._tenant_id = None
        self._id = None
        self._name = None
        self._display_name = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AuthServiceUser.
        The id of the compartment.


        :return: The compartment_id of this AuthServiceUser.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AuthServiceUser.
        The id of the compartment.


        :param compartment_id: The compartment_id of this AuthServiceUser.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this AuthServiceUser.
        The id of the tenant.


        :return: The tenant_id of this AuthServiceUser.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this AuthServiceUser.
        The id of the tenant.


        :param tenant_id: The tenant_id of this AuthServiceUser.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AuthServiceUser.
        The user's Oracle ID (OCID).


        :return: The id of this AuthServiceUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuthServiceUser.
        The user's Oracle ID (OCID).


        :param id: The id of this AuthServiceUser.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AuthServiceUser.
        The name of the user.


        :return: The name of this AuthServiceUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AuthServiceUser.
        The name of the user.


        :param name: The name of this AuthServiceUser.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AuthServiceUser.
        The display name of the user.


        :return: The display_name of this AuthServiceUser.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AuthServiceUser.
        The display name of the user.


        :param display_name: The display_name of this AuthServiceUser.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
