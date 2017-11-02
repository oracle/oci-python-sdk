# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

import six

from ..base_client import BaseClient
from ..config import get_config_value_or_default, validate_config
from ..signer import Signer
from ..util import Sentinel
from .models import object_storage_type_mapping
missing = Sentinel("Missing")


class ObjectStorageClient(object):

    def __init__(self, config):
        validate_config(config)
        signer = Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config.get("key_file"),
            pass_phrase=get_config_value_or_default(config, "pass_phrase"),
            private_key_content=config.get("key_content")
        )
        self.base_client = BaseClient("object_storage", config, signer, object_storage_type_mapping)

    def abort_multipart_upload(self, namespace_name, bucket_name, object_name, upload_id, **kwargs):
        """
        Abort Multipart Upload
        Aborts an in-progress multipart upload and deletes all parts that have been uploaded.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str upload_id: (required)
            The upload ID for a multipart upload.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u/{objectName}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "abort_multipart_upload got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "uploadId": upload_id
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
            header_params=header_params)

    def commit_multipart_upload(self, namespace_name, bucket_name, object_name, upload_id, commit_multipart_upload_details, **kwargs):
        """
        Commit Multipart Upload
        Commits a multipart upload, which involves checking part numbers and ETags of the parts, to create an aggregate object.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str upload_id: (required)
            The upload ID for a multipart upload.

        :param CommitMultipartUploadDetails commit_multipart_upload_details: (required)
            The part numbers and ETags for the parts you want to commit.

        :param str if_match: (optional)
            The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists.
            For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u/{objectName}"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match",
            "if_none_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "commit_multipart_upload got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "uploadId": upload_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

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
            query_params=query_params,
            header_params=header_params,
            body=commit_multipart_upload_details)

    def create_bucket(self, namespace_name, create_bucket_details, **kwargs):
        """
        Create Bucket
        Creates a bucket in the given namespace with a bucket name and optional user-defined metadata.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param CreateBucketDetails create_bucket_details: (required)
            Request object for creating a bucket.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.Bucket`
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

    def create_multipart_upload(self, namespace_name, bucket_name, create_multipart_upload_details, **kwargs):
        """
        Create Multipart Upload
        Starts a new multipart upload to a specific object in the given bucket in the given namespace.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param CreateMultipartUploadDetails create_multipart_upload_details: (required)
            Request object for creating a multi-part upload.

        :param str if_match: (optional)
            The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists.
            For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.MultipartUpload`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match",
            "if_none_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_multipart_upload got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
            body=create_multipart_upload_details,
            response_type="MultipartUpload")

    def create_preauthenticated_request(self, namespace_name, bucket_name, create_preauthenticated_request_details, **kwargs):
        """
        Create Preauthenticated Request
        Creates a pre-authenticated request specific to the bucket.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param CreatePreauthenticatedRequestDetails create_preauthenticated_request_details: (required)
            Information needed to create the pre-authenticated request.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.PreauthenticatedRequest`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/p/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_preauthenticated_request got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
            body=create_preauthenticated_request_details,
            response_type="PreauthenticatedRequest")

    def delete_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        DELETE Bucket
        Deletes a bucket if it is already empty. If the bucket is not empty, use :func:`delete_object` first.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str if_match: (optional)
            The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
        DELETE Object
        Deletes an object.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str if_match: (optional)
            The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

    def delete_preauthenticated_request(self, namespace_name, bucket_name, par_id, **kwargs):
        """
        DELETE Preauthenticated Request
        Deletes the pre-authenticated request for the bucket.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str par_id: (required)
            The unique identifier for the pre-authenticated request. This can be used to manage operations against
            the pre-authenticated request, such as GET or DELETE.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/p/{parId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_preauthenticated_request got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "parId": par_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
            header_params=header_params)

    def get_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        GET Bucket
        Gets the current representation of the given bucket in the given namespace.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str if_match: (optional)
            The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists.
            For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.Bucket`
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
        GET Namespace Name
        Gets the name of the namespace for the user making the request. An account name must be unique, must start with a
        letter, and can have up to 15 lowercase letters and numbers. You cannot use spaces or special characters.


        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type str
        :rtype: :class:`~oci.response.Response`
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

    def get_namespace_metadata(self, namespace_name, **kwargs):
        """
        GetNamespaceMetadata
        Get the metadata for the namespace, which contains defaultS3CompartmentId and defaultSwiftCompartmentId.
        Any user with the NAMESPACE_READ permission will be able to see the current metadata. If you're not authorized,
        talk to an administrator. If you're an administrator who needs to write
        policies to give users access, see `Getting Started with Policies`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.NamespaceMetadata`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_namespace_metadata got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
            response_type="NamespaceMetadata")

    def get_object(self, namespace_name, bucket_name, object_name, **kwargs):
        """
        GET Object
        Gets the metadata and body of an object.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str if_match: (optional)
            The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists.
            For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str range: (optional)
            Optional byte range to fetch, as described in `RFC 7233`__, section 2.1.
            Note that only a single range of bytes is supported.

            __ https://tools.ietf.org/rfc/rfc7233

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

    def get_preauthenticated_request(self, namespace_name, bucket_name, par_id, **kwargs):
        """
        GET Preauthenticated Request
        Gets the pre-authenticated request for the bucket.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str par_id: (required)
            The unique identifier for the pre-authenticated request. This can be used to manage operations against
            the pre-authenticated request, such as GET or DELETE.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.PreauthenticatedRequestSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/p/{parId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_preauthenticated_request got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "parId": par_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
            response_type="PreauthenticatedRequestSummary")

    def head_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        HEAD Bucket
        Efficiently checks to see if a bucket exists and gets the current ETag for the bucket.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str if_match: (optional)
            The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists.
            For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
        HEAD Object
        Gets the user-defined metadata and entity tag for an object.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str if_match: (optional)
            The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists.
            For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
        List Buckets
        Gets a list of all `BucketSummary`s in a compartment. A `BucketSummary` contains only summary fields for the bucket
        and does not contain fields like the user-defined metadata.

        To use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,
        talk to an administrator. If you're an administrator who needs to write policies to give users access, see
        `Getting Started with Policies`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str compartment_id: (required)
            The ID of the compartment in which to create the bucket.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.BucketSummary`
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

    def list_multipart_upload_parts(self, namespace_name, bucket_name, object_name, upload_id, **kwargs):
        """
        List Multipart Upload Parts
        Lists the parts of an in-progress multipart upload.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str upload_id: (required)
            The upload ID for a multipart upload.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.MultipartUploadPartSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u/{objectName}"
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
                "list_multipart_upload_parts got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "uploadId": upload_id,
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
            response_type="list[MultipartUploadPartSummary]")

    def list_multipart_uploads(self, namespace_name, bucket_name, **kwargs):
        """
        List Multipart Uploads
        Lists all in-progress multipart uploads for the given bucket in the given namespace.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.MultipartUpload`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u"
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
                "list_multipart_uploads got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
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
            response_type="list[MultipartUpload]")

    def list_objects(self, namespace_name, bucket_name, **kwargs):
        """
        List Objects
        Lists the objects in a bucket.

        To use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,
        talk to an administrator. If you're an administrator who needs to write policies to give users access, see
        `Getting Started with Policies`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str prefix: (optional)
            The string to use for matching against the start of object names in a list query.

        :param str start: (optional)
            Object names returned by a list query must be greater or equal to this parameter.

        :param str end: (optional)
            Object names returned by a list query must be strictly less than this parameter.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str delimiter: (optional)
            When this parameter is set, only objects whose names do not contain the delimiter character
            (after an optionally specified prefix) are returned. Scanned objects whose names contain the
            delimiter have part of their name up to the last occurrence of the delimiter (after the optional
            prefix) returned as a set of prefixes. Note that only '/' is a supported delimiter character at
            this time.

        :param str fields: (optional)
            Object summary in list of objects includes the 'name' field. This parameter can also include 'size'
            (object size in bytes), 'md5', and 'timeCreated' (object creation date and time) fields.
            Value of this parameter should be a comma-separated, case-insensitive list of those field names.
            For example 'name,timeCreated,md5'.

            Allowed values are: "name", "size", "timeCreated", "md5"

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.ListObjects`
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

    def list_preauthenticated_requests(self, namespace_name, bucket_name, **kwargs):
        """
        List Preauthenticated Requests
        Lists pre-authenticated requests for the bucket.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name_prefix: (optional)
            User-specified object name prefixes can be used to query and return a list of pre-authenticated requests.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.PreauthenticatedRequestSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/p/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "object_name_prefix",
            "limit",
            "page",
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_preauthenticated_requests got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "objectNamePrefix": kwargs.get("object_name_prefix", missing),
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
            response_type="list[PreauthenticatedRequestSummary]")

    def put_object(self, namespace_name, bucket_name, object_name, put_object_body, **kwargs):
        """
        PUT Object
        Creates a new object or overwrites an existing one.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param stream put_object_body: (required)
            The object to upload to the object store.

        :param int content_length: (optional)
            The content length of the body.

        :param str if_match: (optional)
            The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists.
            For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

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

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

    def rename_object(self, namespace_name, bucket_name, rename_object_details, **kwargs):
        """
        RenameObject
        Rename an object from source key to target key in the given namespace.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param RenameObjectDetails rename_object_details: (required)
            The sourceName and newName of rename operation.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/renameObject"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "rename_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
            body=rename_object_details)

    def restore_objects(self, namespace_name, bucket_name, restore_objects_details, **kwargs):
        """
        RestoreObjects
        Restore one or more objects specified by objectName parameter.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param RestoreObjectsDetails restore_objects_details: (required)
            Request to restore objects.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/restoreObjects"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "restore_objects got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
            body=restore_objects_details)

    def update_bucket(self, namespace_name, bucket_name, update_bucket_details, **kwargs):
        """
        POST Bucket
        Performs a partial or full update of a bucket's user-defined metadata.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param UpdateBucketDetails update_bucket_details: (required)
            Request object for updating a bucket.

        :param str if_match: (optional)
            The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.Bucket`
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

    def update_namespace_metadata(self, namespace_name, update_namespace_metadata_details, **kwargs):
        """
        UpdateNamespaceMetadata
        Change the default Swift/S3 compartmentId of user's namespace into the user-defined compartmentId. Upon doing
        this, all subsequent bucket creations will use the new default compartment, but no previously created
        buckets will be modified. A user must have the NAMESPACE_UPDATE permission to make changes to the default
        compartments for S3 and Swift.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param UpdateNamespaceMetadataDetails update_namespace_metadata_details: (required)
            Request object for update NamespaceMetadata.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.NamespaceMetadata`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_client_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_namespace_metadata got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
            body=update_namespace_metadata_details,
            response_type="NamespaceMetadata")

    def upload_part(self, namespace_name, bucket_name, object_name, upload_id, upload_part_num, upload_part_body, **kwargs):
        """
        Upload Multipart Object Part
        Uploads a single part of a multipart upload.


        :param str namespace_name: (required)
            The top-level namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str upload_id: (required)
            The upload ID for a multipart upload.

        :param int upload_part_num: (required)
            The part number that identifies the object part currently being uploaded.

        :param stream upload_part_body: (required)
            The part being uploaded to the Object Storage Service.

        :param int content_length: (optional)
            The content length of the body.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str if_match: (optional)
            The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists.
            For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.

        :param str expect: (optional)
            100-continue

        :param str content_md5: (optional)
            The base-64 encoded MD5 hash of the body.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u/{objectName}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "content_length",
            "opc_client_request_id",
            "if_match",
            "if_none_match",
            "expect",
            "content_md5"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "upload_part got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "uploadId": upload_id,
            "uploadPartNum": upload_part_num
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "Expect": kwargs.get("expect", missing),
            "Content-Length": kwargs.get("content_length", missing),
            "Content-MD5": kwargs.get("content_md5", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        if (not isinstance(upload_part_body, (six.binary_type, six.string_types)) and
                not hasattr(upload_part_body, "read")):
            raise TypeError('The body must be a string, bytes, or provide a read() method.')

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=upload_part_body,
            enforce_content_headers=False)
