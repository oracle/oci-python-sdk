# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSubscriptionDetails(object):
    """
    The configuration details for updating the subscription.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSubscriptionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param delivery_policy:
            The value to assign to the delivery_policy property of this UpdateSubscriptionDetails.
        :type delivery_policy: oci.ons.models.DeliveryPolicy

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSubscriptionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSubscriptionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'delivery_policy': 'DeliveryPolicy',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'delivery_policy': 'deliveryPolicy',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._delivery_policy = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def delivery_policy(self):
        """
        Gets the delivery_policy of this UpdateSubscriptionDetails.
        The delivery policy of the subscription. Stored as a JSON string.


        :return: The delivery_policy of this UpdateSubscriptionDetails.
        :rtype: oci.ons.models.DeliveryPolicy
        """
        return self._delivery_policy

    @delivery_policy.setter
    def delivery_policy(self, delivery_policy):
        """
        Sets the delivery_policy of this UpdateSubscriptionDetails.
        The delivery policy of the subscription. Stored as a JSON string.


        :param delivery_policy: The delivery_policy of this UpdateSubscriptionDetails.
        :type: oci.ons.models.DeliveryPolicy
        """
        self._delivery_policy = delivery_policy

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateSubscriptionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateSubscriptionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateSubscriptionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateSubscriptionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateSubscriptionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateSubscriptionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateSubscriptionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateSubscriptionDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
