# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntitlementSummary(object):
    """
    A summary of an entitlement included in a usage plan.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EntitlementSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this EntitlementSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this EntitlementSummary.
        :type description: str

        :param rate_limit:
            The value to assign to the rate_limit property of this EntitlementSummary.
        :type rate_limit: oci.apigateway.models.RateLimit

        :param quota:
            The value to assign to the quota property of this EntitlementSummary.
        :type quota: oci.apigateway.models.Quota

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'rate_limit': 'RateLimit',
            'quota': 'Quota'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'rate_limit': 'rateLimit',
            'quota': 'quota'
        }

        self._name = None
        self._description = None
        self._rate_limit = None
        self._quota = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this EntitlementSummary.
        An entitlement name, unique within a usage plan.


        :return: The name of this EntitlementSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EntitlementSummary.
        An entitlement name, unique within a usage plan.


        :param name: The name of this EntitlementSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this EntitlementSummary.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :return: The description of this EntitlementSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EntitlementSummary.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :param description: The description of this EntitlementSummary.
        :type: str
        """
        self._description = description

    @property
    def rate_limit(self):
        """
        Gets the rate_limit of this EntitlementSummary.

        :return: The rate_limit of this EntitlementSummary.
        :rtype: oci.apigateway.models.RateLimit
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        """
        Sets the rate_limit of this EntitlementSummary.

        :param rate_limit: The rate_limit of this EntitlementSummary.
        :type: oci.apigateway.models.RateLimit
        """
        self._rate_limit = rate_limit

    @property
    def quota(self):
        """
        Gets the quota of this EntitlementSummary.

        :return: The quota of this EntitlementSummary.
        :rtype: oci.apigateway.models.Quota
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """
        Sets the quota of this EntitlementSummary.

        :param quota: The quota of this EntitlementSummary.
        :type: oci.apigateway.models.Quota
        """
        self._quota = quota

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
