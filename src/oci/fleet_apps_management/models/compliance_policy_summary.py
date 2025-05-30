# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CompliancePolicySummary(object):
    """
    Summary information about a CompliancePolicy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CompliancePolicySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CompliancePolicySummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this CompliancePolicySummary.
        :type display_name: str

        :param product_id:
            The value to assign to the product_id property of this CompliancePolicySummary.
        :type product_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CompliancePolicySummary.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this CompliancePolicySummary.
        :type type: str

        :param time_created:
            The value to assign to the time_created property of this CompliancePolicySummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this CompliancePolicySummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CompliancePolicySummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this CompliancePolicySummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CompliancePolicySummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CompliancePolicySummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this CompliancePolicySummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'product_id': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'product_id': 'productId',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._display_name = None
        self._product_id = None
        self._compartment_id = None
        self._type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CompliancePolicySummary.
        The OCID of the CompliancePolicy.


        :return: The id of this CompliancePolicySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CompliancePolicySummary.
        The OCID of the CompliancePolicy.


        :param id: The id of this CompliancePolicySummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CompliancePolicySummary.
        Display name for the CompliancePolicy.


        :return: The display_name of this CompliancePolicySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CompliancePolicySummary.
        Display name for the CompliancePolicy.


        :param display_name: The display_name of this CompliancePolicySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def product_id(self):
        """
        **[Required]** Gets the product_id of this CompliancePolicySummary.
        platformConfiguration OCID corresponding to the Product.


        :return: The product_id of this CompliancePolicySummary.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this CompliancePolicySummary.
        platformConfiguration OCID corresponding to the Product.


        :param product_id: The product_id of this CompliancePolicySummary.
        :type: str
        """
        self._product_id = product_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CompliancePolicySummary.
        The OCID of the compartment the CompliancePolicy belongs to.


        :return: The compartment_id of this CompliancePolicySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CompliancePolicySummary.
        The OCID of the compartment the CompliancePolicy belongs to.


        :param compartment_id: The compartment_id of this CompliancePolicySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def type(self):
        """
        Gets the type of this CompliancePolicySummary.
        The type of the Compliance Policy.


        :return: The type of this CompliancePolicySummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CompliancePolicySummary.
        The type of the Compliance Policy.


        :param type: The type of this CompliancePolicySummary.
        :type: str
        """
        self._type = type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this CompliancePolicySummary.
        The date and time the CompliancePolicy was created, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CompliancePolicySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CompliancePolicySummary.
        The date and time the CompliancePolicy was created, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CompliancePolicySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this CompliancePolicySummary.
        The date and time the CompliancePolicy was updated, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this CompliancePolicySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this CompliancePolicySummary.
        The date and time the CompliancePolicy was updated, in the format defined by `RFC 3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this CompliancePolicySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this CompliancePolicySummary.
        The current state of the CompliancePolicy.


        :return: The lifecycle_state of this CompliancePolicySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CompliancePolicySummary.
        The current state of the CompliancePolicy.


        :param lifecycle_state: The lifecycle_state of this CompliancePolicySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this CompliancePolicySummary.
        A message that describes the current state of the CompliancePolicy in more detail. For example,
        can be used to provide actionable information for a resource in the Failed state.


        :return: The lifecycle_details of this CompliancePolicySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this CompliancePolicySummary.
        A message that describes the current state of the CompliancePolicy in more detail. For example,
        can be used to provide actionable information for a resource in the Failed state.


        :param lifecycle_details: The lifecycle_details of this CompliancePolicySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this CompliancePolicySummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CompliancePolicySummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CompliancePolicySummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CompliancePolicySummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this CompliancePolicySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CompliancePolicySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CompliancePolicySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CompliancePolicySummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this CompliancePolicySummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this CompliancePolicySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this CompliancePolicySummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this CompliancePolicySummary.
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
