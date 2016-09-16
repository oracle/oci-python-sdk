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

class ComputeApi(object):

    def __init__(self, config):
        signer = Signer(config.tenancy, config.user, config.fingerprint, config.key_file)
        self.api_client =  ApiClient(config, signer)


    def attach_volume(self, attach_volume_details, **kwargs):
        """
        AttachVolume
        Attaches a storage volume to the specified instance.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param AttachVolumeDetails attach_volume_details: Attach volume request (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type VolumeAttachment
        """

        all_params = ['attach_volume_details', 'opc_retry_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method attach_volume" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'attach_volume_details' is set
        if ('attach_volume_details' not in params) or (params['attach_volume_details'] is None):
            raise ValueError("Missing the required parameter `attach_volume_details` when calling `attach_volume`")

        resource_path = '/volumeAttachments/'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None
        if 'attach_volume_details' in params:
            body_params = params['attach_volume_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='VolumeAttachment')
        return response

    def capture_console_history(self, capture_console_history_details, **kwargs):
        """
        CaptureConsoleHistory
        Captures the most recent serial console data (up to a megabyte) for the\nspecified instance. The data includes configuration messages that occur when the\ninstance boots, such as kernel and BIOS messages, and is useful for checking the\nstatus of the instance or diagnosing problems.  The console data is minimally\nformatted ASCII text.\n\nThe `CaptureConsoleHistory` operation works with the other console history operations\nas described below.\n\n1. Use `CaptureConsoleHistory` to request the capture of up to a megabyte of the\nmost recent console history. This call returns a `ConsoleHistoryMetadata`\nobject. The object will have a state of `requested`.\n2. Wait for the capture operation to succeed by polling `GetConsoleHistory` with\nthe identifier of the console history metadata. The state of the\n`ConsoleHistoryMetadata` object will go from `requested` to `getting-history` and\nthen `succeeded` (or `failed`).\n3. Use `ShowConsoleHistoryData` to get the actual console history data (not the\nmetadata).\n4. Optionally, use `DeleteConsoleHistory` to delete the console history metadata\nand the console history data.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CaptureConsoleHistoryDetails capture_console_history_details: Console history details (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type ConsoleHistoryMetadata
        """

        all_params = ['capture_console_history_details', 'opc_retry_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method capture_console_history" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'capture_console_history_details' is set
        if ('capture_console_history_details' not in params) or (params['capture_console_history_details'] is None):
            raise ValueError("Missing the required parameter `capture_console_history_details` when calling `capture_console_history`")

        resource_path = '/instanceConsoleHistories/'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None
        if 'capture_console_history_details' in params:
            body_params = params['capture_console_history_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='ConsoleHistoryMetadata')
        return response

    def create_image(self, create_image_details, **kwargs):
        """
        CreateImage
        Creates a boot disk image for the specified instance. For more information about images, see\n[Managing Custom Images](/Content/Compute/Tasks/managingcustomimages.htm).\n\nYou must provide the OCID of the instance you want to use as the basis for the image.\n\nYou must provide the OCID of the compartment containing the instance you want to use as the basis for the image.\nConsult an Oracle Bare Metal Cloud Administrator in your organization if you're not sure which compartment to\nuse.\n\nYou may specify a *display name* for the image, which is simply a friendly name or description.\nIt does not have to be unique, and it is changeable. See [UpdateImage](#/en/iaas/20160918/Image/UpdateImage).\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateImageDetails create_image_details: Image creation details (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type Image
        """

        all_params = ['create_image_details', 'opc_retry_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_image" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_image_details' is set
        if ('create_image_details' not in params) or (params['create_image_details'] is None):
            raise ValueError("Missing the required parameter `create_image_details` when calling `create_image`")

        resource_path = '/images/'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None
        if 'create_image_details' in params:
            body_params = params['create_image_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Image')
        return response

    def delete_console_history(self, instance_console_history_id, **kwargs):
        """
        DeleteConsoleHistory
        Deletes the specified console history metadata and the console history data.

        :param str instance_console_history_id: The OCID of the console history. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['instance_console_history_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_console_history" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'instance_console_history_id' is set
        if ('instance_console_history_id' not in params) or (params['instance_console_history_id'] is None):
            raise ValueError("Missing the required parameter `instance_console_history_id` when calling `delete_console_history`")

        resource_path = '/instanceConsoleHistories/{instanceConsoleHistoryId}'
        path_params = {}
        if 'instance_console_history_id' in params:
            path_params['instanceConsoleHistoryId'] = params['instance_console_history_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def delete_image(self, image_id, **kwargs):
        """
        DeleteImage
        Deletes an image.

        :param str image_id: The OCID of the image. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['image_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_image" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'image_id' is set
        if ('image_id' not in params) or (params['image_id'] is None):
            raise ValueError("Missing the required parameter `image_id` when calling `delete_image`")

        resource_path = '/images/{imageId}'
        path_params = {}
        if 'image_id' in params:
            path_params['imageId'] = params['image_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def detach_volume(self, volume_attachment_id, **kwargs):
        """
        DetachVolume
        Detaches a storage volume from the specified instance.\n\nThis is an asynchronous operation; the attachment's `lifecycleState` will change to DETACHING temporarily\nuntil the attachment is completely removed.\n

        :param str volume_attachment_id: The OCID of the volume attachment. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['volume_attachment_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method detach_volume" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'volume_attachment_id' is set
        if ('volume_attachment_id' not in params) or (params['volume_attachment_id'] is None):
            raise ValueError("Missing the required parameter `volume_attachment_id` when calling `detach_volume`")

        resource_path = '/volumeAttachments/{volumeAttachmentId}'
        path_params = {}
        if 'volume_attachment_id' in params:
            path_params['volumeAttachmentId'] = params['volume_attachment_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def get_console_history(self, instance_console_history_id, **kwargs):
        """
        GetConsoleHistory
        Shows the metadata for the specified console history.\nSee [CaptureConsoleHistory](#/en/iaas/20160918/ConsoleHistoryMetadata/CaptureConsoleHistory)\nfor details about using the console history operations.\n

        :param str instance_console_history_id: The OCID of the console history. (required)
        :return: A Response object with data of type ConsoleHistoryMetadata
        """

        all_params = ['instance_console_history_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_console_history" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'instance_console_history_id' is set
        if ('instance_console_history_id' not in params) or (params['instance_console_history_id'] is None):
            raise ValueError("Missing the required parameter `instance_console_history_id` when calling `get_console_history`")

        resource_path = '/instanceConsoleHistories/{instanceConsoleHistoryId}'
        path_params = {}
        if 'instance_console_history_id' in params:
            path_params['instanceConsoleHistoryId'] = params['instance_console_history_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='ConsoleHistoryMetadata')
        return response

    def get_image(self, image_id, **kwargs):
        """
        GetImage
        Gets the specified image.

        :param str image_id: The OCID of the image. (required)
        :return: A Response object with data of type Image
        """

        all_params = ['image_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'image_id' is set
        if ('image_id' not in params) or (params['image_id'] is None):
            raise ValueError("Missing the required parameter `image_id` when calling `get_image`")

        resource_path = '/images/{imageId}'
        path_params = {}
        if 'image_id' in params:
            path_params['imageId'] = params['image_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Image')
        return response

    def get_instance(self, instance_id, **kwargs):
        """
        GetInstance
        Gets information about the specified instance.

        :param str instance_id: The OCID of the instance. (required)
        :return: A Response object with data of type Instance
        """

        all_params = ['instance_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_instance" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'instance_id' is set
        if ('instance_id' not in params) or (params['instance_id'] is None):
            raise ValueError("Missing the required parameter `instance_id` when calling `get_instance`")

        resource_path = '/instances/{instanceId}'
        path_params = {}
        if 'instance_id' in params:
            path_params['instanceId'] = params['instance_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Instance')
        return response

    def get_volume_attachment(self, volume_attachment_id, **kwargs):
        """
        GetVolumeAttachment
        Gets information about the specified volume attachment.

        :param str volume_attachment_id: The OCID of the volume attachment. (required)
        :return: A Response object with data of type VolumeAttachment
        """

        all_params = ['volume_attachment_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_volume_attachment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'volume_attachment_id' is set
        if ('volume_attachment_id' not in params) or (params['volume_attachment_id'] is None):
            raise ValueError("Missing the required parameter `volume_attachment_id` when calling `get_volume_attachment`")

        resource_path = '/volumeAttachments/{volumeAttachmentId}'
        path_params = {}
        if 'volume_attachment_id' in params:
            path_params['volumeAttachmentId'] = params['volume_attachment_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='VolumeAttachment')
        return response

    def instance_action(self, instance_id, action, **kwargs):
        """
        InstanceAction
        Performs one of the power actions (start, stop, softreset, or reset),\non the specified instance.\n\n**start** - power on\n\n**stop** - power off\n\n**softreset** - ACPI shutdown and power on\n\n**reset** - power off and power on\n\nNote that the **stop** state has no effect on the resources you consume.\nBilling continues for instances that you stop, and related resources continue\nto apply against any relevant quotas. You must [Terminate](#/en/iaas/20160918/Instance/TerminateInstance)\nan instance to remove its resources from billing and quotas.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str instance_id: The OCID of the instance. (required)
        :param str action: The action to perform on the instance. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type Instance
        """

        all_params = ['instance_id', 'action', 'opc_retry_token', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method instance_action" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'instance_id' is set
        if ('instance_id' not in params) or (params['instance_id'] is None):
            raise ValueError("Missing the required parameter `instance_id` when calling `instance_action`")
        # verify the required parameter 'action' is set
        if ('action' not in params) or (params['action'] is None):
            raise ValueError("Missing the required parameter `action` when calling `instance_action`")

        resource_path = '/instances/{instanceId}'
        path_params = {}
        if 'instance_id' in params:
            path_params['instanceId'] = params['instance_id']

        query_params = {}
        if 'action' in params:
            query_params['action'] = params['action']

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Instance')
        return response

    def launch_instance(self, launch_instance_details, **kwargs):
        """
        LaunchInstance
        Creates a new instance in the specified compartment and the specified Availability Domain.\n\nFor information about access control and compartments, see\n[Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm).\n\nFor information about Availability Domains, see\n[Regions and Availability Domains](/Content/General/Concepts/regions.htm).\nTo get a list of Availablity Domains, use the `ListAvailabilityDomains` operation\nin the Identity and Access Management Service API.\n\nAll Oracle Bare Metal IaaS resources, including instances, get an Oracle-assigned,\nunique ID called an Oracle Cloud Identifier (OCID).\nWhen you create a resource, you can find its OCID in the response. You can\nalso retrieve a resource's OCID by using a List API operation\non that resource type, or by viewing the resource in the Console.\n\nWhen you launch an instance, it is automatically attached to a Virtual\nNetwork Interface Card (VNIC) and given both a public and private IP address.\nTo get both addresses, use the [ListVnicAttachments](#/en/iaas/20160918/VnicAttachment/ListVnicAttachments)\noperation to get the VNIC ID for the instance, and then call\n[GetVnic](#/en/iaas/20160918/Vnic/GetVnic) with the VNIC ID.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param LaunchInstanceDetails launch_instance_details: Instance details (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :param str opc_host_serial: For Oracle internal use only.
        :param str opc_pool_name: For Oracle internal use only.
        :param str opc_vnic_id: For Oracle internal use only.
        :return: A Response object with data of type Instance
        """

        all_params = ['launch_instance_details', 'opc_retry_token', 'opc_host_serial', 'opc_pool_name', 'opc_vnic_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method launch_instance" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'launch_instance_details' is set
        if ('launch_instance_details' not in params) or (params['launch_instance_details'] is None):
            raise ValueError("Missing the required parameter `launch_instance_details` when calling `launch_instance`")

        resource_path = '/instances/'
        path_params = {}

        query_params = {}
        if 'opc_host_serial' in params:
            query_params['opc-host-serial'] = params['opc_host_serial']
        if 'opc_pool_name' in params:
            query_params['opc-pool-name'] = params['opc_pool_name']
        if 'opc_vnic_id' in params:
            query_params['opc-vnic-id'] = params['opc_vnic_id']

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None
        if 'launch_instance_details' in params:
            body_params = params['launch_instance_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Instance')
        return response

    def list_console_histories(self, compartment_id, **kwargs):
        """
        ListConsoleHistories
        Lists all the console history metadata for the specified compartment or instance.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str availability_domain: The name of the Availability Domain.\n\nExample: `Uocm:PHX-AD-1`\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param str instance_id: The OCID of the instance.
        :return: A Response object with data of type list[ConsoleHistoryMetadata]
        """

        all_params = ['compartment_id', 'availability_domain', 'limit', 'page', 'instance_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_console_histories" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_console_histories`")

        resource_path = '/instanceConsoleHistories/'
        path_params = {}

        query_params = {}
        if 'availability_domain' in params:
            query_params['availabilityDomain'] = params['availability_domain']
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'instance_id' in params:
            query_params['instanceId'] = params['instance_id']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[ConsoleHistoryMetadata]')
        return response

    def list_images(self, compartment_id, **kwargs):
        """
        ListImages
        Lists images

        :param str compartment_id: The OCID of the compartment. (required)
        :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable.\n\nExample: `My new resource`\n
        :param str operating_system: The image's operating system.\n\nExample: `Oracle Linux`\n
        :param str operating_system_version: The image's operating system version.\n\nExample: `7.2`\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[Image]
        """

        all_params = ['compartment_id', 'display_name', 'operating_system', 'operating_system_version', 'limit', 'page']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_images" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_images`")

        resource_path = '/images/'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'display_name' in params:
            query_params['displayName'] = params['display_name']
        if 'operating_system' in params:
            query_params['operatingSystem'] = params['operating_system']
        if 'operating_system_version' in params:
            query_params['operatingSystemVersion'] = params['operating_system_version']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[Image]')
        return response

    def list_instances(self, compartment_id, **kwargs):
        """
        ListInstances
        Gets a list of all the instances in the specified compartment and the specified Availability Domain.\nYou can limit the list by specifying an instance name (the list will include all the identically-named\ninstances in the compartment).\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str availability_domain: The name of the Availability Domain.\n\nExample: `Uocm:PHX-AD-1`\n
        :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable.\n\nExample: `My new resource`\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[Instance]
        """

        all_params = ['compartment_id', 'availability_domain', 'display_name', 'limit', 'page']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_instances" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_instances`")

        resource_path = '/instances/'
        path_params = {}

        query_params = {}
        if 'availability_domain' in params:
            query_params['availabilityDomain'] = params['availability_domain']
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'display_name' in params:
            query_params['displayName'] = params['display_name']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[Instance]')
        return response

    def list_shapes(self, compartment_id, **kwargs):
        """
        ListShapes
        Lists all shapes that can be used to launch an instance within this compartment. Can filter by\ncompatibility with a specific image.\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str availability_domain: The name of the Availability Domain.\n\nExample: `Uocm:PHX-AD-1`\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param str image_id: The OCID of an image.
        :return: A Response object with data of type list[Shape]
        """

        all_params = ['compartment_id', 'availability_domain', 'limit', 'page', 'image_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_shapes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_shapes`")

        resource_path = '/shapes'
        path_params = {}

        query_params = {}
        if 'availability_domain' in params:
            query_params['availabilityDomain'] = params['availability_domain']
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'image_id' in params:
            query_params['imageId'] = params['image_id']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[Shape]')
        return response

    def list_vnic_attachments(self, compartment_id, **kwargs):
        """
        ListVnicAttachments
        Gets a list of the VNIC attachments for the specified compartment. The list can be filtered by\ninstance and by VNIC.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str availability_domain: The name of the Availability Domain.\n\nExample: `Uocm:PHX-AD-1`\n
        :param str instance_id: The OCID of the instance.
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param str vnic_id: The OCID of the VNIC.
        :return: A Response object with data of type list[VnicAttachment]
        """

        all_params = ['compartment_id', 'availability_domain', 'instance_id', 'limit', 'page', 'vnic_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_vnic_attachments" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_vnic_attachments`")

        resource_path = '/vnicAttachments/'
        path_params = {}

        query_params = {}
        if 'availability_domain' in params:
            query_params['availabilityDomain'] = params['availability_domain']
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'instance_id' in params:
            query_params['instanceId'] = params['instance_id']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'vnic_id' in params:
            query_params['vnicId'] = params['vnic_id']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[VnicAttachment]')
        return response

    def list_volume_attachments(self, compartment_id, **kwargs):
        """
        ListVolumeAttachments
        Gets a list of the volume attachments in the specified compartment. You can limit the\nlist by specifying an instance OCID, volume OCID, or both.\n\nCurrently, the only supported volume attachment type is [IScsiVolumeAttachment](#/en/iaas/20160918/IScsiVolumeAttachment/).\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str availability_domain: The name of the Availability Domain.\n\nExample: `Uocm:PHX-AD-1`\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :param str instance_id: The OCID of the instance.
        :param str volume_id: The OCID of the volume.
        :return: A Response object with data of type list[VolumeAttachment]
        """

        all_params = ['compartment_id', 'availability_domain', 'limit', 'page', 'instance_id', 'volume_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_volume_attachments" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_volume_attachments`")

        resource_path = '/volumeAttachments/'
        path_params = {}

        query_params = {}
        if 'availability_domain' in params:
            query_params['availabilityDomain'] = params['availability_domain']
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'instance_id' in params:
            query_params['instanceId'] = params['instance_id']
        if 'volume_id' in params:
            query_params['volumeId'] = params['volume_id']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[VolumeAttachment]')
        return response

    def show_console_history_data(self, instance_console_history_id, **kwargs):
        """
        ShowConsoleHistoryData
        Gets the actual console history data (not the metadata).\nSee [CaptureConsoleHistory](#/en/iaas/20160918/ConsoleHistoryMetadata/CaptureConsoleHistory)\nfor details about using the console history operations.\n

        :param str instance_console_history_id: The OCID of the console history. (required)
        :param int offset: Offset of the snapshot data to retrieve.
        :param int length: Length of the snapshot data to retrieve.
        :return: A Response object with data of type str
        """

        all_params = ['instance_console_history_id', 'offset', 'length']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show_console_history_data" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'instance_console_history_id' is set
        if ('instance_console_history_id' not in params) or (params['instance_console_history_id'] is None):
            raise ValueError("Missing the required parameter `instance_console_history_id` when calling `show_console_history_data`")

        resource_path = '/instanceConsoleHistories/{instanceConsoleHistoryId}/data'
        path_params = {}
        if 'instance_console_history_id' in params:
            path_params['instanceConsoleHistoryId'] = params['instance_console_history_id']

        query_params = {}
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'length' in params:
            query_params['length'] = params['length']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='str')
        return response

    def terminate_instance(self, instance_id, **kwargs):
        """
        TerminateInstance
        Terminates the specified instance. Any attached VNICs and volumes are automatically detached\nwhen the instance terminates.\n\nThis is an asynchronous operation; the instance's `lifecycleState` will change to TERMINATING temporarily\nuntil the instance is completely removed.\n

        :param str instance_id: The OCID of the instance. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['instance_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method terminate_instance" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'instance_id' is set
        if ('instance_id' not in params) or (params['instance_id'] is None):
            raise ValueError("Missing the required parameter `instance_id` when calling `terminate_instance`")

        resource_path = '/instances/{instanceId}'
        path_params = {}
        if 'instance_id' in params:
            path_params['instanceId'] = params['instance_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def update_image(self, image_id, update_image_details, **kwargs):
        """
        UpdateImage
        Updates the name of the image.

        :param str image_id: The OCID of the image. (required)
        :param UpdateImageDetails update_image_details: Updates the image display name field. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type Image
        """

        all_params = ['image_id', 'update_image_details', 'opc_retry_token', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_image" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'image_id' is set
        if ('image_id' not in params) or (params['image_id'] is None):
            raise ValueError("Missing the required parameter `image_id` when calling `update_image`")
        # verify the required parameter 'update_image_details' is set
        if ('update_image_details' not in params) or (params['update_image_details'] is None):
            raise ValueError("Missing the required parameter `update_image_details` when calling `update_image`")

        resource_path = '/images/{imageId}'
        path_params = {}
        if 'image_id' in params:
            path_params['imageId'] = params['image_id']

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_image_details' in params:
            body_params = params['update_image_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Image')
        return response

    def update_instance(self, instance_id, update_instance_details, **kwargs):
        """
        UpdateInstance
        Updates the name of the specified instance. The OCID of the instance remains the same.

        :param str instance_id: The OCID of the instance. (required)
        :param UpdateInstanceDetails update_instance_details: Update instance fields (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type Instance
        """

        all_params = ['instance_id', 'update_instance_details', 'opc_retry_token', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_instance" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'instance_id' is set
        if ('instance_id' not in params) or (params['instance_id'] is None):
            raise ValueError("Missing the required parameter `instance_id` when calling `update_instance`")
        # verify the required parameter 'update_instance_details' is set
        if ('update_instance_details' not in params) or (params['update_instance_details'] is None):
            raise ValueError("Missing the required parameter `update_instance_details` when calling `update_instance`")

        resource_path = '/instances/{instanceId}'
        path_params = {}
        if 'instance_id' in params:
            path_params['instanceId'] = params['instance_id']

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_instance_details' in params:
            body_params = params['update_instance_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_compute_api,
                                            resource_path,
                                            'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Instance')
        return response
