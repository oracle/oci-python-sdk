# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostInstanceMap(object):
    """
    Object containing hostname and instance name mapping.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostInstanceMap object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host_name:
            The value to assign to the host_name property of this HostInstanceMap.
        :type host_name: str

        :param instance_name:
            The value to assign to the instance_name property of this HostInstanceMap.
        :type instance_name: str

        """
        self.swagger_types = {
            'host_name': 'str',
            'instance_name': 'str'
        }

        self.attribute_map = {
            'host_name': 'hostName',
            'instance_name': 'instanceName'
        }

        self._host_name = None
        self._instance_name = None

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this HostInstanceMap.
        The hostname of the database insight resource.


        :return: The host_name of this HostInstanceMap.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this HostInstanceMap.
        The hostname of the database insight resource.


        :param host_name: The host_name of this HostInstanceMap.
        :type: str
        """
        self._host_name = host_name

    @property
    def instance_name(self):
        """
        **[Required]** Gets the instance_name of this HostInstanceMap.
        The instance name of the database insight resource.


        :return: The instance_name of this HostInstanceMap.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """
        Sets the instance_name of this HostInstanceMap.
        The instance name of the database insight resource.


        :param instance_name: The instance_name of this HostInstanceMap.
        :type: str
        """
        self._instance_name = instance_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
