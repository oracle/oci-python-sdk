# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Request(object):
    """
    A container object for request attributes.

    Example:

    -----
    {
    \"id\": \"<unique_ID>\",
    \"path\": \"/20160918/instances/ocid1.instance.oc1.phx.<unique_ID>\",
    \"action\": \"GET\",
    \"parameters\": {},
    \"headers\": {
    \"opc-principal\": [
    \"{\\\"tenantId\\\":\\\"ocid1.tenancy.oc1..<unique_ID>\\\",\\\"subjectId\\\":\\\"ocid1.user.oc1..<unique_ID>\\\",\\\"claims\\\":[{\\\"key\\\":\\\"pstype\\\",\\\"value\\\":\\\"natv\\\",\\\"issuer\\\":\\\"authService.oracle.com\\\"},{\\\"key\\\":\\\"h_host\\\",\\\"value\\\":\\\"iaas.r2.oracleiaas.com\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_opc-request-id\\\",\\\"value\\\":\\\"<unique_ID>\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"ptype\\\",\\\"value\\\":\\\"user\\\",\\\"issuer\\\":\\\"authService.oracle.com\\\"},{\\\"key\\\":\\\"h_date\\\",\\\"value\\\":\\\"Wed, 18 Sep 2019 00:10:58 UTC\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_accept\\\",\\\"value\\\":\\\"application/json\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"authorization\\\",\\\"value\\\":\\\"Signature headers=\\\\\\\"date (request-target) host accept opc-request-id\\\\\\\",keyId=\\\\\\\"ocid1.tenancy.oc1..<unique_ID>/ocid1.user.oc1..<unique_ID>/8c:b4:5f:18:e7:ec:db:08:b8:fa:d2:2a:7d:11:76:ac\\\\\\\",algorithm=\\\\\\\"rsa-pss-sha256\\\\\\\",signature=\\\\\\\"<unique_ID>\\\\\\\",version=\\\\\\\"1\\\\\\\"\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_(request-target)\\\",\\\"value\\\":\\\"get /20160918/instances/ocid1.instance.oc1.phx.<unique_ID>\\\",\\\"issuer\\\":\\\"h\\\"}]}\"
    ],
    \"Accept\": [
    \"application/json\"
    ],
    \"X-Oracle-Auth-Client-CN\": [
    \"splat-proxy-se-02302.node.ad2.r2\"
    ],
    \"X-Forwarded-Host\": [
    \"compute-api.svc.ad1.r2\"
    ],
    \"Connection\": [
    \"close\"
    ],
    \"User-Agent\": [
    \"Jersey/2.23 (HttpUrlConnection 1.8.0_212)\"
    ],
    \"X-Forwarded-For\": [
    \"172.24.80.88\"
    ],
    \"X-Real-IP\": [
    \"172.24.80.88\"
    ],
    \"oci-original-url\": [
    \"https://iaas.r2.oracleiaas.com/20160918/instances/ocid1.instance.oc1.phx.<unique_ID>\"
    ],
    \"opc-request-id\": [
    \"<unique_ID>\"
    ],
    \"Date\": [
    \"Wed, 18 Sep 2019 00:10:58 UTC\"
    ]
    }
    }
    -----
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Request object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Request.
        :type id: str

        :param path:
            The value to assign to the path property of this Request.
        :type path: str

        :param action:
            The value to assign to the action property of this Request.
        :type action: str

        :param parameters:
            The value to assign to the parameters property of this Request.
        :type parameters: dict(str, list[str])

        :param headers:
            The value to assign to the headers property of this Request.
        :type headers: dict(str, list[str])

        """
        self.swagger_types = {
            'id': 'str',
            'path': 'str',
            'action': 'str',
            'parameters': 'dict(str, list[str])',
            'headers': 'dict(str, list[str])'
        }

        self.attribute_map = {
            'id': 'id',
            'path': 'path',
            'action': 'action',
            'parameters': 'parameters',
            'headers': 'headers'
        }

        self._id = None
        self._path = None
        self._action = None
        self._parameters = None
        self._headers = None

    @property
    def id(self):
        """
        Gets the id of this Request.
        The opc-request-id of the request.


        :return: The id of this Request.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Request.
        The opc-request-id of the request.


        :param id: The id of this Request.
        :type: str
        """
        self._id = id

    @property
    def path(self):
        """
        Gets the path of this Request.
        The full path of the API request.

        Example: `/20160918/instances/ocid1.instance.oc1.phx.<unique_ID>`


        :return: The path of this Request.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Request.
        The full path of the API request.

        Example: `/20160918/instances/ocid1.instance.oc1.phx.<unique_ID>`


        :param path: The path of this Request.
        :type: str
        """
        self._path = path

    @property
    def action(self):
        """
        Gets the action of this Request.
        The HTTP method of the request.

        Example: `GET`


        :return: The action of this Request.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this Request.
        The HTTP method of the request.

        Example: `GET`


        :param action: The action of this Request.
        :type: str
        """
        self._action = action

    @property
    def parameters(self):
        """
        Gets the parameters of this Request.
        The parameters supplied by the caller during this operation.


        :return: The parameters of this Request.
        :rtype: dict(str, list[str])
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this Request.
        The parameters supplied by the caller during this operation.


        :param parameters: The parameters of this Request.
        :type: dict(str, list[str])
        """
        self._parameters = parameters

    @property
    def headers(self):
        """
        Gets the headers of this Request.
        The HTTP header fields and values in the request.

        Example:

          -----
            {
              \"opc-principal\": [
                \"{\\\"tenantId\\\":\\\"ocid1.tenancy.oc1..<unique_ID>\\\",\\\"subjectId\\\":\\\"ocid1.user.oc1..<unique_ID>\\\",\\\"claims\\\":[{\\\"key\\\":\\\"pstype\\\",\\\"value\\\":\\\"natv\\\",\\\"issuer\\\":\\\"authService.oracle.com\\\"},{\\\"key\\\":\\\"h_host\\\",\\\"value\\\":\\\"iaas.r2.oracleiaas.com\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_opc-request-id\\\",\\\"value\\\":\\\"<unique_ID>\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"ptype\\\",\\\"value\\\":\\\"user\\\",\\\"issuer\\\":\\\"authService.oracle.com\\\"},{\\\"key\\\":\\\"h_date\\\",\\\"value\\\":\\\"Wed, 18 Sep 2019 00:10:58 UTC\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_accept\\\",\\\"value\\\":\\\"application/json\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"authorization\\\",\\\"value\\\":\\\"Signature headers=\\\\\\\"date (request-target) host accept opc-request-id\\\\\\\",keyId=\\\\\\\"ocid1.tenancy.oc1..<unique_ID>/ocid1.user.oc1..<unique_ID>/8c:b4:5f:18:e7:ec:db:08:b8:fa:d2:2a:7d:11:76:ac\\\\\\\",algorithm=\\\\\\\"rsa-pss-sha256\\\\\\\",signature=\\\\\\\"<unique_ID>\\\\\\\",version=\\\\\\\"1\\\\\\\"\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_(request-target)\\\",\\\"value\\\":\\\"get /20160918/instances/ocid1.instance.oc1.phx.<unique_ID>\\\",\\\"issuer\\\":\\\"h\\\"}]}\"
              ],
              \"Accept\": [
                \"application/json\"
              ],
              \"X-Oracle-Auth-Client-CN\": [
                \"splat-proxy-se-02302.node.ad2.r2\"
              ],
              \"X-Forwarded-Host\": [
                \"compute-api.svc.ad1.r2\"
              ],
              \"Connection\": [
                \"close\"
              ],
              \"User-Agent\": [
                \"Jersey/2.23 (HttpUrlConnection 1.8.0_212)\"
              ],
              \"X-Forwarded-For\": [
                \"172.24.80.88\"
              ],
              \"X-Real-IP\": [
                \"172.24.80.88\"
              ],
              \"oci-original-url\": [
                \"https://iaas.r2.oracleiaas.com/20160918/instances/ocid1.instance.oc1.phx.<unique_ID>\"
              ],
              \"opc-request-id\": [
                \"<unique_ID>\"
              ],
              \"Date\": [
                \"Wed, 18 Sep 2019 00:10:58 UTC\"
              ]
            }
          -----


        :return: The headers of this Request.
        :rtype: dict(str, list[str])
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this Request.
        The HTTP header fields and values in the request.

        Example:

          -----
            {
              \"opc-principal\": [
                \"{\\\"tenantId\\\":\\\"ocid1.tenancy.oc1..<unique_ID>\\\",\\\"subjectId\\\":\\\"ocid1.user.oc1..<unique_ID>\\\",\\\"claims\\\":[{\\\"key\\\":\\\"pstype\\\",\\\"value\\\":\\\"natv\\\",\\\"issuer\\\":\\\"authService.oracle.com\\\"},{\\\"key\\\":\\\"h_host\\\",\\\"value\\\":\\\"iaas.r2.oracleiaas.com\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_opc-request-id\\\",\\\"value\\\":\\\"<unique_ID>\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"ptype\\\",\\\"value\\\":\\\"user\\\",\\\"issuer\\\":\\\"authService.oracle.com\\\"},{\\\"key\\\":\\\"h_date\\\",\\\"value\\\":\\\"Wed, 18 Sep 2019 00:10:58 UTC\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_accept\\\",\\\"value\\\":\\\"application/json\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"authorization\\\",\\\"value\\\":\\\"Signature headers=\\\\\\\"date (request-target) host accept opc-request-id\\\\\\\",keyId=\\\\\\\"ocid1.tenancy.oc1..<unique_ID>/ocid1.user.oc1..<unique_ID>/8c:b4:5f:18:e7:ec:db:08:b8:fa:d2:2a:7d:11:76:ac\\\\\\\",algorithm=\\\\\\\"rsa-pss-sha256\\\\\\\",signature=\\\\\\\"<unique_ID>\\\\\\\",version=\\\\\\\"1\\\\\\\"\\\",\\\"issuer\\\":\\\"h\\\"},{\\\"key\\\":\\\"h_(request-target)\\\",\\\"value\\\":\\\"get /20160918/instances/ocid1.instance.oc1.phx.<unique_ID>\\\",\\\"issuer\\\":\\\"h\\\"}]}\"
              ],
              \"Accept\": [
                \"application/json\"
              ],
              \"X-Oracle-Auth-Client-CN\": [
                \"splat-proxy-se-02302.node.ad2.r2\"
              ],
              \"X-Forwarded-Host\": [
                \"compute-api.svc.ad1.r2\"
              ],
              \"Connection\": [
                \"close\"
              ],
              \"User-Agent\": [
                \"Jersey/2.23 (HttpUrlConnection 1.8.0_212)\"
              ],
              \"X-Forwarded-For\": [
                \"172.24.80.88\"
              ],
              \"X-Real-IP\": [
                \"172.24.80.88\"
              ],
              \"oci-original-url\": [
                \"https://iaas.r2.oracleiaas.com/20160918/instances/ocid1.instance.oc1.phx.<unique_ID>\"
              ],
              \"opc-request-id\": [
                \"<unique_ID>\"
              ],
              \"Date\": [
                \"Wed, 18 Sep 2019 00:10:58 UTC\"
              ]
            }
          -----


        :param headers: The headers of this Request.
        :type: dict(str, list[str])
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
