# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import base64
import json
import requests
import uuid
import oci.util as oci_util
from . import util
from datetime import datetime

SERVICE_HOSTNAME = 'localhost'
SERVICE_PORT = '8090'
SERVICE_ROOT_URL = 'http://{hostname}:{port}/SDKTestingService'.format(hostname=SERVICE_HOSTNAME, port=SERVICE_PORT)
SERVICE_LANGUAGE = "Python"


class TestingServiceClient:
    def get_test_config(self, service_name, client_name, api_name):
        """
        Gets testing config from testing service. (oci config)

        :param str service_name
            The name of the service to request config object for.

        :param str client_name
            The client of the API to request config object for.

        :param str api_name
            The name of the API to request config object for.

        :return: A dicts containing config properties to call the API specified by service_name, client_name and api_name

        """
        service_name = service_name.replace('_', '').lower()

        params = {
            'serviceName': service_name,
            'apiName': api_name,
            'lang': SERVICE_LANGUAGE,
            'clientName': client_name
        }

        url = '{service_root_url}/config'.format(service_root_url=SERVICE_ROOT_URL)
        response = requests.get(url, params=params)
        response_content = response.content.decode('UTF-8')
        try:
            return json.loads(response_content)
        except json.decoder.JSONDecodeError as e:
            print('Failed to parse testing service response as valid JSON. Response: ' + response_content)
            raise e

    def get_requests(self, service_name, api_name):
        """
        Gets a list of requests from the testing service to be used in calling the API specified by service_name and api_name.

        :param str service_name
            The name of the service to request input parameters for. The testing service uses the following template to
            construct the Java SDK request object:
            String.format("com.oracle.bmc.%s.requests.%sRequest", serviceName, apiName);

        :param str api_name
            The name of the API to request input parameters for. The testing service uses the following template to
            construct the Java SDK request object:
            String.format("com.oracle.bmc.%s.requests.%sRequest", serviceName, apiName);

        :return: A list of dicts containing parameters to call the API specified by service_name and api_name

        """
        if not self.session_id:
            raise RuntimeError('Must call create_session before calling get_requests.')

        # standardize service name to convention for Java SDK model namespaces (all lower case one word)
        service_name = service_name.replace('_', '').lower()

        params = {
            'serviceName': service_name,
            'apiName': api_name,
            'lang': SERVICE_LANGUAGE,
            'sessionId': self.session_id
        }

        url = '{service_root_url}/request'.format(service_root_url=SERVICE_ROOT_URL)
        response = requests.get(url, params=params)
        response_content = response.content.decode('UTF-8')
        try:
            return json.loads(response_content)
        except json.decoder.JSONDecodeError as e:
            print('Failed to parse testing service response as valid JSON. Response: ' + response_content)
            raise e

    def validate_result(self, service_name, api_name, container_id, request, oci_responses, service_error, data_field_name, is_delete_operation, is_paginated_call):
        """
        Calls the testing service to validate a Python response.

        :param str service_name
            The name of the service to request input parameters for. The testing service uses the following template to
            construct the Java SDK request object:
            String.format("com.oracle.bmc.%s.requests.%sRequest", serviceName, apiName);

        :param str api_name
            The name of the API to request input parameters for. The testing service uses the following template to
            construct the Java SDK request object:
            String.format("com.oracle.bmc.%s.requests.%sRequest", serviceName, apiName);

        :param str container_id:
            The ID of the current container.

        :param str request:
            The json content of the request object.

        :param [oci.response.Response] oci_responses:
            The response objects from oci services.

        :param ServiceError service_error:
            The service error from OCI services

        :param str data_field_name:
            The PythonSDK returns the main resource under the field name 'data' but we need to convert it to
            the name used in the Java SDK (e.g. for GetGroup data -> group)

        :param bool is_delete_operation:
            Is the current operation a delete operation

        :param bool is_paginated_call:
            Is the current operation a paginated call

        :return: None

        """
        # standardize service name to convention for Java SDK model namespaces (all lower case one word)
        java_package_name = service_name.replace('_', '').lower()
        request_class = 'com.oracle.bmc.{java_package_name}.requests.{api_name}Request'.format(java_package_name=java_package_name, api_name=api_name)
        response_class = 'com.oracle.bmc.{java_package_name}.responses.{api_name}Response'.format(java_package_name=java_package_name, api_name=api_name)

        success_url = '{service_root_url}/response'.format(service_root_url=SERVICE_ROOT_URL)
        error_url = '{service_root_url}/error'.format(service_root_url=SERVICE_ROOT_URL)
        data = {
            'containerId': container_id,
            'listResponse': is_paginated_call,
            'requestClass': request_class,
            'requestJson': json.dumps(request),
        }

        params = {
            "sessionId": self.session_id,
            "lang": SERVICE_LANGUAGE
        }

        response_types_keep_data_field_name = ['ListObjects',
                                               'TerraformVersionCollection',
                                               'MultipleTransferAppliances',
                                               'MultipleTransferDevices',
                                               'MultipleTransferPackages']

        if not service_error:
            if is_paginated_call:
                # response_class = 'java.util.List<com.oracle.bmc.{java_package_name}.responses.{api_name}Response>'.format(java_package_name=java_package_name, api_name=api_name)
                list_responses = []
                for oci_response in oci_responses:
                    # This is for specs that do not adhere to the API guidelines that explicitly model a schema that
                    # contains a list within the schema.  Example: AnnouncementClient#list_announcements()
                    if oci_response.request.response_type.startswith('list['):
                        data_field_name = 'items'
                    else:
                        data_field_name = util.camelize(oci_response.request.response_type, False)
                    list_responses.append(self.get_response_dictionary(oci_response, is_delete_operation, data_field_name))
                response_json = util.make_dict_keys_camel_case(list_responses, ['freeformTags', 'definedTags', 'systemTags'])
            else:
                oci_response = oci_responses[0]
                response_type = oci_response.request.response_type
                is_list_api = api_name.lower().startswith('list')
                if is_list_api or (response_type and response_type.startswith('list[') and response_type.endswith('Summary]')):
                    # Hack alert for object storage and resource manager!
                    if response_type and response_type not in response_types_keep_data_field_name:
                        data_field_name = 'items'
                # For BatchServiceClient#get_job_log()
                elif response_type in ['str', 'bytes']:
                    data_field_name = 'value'
                # For StreamClient#get_messages(), which is not considered a paginated call (no page param)
                elif response_type in ['list[Message]', 'list[MetricData]']:
                    data_field_name = 'items'
                response_dict = self.get_response_dictionary(oci_response, is_delete_operation, data_field_name)
                response_json = util.make_dict_keys_camel_case(response_dict, ['freeformTags', 'definedTags', 'systemTags'])

            data['responseJson'] = json.dumps(response_json)
            data['responseClass'] = response_class
            print('dataToValidate: {}'.format(json.dumps(data, indent=2)))
            response = requests.post(success_url, params=params, data=json.dumps(data))
        else:
            error = {}
            error['code'] = service_error.code
            error['statusCode'] = service_error.status
            error['message'] = service_error.message
            error['opcRequestId'] = service_error.request_id

            data['errorJson'] = json.dumps(error)
            print('errorToValidate: {}'.format(json.dumps(data, indent=2)))

            response = requests.post(error_url, params=params, data=json.dumps(data))

        # dump messages when testing service return 500 (all exceptions inside testing service)
        if response.status_code == 500:
            print('Testing service return 500: {content}'.format(content=response.content))

        assert response.status_code == 200, response.content
        assert len(response.content) == 0, response.content

    def get_response_dictionary(self, oci_response, is_delete_operation, data_field_name):
        if is_delete_operation:
            oci_response.data = {}
        print('data field name is ' + data_field_name)
        if data_field_name == 'stream':
            # for binary data, decode them first then put into inputStream
            response_dict = {"inputStream": str(base64.b64encode(oci_response.data.content).decode('utf-8'))}
            if hasattr(oci_response.data, 'content'):
                response_dict['contentLength'] = len(oci_response.data.content)
        elif data_field_name == 'value':
            # for value field (originally str or binary), decode to string
            try:
                val = oci_response.data.decode('utf-8')
            except (UnicodeDecodeError, AttributeError):
                val = oci_response.data
            response_dict = oci_util.to_dict({data_field_name: val})
        else:
            response_dict = oci_util.to_dict({data_field_name: oci_response.data})
        # response_dict = oci_util.to_dict({data_field_name: oci_response.data})
        response_dict['opcRequestId'] = oci_response.request_id
        if oci_response.next_page is not None:
            response_dict['opcNextPage'] = oci_response.next_page
        if 'opc-prev-page' in oci_response.headers:
            response_dict['opcPrevPage'] = oci_response.headers['opc-prev-page']
        if 'opc-previous-page' in oci_response.headers:
            response_dict['opcPreviousPage'] = oci_response.headers['opc-previous-page']
        if 'opc-next-cursor' in oci_response.headers:
            response_dict['opcNextCursor'] = oci_response.headers['opc-next-cursor']

        work_request_id = 'opc-work-request-id'
        if work_request_id in oci_response.headers:
            response_dict[util.camelize(work_request_id)] = oci_response.headers[work_request_id]

        if 'etag' in oci_response.headers:
            response_dict['eTag'] = oci_response.headers['etag']

        # For Analytics API
        if 'location' in oci_response.headers:
            response_dict['location'] = oci_response.headers['location']

        # For work requests and/or throttled responses
        if 'retry-after' in oci_response.headers:
            time_value = oci_response.headers['retry-after']
            if '.' in time_value:
                response_dict['retryAfter'] = float(time_value)
            else:
                response_dict['retryAfter'] = int(time_value)

        # For ComputeClient#get_console_history_content
        if 'opc-bytes-remaining' in oci_response.headers:
            response_dict['opcBytesRemaining'] = int(oci_response.headers['opc-bytes-remaining'])

        # For DataScienceClient
        if 'last-modified' in oci_response.headers:
            # Example format: 'Fri, 6 Mar 2065 12:06:55 GMT'
            native_datetime = datetime.strptime(oci_response.headers['last-modified'], "%a, %d %b %Y %H:%M:%S %Z")
            response_dict['lastModified'] = native_datetime.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        if 'content-disposition' in oci_response.headers:
            response_dict['contentDisposition'] = oci_response.headers['content-disposition']

        # For DnsClient
        if 'opc-total-items' in oci_response.headers:
            response_dict['opcTotalItems'] = int(oci_response.headers['opc-total-items'])
        # Hack to always add a notModified field for 304 response code support
        response_dict['notModified'] = False

        # For ObjectStorageClient
        if 'opc-client-request-id' in oci_response.headers:
            response_dict['opcClientRequestId'] = oci_response.headers['opc-client-request-id']
        if 'opc-multipart-md5' in oci_response.headers:
            response_dict['opcMultipartMd5'] = oci_response.headers['opc-multipart-md5']

        return response_dict

    def create_session(self):
        """
        Initializes a session with the testing service.

        """
        url = '{service_root_url}/sessions'.format(service_root_url=SERVICE_ROOT_URL)
        data = {'language': SERVICE_LANGUAGE}
        response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json', 'Accept': 'text/plain'})
        assert response.status_code == 200, 'Failed to create session. Response from testing service: {}'.format(response.content)

        session_id_response = response.content.decode('UTF-8')
        try:
            int(session_id_response)
        except ValueError as e:
            print('Failed to create session, did not receive valid session ID from testing service: {}'.format(session_id_response))
            raise e

        self.session_id = session_id_response
        print('Created session: {}'.format(self.session_id))
        return self.session_id

    def build_request_id(self):
        return str(uuid.uuid4()).replace('-', '').upper()

    def end_session(self):
        """
        Ends the existing session with the testing service.

        """
        if not self.session_id:
            raise RuntimeError('Must call create_session before calling end_session.')

        print('Ending session for {}'.format(self.session_id))
        url = '{service_root_url}/sessions/{session_id}'.format(service_root_url=SERVICE_ROOT_URL, session_id=self.session_id)
        response = requests.delete(url)
        assert response.status_code == 204, 'Failed to end session. Response: {}'.format(response.content)

    def is_api_enabled(self, service_name, api_name):
        """
        Checks if a given service_name / api_name is supported by the testing service and enabled for this client / language.

        :param str service_name
            The name of the service to request input parameters for. The testing service uses the following template to
            construct the Java SDK request object:
            String.format("com.oracle.bmc.%s.requests.%sRequest", serviceName, apiName);

        :param str api_name
            The name of the API to request input parameters for. The testing service uses the following template to
            construct the Java SDK request object:
            String.format("com.oracle.bmc.%s.requests.%sRequest", serviceName, apiName);

        :return: Whether or not this API is enabled in the testing service.

        """
        # standardize service name to convention for Java SDK model namespaces (all lower case one word)
        service_name = service_name.replace('_', '').lower()

        url = '{service_root_url}/request/enable'.format(service_root_url=SERVICE_ROOT_URL)
        params = {
            'lang': SERVICE_LANGUAGE,
            'serviceName': service_name,
            'apiName': api_name
        }

        response = requests.get(url, params=params)
        assert response.status_code == 200, response.content

        response_content = response.content.decode('UTF-8')
        try:
            api_enabled_response = json.loads(response_content)
        except json.decoder.JSONDecodeError as e:
            print('Failed to parse testing service response as valid JSON. Response: {}'.format(response_content))
            raise e

        assert api_enabled_response is True or api_enabled_response is False, 'Received invalid response from testing service, should be true or false. Response: {}'.format(api_enabled_response)
        return api_enabled_response

    def get_endpoint(self, service_name, client_name, api_name):
        # standardize service name to convention for Java SDK model namespaces (all lower case one word)
        service_name = service_name.replace('_', '').lower()

        url = '{service_root_url}/endpoint'.format(service_root_url=SERVICE_ROOT_URL)
        params = {
            'sessionId': self.session_id,
            'serviceName': service_name,
            'clientName': client_name,
            'lang': SERVICE_LANGUAGE,
            'apiName': api_name
        }

        response = requests.get(url, params=params)
        assert response.status_code == 200, response.content
        return response.content.decode('UTF-8')
