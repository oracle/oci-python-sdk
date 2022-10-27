# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection import Connection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GoldenGateConnection(Connection):
    """
    Represents the metadata of a GoldenGate Connection.
    """

    #: A constant which can be used with the technology_type property of a GoldenGateConnection.
    #: This constant has a value of "GOLDENGATE"
    TECHNOLOGY_TYPE_GOLDENGATE = "GOLDENGATE"

    def __init__(self, **kwargs):
        """
        Initializes a new GoldenGateConnection object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.GoldenGateConnection.connection_type` attribute
        of this class is ``GOLDENGATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this GoldenGateConnection.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        :param id:
            The value to assign to the id property of this GoldenGateConnection.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this GoldenGateConnection.
        :type display_name: str

        :param description:
            The value to assign to the description property of this GoldenGateConnection.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this GoldenGateConnection.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this GoldenGateConnection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this GoldenGateConnection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this GoldenGateConnection.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this GoldenGateConnection.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this GoldenGateConnection.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this GoldenGateConnection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this GoldenGateConnection.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this GoldenGateConnection.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this GoldenGateConnection.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this GoldenGateConnection.
        :type subnet_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this GoldenGateConnection.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this GoldenGateConnection.
        :type nsg_ids: list[str]

        :param technology_type:
            The value to assign to the technology_type property of this GoldenGateConnection.
            Allowed values for this property are: "GOLDENGATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type technology_type: str

        :param deployment_id:
            The value to assign to the deployment_id property of this GoldenGateConnection.
        :type deployment_id: str

        :param host:
            The value to assign to the host property of this GoldenGateConnection.
        :type host: str

        :param port:
            The value to assign to the port property of this GoldenGateConnection.
        :type port: int

        :param private_ip:
            The value to assign to the private_ip property of this GoldenGateConnection.
        :type private_ip: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'vault_id': 'str',
            'key_id': 'str',
            'subnet_id': 'str',
            'ingress_ips': 'list[IngressIpDetails]',
            'nsg_ids': 'list[str]',
            'technology_type': 'str',
            'deployment_id': 'str',
            'host': 'str',
            'port': 'int',
            'private_ip': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'subnet_id': 'subnetId',
            'ingress_ips': 'ingressIps',
            'nsg_ids': 'nsgIds',
            'technology_type': 'technologyType',
            'deployment_id': 'deploymentId',
            'host': 'host',
            'port': 'port',
            'private_ip': 'privateIp'
        }

        self._connection_type = None
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._vault_id = None
        self._key_id = None
        self._subnet_id = None
        self._ingress_ips = None
        self._nsg_ids = None
        self._technology_type = None
        self._deployment_id = None
        self._host = None
        self._port = None
        self._private_ip = None
        self._connection_type = 'GOLDENGATE'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this GoldenGateConnection.
        The GoldenGate technology type.

        Allowed values for this property are: "GOLDENGATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The technology_type of this GoldenGateConnection.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this GoldenGateConnection.
        The GoldenGate technology type.


        :param technology_type: The technology_type of this GoldenGateConnection.
        :type: str
        """
        allowed_values = ["GOLDENGATE"]
        if not value_allowed_none_or_none_sentinel(technology_type, allowed_values):
            technology_type = 'UNKNOWN_ENUM_VALUE'
        self._technology_type = technology_type

    @property
    def deployment_id(self):
        """
        Gets the deployment_id of this GoldenGateConnection.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The deployment_id of this GoldenGateConnection.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """
        Sets the deployment_id of this GoldenGateConnection.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param deployment_id: The deployment_id of this GoldenGateConnection.
        :type: str
        """
        self._deployment_id = deployment_id

    @property
    def host(self):
        """
        Gets the host of this GoldenGateConnection.
        The name or address of a host.


        :return: The host of this GoldenGateConnection.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this GoldenGateConnection.
        The name or address of a host.


        :param host: The host of this GoldenGateConnection.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this GoldenGateConnection.
        The port of an endpoint usually specified for a connection.


        :return: The port of this GoldenGateConnection.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this GoldenGateConnection.
        The port of an endpoint usually specified for a connection.


        :param port: The port of this GoldenGateConnection.
        :type: int
        """
        self._port = port

    @property
    def private_ip(self):
        """
        Gets the private_ip of this GoldenGateConnection.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :return: The private_ip of this GoldenGateConnection.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this GoldenGateConnection.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :param private_ip: The private_ip of this GoldenGateConnection.
        :type: str
        """
        self._private_ip = private_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
