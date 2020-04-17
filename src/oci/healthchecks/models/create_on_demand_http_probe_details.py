# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOnDemandHttpProbeDetails(object):
    """
    The request body used to create an on-demand HTTP probe.
    """

    #: A constant which can be used with the protocol property of a CreateOnDemandHttpProbeDetails.
    #: This constant has a value of "HTTP"
    PROTOCOL_HTTP = "HTTP"

    #: A constant which can be used with the protocol property of a CreateOnDemandHttpProbeDetails.
    #: This constant has a value of "HTTPS"
    PROTOCOL_HTTPS = "HTTPS"

    #: A constant which can be used with the method property of a CreateOnDemandHttpProbeDetails.
    #: This constant has a value of "GET"
    METHOD_GET = "GET"

    #: A constant which can be used with the method property of a CreateOnDemandHttpProbeDetails.
    #: This constant has a value of "HEAD"
    METHOD_HEAD = "HEAD"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOnDemandHttpProbeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOnDemandHttpProbeDetails.
        :type compartment_id: str

        :param targets:
            The value to assign to the targets property of this CreateOnDemandHttpProbeDetails.
        :type targets: list[str]

        :param vantage_point_names:
            The value to assign to the vantage_point_names property of this CreateOnDemandHttpProbeDetails.
        :type vantage_point_names: list[str]

        :param port:
            The value to assign to the port property of this CreateOnDemandHttpProbeDetails.
        :type port: int

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this CreateOnDemandHttpProbeDetails.
        :type timeout_in_seconds: int

        :param protocol:
            The value to assign to the protocol property of this CreateOnDemandHttpProbeDetails.
            Allowed values for this property are: "HTTP", "HTTPS"
        :type protocol: str

        :param method:
            The value to assign to the method property of this CreateOnDemandHttpProbeDetails.
            Allowed values for this property are: "GET", "HEAD"
        :type method: str

        :param path:
            The value to assign to the path property of this CreateOnDemandHttpProbeDetails.
        :type path: str

        :param headers:
            The value to assign to the headers property of this CreateOnDemandHttpProbeDetails.
        :type headers: dict(str, str)

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'targets': 'list[str]',
            'vantage_point_names': 'list[str]',
            'port': 'int',
            'timeout_in_seconds': 'int',
            'protocol': 'str',
            'method': 'str',
            'path': 'str',
            'headers': 'dict(str, str)'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'targets': 'targets',
            'vantage_point_names': 'vantagePointNames',
            'port': 'port',
            'timeout_in_seconds': 'timeoutInSeconds',
            'protocol': 'protocol',
            'method': 'method',
            'path': 'path',
            'headers': 'headers'
        }

        self._compartment_id = None
        self._targets = None
        self._vantage_point_names = None
        self._port = None
        self._timeout_in_seconds = None
        self._protocol = None
        self._method = None
        self._path = None
        self._headers = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateOnDemandHttpProbeDetails.
        The OCID of the compartment.


        :return: The compartment_id of this CreateOnDemandHttpProbeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateOnDemandHttpProbeDetails.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this CreateOnDemandHttpProbeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def targets(self):
        """
        **[Required]** Gets the targets of this CreateOnDemandHttpProbeDetails.
        A list of targets (hostnames or IP addresses) of the probe.


        :return: The targets of this CreateOnDemandHttpProbeDetails.
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this CreateOnDemandHttpProbeDetails.
        A list of targets (hostnames or IP addresses) of the probe.


        :param targets: The targets of this CreateOnDemandHttpProbeDetails.
        :type: list[str]
        """
        self._targets = targets

    @property
    def vantage_point_names(self):
        """
        Gets the vantage_point_names of this CreateOnDemandHttpProbeDetails.
        A list of names of vantage points from which to execute the probe.


        :return: The vantage_point_names of this CreateOnDemandHttpProbeDetails.
        :rtype: list[str]
        """
        return self._vantage_point_names

    @vantage_point_names.setter
    def vantage_point_names(self, vantage_point_names):
        """
        Sets the vantage_point_names of this CreateOnDemandHttpProbeDetails.
        A list of names of vantage points from which to execute the probe.


        :param vantage_point_names: The vantage_point_names of this CreateOnDemandHttpProbeDetails.
        :type: list[str]
        """
        self._vantage_point_names = vantage_point_names

    @property
    def port(self):
        """
        Gets the port of this CreateOnDemandHttpProbeDetails.
        The port on which to probe endpoints. If unspecified, probes will use the
        default port of their protocol.


        :return: The port of this CreateOnDemandHttpProbeDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this CreateOnDemandHttpProbeDetails.
        The port on which to probe endpoints. If unspecified, probes will use the
        default port of their protocol.


        :param port: The port of this CreateOnDemandHttpProbeDetails.
        :type: int
        """
        self._port = port

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this CreateOnDemandHttpProbeDetails.
        The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
        The probe timeout must be less than or equal to `intervalInSeconds` for monitors.


        :return: The timeout_in_seconds of this CreateOnDemandHttpProbeDetails.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this CreateOnDemandHttpProbeDetails.
        The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
        The probe timeout must be less than or equal to `intervalInSeconds` for monitors.


        :param timeout_in_seconds: The timeout_in_seconds of this CreateOnDemandHttpProbeDetails.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this CreateOnDemandHttpProbeDetails.
        Allowed values for this property are: "HTTP", "HTTPS"


        :return: The protocol of this CreateOnDemandHttpProbeDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this CreateOnDemandHttpProbeDetails.

        :param protocol: The protocol of this CreateOnDemandHttpProbeDetails.
        :type: str
        """
        allowed_values = ["HTTP", "HTTPS"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            raise ValueError(
                "Invalid value for `protocol`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._protocol = protocol

    @property
    def method(self):
        """
        Gets the method of this CreateOnDemandHttpProbeDetails.
        Allowed values for this property are: "GET", "HEAD"


        :return: The method of this CreateOnDemandHttpProbeDetails.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this CreateOnDemandHttpProbeDetails.

        :param method: The method of this CreateOnDemandHttpProbeDetails.
        :type: str
        """
        allowed_values = ["GET", "HEAD"]
        if not value_allowed_none_or_none_sentinel(method, allowed_values):
            raise ValueError(
                "Invalid value for `method`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._method = method

    @property
    def path(self):
        """
        Gets the path of this CreateOnDemandHttpProbeDetails.
        The optional URL path to probe, including query parameters.


        :return: The path of this CreateOnDemandHttpProbeDetails.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this CreateOnDemandHttpProbeDetails.
        The optional URL path to probe, including query parameters.


        :param path: The path of this CreateOnDemandHttpProbeDetails.
        :type: str
        """
        self._path = path

    @property
    def headers(self):
        """
        Gets the headers of this CreateOnDemandHttpProbeDetails.
        A dictionary of HTTP request headers.

        *Note:* Monitors and probes do not support the use of the `Authorization` HTTP header.


        :return: The headers of this CreateOnDemandHttpProbeDetails.
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this CreateOnDemandHttpProbeDetails.
        A dictionary of HTTP request headers.

        *Note:* Monitors and probes do not support the use of the `Authorization` HTTP header.


        :param headers: The headers of this CreateOnDemandHttpProbeDetails.
        :type: dict(str, str)
        """
        self._headers = headers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
