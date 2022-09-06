# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dp_endpoint import DpEndpoint
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DpEndpointFromPrivate(DpEndpoint):
    """
    The endpoint details of a private endpoint.
    """

    #: A constant which can be used with the state property of a DpEndpointFromPrivate.
    #: This constant has a value of "ACTIVE"
    STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the state property of a DpEndpointFromPrivate.
    #: This constant has a value of "INACTIVE"
    STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new DpEndpointFromPrivate object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.DpEndpointFromPrivate.model_type` attribute
        of this class is ``PRIVATE_END_POINT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DpEndpointFromPrivate.
            Allowed values for this property are: "PRIVATE_END_POINT", "PUBLIC_END_POINT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this DpEndpointFromPrivate.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DpEndpointFromPrivate.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this DpEndpointFromPrivate.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this DpEndpointFromPrivate.
        :type name: str

        :param description:
            The value to assign to the description property of this DpEndpointFromPrivate.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this DpEndpointFromPrivate.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this DpEndpointFromPrivate.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DpEndpointFromPrivate.
        :type identifier: str

        :param data_assets:
            The value to assign to the data_assets property of this DpEndpointFromPrivate.
        :type data_assets: list[oci.data_connectivity.models.DataAsset]

        :param dcms_endpoint_id:
            The value to assign to the dcms_endpoint_id property of this DpEndpointFromPrivate.
        :type dcms_endpoint_id: str

        :param pe_id:
            The value to assign to the pe_id property of this DpEndpointFromPrivate.
        :type pe_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DpEndpointFromPrivate.
        :type compartment_id: str

        :param dns_proxy_ip:
            The value to assign to the dns_proxy_ip property of this DpEndpointFromPrivate.
        :type dns_proxy_ip: str

        :param private_endpoint_ip:
            The value to assign to the private_endpoint_ip property of this DpEndpointFromPrivate.
        :type private_endpoint_ip: str

        :param dns_zones:
            The value to assign to the dns_zones property of this DpEndpointFromPrivate.
        :type dns_zones: list[str]

        :param state:
            The value to assign to the state property of this DpEndpointFromPrivate.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type state: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'data_assets': 'list[DataAsset]',
            'dcms_endpoint_id': 'str',
            'pe_id': 'str',
            'compartment_id': 'str',
            'dns_proxy_ip': 'str',
            'private_endpoint_ip': 'str',
            'dns_zones': 'list[str]',
            'state': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'data_assets': 'dataAssets',
            'dcms_endpoint_id': 'dcmsEndpointId',
            'pe_id': 'peId',
            'compartment_id': 'compartmentId',
            'dns_proxy_ip': 'dnsProxyIp',
            'private_endpoint_ip': 'privateEndpointIp',
            'dns_zones': 'dnsZones',
            'state': 'state'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._data_assets = None
        self._dcms_endpoint_id = None
        self._pe_id = None
        self._compartment_id = None
        self._dns_proxy_ip = None
        self._private_endpoint_ip = None
        self._dns_zones = None
        self._state = None
        self._model_type = 'PRIVATE_END_POINT'

    @property
    def dcms_endpoint_id(self):
        """
        **[Required]** Gets the dcms_endpoint_id of this DpEndpointFromPrivate.
        The endpoint ID provided by control plane.


        :return: The dcms_endpoint_id of this DpEndpointFromPrivate.
        :rtype: str
        """
        return self._dcms_endpoint_id

    @dcms_endpoint_id.setter
    def dcms_endpoint_id(self, dcms_endpoint_id):
        """
        Sets the dcms_endpoint_id of this DpEndpointFromPrivate.
        The endpoint ID provided by control plane.


        :param dcms_endpoint_id: The dcms_endpoint_id of this DpEndpointFromPrivate.
        :type: str
        """
        self._dcms_endpoint_id = dcms_endpoint_id

    @property
    def pe_id(self):
        """
        Gets the pe_id of this DpEndpointFromPrivate.
        The OCID of the private endpoint resource.


        :return: The pe_id of this DpEndpointFromPrivate.
        :rtype: str
        """
        return self._pe_id

    @pe_id.setter
    def pe_id(self, pe_id):
        """
        Sets the pe_id of this DpEndpointFromPrivate.
        The OCID of the private endpoint resource.


        :param pe_id: The pe_id of this DpEndpointFromPrivate.
        :type: str
        """
        self._pe_id = pe_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DpEndpointFromPrivate.
        The compartmentId of the private endpoint resource.


        :return: The compartment_id of this DpEndpointFromPrivate.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DpEndpointFromPrivate.
        The compartmentId of the private endpoint resource.


        :param compartment_id: The compartment_id of this DpEndpointFromPrivate.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def dns_proxy_ip(self):
        """
        Gets the dns_proxy_ip of this DpEndpointFromPrivate.
        The IP address of the DNS proxy.


        :return: The dns_proxy_ip of this DpEndpointFromPrivate.
        :rtype: str
        """
        return self._dns_proxy_ip

    @dns_proxy_ip.setter
    def dns_proxy_ip(self, dns_proxy_ip):
        """
        Sets the dns_proxy_ip of this DpEndpointFromPrivate.
        The IP address of the DNS proxy.


        :param dns_proxy_ip: The dns_proxy_ip of this DpEndpointFromPrivate.
        :type: str
        """
        self._dns_proxy_ip = dns_proxy_ip

    @property
    def private_endpoint_ip(self):
        """
        Gets the private_endpoint_ip of this DpEndpointFromPrivate.
        The OCID of the private endpoint resource.


        :return: The private_endpoint_ip of this DpEndpointFromPrivate.
        :rtype: str
        """
        return self._private_endpoint_ip

    @private_endpoint_ip.setter
    def private_endpoint_ip(self, private_endpoint_ip):
        """
        Sets the private_endpoint_ip of this DpEndpointFromPrivate.
        The OCID of the private endpoint resource.


        :param private_endpoint_ip: The private_endpoint_ip of this DpEndpointFromPrivate.
        :type: str
        """
        self._private_endpoint_ip = private_endpoint_ip

    @property
    def dns_zones(self):
        """
        Gets the dns_zones of this DpEndpointFromPrivate.
        Array of DNS zones to be used during the private endpoint resolution.


        :return: The dns_zones of this DpEndpointFromPrivate.
        :rtype: list[str]
        """
        return self._dns_zones

    @dns_zones.setter
    def dns_zones(self, dns_zones):
        """
        Sets the dns_zones of this DpEndpointFromPrivate.
        Array of DNS zones to be used during the private endpoint resolution.


        :param dns_zones: The dns_zones of this DpEndpointFromPrivate.
        :type: list[str]
        """
        self._dns_zones = dns_zones

    @property
    def state(self):
        """
        Gets the state of this DpEndpointFromPrivate.
        Specifies the private endpoint state.

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The state of this DpEndpointFromPrivate.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this DpEndpointFromPrivate.
        Specifies the private endpoint state.


        :param state: The state of this DpEndpointFromPrivate.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            state = 'UNKNOWN_ENUM_VALUE'
        self._state = state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
