# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateExadataInfrastructureDetails(object):
    """
    Updates the Exadata Cloud@Customer infrastructure.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateExadataInfrastructureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cloud_control_plane_server1:
            The value to assign to the cloud_control_plane_server1 property of this UpdateExadataInfrastructureDetails.
        :type cloud_control_plane_server1: str

        :param cloud_control_plane_server2:
            The value to assign to the cloud_control_plane_server2 property of this UpdateExadataInfrastructureDetails.
        :type cloud_control_plane_server2: str

        :param netmask:
            The value to assign to the netmask property of this UpdateExadataInfrastructureDetails.
        :type netmask: str

        :param gateway:
            The value to assign to the gateway property of this UpdateExadataInfrastructureDetails.
        :type gateway: str

        :param admin_network_cidr:
            The value to assign to the admin_network_cidr property of this UpdateExadataInfrastructureDetails.
        :type admin_network_cidr: str

        :param infini_band_network_cidr:
            The value to assign to the infini_band_network_cidr property of this UpdateExadataInfrastructureDetails.
        :type infini_band_network_cidr: str

        :param corporate_proxy:
            The value to assign to the corporate_proxy property of this UpdateExadataInfrastructureDetails.
        :type corporate_proxy: str

        :param contacts:
            The value to assign to the contacts property of this UpdateExadataInfrastructureDetails.
        :type contacts: list[ExadataInfrastructureContact]

        :param dns_server:
            The value to assign to the dns_server property of this UpdateExadataInfrastructureDetails.
        :type dns_server: list[str]

        :param ntp_server:
            The value to assign to the ntp_server property of this UpdateExadataInfrastructureDetails.
        :type ntp_server: list[str]

        :param time_zone:
            The value to assign to the time_zone property of this UpdateExadataInfrastructureDetails.
        :type time_zone: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateExadataInfrastructureDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateExadataInfrastructureDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'cloud_control_plane_server1': 'str',
            'cloud_control_plane_server2': 'str',
            'netmask': 'str',
            'gateway': 'str',
            'admin_network_cidr': 'str',
            'infini_band_network_cidr': 'str',
            'corporate_proxy': 'str',
            'contacts': 'list[ExadataInfrastructureContact]',
            'dns_server': 'list[str]',
            'ntp_server': 'list[str]',
            'time_zone': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'cloud_control_plane_server1': 'cloudControlPlaneServer1',
            'cloud_control_plane_server2': 'cloudControlPlaneServer2',
            'netmask': 'netmask',
            'gateway': 'gateway',
            'admin_network_cidr': 'adminNetworkCIDR',
            'infini_band_network_cidr': 'infiniBandNetworkCIDR',
            'corporate_proxy': 'corporateProxy',
            'contacts': 'contacts',
            'dns_server': 'dnsServer',
            'ntp_server': 'ntpServer',
            'time_zone': 'timeZone',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._cloud_control_plane_server1 = None
        self._cloud_control_plane_server2 = None
        self._netmask = None
        self._gateway = None
        self._admin_network_cidr = None
        self._infini_band_network_cidr = None
        self._corporate_proxy = None
        self._contacts = None
        self._dns_server = None
        self._ntp_server = None
        self._time_zone = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def cloud_control_plane_server1(self):
        """
        Gets the cloud_control_plane_server1 of this UpdateExadataInfrastructureDetails.
        The IP address for the first control plane server.


        :return: The cloud_control_plane_server1 of this UpdateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._cloud_control_plane_server1

    @cloud_control_plane_server1.setter
    def cloud_control_plane_server1(self, cloud_control_plane_server1):
        """
        Sets the cloud_control_plane_server1 of this UpdateExadataInfrastructureDetails.
        The IP address for the first control plane server.


        :param cloud_control_plane_server1: The cloud_control_plane_server1 of this UpdateExadataInfrastructureDetails.
        :type: str
        """
        self._cloud_control_plane_server1 = cloud_control_plane_server1

    @property
    def cloud_control_plane_server2(self):
        """
        Gets the cloud_control_plane_server2 of this UpdateExadataInfrastructureDetails.
        The IP address for the second control plane server.


        :return: The cloud_control_plane_server2 of this UpdateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._cloud_control_plane_server2

    @cloud_control_plane_server2.setter
    def cloud_control_plane_server2(self, cloud_control_plane_server2):
        """
        Sets the cloud_control_plane_server2 of this UpdateExadataInfrastructureDetails.
        The IP address for the second control plane server.


        :param cloud_control_plane_server2: The cloud_control_plane_server2 of this UpdateExadataInfrastructureDetails.
        :type: str
        """
        self._cloud_control_plane_server2 = cloud_control_plane_server2

    @property
    def netmask(self):
        """
        Gets the netmask of this UpdateExadataInfrastructureDetails.
        The netmask for the control plane network.


        :return: The netmask of this UpdateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """
        Sets the netmask of this UpdateExadataInfrastructureDetails.
        The netmask for the control plane network.


        :param netmask: The netmask of this UpdateExadataInfrastructureDetails.
        :type: str
        """
        self._netmask = netmask

    @property
    def gateway(self):
        """
        Gets the gateway of this UpdateExadataInfrastructureDetails.
        The gateway for the control plane network.


        :return: The gateway of this UpdateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """
        Sets the gateway of this UpdateExadataInfrastructureDetails.
        The gateway for the control plane network.


        :param gateway: The gateway of this UpdateExadataInfrastructureDetails.
        :type: str
        """
        self._gateway = gateway

    @property
    def admin_network_cidr(self):
        """
        Gets the admin_network_cidr of this UpdateExadataInfrastructureDetails.
        The CIDR block for the Exadata administration network.


        :return: The admin_network_cidr of this UpdateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._admin_network_cidr

    @admin_network_cidr.setter
    def admin_network_cidr(self, admin_network_cidr):
        """
        Sets the admin_network_cidr of this UpdateExadataInfrastructureDetails.
        The CIDR block for the Exadata administration network.


        :param admin_network_cidr: The admin_network_cidr of this UpdateExadataInfrastructureDetails.
        :type: str
        """
        self._admin_network_cidr = admin_network_cidr

    @property
    def infini_band_network_cidr(self):
        """
        Gets the infini_band_network_cidr of this UpdateExadataInfrastructureDetails.
        The CIDR block for the Exadata InfiniBand interconnect.


        :return: The infini_band_network_cidr of this UpdateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._infini_band_network_cidr

    @infini_band_network_cidr.setter
    def infini_band_network_cidr(self, infini_band_network_cidr):
        """
        Sets the infini_band_network_cidr of this UpdateExadataInfrastructureDetails.
        The CIDR block for the Exadata InfiniBand interconnect.


        :param infini_band_network_cidr: The infini_band_network_cidr of this UpdateExadataInfrastructureDetails.
        :type: str
        """
        self._infini_band_network_cidr = infini_band_network_cidr

    @property
    def corporate_proxy(self):
        """
        Gets the corporate_proxy of this UpdateExadataInfrastructureDetails.
        The corporate network proxy for access to the control plane network.


        :return: The corporate_proxy of this UpdateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._corporate_proxy

    @corporate_proxy.setter
    def corporate_proxy(self, corporate_proxy):
        """
        Sets the corporate_proxy of this UpdateExadataInfrastructureDetails.
        The corporate network proxy for access to the control plane network.


        :param corporate_proxy: The corporate_proxy of this UpdateExadataInfrastructureDetails.
        :type: str
        """
        self._corporate_proxy = corporate_proxy

    @property
    def contacts(self):
        """
        Gets the contacts of this UpdateExadataInfrastructureDetails.
        The list of contacts for the Exadata infrastructure.


        :return: The contacts of this UpdateExadataInfrastructureDetails.
        :rtype: list[ExadataInfrastructureContact]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """
        Sets the contacts of this UpdateExadataInfrastructureDetails.
        The list of contacts for the Exadata infrastructure.


        :param contacts: The contacts of this UpdateExadataInfrastructureDetails.
        :type: list[ExadataInfrastructureContact]
        """
        self._contacts = contacts

    @property
    def dns_server(self):
        """
        Gets the dns_server of this UpdateExadataInfrastructureDetails.
        The list of DNS server IP addresses. Maximum of 3 allowed.


        :return: The dns_server of this UpdateExadataInfrastructureDetails.
        :rtype: list[str]
        """
        return self._dns_server

    @dns_server.setter
    def dns_server(self, dns_server):
        """
        Sets the dns_server of this UpdateExadataInfrastructureDetails.
        The list of DNS server IP addresses. Maximum of 3 allowed.


        :param dns_server: The dns_server of this UpdateExadataInfrastructureDetails.
        :type: list[str]
        """
        self._dns_server = dns_server

    @property
    def ntp_server(self):
        """
        Gets the ntp_server of this UpdateExadataInfrastructureDetails.
        The list of NTP server IP addresses. Maximum of 3 allowed.


        :return: The ntp_server of this UpdateExadataInfrastructureDetails.
        :rtype: list[str]
        """
        return self._ntp_server

    @ntp_server.setter
    def ntp_server(self, ntp_server):
        """
        Sets the ntp_server of this UpdateExadataInfrastructureDetails.
        The list of NTP server IP addresses. Maximum of 3 allowed.


        :param ntp_server: The ntp_server of this UpdateExadataInfrastructureDetails.
        :type: list[str]
        """
        self._ntp_server = ntp_server

    @property
    def time_zone(self):
        """
        Gets the time_zone of this UpdateExadataInfrastructureDetails.
        The time zone of the Exadata infrastructure. For details, see `Exadata Infrastructure Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this UpdateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this UpdateExadataInfrastructureDetails.
        The time zone of the Exadata infrastructure. For details, see `Exadata Infrastructure Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this UpdateExadataInfrastructureDetails.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateExadataInfrastructureDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateExadataInfrastructureDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateExadataInfrastructureDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateExadataInfrastructureDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateExadataInfrastructureDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateExadataInfrastructureDetails.
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
