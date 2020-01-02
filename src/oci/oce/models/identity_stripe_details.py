# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IdentityStripeDetails(object):
    """
    Identity Stripe
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IdentityStripeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param service_name:
            The value to assign to the service_name property of this IdentityStripeDetails.
        :type service_name: str

        :param tenancy:
            The value to assign to the tenancy property of this IdentityStripeDetails.
        :type tenancy: str

        """
        self.swagger_types = {
            'service_name': 'str',
            'tenancy': 'str'
        }

        self.attribute_map = {
            'service_name': 'serviceName',
            'tenancy': 'tenancy'
        }

        self._service_name = None
        self._tenancy = None

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this IdentityStripeDetails.
        Name of the Identity Cloud Service instance in My Services to be used.
        Example: `secondstripe`


        :return: The service_name of this IdentityStripeDetails.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this IdentityStripeDetails.
        Name of the Identity Cloud Service instance in My Services to be used.
        Example: `secondstripe`


        :param service_name: The service_name of this IdentityStripeDetails.
        :type: str
        """
        self._service_name = service_name

    @property
    def tenancy(self):
        """
        **[Required]** Gets the tenancy of this IdentityStripeDetails.
        Value of the Identity Cloud Service tenancy.
        Example: `idcs-8416ebdd0d674f84803f4193cce026e9`


        :return: The tenancy of this IdentityStripeDetails.
        :rtype: str
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        """
        Sets the tenancy of this IdentityStripeDetails.
        Value of the Identity Cloud Service tenancy.
        Example: `idcs-8416ebdd0d674f84803f4193cce026e9`


        :param tenancy: The tenancy of this IdentityStripeDetails.
        :type: str
        """
        self._tenancy = tenancy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
