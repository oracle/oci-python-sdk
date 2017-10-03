# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class AuditEvent(object):

    def __init__(self):

        self.swagger_types = {
            'tenant_id': 'str',
            'compartment_id': 'str',
            'event_id': 'str',
            'event_source': 'str',
            'event_type': 'str',
            'event_time': 'datetime',
            'principal_id': 'str',
            'credential_id': 'str',
            'request_action': 'str',
            'request_id': 'str',
            'request_agent': 'str',
            'request_headers': 'dict(str, list[str])',
            'request_origin': 'str',
            'request_parameters': 'dict(str, list[str])',
            'request_resource': 'str',
            'response_headers': 'dict(str, list[str])',
            'response_status': 'str',
            'response_time': 'datetime'
        }

        self.attribute_map = {
            'tenant_id': 'tenantId',
            'compartment_id': 'compartmentId',
            'event_id': 'eventId',
            'event_source': 'eventSource',
            'event_type': 'eventType',
            'event_time': 'eventTime',
            'principal_id': 'principalId',
            'credential_id': 'credentialId',
            'request_action': 'requestAction',
            'request_id': 'requestId',
            'request_agent': 'requestAgent',
            'request_headers': 'requestHeaders',
            'request_origin': 'requestOrigin',
            'request_parameters': 'requestParameters',
            'request_resource': 'requestResource',
            'response_headers': 'responseHeaders',
            'response_status': 'responseStatus',
            'response_time': 'responseTime'
        }

        self._tenant_id = None
        self._compartment_id = None
        self._event_id = None
        self._event_source = None
        self._event_type = None
        self._event_time = None
        self._principal_id = None
        self._credential_id = None
        self._request_action = None
        self._request_id = None
        self._request_agent = None
        self._request_headers = None
        self._request_origin = None
        self._request_parameters = None
        self._request_resource = None
        self._response_headers = None
        self._response_status = None
        self._response_time = None

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this AuditEvent.
        The OCID of the tenant.


        :return: The tenant_id of this AuditEvent.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this AuditEvent.
        The OCID of the tenant.


        :param tenant_id: The tenant_id of this AuditEvent.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this AuditEvent.
        The OCID of the compartment.


        :return: The compartment_id of this AuditEvent.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AuditEvent.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this AuditEvent.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def event_id(self):
        """
        Gets the event_id of this AuditEvent.
        The GUID of the event.


        :return: The event_id of this AuditEvent.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this AuditEvent.
        The GUID of the event.


        :param event_id: The event_id of this AuditEvent.
        :type: str
        """
        self._event_id = event_id

    @property
    def event_source(self):
        """
        Gets the event_source of this AuditEvent.
        The source of the event.


        :return: The event_source of this AuditEvent.
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """
        Sets the event_source of this AuditEvent.
        The source of the event.


        :param event_source: The event_source of this AuditEvent.
        :type: str
        """
        self._event_source = event_source

    @property
    def event_type(self):
        """
        Gets the event_type of this AuditEvent.
        The type of the event.


        :return: The event_type of this AuditEvent.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this AuditEvent.
        The type of the event.


        :param event_type: The event_type of this AuditEvent.
        :type: str
        """
        self._event_type = event_type

    @property
    def event_time(self):
        """
        Gets the event_time of this AuditEvent.
        The time the event occurred, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :return: The event_time of this AuditEvent.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """
        Sets the event_time of this AuditEvent.
        The time the event occurred, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :param event_time: The event_time of this AuditEvent.
        :type: datetime
        """
        self._event_time = event_time

    @property
    def principal_id(self):
        """
        Gets the principal_id of this AuditEvent.
        The OCID of the user whose action triggered the event.


        :return: The principal_id of this AuditEvent.
        :rtype: str
        """
        return self._principal_id

    @principal_id.setter
    def principal_id(self, principal_id):
        """
        Sets the principal_id of this AuditEvent.
        The OCID of the user whose action triggered the event.


        :param principal_id: The principal_id of this AuditEvent.
        :type: str
        """
        self._principal_id = principal_id

    @property
    def credential_id(self):
        """
        Gets the credential_id of this AuditEvent.
        The credential ID of the user. This value is extracted from the HTTP 'Authorization' request header. It consists of the tenantId, userId, and user fingerprint, all delimited by a slash (/).


        :return: The credential_id of this AuditEvent.
        :rtype: str
        """
        return self._credential_id

    @credential_id.setter
    def credential_id(self, credential_id):
        """
        Sets the credential_id of this AuditEvent.
        The credential ID of the user. This value is extracted from the HTTP 'Authorization' request header. It consists of the tenantId, userId, and user fingerprint, all delimited by a slash (/).


        :param credential_id: The credential_id of this AuditEvent.
        :type: str
        """
        self._credential_id = credential_id

    @property
    def request_action(self):
        """
        Gets the request_action of this AuditEvent.
        The HTTP method of the request.


        :return: The request_action of this AuditEvent.
        :rtype: str
        """
        return self._request_action

    @request_action.setter
    def request_action(self, request_action):
        """
        Sets the request_action of this AuditEvent.
        The HTTP method of the request.


        :param request_action: The request_action of this AuditEvent.
        :type: str
        """
        self._request_action = request_action

    @property
    def request_id(self):
        """
        Gets the request_id of this AuditEvent.
        The opc-request-id of the request.


        :return: The request_id of this AuditEvent.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this AuditEvent.
        The opc-request-id of the request.


        :param request_id: The request_id of this AuditEvent.
        :type: str
        """
        self._request_id = request_id

    @property
    def request_agent(self):
        """
        Gets the request_agent of this AuditEvent.
        The user agent of the client that made the request.


        :return: The request_agent of this AuditEvent.
        :rtype: str
        """
        return self._request_agent

    @request_agent.setter
    def request_agent(self, request_agent):
        """
        Sets the request_agent of this AuditEvent.
        The user agent of the client that made the request.


        :param request_agent: The request_agent of this AuditEvent.
        :type: str
        """
        self._request_agent = request_agent

    @property
    def request_headers(self):
        """
        Gets the request_headers of this AuditEvent.
        The HTTP header fields and values in the request.


        :return: The request_headers of this AuditEvent.
        :rtype: dict(str, list[str])
        """
        return self._request_headers

    @request_headers.setter
    def request_headers(self, request_headers):
        """
        Sets the request_headers of this AuditEvent.
        The HTTP header fields and values in the request.


        :param request_headers: The request_headers of this AuditEvent.
        :type: dict(str, list[str])
        """
        self._request_headers = request_headers

    @property
    def request_origin(self):
        """
        Gets the request_origin of this AuditEvent.
        The IP address of the source of the request.


        :return: The request_origin of this AuditEvent.
        :rtype: str
        """
        return self._request_origin

    @request_origin.setter
    def request_origin(self, request_origin):
        """
        Sets the request_origin of this AuditEvent.
        The IP address of the source of the request.


        :param request_origin: The request_origin of this AuditEvent.
        :type: str
        """
        self._request_origin = request_origin

    @property
    def request_parameters(self):
        """
        Gets the request_parameters of this AuditEvent.
        The query parameter fields and values for the request.


        :return: The request_parameters of this AuditEvent.
        :rtype: dict(str, list[str])
        """
        return self._request_parameters

    @request_parameters.setter
    def request_parameters(self, request_parameters):
        """
        Sets the request_parameters of this AuditEvent.
        The query parameter fields and values for the request.


        :param request_parameters: The request_parameters of this AuditEvent.
        :type: dict(str, list[str])
        """
        self._request_parameters = request_parameters

    @property
    def request_resource(self):
        """
        Gets the request_resource of this AuditEvent.
        The resource targeted by the request.


        :return: The request_resource of this AuditEvent.
        :rtype: str
        """
        return self._request_resource

    @request_resource.setter
    def request_resource(self, request_resource):
        """
        Sets the request_resource of this AuditEvent.
        The resource targeted by the request.


        :param request_resource: The request_resource of this AuditEvent.
        :type: str
        """
        self._request_resource = request_resource

    @property
    def response_headers(self):
        """
        Gets the response_headers of this AuditEvent.
        The headers of the response.


        :return: The response_headers of this AuditEvent.
        :rtype: dict(str, list[str])
        """
        return self._response_headers

    @response_headers.setter
    def response_headers(self, response_headers):
        """
        Sets the response_headers of this AuditEvent.
        The headers of the response.


        :param response_headers: The response_headers of this AuditEvent.
        :type: dict(str, list[str])
        """
        self._response_headers = response_headers

    @property
    def response_status(self):
        """
        Gets the response_status of this AuditEvent.
        The status code of the response.


        :return: The response_status of this AuditEvent.
        :rtype: str
        """
        return self._response_status

    @response_status.setter
    def response_status(self, response_status):
        """
        Sets the response_status of this AuditEvent.
        The status code of the response.


        :param response_status: The response_status of this AuditEvent.
        :type: str
        """
        self._response_status = response_status

    @property
    def response_time(self):
        """
        Gets the response_time of this AuditEvent.
        The time of the response to the audited request, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :return: The response_time of this AuditEvent.
        :rtype: datetime
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """
        Sets the response_time of this AuditEvent.
        The time of the response to the audited request, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :param response_time: The response_time of this AuditEvent.
        :type: datetime
        """
        self._response_time = response_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
