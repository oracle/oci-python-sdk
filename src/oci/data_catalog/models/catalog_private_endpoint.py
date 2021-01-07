# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CatalogPrivateEndpoint(object):
    """
    A private network reverse connection creates a connection from service to customer subnet over a private network.
    """

    #: A constant which can be used with the lifecycle_state property of a CatalogPrivateEndpoint.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a CatalogPrivateEndpoint.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CatalogPrivateEndpoint.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CatalogPrivateEndpoint.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CatalogPrivateEndpoint.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CatalogPrivateEndpoint.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a CatalogPrivateEndpoint.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a CatalogPrivateEndpoint.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new CatalogPrivateEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CatalogPrivateEndpoint.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CatalogPrivateEndpoint.
        :type compartment_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CatalogPrivateEndpoint.
        :type subnet_id: str

        :param display_name:
            The value to assign to the display_name property of this CatalogPrivateEndpoint.
        :type display_name: str

        :param dns_zones:
            The value to assign to the dns_zones property of this CatalogPrivateEndpoint.
        :type dns_zones: list[str]

        :param time_created:
            The value to assign to the time_created property of this CatalogPrivateEndpoint.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this CatalogPrivateEndpoint.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CatalogPrivateEndpoint.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CatalogPrivateEndpoint.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CatalogPrivateEndpoint.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this CatalogPrivateEndpoint.
        :type lifecycle_details: str

        :param attached_catalogs:
            The value to assign to the attached_catalogs property of this CatalogPrivateEndpoint.
        :type attached_catalogs: list[str]

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
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'attached_catalogs': 'list[str]'
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
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'attached_catalogs': 'attachedCatalogs'
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
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._attached_catalogs = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CatalogPrivateEndpoint.
        Unique identifier that is immutable


        :return: The id of this CatalogPrivateEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CatalogPrivateEndpoint.
        Unique identifier that is immutable


        :param id: The id of this CatalogPrivateEndpoint.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CatalogPrivateEndpoint.
        Compartment Identifier.


        :return: The compartment_id of this CatalogPrivateEndpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CatalogPrivateEndpoint.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this CatalogPrivateEndpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CatalogPrivateEndpoint.
        Subnet Identifier


        :return: The subnet_id of this CatalogPrivateEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CatalogPrivateEndpoint.
        Subnet Identifier


        :param subnet_id: The subnet_id of this CatalogPrivateEndpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CatalogPrivateEndpoint.
        Private Reverse Connection Endpoint display name


        :return: The display_name of this CatalogPrivateEndpoint.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CatalogPrivateEndpoint.
        Private Reverse Connection Endpoint display name


        :param display_name: The display_name of this CatalogPrivateEndpoint.
        :type: str
        """
        self._display_name = display_name

    @property
    def dns_zones(self):
        """
        **[Required]** Gets the dns_zones of this CatalogPrivateEndpoint.
        List of DNS zones to be used by the data assets to be harvested.
        Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com


        :return: The dns_zones of this CatalogPrivateEndpoint.
        :rtype: list[str]
        """
        return self._dns_zones

    @dns_zones.setter
    def dns_zones(self, dns_zones):
        """
        Sets the dns_zones of this CatalogPrivateEndpoint.
        List of DNS zones to be used by the data assets to be harvested.
        Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com


        :param dns_zones: The dns_zones of this CatalogPrivateEndpoint.
        :type: list[str]
        """
        self._dns_zones = dns_zones

    @property
    def time_created(self):
        """
        Gets the time_created of this CatalogPrivateEndpoint.
        The time the private endpoint was created. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CatalogPrivateEndpoint.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CatalogPrivateEndpoint.
        The time the private endpoint was created. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CatalogPrivateEndpoint.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this CatalogPrivateEndpoint.
        The time the private endpoint was updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this CatalogPrivateEndpoint.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this CatalogPrivateEndpoint.
        The time the private endpoint was updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this CatalogPrivateEndpoint.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CatalogPrivateEndpoint.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CatalogPrivateEndpoint.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CatalogPrivateEndpoint.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CatalogPrivateEndpoint.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CatalogPrivateEndpoint.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CatalogPrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CatalogPrivateEndpoint.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CatalogPrivateEndpoint.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CatalogPrivateEndpoint.
        The current state of the private endpoint resource.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CatalogPrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CatalogPrivateEndpoint.
        The current state of the private endpoint resource.


        :param lifecycle_state: The lifecycle_state of this CatalogPrivateEndpoint.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this CatalogPrivateEndpoint.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.


        :return: The lifecycle_details of this CatalogPrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this CatalogPrivateEndpoint.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.


        :param lifecycle_details: The lifecycle_details of this CatalogPrivateEndpoint.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def attached_catalogs(self):
        """
        Gets the attached_catalogs of this CatalogPrivateEndpoint.
        The list of catalogs using the private reverse connection endpoint


        :return: The attached_catalogs of this CatalogPrivateEndpoint.
        :rtype: list[str]
        """
        return self._attached_catalogs

    @attached_catalogs.setter
    def attached_catalogs(self, attached_catalogs):
        """
        Sets the attached_catalogs of this CatalogPrivateEndpoint.
        The list of catalogs using the private reverse connection endpoint


        :param attached_catalogs: The attached_catalogs of this CatalogPrivateEndpoint.
        :type: list[str]
        """
        self._attached_catalogs = attached_catalogs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
