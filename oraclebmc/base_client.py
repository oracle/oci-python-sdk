# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import
import json
import logging
import platform
import re
import six.moves
import uuid
from datetime import date, datetime

import requests
import six
from dateutil.parser import parse

from . import constants, exceptions, regions
from .config import get_config_value_or_default, validate_config
from .request import Request
from .response import Response
from .version import __version__

USER_INFO = "Oracle-PythonSDK/{}".format(__version__)


def merge_type_mappings(*dictionaries):
    merged = {}
    for dictionary in dictionaries:
        merged.update(dictionary)
    return merged


def build_user_agent(extra=""):
    agent = "{} (python {}; {}-{}) {}".format(
        USER_INFO,
        platform.python_version(),
        platform.machine(),
        platform.system(),
        (extra or "")
    )
    return agent.strip()


STREAM_RESPONSE_TYPE = 'stream'
BYTES_RESPONSE_TYPE = 'bytes'


class BaseClient(object):
    primitive_type_map = {
        'int': int,
        'float': float,
        'str': six.u,
        'bool': bool,
        'date': date,
        'datetime': datetime,
        "object": object
    }

    def __init__(self, service, config, signer, type_mapping):
        validate_config(config)
        self.signer = signer
        self.endpoint = regions.endpoint_for(
            service,
            region=config.get("region"),
            endpoint=config.get("endpoint"))

        self.type_mappings = merge_type_mappings(self.primitive_type_map, type_mapping)
        self.session = requests.Session()
        self.user_agent = build_user_agent(get_config_value_or_default(config, "additional_user_agent"))

        self.logger = logging.getLogger("{}.{}".format(__name__, id(self)))
        self.logger.addHandler(logging.NullHandler())
        if get_config_value_or_default(config, "log_requests"):
            self.logger.setLevel(logging.DEBUG)
            six.moves.http_client.HTTPConnection.debuglevel = 1
        else:
            six.moves.http_client.HTTPConnection.debuglevel = 0

    def call_api(self, resource_path, method,
                 path_params=None,
                 query_params=None,
                 header_params=None,
                 body=None,
                 response_type=None,
                 enforce_content_headers=True):
        """
        Makes the HTTP request and return the deserialized data.

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

        header_params[constants.HEADER_CLIENT_INFO] = USER_INFO
        header_params[constants.HEADER_USER_AGENT] = self.user_agent
        header_params[constants.HEADER_REQUEST_ID] = self.build_request_id()

        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            for k, v in path_params.items():
                replacement = six.moves.urllib.parse.quote(str(self.to_path_value(v)))
                resource_path = resource_path.\
                    replace('{' + k + '}', replacement)

        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = {k: self.to_path_value(v)
                            for k, v in query_params.items()}

        if body and header_params.get('content-type') == 'application/json':
            body = self.sanitize_for_serialization(body)
            body = json.dumps(body)

        url = self.endpoint + resource_path

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
            signer = signer.without_content_headers

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
        self.logger.debug("Response status: %s" % str(response.status_code))

        if not 200 <= response.status_code <= 299:
            self.raise_service_error(response)

        if stream:
            # Don't unpack a streaming response body
            deserialized_data = response
        elif response_type == BYTES_RESPONSE_TYPE:
            # Don't deserialize data responses.
            deserialized_data = response.content
        elif response_type:
            deserialized_data = self.deserialize_response_data(response.content, response_type)
        else:
            deserialized_data = None

        return Response(response.status_code, response.headers, deserialized_data, request)

    # Builds the client info string to be sent with each request.
    def build_request_id(self):
        return str(uuid.uuid4()).replace('-', '').upper()

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

        If obj is str, int, float, bool, None, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        types = (six.string_types, int, float, bool, type(None))

        if isinstance(obj, types):
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

    def raise_service_error(self, response):
        deserialized_data = self.deserialize_response_data(response.content, 'object')
        service_code = None
        message = None

        if isinstance(deserialized_data, dict):
            service_code = deserialized_data.get('code')
            message = deserialized_data.get('message')

        raise exceptions.ServiceError(
            response.status_code,
            service_code,
            response.headers,
            message)

    def deserialize_response_data(self, response_data, response_type):
        """
        Deserializes response into an object.

        :param response_data: object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """

        # response.content is always bytes
        response_data = response_data.decode('utf8')

        # TODO: not all valid json strings should be loaded as JSON.
        # TODO: conditionally load json based on response_type.
        try:
            response_data = json.loads(response_data)
        except ValueError:
            pass

        return self.__deserialize(response_data, response_type)

    def __deserialize(self, data, cls):
        """
        Deserialize a dict, list, or str into an object.

        :param data: dict, list or str
        :param cls: string of class name

        :return: object.
        """
        if data is None:
            return None

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
            cls = cls.get_subtype(data)  # get_subtype returns a str
            cls = self.type_mappings[cls]

        if cls in [int, float, six.u, bool]:
            return self.__deserialize_primitive(data, cls)
        elif cls == object:
            return data
        elif cls == date:
            return self.__deserialize_date(data)
        elif cls == datetime:
            return self.__deserialize_datetime(data)
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

    def __deserialize_datetime(self, string):
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
