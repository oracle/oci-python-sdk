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


class BlockstorageClient(object):

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
        self.base_client = BaseClient("blockstorage", config, signer, core_type_mapping)

    def create_volume(self, create_volume_details, **kwargs):
        """
        CreateVolume
        Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from
        50 GB (51200 MB) to 16 TB (16777216 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB).
        For general information about block volumes, see
        `Overview of Block Volume Service`__.

        A volume and instance can be in separate compartments but must be in the same Availability Domain.
        For information about access control and compartments, see
        `Overview of the IAM Service`__. For information about
        Availability Domains, see `Regions and Availability Domains`__.
        To get a list of Availability Domains, use the `ListAvailabilityDomains` operation
        in the Identity and Access Management Service API.

        You may optionally specify a *display name* for the volume, which is simply a friendly name or
        description. It does not have to be unique, and you can change it. Avoid entering confidential information.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Block/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm


        :param CreateVolumeDetails create_volume_details: (required)
            Request to create a new volume.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Volume`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/volumes"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_volume got unknown kwargs: {!r}".format(extra_kwargs))

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
            body=create_volume_details,
            response_type="Volume")

    def create_volume_backup(self, create_volume_backup_details, **kwargs):
        """
        CreateVolumeBackup
        Creates a new backup of the specified volume. For general information about volume backups,
        see `Overview of Block Volume Service Backups`__

        When the request is received, the backup object is in a REQUEST_RECEIVED state.
        When the data is imaged, it goes into a CREATING state.
        After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Block/Concepts/blockvolumebackups.htm


        :param CreateVolumeBackupDetails create_volume_backup_details: (required)
            Request to create a new backup of given volume.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeBackup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/volumeBackups"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

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
            body=create_volume_backup_details,
            response_type="VolumeBackup")

    def delete_boot_volume(self, boot_volume_id, **kwargs):
        """
        DeleteBootVolume
        Deletes the specified boot volume. The volume cannot have an active connection to an instance.
        To disconnect the boot volume from a connected instance, see
        `Disconnecting From a Boot Volume`__.
        **Warning:** All data on the boot volume will be permanently lost when the boot volume is deleted.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Block/Tasks/deletingbootvolume.htm


        :param str boot_volume_id: (required)
            The OCID of the boot volume.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/bootVolumes/{bootVolumeId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_boot_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeId": boot_volume_id
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

    def delete_volume(self, volume_id, **kwargs):
        """
        DeleteVolume
        Deletes the specified volume. The volume cannot have an active connection to an instance.
        To disconnect the volume from a connected instance, see
        `Disconnecting From a Volume`__.
        **Warning:** All data on the volume will be permanently lost when the volume is deleted.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Block/Tasks/disconnectingfromavolume.htm


        :param str volume_id: (required)
            The OCID of the volume.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/volumes/{volumeId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeId": volume_id
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

    def delete_volume_backup(self, volume_backup_id, **kwargs):
        """
        DeleteVolumeBackup
        Deletes a volume backup.


        :param str volume_backup_id: (required)
            The OCID of the volume backup.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/volumeBackups/{volumeBackupId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeBackupId": volume_backup_id
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

    def get_boot_volume(self, boot_volume_id, **kwargs):
        """
        GetBootVolume
        Gets information for the specified boot volume.


        :param str boot_volume_id: (required)
            The OCID of the boot volume.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolume`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/bootVolumes/{bootVolumeId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_boot_volume got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "bootVolumeId": boot_volume_id
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
            response_type="BootVolume")

    def get_volume(self, volume_id, **kwargs):
        """
        GetVolume
        Gets information for the specified volume.


        :param str volume_id: (required)
            The OCID of the volume.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Volume`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/volumes/{volumeId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_volume got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "volumeId": volume_id
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
            response_type="Volume")

    def get_volume_backup(self, volume_backup_id, **kwargs):
        """
        GetVolumeBackup
        Gets information for the specified volume backup.


        :param str volume_backup_id: (required)
            The OCID of the volume backup.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeBackup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/volumeBackups/{volumeBackupId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_volume_backup got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "volumeBackupId": volume_backup_id
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
            response_type="VolumeBackup")

    def list_boot_volumes(self, availability_domain, compartment_id, **kwargs):
        """
        ListBootVolumes
        Lists the boot volumes in the specified compartment and Availability Domain.


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

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.BootVolume`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/bootVolumes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_boot_volumes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
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
            response_type="list[BootVolume]")

    def list_volume_backups(self, compartment_id, **kwargs):
        """
        ListVolumeBackups
        Lists the volume backups in the specified compartment. You can filter the results by volume.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str volume_id: (optional)
            The OCID of the volume.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

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

            Allowed values are: "CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.VolumeBackup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/volumeBackups"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "volume_id",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_volume_backups got unknown kwargs: {!r}".format(extra_kwargs))

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
            lifecycle_state_allowed_values = ["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "volumeId": kwargs.get("volume_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
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
            response_type="list[VolumeBackup]")

    def list_volumes(self, compartment_id, **kwargs):
        """
        ListVolumes
        Lists the volumes in the specified compartment and Availability Domain.


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

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

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

            Allowed values are: "PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.Volume`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/volumes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "availability_domain",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_volumes got unknown kwargs: {!r}".format(extra_kwargs))

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
            lifecycle_state_allowed_values = ["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
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
            response_type="list[Volume]")

    def update_boot_volume(self, boot_volume_id, update_boot_volume_details, **kwargs):
        """
        UpdateBootVolume
        Updates the specified boot volume's display name.


        :param str boot_volume_id: (required)
            The OCID of the boot volume.

        :param UpdateBootVolumeDetails update_boot_volume_details: (required)
            Update boot volume's display name.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolume`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/bootVolumes/{bootVolumeId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_boot_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeId": boot_volume_id
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
            body=update_boot_volume_details,
            response_type="BootVolume")

    def update_volume(self, volume_id, update_volume_details, **kwargs):
        """
        UpdateVolume
        Updates the specified volume's display name.
        Avoid entering confidential information.


        :param str volume_id: (required)
            The OCID of the volume.

        :param UpdateVolumeDetails update_volume_details: (required)
            Update volume's display name. Avoid entering confidential information.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Volume`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/volumes/{volumeId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeId": volume_id
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
            body=update_volume_details,
            response_type="Volume")

    def update_volume_backup(self, volume_backup_id, update_volume_backup_details, **kwargs):
        """
        UpdateVolumeBackup
        Updates the display name for the specified volume backup.
        Avoid entering confidential information.


        :param str volume_backup_id: (required)
            The OCID of the volume backup.

        :param UpdateVolumeBackupDetails update_volume_backup_details: (required)
            Update volume backup fields

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeBackup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/volumeBackups/{volumeBackupId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeBackupId": volume_backup_id
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
            body=update_volume_backup_details,
            response_type="VolumeBackup")
