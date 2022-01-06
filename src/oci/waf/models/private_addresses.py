# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateAddresses(object):
    """
    A pair of VCN OCID and private IP address prefix in CIDR notation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateAddresses object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vcn_id:
            The value to assign to the vcn_id property of this PrivateAddresses.
        :type vcn_id: str

        :param addresses:
            The value to assign to the addresses property of this PrivateAddresses.
        :type addresses: str

        """
        self.swagger_types = {
            'vcn_id': 'str',
            'addresses': 'str'
        }

        self.attribute_map = {
            'vcn_id': 'vcnId',
            'addresses': 'addresses'
        }

        self._vcn_id = None
        self._addresses = None

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this PrivateAddresses.
        The `OCID`__ of the VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this PrivateAddresses.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this PrivateAddresses.
        The `OCID`__ of the VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this PrivateAddresses.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def addresses(self):
        """
        **[Required]** Gets the addresses of this PrivateAddresses.
        A private IP address or CIDR IP address range.


        :return: The addresses of this PrivateAddresses.
        :rtype: str
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this PrivateAddresses.
        A private IP address or CIDR IP address range.


        :param addresses: The addresses of this PrivateAddresses.
        :type: str
        """
        self._addresses = addresses

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
