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
# python 2 and python 3 compatibility library
from six import iteritems

class BlockstorageApi(object):

    def __init__(self, api_client):
        self.api_client = api_client


    def create_volume(self, create_volume_request, **kwargs):
        """
        CreateVolume
        Creates a new 256 GB volume in the specified compartment.\nA volume and instance can be in separate compartments but must be in the same Availability Domain. You can set\nthe Availability Domain that the volume will reside in by defining `availabilityDomain`. This setting is permanent.\nYou may optionally specify a display name for the volume, which is simply a friendly name or description. This\ndoes not have to be unique and you can change it with `UpdateVolume`.\n

        :param CreateVolumeRequest create_volume_request: Request to create a new volume. (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :return: Volume
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_volume_request', 'opc_idempotency_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_volume" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_volume_request' is set
        if ('create_volume_request' not in params) or (params['create_volume_request'] is None):
            raise ValueError("Missing the required parameter `create_volume_request` when calling `create_volume`")

        resource_path = '/volumes'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']

        body_params = None
        if 'create_volume_request' in params:
            body_params = params['create_volume_request']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_blockstorage_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Volume')
        return response

    def delete_volume(self, volume_id, **kwargs):
        """
        DeleteVolume
        Deletes the specified volume. The volume can't have an active connection to an instance.\nTo disconnect the volume from a connected instance, see\n[Disconnecting From a Volume](../../../#Block/Tasks/disconnectingfromavolume.htm).\n**Warning:** All data on the volume will be permanently lost once the volume is deleted.\n

        :param str volume_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['volume_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_volume" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'volume_id' is set
        if ('volume_id' not in params) or (params['volume_id'] is None):
            raise ValueError("Missing the required parameter `volume_id` when calling `delete_volume`")

        resource_path = '/volumes/{volumeId}'
        path_params = {}
        if 'volume_id' in params:
            path_params['volumeId'] = params['volume_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_blockstorage_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def get_volume(self, volume_id, **kwargs):
        """
        GetVolume
        Gets information on the specified volume.

        :param str volume_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume. (required)
        :return: Volume
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['volume_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_volume" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'volume_id' is set
        if ('volume_id' not in params) or (params['volume_id'] is None):
            raise ValueError("Missing the required parameter `volume_id` when calling `get_volume`")

        resource_path = '/volumes/{volumeId}'
        path_params = {}
        if 'volume_id' in params:
            path_params['volumeId'] = params['volume_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_blockstorage_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Volume')
        return response

    def list_volumes(self, compartment_id, **kwargs):
        """
        ListVolumes
        Gets a list of volumes in the specified compartment and Availability Domain.

        :param str compartment_id: The OCID of the compartment. (required)
        :param str availability_domain: The name of the Availability Domain.
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :return: list[Volume]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['compartment_id', 'availability_domain', 'limit', 'page']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_volumes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_volumes`")

        resource_path = '/volumes'
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

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_blockstorage_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[Volume]')
        return response

    def update_volume(self, volume_id, update_volume_request, **kwargs):
        """
        UpdateVolume
        Updates the specified volume's display name.

        :param str volume_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume. (required)
        :param UpdateVolumeRequest update_volume_request: Update volume's display name. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: Volume
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['volume_id', 'update_volume_request', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_volume" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'volume_id' is set
        if ('volume_id' not in params) or (params['volume_id'] is None):
            raise ValueError("Missing the required parameter `volume_id` when calling `update_volume`")
        # verify the required parameter 'update_volume_request' is set
        if ('update_volume_request' not in params) or (params['update_volume_request'] is None):
            raise ValueError("Missing the required parameter `update_volume_request` when calling `update_volume`")

        resource_path = '/volumes/{volumeId}'
        path_params = {}
        if 'volume_id' in params:
            path_params['volumeId'] = params['volume_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_volume_request' in params:
            body_params = params['update_volume_request']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_blockstorage_api,
                                            resource_path,
                                            'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Volume')
        return response
