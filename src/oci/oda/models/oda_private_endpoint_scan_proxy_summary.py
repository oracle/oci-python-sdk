# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OdaPrivateEndpointScanProxySummary(object):
    """
    Details pertaining to a scan proxy instance created for a scan listener FQDN/IPs
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OdaPrivateEndpointScanProxySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OdaPrivateEndpointScanProxySummary.
        :type id: str

        :param scan_listener_type:
            The value to assign to the scan_listener_type property of this OdaPrivateEndpointScanProxySummary.
        :type scan_listener_type: str

        :param protocol:
            The value to assign to the protocol property of this OdaPrivateEndpointScanProxySummary.
        :type protocol: str

        :param scan_listener_infos:
            The value to assign to the scan_listener_infos property of this OdaPrivateEndpointScanProxySummary.
        :type scan_listener_infos: list[oci.oda.models.ScanListenerInfo]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OdaPrivateEndpointScanProxySummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this OdaPrivateEndpointScanProxySummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'scan_listener_type': 'str',
            'protocol': 'str',
            'scan_listener_infos': 'list[ScanListenerInfo]',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'scan_listener_type': 'scanListenerType',
            'protocol': 'protocol',
            'scan_listener_infos': 'scanListenerInfos',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._scan_listener_type = None
        self._protocol = None
        self._scan_listener_infos = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OdaPrivateEndpointScanProxySummary.
        The `OCID`__ of the ODA Private Endpoint Scan Proxy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this OdaPrivateEndpointScanProxySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OdaPrivateEndpointScanProxySummary.
        The `OCID`__ of the ODA Private Endpoint Scan Proxy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this OdaPrivateEndpointScanProxySummary.
        :type: str
        """
        self._id = id

    @property
    def scan_listener_type(self):
        """
        **[Required]** Gets the scan_listener_type of this OdaPrivateEndpointScanProxySummary.
        Type indicating whether Scan listener is specified by its FQDN or list of IPs


        :return: The scan_listener_type of this OdaPrivateEndpointScanProxySummary.
        :rtype: str
        """
        return self._scan_listener_type

    @scan_listener_type.setter
    def scan_listener_type(self, scan_listener_type):
        """
        Sets the scan_listener_type of this OdaPrivateEndpointScanProxySummary.
        Type indicating whether Scan listener is specified by its FQDN or list of IPs


        :param scan_listener_type: The scan_listener_type of this OdaPrivateEndpointScanProxySummary.
        :type: str
        """
        self._scan_listener_type = scan_listener_type

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this OdaPrivateEndpointScanProxySummary.
        The protocol used for communication between client, scanProxy and RAC's scan listeners


        :return: The protocol of this OdaPrivateEndpointScanProxySummary.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this OdaPrivateEndpointScanProxySummary.
        The protocol used for communication between client, scanProxy and RAC's scan listeners


        :param protocol: The protocol of this OdaPrivateEndpointScanProxySummary.
        :type: str
        """
        self._protocol = protocol

    @property
    def scan_listener_infos(self):
        """
        **[Required]** Gets the scan_listener_infos of this OdaPrivateEndpointScanProxySummary.
        The FQDN/IPs and port information of customer's Real Application Cluster (RAC)'s SCAN listeners.


        :return: The scan_listener_infos of this OdaPrivateEndpointScanProxySummary.
        :rtype: list[oci.oda.models.ScanListenerInfo]
        """
        return self._scan_listener_infos

    @scan_listener_infos.setter
    def scan_listener_infos(self, scan_listener_infos):
        """
        Sets the scan_listener_infos of this OdaPrivateEndpointScanProxySummary.
        The FQDN/IPs and port information of customer's Real Application Cluster (RAC)'s SCAN listeners.


        :param scan_listener_infos: The scan_listener_infos of this OdaPrivateEndpointScanProxySummary.
        :type: list[oci.oda.models.ScanListenerInfo]
        """
        self._scan_listener_infos = scan_listener_infos

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OdaPrivateEndpointScanProxySummary.
        The current state of the ODA Private Endpoint Scan Proxy.


        :return: The lifecycle_state of this OdaPrivateEndpointScanProxySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OdaPrivateEndpointScanProxySummary.
        The current state of the ODA Private Endpoint Scan Proxy.


        :param lifecycle_state: The lifecycle_state of this OdaPrivateEndpointScanProxySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this OdaPrivateEndpointScanProxySummary.
        When the resource was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this OdaPrivateEndpointScanProxySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OdaPrivateEndpointScanProxySummary.
        When the resource was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this OdaPrivateEndpointScanProxySummary.
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
