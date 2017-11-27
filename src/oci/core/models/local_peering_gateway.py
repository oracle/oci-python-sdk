# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LocalPeeringGateway(object):

    def __init__(self, **kwargs):
        """
        Initializes a new LocalPeeringGateway object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this LocalPeeringGateway.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this LocalPeeringGateway.
        :type display_name: str

        :param id:
            The value to assign to the id property of this LocalPeeringGateway.
        :type id: str

        :param is_cross_tenancy_peering:
            The value to assign to the is_cross_tenancy_peering property of this LocalPeeringGateway.
        :type is_cross_tenancy_peering: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LocalPeeringGateway.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param peer_advertised_cidr:
            The value to assign to the peer_advertised_cidr property of this LocalPeeringGateway.
        :type peer_advertised_cidr: str

        :param peering_status:
            The value to assign to the peering_status property of this LocalPeeringGateway.
            Allowed values for this property are: "INVALID", "NEW", "PEERED", "PENDING", "REVOKED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
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
            'display_name': 'str',
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
            'display_name': 'displayName',
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
        self._display_name = None
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
        Gets the compartment_id of this LocalPeeringGateway.
        The OCID of the compartment containing the LPG.


        :return: The compartment_id of this LocalPeeringGateway.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LocalPeeringGateway.
        The OCID of the compartment containing the LPG.


        :param compartment_id: The compartment_id of this LocalPeeringGateway.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this LocalPeeringGateway.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :return: The display_name of this LocalPeeringGateway.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LocalPeeringGateway.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :param display_name: The display_name of this LocalPeeringGateway.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this LocalPeeringGateway.
        The LPG's Oracle ID (OCID).


        :return: The id of this LocalPeeringGateway.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LocalPeeringGateway.
        The LPG's Oracle ID (OCID).


        :param id: The id of this LocalPeeringGateway.
        :type: str
        """
        self._id = id

    @property
    def is_cross_tenancy_peering(self):
        """
        Gets the is_cross_tenancy_peering of this LocalPeeringGateway.
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
        Gets the lifecycle_state of this LocalPeeringGateway.
        The LPG's current lifecycle state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


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
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
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
        Gets the peering_status of this LocalPeeringGateway.
        Whether the LPG is peered with another LPG. `NEW` means the LPG has not yet been
        peered. `PENDING` means the peering is being established. `REVOKED` means the
        LPG at the other end of the peering has been deleted.

        Allowed values for this property are: "INVALID", "NEW", "PEERED", "PENDING", "REVOKED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


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
        if peering_status not in allowed_values:
            peering_status = 'UNKNOWN_ENUM_VALUE'
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
        Gets the time_created of this LocalPeeringGateway.
        The date and time the LPG was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this LocalPeeringGateway.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LocalPeeringGateway.
        The date and time the LPG was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this LocalPeeringGateway.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this LocalPeeringGateway.
        The OCID of the VCN the LPG belongs to.


        :return: The vcn_id of this LocalPeeringGateway.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this LocalPeeringGateway.
        The OCID of the VCN the LPG belongs to.


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
