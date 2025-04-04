# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220618


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DesktopPoolPrivateAccessDetails(object):
    """
    The details of the desktop's private access network connectivity that were used to create the pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DesktopPoolPrivateAccessDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vcn_id:
            The value to assign to the vcn_id property of this DesktopPoolPrivateAccessDetails.
        :type vcn_id: str

        :param endpoint_fqdn:
            The value to assign to the endpoint_fqdn property of this DesktopPoolPrivateAccessDetails.
        :type endpoint_fqdn: str

        :param subnet_id:
            The value to assign to the subnet_id property of this DesktopPoolPrivateAccessDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this DesktopPoolPrivateAccessDetails.
        :type nsg_ids: list[str]

        :param private_ip:
            The value to assign to the private_ip property of this DesktopPoolPrivateAccessDetails.
        :type private_ip: str

        """
        self.swagger_types = {
            'vcn_id': 'str',
            'endpoint_fqdn': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'private_ip': 'str'
        }
        self.attribute_map = {
            'vcn_id': 'vcnId',
            'endpoint_fqdn': 'endpointFqdn',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'private_ip': 'privateIp'
        }
        self._vcn_id = None
        self._endpoint_fqdn = None
        self._subnet_id = None
        self._nsg_ids = None
        self._private_ip = None

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this DesktopPoolPrivateAccessDetails.
        The `OCID`__ of the customer VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this DesktopPoolPrivateAccessDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this DesktopPoolPrivateAccessDetails.
        The `OCID`__ of the customer VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this DesktopPoolPrivateAccessDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def endpoint_fqdn(self):
        """
        Gets the endpoint_fqdn of this DesktopPoolPrivateAccessDetails.
        The three-label FQDN to use for the private endpoint. The customer VCN's DNS records are
        updated with this FQDN. This enables the customer to use the FQDN instead of the private endpoint's
        private IP address to access the service (for example,\u00A0xyz.oraclecloud.com).


        :return: The endpoint_fqdn of this DesktopPoolPrivateAccessDetails.
        :rtype: str
        """
        return self._endpoint_fqdn

    @endpoint_fqdn.setter
    def endpoint_fqdn(self, endpoint_fqdn):
        """
        Sets the endpoint_fqdn of this DesktopPoolPrivateAccessDetails.
        The three-label FQDN to use for the private endpoint. The customer VCN's DNS records are
        updated with this FQDN. This enables the customer to use the FQDN instead of the private endpoint's
        private IP address to access the service (for example,\u00A0xyz.oraclecloud.com).


        :param endpoint_fqdn: The endpoint_fqdn of this DesktopPoolPrivateAccessDetails.
        :type: str
        """
        self._endpoint_fqdn = endpoint_fqdn

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this DesktopPoolPrivateAccessDetails.
        The `OCID`__ of the subnet in the customer VCN where the
        connectivity will be established.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this DesktopPoolPrivateAccessDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DesktopPoolPrivateAccessDetails.
        The `OCID`__ of the subnet in the customer VCN where the
        connectivity will be established.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this DesktopPoolPrivateAccessDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this DesktopPoolPrivateAccessDetails.
        A list of network security groups for the private access.


        :return: The nsg_ids of this DesktopPoolPrivateAccessDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this DesktopPoolPrivateAccessDetails.
        A list of network security groups for the private access.


        :param nsg_ids: The nsg_ids of this DesktopPoolPrivateAccessDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def private_ip(self):
        """
        Gets the private_ip of this DesktopPoolPrivateAccessDetails.
        The IPv4 address from the provided OCI subnet which needs to be assigned to the VNIC. If not provided, it will
        be auto-assigned with an available IPv4 address from the subnet.


        :return: The private_ip of this DesktopPoolPrivateAccessDetails.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this DesktopPoolPrivateAccessDetails.
        The IPv4 address from the provided OCI subnet which needs to be assigned to the VNIC. If not provided, it will
        be auto-assigned with an available IPv4 address from the subnet.


        :param private_ip: The private_ip of this DesktopPoolPrivateAccessDetails.
        :type: str
        """
        self._private_ip = private_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
