# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOrganizationDetails(object):
    """
    The parameters for updating an organization.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOrganizationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param default_ucm_subscription_id:
            The value to assign to the default_ucm_subscription_id property of this UpdateOrganizationDetails.
        :type default_ucm_subscription_id: str

        """
        self.swagger_types = {
            'default_ucm_subscription_id': 'str'
        }

        self.attribute_map = {
            'default_ucm_subscription_id': 'defaultUcmSubscriptionId'
        }

        self._default_ucm_subscription_id = None

    @property
    def default_ucm_subscription_id(self):
        """
        **[Required]** Gets the default_ucm_subscription_id of this UpdateOrganizationDetails.
        OCID of the default UCM subscription. Any tenancy joining the organization will automatically get assigned this subscription if a subscription if not explictly assigned.


        :return: The default_ucm_subscription_id of this UpdateOrganizationDetails.
        :rtype: str
        """
        return self._default_ucm_subscription_id

    @default_ucm_subscription_id.setter
    def default_ucm_subscription_id(self, default_ucm_subscription_id):
        """
        Sets the default_ucm_subscription_id of this UpdateOrganizationDetails.
        OCID of the default UCM subscription. Any tenancy joining the organization will automatically get assigned this subscription if a subscription if not explictly assigned.


        :param default_ucm_subscription_id: The default_ucm_subscription_id of this UpdateOrganizationDetails.
        :type: str
        """
        self._default_ucm_subscription_id = default_ucm_subscription_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
