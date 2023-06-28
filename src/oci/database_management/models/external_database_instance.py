# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalDatabaseInstance(object):
    """
    The details of an external database instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalDatabaseInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_number:
            The value to assign to the instance_number property of this ExternalDatabaseInstance.
        :type instance_number: int

        :param instance_name:
            The value to assign to the instance_name property of this ExternalDatabaseInstance.
        :type instance_name: str

        :param host_name:
            The value to assign to the host_name property of this ExternalDatabaseInstance.
        :type host_name: str

        """
        self.swagger_types = {
            'instance_number': 'int',
            'instance_name': 'str',
            'host_name': 'str'
        }

        self.attribute_map = {
            'instance_number': 'instanceNumber',
            'instance_name': 'instanceName',
            'host_name': 'hostName'
        }

        self._instance_number = None
        self._instance_name = None
        self._host_name = None

    @property
    def instance_number(self):
        """
        **[Required]** Gets the instance_number of this ExternalDatabaseInstance.
        The instance number of the database instance.


        :return: The instance_number of this ExternalDatabaseInstance.
        :rtype: int
        """
        return self._instance_number

    @instance_number.setter
    def instance_number(self, instance_number):
        """
        Sets the instance_number of this ExternalDatabaseInstance.
        The instance number of the database instance.


        :param instance_number: The instance_number of this ExternalDatabaseInstance.
        :type: int
        """
        self._instance_number = instance_number

    @property
    def instance_name(self):
        """
        **[Required]** Gets the instance_name of this ExternalDatabaseInstance.
        The name of the database instance.


        :return: The instance_name of this ExternalDatabaseInstance.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """
        Sets the instance_name of this ExternalDatabaseInstance.
        The name of the database instance.


        :param instance_name: The instance_name of this ExternalDatabaseInstance.
        :type: str
        """
        self._instance_name = instance_name

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this ExternalDatabaseInstance.
        The name of the host machine.


        :return: The host_name of this ExternalDatabaseInstance.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this ExternalDatabaseInstance.
        The name of the host machine.


        :param host_name: The host_name of this ExternalDatabaseInstance.
        :type: str
        """
        self._host_name = host_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
