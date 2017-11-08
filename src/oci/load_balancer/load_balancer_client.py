# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

import six

from ..base_client import BaseClient
from ..config import get_config_value_or_default, validate_config
from ..signer import Signer
from ..util import Sentinel
from .models import load_balancer_type_mapping
missing = Sentinel("Missing")


class LoadBalancerClient(object):

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
        self.base_client = BaseClient("load_balancer", config, signer, load_balancer_type_mapping)

    def create_backend(self, create_backend_details, load_balancer_id, backend_set_name, **kwargs):
        """
        CreateBackend
        Adds a backend server to a backend set.


        :param CreateBackendDetails create_backend_details: (required)
            The details to add a backend server to a backend set.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend set and servers.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set to add the backend server to.

            Example: `My_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets/{backendSetName}/backends"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_backend got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=create_backend_details)

    def create_backend_set(self, create_backend_set_details, load_balancer_id, **kwargs):
        """
        CreateBackendSet
        Adds a backend set to a load balancer.


        :param CreateBackendSetDetails create_backend_set_details: (required)
            The details for adding a backend set.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer on which to add a backend set.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_backend_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=create_backend_set_details)

    def create_certificate(self, create_certificate_details, load_balancer_id, **kwargs):
        """
        CreateCertificate
        Creates an asynchronous request to add an SSL certificate.


        :param CreateCertificateDetails create_certificate_details: (required)
            The details of the certificate to add.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer on which to add the certificate.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/certificates"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_certificate got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=create_certificate_details)

    def create_listener(self, create_listener_details, load_balancer_id, **kwargs):
        """
        CreateListener
        Adds a listener to a load balancer.


        :param CreateListenerDetails create_listener_details: (required)
            Details to add a listener.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer on which to add a listener.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/listeners"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_listener got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=create_listener_details)

    def create_load_balancer(self, create_load_balancer_details, **kwargs):
        """
        CreateLoadBalancer
        Creates a new load balancer in the specified compartment. For general information about load balancers,
        see `Overview of the Load Balancing Service`__.

        For the purposes of access control, you must provide the OCID of the compartment where you want
        the load balancer to reside. Notice that the load balancer doesn't have to be in the same compartment as the VCN
        or backend set. If you're not sure which compartment to use, put the load balancer in the same compartment as the VCN.
        For information about access control and compartments, see
        `Overview of the IAM Service`__.

        You must specify a display name for the load balancer. It does not have to be unique, and you can change it.

        For information about Availability Domains, see
        `Regions and Availability Domains`__.
        To get a list of Availability Domains, use the `ListAvailabilityDomains` operation
        in the Identity and Access Management Service API.

        All Oracle Cloud Infrastructure resources, including load balancers, get an Oracle-assigned,
        unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID
        in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type,
        or by viewing the resource in the Console. Fore more information, see
        `Resource Identifiers`__.

        After you send your request, the new object's state will temporarily be PROVISIONING. Before using the
        object, first make sure its state has changed to RUNNING.

        When you create a load balancer, the system assigns an IP address.
        To get the IP address, use the :func:`get_load_balancer` operation.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Balance/Concepts/balanceoverview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param CreateLoadBalancerDetails create_load_balancer_details: (required)
            The configuration details for creating a load balancer.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_load_balancer got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_load_balancer_details)

    def delete_backend(self, load_balancer_id, backend_set_name, backend_name, **kwargs):
        """
        DeleteBackend
        Removes a backend server from a given load balancer and backend set.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend set and server.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the backend server.

            Example: `My_backend_set`

        :param str backend_name: (required)
            The IP address and port of the backend server to remove.

            Example: `1.1.1.7:42`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets/{backendSetName}/backends/{backendName}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_backend got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "backendSetName": backend_set_name,
            "backendName": backend_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_backend_set(self, load_balancer_id, backend_set_name, **kwargs):
        """
        DeleteBackendSet
        Deletes the specified backend set. Note that deleting a backend set removes its backend servers from the load balancer.

        Before you can delete a backend set, you must remove it from any active listeners.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend set.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set to delete.

            Example: `My_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets/{backendSetName}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_backend_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_certificate(self, load_balancer_id, certificate_name, **kwargs):
        """
        DeleteCertificate
        Deletes an SSL certificate from a load balancer.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the certificate to be deleted.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str certificate_name: (required)
            The name of the certificate to delete.

            Example: `My_certificate_bundle`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/certificates/{certificateName}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_certificate got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "certificateName": certificate_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_listener(self, load_balancer_id, listener_name, **kwargs):
        """
        DeleteListener
        Deletes a listener from a load balancer.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the listener to delete.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str listener_name: (required)
            The name of the listener to delete.

            Example: `My listener`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/listeners/{listenerName}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_listener got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "listenerName": listener_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_load_balancer(self, load_balancer_id, **kwargs):
        """
        DeleteLoadBalancer
        Stops a load balancer and removes it from service.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer to delete.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_load_balancer got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def get_backend(self, load_balancer_id, backend_set_name, backend_name, **kwargs):
        """
        GetBackend
        Gets the specified backend server's configuration information.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend set and server.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set that includes the backend server.

            Example: `My_backend_set`

        :param str backend_name: (required)
            The IP address and port of the backend server to retrieve.

            Example: `1.1.1.7:42`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.load_balancer.models.Backend`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets/{backendSetName}/backends/{backendName}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_backend got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "backendSetName": backend_set_name,
            "backendName": backend_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Backend")

    def get_backend_health(self, load_balancer_id, backend_set_name, backend_name, **kwargs):
        """
        BackendHealth
        Gets the current health status of the specified backend server.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend server health status to be retrieved.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the backend server to retrieve the health status for.

            Example: `My_backend_set`

        :param str backend_name: (required)
            The IP address and port of the backend server to retrieve the health status for.

            Example: `1.1.1.7:42`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.load_balancer.models.BackendHealth`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets/{backendSetName}/backends/{backendName}/health"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_backend_health got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "backendSetName": backend_set_name,
            "backendName": backend_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="BackendHealth")

    def get_backend_set(self, load_balancer_id, backend_set_name, **kwargs):
        """
        GetBackendSet
        Gets the specified backend set's configuration information.


        :param str load_balancer_id: (required)
            The `OCID`__ of the specified load balancer.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set to retrieve.

            Example: `My_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.load_balancer.models.BackendSet`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets/{backendSetName}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_backend_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="BackendSet")

    def get_backend_set_health(self, load_balancer_id, backend_set_name, **kwargs):
        """
        BackendSetHealth
        Gets the health status for the specified backend set.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend set health status to be retrieved.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set to retrieve the health status for.

            Example: `My_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.load_balancer.models.BackendSetHealth`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets/{backendSetName}/health"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_backend_set_health got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="BackendSetHealth")

    def get_health_checker(self, load_balancer_id, backend_set_name, **kwargs):
        """
        GetHealthChecker
        Gets the health check policy information for a given load balancer and backend set.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the health check policy to be retrieved.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the health check policy to be retrieved.

            Example: `My_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.load_balancer.models.HealthChecker`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets/{backendSetName}/healthChecker"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_health_checker got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="HealthChecker")

    def get_load_balancer(self, load_balancer_id, **kwargs):
        """
        GetLoadBalancer
        Gets the specified load balancer's configuration information.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer to retrieve.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.load_balancer.models.LoadBalancer`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_load_balancer got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="LoadBalancer")

    def get_load_balancer_health(self, load_balancer_id, **kwargs):
        """
        LoadBalancerHealth
        Gets the health status for the specified load balancer.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer to return health status for.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.load_balancer.models.LoadBalancerHealth`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/health"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_load_balancer_health got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="LoadBalancerHealth")

    def get_work_request(self, work_request_id, **kwargs):
        """
        GetWorkRequest
        Gets the details of a work request.


        :param str work_request_id: (required)
            The `OCID`__ of the work request to retrieve.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.load_balancer.models.WorkRequest`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancerWorkRequests/{workRequestId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_work_request got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workRequestId": work_request_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="WorkRequest")

    def list_backend_sets(self, load_balancer_id, **kwargs):
        """
        ListBackendSets
        Lists all backend sets associated with a given load balancer.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend sets to retrieve.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.load_balancer.models.BackendSet`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_backend_sets got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="list[BackendSet]")

    def list_backends(self, load_balancer_id, backend_set_name, **kwargs):
        """
        ListBackends
        Lists the backend servers for a given load balancer and backend set.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend set and servers.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the backend servers.

            Example: `My_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.load_balancer.models.Backend`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets/{backendSetName}/backends"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_backends got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="list[Backend]")

    def list_certificates(self, load_balancer_id, **kwargs):
        """
        ListCertificates
        Lists all SSL certificates associated with a given load balancer.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the certificates to be listed.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.load_balancer.models.Certificate`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/certificates"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_certificates got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="list[Certificate]")

    def list_load_balancer_healths(self, compartment_id, **kwargs):
        """
        ListLoadBalancerHealths
        Lists the summary health statuses for all load balancers in the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the load balancers to return health status information for.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

            Example: `3`

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.load_balancer.models.LoadBalancerHealthSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancerHealths"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_load_balancer_healths got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "compartmentId": compartment_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[LoadBalancerHealthSummary]")

    def list_load_balancers(self, compartment_id, **kwargs):
        """
        ListLoadBalancers
        Lists all load balancers in the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the load balancers to list.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

            Example: `3`

        :param str detail: (optional)
            The level of detail to return for each result. Can be `full` or `simple`.

            Example: `full`

        :param str sort_by: (optional)
            The field to sort by.  Only one sort order may be provided.  Time created is default ordered as descending.  Display name is default ordered as ascending.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either 'asc' or 'desc'

            Allowed values are: "ASC", "DESC"

        :param str display_name: (optional)
            A filter to only return resources that match the given display name exactly.

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state.

            Allowed values are: "CREATING", "FAILED", "ACTIVE", "DELETING", "DELETED"

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.load_balancer.models.LoadBalancer`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "limit",
            "page",
            "detail",
            "sort_by",
            "sort_order",
            "display_name",
            "lifecycle_state"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_load_balancers got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "FAILED", "ACTIVE", "DELETING", "DELETED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "compartmentId": compartment_id,
            "detail": kwargs.get("detail", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "displayName": kwargs.get("display_name", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[LoadBalancer]")

    def list_policies(self, compartment_id, **kwargs):
        """
        ListPolicies
        Lists the available load balancer policies.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the load balancer policies to list.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

            Example: `3`

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.load_balancer.models.LoadBalancerPolicy`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancerPolicies"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_policies got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[LoadBalancerPolicy]")

    def list_protocols(self, compartment_id, **kwargs):
        """
        ListProtocols
        Lists all supported traffic protocols.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the load balancer protocols to list.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

            Example: `3`

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.load_balancer.models.LoadBalancerProtocol`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancerProtocols"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_protocols got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[LoadBalancerProtocol]")

    def list_shapes(self, compartment_id, **kwargs):
        """
        ListShapes
        Lists the valid load balancer shapes.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the load balancer shapes to list.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

            Example: `3`

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.load_balancer.models.LoadBalancerShape`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancerShapes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_shapes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[LoadBalancerShape]")

    def list_work_requests(self, load_balancer_id, **kwargs):
        """
        ListWorkRequests
        Lists the work requests for a given load balancer.


        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the work requests to retrieve.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

            Example: `3`

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.load_balancer.models.WorkRequest`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/workRequests"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_work_requests got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id
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
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            response_type="list[WorkRequest]")

    def update_backend(self, update_backend_details, load_balancer_id, backend_set_name, backend_name, **kwargs):
        """
        UpdateBackend
        Updates the configuration of a backend server within the specified backend set.


        :param UpdateBackendDetails update_backend_details: (required)
            Details for updating a backend server.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend set and server.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the backend server.

            Example: `My_backend_set`

        :param str backend_name: (required)
            The IP address and port of the backend server to update.

            Example: `1.1.1.7:42`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets/{backendSetName}/backends/{backendName}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_backend got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "backendSetName": backend_set_name,
            "backendName": backend_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_backend_details)

    def update_backend_set(self, update_backend_set_details, load_balancer_id, backend_set_name, **kwargs):
        """
        UpdateBackendSet
        Updates a backend set.


        :param UpdateBackendSetDetails update_backend_set_details: (required)
            The details to update a backend set.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the backend set.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set to update.

            Example: `My_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets/{backendSetName}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_backend_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_backend_set_details)

    def update_health_checker(self, health_checker, load_balancer_id, backend_set_name, **kwargs):
        """
        UpdateHealthChecker
        Updates the health check policy for a given load balancer and backend set.


        :param UpdateHealthCheckerDetails health_checker: (required)
            The health check policy configuration details.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the health check policy to be updated.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the health check policy to be retrieved.

            Example: `My_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/backendSets/{backendSetName}/healthChecker"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_health_checker got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=health_checker)

    def update_listener(self, update_listener_details, load_balancer_id, listener_name, **kwargs):
        """
        UpdateListener
        Updates a listener for a given load balancer.


        :param UpdateListenerDetails update_listener_details: (required)
            Details to update a listener.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer associated with the listener to update.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str listener_name: (required)
            The name of the listener to update.

            Example: `My listener`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}/listeners/{listenerName}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_listener got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id,
            "listenerName": listener_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_listener_details)

    def update_load_balancer(self, update_load_balancer_details, load_balancer_id, **kwargs):
        """
        UpdateLoadBalancer
        Updates a load balancer's configuration.


        :param UpdateLoadBalancerDetails update_load_balancer_details: (required)
            The details for updating a load balancer's configuration.

        :param str load_balancer_id: (required)
            The `OCID`__ of the load balancer to update.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/loadBalancers/{loadBalancerId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_load_balancer got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "loadBalancerId": load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_load_balancer_details)
