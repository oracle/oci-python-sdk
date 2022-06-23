# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LocalPeeringGateway(object):
    """
    A local peering gateway (LPG) is an object on a VCN that lets that VCN peer
    with another VCN in the same region. *Peering* means that the two VCNs can
    communicate using private IP addresses, but without the traffic traversing the
    internet or routing through your on-premises network. For more information,
    see `VCN Peering`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/VCNpeering.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a LocalPeeringGateway.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a LocalPeeringGateway.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a LocalPeeringGateway.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a LocalPeeringGateway.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the peering_status property of a LocalPeeringGateway.
    #: This constant has a value of "INVALID"
    PEERING_STATUS_INVALID = "INVALID"

    #: A constant which can be used with the peering_status property of a LocalPeeringGateway.
    #: This constant has a value of "NEW"
    PEERING_STATUS_NEW = "NEW"

    #: A constant which can be used with the peering_status property of a LocalPeeringGateway.
    #: This constant has a value of "PEERED"
    PEERING_STATUS_PEERED = "PEERED"

    #: A constant which can be used with the peering_status property of a LocalPeeringGateway.
    #: This constant has a value of "PENDING"
    PEERING_STATUS_PENDING = "PENDING"

    #: A constant which can be used with the peering_status property of a LocalPeeringGateway.
    #: This constant has a value of "REVOKED"
    PEERING_STATUS_REVOKED = "REVOKED"

    def __init__(self, **kwargs):
        """
        Initializes a new LocalPeeringGateway object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this LocalPeeringGateway.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this LocalPeeringGateway.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this LocalPeeringGateway.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LocalPeeringGateway.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this LocalPeeringGateway.
        :type id: str

        :param is_cross_tenancy_peering:
            The value to assign to the is_cross_tenancy_peering property of this LocalPeeringGateway.
        :type is_cross_tenancy_peering: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LocalPeeringGateway.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"
        :type lifecycle_state: str

        :param peer_advertised_cidr:
            The value to assign to the peer_advertised_cidr property of this LocalPeeringGateway.
        :type peer_advertised_cidr: str

        :param peering_status:
            The value to assign to the peering_status property of this LocalPeeringGateway.
            Allowed values for this property are: "INVALID", "NEW", "PEERED", "PENDING", "REVOKED"
        :type peering_status: str

        :param peering_status_details:
            The value to assign to the peering_status_details property of this LocalPeeringGateway.
        :type peering_status_details: str

        :param time_created:
            The value to assign to the time_created property of this LocalPeeringGateway.
        :type time_created: datetime

        :param vcn_id:
            The value to assign to the vcn_id property of this LocalPeeringGateway.
        :type vcn_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'is_cross_tenancy_peering': 'bool',
            'lifecycle_state': 'str',
            'peer_advertised_cidr': 'str',
            'peering_status': 'str',
            'peering_status_details': 'str',
            'time_created': 'datetime',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'is_cross_tenancy_peering': 'isCrossTenancyPeering',
            'lifecycle_state': 'lifecycleState',
            'peer_advertised_cidr': 'peerAdvertisedCidr',
            'peering_status': 'peeringStatus',
            'peering_status_details': 'peeringStatusDetails',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._is_cross_tenancy_peering = None
        self._lifecycle_state = None
        self._peer_advertised_cidr = None
        self._peering_status = None
        self._peering_status_details = None
        self._time_created = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LocalPeeringGateway.
        The `OCID`__ of the compartment containing the LPG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this LocalPeeringGateway.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LocalPeeringGateway.
        The `OCID`__ of the compartment containing the LPG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this LocalPeeringGateway.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this LocalPeeringGateway.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this LocalPeeringGateway.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this LocalPeeringGateway.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this LocalPeeringGateway.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this LocalPeeringGateway.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this LocalPeeringGateway.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LocalPeeringGateway.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this LocalPeeringGateway.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this LocalPeeringGateway.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this LocalPeeringGateway.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this LocalPeeringGateway.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this LocalPeeringGateway.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this LocalPeeringGateway.
        The LPG's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this LocalPeeringGateway.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LocalPeeringGateway.
        The LPG's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this LocalPeeringGateway.
        :type: str
        """
        self._id = id

    @property
    def is_cross_tenancy_peering(self):
        """
        **[Required]** Gets the is_cross_tenancy_peering of this LocalPeeringGateway.
        Whether the VCN at the other end of the peering is in a different tenancy.

        Example: `false`


        :return: The is_cross_tenancy_peering of this LocalPeeringGateway.
        :rtype: bool
        """
        return self._is_cross_tenancy_peering

    @is_cross_tenancy_peering.setter
    def is_cross_tenancy_peering(self, is_cross_tenancy_peering):
        """
        Sets the is_cross_tenancy_peering of this LocalPeeringGateway.
        Whether the VCN at the other end of the peering is in a different tenancy.

        Example: `false`


        :param is_cross_tenancy_peering: The is_cross_tenancy_peering of this LocalPeeringGateway.
        :type: bool
        """
        self._is_cross_tenancy_peering = is_cross_tenancy_peering

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this LocalPeeringGateway.
        The LPG's current lifecycle state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"


        :return: The lifecycle_state of this LocalPeeringGateway.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LocalPeeringGateway.
        The LPG's current lifecycle state.


        :param lifecycle_state: The lifecycle_state of this LocalPeeringGateway.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def peer_advertised_cidr(self):
        """
        Gets the peer_advertised_cidr of this LocalPeeringGateway.
        The range of IP addresses available on the VCN at the other
        end of the peering from this LPG. The value is `null` if the LPG is not peered.
        You can use this as the destination CIDR for a route rule to route a subnet's
        traffic to this LPG.

        Example: `192.168.0.0/16`


        :return: The peer_advertised_cidr of this LocalPeeringGateway.
        :rtype: str
        """
        return self._peer_advertised_cidr

    @peer_advertised_cidr.setter
    def peer_advertised_cidr(self, peer_advertised_cidr):
        """
        Sets the peer_advertised_cidr of this LocalPeeringGateway.
        The range of IP addresses available on the VCN at the other
        end of the peering from this LPG. The value is `null` if the LPG is not peered.
        You can use this as the destination CIDR for a route rule to route a subnet's
        traffic to this LPG.

        Example: `192.168.0.0/16`


        :param peer_advertised_cidr: The peer_advertised_cidr of this LocalPeeringGateway.
        :type: str
        """
        self._peer_advertised_cidr = peer_advertised_cidr

    @property
    def peering_status(self):
        """
        **[Required]** Gets the peering_status of this LocalPeeringGateway.
        Whether the LPG is peered with another LPG. `NEW` means the LPG has not yet been
        peered. `PENDING` means the peering is being established. `REVOKED` means the
        LPG at the other end of the peering has been deleted.

        Allowed values for this property are: "INVALID", "NEW", "PEERED", "PENDING", "REVOKED"


        :return: The peering_status of this LocalPeeringGateway.
        :rtype: str
        """
        return self._peering_status

    @peering_status.setter
    def peering_status(self, peering_status):
        """
        Sets the peering_status of this LocalPeeringGateway.
        Whether the LPG is peered with another LPG. `NEW` means the LPG has not yet been
        peered. `PENDING` means the peering is being established. `REVOKED` means the
        LPG at the other end of the peering has been deleted.


        :param peering_status: The peering_status of this LocalPeeringGateway.
        :type: str
        """
        allowed_values = ["INVALID", "NEW", "PEERED", "PENDING", "REVOKED"]
        if not value_allowed_none_or_none_sentinel(peering_status, allowed_values):
            raise ValueError(
                "Invalid value for `peering_status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._peering_status = peering_status

    @property
    def peering_status_details(self):
        """
        Gets the peering_status_details of this LocalPeeringGateway.
        Additional information regarding the peering status, if applicable.


        :return: The peering_status_details of this LocalPeeringGateway.
        :rtype: str
        """
        return self._peering_status_details

    @peering_status_details.setter
    def peering_status_details(self, peering_status_details):
        """
        Sets the peering_status_details of this LocalPeeringGateway.
        Additional information regarding the peering status, if applicable.


        :param peering_status_details: The peering_status_details of this LocalPeeringGateway.
        :type: str
        """
        self._peering_status_details = peering_status_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this LocalPeeringGateway.
        The date and time the LPG was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this LocalPeeringGateway.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LocalPeeringGateway.
        The date and time the LPG was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this LocalPeeringGateway.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this LocalPeeringGateway.
        The `OCID`__ of the VCN that uses the LPG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this LocalPeeringGateway.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this LocalPeeringGateway.
        The `OCID`__ of the VCN that uses the LPG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this LocalPeeringGateway.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
