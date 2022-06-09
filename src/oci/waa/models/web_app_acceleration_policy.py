# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WebAppAccelerationPolicy(object):
    """
    The details of WebAppAccelerationPolicy. A policy is comprised of rules, which allows enablement of Caching
    and Compression of HTTP response.
    Caching can be enabled for a particular path
    Compression is enabled at global level
    """

    #: A constant which can be used with the lifecycle_state property of a WebAppAccelerationPolicy.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a WebAppAccelerationPolicy.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a WebAppAccelerationPolicy.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a WebAppAccelerationPolicy.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a WebAppAccelerationPolicy.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a WebAppAccelerationPolicy.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new WebAppAccelerationPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WebAppAccelerationPolicy.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this WebAppAccelerationPolicy.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WebAppAccelerationPolicy.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this WebAppAccelerationPolicy.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this WebAppAccelerationPolicy.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this WebAppAccelerationPolicy.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this WebAppAccelerationPolicy.
        :type lifecycle_details: str

        :param response_caching_policy:
            The value to assign to the response_caching_policy property of this WebAppAccelerationPolicy.
        :type response_caching_policy: oci.waa.models.ResponseCachingPolicy

        :param response_compression_policy:
            The value to assign to the response_compression_policy property of this WebAppAccelerationPolicy.
        :type response_compression_policy: oci.waa.models.ResponseCompressionPolicy

        :param freeform_tags:
            The value to assign to the freeform_tags property of this WebAppAccelerationPolicy.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this WebAppAccelerationPolicy.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this WebAppAccelerationPolicy.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'response_caching_policy': 'ResponseCachingPolicy',
            'response_compression_policy': 'ResponseCompressionPolicy',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'response_caching_policy': 'responseCachingPolicy',
            'response_compression_policy': 'responseCompressionPolicy',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._response_caching_policy = None
        self._response_compression_policy = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WebAppAccelerationPolicy.
        The `OCID`__ of the WebAppAccelerationPolicy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this WebAppAccelerationPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WebAppAccelerationPolicy.
        The `OCID`__ of the WebAppAccelerationPolicy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this WebAppAccelerationPolicy.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this WebAppAccelerationPolicy.
        WebAppAccelerationPolicy display name, can be renamed.


        :return: The display_name of this WebAppAccelerationPolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this WebAppAccelerationPolicy.
        WebAppAccelerationPolicy display name, can be renamed.


        :param display_name: The display_name of this WebAppAccelerationPolicy.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WebAppAccelerationPolicy.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this WebAppAccelerationPolicy.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WebAppAccelerationPolicy.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this WebAppAccelerationPolicy.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this WebAppAccelerationPolicy.
        The time the WebAppAccelerationPolicy was created. An RFC3339 formatted datetime string.


        :return: The time_created of this WebAppAccelerationPolicy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this WebAppAccelerationPolicy.
        The time the WebAppAccelerationPolicy was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this WebAppAccelerationPolicy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this WebAppAccelerationPolicy.
        The time the WebAppAccelerationPolicy was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this WebAppAccelerationPolicy.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this WebAppAccelerationPolicy.
        The time the WebAppAccelerationPolicy was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this WebAppAccelerationPolicy.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this WebAppAccelerationPolicy.
        The current state of the WebAppAccelerationPolicy.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this WebAppAccelerationPolicy.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this WebAppAccelerationPolicy.
        The current state of the WebAppAccelerationPolicy.


        :param lifecycle_state: The lifecycle_state of this WebAppAccelerationPolicy.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this WebAppAccelerationPolicy.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource in FAILED state.


        :return: The lifecycle_details of this WebAppAccelerationPolicy.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this WebAppAccelerationPolicy.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource in FAILED state.


        :param lifecycle_details: The lifecycle_details of this WebAppAccelerationPolicy.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def response_caching_policy(self):
        """
        Gets the response_caching_policy of this WebAppAccelerationPolicy.

        :return: The response_caching_policy of this WebAppAccelerationPolicy.
        :rtype: oci.waa.models.ResponseCachingPolicy
        """
        return self._response_caching_policy

    @response_caching_policy.setter
    def response_caching_policy(self, response_caching_policy):
        """
        Sets the response_caching_policy of this WebAppAccelerationPolicy.

        :param response_caching_policy: The response_caching_policy of this WebAppAccelerationPolicy.
        :type: oci.waa.models.ResponseCachingPolicy
        """
        self._response_caching_policy = response_caching_policy

    @property
    def response_compression_policy(self):
        """
        Gets the response_compression_policy of this WebAppAccelerationPolicy.

        :return: The response_compression_policy of this WebAppAccelerationPolicy.
        :rtype: oci.waa.models.ResponseCompressionPolicy
        """
        return self._response_compression_policy

    @response_compression_policy.setter
    def response_compression_policy(self, response_compression_policy):
        """
        Sets the response_compression_policy of this WebAppAccelerationPolicy.

        :param response_compression_policy: The response_compression_policy of this WebAppAccelerationPolicy.
        :type: oci.waa.models.ResponseCompressionPolicy
        """
        self._response_compression_policy = response_compression_policy

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this WebAppAccelerationPolicy.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this WebAppAccelerationPolicy.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this WebAppAccelerationPolicy.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this WebAppAccelerationPolicy.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this WebAppAccelerationPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this WebAppAccelerationPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this WebAppAccelerationPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this WebAppAccelerationPolicy.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        **[Required]** Gets the system_tags of this WebAppAccelerationPolicy.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this WebAppAccelerationPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this WebAppAccelerationPolicy.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this WebAppAccelerationPolicy.
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
