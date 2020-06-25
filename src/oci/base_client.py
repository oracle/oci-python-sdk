# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import
import json
import logging
import platform
import pytz
import random
import os
import re
import string
import uuid
# This was added to address thread safety issues with datetime.strptime
# See https://bugs.python.org/issue7980.
import _strptime  # noqa: F401
from datetime import date, datetime
from timeit import default_timer as timer

from oci._vendor import requests, six
from dateutil.parser import parse
from dateutil import tz

from . import constants, exceptions, regions
from .auth import signers
from .config import get_config_value_or_default, validate_config
from .request import Request
from .response import Response
from .version import __version__
from .util import NONE_SENTINEL, Sentinel
missing = Sentinel("Missing")

USER_INFO = "Oracle-PythonSDK/{}".format(__version__)

DICT_VALUE_TYPE_REGEX = re.compile('dict\(str, (.+?)\)$')  # noqa: W605
LIST_ITEM_TYPE_REGEX = re.compile('list\[(.+?)\]$')  # noqa: W605


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


def utc_now():
    return " " + str(datetime.utcnow()) + ": "


def is_http_log_enabled(is_enabled):
    if is_enabled:
        six.moves.http_client.HTTPConnection.debuglevel = 1
    else:
        six.moves.http_client.HTTPConnection.debuglevel = 0


STREAM_RESPONSE_TYPE = 'stream'
BYTES_RESPONSE_TYPE = 'bytes'

# Default timeout value(second)
DEFAULT_CONNECTION_TIMEOUT = 10.0
DEFAULT_READ_TIMEOUT = 60.0

