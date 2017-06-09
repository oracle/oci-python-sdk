# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

import six

from ..base_client import BaseClient
from ..config import get_config_value_or_default, validate_config
from ..signer import Signer
from ..util import Sentinel
from .models import core_type_mapping
missing = Sentinel("Missing")


class ComputeClient(object):

    def __init__(self, config):
        validate_config(config)
        signer = Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config["key_file"],
            pass_phrase=get_config_value_or_default(config, "pass_phrase")
        )
        self.base_client = BaseClient("compute", config, signer, core_type_mapping)

    def attach_volume(self, attach_volume_details, **kwargs):
        """
        AttachVolume
        Attaches the specified storage volume to the specified instance.


        :param AttachVolumeDetails attach_volume_details: (required)
            Attach volume request

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type VolumeAttachment
        :rtype: VolumeAttachment
        """
        resource_path = "/volumeAttachments/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "attach_volume got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=attach_volume_details,
            response_type="VolumeAttachment")

    def capture_console_history(self, capture_console_history_details, **kwargs):
        """
        CaptureConsoleHistory
        Captures the most recent serial console data (up to a megabyte) for the
        specified instance.

        The `CaptureConsoleHistory` operation works with the other console history operations
        as described below.

        1. Use `CaptureConsoleHistory` to request the capture of up to a megabyte of the
        most recent console history. This call returns a `ConsoleHistory`
        object. The object will have a state of REQUESTED.
        2. Wait for the capture operation to succeed by polling `GetConsoleHistory` with
        the identifier of the console history metadata. The state of the
        `ConsoleHistory` object will go from REQUESTED to GETTING-HISTORY and
        then SUCCEEDED (or FAILED).
        3. Use `GetConsoleHistoryContent` to get the actual console history data (not the
        metadata).
        4. Optionally, use `DeleteConsoleHistory` to delete the console history metadata
        and the console history data.


        :param CaptureConsoleHistoryDetails capture_console_history_details: (required)
            Console history details

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type ConsoleHistory
        :rtype: ConsoleHistory
        """
        resource_path = "/instanceConsoleHistories/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "capture_console_history got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=capture_console_history_details,
            response_type="ConsoleHistory")

    def create_image(self, create_image_details, **kwargs):
        """
        CreateImage
        Creates a boot disk image for the specified instance. For more information about images, see
        `Managing Custom Images`__.

        You must provide the OCID of the instance you want to use as the basis for the image, and
        the OCID of the compartment containing that instance.

        You may optionally specify a *display name* for the image, which is simply a friendly name or description.
        It does not have to be unique, and you can change it. See :func:`update_image`.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/managingcustomimages.htm


        :param CreateImageDetails create_image_details: (required)
            Image creation details

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type Image
        :rtype: Image
        """
        resource_path = "/images/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_image got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_image_details,
            response_type="Image")

    def delete_console_history(self, instance_console_history_id, **kwargs):
        """
        DeleteConsoleHistory
        Deletes the specified console history metadata and the console history data.


        :param str instance_console_history_id: (required)
            The OCID of the console history.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/instanceConsoleHistories/{instanceConsoleHistoryId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_console_history got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "instanceConsoleHistoryId": instance_console_history_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_image(self, image_id, **kwargs):
        """
        DeleteImage
        Deletes an image.


        :param str image_id: (required)
            The OCID of the image.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/images/{imageId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_image got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "imageId": image_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def detach_volume(self, volume_attachment_id, **kwargs):
        """
        DetachVolume
        Detaches a storage volume from an instance. You must specify the OCID of the volume attachment.

        This is an asynchronous operation; the attachment's `lifecycleState` will change to DETACHING temporarily
        until the attachment is completely removed.


        :param str volume_attachment_id: (required)
            The OCID of the volume attachment.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/volumeAttachments/{volumeAttachmentId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "detach_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeAttachmentId": volume_attachment_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def get_console_history(self, instance_console_history_id, **kwargs):
        """
        GetConsoleHistory
        Shows the metadata for the specified console history.
        See :func:`capture_console_history`
        for details about using the console history operations.


        :param str instance_console_history_id: (required)
            The OCID of the console history.

        :return: A Response object with data of type ConsoleHistory
        :rtype: ConsoleHistory
        """
        resource_path = "/instanceConsoleHistories/{instanceConsoleHistoryId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_console_history got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "instanceConsoleHistoryId": instance_console_history_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="ConsoleHistory")

    def get_console_history_content(self, instance_console_history_id, **kwargs):
        """
        GetConsoleHistoryContent
        Gets the actual console history data (not the metadata).
        See :func:`capture_console_history`
        for details about using the console history operations.


        :param str instance_console_history_id: (required)
            The OCID of the console history.

        :param int offset: (optional)
            Offset of the snapshot data to retrieve.

        :param int length: (optional)
            Length of the snapshot data to retrieve.

        :return: A Response object with data of type bytes
        :rtype: bytes
        """
        resource_path = "/instanceConsoleHistories/{instanceConsoleHistoryId}/data"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "offset",
            "length"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_console_history_content got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "instanceConsoleHistoryId": instance_console_history_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        query_params = {
            "offset": kwargs.get("offset", missing),
            "length": kwargs.get("length", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            response_type="bytes")

    def get_image(self, image_id, **kwargs):
        """
        GetImage
        Gets the specified image.


        :param str image_id: (required)
            The OCID of the image.

        :return: A Response object with data of type Image
        :rtype: Image
        """
        resource_path = "/images/{imageId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_image got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "imageId": image_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Image")

    def get_instance(self, instance_id, **kwargs):
        """
        GetInstance
        Gets information about the specified instance.


        :param str instance_id: (required)
            The OCID of the instance.

        :return: A Response object with data of type Instance
        :rtype: Instance
        """
        resource_path = "/instances/{instanceId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_instance got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "instanceId": instance_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Instance")

    def get_volume_attachment(self, volume_attachment_id, **kwargs):
        """
        GetVolumeAttachment
        Gets information about the specified volume attachment.


        :param str volume_attachment_id: (required)
            The OCID of the volume attachment.

        :return: A Response object with data of type VolumeAttachment
        :rtype: VolumeAttachment
        """
        resource_path = "/volumeAttachments/{volumeAttachmentId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_volume_attachment got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "volumeAttachmentId": volume_attachment_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="VolumeAttachment")

    def get_windows_instance_initial_credentials(self, instance_id, **kwargs):
        """
        GetWindowsInstanceInitialCredentials
        Gets the generated credentials for the instance. Only works for Windows instances. The returned credentials
        are only valid for the initial login.


        :param str instance_id: (required)
            The OCID of the instance.

        :return: A Response object with data of type InstanceCredentials
        :rtype: InstanceCredentials
        """
        resource_path = "/instances/{instanceId}/initialCredentials"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_windows_instance_initial_credentials got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "instanceId": instance_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="InstanceCredentials")

    def instance_action(self, instance_id, action, **kwargs):
        """
        InstanceAction
        Performs one of the power actions (start, stop, softreset, or reset)
        on the specified instance.

        **start** - power on

        **stop** - power off

        **softreset** - ACPI shutdown and power on

        **reset** - power off and power on

        Note that the **stop** state has no effect on the resources you consume.
        Billing continues for instances that you stop, and related resources continue
        to apply against any relevant quotas. You must terminate an instance
        (:func:`terminate_instance`)
        to remove its resources from billing and quotas.


        :param str instance_id: (required)
            The OCID of the instance.

        :param str action: (required)
            The action to perform on the instance.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type Instance
        :rtype: Instance
        """
        resource_path = "/instances/{instanceId}"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "instance_action got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "instanceId": instance_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        query_params = {
            "action": action
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            response_type="Instance")

    def launch_instance(self, launch_instance_details, **kwargs):
        """
        LaunchInstance
        Creates a new instance in the specified compartment and the specified Availability Domain.
        For general information about instances, see
        `Overview of the Compute Service`__.

        For information about access control and compartments, see
        `Overview of the IAM Service`__.

        For information about Availability Domains, see
        `Regions and Availability Domains`__.
        To get a list of Availability Domains, use the `ListAvailabilityDomains` operation
        in the Identity and Access Management Service API.

        All Oracle Bare Metal Cloud Services resources, including instances, get an Oracle-assigned,
        unique ID called an Oracle Cloud Identifier (OCID).
        When you create a resource, you can find its OCID in the response. You can
        also retrieve a resource's OCID by using a List API operation
        on that resource type, or by viewing the resource in the Console.

        When you launch an instance, it is automatically attached to a Virtual
        Network Interface Card (VNIC). The VNIC has a private IP address from
        the subnet's CIDR, and optionally a public IP address.
        To get the addresses, use the :func:`list_vnic_attachments`
        operation to get the VNIC ID for the instance, and then call
        :func:`get_vnic` with the VNIC ID.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Concepts/computeoverview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm


        :param LaunchInstanceDetails launch_instance_details: (required)
            Instance details

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type Instance
        :rtype: Instance
        """
        resource_path = "/instances/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "launch_instance got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=launch_instance_details,
            response_type="Instance")

    def list_console_histories(self, compartment_id, **kwargs):
        """
        ListConsoleHistories
        Lists the console history metadata for the specified compartment or instance.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str availability_domain: (optional)
            The name of the Availability Domain.

            Example: `Uocm:PHX-AD-1`

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str instance_id: (optional)
            The OCID of the instance.

        :return: A Response object with data of type list[ConsoleHistory]
        :rtype: list[ConsoleHistory]
        """
        resource_path = "/instanceConsoleHistories/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "availability_domain",
            "limit",
            "page",
            "instance_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_console_histories got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "instanceId": kwargs.get("instance_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[ConsoleHistory]")

    def list_images(self, compartment_id, **kwargs):
        """
        ListImages
        Lists the available images in the specified compartment. For more
        information about images, see
        `Managing Custom Images`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/managingcustomimages.htm


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str display_name: (optional)
            A user-friendly name. Does not have to be unique, and it's changeable.

            Example: `My new resource`

        :param str operating_system: (optional)
            The image's operating system.

            Example: `Oracle Linux`

        :param str operating_system_version: (optional)
            The image's operating system version.

            Example: `7.2`

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[Image]
        :rtype: list[Image]
        """
        resource_path = "/images/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "display_name",
            "operating_system",
            "operating_system_version",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_images got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "displayName": kwargs.get("display_name", missing),
            "operatingSystem": kwargs.get("operating_system", missing),
            "operatingSystemVersion": kwargs.get("operating_system_version", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Image]")

    def list_instances(self, compartment_id, **kwargs):
        """
        ListInstances
        Lists the instances in the specified compartment and the specified Availability Domain.
        You can filter the results by specifying an instance name (the list will include all the identically-named
        instances in the compartment).


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str availability_domain: (optional)
            The name of the Availability Domain.

            Example: `Uocm:PHX-AD-1`

        :param str display_name: (optional)
            A user-friendly name. Does not have to be unique, and it's changeable.

            Example: `My new resource`

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[Instance]
        :rtype: list[Instance]
        """
        resource_path = "/instances/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "availability_domain",
            "display_name",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_instances got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": compartment_id,
            "displayName": kwargs.get("display_name", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Instance]")

    def list_shapes(self, compartment_id, **kwargs):
        """
        ListShapes
        Lists the shapes that can be used to launch an instance within the specified compartment. You can
        filter the list by compatibility with a specific image.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str availability_domain: (optional)
            The name of the Availability Domain.

            Example: `Uocm:PHX-AD-1`

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str image_id: (optional)
            The OCID of an image.

        :return: A Response object with data of type list[Shape]
        :rtype: list[Shape]
        """
        resource_path = "/shapes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "availability_domain",
            "limit",
            "page",
            "image_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_shapes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "imageId": kwargs.get("image_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Shape]")

    def list_vnic_attachments(self, compartment_id, **kwargs):
        """
        ListVnicAttachments
        Lists the VNIC attachments for the specified compartment. The list can be filtered by
        instance and by VNIC.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str availability_domain: (optional)
            The name of the Availability Domain.

            Example: `Uocm:PHX-AD-1`

        :param str instance_id: (optional)
            The OCID of the instance.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str vnic_id: (optional)
            The OCID of the VNIC.

        :return: A Response object with data of type list[VnicAttachment]
        :rtype: list[VnicAttachment]
        """
        resource_path = "/vnicAttachments/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "availability_domain",
            "instance_id",
            "limit",
            "page",
            "vnic_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_vnic_attachments got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": compartment_id,
            "instanceId": kwargs.get("instance_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "vnicId": kwargs.get("vnic_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[VnicAttachment]")

    def list_volume_attachments(self, compartment_id, **kwargs):
        """
        ListVolumeAttachments
        Lists the volume attachments in the specified compartment. You can filter the
        list by specifying an instance OCID, volume OCID, or both.

        Currently, the only supported volume attachment type is :class:`IScsiVolumeAttachment`.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str availability_domain: (optional)
            The name of the Availability Domain.

            Example: `Uocm:PHX-AD-1`

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str instance_id: (optional)
            The OCID of the instance.

        :param str volume_id: (optional)
            The OCID of the volume.

        :return: A Response object with data of type list[VolumeAttachment]
        :rtype: list[VolumeAttachment]
        """
        resource_path = "/volumeAttachments/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "availability_domain",
            "limit",
            "page",
            "instance_id",
            "volume_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_volume_attachments got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "instanceId": kwargs.get("instance_id", missing),
            "volumeId": kwargs.get("volume_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[VolumeAttachment]")

    def terminate_instance(self, instance_id, **kwargs):
        """
        TerminateInstance
        Terminates the specified instance. Any attached VNICs and volumes are automatically detached
        when the instance terminates.

        This is an asynchronous operation; the instance's `lifecycleState` will change to TERMINATING temporarily
        until the instance is completely removed.


        :param str instance_id: (required)
            The OCID of the instance.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/instances/{instanceId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "terminate_instance got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "instanceId": instance_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def update_image(self, image_id, update_image_details, **kwargs):
        """
        UpdateImage
        Updates the display name of the image.


        :param str image_id: (required)
            The OCID of the image.

        :param UpdateImageDetails update_image_details: (required)
            Updates the image display name field.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type Image
        :rtype: Image
        """
        resource_path = "/images/{imageId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_image got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "imageId": image_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_image_details,
            response_type="Image")

    def update_instance(self, instance_id, update_instance_details, **kwargs):
        """
        UpdateInstance
        Updates the display name of the specified instance. The OCID of the instance
        remains the same.


        :param str instance_id: (required)
            The OCID of the instance.

        :param UpdateInstanceDetails update_instance_details: (required)
            Update instance fields

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type Instance
        :rtype: Instance
        """
        resource_path = "/instances/{instanceId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_instance got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "instanceId": instance_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_instance_details,
            response_type="Instance")
