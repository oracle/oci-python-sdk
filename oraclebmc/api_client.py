"""
This is a modified version of the api_client template from swagger-codegen,
where the original can be found at
https://github.com/swagger-api/swagger-codegen/blob/master/modules/swagger-codegen/src/main/resources/python/api_client.mustache.
The original license is below.

   Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   ref: https://github.com/swagger-api/swagger-codegen
"""

from __future__ import absolute_import
import http.client
import json
import logging
import platform
import re
import uuid
from datetime import date, datetime
from urllib.parse import quote

import requests
import six
from dateutil.parser import parse

from . import __version__, constants, exceptions, models
from .data_stream import DataStream
from .request import Request
from .response import Response
from .signer import ObjectUploadSigner


def merge_type_mappings(*dictionaries):
    merged = {}
    for dictionary in dictionaries:
        merged.update(dictionary)
    return merged

STREAM_RESPONSE_TYPE = 'stream'


class ApiClient(object):
    primitive_type_map = {
        'int': int,
        'float': float,
        'str': str,
        'bool': bool,
        'date': date,
        'datetime': datetime
    }

    def __init__(self, config, signer):
        self.config = config
        self.signer = signer

        self.type_mappings = merge_type_mappings(self.primitive_type_map,
                                                 models.core_type_mapping,
                                                 models.identity_type_mapping,
                                                 models.object_storage_type_mapping)
        self._session = None

        self.logger = logging.getLogger("%s.%s" % (__name__, str(id(self))))

        if self.config.log_requests:
            self.logger.addHandler(logging.StreamHandler())
            self.logger.setLevel(logging.DEBUG)

            http.client.HTTPConnection.debuglevel = 1
        else:
            http.client.HTTPConnection.debuglevel = 0

    @property
    def session(self):
        if self._session is None:
            self._session = requests.Session()
            self._session.verify = self.config.verify_ssl
        return self._session

    def call_api(self, endpoint, resource_path, method,
                 path_params=None,
                 query_params=None,
                 header_params=None,
                 body=None,
                 response_type=None,
                 enforce_content_headers=True):
        """
        Makes the HTTP request and return the deserialized data.

        :param endpoint: URL of the endpoint
        :param resource_path: Path to the resource (e.g. /instance)
        :param method: HTTP method
        :param path_params: (optional) Path parameters in the url.
        :param query_params: (optional) Query parameters in the url.
        :param header_params: (optional) Request header params.
        :param body: (optional) Request body.
        :param response_type: (optional) Response data type.
        :param enforce_content_headers: (optional) Whether content headers should be added for
            PUT and POST requests when not present.  Defaults to True.
        :return: A Response object, or throw in the case of an error.

        """

        if header_params:
            header_params = self.sanitize_for_serialization(header_params)

        header_params = header_params or {}

        header_params[constants.HEADER_CLIENT_INFO] = self.build_user_info()
        header_params[constants.HEADER_USER_AGENT] = self.build_user_agent()
        header_params[constants.HEADER_REQUEST_ID] = self.build_request_id()

        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            for k, v in path_params.items():
                replacement = quote(str(self.to_path_value(v)))
                resource_path = resource_path.\
                    replace('{' + k + '}', replacement)

        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = {k: self.to_path_value(v)
                            for k, v in query_params.items()}

        if body and header_params.get('content-type') == 'application/json':
            body = self.sanitize_for_serialization(body)
            body = json.dumps(body)

        url = endpoint + resource_path

        request = Request(
            method=method,
            url=url,
            query_params=query_params,
            header_params=header_params,
            body=body,
            response_type=response_type,
            enforce_content_headers=enforce_content_headers
        )

        return self.request(request)

    def request(self, request):
        self.logger.info("Request: %s %s" % (str(request.method), request.url))

        signer = self.signer
        if not request.enforce_content_headers:
            signer = ObjectUploadSigner(signer)

        stream = False
        if request.response_type == STREAM_RESPONSE_TYPE:
            stream = True

        response = self.session.request(
            request.method,
            request.url,
            auth=signer,
            params=request.query_params,
            headers=request.header_params,
            data=request.body,
            stream=stream)

        response_type = request.response_type
        is_error = not 200 <= response.status_code <= 299

        if is_error:
            response_type = 'Error'

        # deserialize response data
        if stream and not is_error:
            deserialized_data = DataStream(response)
        elif response_type:
            deserialized_data = self.deserialize_response_data(response.content, response_type)
        else:
            deserialized_data = None

        if is_error:
            raise exceptions.ServiceError(
                response.status_code,
                response.headers,
                deserialized_data)

        self.logger.info("Response status: %s" % str(response.status_code))

        return Response(response.status_code, response.headers, deserialized_data, request)

    # Builds the client info string to be sent with each request.
    def build_request_id(self):
        return str(uuid.uuid4()).replace('-', '').upper()

    # Builds the client info string to be sent with each request.
    def build_user_info(self):
        return "Oracle-PythonSDK/{}".format(__version__)

    # Build the user agent string to be send with each request.
    def build_user_agent(self):
        # Example: Oracle-PythonSDK/0.0.2 (python 3.5.2; x86_64-Darwin)
        agent = "{} (python {}; {}-{})".format(
            self.build_user_info(),
            platform.python_version(),
            platform.machine(),
            platform.system()
        )

        if self.config.additional_user_agent:
            agent = "{} {}".format(agent, self.config.additional_user_agent)

        return agent

    def to_path_value(self, obj):
        """
        Takes value and turn it into a string suitable for inclusion in
        the path, by url-encoding.

        :param obj: object or string value.

        :return string: quoted value.
        """
        if type(obj) == list:
            return ','.join(obj)
        else:
            return str(obj)

    def sanitize_for_serialization(self, obj):
        """
        Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        types = (str, int, float, bool, tuple)

        if isinstance(obj, type(None)):
            return None
        elif isinstance(obj, types):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()
        else:
            if isinstance(obj, dict):
                obj_dict = obj
            else:
                obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                            for attr, _ in obj.swagger_types.items()
                            if getattr(obj, attr) is not None}

            return {key: self.sanitize_for_serialization(val)
                    for key, val in obj_dict.items()}

    def deserialize_response_data(self, response_data, response_type):
        """
        Deserializes response into an object.

        :param response: object to be deserialized.
        :param response_type: class literal for
            deserialzied object, or string of class name.

        :return: deserialized object.
        """

        # In the python 3, the response.data is bytes.
        # we need to decode it to string.
        if response_data:
            response_data = response_data.decode('utf8')

        try:
            data = json.loads(response_data)
        except ValueError:
            data = response_data

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, cls):
        """
        Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param cls: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if type(cls) == str:
            if cls.startswith('list['):
                sub_kls = re.match('list\[(.*)\]', cls).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if cls.startswith('dict('):
                sub_kls = re.match('dict\(([^,]*), (.*)\)', cls).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in data.items()}

            cls = self.type_mappings[cls]

            if hasattr(cls, 'get_subtype'):
                # Use the discriminator value to get the correct subtype.
                cls = cls.get_subtype(data)
                cls = self.type_mappings[cls]

        if cls in [int, float, str, bool]:
            return self.__deserialize_primitive(data, cls)
        elif cls == object:
            return data
        elif cls == date:
            return self.__deserialize_date(data)
        elif cls == datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, cls)

    def __deserialize_primitive(self, data, cls):
        """
        Deserializes string to primitive type.

        :param data: str.
        :param cls: class literal.

        :return: int, float, str, bool.
        """
        try:
            value = cls(data)
        except UnicodeEncodeError:
            value = six.u(data)
        except TypeError:
            value = data
        return value

    def __deserialize_date(self, string):
        """
        Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise Exception("Failed to parse `{0}` into a date object".format(string))

    def __deserialize_datatime(self, string):
        """
        Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise Exception("Failed to parse `{0}` into a datetime object".format(string))

    def __deserialize_model(self, data, cls):
        """
        Deserializes list or dict to model.

        :param data: dict, list.
        :param cls: class literal.
        :return: model object.
        """
        instance = cls()

        for attr, attr_type in instance.swagger_types.items():
            property = instance.attribute_map[attr]
            if property in data:
                value = data[property]
                setattr(instance, attr, self.__deserialize(value, attr_type))

        return instance
