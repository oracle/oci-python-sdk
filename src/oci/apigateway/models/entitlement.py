# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Entitlement(object):
    """
    A usage plan entitlement, comprising of rate limits, quotas and the deployments they are applied to.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Entitlement object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Entitlement.
        :type name: str

        :param description:
            The value to assign to the description property of this Entitlement.
        :type description: str

        :param rate_limit:
            The value to assign to the rate_limit property of this Entitlement.
        :type rate_limit: oci.apigateway.models.RateLimit

        :param quota:
            The value to assign to the quota property of this Entitlement.
        :type quota: oci.apigateway.models.Quota

        :param targets:
            The value to assign to the targets property of this Entitlement.
        :type targets: list[oci.apigateway.models.EntitlementTarget]

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'rate_limit': 'RateLimit',
            'quota': 'Quota',
            'targets': 'list[EntitlementTarget]'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'rate_limit': 'rateLimit',
            'quota': 'quota',
            'targets': 'targets'
        }

        self._name = None
        self._description = None
        self._rate_limit = None
        self._quota = None
        self._targets = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Entitlement.
        An entitlement name, unique within a usage plan.


        :return: The name of this Entitlement.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Entitlement.
        An entitlement name, unique within a usage plan.


        :param name: The name of this Entitlement.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Entitlement.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :return: The description of this Entitlement.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Entitlement.
        A user-friendly description. To provide some insight about the resource.
        Avoid entering confidential information.


        :param description: The description of this Entitlement.
        :type: str
        """
        self._description = description

    @property
    def rate_limit(self):
        """
        Gets the rate_limit of this Entitlement.

        :return: The rate_limit of this Entitlement.
        :rtype: oci.apigateway.models.RateLimit
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        """
        Sets the rate_limit of this Entitlement.

        :param rate_limit: The rate_limit of this Entitlement.
        :type: oci.apigateway.models.RateLimit
        """
        self._rate_limit = rate_limit

    @property
    def quota(self):
        """
        Gets the quota of this Entitlement.

        :return: The quota of this Entitlement.
        :rtype: oci.apigateway.models.Quota
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """
        Sets the quota of this Entitlement.

        :param quota: The quota of this Entitlement.
        :type: oci.apigateway.models.Quota
        """
        self._quota = quota

    @property
    def targets(self):
        """
        Gets the targets of this Entitlement.
        A collection of targeted deployments that the entitlement will be applied to.


        :return: The targets of this Entitlement.
        :rtype: list[oci.apigateway.models.EntitlementTarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this Entitlement.
        A collection of targeted deployments that the entitlement will be applied to.


        :param targets: The targets of this Entitlement.
        :type: list[oci.apigateway.models.EntitlementTarget]
        """
        self._targets = targets

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
