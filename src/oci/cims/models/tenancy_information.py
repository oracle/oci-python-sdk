# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TenancyInformation(object):
    """
    Details about the customer's tenancy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TenancyInformation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param customer_support_key:
            The value to assign to the customer_support_key property of this TenancyInformation.
        :type customer_support_key: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this TenancyInformation.
        :type tenancy_id: str

        """
        self.swagger_types = {
            'customer_support_key': 'str',
            'tenancy_id': 'str'
        }

        self.attribute_map = {
            'customer_support_key': 'customerSupportKey',
            'tenancy_id': 'tenancyId'
        }

        self._customer_support_key = None
        self._tenancy_id = None

    @property
    def customer_support_key(self):
        """
        **[Required]** Gets the customer_support_key of this TenancyInformation.
        The Customer Support Identifier number associated with the tenancy.


        :return: The customer_support_key of this TenancyInformation.
        :rtype: str
        """
        return self._customer_support_key

    @customer_support_key.setter
    def customer_support_key(self, customer_support_key):
        """
        Sets the customer_support_key of this TenancyInformation.
        The Customer Support Identifier number associated with the tenancy.


        :param customer_support_key: The customer_support_key of this TenancyInformation.
        :type: str
        """
        self._customer_support_key = customer_support_key

    @property
    def tenancy_id(self):
        """
        **[Required]** Gets the tenancy_id of this TenancyInformation.
        The OCID of the tenancy.


        :return: The tenancy_id of this TenancyInformation.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this TenancyInformation.
        The OCID of the tenancy.


        :param tenancy_id: The tenancy_id of this TenancyInformation.
        :type: str
        """
        self._tenancy_id = tenancy_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
