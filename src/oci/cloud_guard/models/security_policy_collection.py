# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityPolicyCollection(object):
    """
    Results of a security policy search.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityPolicyCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this SecurityPolicyCollection.
        :type items: list[oci.cloud_guard.models.SecurityPolicySummary]

        :param locks:
            The value to assign to the locks property of this SecurityPolicyCollection.
        :type locks: list[oci.cloud_guard.models.ResourceLock]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SecurityPolicyCollection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SecurityPolicyCollection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SecurityPolicyCollection.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'items': 'list[SecurityPolicySummary]',
            'locks': 'list[ResourceLock]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'items': 'items',
            'locks': 'locks',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._items = None
        self._locks = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this SecurityPolicyCollection.
        A list of SecurityPolicySummary resources


        :return: The items of this SecurityPolicyCollection.
        :rtype: list[oci.cloud_guard.models.SecurityPolicySummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this SecurityPolicyCollection.
        A list of SecurityPolicySummary resources


        :param items: The items of this SecurityPolicyCollection.
        :type: list[oci.cloud_guard.models.SecurityPolicySummary]
        """
        self._items = items

    @property
    def locks(self):
        """
        Gets the locks of this SecurityPolicyCollection.
        Locks associated with this resource.


        :return: The locks of this SecurityPolicyCollection.
        :rtype: list[oci.cloud_guard.models.ResourceLock]
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """
        Sets the locks of this SecurityPolicyCollection.
        Locks associated with this resource.


        :param locks: The locks of this SecurityPolicyCollection.
        :type: list[oci.cloud_guard.models.ResourceLock]
        """
        self._locks = locks

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SecurityPolicyCollection.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this SecurityPolicyCollection.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SecurityPolicyCollection.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this SecurityPolicyCollection.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SecurityPolicyCollection.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this SecurityPolicyCollection.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SecurityPolicyCollection.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this SecurityPolicyCollection.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this SecurityPolicyCollection.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this SecurityPolicyCollection.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this SecurityPolicyCollection.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this SecurityPolicyCollection.
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
