# coding: utf-8

# This is a modified version of the same template from swagger-codegen.
# The original can be found at https://github.com/swagger-api/swagger-codegen.
# The original license is below.
#
#     Copyright 2016 SmartBear Software
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#     Ref: https://github.com/swagger-api/swagger-codegen

from __future__ import absolute_import

# python 2 and python 3 compatibility library
from six import iteritems
from io import IOBase

from ..signer import Signer
from ..api_client import ApiClient

class ObjectStorageApi(object):

    def __init__(self, config):
        signer = Signer(config.tenancy, config.user, config.fingerprint, config.key_file)
        self.api_client =  ApiClient(config, signer)


    def create_bucket(self, namespace_name, create_bucket_details, **kwargs):
        """
        CreateBucket
        Create a bucket in the given namespace with a bucket name and optional user-defined metadata.\n

        :param str namespace_name: The top-level namespace used for the request. (required)
        :param CreateBucketDetails create_bucket_details: Request object for creating a bucket. (required)
        :param str opc_client_request_id: The client request ID for tracing
        :return: A Response object with data of type Bucket
        """

        all_params = ['namespace_name', 'create_bucket_details', 'opc_client_request_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_bucket" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'namespace_name' is set
        if ('namespace_name' not in params) or (params['namespace_name'] is None):
            raise ValueError("Missing the required parameter `namespace_name` when calling `create_bucket`")
        # verify the required parameter 'create_bucket_details' is set
        if ('create_bucket_details' not in params) or (params['create_bucket_details'] is None):
            raise ValueError("Missing the required parameter `create_bucket_details` when calling `create_bucket`")

        resource_path = '/n/{namespaceName}/b/'
        path_params = {}
        if 'namespace_name' in params:
            path_params['namespaceName'] = params['namespace_name']

        query_params = {}

        header_params = {}
        if 'opc_client_request_id' in params:
            header_params['opc-client-request-id'] = params['opc_client_request_id']

        body_params = None
        if 'create_bucket_details' in params:
            body_params = params['create_bucket_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_object_storage_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Bucket')
        return response

    def delete_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        DeleteBucket
        Delete a bucket if it is already empty.\n

        :param str namespace_name: The top-level namespace used for the request. (required)
        :param str bucket_name: The name of the bucket. (required)
        :param str if_match: The entity tag to match.
        :param str opc_client_request_id: The client request ID for tracing
        :return: A Response object with data of type None
        """

        all_params = ['namespace_name', 'bucket_name', 'if_match', 'opc_client_request_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bucket" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'namespace_name' is set
        if ('namespace_name' not in params) or (params['namespace_name'] is None):
            raise ValueError("Missing the required parameter `namespace_name` when calling `delete_bucket`")
        # verify the required parameter 'bucket_name' is set
        if ('bucket_name' not in params) or (params['bucket_name'] is None):
            raise ValueError("Missing the required parameter `bucket_name` when calling `delete_bucket`")

        resource_path = '/n/{namespaceName}/b/{bucketName}/'
        path_params = {}
        if 'namespace_name' in params:
            path_params['namespaceName'] = params['namespace_name']
        if 'bucket_name' in params:
            path_params['bucketName'] = params['bucket_name']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']
        if 'opc_client_request_id' in params:
            header_params['opc-client-request-id'] = params['opc_client_request_id']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_object_storage_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def delete_object(self, namespace_name, bucket_name, object_name, **kwargs):
        """
        DeleteObject
        Delete an object.\n

        :param str namespace_name: The top-level namespace used for the request. (required)
        :param str bucket_name: The name of the bucket. (required)
        :param str object_name: The name of the object. (required)
        :param str if_match: The entity tag to match.
        :param str opc_client_request_id: The client request ID for tracing
        :return: A Response object with data of type None
        """

        all_params = ['namespace_name', 'bucket_name', 'object_name', 'if_match', 'opc_client_request_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_object" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'namespace_name' is set
        if ('namespace_name' not in params) or (params['namespace_name'] is None):
            raise ValueError("Missing the required parameter `namespace_name` when calling `delete_object`")
        # verify the required parameter 'bucket_name' is set
        if ('bucket_name' not in params) or (params['bucket_name'] is None):
            raise ValueError("Missing the required parameter `bucket_name` when calling `delete_object`")
        # verify the required parameter 'object_name' is set
        if ('object_name' not in params) or (params['object_name'] is None):
            raise ValueError("Missing the required parameter `object_name` when calling `delete_object`")

        resource_path = '/n/{namespaceName}/b/{bucketName}/o/{objectName}'
        path_params = {}
        if 'namespace_name' in params:
            path_params['namespaceName'] = params['namespace_name']
        if 'bucket_name' in params:
            path_params['bucketName'] = params['bucket_name']
        if 'object_name' in params:
            path_params['objectName'] = params['object_name']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']
        if 'opc_client_request_id' in params:
            header_params['opc-client-request-id'] = params['opc_client_request_id']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_object_storage_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def get_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        GetBucket
        Get the current representation of the given bucket in the given namespace.\n

        :param str namespace_name: The top-level namespace used for the request. (required)
        :param str bucket_name: The name of the bucket. (required)
        :param str if_match: The entity tag to match.
        :param str if_none_match: The entity tag to avoid matching.
        :param str opc_client_request_id: The client request ID for tracing
        :return: A Response object with data of type Bucket
        """

        all_params = ['namespace_name', 'bucket_name', 'if_match', 'if_none_match', 'opc_client_request_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bucket" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'namespace_name' is set
        if ('namespace_name' not in params) or (params['namespace_name'] is None):
            raise ValueError("Missing the required parameter `namespace_name` when calling `get_bucket`")
        # verify the required parameter 'bucket_name' is set
        if ('bucket_name' not in params) or (params['bucket_name'] is None):
            raise ValueError("Missing the required parameter `bucket_name` when calling `get_bucket`")

        resource_path = '/n/{namespaceName}/b/{bucketName}/'
        path_params = {}
        if 'namespace_name' in params:
            path_params['namespaceName'] = params['namespace_name']
        if 'bucket_name' in params:
            path_params['bucketName'] = params['bucket_name']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']
        if 'if_none_match' in params:
            header_params['if-none-match'] = params['if_none_match']
        if 'opc_client_request_id' in params:
            header_params['opc-client-request-id'] = params['opc_client_request_id']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_object_storage_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Bucket')
        return response

    def get_namespace(self, **kwargs):
        """
        GetNamespace
        Get the name of the namespace for the user making the request. An account name must be unique, must start with a\nletter, and can have up to 15 lower case letters and numbers. You cannot use spaces and special characters.\n

        :param str opc_client_request_id: The client request ID for tracing
        :return: A Response object with data of type str
        """

        all_params = ['opc_client_request_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_namespace" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/n/'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_client_request_id' in params:
            header_params['opc-client-request-id'] = params['opc_client_request_id']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_object_storage_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='str')
        return response

    def get_object(self, namespace_name, bucket_name, object_name, **kwargs):
        """
        GetObject
        Get the metadata and body of an object.\n

        :param str namespace_name: The top-level namespace used for the request. (required)
        :param str bucket_name: The name of the bucket. (required)
        :param str object_name: The name of the object. (required)
        :param str if_match: The entity tag to match.
        :param str if_none_match: The entity tag to avoid matching.
        :param str opc_client_request_id: The client request ID for tracing
        :param str range: Optional byte range to fetch, follows https://tools.ietf.org/html/rfc7233#section-2.1. Note, only one byte range is supported.
        :return: A Response object with data of type stream
        """

        all_params = ['namespace_name', 'bucket_name', 'object_name', 'if_match', 'if_none_match', 'opc_client_request_id', 'range']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_object" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'namespace_name' is set
        if ('namespace_name' not in params) or (params['namespace_name'] is None):
            raise ValueError("Missing the required parameter `namespace_name` when calling `get_object`")
        # verify the required parameter 'bucket_name' is set
        if ('bucket_name' not in params) or (params['bucket_name'] is None):
            raise ValueError("Missing the required parameter `bucket_name` when calling `get_object`")
        # verify the required parameter 'object_name' is set
        if ('object_name' not in params) or (params['object_name'] is None):
            raise ValueError("Missing the required parameter `object_name` when calling `get_object`")

        resource_path = '/n/{namespaceName}/b/{bucketName}/o/{objectName}'
        path_params = {}
        if 'namespace_name' in params:
            path_params['namespaceName'] = params['namespace_name']
        if 'bucket_name' in params:
            path_params['bucketName'] = params['bucket_name']
        if 'object_name' in params:
            path_params['objectName'] = params['object_name']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']
        if 'if_none_match' in params:
            header_params['if-none-match'] = params['if_none_match']
        if 'opc_client_request_id' in params:
            header_params['opc-client-request-id'] = params['opc_client_request_id']
        if 'range' in params:
            header_params['range'] = params['range']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_object_storage_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='stream')
        return response

    def head_object(self, namespace_name, bucket_name, object_name, **kwargs):
        """
        HeadObject
        Get the user-defined metadata and entity tag for an object.\n

        :param str namespace_name: The top-level namespace used for the request. (required)
        :param str bucket_name: The name of the bucket. (required)
        :param str object_name: The name of the object. (required)
        :param str if_match: The entity tag to match.
        :param str if_none_match: The entity tag to avoid matching.
        :param str opc_client_request_id: The client request ID for tracing
        :return: A Response object with data of type None
        """

        all_params = ['namespace_name', 'bucket_name', 'object_name', 'if_match', 'if_none_match', 'opc_client_request_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_object" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'namespace_name' is set
        if ('namespace_name' not in params) or (params['namespace_name'] is None):
            raise ValueError("Missing the required parameter `namespace_name` when calling `head_object`")
        # verify the required parameter 'bucket_name' is set
        if ('bucket_name' not in params) or (params['bucket_name'] is None):
            raise ValueError("Missing the required parameter `bucket_name` when calling `head_object`")
        # verify the required parameter 'object_name' is set
        if ('object_name' not in params) or (params['object_name'] is None):
            raise ValueError("Missing the required parameter `object_name` when calling `head_object`")

        resource_path = '/n/{namespaceName}/b/{bucketName}/o/{objectName}'
        path_params = {}
        if 'namespace_name' in params:
            path_params['namespaceName'] = params['namespace_name']
        if 'bucket_name' in params:
            path_params['bucketName'] = params['bucket_name']
        if 'object_name' in params:
            path_params['objectName'] = params['object_name']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']
        if 'if_none_match' in params:
            header_params['if-none-match'] = params['if_none_match']
        if 'opc_client_request_id' in params:
            header_params['opc-client-request-id'] = params['opc_client_request_id']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_object_storage_api,
                                            resource_path,
                                            'HEAD',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def list_buckets(self, namespace_name, compartment_id, **kwargs):
        """
        ListBuckets
        Get a list of all the buckets in a namespace.\n

        :param str namespace_name: The top-level namespace used for the request. (required)
        :param str compartment_id: The compartment ID in which to create the bucket. (required)
        :param int limit: The maximum number of items to return.
        :param str page: The page at which to start retrieving results.
        :param str opc_client_request_id: The client request ID for tracing
        :return: A Response object with data of type list[Bucket]
        """

        all_params = ['namespace_name', 'compartment_id', 'limit', 'page', 'opc_client_request_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_buckets" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'namespace_name' is set
        if ('namespace_name' not in params) or (params['namespace_name'] is None):
            raise ValueError("Missing the required parameter `namespace_name` when calling `list_buckets`")
        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_buckets`")

        resource_path = '/n/{namespaceName}/b/'
        path_params = {}
        if 'namespace_name' in params:
            path_params['namespaceName'] = params['namespace_name']

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}
        if 'opc_client_request_id' in params:
            header_params['opc-client-request-id'] = params['opc_client_request_id']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_object_storage_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[Bucket]')
        return response

    def list_objects(self, namespace_name, bucket_name, **kwargs):
        """
        ListObjects
        List the objects in a bucket.\n

        :param str namespace_name: The top-level namespace used for the request. (required)
        :param str bucket_name: The name of the bucket. (required)
        :param str prefix: Object names returned by a list query must start with prefix
        :param str start: Object names returned by a list query must be greater or equal to this parameter
        :param str end: Object names returned by a list query must be strictly less than this parameter
        :param int limit: The maximum number of items to return.
        :param str delimiter: When this parameter is set to '/' character (other values not supported), only objects that do not have it in name, after an optionally specified prefix, are returned.   For all other scanned objects, part of their name up to the last occurence of the delimiter, after prefix, is returned as a set of prefixes.
        :param str fields: Object summary in list of objects includes the 'name' field.   This parameter may be used to also include 'size' (object size in bytes), 'md5', and 'timeCreated' (object creation date and time) fields. Value of this parameter should be a comma separated, case-insensitive list of those field names. For example 'name,timeCreated,md5'
        :param str opc_client_request_id: The client request ID for tracing
        :return: A Response object with data of type ListObjects
        """

        all_params = ['namespace_name', 'bucket_name', 'prefix', 'start', 'end', 'limit', 'delimiter', 'fields', 'opc_client_request_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_objects" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'namespace_name' is set
        if ('namespace_name' not in params) or (params['namespace_name'] is None):
            raise ValueError("Missing the required parameter `namespace_name` when calling `list_objects`")
        # verify the required parameter 'bucket_name' is set
        if ('bucket_name' not in params) or (params['bucket_name'] is None):
            raise ValueError("Missing the required parameter `bucket_name` when calling `list_objects`")

        resource_path = '/n/{namespaceName}/b/{bucketName}/o'
        path_params = {}
        if 'namespace_name' in params:
            path_params['namespaceName'] = params['namespace_name']
        if 'bucket_name' in params:
            path_params['bucketName'] = params['bucket_name']

        query_params = {}
        if 'prefix' in params:
            query_params['prefix'] = params['prefix']
        if 'start' in params:
            query_params['start'] = params['start']
        if 'end' in params:
            query_params['end'] = params['end']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'delimiter' in params:
            query_params['delimiter'] = params['delimiter']
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}
        if 'opc_client_request_id' in params:
            header_params['opc-client-request-id'] = params['opc_client_request_id']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_object_storage_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='ListObjects')
        return response

    def put_object(self, namespace_name, bucket_name, object_name, put_object_body, **kwargs):
        """
        PutObject
        Create a new object or overwrite an existing one.\n

        :param str namespace_name: The top-level namespace used for the request. (required)
        :param str bucket_name: The name of the bucket. (required)
        :param str object_name: The name of the object. (required)
        :param int content_length: The content type of the body.
        :param stream put_object_body: The object being put to the object store. (required)
        :param str if_match: The entity tag to match.
        :param str if_none_match: The entity tag to avoid matching.
        :param str opc_client_request_id: The client request ID for tracing
        :param str expect: 100-continue
        :param str content_md5: The base-64 encoded MD5 hash of the body.
        :param dict(str, str) opc_meta: Optional user-defined metadata key and value.
        :return: A Response object with data of type None
        """

        all_params = ['namespace_name', 'bucket_name', 'object_name', 'content_length', 'put_object_body', 'if_match', 'if_none_match', 'opc_client_request_id', 'expect', 'content_md5', 'opc_meta']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_object" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'namespace_name' is set
        if ('namespace_name' not in params) or (params['namespace_name'] is None):
            raise ValueError("Missing the required parameter `namespace_name` when calling `put_object`")
        # verify the required parameter 'bucket_name' is set
        if ('bucket_name' not in params) or (params['bucket_name'] is None):
            raise ValueError("Missing the required parameter `bucket_name` when calling `put_object`")
        # verify the required parameter 'object_name' is set
        if ('object_name' not in params) or (params['object_name'] is None):
            raise ValueError("Missing the required parameter `object_name` when calling `put_object`")
        # verify the required parameter 'put_object_body' is set
        if ('put_object_body' not in params) or (params['put_object_body'] is None):
            raise ValueError("Missing the required parameter `put_object_body` when calling `put_object`")

        resource_path = '/n/{namespaceName}/b/{bucketName}/o/{objectName}'
        path_params = {}
        if 'namespace_name' in params:
            path_params['namespaceName'] = params['namespace_name']
        if 'bucket_name' in params:
            path_params['bucketName'] = params['bucket_name']
        if 'object_name' in params:
            path_params['objectName'] = params['object_name']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']
        if 'if_none_match' in params:
            header_params['if-none-match'] = params['if_none_match']
        if 'opc_client_request_id' in params:
            header_params['opc-client-request-id'] = params['opc_client_request_id']
        if 'expect' in params:
            header_params['Expect'] = params['expect']
        if 'content_length' in params:
            header_params['Content-Length'] = params['content_length']
        if 'content_md5' in params:
            header_params['Content-MD5'] = params['content_md5']
        if 'opc_meta' in params:
            for key, value in params['opc_meta'].items():
                header_params['opc-meta-' + key] = value

        body_params = None
        if 'put_object_body' in params:
            body_params = params['put_object_body']

        header_params['accept'] = 'application/json'
        if not (isinstance(body_params, str) or isinstance(body_params, IOBase)):
            raise TypeError('The body must be a string or io.IOBase.')
        response = self.api_client.call_api(self.api_client.config.endpoint_object_storage_api,
                                            resource_path,
                                            'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            enforce_content_headers=False,
                                            response_type=None)
        return response

    def update_bucket(self, namespace_name, bucket_name, update_bucket_details, **kwargs):
        """
        UpdateBucket
        Perform a partial (or full) update of a bucket, currently including just the user-defined metadata.\n

        :param str namespace_name: The top-level namespace used for the request. (required)
        :param str bucket_name: The name of the bucket. (required)
        :param UpdateBucketDetails update_bucket_details: Request object for updating a bucket. (required)
        :param str if_match: The entity tag to match.
        :param str opc_client_request_id: The client request ID for tracing
        :return: A Response object with data of type Bucket
        """

        all_params = ['namespace_name', 'bucket_name', 'update_bucket_details', 'if_match', 'opc_client_request_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_bucket" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'namespace_name' is set
        if ('namespace_name' not in params) or (params['namespace_name'] is None):
            raise ValueError("Missing the required parameter `namespace_name` when calling `update_bucket`")
        # verify the required parameter 'bucket_name' is set
        if ('bucket_name' not in params) or (params['bucket_name'] is None):
            raise ValueError("Missing the required parameter `bucket_name` when calling `update_bucket`")
        # verify the required parameter 'update_bucket_details' is set
        if ('update_bucket_details' not in params) or (params['update_bucket_details'] is None):
            raise ValueError("Missing the required parameter `update_bucket_details` when calling `update_bucket`")

        resource_path = '/n/{namespaceName}/b/{bucketName}/'
        path_params = {}
        if 'namespace_name' in params:
            path_params['namespaceName'] = params['namespace_name']
        if 'bucket_name' in params:
            path_params['bucketName'] = params['bucket_name']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']
        if 'opc_client_request_id' in params:
            header_params['opc-client-request-id'] = params['opc_client_request_id']

        body_params = None
        if 'update_bucket_details' in params:
            body_params = params['update_bucket_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_object_storage_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Bucket')
        return response
