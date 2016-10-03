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

import six

from ..api_client import ApiClient
from ..signer import Signer
missing_param = object()


class ObjectStorageApi(object):

    def __init__(self, config):
        signer = Signer(config.tenancy, config.user, config.fingerprint, config.key_file)
        self.api_client = ApiClient(config, signer)

    def create_bucket(self, namespace_name, create_bucket_details, **kwargs):
        """
        CreateBucket
        Create a bucket in the given namespace with a bucket name and optional user-defined metadata.\n

        :param str namespace_name: The top-level namespace used for the request. (required)
        :param CreateBucketDetails create_bucket_details: Request object for creating a bucket. (required)
        :param str opc_client_request_id: The client request ID for tracing
        :return: A Response object with data of type Bucket
        """
        resource_path = "/n/{namespaceName}/b/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "namespace_name",
            "create_bucket_details",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_object_storage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=create_bucket_details,
            response_type="Bucket")

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
        resource_path = "/n/{namespaceName}/b/{bucketName}/"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "namespace_name",
            "bucket_name",
            "if_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_object_storage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

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
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "namespace_name",
            "bucket_name",
            "object_name",
            "if_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_object_storage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

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
        resource_path = "/n/{namespaceName}/b/{bucketName}/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "namespace_name",
            "bucket_name",
            "if_match",
            "if_none_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param),
            "if-none-match": kwargs.get("if_none_match", missing_param),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_object_storage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Bucket")

    def get_namespace(self, **kwargs):
        """
        GetNamespace
        Get the name of the namespace for the user making the request. An account name must be unique, must start with a\nletter, and can have up to 15 lower case letters and numbers. You cannot use spaces and special characters.\n

        :param str opc_client_request_id: The client request ID for tracing
        :return: A Response object with data of type str
        """
        resource_path = "/n/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_namespace got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_object_storage_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            response_type="str")

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
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "namespace_name",
            "bucket_name",
            "object_name",
            "if_match",
            "if_none_match",
            "opc_client_request_id",
            "range"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param),
            "if-none-match": kwargs.get("if_none_match", missing_param),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing_param),
            "range": kwargs.get("range", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_object_storage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="stream")

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
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "HEAD"

        # Don't accept unknown kwargs
        expected_params = [
            "namespace_name",
            "bucket_name",
            "object_name",
            "if_match",
            "if_none_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "head_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param),
            "if-none-match": kwargs.get("if_none_match", missing_param),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_object_storage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

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
        resource_path = "/n/{namespaceName}/b/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "namespace_name",
            "compartment_id",
            "limit",
            "page",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_buckets got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing_param),
            "page": kwargs.get("page", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_object_storage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Bucket]")

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
        resource_path = "/n/{namespaceName}/b/{bucketName}/o"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "namespace_name",
            "bucket_name",
            "prefix",
            "start",
            "end",
            "limit",
            "delimiter",
            "fields",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_objects got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        query_params = {
            "prefix": kwargs.get("prefix", missing_param),
            "start": kwargs.get("start", missing_param),
            "end": kwargs.get("end", missing_param),
            "limit": kwargs.get("limit", missing_param),
            "delimiter": kwargs.get("delimiter", missing_param),
            "fields": kwargs.get("fields", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_object_storage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            response_type="ListObjects")

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
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_params = [
            "namespace_name",
            "bucket_name",
            "object_name",
            "content_length",
            "put_object_body",
            "if_match",
            "if_none_match",
            "opc_client_request_id",
            "expect",
            "content_md5",
            "opc_meta"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "put_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "if-match": kwargs.get("if_match", missing_param),
            "if-none-match": kwargs.get("if_none_match", missing_param),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing_param),
            "Expect": kwargs.get("expect", missing_param),
            "Content-Length": kwargs.get("content_length", missing_param),
            "Content-MD5": kwargs.get("content_md5", missing_param),

        }
        for key, value in six.iteritems(kwargs.get("opc_meta", {})):
            header_params["opc-meta-" + key] = value
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        if (not isinstance(put_object_body, (six.binary_type, six.string_types)) and
                not hasattr(put_object_body, "read")):
            raise TypeError('The body must be a string, bytes, or provide a read() method.')

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_object_storage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=put_object_body,
            enforce_content_headers=False)

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
        resource_path = "/n/{namespaceName}/b/{bucketName}/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "namespace_name",
            "bucket_name",
            "update_bucket_details",
            "if_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "update_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_object_storage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_bucket_details,
            response_type="Bucket")
