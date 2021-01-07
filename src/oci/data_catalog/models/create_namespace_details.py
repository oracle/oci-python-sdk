# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNamespaceDetails(object):
    """
    Properties used in custom property create operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNamespaceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateNamespaceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateNamespaceDetails.
        :type description: str

        :param is_service_defined:
            The value to assign to the is_service_defined property of this CreateNamespaceDetails.
        :type is_service_defined: bool

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'is_service_defined': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'is_service_defined': 'isServiceDefined'
        }

        self._display_name = None
        self._description = None
        self._is_service_defined = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateNamespaceDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateNamespaceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateNamespaceDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateNamespaceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateNamespaceDetails.
        Detailed description of the Namespace.


        :return: The description of this CreateNamespaceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateNamespaceDetails.
        Detailed description of the Namespace.


        :param description: The description of this CreateNamespaceDetails.
        :type: str
        """
        self._description = description

    @property
    def is_service_defined(self):
        """
        Gets the is_service_defined of this CreateNamespaceDetails.
        If this field is defined by service or by a user


        :return: The is_service_defined of this CreateNamespaceDetails.
        :rtype: bool
        """
        return self._is_service_defined

    @is_service_defined.setter
    def is_service_defined(self, is_service_defined):
        """
        Sets the is_service_defined of this CreateNamespaceDetails.
        If this field is defined by service or by a user


        :param is_service_defined: The is_service_defined of this CreateNamespaceDetails.
        :type: bool
        """
        self._is_service_defined = is_service_defined

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
