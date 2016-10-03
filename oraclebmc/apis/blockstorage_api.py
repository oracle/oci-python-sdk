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


class BlockstorageApi(object):

    def __init__(self, config):
        signer = Signer(config.tenancy, config.user, config.fingerprint, config.key_file)
        self.api_client = ApiClient(config, signer)

    def create_volume(self, create_volume_details, **kwargs):
        """
        CreateVolume
        Creates a new 256 GB volume in the specified compartment.\n\nA volume and instance can be in separate compartments but must be in the same Availability Domain. You can set\nthe Availability Domain that the volume will reside in by defining `availabilityDomain`. This setting is\npermanent. You may optionally specify a display name for the volume, which is simply a friendly name or\ndescription. This does not have to be unique and you can change it with `UpdateVolume`.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateVolumeDetails create_volume_details: Request to create a new volume. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type Volume
        """
        resource_path = "/volumes"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_volume_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_volume got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_blockstorage_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_volume_details,
            response_type="Volume")

    def create_volume_backup(self, create_volume_backup_details, **kwargs):
        """
        CreateVolumeBackup
        Creates a new backup of the specified volume.\nWhen the request is received, the backup object is in a REQUEST_RECEIVED state.\nWhen the data is imaged, it goes into a CREATING state.\nAfter the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateVolumeBackupDetails create_volume_backup_details: Request to create a new backup of given volume. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type VolumeBackup
        """
        resource_path = "/volumeBackups"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_volume_backup_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_blockstorage_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_volume_backup_details,
            response_type="VolumeBackup")

    def delete_volume(self, volume_id, **kwargs):
        """
        DeleteVolume
        Deletes the specified volume. The volume cannot have an active connection to an instance.\nTo disconnect the volume from a connected instance, see\n[Disconnecting From a Volume](/Content/Block/Tasks/disconnectingfromavolume.htm).\n**Warning:** All data on the volume will be permanently lost when the volume is deleted.\n

        :param str volume_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/volumes/{volumeId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "volume_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeId": volume_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_blockstorage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_volume_backup(self, volume_backup_id, **kwargs):
        """
        DeleteVolumeBackup
        Deletes a volume backup.

        :param str volume_backup_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume backup. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/volumeBackups/{volumeBackupId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "volume_backup_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeBackupId": volume_backup_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_blockstorage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def get_volume(self, volume_id, **kwargs):
        """
        GetVolume
        Gets information on the specified volume.

        :param str volume_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume. (required)
        :return: A Response object with data of type Volume
        """
        resource_path = "/volumes/{volumeId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "volume_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeId": volume_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_blockstorage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Volume")

    def get_volume_backup(self, volume_backup_id, **kwargs):
        """
        GetVolumeBackup
        Gets information for the specified volume backup.

        :param str volume_backup_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume backup. (required)
        :return: A Response object with data of type VolumeBackup
        """
        resource_path = "/volumeBackups/{volumeBackupId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "volume_backup_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeBackupId": volume_backup_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_blockstorage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="VolumeBackup")

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
        resource_path = "/volumeBackups"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "volume_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_volume_backups got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "volumeId": kwargs.get("volume_id", missing_param),
            "limit": kwargs.get("limit", missing_param),
            "page": kwargs.get("page", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_blockstorage_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[VolumeBackup]")

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
        resource_path = "/volumes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "availability_domain",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_volumes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing_param),
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing_param),
            "page": kwargs.get("page", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_blockstorage_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Volume]")

    def update_volume(self, volume_id, update_volume_details, **kwargs):
        """
        UpdateVolume
        Updates the specified volume's display name.

        :param str volume_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume. (required)
        :param UpdateVolumeDetails update_volume_details: Update volume's display name. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type Volume
        """
        resource_path = "/volumes/{volumeId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_params = [
            "volume_id",
            "update_volume_details",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "update_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeId": volume_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_blockstorage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_volume_details,
            response_type="Volume")

    def update_volume_backup(self, volume_backup_id, update_volume_backup_details, **kwargs):
        """
        UpdateVolumeBackup
        Updates the display name for the specified volume backup.

        :param str volume_backup_id: The Oracle Cloud ID (OCID) that uniquely identifies the volume backup. (required)
        :param UpdateVolumeBackupDetails update_volume_backup_details: Update volume backup fields (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type VolumeBackup
        """
        resource_path = "/volumeBackups/{volumeBackupId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_params = [
            "volume_backup_id",
            "update_volume_backup_details",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "update_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeBackupId": volume_backup_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_blockstorage_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_volume_backup_details,
            response_type="VolumeBackup")
