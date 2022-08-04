# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VirtualCloudNetwork(object):
    """
    Virtual Cloud Network definition.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VirtualCloudNetwork object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this VirtualCloudNetwork.
        :type id: str

        :param allowlisted_ips:
            The value to assign to the allowlisted_ips property of this VirtualCloudNetwork.
        :type allowlisted_ips: list[str]

        """
        self.swagger_types = {
            'id': 'str',
            'allowlisted_ips': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'allowlisted_ips': 'allowlistedIps'
        }

        self._id = None
        self._allowlisted_ips = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VirtualCloudNetwork.
        The Virtual Cloud Network OCID.


        :return: The id of this VirtualCloudNetwork.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VirtualCloudNetwork.
        The Virtual Cloud Network OCID.


        :param id: The id of this VirtualCloudNetwork.
        :type: str
        """
        self._id = id

    @property
    def allowlisted_ips(self):
        """
        Gets the allowlisted_ips of this VirtualCloudNetwork.
        Source IP addresses or IP address ranges ingress rules. (ex: \"168.122.59.5\", \"10.20.30.0/26\")
        An invalid IP or CIDR block will result in a 400 response.


        :return: The allowlisted_ips of this VirtualCloudNetwork.
        :rtype: list[str]
        """
        return self._allowlisted_ips

    @allowlisted_ips.setter
    def allowlisted_ips(self, allowlisted_ips):
        """
        Sets the allowlisted_ips of this VirtualCloudNetwork.
        Source IP addresses or IP address ranges ingress rules. (ex: \"168.122.59.5\", \"10.20.30.0/26\")
        An invalid IP or CIDR block will result in a 400 response.


        :param allowlisted_ips: The allowlisted_ips of this VirtualCloudNetwork.
        :type: list[str]
        """
        self._allowlisted_ips = allowlisted_ips

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
