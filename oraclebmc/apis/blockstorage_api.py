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

class BlockstorageApi(object):

    def __init__(self, config):
        signer = Signer(config.tenancy, config.user, config.fingerprint, config.key_file)
        self.api_client =  ApiClient(config, signer)


    def create_volume(self, create_volume_details, **kwargs):
        """
        CreateVolume
        Creates a new 256 GB volume in the specified compartment.\n\nA volume and instance can be in separate compartments but must be in the same Availability Domain. You can set\nthe Availability Domain that the volume will reside in by defining `availabilityDomain`. This setting is\npermanent. You may optionally specify a display name for the volume, which is simply a friendly name or\ndescription. This does not have to be unique and you can change it with `UpdateVolume`.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateVolumeDetails create_volume_details: Request to create a new volume. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type Volume
        """

        all_params = ['create_volume_details', 'opc_retry_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_volume" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_volume_details' is set
        if ('create_volume_details' not in params) or (params['create_volume_details'] is None):
            raise ValueError("Missing the required parameter `create_volume_details` when calling `create_volume`")

        resource_path = '/volumes'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None
        if 'create_volume_details' in params:
            body_params = params['create_volume_details']

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

    def create_volume_backup(self, create_volume_backup_details, **kwargs):
        """
        CreateVolumeBackup
        Creates a new backup of the specified volume.\nWhen the request is received, the backup object is in a REQUEST_RECEIVED state.\nWhen the data is imaged, it goes into a CREATING state.\nAfter the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateVolumeBackupDetails create_volume_backup_details: Request to create a new backup of given volume. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type VolumeBackup
        """

        all_params = ['create_volume_backup_details', 'opc_retry_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_volume_backup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_volume_backup_details' is set
        if ('create_volume_backup_details' not in params) or (params['create_volume_backup_details'] is None):
            raise ValueError("Missing the required parameter `create_volume_backup_details` when calling `create_volume_backup`")

        resource_path = '/volumeBackups'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_retry_token' in params:
            header_params['opc-retry-token'] = params['opc_retry_token']

        body_params = None
        if 'create_volume_backup_details' in params:
            body_params = params['create_volume_backup_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_blockstorage_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='VolumeBackup')
        return response

    def delete_volume(self, volume_id, **kwargs):
        """
        DeleteVolume
        Deletes the specified volume. The volume cannot have an active connection to an instance.\nTo disconnect the volume from a connected instance, see\n[Disconnecting From a Volume](/Content/Block/Tasks/disconnectingfromavolume.htm).\n**Warning:** All data on the volume will be permanently lost when the volume is deleted.\n

        :param str volume_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
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

    def delete_volume_backup(self, volume_backup_id, **kwargs):
        """
        DeleteVolumeBackup
        Deletes a volume backup.

        :param str volume_backup_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume backup. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['volume_backup_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_volume_backup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'volume_backup_id' is set
        if ('volume_backup_id' not in params) or (params['volume_backup_id'] is None):
            raise ValueError("Missing the required parameter `volume_backup_id` when calling `delete_volume_backup`")

        resource_path = '/volumeBackups/{volumeBackupId}'
        path_params = {}
        if 'volume_backup_id' in params:
            path_params['volumeBackupId'] = params['volume_backup_id']

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
        :return: A Response object with data of type Volume
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

    def get_volume_backup(self, volume_backup_id, **kwargs):
        """
        GetVolumeBackup
        Gets information for the specified volume backup.

        :param str volume_backup_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume backup. (required)
        :return: A Response object with data of type VolumeBackup
        """

        all_params = ['volume_backup_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_volume_backup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'volume_backup_id' is set
        if ('volume_backup_id' not in params) or (params['volume_backup_id'] is None):
            raise ValueError("Missing the required parameter `volume_backup_id` when calling `get_volume_backup`")

        resource_path = '/volumeBackups/{volumeBackupId}'
        path_params = {}
        if 'volume_backup_id' in params:
            path_params['volumeBackupId'] = params['volume_backup_id']

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
                                            response_type='VolumeBackup')
        return response

    def list_volume_backups(self, compartment_id, **kwargs):
        """
        ListVolumeBackups
        Gets a list of volume backups in the specified compartment.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str volume_id: The OCID of the volume.
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[VolumeBackup]
        """

        all_params = ['compartment_id', 'volume_id', 'limit', 'page']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_volume_backups" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_volume_backups`")

        resource_path = '/volumeBackups'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'volume_id' in params:
            query_params['volumeId'] = params['volume_id']
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
                                            response_type='list[VolumeBackup]')
        return response

    def list_volumes(self, compartment_id, **kwargs):
        """
        ListVolumes
        Gets a list of volumes in the specified compartment and Availability Domain.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str availability_domain: The name of the Availability Domain.\n\nExample: `Uocm:PHX-AD-1`\n
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[Volume]
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

    def update_volume(self, volume_id, update_volume_details, **kwargs):
        """
        UpdateVolume
        Updates the specified volume's display name.

        :param str volume_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume. (required)
        :param UpdateVolumeDetails update_volume_details: Update volume's display name. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type Volume
        """

        all_params = ['volume_id', 'update_volume_details', 'if_match']

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
        # verify the required parameter 'update_volume_details' is set
        if ('update_volume_details' not in params) or (params['update_volume_details'] is None):
            raise ValueError("Missing the required parameter `update_volume_details` when calling `update_volume`")

        resource_path = '/volumes/{volumeId}'
        path_params = {}
        if 'volume_id' in params:
            path_params['volumeId'] = params['volume_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_volume_details' in params:
            body_params = params['update_volume_details']

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

    def update_volume_backup(self, volume_backup_id, update_volume_backup_details, **kwargs):
        """
        UpdateVolumeBackup
        Updates the display name for the specified volume backup.

        :param str volume_backup_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume backup. (required)
        :param UpdateVolumeBackupDetails update_volume_backup_details: Update volume backup fields (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type VolumeBackup
        """

        all_params = ['volume_backup_id', 'update_volume_backup_details', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_volume_backup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'volume_backup_id' is set
        if ('volume_backup_id' not in params) or (params['volume_backup_id'] is None):
            raise ValueError("Missing the required parameter `volume_backup_id` when calling `update_volume_backup`")
        # verify the required parameter 'update_volume_backup_details' is set
        if ('update_volume_backup_details' not in params) or (params['update_volume_backup_details'] is None):
            raise ValueError("Missing the required parameter `update_volume_backup_details` when calling `update_volume_backup`")

        resource_path = '/volumeBackups/{volumeBackupId}'
        path_params = {}
        if 'volume_backup_id' in params:
            path_params['volumeBackupId'] = params['volume_backup_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_volume_backup_details' in params:
            body_params = params['update_volume_backup_details']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_blockstorage_api,
                                            resource_path,
                                            'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='VolumeBackup')
        return response
