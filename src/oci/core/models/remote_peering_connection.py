# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemotePeeringConnection(object):
    """
    A remote peering connection (RPC) is an object on a DRG that lets the VCN that is attached
    to the DRG peer with a VCN in a different region. *Peering* means that the two VCNs can
    communicate using private IP addresses, but without the traffic traversing the internet or
    routing through your on-premises network. For more information, see
    `VCN Peering`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/VCNpeering.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a RemotePeeringConnection.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a RemotePeeringConnection.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a RemotePeeringConnection.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a RemotePeeringConnection.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the peering_status property of a RemotePeeringConnection.
    #: This constant has a value of "INVALID"
    PEERING_STATUS_INVALID = "INVALID"

    #: A constant which can be used with the peering_status property of a RemotePeeringConnection.
    #: This constant has a value of "NEW"
    PEERING_STATUS_NEW = "NEW"

    #: A constant which can be used with the peering_status property of a RemotePeeringConnection.
    #: This constant has a value of "PENDING"
    PEERING_STATUS_PENDING = "PENDING"

    #: A constant which can be used with the peering_status property of a RemotePeeringConnection.
    #: This constant has a value of "PEERED"
    PEERING_STATUS_PEERED = "PEERED"

    #: A constant which can be used with the peering_status property of a RemotePeeringConnection.
    #: This constant has a value of "REVOKED"
    PEERING_STATUS_REVOKED = "REVOKED"

    def __init__(self, **kwargs):
        """
        Initializes a new RemotePeeringConnection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this RemotePeeringConnection.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this RemotePeeringConnection.
        :type display_name: str

        :param drg_id:
            The value to assign to the drg_id property of this RemotePeeringConnection.
        :type drg_id: str

        :param id:
            The value to assign to the id property of this RemotePeeringConnection.
        :type id: str

        :param is_cross_tenancy_peering:
            The value to assign to the is_cross_tenancy_peering property of this RemotePeeringConnection.
        :type is_cross_tenancy_peering: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RemotePeeringConnection.
            Allowed values for this property are: "AVAILABLE", "PROVISIONING", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param peer_id:
            The value to assign to the peer_id property of this RemotePeeringConnection.
        :type peer_id: str

        :param peer_region_name:
            The value to assign to the peer_region_name property of this RemotePeeringConnection.
        :type peer_region_name: str

        :param peer_tenancy_id:
            The value to assign to the peer_tenancy_id property of this RemotePeeringConnection.
        :type peer_tenancy_id: str

        :param peering_status:
            The value to assign to the peering_status property of this RemotePeeringConnection.
            Allowed values for this property are: "INVALID", "NEW", "PENDING", "PEERED", "REVOKED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type peering_status: str

        :param time_created:
            The value to assign to the time_created property of this RemotePeeringConnection.
        :type time_created: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'drg_id': 'str',
            'id': 'str',
            'is_cross_tenancy_peering': 'bool',
            'lifecycle_state': 'str',
            'peer_id': 'str',
            'peer_region_name': 'str',
            'peer_tenancy_id': 'str',
            'peering_status': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'drg_id': 'drgId',
            'id': 'id',
            'is_cross_tenancy_peering': 'isCrossTenancyPeering',
            'lifecycle_state': 'lifecycleState',
            'peer_id': 'peerId',
            'peer_region_name': 'peerRegionName',
            'peer_tenancy_id': 'peerTenancyId',
            'peering_status': 'peeringStatus',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._display_name = None
        self._drg_id = None
        self._id = None
        self._is_cross_tenancy_peering = None
        self._lifecycle_state = None
        self._peer_id = None
        self._peer_region_name = None
        self._peer_tenancy_id = None
        self._peering_status = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RemotePeeringConnection.
        The OCID of the compartment that contains the RPC.


        :return: The compartment_id of this RemotePeeringConnection.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RemotePeeringConnection.
        The OCID of the compartment that contains the RPC.


        :param compartment_id: The compartment_id of this RemotePeeringConnection.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this RemotePeeringConnection.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this RemotePeeringConnection.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RemotePeeringConnection.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this RemotePeeringConnection.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        **[Required]** Gets the drg_id of this RemotePeeringConnection.
        The OCID of the DRG that this RPC belongs to.


        :return: The drg_id of this RemotePeeringConnection.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this RemotePeeringConnection.
        The OCID of the DRG that this RPC belongs to.


        :param drg_id: The drg_id of this RemotePeeringConnection.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RemotePeeringConnection.
        The OCID of the RPC.


        :return: The id of this RemotePeeringConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RemotePeeringConnection.
        The OCID of the RPC.


        :param id: The id of this RemotePeeringConnection.
        :type: str
        """
        self._id = id

    @property
    def is_cross_tenancy_peering(self):
        """
        **[Required]** Gets the is_cross_tenancy_peering of this RemotePeeringConnection.
        Whether the VCN at the other end of the peering is in a different tenancy.

        Example: `false`


        :return: The is_cross_tenancy_peering of this RemotePeeringConnection.
        :rtype: bool
        """
        return self._is_cross_tenancy_peering

    @is_cross_tenancy_peering.setter
    def is_cross_tenancy_peering(self, is_cross_tenancy_peering):
        """
        Sets the is_cross_tenancy_peering of this RemotePeeringConnection.
        Whether the VCN at the other end of the peering is in a different tenancy.

        Example: `false`


        :param is_cross_tenancy_peering: The is_cross_tenancy_peering of this RemotePeeringConnection.
        :type: bool
        """
        self._is_cross_tenancy_peering = is_cross_tenancy_peering

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this RemotePeeringConnection.
        The RPC's current lifecycle state.

        Allowed values for this property are: "AVAILABLE", "PROVISIONING", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RemotePeeringConnection.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RemotePeeringConnection.
        The RPC's current lifecycle state.


        :param lifecycle_state: The lifecycle_state of this RemotePeeringConnection.
        :type: str
        """
        allowed_values = ["AVAILABLE", "PROVISIONING", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def peer_id(self):
        """
        Gets the peer_id of this RemotePeeringConnection.
        If this RPC is peered, this value is the OCID of the other RPC.


        :return: The peer_id of this RemotePeeringConnection.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """
        Sets the peer_id of this RemotePeeringConnection.
        If this RPC is peered, this value is the OCID of the other RPC.


        :param peer_id: The peer_id of this RemotePeeringConnection.
        :type: str
        """
        self._peer_id = peer_id

    @property
    def peer_region_name(self):
        """
        Gets the peer_region_name of this RemotePeeringConnection.
        If this RPC is peered, this value is the region that contains the other RPC.

        Example: `us-ashburn-1`


        :return: The peer_region_name of this RemotePeeringConnection.
        :rtype: str
        """
        return self._peer_region_name

    @peer_region_name.setter
    def peer_region_name(self, peer_region_name):
        """
        Sets the peer_region_name of this RemotePeeringConnection.
        If this RPC is peered, this value is the region that contains the other RPC.

        Example: `us-ashburn-1`


        :param peer_region_name: The peer_region_name of this RemotePeeringConnection.
        :type: str
        """
        self._peer_region_name = peer_region_name

    @property
    def peer_tenancy_id(self):
        """
        Gets the peer_tenancy_id of this RemotePeeringConnection.
        If this RPC is peered, this value is the OCID of the other RPC's tenancy.


        :return: The peer_tenancy_id of this RemotePeeringConnection.
        :rtype: str
        """
        return self._peer_tenancy_id

    @peer_tenancy_id.setter
    def peer_tenancy_id(self, peer_tenancy_id):
        """
        Sets the peer_tenancy_id of this RemotePeeringConnection.
        If this RPC is peered, this value is the OCID of the other RPC's tenancy.


        :param peer_tenancy_id: The peer_tenancy_id of this RemotePeeringConnection.
        :type: str
        """
        self._peer_tenancy_id = peer_tenancy_id

    @property
    def peering_status(self):
        """
        **[Required]** Gets the peering_status of this RemotePeeringConnection.
        Whether the RPC is peered with another RPC. `NEW` means the RPC has not yet been
        peered. `PENDING` means the peering is being established. `REVOKED` means the
        RPC at the other end of the peering has been deleted.

        Allowed values for this property are: "INVALID", "NEW", "PENDING", "PEERED", "REVOKED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The peering_status of this RemotePeeringConnection.
        :rtype: str
        """
        return self._peering_status

    @peering_status.setter
    def peering_status(self, peering_status):
        """
        Sets the peering_status of this RemotePeeringConnection.
        Whether the RPC is peered with another RPC. `NEW` means the RPC has not yet been
        peered. `PENDING` means the peering is being established. `REVOKED` means the
        RPC at the other end of the peering has been deleted.


        :param peering_status: The peering_status of this RemotePeeringConnection.
        :type: str
        """
        allowed_values = ["INVALID", "NEW", "PENDING", "PEERED", "REVOKED"]
        if not value_allowed_none_or_none_sentinel(peering_status, allowed_values):
            peering_status = 'UNKNOWN_ENUM_VALUE'
        self._peering_status = peering_status

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this RemotePeeringConnection.
        The date and time the RPC was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this RemotePeeringConnection.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RemotePeeringConnection.
        The date and time the RPC was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this RemotePeeringConnection.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
