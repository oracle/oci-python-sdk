# coding: utf-8
# Copyright (c) 2016 Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

import six

from ..base_client import BaseClient
from ..config import validate_config
from ..signer import Signer
from ..util import Sentinel
missing = Sentinel("Missing")


class ObjectStorageClient(object):

    def __init__(self, config):
        validate_config(config)
        signer = Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config["key_file"],
            pass_phrase=config["pass_phrase"]
        )
        self.base_client = BaseClient("object_storage", config, signer)

    def create_bucket(self, namespace_name, create_bucket_details, **kwargs):
        """
        CreateBucket
        Creates a bucket in the given namespace with a bucket name and optional user-defined metadata.
        To use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,
        talk to an administrator. If you're an admin who needs to write policies to give users access, see
        [Getting Started with Policies]({{DOC_SERVER_URL}}/Content/Identity/Concepts/policygetstarted.htm).

        :param str namespace_name: (required)
            The top-level namespace used for the request.
                :param CreateBucketDetails create_bucket_details: (required)
            Request object for creating a bucket.
        :param str opc_client_request_id: (optional)
            The client request ID for tracing
        :return: A Response object with data of type Bucket
        """
        resource_path = "/n/{namespaceName}/b/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=create_bucket_details,
            response_type="Bucket")

    def delete_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        DeleteBucket
        Deletes a bucket if it is already empty. If the bucket is not empty, use DeleteObject first.

        :param str namespace_name: (required)
            The top-level namespace used for the request.
                :param str bucket_name: (required)
            The name of the bucket.
            Example: `my-new-bucket1`
        :param str if_match: (optional)
            The entity tag to match.
        :param str opc_client_request_id: (optional)
            The client request ID for tracing
        :return: A Response object with data of type None
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_object(self, namespace_name, bucket_name, object_name, **kwargs):
        """
        DeleteObject
        Delete an object.

        :param str namespace_name: (required)
            The top-level namespace used for the request.
                :param str bucket_name: (required)
            The name of the bucket.
            Example: `my-new-bucket1`
                :param str object_name: (required)
            The name of the object.
            Example: `test/test1`
        :param str if_match: (optional)
            The entity tag to match.
        :param str opc_client_request_id: (optional)
            The client request ID for tracing
        :return: A Response object with data of type None
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def get_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        GetBucket
        Gets the current representation of the given bucket in the given namespace.

        :param str namespace_name: (required)
            The top-level namespace used for the request.
                :param str bucket_name: (required)
            The name of the bucket.
            Example: `my-new-bucket1`
        :param str if_match: (optional)
            The entity tag to match.
        :param str if_none_match: (optional)
            The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists.
        :param str opc_client_request_id: (optional)
            The client request ID for tracing
        :return: A Response object with data of type Bucket
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match",
            "if_none_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Bucket")

    def get_namespace(self, **kwargs):
        """
        GetNamespace
        Get the name of the namespace for the user making the request. An account name must be unique, must start with a
        letter, and can have up to 15 lower case letters and numbers. You cannot use spaces and special characters.

