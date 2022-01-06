# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateEndpoint(object):
    """
    A Data Flow private endpoint object.
    """

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a PrivateEndpoint.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this PrivateEndpoint.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this PrivateEndpoint.
        :type defined_tags: dict(str, dict(str, object))

        :param description:
            The value to assign to the description property of this PrivateEndpoint.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this PrivateEndpoint.
        :type display_name: str

        :param dns_zones:
            The value to assign to the dns_zones property of this PrivateEndpoint.
        :type dns_zones: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PrivateEndpoint.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this PrivateEndpoint.
        :type id: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this PrivateEndpoint.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PrivateEndpoint.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param max_host_count:
            The value to assign to the max_host_count property of this PrivateEndpoint.
        :type max_host_count: int

        :param nsg_ids:
            The value to assign to the nsg_ids property of this PrivateEndpoint.
        :type nsg_ids: list[str]

        :param owner_principal_id:
            The value to assign to the owner_principal_id property of this PrivateEndpoint.
        :type owner_principal_id: str

        :param owner_user_name:
            The value to assign to the owner_user_name property of this PrivateEndpoint.
        :type owner_user_name: str

        :param subnet_id:
            The value to assign to the subnet_id property of this PrivateEndpoint.
        :type subnet_id: str

        :param time_created:
            The value to assign to the time_created property of this PrivateEndpoint.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this PrivateEndpoint.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'description': 'str',
            'display_name': 'str',
            'dns_zones': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'max_host_count': 'int',
            'nsg_ids': 'list[str]',
            'owner_principal_id': 'str',
            'owner_user_name': 'str',
            'subnet_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'description': 'description',
            'display_name': 'displayName',
            'dns_zones': 'dnsZones',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'max_host_count': 'maxHostCount',
            'nsg_ids': 'nsgIds',
            'owner_principal_id': 'ownerPrincipalId',
            'owner_user_name': 'ownerUserName',
            'subnet_id': 'subnetId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._description = None
        self._display_name = None
        self._dns_zones = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._max_host_count = None
        self._nsg_ids = None
        self._owner_principal_id = None
        self._owner_user_name = None
        self._subnet_id = None
        self._time_created = None
        self._time_updated = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PrivateEndpoint.
        The OCID of a compartment.


        :return: The compartment_id of this PrivateEndpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PrivateEndpoint.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this PrivateEndpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this PrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this PrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this PrivateEndpoint.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def description(self):
        """
        Gets the description of this PrivateEndpoint.
        A user-friendly description. Avoid entering confidential information.


        :return: The description of this PrivateEndpoint.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PrivateEndpoint.
        A user-friendly description. Avoid entering confidential information.


        :param description: The description of this PrivateEndpoint.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this PrivateEndpoint.
        A user-friendly name. It does not have to be unique. Avoid entering confidential information.


        :return: The display_name of this PrivateEndpoint.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PrivateEndpoint.
        A user-friendly name. It does not have to be unique. Avoid entering confidential information.


        :param display_name: The display_name of this PrivateEndpoint.
        :type: str
        """
        self._display_name = display_name

    @property
    def dns_zones(self):
        """
        **[Required]** Gets the dns_zones of this PrivateEndpoint.
        An array of DNS zone names.
        Example: `[ \"app.examplecorp.com\", \"app.examplecorp2.com\" ]`


        :return: The dns_zones of this PrivateEndpoint.
        :rtype: list[str]
        """
        return self._dns_zones

    @dns_zones.setter
    def dns_zones(self, dns_zones):
        """
        Sets the dns_zones of this PrivateEndpoint.
        An array of DNS zone names.
        Example: `[ \"app.examplecorp.com\", \"app.examplecorp2.com\" ]`


        :param dns_zones: The dns_zones of this PrivateEndpoint.
        :type: list[str]
        """
        self._dns_zones = dns_zones

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this PrivateEndpoint.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this PrivateEndpoint.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PrivateEndpoint.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this PrivateEndpoint.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PrivateEndpoint.
        The OCID of a private endpoint.


        :return: The id of this PrivateEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PrivateEndpoint.
        The OCID of a private endpoint.


        :param id: The id of this PrivateEndpoint.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this PrivateEndpoint.
        The detailed messages about the lifecycle state.


        :return: The lifecycle_details of this PrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this PrivateEndpoint.
        The detailed messages about the lifecycle state.


        :param lifecycle_details: The lifecycle_details of this PrivateEndpoint.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PrivateEndpoint.
        The current state of this private endpoint.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PrivateEndpoint.
        The current state of this private endpoint.


        :param lifecycle_state: The lifecycle_state of this PrivateEndpoint.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def max_host_count(self):
        """
        Gets the max_host_count of this PrivateEndpoint.
        The maximum number of hosts to be accessed through the private endpoint. This value is used
        to calculate the relevant CIDR block and should be a multiple of 256.  If the value is not a
        multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up
        to 512.


        :return: The max_host_count of this PrivateEndpoint.
        :rtype: int
        """
        return self._max_host_count

    @max_host_count.setter
    def max_host_count(self, max_host_count):
        """
        Sets the max_host_count of this PrivateEndpoint.
        The maximum number of hosts to be accessed through the private endpoint. This value is used
        to calculate the relevant CIDR block and should be a multiple of 256.  If the value is not a
        multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up
        to 512.


        :param max_host_count: The max_host_count of this PrivateEndpoint.
        :type: int
        """
        self._max_host_count = max_host_count

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this PrivateEndpoint.
        An array of network security group OCIDs.


        :return: The nsg_ids of this PrivateEndpoint.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this PrivateEndpoint.
        An array of network security group OCIDs.


        :param nsg_ids: The nsg_ids of this PrivateEndpoint.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def owner_principal_id(self):
        """
        **[Required]** Gets the owner_principal_id of this PrivateEndpoint.
        The OCID of the user who created the resource.


        :return: The owner_principal_id of this PrivateEndpoint.
        :rtype: str
        """
        return self._owner_principal_id

    @owner_principal_id.setter
    def owner_principal_id(self, owner_principal_id):
        """
        Sets the owner_principal_id of this PrivateEndpoint.
        The OCID of the user who created the resource.


        :param owner_principal_id: The owner_principal_id of this PrivateEndpoint.
        :type: str
        """
        self._owner_principal_id = owner_principal_id

    @property
    def owner_user_name(self):
        """
        Gets the owner_user_name of this PrivateEndpoint.
        The username of the user who created the resource.  If the username of the owner does not exist,
        `null` will be returned and the caller should refer to the ownerPrincipalId value instead.


        :return: The owner_user_name of this PrivateEndpoint.
        :rtype: str
        """
        return self._owner_user_name

    @owner_user_name.setter
    def owner_user_name(self, owner_user_name):
        """
        Sets the owner_user_name of this PrivateEndpoint.
        The username of the user who created the resource.  If the username of the owner does not exist,
        `null` will be returned and the caller should refer to the ownerPrincipalId value instead.


        :param owner_user_name: The owner_user_name of this PrivateEndpoint.
        :type: str
        """
        self._owner_user_name = owner_user_name

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this PrivateEndpoint.
        The OCID of a subnet.


        :return: The subnet_id of this PrivateEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this PrivateEndpoint.
        The OCID of a subnet.


        :param subnet_id: The subnet_id of this PrivateEndpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PrivateEndpoint.
        The date and time a application was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this PrivateEndpoint.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PrivateEndpoint.
        The date and time a application was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this PrivateEndpoint.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this PrivateEndpoint.
        The date and time a application was updated, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this PrivateEndpoint.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this PrivateEndpoint.
        The date and time a application was updated, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this PrivateEndpoint.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
