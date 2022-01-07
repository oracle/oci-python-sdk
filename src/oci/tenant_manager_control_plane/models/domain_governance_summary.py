# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DomainGovernanceSummary(object):
    """
    The summary of a domain govenance entity owned by a tenancy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DomainGovernanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DomainGovernanceSummary.
        :type id: str

        :param owner_id:
            The value to assign to the owner_id property of this DomainGovernanceSummary.
        :type owner_id: str

        :param domain_id:
            The value to assign to the domain_id property of this DomainGovernanceSummary.
        :type domain_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DomainGovernanceSummary.
        :type lifecycle_state: str

        :param is_governance_enabled:
            The value to assign to the is_governance_enabled property of this DomainGovernanceSummary.
        :type is_governance_enabled: bool

        :param subscription_email:
            The value to assign to the subscription_email property of this DomainGovernanceSummary.
        :type subscription_email: str

        :param ons_topic_id:
            The value to assign to the ons_topic_id property of this DomainGovernanceSummary.
        :type ons_topic_id: str

        :param ons_subscription_id:
            The value to assign to the ons_subscription_id property of this DomainGovernanceSummary.
        :type ons_subscription_id: str

        :param time_created:
            The value to assign to the time_created property of this DomainGovernanceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DomainGovernanceSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DomainGovernanceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DomainGovernanceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DomainGovernanceSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'owner_id': 'str',
            'domain_id': 'str',
            'lifecycle_state': 'str',
            'is_governance_enabled': 'bool',
            'subscription_email': 'str',
            'ons_topic_id': 'str',
            'ons_subscription_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'owner_id': 'ownerId',
            'domain_id': 'domainId',
            'lifecycle_state': 'lifecycleState',
            'is_governance_enabled': 'isGovernanceEnabled',
            'subscription_email': 'subscriptionEmail',
            'ons_topic_id': 'onsTopicId',
            'ons_subscription_id': 'onsSubscriptionId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._owner_id = None
        self._domain_id = None
        self._lifecycle_state = None
        self._is_governance_enabled = None
        self._subscription_email = None
        self._ons_topic_id = None
        self._ons_subscription_id = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DomainGovernanceSummary.
        The OCID of the domain governance entity.


        :return: The id of this DomainGovernanceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DomainGovernanceSummary.
        The OCID of the domain governance entity.


        :param id: The id of this DomainGovernanceSummary.
        :type: str
        """
        self._id = id

    @property
    def owner_id(self):
        """
        **[Required]** Gets the owner_id of this DomainGovernanceSummary.
        The OCID of the tenancy that owns this domain governance entity.


        :return: The owner_id of this DomainGovernanceSummary.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this DomainGovernanceSummary.
        The OCID of the tenancy that owns this domain governance entity.


        :param owner_id: The owner_id of this DomainGovernanceSummary.
        :type: str
        """
        self._owner_id = owner_id

    @property
    def domain_id(self):
        """
        **[Required]** Gets the domain_id of this DomainGovernanceSummary.
        The OCID of the domain associated with this domain governance entity.


        :return: The domain_id of this DomainGovernanceSummary.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """
        Sets the domain_id of this DomainGovernanceSummary.
        The OCID of the domain associated with this domain governance entity.


        :param domain_id: The domain_id of this DomainGovernanceSummary.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DomainGovernanceSummary.
        The lifecycle state of the domain governance entity.


        :return: The lifecycle_state of this DomainGovernanceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DomainGovernanceSummary.
        The lifecycle state of the domain governance entity.


        :param lifecycle_state: The lifecycle_state of this DomainGovernanceSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def is_governance_enabled(self):
        """
        **[Required]** Gets the is_governance_enabled of this DomainGovernanceSummary.
        Indicates whether governance is enabled for this domain.


        :return: The is_governance_enabled of this DomainGovernanceSummary.
        :rtype: bool
        """
        return self._is_governance_enabled

    @is_governance_enabled.setter
    def is_governance_enabled(self, is_governance_enabled):
        """
        Sets the is_governance_enabled of this DomainGovernanceSummary.
        Indicates whether governance is enabled for this domain.


        :param is_governance_enabled: The is_governance_enabled of this DomainGovernanceSummary.
        :type: bool
        """
        self._is_governance_enabled = is_governance_enabled

    @property
    def subscription_email(self):
        """
        Gets the subscription_email of this DomainGovernanceSummary.
        The email to notify the user, and that the ONS subscription will be created with.


        :return: The subscription_email of this DomainGovernanceSummary.
        :rtype: str
        """
        return self._subscription_email

    @subscription_email.setter
    def subscription_email(self, subscription_email):
        """
        Sets the subscription_email of this DomainGovernanceSummary.
        The email to notify the user, and that the ONS subscription will be created with.


        :param subscription_email: The subscription_email of this DomainGovernanceSummary.
        :type: str
        """
        self._subscription_email = subscription_email

    @property
    def ons_topic_id(self):
        """
        **[Required]** Gets the ons_topic_id of this DomainGovernanceSummary.
        The ONS topic associated with this domain governance entity.


        :return: The ons_topic_id of this DomainGovernanceSummary.
        :rtype: str
        """
        return self._ons_topic_id

    @ons_topic_id.setter
    def ons_topic_id(self, ons_topic_id):
        """
        Sets the ons_topic_id of this DomainGovernanceSummary.
        The ONS topic associated with this domain governance entity.


        :param ons_topic_id: The ons_topic_id of this DomainGovernanceSummary.
        :type: str
        """
        self._ons_topic_id = ons_topic_id

    @property
    def ons_subscription_id(self):
        """
        **[Required]** Gets the ons_subscription_id of this DomainGovernanceSummary.
        The ONS subscription associated with this domain governance entity.


        :return: The ons_subscription_id of this DomainGovernanceSummary.
        :rtype: str
        """
        return self._ons_subscription_id

    @ons_subscription_id.setter
    def ons_subscription_id(self, ons_subscription_id):
        """
        Sets the ons_subscription_id of this DomainGovernanceSummary.
        The ONS subscription associated with this domain governance entity.


        :param ons_subscription_id: The ons_subscription_id of this DomainGovernanceSummary.
        :type: str
        """
        self._ons_subscription_id = ons_subscription_id

    @property
    def time_created(self):
        """
        Gets the time_created of this DomainGovernanceSummary.
        Date-time when this domain governance was created. An RFC 3339-formatted date and time string.


        :return: The time_created of this DomainGovernanceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DomainGovernanceSummary.
        Date-time when this domain governance was created. An RFC 3339-formatted date and time string.


        :param time_created: The time_created of this DomainGovernanceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DomainGovernanceSummary.
        Date-time when this domain governance was last updated. An RFC 3339-formatted date and time string.


        :return: The time_updated of this DomainGovernanceSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DomainGovernanceSummary.
        Date-time when this domain governance was last updated. An RFC 3339-formatted date and time string.


        :param time_updated: The time_updated of this DomainGovernanceSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DomainGovernanceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DomainGovernanceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DomainGovernanceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DomainGovernanceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DomainGovernanceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DomainGovernanceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DomainGovernanceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DomainGovernanceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DomainGovernanceSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DomainGovernanceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DomainGovernanceSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DomainGovernanceSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
