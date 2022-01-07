# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSubscriptionMappingDetails(object):
    """
    CreateSubscriptionMappingDetails contains subscription and compartment identified by the tenancy, and OCID information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSubscriptionMappingDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSubscriptionMappingDetails.
        :type compartment_id: str

        :param subscription_id:
            The value to assign to the subscription_id property of this CreateSubscriptionMappingDetails.
        :type subscription_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'subscription_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'subscription_id': 'subscriptionId'
        }

        self._compartment_id = None
        self._subscription_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSubscriptionMappingDetails.
        OCID of the compartment. Always a tenancy OCID.


        :return: The compartment_id of this CreateSubscriptionMappingDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSubscriptionMappingDetails.
        OCID of the compartment. Always a tenancy OCID.


        :param compartment_id: The compartment_id of this CreateSubscriptionMappingDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def subscription_id(self):
        """
        **[Required]** Gets the subscription_id of this CreateSubscriptionMappingDetails.
        OCID of subscription.


        :return: The subscription_id of this CreateSubscriptionMappingDetails.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this CreateSubscriptionMappingDetails.
        OCID of subscription.


        :param subscription_id: The subscription_id of this CreateSubscriptionMappingDetails.
        :type: str
        """
        self._subscription_id = subscription_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
