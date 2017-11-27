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
            private_key_file_location=config.get("key_file"),
            pass_phrase=get_config_value_or_default(config, "pass_phrase"),
            private_key_content=config.get("key_content")
        )
        self.base_client = BaseClient("compute", config, signer, core_type_mapping)

    def attach_boot_volume(self, attach_boot_volume_details, **kwargs):
        """
        AttachBootVolume
        Attaches the specified boot volume to the specified instance.


        :param AttachBootVolumeDetails attach_boot_volume_details: (required)
            Attach boot volume request

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolumeAttachment`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/bootVolumeAttachments/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "attach_boot_volume got unknown kwargs: {!r}".format(extra_kwargs))

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
            body=attach_boot_volume_details,
            response_type="BootVolumeAttachment")

    def attach_vnic(self, attach_vnic_details, **kwargs):
        """
        AttachVnic
        Creates a secondary VNIC and attaches it to the specified instance.
        For more information about secondary VNICs, see
        `Virtual Network Interface Cards (VNICs)`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingVNICs.htm


        :param AttachVnicDetails attach_vnic_details: (required)
            Attach VNIC details.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VnicAttachment`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vnicAttachments/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "attach_vnic got unknown kwargs: {!r}".format(extra_kwargs))

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
            body=attach_vnic_details,
            response_type="VnicAttachment")

    def attach_volume(self, attach_volume_details, **kwargs):
        """
        AttachVolume
        Attaches the specified storage volume to the specified instance.


        :param AttachVolumeDetails attach_volume_details: (required)
            Attach volume request

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeAttachment`
        :rtype: :class:`~oci.response.Response`
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
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.ConsoleHistory`
        :rtype: :class:`~oci.response.Response`
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
        Creates a boot disk image for the specified instance or imports an exported image from the Oracle Cloud Infrastructure Object Storage service.

        When creating a new image, you must provide the OCID of the instance you want to use as the basis for the image, and
        the OCID of the compartment containing that instance. For more information about images,
        see `Managing Custom Images`__.

        When importing an exported image from Object Storage, you specify the source information
        in :func:`image_source_details`.

        When importing an image based on the namespace, bucket name, and object name,
        use :func:`image_source_via_object_storage_tuple_details`.

        When importing an image based on the Object Storage URL, use
        :func:`image_source_via_object_storage_uri_details`.
        See `Object Storage URLs`__ and `pre-authenticated requests`__
        for constructing URLs for image import/export.

        For more information about importing exported images, see
        `Image Import/Export`__.

        You may optionally specify a *display name* for the image, which is simply a friendly name or description.
        It does not have to be unique, and you can change it. See :func:`update_image`.
        Avoid entering confidential information.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/managingcustomimages.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/imageimportexport.htm#URLs
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingaccess.htm#pre-auth
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/imageimportexport.htm


        :param CreateImageDetails create_image_details: (required)
            Image creation details

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Image`
        :rtype: :class:`~oci.response.Response`
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

    def create_instance_console_connection(self, create_instance_console_connection_details, **kwargs):
        """
        CreateInstanceConsoleConnection
        Creates a new console connection to the specified instance.
        Once the console connection has been created and is available,
        you connect to the console using SSH.

        For more information about console access, see `Accessing the Console`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/References/serialconsole.htm


        :param CreateInstanceConsoleConnectionDetails create_instance_console_connection_details: (required)
            Request object for creating an InstanceConsoleConnection

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.InstanceConsoleConnection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/instanceConsoleConnections"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_instance_console_connection got unknown kwargs: {!r}".format(extra_kwargs))

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
            body=create_instance_console_connection_details,
            response_type="InstanceConsoleConnection")

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

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

    def delete_instance_console_connection(self, instance_console_connection_id, **kwargs):
        """
        DeleteInstanceConsoleConnection
        Deletes the specified instance console connection.


        :param str instance_console_connection_id: (required)
            The OCID of the intance console connection

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/instanceConsoleConnections/{instanceConsoleConnectionId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_instance_console_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "instanceConsoleConnectionId": instance_console_connection_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

    def detach_boot_volume(self, boot_volume_attachment_id, **kwargs):
        """
        DetachBootVolume
        Detaches a boot volume from an instance. You must specify the OCID of the boot volume attachment.

        This is an asynchronous operation. The attachment's `lifecycleState` will change to DETACHING temporarily
        until the attachment is completely removed.


        :param str boot_volume_attachment_id: (required)
            The OCID of the boot volume attachment.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/bootVolumeAttachments/{bootVolumeAttachmentId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "detach_boot_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeAttachmentId": boot_volume_attachment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

    def detach_vnic(self, vnic_attachment_id, **kwargs):
        """
        DetachVnic
        Detaches and deletes the specified secondary VNIC.
        This operation cannot be used on the instance's primary VNIC.
        When you terminate an instance, all attached VNICs (primary
        and secondary) are automatically detached and deleted.

        **Important:** If the VNIC has a
        :class:`PrivateIp` that is the
        `target of a route rule`__,
        deleting the VNIC causes that route rule to blackhole and the traffic
        will be dropped.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingroutetables.htm#privateip


        :param str vnic_attachment_id: (required)
            The OCID of the VNIC attachment.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vnicAttachments/{vnicAttachmentId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "detach_vnic got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vnicAttachmentId": vnic_attachment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

        This is an asynchronous operation. The attachment's `lifecycleState` will change to DETACHING temporarily
        until the attachment is completely removed.


        :param str volume_attachment_id: (required)
            The OCID of the volume attachment.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

    def export_image(self, image_id, export_image_details, **kwargs):
        """
        ExportImage
        Exports the specified image to the Oracle Cloud Infrastructure Object Storage service. You can use the Object Storage URL,
        or the namespace, bucket name, and object name when specifying the location to export to.

        For more information about exporting images, see `Image Import/Export`__.

        To perform an image export, you need write access to the Object Storage bucket for the image,
        see `Let Users Write Objects to Object Storage Buckets`__.

        See `Object Storage URLs`__ and `pre-authenticated requests`__
        for constructing URLs for image import/export.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/imageimportexport.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/commonpolicies.htm#Let4
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/imageimportexport.htm#URLs
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingaccess.htm#pre-auth


        :param str image_id: (required)
            The OCID of the image.

        :param ExportImageDetails export_image_details: (required)
            Details for the image export.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Image`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/images/{imageId}/actions/export"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "export_image got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "imageId": image_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
            body=export_image_details,
            response_type="Image")

    def get_boot_volume_attachment(self, boot_volume_attachment_id, **kwargs):
        """
        GetBootVolumeAttachment
        Gets information about the specified boot volume attachment.


        :param str boot_volume_attachment_id: (required)
            The OCID of the boot volume attachment.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolumeAttachment`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/bootVolumeAttachments/{bootVolumeAttachmentId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_boot_volume_attachment got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "bootVolumeAttachmentId": boot_volume_attachment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="BootVolumeAttachment")

    def get_console_history(self, instance_console_history_id, **kwargs):
        """
        GetConsoleHistory
        Shows the metadata for the specified console history.
        See :func:`capture_console_history`
        for details about using the console history operations.


        :param str instance_console_history_id: (required)
            The OCID of the console history.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.ConsoleHistory`
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

        :return: A :class:`~oci.response.Response` object with data of type bytes
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Image`
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Instance`
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

    def get_instance_console_connection(self, instance_console_connection_id, **kwargs):
        """
        GetInstanceConsoleConnection
        Gets the specified instance console connection's information.


        :param str instance_console_connection_id: (required)
            The OCID of the intance console connection

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.InstanceConsoleConnection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/instanceConsoleConnections/{instanceConsoleConnectionId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_instance_console_connection got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "instanceConsoleConnectionId": instance_console_connection_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="InstanceConsoleConnection")

    def get_vnic_attachment(self, vnic_attachment_id, **kwargs):
        """
        GetVnicAttachment
        Gets the information for the specified VNIC attachment.


        :param str vnic_attachment_id: (required)
            The OCID of the VNIC attachment.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VnicAttachment`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vnicAttachments/{vnicAttachmentId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_vnic_attachment got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "vnicAttachmentId": vnic_attachment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="VnicAttachment")

    def get_volume_attachment(self, volume_attachment_id, **kwargs):
        """
        GetVolumeAttachment
        Gets information about the specified volume attachment.


        :param str volume_attachment_id: (required)
            The OCID of the volume attachment.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeAttachment`
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.InstanceCredentials`
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

            Allowed values are: "STOP", "START", "SOFTRESET", "RESET"

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Instance`
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

        All Oracle Cloud Infrastructure resources, including instances, get an Oracle-assigned,
        unique ID called an Oracle Cloud Identifier (OCID).
        When you create a resource, you can find its OCID in the response. You can
        also retrieve a resource's OCID by using a List API operation
        on that resource type, or by viewing the resource in the Console.

        When you launch an instance, it is automatically attached to a virtual
        network interface card (VNIC), called the *primary VNIC*. The VNIC
        has a private IP address from the subnet's CIDR. You can either assign a
        private IP address of your choice or let Oracle automatically assign one.
        You can choose whether the instance has a public IP address. To retrieve the
        addresses, use the :func:`list_vnic_attachments`
        operation to get the VNIC ID for the instance, and then call
        :func:`get_vnic` with the VNIC ID.

        You can later add secondary VNICs to an instance. For more information, see
        `Virtual Network Interface Cards (VNICs)`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Concepts/computeoverview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingVNICs.htm


        :param LaunchInstanceDetails launch_instance_details: (required)
            Instance details

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Instance`
        :rtype: :class:`~oci.response.Response`
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

    def list_boot_volume_attachments(self, availability_domain, compartment_id, **kwargs):
        """
        ListBootVolumeAttachments
        Lists the boot volume attachments in the specified compartment. You can filter the
        list by specifying an instance OCID, boot volume OCID, or both.


        :param str availability_domain: (required)
            The name of the Availability Domain.

            Example: `Uocm:PHX-AD-1`

        :param str compartment_id: (required)
            The OCID of the compartment.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str instance_id: (optional)
            The OCID of the instance.

        :param str boot_volume_id: (optional)
            The OCID of the boot volume.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.BootVolumeAttachment`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/bootVolumeAttachments/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page",
            "instance_id",
            "boot_volume_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_boot_volume_attachments got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "instanceId": kwargs.get("instance_id", missing),
            "bootVolumeId": kwargs.get("boot_volume_id", missing)
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
            response_type="list[BootVolumeAttachment]")

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

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by Availability Domain if the scope of the resource type is within a
            single Availability Domain. If you call one of these \"List\" operations without specifying
            an Availability Domain, the resources are grouped by Availability Domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.

            Allowed values are: "REQUESTED", "GETTING-HISTORY", "SUCCEEDED", "FAILED"

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.ConsoleHistory`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/instanceConsoleHistories/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "availability_domain",
            "limit",
            "page",
            "instance_id",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_console_histories got unknown kwargs: {!r}".format(extra_kwargs))

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
            lifecycle_state_allowed_values = ["REQUESTED", "GETTING-HISTORY", "SUCCEEDED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "instanceId": kwargs.get("instance_id", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
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
        Lists the available images in the specified compartment.
        If you specify a value for the `sortBy` parameter, Oracle-provided images appear first in the list, followed by custom images.
        For more
        information about images, see
        `Managing Custom Images`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/managingcustomimages.htm


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

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

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by Availability Domain if the scope of the resource type is within a
            single Availability Domain. If you call one of these \"List\" operations without specifying
            an Availability Domain, the resources are grouped by Availability Domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.Image`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/images/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "display_name",
            "operating_system",
            "operating_system_version",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_images got unknown kwargs: {!r}".format(extra_kwargs))

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
            lifecycle_state_allowed_values = ["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "displayName": kwargs.get("display_name", missing),
            "operatingSystem": kwargs.get("operating_system", missing),
            "operatingSystemVersion": kwargs.get("operating_system_version", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
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

    def list_instance_console_connections(self, compartment_id, **kwargs):
        """
        ListInstanceConsoleConnections
        Lists the console connections for the specified compartment or instance.

        For more information about console access, see `Accessing the Instance Console`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/References/serialconsole.htm


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str instance_id: (optional)
            The OCID of the instance.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.InstanceConsoleConnection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/instanceConsoleConnections"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "instance_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_instance_console_connections got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "instanceId": kwargs.get("instance_id", missing),
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
            response_type="list[InstanceConsoleConnection]")

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
            A filter to return only resources that match the given display name exactly.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by Availability Domain if the scope of the resource type is within a
            single Availability Domain. If you call one of these \"List\" operations without specifying
            an Availability Domain, the resources are grouped by Availability Domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.Instance`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/instances/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "availability_domain",
            "display_name",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_instances got unknown kwargs: {!r}".format(extra_kwargs))

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
            lifecycle_state_allowed_values = ["PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": compartment_id,
            "displayName": kwargs.get("display_name", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
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

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.Shape`
        :rtype: :class:`~oci.response.Response`
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
        Lists the VNIC attachments in the specified compartment. A VNIC attachment
        resides in the same compartment as the attached instance. The list can be
        filtered by instance, VNIC, or Availability Domain.


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

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.VnicAttachment`
        :rtype: :class:`~oci.response.Response`
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

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.VolumeAttachment`
        :rtype: :class:`~oci.response.Response`
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

        To preserve the boot volume associated with the instance, specify `true` for `PreserveBootVolumeQueryParam`.
        To delete the boot volume when the instance is deleted, specify `false` or do not specify a value for `PreserveBootVolumeQueryParam`.

        This is an asynchronous operation. The instance's `lifecycleState` will change to TERMINATING temporarily
        until the instance is completely removed.


        :param str instance_id: (required)
            The OCID of the instance.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param bool preserve_boot_volume: (optional)
            Specifies whether to delete or preserve the boot volume when terminating an instance.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/instances/{instanceId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match",
            "preserve_boot_volume"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "terminate_instance got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "instanceId": instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "preserveBootVolume": kwargs.get("preserve_boot_volume", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

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
            query_params=query_params,
            header_params=header_params)

    def update_console_history(self, instance_console_history_id, update_console_history_details, **kwargs):
        """
        UpdateConsoleHistory
        Updates the specified console history metadata.


        :param str instance_console_history_id: (required)
            The OCID of the console history.

        :param UpdateConsoleHistoryDetails update_console_history_details: (required)
            Update instance fields

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.ConsoleHistory`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/instanceConsoleHistories/{instanceConsoleHistoryId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_console_history got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "instanceConsoleHistoryId": instance_console_history_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
            header_params=header_params,
            body=update_console_history_details,
            response_type="ConsoleHistory")

    def update_image(self, image_id, update_image_details, **kwargs):
        """
        UpdateImage
        Updates the display name of the image. Avoid entering confidential information.


        :param str image_id: (required)
            The OCID of the image.

        :param UpdateImageDetails update_image_details: (required)
            Updates the image display name field. Avoid entering confidential information.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Image`
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
        Updates the display name of the specified instance. Avoid entering confidential information.
        The OCID of the instance remains the same.


        :param str instance_id: (required)
            The OCID of the instance.

        :param UpdateInstanceDetails update_instance_details: (required)
            Update instance fields

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Instance`
        :rtype: :class:`~oci.response.Response`
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

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
