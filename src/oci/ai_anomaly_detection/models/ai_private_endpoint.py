# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AiPrivateEndpoint(object):
    """
    A private network reverse connection creates a connection from service to customer subnet over a private network.
    """

    #: A constant which can be used with the lifecycle_state property of a AiPrivateEndpoint.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AiPrivateEndpoint.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AiPrivateEndpoint.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AiPrivateEndpoint.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AiPrivateEndpoint.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AiPrivateEndpoint.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AiPrivateEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AiPrivateEndpoint.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AiPrivateEndpoint.
        :type compartment_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this AiPrivateEndpoint.
        :type subnet_id: str

        :param display_name:
            The value to assign to the display_name property of this AiPrivateEndpoint.
        :type display_name: str

        :param dns_zones:
            The value to assign to the dns_zones property of this AiPrivateEndpoint.
        :type dns_zones: list[str]

        :param time_created:
            The value to assign to the time_created property of this AiPrivateEndpoint.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AiPrivateEndpoint.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AiPrivateEndpoint.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AiPrivateEndpoint.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AiPrivateEndpoint.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AiPrivateEndpoint.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AiPrivateEndpoint.
        :type lifecycle_details: str

        :param attached_data_assets:
            The value to assign to the attached_data_assets property of this AiPrivateEndpoint.
        :type attached_data_assets: list[str]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'subnet_id': 'str',
            'display_name': 'str',
            'dns_zones': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'attached_data_assets': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'subnet_id': 'subnetId',
            'display_name': 'displayName',
            'dns_zones': 'dnsZones',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'attached_data_assets': 'attachedDataAssets'
        }

        self._id = None
        self._compartment_id = None
        self._subnet_id = None
        self._display_name = None
        self._dns_zones = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._attached_data_assets = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AiPrivateEndpoint.
        Unique identifier that is immutable.


        :return: The id of this AiPrivateEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AiPrivateEndpoint.
        Unique identifier that is immutable.


        :param id: The id of this AiPrivateEndpoint.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AiPrivateEndpoint.
        Compartment Identifier.


        :return: The compartment_id of this AiPrivateEndpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AiPrivateEndpoint.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this AiPrivateEndpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this AiPrivateEndpoint.
        Subnet Identifier


        :return: The subnet_id of this AiPrivateEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this AiPrivateEndpoint.
        Subnet Identifier


        :param subnet_id: The subnet_id of this AiPrivateEndpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def display_name(self):
        """
        Gets the display_name of this AiPrivateEndpoint.
        Private Reverse Connection Endpoint display name.


        :return: The display_name of this AiPrivateEndpoint.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AiPrivateEndpoint.
        Private Reverse Connection Endpoint display name.


        :param display_name: The display_name of this AiPrivateEndpoint.
        :type: str
        """
        self._display_name = display_name

    @property
    def dns_zones(self):
        """
        **[Required]** Gets the dns_zones of this AiPrivateEndpoint.
        List of DNS zones to be used by the data assets.
        Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com


        :return: The dns_zones of this AiPrivateEndpoint.
        :rtype: list[str]
        """
        return self._dns_zones

    @dns_zones.setter
    def dns_zones(self, dns_zones):
        """
        Sets the dns_zones of this AiPrivateEndpoint.
        List of DNS zones to be used by the data assets.
        Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com


        :param dns_zones: The dns_zones of this AiPrivateEndpoint.
        :type: list[str]
        """
        self._dns_zones = dns_zones

    @property
    def time_created(self):
        """
        Gets the time_created of this AiPrivateEndpoint.
        The time the private endpoint was created. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this AiPrivateEndpoint.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AiPrivateEndpoint.
        The time the private endpoint was created. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this AiPrivateEndpoint.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this AiPrivateEndpoint.
        The time the private endpoint was updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this AiPrivateEndpoint.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AiPrivateEndpoint.
        The time the private endpoint was updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this AiPrivateEndpoint.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AiPrivateEndpoint.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this AiPrivateEndpoint.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AiPrivateEndpoint.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this AiPrivateEndpoint.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AiPrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this AiPrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AiPrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this AiPrivateEndpoint.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AiPrivateEndpoint.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this AiPrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AiPrivateEndpoint.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this AiPrivateEndpoint.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AiPrivateEndpoint.
        The current state of the private endpoint resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AiPrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AiPrivateEndpoint.
        The current state of the private endpoint resource.


        :param lifecycle_state: The lifecycle_state of this AiPrivateEndpoint.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AiPrivateEndpoint.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.


        :return: The lifecycle_details of this AiPrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AiPrivateEndpoint.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.


        :param lifecycle_details: The lifecycle_details of this AiPrivateEndpoint.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def attached_data_assets(self):
        """
        Gets the attached_data_assets of this AiPrivateEndpoint.
        The list of dataAssets using the private reverse connection endpoint.


        :return: The attached_data_assets of this AiPrivateEndpoint.
        :rtype: list[str]
        """
        return self._attached_data_assets

    @attached_data_assets.setter
    def attached_data_assets(self, attached_data_assets):
        """
        Sets the attached_data_assets of this AiPrivateEndpoint.
        The list of dataAssets using the private reverse connection endpoint.


        :param attached_data_assets: The attached_data_assets of this AiPrivateEndpoint.
        :type: list[str]
        """
        self._attached_data_assets = attached_data_assets

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
