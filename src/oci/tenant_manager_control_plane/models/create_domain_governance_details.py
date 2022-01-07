# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDomainGovernanceDetails(object):
    """
    The parameters for creating a domain governance entity.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDomainGovernanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDomainGovernanceDetails.
        :type compartment_id: str

        :param domain_id:
            The value to assign to the domain_id property of this CreateDomainGovernanceDetails.
        :type domain_id: str

        :param subscription_email:
            The value to assign to the subscription_email property of this CreateDomainGovernanceDetails.
        :type subscription_email: str

        :param ons_topic_id:
            The value to assign to the ons_topic_id property of this CreateDomainGovernanceDetails.
        :type ons_topic_id: str

        :param ons_subscription_id:
            The value to assign to the ons_subscription_id property of this CreateDomainGovernanceDetails.
        :type ons_subscription_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDomainGovernanceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDomainGovernanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'domain_id': 'str',
            'subscription_email': 'str',
            'ons_topic_id': 'str',
            'ons_subscription_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'domain_id': 'domainId',
            'subscription_email': 'subscriptionEmail',
            'ons_topic_id': 'onsTopicId',
            'ons_subscription_id': 'onsSubscriptionId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._domain_id = None
        self._subscription_email = None
        self._ons_topic_id = None
        self._ons_subscription_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDomainGovernanceDetails.
        OCID of the tenancy.


        :return: The compartment_id of this CreateDomainGovernanceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDomainGovernanceDetails.
        OCID of the tenancy.


        :param compartment_id: The compartment_id of this CreateDomainGovernanceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def domain_id(self):
        """
        **[Required]** Gets the domain_id of this CreateDomainGovernanceDetails.
        OCID of the domain.


        :return: The domain_id of this CreateDomainGovernanceDetails.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """
        Sets the domain_id of this CreateDomainGovernanceDetails.
        OCID of the domain.


        :param domain_id: The domain_id of this CreateDomainGovernanceDetails.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def subscription_email(self):
        """
        **[Required]** Gets the subscription_email of this CreateDomainGovernanceDetails.
        The email to notify the user, and that the ONS subscription will be created with.


        :return: The subscription_email of this CreateDomainGovernanceDetails.
        :rtype: str
        """
        return self._subscription_email

    @subscription_email.setter
    def subscription_email(self, subscription_email):
        """
        Sets the subscription_email of this CreateDomainGovernanceDetails.
        The email to notify the user, and that the ONS subscription will be created with.


        :param subscription_email: The subscription_email of this CreateDomainGovernanceDetails.
        :type: str
        """
        self._subscription_email = subscription_email

    @property
    def ons_topic_id(self):
        """
        **[Required]** Gets the ons_topic_id of this CreateDomainGovernanceDetails.
        The ONS topic associated with this domain governance entity.


        :return: The ons_topic_id of this CreateDomainGovernanceDetails.
        :rtype: str
        """
        return self._ons_topic_id

    @ons_topic_id.setter
    def ons_topic_id(self, ons_topic_id):
        """
        Sets the ons_topic_id of this CreateDomainGovernanceDetails.
        The ONS topic associated with this domain governance entity.


        :param ons_topic_id: The ons_topic_id of this CreateDomainGovernanceDetails.
        :type: str
        """
        self._ons_topic_id = ons_topic_id

    @property
    def ons_subscription_id(self):
        """
        **[Required]** Gets the ons_subscription_id of this CreateDomainGovernanceDetails.
        The ONS subscription associated with this domain governance entity.


        :return: The ons_subscription_id of this CreateDomainGovernanceDetails.
        :rtype: str
        """
        return self._ons_subscription_id

    @ons_subscription_id.setter
    def ons_subscription_id(self, ons_subscription_id):
        """
        Sets the ons_subscription_id of this CreateDomainGovernanceDetails.
        The ONS subscription associated with this domain governance entity.


        :param ons_subscription_id: The ons_subscription_id of this CreateDomainGovernanceDetails.
        :type: str
        """
        self._ons_subscription_id = ons_subscription_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDomainGovernanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDomainGovernanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDomainGovernanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDomainGovernanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDomainGovernanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDomainGovernanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDomainGovernanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDomainGovernanceDetails.
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
