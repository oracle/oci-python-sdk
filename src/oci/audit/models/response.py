# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Response(object):
    """
    A container object for response attributes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Response object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this Response.
        :type status: str

        :param response_time:
            The value to assign to the response_time property of this Response.
        :type response_time: datetime

        :param headers:
            The value to assign to the headers property of this Response.
        :type headers: dict(str, list[str])

        :param payload:
            The value to assign to the payload property of this Response.
        :type payload: dict(str, object)

        :param message:
            The value to assign to the message property of this Response.
        :type message: str

        """
        self.swagger_types = {
            'status': 'str',
            'response_time': 'datetime',
            'headers': 'dict(str, list[str])',
            'payload': 'dict(str, object)',
            'message': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'response_time': 'responseTime',
            'headers': 'headers',
            'payload': 'payload',
            'message': 'message'
        }

        self._status = None
        self._response_time = None
        self._headers = None
        self._payload = None
        self._message = None

    @property
    def status(self):
        """
        Gets the status of this Response.
        The status code of the response.

        Example: `200`


        :return: The status of this Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Response.
        The status code of the response.

        Example: `200`


        :param status: The status of this Response.
        :type: str
        """
        self._status = status

    @property
    def response_time(self):
        """
        Gets the response_time of this Response.
        The time of the response to the audited request, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2019-09-18T00:10:59.278Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The response_time of this Response.
        :rtype: datetime
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """
        Sets the response_time of this Response.
        The time of the response to the audited request, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2019-09-18T00:10:59.278Z`

        __ https://tools.ietf.org/html/rfc3339


        :param response_time: The response_time of this Response.
        :type: datetime
        """
        self._response_time = response_time

    @property
    def headers(self):
        """
        Gets the headers of this Response.
        The headers of the response.

        Example:

          -----
            {
              \"ETag\": [
                \"<unique_ID>\"
              ],
              \"Connection\": [
                \"close\"
              ],
              \"Content-Length\": [
                \"1828\"
              ],
              \"opc-request-id\": [
                \"<unique_ID>\"
              ],
              \"Date\": [
                \"Wed, 18 Sep 2019 00:10:59 GMT\"
              ],
              \"Content-Type\": [
                \"application/json\"
              ]
            }
          -----


        :return: The headers of this Response.
        :rtype: dict(str, list[str])
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this Response.
        The headers of the response.

        Example:

          -----
            {
              \"ETag\": [
                \"<unique_ID>\"
              ],
              \"Connection\": [
                \"close\"
              ],
              \"Content-Length\": [
                \"1828\"
              ],
              \"opc-request-id\": [
                \"<unique_ID>\"
              ],
              \"Date\": [
                \"Wed, 18 Sep 2019 00:10:59 GMT\"
              ],
              \"Content-Type\": [
                \"application/json\"
              ]
            }
          -----


        :param headers: The headers of this Response.
        :type: dict(str, list[str])
        """
        self._headers = headers

    @property
    def payload(self):
        """
        Gets the payload of this Response.
        This value is included for backward compatibility with the Audit version 1 schema, where
        it contained metadata of interest from the response payload.

        Example:

          -----
            {
              \"resourceName\": \"my_instance\",
              \"id\": \"ocid1.instance.oc1.phx.<unique_ID>\"
            }
          -----


        :return: The payload of this Response.
        :rtype: dict(str, object)
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this Response.
        This value is included for backward compatibility with the Audit version 1 schema, where
        it contained metadata of interest from the response payload.

        Example:

          -----
            {
              \"resourceName\": \"my_instance\",
              \"id\": \"ocid1.instance.oc1.phx.<unique_ID>\"
            }
          -----


        :param payload: The payload of this Response.
        :type: dict(str, object)
        """
        self._payload = payload

    @property
    def message(self):
        """
        Gets the message of this Response.
        A friendly description of what happened during the operation. Use this for troubleshooting.


        :return: The message of this Response.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Response.
        A friendly description of what happened during the operation. Use this for troubleshooting.


        :param message: The message of this Response.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
