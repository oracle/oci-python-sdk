# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeCloudExadataInfrastructureSubscriptionDetails(object):
    """
    The configuration details for associating the cloud Exadata infrastructure resource with a different subscription.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeCloudExadataInfrastructureSubscriptionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param subscription_id:
            The value to assign to the subscription_id property of this ChangeCloudExadataInfrastructureSubscriptionDetails.
        :type subscription_id: str

        :param is_default:
            The value to assign to the is_default property of this ChangeCloudExadataInfrastructureSubscriptionDetails.
        :type is_default: bool

        """
        self.swagger_types = {
            'subscription_id': 'str',
            'is_default': 'bool'
        }

        self.attribute_map = {
            'subscription_id': 'subscriptionId',
            'is_default': 'isDefault'
        }

        self._subscription_id = None
        self._is_default = None

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this ChangeCloudExadataInfrastructureSubscriptionDetails.
        The `OCID`__ of the subscription with which resource needs to be associated with.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subscription_id of this ChangeCloudExadataInfrastructureSubscriptionDetails.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this ChangeCloudExadataInfrastructureSubscriptionDetails.
        The `OCID`__ of the subscription with which resource needs to be associated with.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subscription_id: The subscription_id of this ChangeCloudExadataInfrastructureSubscriptionDetails.
        :type: str
        """
        self._subscription_id = subscription_id

    @property
    def is_default(self):
        """
        Gets the is_default of this ChangeCloudExadataInfrastructureSubscriptionDetails.
        Indicates if the subscription is UCM or not.


        :return: The is_default of this ChangeCloudExadataInfrastructureSubscriptionDetails.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this ChangeCloudExadataInfrastructureSubscriptionDetails.
        Indicates if the subscription is UCM or not.


        :param is_default: The is_default of this ChangeCloudExadataInfrastructureSubscriptionDetails.
        :type: bool
        """
        self._is_default = is_default

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
