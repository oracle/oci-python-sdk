# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Namespace(object):
    """
    This is the namespace details of a tenancy in Logan Analytics application
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Namespace object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace_name:
            The value to assign to the namespace_name property of this Namespace.
        :type namespace_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Namespace.
        :type compartment_id: str

        :param is_onboarded:
            The value to assign to the is_onboarded property of this Namespace.
        :type is_onboarded: bool

        """
        self.swagger_types = {
            'namespace_name': 'str',
            'compartment_id': 'str',
            'is_onboarded': 'bool'
        }

        self.attribute_map = {
            'namespace_name': 'namespaceName',
            'compartment_id': 'compartmentId',
            'is_onboarded': 'isOnboarded'
        }

        self._namespace_name = None
        self._compartment_id = None
        self._is_onboarded = None

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this Namespace.
        This is the namespace name of a tenancy


        :return: The namespace_name of this Namespace.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this Namespace.
        This is the namespace name of a tenancy


        :param namespace_name: The namespace_name of this Namespace.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Namespace.
        The is the tenancy ID


        :return: The compartment_id of this Namespace.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Namespace.
        The is the tenancy ID


        :param compartment_id: The compartment_id of this Namespace.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_onboarded(self):
        """
        **[Required]** Gets the is_onboarded of this Namespace.
        This indicates if the tenancy is onboarded to Logging Analytics


        :return: The is_onboarded of this Namespace.
        :rtype: bool
        """
        return self._is_onboarded

    @is_onboarded.setter
    def is_onboarded(self, is_onboarded):
        """
        Sets the is_onboarded of this Namespace.
        This indicates if the tenancy is onboarded to Logging Analytics


        :param is_onboarded: The is_onboarded of this Namespace.
        :type: bool
        """
        self._is_onboarded = is_onboarded

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
