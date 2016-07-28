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

from . import models
from .response import Response
from .service_error import ServiceError

import logging
import ssl
import certifi
import io
import os
import re
import sys
import json
import mimetypes
import requests

from datetime import datetime
from datetime import date
from dateutil.parser import parse

try:
    # for python3
    from urllib.parse import quote, urlencode
except ImportError:
    # for python2
    from urllib import quote

logger = logging.getLogger(__name__)

def merge_type_mappings(*dictionaries):
    merged = {}
    for dictionary in dictionaries:
        merged.update(dictionary)
    return merged

class ApiClient(object):

    primitive_type_map = {
        'int': int,
        'float': float,
        'str': str,
        'bool': bool,
        'date': date,
        'datetime': datetime,
    }

    def __init__(self, config, signer):
        self.config = config
        self.signer = signer

        self.type_mappings = merge_type_mappings(self.primitive_type_map, models.core_type_mapping, models.identity_type_mapping)
        self._session = None

    @property
    def session(self):
        if self._session is None:
            self._session = requests.Session()
            self._session.verify = self.config.verify_ssl
        return self._session

    def call_api(self,
                   endpoint,
                   resource_path,
                   method,
                   path_params=None,
                   query_params=None,
                   header_params=None,
                   body=None,
                   response_type=None):
        """
        Makes the HTTP request and return the deserialized data.

        :param endpoint: URL of the endpoint
        :param resource_path: Path to the resourcd (e.g. /instance)
        :param method: HTTP method
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Request header params.
        :param body: Request body.
        :param response: Response data type.
        :return: A Response object, or throw in the case of an error.

        """

        if header_params:
            header_params = self.sanitize_for_serialization(header_params)

        header_params = header_params or {}

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

        if body:
            body = self.sanitize_for_serialization(body)
            body = json.dumps(body)

        url = endpoint + resource_path

        response = self.session.request(method,
                                 url,
                                 auth=self.signer,
                                 params=query_params,
                                 headers=header_params,
                                 data=body)

        is_error = response.status_code not in range(200, 299)
        if is_error:
            response_type = 'Error'

        # deserialize response data
        if response_type:
            deserialized_data = self.deserialize_response_data(response.content, response_type)
        else:
            deserialized_data = None

        if is_error:
            raise ServiceError(response.status_code, response.headers, deserialized_data)

        logger.debug("Response body: %s" % str(deserialized_data))

        return Response(response.status_code, response.headers, deserialized_data)

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
            value = unicode(data)
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


