# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDomainDetails(object):
    """
    The parameters for creating a domain.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDomainDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDomainDetails.
        :type compartment_id: str

        :param domain_name:
            The value to assign to the domain_name property of this CreateDomainDetails.
        :type domain_name: str

        :param subscription_email:
            The value to assign to the subscription_email property of this CreateDomainDetails.
        :type subscription_email: str

        :param is_governance_enabled:
            The value to assign to the is_governance_enabled property of this CreateDomainDetails.
        :type is_governance_enabled: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDomainDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDomainDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'domain_name': 'str',
            'subscription_email': 'str',
            'is_governance_enabled': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'domain_name': 'domainName',
            'subscription_email': 'subscriptionEmail',
            'is_governance_enabled': 'isGovernanceEnabled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._domain_name = None
        self._subscription_email = None
        self._is_governance_enabled = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDomainDetails.
        OCID of the tenancy.


        :return: The compartment_id of this CreateDomainDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDomainDetails.
        OCID of the tenancy.


        :param compartment_id: The compartment_id of this CreateDomainDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def domain_name(self):
        """
        **[Required]** Gets the domain_name of this CreateDomainDetails.
        The domain name.


        :return: The domain_name of this CreateDomainDetails.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """
        Sets the domain_name of this CreateDomainDetails.
        The domain name.


        :param domain_name: The domain_name of this CreateDomainDetails.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def subscription_email(self):
        """
        Gets the subscription_email of this CreateDomainDetails.
        The email to notify the user, and that the ONS subscription will be created with.


        :return: The subscription_email of this CreateDomainDetails.
        :rtype: str
        """
        return self._subscription_email

    @subscription_email.setter
    def subscription_email(self, subscription_email):
        """
        Sets the subscription_email of this CreateDomainDetails.
        The email to notify the user, and that the ONS subscription will be created with.


        :param subscription_email: The subscription_email of this CreateDomainDetails.
        :type: str
        """
        self._subscription_email = subscription_email

    @property
    def is_governance_enabled(self):
        """
        Gets the is_governance_enabled of this CreateDomainDetails.
        Indicates whether governance should be enabled for this domain. Defaults to false.


        :return: The is_governance_enabled of this CreateDomainDetails.
        :rtype: bool
        """
        return self._is_governance_enabled

    @is_governance_enabled.setter
    def is_governance_enabled(self, is_governance_enabled):
        """
        Sets the is_governance_enabled of this CreateDomainDetails.
        Indicates whether governance should be enabled for this domain. Defaults to false.


        :param is_governance_enabled: The is_governance_enabled of this CreateDomainDetails.
        :type: bool
        """
        self._is_governance_enabled = is_governance_enabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDomainDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDomainDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDomainDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDomainDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDomainDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDomainDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDomainDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDomainDetails.
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