:param str opc_client_request_id: (optional)
            The client request ID for tracing
        :return: A Response object with data of type str
        """
        resource_path = "/n/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_namespace got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            response_type="str")

    def get_object(self, namespace_name, bucket_name, object_name, **kwargs):
        """
        GetObject
        Gets the metadata and body of an object.

        :param str namespace_name: (required)
            The top-level namespace used for the request.
                :param str bucket_name: (required)
            The name of the bucket.
            Example: `my-new-bucket1`
                :param str object_name: (required)
            The name of the object.
            Example: `test/test1`
        :param str if_match: (optional)
            The entity tag to match.
        :param str if_none_match: (optional)
            The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists.
        :param str opc_client_request_id: (optional)
            The client request ID for tracing
        :param str range: (optional)
            Optional byte range to fetch. Follows https://tools.ietf.org/html/rfc7233#section-2.1.
            Note, only one byte range is supported.
        :return: A Response object with data of type stream
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match",
            "if_none_match",
            "opc_client_request_id",
            "range"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing),
            "range": kwargs.get("range", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="stream")

    def head_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        HeadBucket
        An efficient method to check if a bucket exists, and to get the current ETag for the bucket.

        :param str namespace_name: (required)
            The top-level namespace used for the request.
                :param str bucket_name: (required)
            The name of the bucket.
            Example: `my-new-bucket1`
        :param str if_match: (optional)
            The entity tag to match.
        :param str if_none_match: (optional)
            The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists.
        :param str opc_client_request_id: (optional)
            The client request ID for tracing
        :return: A Response object with data of type None
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/"
        method = "HEAD"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match",
            "if_none_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "head_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def head_object(self, namespace_name, bucket_name, object_name, **kwargs):
        """
        HeadObject
        Gets the user-defined metadata and entity tag for an object.

        :param str namespace_name: (required)
            The top-level namespace used for the request.
                :param str bucket_name: (required)
            The name of the bucket.
            Example: `my-new-bucket1`
                :param str object_name: (required)
            The name of the object.
            Example: `test/test1`
        :param str if_match: (optional)
            The entity tag to match.
        :param str if_none_match: (optional)
            The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists.
        :param str opc_client_request_id: (optional)
            The client request ID for tracing
        :return: A Response object with data of type None
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "HEAD"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match",
            "if_none_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "head_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def list_buckets(self, namespace_name, compartment_id, **kwargs):
        """
        ListBuckets
        Get a list of all `BucketSummary`s in a namespace. A `BucketSummary` contains only summary fields for the bucket
        and does not contain fields like the user-defined metadata.
        To use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,
        talk to an administrator. If you're an admin who needs to write policies to give users access, see
        [Getting Started with Policies]({{DOC_SERVER_URL}}/Content/Identity/Concepts/policygetstarted.htm).

        :param str namespace_name: (required)
            The top-level namespace used for the request.
                :param str compartment_id: (required)
            The compartment ID in which to create the bucket.
        :param int limit: (optional)
            The maximum number of items to return.
        :param str page: (optional)
            The page at which to start retrieving results.
        :param str opc_client_request_id: (optional)
            The client request ID for tracing
        :return: A Response object with data of type list[BucketSummary]
        """
        resource_path = "/n/{namespaceName}/b/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_buckets got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            response_type="list[BucketSummary]")

    def list_objects(self, namespace_name, bucket_name, **kwargs):
        """
        ListObjects
        Lists the objects in a bucket.
        To use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,
        talk to an administrator. If you're an admin who needs to write policies to give users access, see
        [Getting Started with Policies]({{DOC_SERVER_URL}}/Content/Identity/Concepts/policygetstarted.htm).

        :param str namespace_name: (required)
            The top-level namespace used for the request.
                :param str bucket_name: (required)
            The name of the bucket.
            Example: `my-new-bucket1`
        :param str prefix: (optional)
            Object names returned by a list query must start with prefix
        :param str start: (optional)
            Object names returned by a list query must be greater or equal to this parameter
        :param str end: (optional)
            Object names returned by a list query must be strictly less than this parameter
        :param int limit: (optional)
            The maximum number of items to return.
        :param str delimiter: (optional)
            When this parameter is set, only objects whose names do not contain the delimiter character
            (after an optionally specified prefix) are returned. Scanned objects whose names contain the
            delimiter have part of their name up to the last occurrence of the delimiter (after the optional
            prefix) returned as a set of prefixes. Note that only '/' is a supported delimiter character at
            this time.
        :param str fields: (optional)
            Object summary in list of objects includes the 'name' field.   This parameter may also include 'size'
            (object size in bytes), 'md5', and 'timeCreated' (object creation date and time) fields.
            Value of this parameter should be a comma separated, case-insensitive list of those field names.
            For example 'name,timeCreated,md5'
        :param str opc_client_request_id: (optional)
            The client request ID for tracing
        :return: A Response object with data of type ListObjects
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "prefix",
            "start",
            "end",
            "limit",
            "delimiter",
            "fields",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_objects got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        query_params = {
            "prefix": kwargs.get("prefix", missing),
            "start": kwargs.get("start", missing),
            "end": kwargs.get("end", missing),
            "limit": kwargs.get("limit", missing),
            "delimiter": kwargs.get("delimiter", missing),
            "fields": kwargs.get("fields", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            response_type="ListObjects")

    def put_object(self, namespace_name, bucket_name, object_name, put_object_body, **kwargs):
        """
        PutObject
        Create a new object or overwrite an existing one.
        To use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,
        talk to an administrator. If you're an admin who needs to write policies to give users access, see
        [Getting Started with Policies]({{DOC_SERVER_URL}}/Content/Identity/Concepts/policygetstarted.htm).

        :param str namespace_name: (required)
            The top-level namespace used for the request.
                :param str bucket_name: (required)
            The name of the bucket.
            Example: `my-new-bucket1`
                :param str object_name: (required)
            The name of the object.
            Example: `test/test1`
                :param stream put_object_body: (required)
            The object being put to the object store.
        :param int content_length: (optional)
            The content length of the body.
        :param str if_match: (optional)
            The entity tag to match.
        :param str if_none_match: (optional)
            The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists.
        :param str opc_client_request_id: (optional)
            The client request ID for tracing
        :param str expect: (optional)
            100-continue
        :param str content_md5: (optional)
            The base-64 encoded MD5 hash of the body.
        :param str content_type: (optional)
            The content type of the object.  Defaults to 'application/octet-stream' if not overridden during the PutObject call.
        :param str content_language: (optional)
            The content language of the object.
        :param str content_encoding: (optional)
            The content encoding of the object.
        :param dict(str, str) opc_meta: (optional)
            Optional user-defined metadata key and value.
        :return: A Response object with data of type None
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "content_length",
            "if_match",
            "if_none_match",
            "opc_client_request_id",
            "expect",
            "content_md5",
            "content_type",
            "content_language",
            "content_encoding",
            "opc_meta"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "put_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing),
            "Expect": kwargs.get("expect", missing),
            "Content-Length": kwargs.get("content_length", missing),
            "Content-MD5": kwargs.get("content_md5", missing),
            "Content-Type": kwargs.get("content_type", missing),
            "Content-Language": kwargs.get("content_language", missing),
            "Content-Encoding": kwargs.get("content_encoding", missing),

        }
        for key, value in six.iteritems(kwargs.get("opc_meta", {})):
            header_params["opc-meta-" + key] = value
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        if (not isinstance(put_object_body, (six.binary_type, six.string_types)) and
                not hasattr(put_object_body, "read")):
            raise TypeError('The body must be a string, bytes, or provide a read() method.')

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=put_object_body,
            enforce_content_headers=False)

    def update_bucket(self, namespace_name, bucket_name, update_bucket_details, **kwargs):
        """
        UpdateBucket
        Performs a partial (or full) update of a bucket, currently including just the user-defined metadata.

        :param str namespace_name: (required)
            The top-level namespace used for the request.
                :param str bucket_name: (required)
            The name of the bucket.
            Example: `my-new-bucket1`
                :param UpdateBucketDetails update_bucket_details: (required)
            Request object for updating a bucket.
        :param str if_match: (optional)
            The entity tag to match.
        :param str opc_client_request_id: (optional)
            The client request ID for tracing
        :return: A Response object with data of type Bucket
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_bucket_details,
            response_type="Bucket")
