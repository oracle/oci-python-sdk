# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuditEvent(object):
    """
    AuditEvent model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AuditEvent object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenant_id:
            The value to assign to the tenant_id property of this AuditEvent.
        :type tenant_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AuditEvent.
        :type compartment_id: str

        :param compartment_name:
            The value to assign to the compartment_name property of this AuditEvent.
        :type compartment_name: str

        :param event_id:
            The value to assign to the event_id property of this AuditEvent.
        :type event_id: str

        :param event_name:
            The value to assign to the event_name property of this AuditEvent.
        :type event_name: str

        :param event_source:
            The value to assign to the event_source property of this AuditEvent.
        :type event_source: str

        :param event_type:
            The value to assign to the event_type property of this AuditEvent.
        :type event_type: str

        :param event_time:
            The value to assign to the event_time property of this AuditEvent.
        :type event_time: datetime

        :param principal_id:
            The value to assign to the principal_id property of this AuditEvent.
        :type principal_id: str

        :param credential_id:
            The value to assign to the credential_id property of this AuditEvent.
        :type credential_id: str

        :param request_action:
            The value to assign to the request_action property of this AuditEvent.
        :type request_action: str

        :param request_id:
            The value to assign to the request_id property of this AuditEvent.
        :type request_id: str

        :param request_agent:
            The value to assign to the request_agent property of this AuditEvent.
        :type request_agent: str

        :param request_headers:
            The value to assign to the request_headers property of this AuditEvent.
        :type request_headers: dict(str, list[str])

        :param request_origin:
            The value to assign to the request_origin property of this AuditEvent.
        :type request_origin: str

        :param request_parameters:
            The value to assign to the request_parameters property of this AuditEvent.
        :type request_parameters: dict(str, list[str])

        :param request_resource:
            The value to assign to the request_resource property of this AuditEvent.
        :type request_resource: str

        :param response_headers:
            The value to assign to the response_headers property of this AuditEvent.
        :type response_headers: dict(str, list[str])

        :param response_status:
            The value to assign to the response_status property of this AuditEvent.
        :type response_status: str

        :param response_time:
            The value to assign to the response_time property of this AuditEvent.
        :type response_time: datetime

        :param response_payload:
            The value to assign to the response_payload property of this AuditEvent.
        :type response_payload: dict(str, object)

        :param user_name:
            The value to assign to the user_name property of this AuditEvent.
        :type user_name: str

        """
        self.swagger_types = {
            'tenant_id': 'str',
            'compartment_id': 'str',
            'compartment_name': 'str',
            'event_id': 'str',
            'event_name': 'str',
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
            'response_time': 'datetime',
            'response_payload': 'dict(str, object)',
            'user_name': 'str'
        }

        self.attribute_map = {
            'tenant_id': 'tenantId',
            'compartment_id': 'compartmentId',
            'compartment_name': 'compartmentName',
            'event_id': 'eventId',
            'event_name': 'eventName',
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
            'response_time': 'responseTime',
            'response_payload': 'responsePayload',
            'user_name': 'userName'
        }

        self._tenant_id = None
        self._compartment_id = None
        self._compartment_name = None
        self._event_id = None
        self._event_name = None
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
        self._response_payload = None
        self._user_name = None

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
    def compartment_name(self):
        """
        Gets the compartment_name of this AuditEvent.
        The name of the compartment. This value is the friendly name associated with compartmentId.
        This value can change, but the service logs the value that appeared at the time of the audit event.


        :return: The compartment_name of this AuditEvent.
        :rtype: str
        """
        return self._compartment_name

    @compartment_name.setter
    def compartment_name(self, compartment_name):
        """
        Sets the compartment_name of this AuditEvent.
        The name of the compartment. This value is the friendly name associated with compartmentId.
        This value can change, but the service logs the value that appeared at the time of the audit event.


        :param compartment_name: The compartment_name of this AuditEvent.
        :type: str
        """
        self._compartment_name = compartment_name

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
    def event_name(self):
        """
        Gets the event_name of this AuditEvent.
        The name of the event.
        Example: `LaunchInstance`


        :return: The event_name of this AuditEvent.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this AuditEvent.
        The name of the event.
        Example: `LaunchInstance`


        :param event_name: The event_name of this AuditEvent.
        :type: str
        """
        self._event_name = event_name

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

    @property
    def response_payload(self):
        """
        Gets the response_payload of this AuditEvent.
        Metadata of interest from the response payload. For example, the OCID of a resource.


        :return: The response_payload of this AuditEvent.
        :rtype: dict(str, object)
        """
        return self._response_payload

    @response_payload.setter
    def response_payload(self, response_payload):
        """
        Sets the response_payload of this AuditEvent.
        Metadata of interest from the response payload. For example, the OCID of a resource.


        :param response_payload: The response_payload of this AuditEvent.
        :type: dict(str, object)
        """
        self._response_payload = response_payload

    @property
    def user_name(self):
        """
        Gets the user_name of this AuditEvent.
        The name of the user or service. This value is the friendly name associated with principalId.


        :return: The user_name of this AuditEvent.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this AuditEvent.
        The name of the user or service. This value is the friendly name associated with principalId.


        :param user_name: The user_name of this AuditEvent.
        :type: str
        """
        self._user_name = user_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
