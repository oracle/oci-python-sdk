# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GetPublicIpByPrivateIpIdDetails(object):
    """
    Details of the private IP that the public IP is assigned to.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GetPublicIpByPrivateIpIdDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param private_ip_id:
            The value to assign to the private_ip_id property of this GetPublicIpByPrivateIpIdDetails.
        :type private_ip_id: str

        """
        self.swagger_types = {
            'private_ip_id': 'str'
        }

        self.attribute_map = {
            'private_ip_id': 'privateIpId'
        }

        self._private_ip_id = None

    @property
    def private_ip_id(self):
        """
        **[Required]** Gets the private_ip_id of this GetPublicIpByPrivateIpIdDetails.
        OCID of the private IP.


        :return: The private_ip_id of this GetPublicIpByPrivateIpIdDetails.
        :rtype: str
        """
        return self._private_ip_id

    @private_ip_id.setter
    def private_ip_id(self, private_ip_id):
        """
        Sets the private_ip_id of this GetPublicIpByPrivateIpIdDetails.
        OCID of the private IP.


        :param private_ip_id: The private_ip_id of this GetPublicIpByPrivateIpIdDetails.
        :type: str
        """
        self._private_ip_id = private_ip_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
