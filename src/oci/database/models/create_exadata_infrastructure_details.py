# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateExadataInfrastructureDetails(object):
    """
    Request to create Exadata infrastructure resource. Applies to Exadata Cloud@Customer instances only.
    See :func:`create_cloud_exadata_infrastructure_details` for information on creating a cloud Exadata infrastructure resource in an Exadata Cloud Service instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateExadataInfrastructureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateExadataInfrastructureDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateExadataInfrastructureDetails.
        :type display_name: str

        :param shape:
            The value to assign to the shape property of this CreateExadataInfrastructureDetails.
        :type shape: str

        :param time_zone:
            The value to assign to the time_zone property of this CreateExadataInfrastructureDetails.
        :type time_zone: str

        :param cloud_control_plane_server1:
            The value to assign to the cloud_control_plane_server1 property of this CreateExadataInfrastructureDetails.
        :type cloud_control_plane_server1: str

        :param cloud_control_plane_server2:
            The value to assign to the cloud_control_plane_server2 property of this CreateExadataInfrastructureDetails.
        :type cloud_control_plane_server2: str

        :param netmask:
            The value to assign to the netmask property of this CreateExadataInfrastructureDetails.
        :type netmask: str

        :param gateway:
            The value to assign to the gateway property of this CreateExadataInfrastructureDetails.
        :type gateway: str

        :param admin_network_cidr:
            The value to assign to the admin_network_cidr property of this CreateExadataInfrastructureDetails.
        :type admin_network_cidr: str

        :param infini_band_network_cidr:
            The value to assign to the infini_band_network_cidr property of this CreateExadataInfrastructureDetails.
        :type infini_band_network_cidr: str

        :param corporate_proxy:
            The value to assign to the corporate_proxy property of this CreateExadataInfrastructureDetails.
        :type corporate_proxy: str

        :param contacts:
            The value to assign to the contacts property of this CreateExadataInfrastructureDetails.
        :type contacts: list[oci.database.models.ExadataInfrastructureContact]

        :param maintenance_window:
            The value to assign to the maintenance_window property of this CreateExadataInfrastructureDetails.
        :type maintenance_window: oci.database.models.MaintenanceWindow

        :param storage_count:
            The value to assign to the storage_count property of this CreateExadataInfrastructureDetails.
        :type storage_count: int

        :param compute_count:
            The value to assign to the compute_count property of this CreateExadataInfrastructureDetails.
        :type compute_count: int

        :param dns_server:
            The value to assign to the dns_server property of this CreateExadataInfrastructureDetails.
        :type dns_server: list[str]

        :param ntp_server:
            The value to assign to the ntp_server property of this CreateExadataInfrastructureDetails.
        :type ntp_server: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateExadataInfrastructureDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateExadataInfrastructureDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'shape': 'str',
            'time_zone': 'str',
            'cloud_control_plane_server1': 'str',
            'cloud_control_plane_server2': 'str',
            'netmask': 'str',
            'gateway': 'str',
            'admin_network_cidr': 'str',
            'infini_band_network_cidr': 'str',
            'corporate_proxy': 'str',
            'contacts': 'list[ExadataInfrastructureContact]',
            'maintenance_window': 'MaintenanceWindow',
            'storage_count': 'int',
            'compute_count': 'int',
            'dns_server': 'list[str]',
            'ntp_server': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'shape': 'shape',
            'time_zone': 'timeZone',
            'cloud_control_plane_server1': 'cloudControlPlaneServer1',
            'cloud_control_plane_server2': 'cloudControlPlaneServer2',
            'netmask': 'netmask',
            'gateway': 'gateway',
            'admin_network_cidr': 'adminNetworkCIDR',
            'infini_band_network_cidr': 'infiniBandNetworkCIDR',
            'corporate_proxy': 'corporateProxy',
            'contacts': 'contacts',
            'maintenance_window': 'maintenanceWindow',
            'storage_count': 'storageCount',
            'compute_count': 'computeCount',
            'dns_server': 'dnsServer',
            'ntp_server': 'ntpServer',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._shape = None
        self._time_zone = None
        self._cloud_control_plane_server1 = None
        self._cloud_control_plane_server2 = None
        self._netmask = None
        self._gateway = None
        self._admin_network_cidr = None
        self._infini_band_network_cidr = None
        self._corporate_proxy = None
        self._contacts = None
        self._maintenance_window = None
        self._storage_count = None
        self._compute_count = None
        self._dns_server = None
        self._ntp_server = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateExadataInfrastructureDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateExadataInfrastructureDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateExadataInfrastructureDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateExadataInfrastructureDetails.
        The user-friendly name for the Exadata infrastructure. The name does not need to be unique.


        :return: The display_name of this CreateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateExadataInfrastructureDetails.
        The user-friendly name for the Exadata infrastructure. The name does not need to be unique.


        :param display_name: The display_name of this CreateExadataInfrastructureDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this CreateExadataInfrastructureDetails.
        The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.


        :return: The shape of this CreateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CreateExadataInfrastructureDetails.
        The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.


        :param shape: The shape of this CreateExadataInfrastructureDetails.
        :type: str
        """
        self._shape = shape

    @property
    def time_zone(self):
        """
        **[Required]** Gets the time_zone of this CreateExadataInfrastructureDetails.
        The time zone of the Exadata infrastructure. For details, see `Exadata Infrastructure Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this CreateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this CreateExadataInfrastructureDetails.
        The time zone of the Exadata infrastructure. For details, see `Exadata Infrastructure Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this CreateExadataInfrastructureDetails.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def cloud_control_plane_server1(self):
        """
        **[Required]** Gets the cloud_control_plane_server1 of this CreateExadataInfrastructureDetails.
        The IP address for the first control plane server.


        :return: The cloud_control_plane_server1 of this CreateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._cloud_control_plane_server1

    @cloud_control_plane_server1.setter
    def cloud_control_plane_server1(self, cloud_control_plane_server1):
        """
        Sets the cloud_control_plane_server1 of this CreateExadataInfrastructureDetails.
        The IP address for the first control plane server.


        :param cloud_control_plane_server1: The cloud_control_plane_server1 of this CreateExadataInfrastructureDetails.
        :type: str
        """
        self._cloud_control_plane_server1 = cloud_control_plane_server1

    @property
    def cloud_control_plane_server2(self):
        """
        **[Required]** Gets the cloud_control_plane_server2 of this CreateExadataInfrastructureDetails.
        The IP address for the second control plane server.


        :return: The cloud_control_plane_server2 of this CreateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._cloud_control_plane_server2

    @cloud_control_plane_server2.setter
    def cloud_control_plane_server2(self, cloud_control_plane_server2):
        """
        Sets the cloud_control_plane_server2 of this CreateExadataInfrastructureDetails.
        The IP address for the second control plane server.


        :param cloud_control_plane_server2: The cloud_control_plane_server2 of this CreateExadataInfrastructureDetails.
        :type: str
        """
        self._cloud_control_plane_server2 = cloud_control_plane_server2

    @property
    def netmask(self):
        """
        **[Required]** Gets the netmask of this CreateExadataInfrastructureDetails.
        The netmask for the control plane network.


        :return: The netmask of this CreateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """
        Sets the netmask of this CreateExadataInfrastructureDetails.
        The netmask for the control plane network.


        :param netmask: The netmask of this CreateExadataInfrastructureDetails.
        :type: str
        """
        self._netmask = netmask

    @property
    def gateway(self):
        """
        **[Required]** Gets the gateway of this CreateExadataInfrastructureDetails.
        The gateway for the control plane network.


        :return: The gateway of this CreateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """
        Sets the gateway of this CreateExadataInfrastructureDetails.
        The gateway for the control plane network.


        :param gateway: The gateway of this CreateExadataInfrastructureDetails.
        :type: str
        """
        self._gateway = gateway

    @property
    def admin_network_cidr(self):
        """
        **[Required]** Gets the admin_network_cidr of this CreateExadataInfrastructureDetails.
        The CIDR block for the Exadata administration network.


        :return: The admin_network_cidr of this CreateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._admin_network_cidr

    @admin_network_cidr.setter
    def admin_network_cidr(self, admin_network_cidr):
        """
        Sets the admin_network_cidr of this CreateExadataInfrastructureDetails.
        The CIDR block for the Exadata administration network.


        :param admin_network_cidr: The admin_network_cidr of this CreateExadataInfrastructureDetails.
        :type: str
        """
        self._admin_network_cidr = admin_network_cidr

    @property
    def infini_band_network_cidr(self):
        """
        **[Required]** Gets the infini_band_network_cidr of this CreateExadataInfrastructureDetails.
        The CIDR block for the Exadata InfiniBand interconnect.


        :return: The infini_band_network_cidr of this CreateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._infini_band_network_cidr

    @infini_band_network_cidr.setter
    def infini_band_network_cidr(self, infini_band_network_cidr):
        """
        Sets the infini_band_network_cidr of this CreateExadataInfrastructureDetails.
        The CIDR block for the Exadata InfiniBand interconnect.


        :param infini_band_network_cidr: The infini_band_network_cidr of this CreateExadataInfrastructureDetails.
        :type: str
        """
        self._infini_band_network_cidr = infini_band_network_cidr

    @property
    def corporate_proxy(self):
        """
        Gets the corporate_proxy of this CreateExadataInfrastructureDetails.
        The corporate network proxy for access to the control plane network. Oracle recommends using an HTTPS proxy when possible
        for enhanced security.


        :return: The corporate_proxy of this CreateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._corporate_proxy

    @corporate_proxy.setter
    def corporate_proxy(self, corporate_proxy):
        """
        Sets the corporate_proxy of this CreateExadataInfrastructureDetails.
        The corporate network proxy for access to the control plane network. Oracle recommends using an HTTPS proxy when possible
        for enhanced security.


        :param corporate_proxy: The corporate_proxy of this CreateExadataInfrastructureDetails.
        :type: str
        """
        self._corporate_proxy = corporate_proxy

    @property
    def contacts(self):
        """
        Gets the contacts of this CreateExadataInfrastructureDetails.
        The list of contacts for the Exadata infrastructure.


        :return: The contacts of this CreateExadataInfrastructureDetails.
        :rtype: list[oci.database.models.ExadataInfrastructureContact]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """
        Sets the contacts of this CreateExadataInfrastructureDetails.
        The list of contacts for the Exadata infrastructure.


        :param contacts: The contacts of this CreateExadataInfrastructureDetails.
        :type: list[oci.database.models.ExadataInfrastructureContact]
        """
        self._contacts = contacts

    @property
    def maintenance_window(self):
        """
        Gets the maintenance_window of this CreateExadataInfrastructureDetails.

        :return: The maintenance_window of this CreateExadataInfrastructureDetails.
        :rtype: oci.database.models.MaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """
        Sets the maintenance_window of this CreateExadataInfrastructureDetails.

        :param maintenance_window: The maintenance_window of this CreateExadataInfrastructureDetails.
        :type: oci.database.models.MaintenanceWindow
        """
        self._maintenance_window = maintenance_window

    @property
    def storage_count(self):
        """
        Gets the storage_count of this CreateExadataInfrastructureDetails.
        The number of storage servers for the Exadata infrastructure.


        :return: The storage_count of this CreateExadataInfrastructureDetails.
        :rtype: int
        """
        return self._storage_count

    @storage_count.setter
    def storage_count(self, storage_count):
        """
        Sets the storage_count of this CreateExadataInfrastructureDetails.
        The number of storage servers for the Exadata infrastructure.


        :param storage_count: The storage_count of this CreateExadataInfrastructureDetails.
        :type: int
        """
        self._storage_count = storage_count

    @property
    def compute_count(self):
        """
        Gets the compute_count of this CreateExadataInfrastructureDetails.
        The number of compute servers for the Exadata infrastructure.


        :return: The compute_count of this CreateExadataInfrastructureDetails.
        :rtype: int
        """
        return self._compute_count

    @compute_count.setter
    def compute_count(self, compute_count):
        """
        Sets the compute_count of this CreateExadataInfrastructureDetails.
        The number of compute servers for the Exadata infrastructure.


        :param compute_count: The compute_count of this CreateExadataInfrastructureDetails.
        :type: int
        """
        self._compute_count = compute_count

    @property
    def dns_server(self):
        """
        **[Required]** Gets the dns_server of this CreateExadataInfrastructureDetails.
        The list of DNS server IP addresses. Maximum of 3 allowed.


        :return: The dns_server of this CreateExadataInfrastructureDetails.
        :rtype: list[str]
        """
        return self._dns_server

    @dns_server.setter
    def dns_server(self, dns_server):
        """
        Sets the dns_server of this CreateExadataInfrastructureDetails.
        The list of DNS server IP addresses. Maximum of 3 allowed.


        :param dns_server: The dns_server of this CreateExadataInfrastructureDetails.
        :type: list[str]
        """
        self._dns_server = dns_server

    @property
    def ntp_server(self):
        """
        **[Required]** Gets the ntp_server of this CreateExadataInfrastructureDetails.
        The list of NTP server IP addresses. Maximum of 3 allowed.


        :return: The ntp_server of this CreateExadataInfrastructureDetails.
        :rtype: list[str]
        """
        return self._ntp_server

    @ntp_server.setter
    def ntp_server(self, ntp_server):
        """
        Sets the ntp_server of this CreateExadataInfrastructureDetails.
        The list of NTP server IP addresses. Maximum of 3 allowed.


        :param ntp_server: The ntp_server of this CreateExadataInfrastructureDetails.
        :type: list[str]
        """
        self._ntp_server = ntp_server

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateExadataInfrastructureDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateExadataInfrastructureDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateExadataInfrastructureDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateExadataInfrastructureDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
