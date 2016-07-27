# coding: utf-8

"""
This is a modified version of the same template from swagger-codegen.
The original can be found at https://github.com/swagger-api/swagger-codegen.
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

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class ComputeApi(object):

    def __init__(self, api_client):
        self.api_client = api_client


    def attach_volume(self, attach_volume_request, **kwargs):
        """
        AttachVolume
        Attaches a storage volume to the specified instance.

        :param AttachVolumeRequest attach_volume_request: Attach volume request (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :return: VolumeAttachment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['attach_volume_request', 'opc_idempotency_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method attach_volume" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'attach_volume_request' is set
        if ('attach_volume_request' not in params) or (params['attach_volume_request'] is None):
            raise ValueError("Missing the required parameter `attach_volume_request` when calling `attach_volume`")

        resource_path = '/volumeAttachments/'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']

        body_params = None
        if 'attach_volume_request' in params:
            body_params = params['attach_volume_request']

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

    def capture_console_history(self, capture_console_history_request, **kwargs):
        """
        CaptureConsoleHistory
        Captures the most recent serial console data (up to a megabyte) for the\nspecified instance. The data includes configuration messages that occur when the\ninstance boots, such as kernel and BIOS messages, and is useful for checking the\nstatus of the instance or diagnosing problems.  The console data is minimally\nformatted ASCII text.\n\nThe `CaptureConsoleHistory` operation works with the other console history operations\nas described below.\n\n1. Use `CaptureConsoleHistory` to request the capture of up to a megabyte of the\nmost recent console history. This call returns a `ConsoleHistoryMetadata`\nobject. The object will have a state of `requested`.\n2. Wait for the capture operation to succeed by polling `GetConsoleHistory` with\nthe identifier of the console history metadata. The state of the\n`ConsoleHistoryMetadata` object will go from `requested` to `getting-history` and\nthen `succeeded` (or `failed`).\n3. Use `ShowConsoleHistoryData` to get the actual console history data (not the\nmetadata).\n4. Optionally, use `DeleteConsoleHistory` to delete the console history metadata\nand the console history data.\n

        :param CaptureConsoleHistoryRequest capture_console_history_request: Console history request (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :return: ConsoleHistoryMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['capture_console_history_request', 'opc_idempotency_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method capture_console_history" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'capture_console_history_request' is set
        if ('capture_console_history_request' not in params) or (params['capture_console_history_request'] is None):
            raise ValueError("Missing the required parameter `capture_console_history_request` when calling `capture_console_history`")

        resource_path = '/instanceConsoleHistories/'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']

        body_params = None
        if 'capture_console_history_request' in params:
            body_params = params['capture_console_history_request']

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

    def delete_console_history(self, instance_console_history_id, **kwargs):
        """
        DeleteConsoleHistory
        Deletes the specified console history metadata and the console history data.

        :param str instance_console_history_id: The OCID of the console history. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
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

    def detach_volume(self, volume_attachment_id, **kwargs):
        """
        DetachVolume
        Detaches a storage volume from the specified instance.

        :param str volume_attachment_id: The OCID of the volume attachment. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
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
        Shows the metadata for the specified console history.\nSee [CaptureConsoleHistory] (#captureConsoleHistory)\nfor details about using the console history operations.\n

        :param str instance_console_history_id: The OCID of the console history. (required)
        :return: ConsoleHistoryMetadata
                 If the method is called asynchronously,
                 returns the request thread.
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

    def get_instance(self, instance_id, **kwargs):
        """
        GetInstance
        Gets information about the specified instance.

        :param str instance_id: The OCID of the instance. (required)
        :return: Instance
                 If the method is called asynchronously,
                 returns the request thread.
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
        :return: VolumeAttachment
                 If the method is called asynchronously,
                 returns the request thread.
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
        Performs an action, such as one of the power actions (start, stop, or reset),\non the specified instance.\n

        :param str instance_id: The OCID of the instance. (required)
        :param str action: The action to perform on the instance. (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: Instance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_id', 'action', 'opc_idempotency_token', 'if_match']

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
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']
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

    def launch_instance(self, launch_instance_request, **kwargs):
        """
        LaunchInstance
        Creates a new instance in the specified compartment and the specified Availability Domain.\n\nFor information about access control and compartments, see\n[Overview of the Identity Service](../../../#Identity/Concepts/overview.htm).\n\nFor information about Availability Domains, see\n[Regions and Availability Domains](../../../#General/Concepts/regions.htm).\nTo get a list of Availablity Domains, use the `ListAvailabilityDomains` operation\nin the Identity Service API.\n\nAll Oracle Bare Metal IaaS resources, including instances, get an Oracle-assigned,\nunique ID called an Oracle Cloud Identifier (OCID).\nWhen you create a resource, you can find its OCID in the response. You can\nalso retrieve a resource's OCID by using a List API operation\non that resource type, or by viewing the resource in the Console.\n\nWhen you launch an instance, it is automatically attached to a Virtual\nNetwork Interface Card (VNIC) and given both a public and private IP address.\nTo get both addresses, use the [ListVnicAttachments](#listVnicAttachments)\noperation to get the VNIC ID for the instance, and then call\n[GetVnic](#getVnic) with the VNIC ID.\n

        :param LaunchInstanceRequest launch_instance_request: Instance request (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :param str opc_host_serial: For Oracle internal use only.
        :param str opc_vnic_id: For Oracle internal use only.
        :return: Instance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['launch_instance_request', 'opc_idempotency_token', 'opc_host_serial', 'opc_vnic_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method launch_instance" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'launch_instance_request' is set
        if ('launch_instance_request' not in params) or (params['launch_instance_request'] is None):
            raise ValueError("Missing the required parameter `launch_instance_request` when calling `launch_instance`")

        resource_path = '/instances/'
        path_params = {}

        query_params = {}
        if 'opc_host_serial' in params:
            query_params['opc-host-serial'] = params['opc_host_serial']
        if 'opc_vnic_id' in params:
            query_params['opc-vnic-id'] = params['opc_vnic_id']

        header_params = {}
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']

        body_params = None
        if 'launch_instance_request' in params:
            body_params = params['launch_instance_request']

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
        Lists all the console history metadata for the specified compartment or instance.

        :param str compartment_id: The OCID of the compartment. (required)
        :param str availability_domain: The name of the Availability Domain.
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str instance_id: The OCID of the instance.
        :return: list[ConsoleHistoryMetadata]
                 If the method is called asynchronously,
                 returns the request thread.
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

    def list_instances(self, compartment_id, **kwargs):
        """
        ListInstances
        Gets a list of all the instances in the specified compartment and the specified Availability Domain.\nYou can limit the list by specifying an instance name (the list will include all the identically-named\ninstances in the compartment).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str availability_domain: The name of the Availability Domain.
        :param str display_name: The non-unique, changeable name of the instance.
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :return: list[Instance]
                 If the method is called asynchronously,
                 returns the request thread.
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
        :param str availability_domain: The name of the Availability Domain.
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str image_id: The Oracle ID (OCID) of an image\n
        :return: list[Shape]
                 If the method is called asynchronously,
                 returns the request thread.
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
        Gets a list of the VNIC attachments for the specified instance.

        :param str compartment_id: The OCID of the compartment. (required)
        :param str availability_domain: The name of the Availability Domain.
        :param str instance_id: The OCID of the instance.
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str vnic_id: The OCID of the VNIC.
        :return: list[VnicAttachment]
                 If the method is called asynchronously,
                 returns the request thread.
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
        Gets a list of the volume attachments in the specified compartment. You can limit the\nlist by specifying an instance OCID, volume OCID, or both.\n\nCurrently, the only supported volume attachment type is [IScsiVolumeAttachment](#IScsiVolumeAttachment).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str availability_domain: The name of the Availability Domain.
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str instance_id: The OCID of the instance.
        :param str volume_id: The OCID of the volume.
        :return: list[VolumeAttachment]
                 If the method is called asynchronously,
                 returns the request thread.
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
        Gets the actual console history data (not the metadata).\nSee [CaptureConsoleHistory] (#captureConsoleHistory)\nfor details about using the console history operations.\n

        :param str instance_console_history_id: The OCID of the console history. (required)
        :param int offset: Offset of snapshot data to retrieve
        :param int length: Length of snapshot data to retrieve
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
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
        Terminates the specified instance. Any attached VNICs and volumes are automatically detached\nwhen the instance terminates.\n

        :param str instance_id: The OCID of the instance. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
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

    def update_instance(self, instance_id, update_instance_request, **kwargs):
        """
        UpdateInstance
        Updates the name of the specified instance. The OCID of the instance remains the same.

        :param str instance_id: The OCID of the instance. (required)
        :param UpdateInstanceRequest update_instance_request: Update instance fields (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: Instance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_id', 'update_instance_request', 'opc_idempotency_token', 'if_match']

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
        # verify the required parameter 'update_instance_request' is set
        if ('update_instance_request' not in params) or (params['update_instance_request'] is None):
            raise ValueError("Missing the required parameter `update_instance_request` when calling `update_instance`")

        resource_path = '/instances/{instanceId}'
        path_params = {}
        if 'instance_id' in params:
            path_params['instanceId'] = params['instance_id']

        query_params = {}

        header_params = {}
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_instance_request' in params:
            body_params = params['update_instance_request']

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
