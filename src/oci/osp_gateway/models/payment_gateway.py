# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PaymentGateway(object):
    """
    Payment gateway details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PaymentGateway object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param merchant_defined_data:
            The value to assign to the merchant_defined_data property of this PaymentGateway.
        :type merchant_defined_data: oci.osp_gateway.models.MerchantDefinedData

        """
        self.swagger_types = {
            'merchant_defined_data': 'MerchantDefinedData'
        }

        self.attribute_map = {
            'merchant_defined_data': 'merchantDefinedData'
        }

        self._merchant_defined_data = None

    @property
    def merchant_defined_data(self):
        """
        Gets the merchant_defined_data of this PaymentGateway.

        :return: The merchant_defined_data of this PaymentGateway.
        :rtype: oci.osp_gateway.models.MerchantDefinedData
        """
        return self._merchant_defined_data

    @merchant_defined_data.setter
    def merchant_defined_data(self, merchant_defined_data):
        """
        Sets the merchant_defined_data of this PaymentGateway.

        :param merchant_defined_data: The merchant_defined_data of this PaymentGateway.
        :type: oci.osp_gateway.models.MerchantDefinedData
        """
        self._merchant_defined_data = merchant_defined_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