# The keys here correspond to the Swagger collection format values described here: https://swagger.io/docs/specification/2-0/describing-parameters/
# and the values represent delimiters we'll use between values of the collection when placing those values in the query string.
#
# Note that the 'multi' type has no delimiter since in the query string we'll want to repeat the same query string param key but
# with different values each time (e.g. myKey=val1&myKey=val2), whereas for the other types we will only pass in a single
# key=value in the query string, where the "value" is the members of the collecction with a given delimiter.
VALID_COLLECTION_FORMAT_TYPES = {
    'multi': None,
    'csv': ',',
    'tsv': '\t',
    'ssv': ' ',
    'pipes': '|'
}


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

    def __init__(self, service, config, signer, type_mapping, **kwargs):
        validate_config(config, signer=signer)
        self.signer = signer

        # Default to true (is a regional client) if there is nothing explicitly set. Regional
        # clients allow us to call set_region and that'll also set the endpoint. For non-regional
        # clients we require an endpoint
        self.regional_client = kwargs.get('regional_client', True)

        self._endpoint = None
        self._base_path = kwargs.get('base_path')
        self.service_endpoint_template = kwargs.get('service_endpoint_template')

        if self.regional_client:
            if kwargs.get('service_endpoint'):
                self.endpoint = kwargs.get('service_endpoint')
            else:
                region_to_use = None
                if 'region' in config and config['region']:
                    region_to_use = config.get('region')
                elif hasattr(signer, 'region'):
                    region_to_use = signer.region

                self.endpoint = regions.endpoint_for(
                    service,
                    service_endpoint_template=self.service_endpoint_template,
                    region=region_to_use,
                    endpoint=config.get('endpoint'))
        else:
            if not kwargs.get('service_endpoint'):
                raise exceptions.MissingEndpointForNonRegionalServiceClientError('An endpoint must be provided for a non-regional service client')
            self.endpoint = kwargs.get('service_endpoint')

        self.service = service
        self.complex_type_mappings = type_mapping
        self.type_mappings = merge_type_mappings(self.primitive_type_map, type_mapping)
        self.session = requests.Session()

        timeout_value_in_kwargs = kwargs.get('timeout')
        self.timeout = timeout_value_in_kwargs if timeout_value_in_kwargs else (DEFAULT_CONNECTION_TIMEOUT, DEFAULT_READ_TIMEOUT)

        self.user_agent = build_user_agent(get_config_value_or_default(config, "additional_user_agent"))

        self.logger = logging.getLogger("{}.{}".format(__name__, id(self)))
        self.logger.addHandler(logging.NullHandler())
        if get_config_value_or_default(config, "log_requests"):
            self.logger.disabled = False
            self.logger.setLevel(logging.DEBUG)
            is_http_log_enabled(True)
        else:
            self.logger.disabled = True
            is_http_log_enabled(False)

        self.skip_deserialization = kwargs.get('skip_deserialization')

    @property
    def endpoint(self):
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        if self._base_path == '/':
            # If it's just the root path then use the endpoint as-is
            self._endpoint = endpoint
        elif self._base_path and not (endpoint.endswith(self._base_path) or endpoint.endswith('{}/'.format(self._base_path))):
            # Account for formats like https://iaas.us-phoenix-1.oraclecloud.com/20160918 and
            # https://iaas.us-phoenix-1.oraclecloud.com/20160918/ as they should both be fine
            self._endpoint = '{}{}'.format(endpoint, self._base_path)
        else:
            self._endpoint = endpoint

    def set_region(self, region):
        if self.regional_client:
            self.endpoint = regions.endpoint_for(self.service, service_endpoint_template=self.service_endpoint_template, region=region)
        else:
            raise TypeError('Setting the region is not allowed for non-regional service clients. You must instead set the endpoint')

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

        # ObjectStorage PutObject and UploadPart require Content-Length as
        # int, but requests requires it as a string.  All the headers
        # have been prepared for serialization at this point
        if header_params.get('Content-Length', missing) is not missing:
            header_params['Content-Length'] = str(header_params['Content-Length'])

        header_params[constants.HEADER_CLIENT_INFO] = USER_INFO
        header_params[constants.HEADER_USER_AGENT] = self.user_agent

        if header_params.get(constants.HEADER_REQUEST_ID, missing) is missing:
            header_params[constants.HEADER_REQUEST_ID] = self.build_request_id()

        # This allows for testing with "fake" database resources.
        opc_host_serial = os.environ.get('OCI_DB_OPC_HOST_SERIAL')
        if opc_host_serial:
            header_params['opc-host-serial'] = opc_host_serial

        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            for k, v in path_params.items():
                replacement = six.moves.urllib.parse.quote(str(self.to_path_value(v)))
                resource_path = resource_path.\
                    replace('{' + k + '}', replacement)

        if query_params:
            query_params = self.process_query_params(query_params)

        if body is not None and header_params.get('content-type') == 'application/json':
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

        if isinstance(self.signer, signers.InstancePrincipalsSecurityTokenSigner) or \
                isinstance(self.signer, signers.ResourcePrincipalsFederationSigner) or \
                isinstance(self.signer, signers.EphemeralResourcePrincipalSigner):
            call_attempts = 0
            while call_attempts < 2:
                try:
                    return self.request(request)
                except exceptions.ServiceError as e:
                    call_attempts += 1
                    if e.status == 401 and call_attempts < 2:
                        self.signer.refresh_security_token()
                    else:
                        raise
        else:
            start = timer()
            response = self.request(request)
            end = timer()
            self.logger.debug('time elapsed for request: {}'.format(str(end - start)))
            return response

    def generate_collection_format_param(self, param_value, collection_format_type):
        if param_value is missing:
            return missing

        if collection_format_type not in VALID_COLLECTION_FORMAT_TYPES:
            raise ValueError('Invalid collection format type {}. Valid types are: {}'.format(collection_format_type, list(VALID_COLLECTION_FORMAT_TYPES.keys())))

        if collection_format_type == 'multi':
            return param_value
        else:
            return VALID_COLLECTION_FORMAT_TYPES[collection_format_type].join(param_value)

    def process_query_params(self, query_params):
        query_params = self.sanitize_for_serialization(query_params)

        processed_query_params = {}
        for k, v in query_params.items():
            # First divide our query params into ones where the param value is "simple" (not a dict or list), a list or a dict. Since we're
            # executing after sanitize_for_serialization has been called it's dicts, lists or primitives all the way down.
            #
            # The params where the value is a dict are, for example, tags we need to handle differently for inclusion
            # in the query string.
            #
            # The params where the value is a list are multivalued parameters in the query string.
            #
            # An example query_params is:
            #
            #   {
            #       "stuff": "things",
            #       "collectionFormat": ["val1", "val2", "val3"]
            #       "definedTags": { "tag1": ["val1", "val2", "val3"], "tag2": ["val1"] },
            #       "definedTagsExists": { "tag3": True, "tag4": True }
            #   }
            #
            # And we can categorize the params as:
            #
            #   Simple: "stuff":"things"
            #   List: "collectionFormat": ["val1", "val2", "val3"]
            #   Dict: "definedTags": { "tag1": ["val1", "val2", "val3"], "tag2": ["val1"] }, "definedTagsExists": { "tag3": True, "tag4": True }
            if not isinstance(v, dict) and not isinstance(v, list):
                processed_query_params[k] = self.to_path_value(v)
            elif isinstance(v, list):
                # The requests library supports lists to represent multivalued params natively
                # (http://docs.python-requests.org/en/master/api/#requests.Session.params) so we just have to assign
                # the list to the key (where the key is the query string param key)
                processed_query_params[k] = v
            else:
                # If we are here then we either have:
                #
                #   1) a dict where the value is an array. The requests library supports lists to represent multivalued params
                #      natively (http://docs.python-requests.org/en/master/api/#requests.Session.params) so we just have to
                #      manipulate things into the right key. In the case of something like:
                #
                #           "definedTags": { "tag1": ["val1", "val2", "val3"], "tag2": ["val1"] }
                #
                #      What we want is to end up with:
                #
                #           "definedTags.tag1": ["val1", "val2", "val3"], "definedTags.tag2": ["val1"]
                #
                #   2) a dict where the value is not an array and in this case we just explode out the content. For example if we have:
                #
                #           "definedTagsExists": { "tag3": True, "tag4": True }
                #
                #       What we'll end up with is:
                #
                #           "definedTagsExists.tag3": True, "definedTagsExists.tag4": True
                for inner_key, inner_val in v.items():
                    processed_query_params['{}.{}'.format(k, inner_key)] = inner_val

        return processed_query_params

    def request(self, request):
        self.logger.info(utc_now() + "Request: %s %s" % (str(request.method), request.url))

        signer = self.signer
        if not request.enforce_content_headers:
            signer = signer.without_content_headers

        stream = False
        if request.response_type == STREAM_RESPONSE_TYPE:
            stream = True

        try:
            start = timer()
            response = self.session.request(
                request.method,
                request.url,
                auth=signer,
                params=request.query_params,
                headers=request.header_params,
                data=request.body,
                stream=stream,
                timeout=self.timeout)
            end = timer()
            if request.header_params[constants.HEADER_REQUEST_ID]:
                self.logger.debug(utc_now() + 'time elapsed for request {}: {}'.format(request.header_params[constants.HEADER_REQUEST_ID], str(end - start)))
            if response and hasattr(response, 'elapsed'):
                self.logger.debug(utc_now() + "time elapsed in response: " + str(response.elapsed))
        except requests.exceptions.ConnectTimeout as e:
            raise exceptions.ConnectTimeout(e)
        except requests.exceptions.RequestException as e:
            raise exceptions.RequestException(e)

        response_type = request.response_type
        self.logger.debug(utc_now() + "Response status: %s" % str(response.status_code))

        if not 200 <= response.status_code <= 299:
            self.raise_service_error(request, response)

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

        resp = Response(response.status_code, response.headers, deserialized_data, request)
        self.logger.debug(utc_now() + "Response returned")
        return resp

    # Builds the client info string to be sent with each request.
    def build_request_id(self):
        return str(uuid.uuid4()).replace('-', '').upper()

    def add_opc_retry_token_if_needed(self, header_params, retry_token_length=30):
        if 'opc-retry-token' not in header_params:
            header_params['opc-retry-token'] = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(retry_token_length))

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

    def sanitize_for_serialization(self, obj, declared_type=None, field_name=None):
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
        types = (six.string_types, six.integer_types, float, bool, type(None))

        declared_swagger_type_to_acceptable_python_types = {
            'str': six.string_types,
            'bool': bool,
            'int': (float, six.integer_types),
            'float': (float, six.integer_types)
        }

        # if there is a declared type for this obj, then validate that obj is of that type. None types (either None or the NONE_SENTINEL) are not validated but
        # instead passed through
        if declared_type and not self.is_none_or_none_sentinel(obj):
            if declared_type.startswith('dict(') and not isinstance(obj, dict):
                self.raise_type_error_serializing_model(field_name, obj, declared_type)
            elif declared_type.startswith('list[') and not (isinstance(obj, list) or isinstance(obj, tuple)):
                self.raise_type_error_serializing_model(field_name, obj, declared_type)
            elif declared_type in self.complex_type_mappings:
                # if its supposed to be one of our models, it can either be an instance of that model OR a dict
                if not isinstance(obj, dict) and not isinstance(obj, self.complex_type_mappings[declared_type]):
                    self.raise_type_error_serializing_model(field_name, obj, declared_type)
            elif declared_type in declared_swagger_type_to_acceptable_python_types and not isinstance(obj, declared_swagger_type_to_acceptable_python_types[declared_type]):
                # if its a primitive with corresponding acceptable python types, validate that obj is an instance of one of those acceptable types
                self.raise_type_error_serializing_model(field_name, obj, declared_type)

        if isinstance(obj, types):
            return obj
        elif obj is NONE_SENTINEL:
            return None
        elif isinstance(obj, list) or isinstance(obj, tuple):
            return [self.sanitize_for_serialization(
                sub_obj,
                self.extract_list_item_type_from_swagger_type(declared_type) if declared_type else None,
                field_name + '[*]' if field_name else None)
                for sub_obj in obj]
        elif isinstance(obj, datetime):
            if not obj.tzinfo:
                obj = pytz.utc.localize(obj)
            return obj.astimezone(pytz.utc).isoformat().replace('+00:00', 'Z')
        elif isinstance(obj, date):
            return obj.isoformat()
        else:
            if isinstance(obj, dict):
                obj_dict = obj

                keys_to_types_and_field_name = None

                # if there is a declared type, then we can use that to validate the types of values in the dict
                if declared_type:
                    dict_value_type = self.extract_dict_value_type_from_swagger_type(declared_type)
                    keys_to_types_and_field_name = {k: (dict_value_type, k) for k in obj_dict}
            else:
                # at this point we are assuming it is one of our models with swagger_types so explicitly throw if its not to give a better error
                if not hasattr(obj, 'swagger_types'):
                    raise TypeError('Not able to serialize data: {} of type: {} in field: {}'.format(str(obj), type(obj).__name__, field_name))

                obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                            for attr, _ in obj.swagger_types.items()
                            if getattr(obj, attr) is not None}

                keys_to_types_and_field_name = {obj.attribute_map[attr]: (swagger_type, attr) for attr, swagger_type in six.iteritems(obj.swagger_types)}

            sanitized_dict = {}
            for key, val in six.iteritems(obj_dict):
                value_declared_type = None
                inner_field_name = key
                if keys_to_types_and_field_name:
                    value_declared_type = keys_to_types_and_field_name[key][0]
                    inner_field_name = keys_to_types_and_field_name[key][1]

                inner_field_name = '{}.{}'.format(field_name, inner_field_name) if field_name else inner_field_name
                sanitized_dict[key] = self.sanitize_for_serialization(val, value_declared_type, inner_field_name)

            return sanitized_dict

    def is_none_or_none_sentinel(self, obj):
        return (obj is None) or (obj is NONE_SENTINEL)

    def raise_type_error_serializing_model(self, field_name, obj, declared_type):
        raise TypeError('Field {} with value {} was expected to be of type {} but was of type {}'.format(field_name, str(obj), declared_type, type(obj).__name__))

    def extract_dict_value_type_from_swagger_type(self, swagger_type):
        m = DICT_VALUE_TYPE_REGEX.search(swagger_type)

        result = None
        if m:
            result = m.group(1)

        return result

    def extract_list_item_type_from_swagger_type(self, swagger_type):
        m = LIST_ITEM_TYPE_REGEX.search(swagger_type)

        result = None
        if m:
            result = m.group(1)

        return result

    def raise_service_error(self, request, response):
        deserialized_data = self.deserialize_response_data(response.content, 'object')
        service_code = None
        message = None

        if isinstance(deserialized_data, dict):
            service_code = deserialized_data.get('code')
            message = deserialized_data.get('message')
        else:
            # Deserialized data should be a string if we couldn't deserialize into a dict (i.e. it failed
            # json.loads()). There could still be error information of value to the customer, so instead
            # of black holing the message, just put it in the error
            message = deserialized_data

        raise exceptions.ServiceError(
            response.status_code,
            service_code,
            response.headers,
            message,
            original_request=request)

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

        try:
            json_response = json.loads(response_data)
            # Load everything as JSON and then verify that the object returned
            # is a string (six.text_type) if the response type is a string.
            # This is matches the previous behavior, which happens to strip
            # the embedded quotes in the get_namespace response.
            # There is the potential that an API will declare that it returns
            # a string and the string will be a valid JSON Object. In that case
            # we do not update the response_data with the json_response.
            # If we do later steps will fail because they are expecting the
            # response_data to be a string.
            if response_type != "str" or type(json_response) == six.text_type:
                response_data = json_response
        except ValueError:
            pass

        if self.skip_deserialization:
            return response_data
        else:
            start = timer()
            res = self.__deserialize(response_data, response_type)
            end = timer()
            self.logger.debug(utc_now() + 'python SDK time elapsed for deserializing: {}'.format(str(end - start)))
            return res

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
            sub_kls = re.match('list\[(.*)\]', cls).group(1)  # noqa: W605
            return [self.__deserialize(sub_data, sub_kls)
                    for sub_data in data]

        if cls.startswith('dict('):
            sub_kls = re.match('dict\(([^,]*), (.*)\)', cls).group(2)  # noqa: W605
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
            # If this parser creates a date without raising an exception
            # then the time zone is utc and needs to be set.
            naivedatetime = datetime.strptime(string, "%Y-%m-%dT%H:%M:%S.%fZ")
            awaredatetime = naivedatetime.replace(tzinfo=tz.tzutc())
            return awaredatetime

        except ValueError:
            try:
                return parse(string)
            except ImportError:
                return string
            except ValueError:
                raise Exception("Failed to parse `{0}` into a datetime object".format(string))
        except ImportError:
            return string

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
