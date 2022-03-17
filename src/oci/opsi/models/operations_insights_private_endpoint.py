# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperationsInsightsPrivateEndpoint(object):
    """
    A private endpoint that allows Operation Insights services to connect to databases in a customer's virtual cloud network (VCN).
    """

    #: A constant which can be used with the lifecycle_state property of a OperationsInsightsPrivateEndpoint.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OperationsInsightsPrivateEndpoint.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OperationsInsightsPrivateEndpoint.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OperationsInsightsPrivateEndpoint.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OperationsInsightsPrivateEndpoint.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OperationsInsightsPrivateEndpoint.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a OperationsInsightsPrivateEndpoint.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new OperationsInsightsPrivateEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OperationsInsightsPrivateEndpoint.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this OperationsInsightsPrivateEndpoint.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OperationsInsightsPrivateEndpoint.
        :type compartment_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this OperationsInsightsPrivateEndpoint.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this OperationsInsightsPrivateEndpoint.
        :type subnet_id: str

        :param private_ip:
            The value to assign to the private_ip property of this OperationsInsightsPrivateEndpoint.
        :type private_ip: str

        :param description:
            The value to assign to the description property of this OperationsInsightsPrivateEndpoint.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this OperationsInsightsPrivateEndpoint.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OperationsInsightsPrivateEndpoint.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OperationsInsightsPrivateEndpoint.
        :type lifecycle_details: str

        :param private_endpoint_status_details:
            The value to assign to the private_endpoint_status_details property of this OperationsInsightsPrivateEndpoint.
        :type private_endpoint_status_details: str

        :param is_used_for_rac_dbs:
            The value to assign to the is_used_for_rac_dbs property of this OperationsInsightsPrivateEndpoint.
        :type is_used_for_rac_dbs: bool

        :param nsg_ids:
            The value to assign to the nsg_ids property of this OperationsInsightsPrivateEndpoint.
        :type nsg_ids: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OperationsInsightsPrivateEndpoint.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OperationsInsightsPrivateEndpoint.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OperationsInsightsPrivateEndpoint.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'private_ip': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'private_endpoint_status_details': 'str',
            'is_used_for_rac_dbs': 'bool',
            'nsg_ids': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'private_ip': 'privateIp',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'private_endpoint_status_details': 'privateEndpointStatusDetails',
            'is_used_for_rac_dbs': 'isUsedForRacDbs',
            'nsg_ids': 'nsgIds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._vcn_id = None
        self._subnet_id = None
        self._private_ip = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._private_endpoint_status_details = None
        self._is_used_for_rac_dbs = None
        self._nsg_ids = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OperationsInsightsPrivateEndpoint.
        The OCID of the Private service accessed database.


        :return: The id of this OperationsInsightsPrivateEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OperationsInsightsPrivateEndpoint.
        The OCID of the Private service accessed database.


        :param id: The id of this OperationsInsightsPrivateEndpoint.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OperationsInsightsPrivateEndpoint.
        The display name of the private endpoint.


        :return: The display_name of this OperationsInsightsPrivateEndpoint.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OperationsInsightsPrivateEndpoint.
        The display name of the private endpoint.


        :param display_name: The display_name of this OperationsInsightsPrivateEndpoint.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OperationsInsightsPrivateEndpoint.
        The compartment OCID of the Private service accessed database.


        :return: The compartment_id of this OperationsInsightsPrivateEndpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OperationsInsightsPrivateEndpoint.
        The compartment OCID of the Private service accessed database.


        :param compartment_id: The compartment_id of this OperationsInsightsPrivateEndpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this OperationsInsightsPrivateEndpoint.
        The OCID of the VCN.


        :return: The vcn_id of this OperationsInsightsPrivateEndpoint.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this OperationsInsightsPrivateEndpoint.
        The OCID of the VCN.


        :param vcn_id: The vcn_id of this OperationsInsightsPrivateEndpoint.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this OperationsInsightsPrivateEndpoint.
        The OCID of the subnet.


        :return: The subnet_id of this OperationsInsightsPrivateEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this OperationsInsightsPrivateEndpoint.
        The OCID of the subnet.


        :param subnet_id: The subnet_id of this OperationsInsightsPrivateEndpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_ip(self):
        """
        Gets the private_ip of this OperationsInsightsPrivateEndpoint.
        The private IP addresses assigned to the private endpoint. All IP addresses will be concatenated if it is RAC DBs.


        :return: The private_ip of this OperationsInsightsPrivateEndpoint.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this OperationsInsightsPrivateEndpoint.
        The private IP addresses assigned to the private endpoint. All IP addresses will be concatenated if it is RAC DBs.


        :param private_ip: The private_ip of this OperationsInsightsPrivateEndpoint.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def description(self):
        """
        Gets the description of this OperationsInsightsPrivateEndpoint.
        The description of the private endpoint.


        :return: The description of this OperationsInsightsPrivateEndpoint.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OperationsInsightsPrivateEndpoint.
        The description of the private endpoint.


        :param description: The description of this OperationsInsightsPrivateEndpoint.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this OperationsInsightsPrivateEndpoint.
        The date and time the private endpoint was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this OperationsInsightsPrivateEndpoint.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OperationsInsightsPrivateEndpoint.
        The date and time the private endpoint was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this OperationsInsightsPrivateEndpoint.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OperationsInsightsPrivateEndpoint.
        The current state of the private endpoint.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OperationsInsightsPrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OperationsInsightsPrivateEndpoint.
        The current state of the private endpoint.


        :param lifecycle_state: The lifecycle_state of this OperationsInsightsPrivateEndpoint.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this OperationsInsightsPrivateEndpoint.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this OperationsInsightsPrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this OperationsInsightsPrivateEndpoint.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this OperationsInsightsPrivateEndpoint.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def private_endpoint_status_details(self):
        """
        Gets the private_endpoint_status_details of this OperationsInsightsPrivateEndpoint.
        A message describing the status of the private endpoint connection of this resource. For example, it can be used to provide actionable information about the validity of the private endpoint connection.


        :return: The private_endpoint_status_details of this OperationsInsightsPrivateEndpoint.
        :rtype: str
        """
        return self._private_endpoint_status_details

    @private_endpoint_status_details.setter
    def private_endpoint_status_details(self, private_endpoint_status_details):
        """
        Sets the private_endpoint_status_details of this OperationsInsightsPrivateEndpoint.
        A message describing the status of the private endpoint connection of this resource. For example, it can be used to provide actionable information about the validity of the private endpoint connection.


        :param private_endpoint_status_details: The private_endpoint_status_details of this OperationsInsightsPrivateEndpoint.
        :type: str
        """
        self._private_endpoint_status_details = private_endpoint_status_details

    @property
    def is_used_for_rac_dbs(self):
        """
        Gets the is_used_for_rac_dbs of this OperationsInsightsPrivateEndpoint.
        The flag is to identify if private endpoint is used for rac database or not


        :return: The is_used_for_rac_dbs of this OperationsInsightsPrivateEndpoint.
        :rtype: bool
        """
        return self._is_used_for_rac_dbs

    @is_used_for_rac_dbs.setter
    def is_used_for_rac_dbs(self, is_used_for_rac_dbs):
        """
        Sets the is_used_for_rac_dbs of this OperationsInsightsPrivateEndpoint.
        The flag is to identify if private endpoint is used for rac database or not


        :param is_used_for_rac_dbs: The is_used_for_rac_dbs of this OperationsInsightsPrivateEndpoint.
        :type: bool
        """
        self._is_used_for_rac_dbs = is_used_for_rac_dbs

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this OperationsInsightsPrivateEndpoint.
        The OCIDs of the network security groups that the private endpoint belongs to.


        :return: The nsg_ids of this OperationsInsightsPrivateEndpoint.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this OperationsInsightsPrivateEndpoint.
        The OCIDs of the network security groups that the private endpoint belongs to.


        :param nsg_ids: The nsg_ids of this OperationsInsightsPrivateEndpoint.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OperationsInsightsPrivateEndpoint.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OperationsInsightsPrivateEndpoint.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OperationsInsightsPrivateEndpoint.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OperationsInsightsPrivateEndpoint.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OperationsInsightsPrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OperationsInsightsPrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OperationsInsightsPrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OperationsInsightsPrivateEndpoint.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OperationsInsightsPrivateEndpoint.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OperationsInsightsPrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OperationsInsightsPrivateEndpoint.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OperationsInsightsPrivateEndpoint.
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
