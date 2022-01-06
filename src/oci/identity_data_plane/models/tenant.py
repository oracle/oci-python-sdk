# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Tenant(object):
    """
    Tenant model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Tenant object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Tenant.
        :type id: str

        :param name:
            The value to assign to the name property of this Tenant.
        :type name: str

        :param service_namespace:
            The value to assign to the service_namespace property of this Tenant.
        :type service_namespace: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'service_namespace': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'service_namespace': 'serviceNamespace'
        }

        self._id = None
        self._name = None
        self._service_namespace = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Tenant.
        The tenant's Oracle ID (OCID).


        :return: The id of this Tenant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Tenant.
        The tenant's Oracle ID (OCID).


        :param id: The id of this Tenant.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Tenant.
        The name of the tenancy.


        :return: The name of this Tenant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Tenant.
        The name of the tenancy.


        :param name: The name of this Tenant.
        :type: str
        """
        self._name = name

    @property
    def service_namespace(self):
        """
        Gets the service_namespace of this Tenant.
        The service namespace.


        :return: The service_namespace of this Tenant.
        :rtype: str
        """
        return self._service_namespace

    @service_namespace.setter
    def service_namespace(self, service_namespace):
        """
        Sets the service_namespace of this Tenant.
        The service namespace.


        :param service_namespace: The service_namespace of this Tenant.
        :type: str
        """
        self._service_namespace = service_namespace

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
