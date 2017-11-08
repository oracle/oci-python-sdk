# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

import six

from ..base_client import BaseClient
from ..config import get_config_value_or_default, validate_config
from ..signer import Signer
from ..util import Sentinel
from .models import database_type_mapping
missing = Sentinel("Missing")


class DatabaseClient(object):

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
        self.base_client = BaseClient("database", config, signer, database_type_mapping)

    def create_backup(self, create_backup_details, **kwargs):
        """
        CreateBackup
        Creates a new backup in the specified database based on the request parameters you provide. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.


        :param CreateBackupDetails create_backup_details: (required)
            Request to create a new database backup.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Backup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backups"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_backup got unknown kwargs: {!r}".format(extra_kwargs))

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
            body=create_backup_details,
            response_type="Backup")

    def create_data_guard_association(self, database_id, create_data_guard_association_details, **kwargs):
        """
        Creates a Data Guard association.
        Creates a new Data Guard association.  A Data Guard association represents the replication relationship between the
        specified database and a peer database. For more information, see `Using Oracle Data Guard`__.

        All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID
        called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response.
        You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the
        resource in the Console. Fore more information, see
        `Resource Identifiers`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Database/Tasks/usingdataguard.htm
        __ http://localhost:8000/Content/General/Concepts/identifiers.htm


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param CreateDataGuardAssociationDetails create_data_guard_association_details: (required)
            A request to create a Data Guard association.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DataGuardAssociation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/dataGuardAssociations"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_data_guard_association got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=create_data_guard_association_details,
            response_type="DataGuardAssociation")

    def create_db_home(self, create_db_home_with_db_system_id_details, **kwargs):
        """
        CreateDbHome
        Creates a new DB Home in the specified DB System based on the request parameters you provide.


        :param CreateDbHomeWithDbSystemIdBase create_db_home_with_db_system_id_details: (required)
            Request to create a new DB Home.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbHome`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_db_home got unknown kwargs: {!r}".format(extra_kwargs))

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
            body=create_db_home_with_db_system_id_details,
            response_type="DbHome")

    def db_node_action(self, db_node_id, action, **kwargs):
        """
        DbNodeAction
        Performs an action, such as one of the power actions (start, stop, softreset, or reset), on the specified DB Node.

        **start** - power on

        **stop** - power off

        **softreset** - ACPI shutdown and power on

        **reset** - power off and power on

        Note that the **stop** state has no effect on the resources you consume.
        Billing continues for DB Nodes that you stop, and related resources continue
        to apply against any relevant quotas. You must terminate the DB System
        (:func:`terminate_db_system`)
        to remove its resources from billing and quotas.


        :param str db_node_id: (required)
            The database node `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str action: (required)
            The action to perform on the DB Node.

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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbNode`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbNodes/{dbNodeId}"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "db_node_action got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbNodeId": db_node_id
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
            response_type="DbNode")

    def delete_backup(self, backup_id, **kwargs):
        """
        DeleteBackup
        Deletes a full backup. You cannot delete automatic backups using this API.


        :param str backup_id: (required)
            The backup OCID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backups/{backupId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "backupId": backup_id
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

    def delete_db_home(self, db_home_id, **kwargs):
        """
        DeleteDbHome
        Deletes a DB Home. The DB Home and its database data are local to the DB System and will be lost when it is deleted. Oracle recommends that you back up any data in the DB System prior to deleting it.


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param bool perform_final_backup: (optional)
            Whether to perform a final backup of the database or not. Default is false. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match",
            "perform_final_backup"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_db_home got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbHomeId": db_home_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "performFinalBackup": kwargs.get("perform_final_backup", missing)
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

    def failover_data_guard_association(self, database_id, data_guard_association_id, failover_data_guard_association_details, **kwargs):
        """
        Performs a failover to transition a standby database into the primary database role.
        Performs a failover to transition the standby database identified by the `databaseId` parameter into the
        specified Data Guard association's primary role after the existing primary database fails or becomes unreachable.

        A failover might result in data loss depending on the protection mode in effect at the time of the primary
        database failure.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param FailoverDataGuardAssociationDetails failover_data_guard_association_details: (required)
            A request to perform a failover, transitioning a standby database into a primary database.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DataGuardAssociation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/dataGuardAssociations/{dataGuardAssociationId}/actions/failover"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "failover_data_guard_association got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id,
            "dataGuardAssociationId": data_guard_association_id
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
            body=failover_data_guard_association_details,
            response_type="DataGuardAssociation")

    def get_backup(self, backup_id, **kwargs):
        """
        GetBackup
        Gets information about the specified backup.


        :param str backup_id: (required)
            The backup OCID.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Backup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backups/{backupId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_backup got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "backupId": backup_id
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
            response_type="Backup")

    def get_data_guard_association(self, database_id, data_guard_association_id, **kwargs):
        """
        Gets configuration information for the specified database and Data Guard association.
        Gets the specified Data Guard association's configuration information.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DataGuardAssociation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/dataGuardAssociations/{dataGuardAssociationId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_data_guard_association got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "databaseId": database_id,
            "dataGuardAssociationId": data_guard_association_id
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
            response_type="DataGuardAssociation")

    def get_database(self, database_id, **kwargs):
        """
        GetDatabase
        Gets information about a specific database.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Database`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_database got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "databaseId": database_id
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
            response_type="Database")

    def get_db_home(self, db_home_id, **kwargs):
        """
        GetDbHome
        Gets information about the specified database home.


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbHome`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_db_home got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "dbHomeId": db_home_id
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
            response_type="DbHome")

    def get_db_home_patch(self, db_home_id, patch_id, **kwargs):
        """
        GetDbHomePatch
        Gets information about a specified patch package.


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str patch_id: (required)
            The OCID of the patch.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Patch`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}/patches/{patchId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_db_home_patch got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "dbHomeId": db_home_id,
            "patchId": patch_id
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
            response_type="Patch")

    def get_db_home_patch_history_entry(self, db_home_id, patch_history_entry_id, **kwargs):
        """
        GetDbHomePatchHistoryEntry
        Gets the patch history details for the specified patchHistoryEntryId


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str patch_history_entry_id: (required)
            The OCID of the patch history entry.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.PatchHistoryEntry`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}/patchHistoryEntries/{patchHistoryEntryId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_db_home_patch_history_entry got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "dbHomeId": db_home_id,
            "patchHistoryEntryId": patch_history_entry_id
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
            response_type="PatchHistoryEntry")

    def get_db_node(self, db_node_id, **kwargs):
        """
        GetDbNode
        Gets information about the specified database node.


        :param str db_node_id: (required)
            The database node `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbNode`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbNodes/{dbNodeId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_db_node got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "dbNodeId": db_node_id
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
            response_type="DbNode")

    def get_db_system(self, db_system_id, **kwargs):
        """
        GetDbSystem
        Gets information about the specified DB System.


        :param str db_system_id: (required)
            The DB System `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbSystem`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_db_system got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "dbSystemId": db_system_id
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
            response_type="DbSystem")

    def get_db_system_patch(self, db_system_id, patch_id, **kwargs):
        """
        GetDbSystemPatch
        Gets information about a specified patch package.


        :param str db_system_id: (required)
            The DB System `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str patch_id: (required)
            The OCID of the patch.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Patch`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}/patches/{patchId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_db_system_patch got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "dbSystemId": db_system_id,
            "patchId": patch_id
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
            response_type="Patch")

    def get_db_system_patch_history_entry(self, db_system_id, patch_history_entry_id, **kwargs):
        """
        GetDbSystemPatchHistoryEntry
        Gets the patch history details for the specified patchHistoryEntryId.


        :param str db_system_id: (required)
            The DB System `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str patch_history_entry_id: (required)
            The OCID of the patch history entry.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.PatchHistoryEntry`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}/patchHistoryEntries/{patchHistoryEntryId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_db_system_patch_history_entry got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "dbSystemId": db_system_id,
            "patchHistoryEntryId": patch_history_entry_id
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
            response_type="PatchHistoryEntry")

    def launch_db_system(self, launch_db_system_details, **kwargs):
        """
        LaunchDbSystem
        Launches a new DB System in the specified compartment and Availability Domain. You'll specify a single Oracle
        Database Edition that applies to all the databases on that DB System. The selected edition cannot be changed.

        An initial database is created on the DB System based on the request parameters you provide and some default
        options. For more information,
        see `Default Options for the Initial Database`__.

        The DB System will include a command line interface (CLI) that you can use to create additional databases and
        manage existing databases. For more information, see the
        `Oracle Database CLI Reference`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Database/Tasks/launchingDB.htm#Default_Options_for_the_Initial_Database
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Database/References/odacli.htm#Oracle_Database_CLI_Reference


        :param LaunchDbSystemDetails launch_db_system_details: (required)
            Request to launch a DB System.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbSystem`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "launch_db_system got unknown kwargs: {!r}".format(extra_kwargs))

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
            body=launch_db_system_details,
            response_type="DbSystem")

    def list_backups(self, **kwargs):
        """
        ListBackups
        Gets a list of backups based on the databaseId or compartmentId specified. Either one of the query parameters must be provided.


        :param str database_id: (optional)
            The OCID of the database.

        :param str compartment_id: (optional)
            The compartment OCID.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The pagination token to continue listing from.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.BackupSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backups"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "database_id",
            "compartment_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_backups got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "databaseId": kwargs.get("database_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing),
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
            response_type="list[BackupSummary]")

    def list_data_guard_associations(self, database_id, **kwargs):
        """
        Lists all Data Guard associations for the specified database.
        Lists all Data Guard associations for the specified database.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The pagination token to continue listing from.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DataGuardAssociationSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/dataGuardAssociations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_data_guard_associations got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id
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
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            response_type="list[DataGuardAssociationSummary]")

    def list_databases(self, compartment_id, db_home_id, **kwargs):
        """
        ListDatabases
        Gets a list of the databases in the specified database home.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str db_home_id: (required)
            A database home `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The pagination token to continue listing from.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DatabaseSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_databases got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "dbHomeId": db_home_id,
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
            response_type="list[DatabaseSummary]")

    def list_db_home_patch_history_entries(self, db_home_id, **kwargs):
        """
        ListDbHomePatchHistoryEntries
        Gets history of the actions taken for patches for the specified database home.


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The pagination token to continue listing from.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.PatchHistoryEntrySummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}/patchHistoryEntries"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_home_patch_history_entries got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbHomeId": db_home_id
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
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            response_type="list[PatchHistoryEntrySummary]")

    def list_db_home_patches(self, db_home_id, **kwargs):
        """
        ListDbHomePatches
        Lists patches applicable to the requested database home.


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The pagination token to continue listing from.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.PatchSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}/patches"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_home_patches got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbHomeId": db_home_id
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
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            response_type="list[PatchSummary]")

    def list_db_homes(self, compartment_id, db_system_id, **kwargs):
        """
        ListDbHomes
        Gets a list of database homes in the specified DB System and compartment. A database home is a directory where Oracle database software is installed.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str db_system_id: (required)
            The `OCID`__ of the DB System.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The pagination token to continue listing from.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DbHomeSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_homes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "dbSystemId": db_system_id,
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
            response_type="list[DbHomeSummary]")

    def list_db_nodes(self, compartment_id, db_system_id, **kwargs):
        """
        ListDbNodes
        Gets a list of database nodes in the specified DB System and compartment. A database node is a server running database software.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str db_system_id: (required)
            The `OCID`__ of the DB System.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The pagination token to continue listing from.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DbNodeSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbNodes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_nodes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "dbSystemId": db_system_id,
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
            response_type="list[DbNodeSummary]")

    def list_db_system_patch_history_entries(self, db_system_id, **kwargs):
        """
        ListDbSystemPatchHistoryEntries
        Gets the history of the patch actions performed on the specified DB System.


        :param str db_system_id: (required)
            The DB System `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The pagination token to continue listing from.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.PatchHistoryEntrySummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}/patchHistoryEntries"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_system_patch_history_entries got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id
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
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            response_type="list[PatchHistoryEntrySummary]")

    def list_db_system_patches(self, db_system_id, **kwargs):
        """
        ListDbSystemPatches
        Lists the patches applicable to the requested DB System.


        :param str db_system_id: (required)
            The DB System `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The pagination token to continue listing from.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.PatchSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}/patches"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_system_patches got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id
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
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            response_type="list[PatchSummary]")

    def list_db_system_shapes(self, availability_domain, compartment_id, **kwargs):
        """
        ListDbSystemShapes
        Gets a list of the shapes that can be used to launch a new DB System. The shape determines resources to allocate to the DB system - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes.


        :param str availability_domain: (required)
            The name of the Availability Domain.

        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The pagination token to continue listing from.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DbSystemShapeSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystemShapes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_system_shapes got unknown kwargs: {!r}".format(extra_kwargs))

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
            response_type="list[DbSystemShapeSummary]")

    def list_db_systems(self, compartment_id, **kwargs):
        """
        ListDbSystems
        Gets a list of the DB Systems in the specified compartment.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The pagination token to continue listing from.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DbSystemSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_systems got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
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
            response_type="list[DbSystemSummary]")

    def list_db_versions(self, compartment_id, **kwargs):
        """
        ListDbVersions
        Gets a list of supported Oracle database versions.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str db_system_shape: (optional)
            If provided, filters the results to the set of database versions which are supported for the given shape.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DbVersionSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbVersions"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page",
            "db_system_shape"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_versions got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "dbSystemShape": kwargs.get("db_system_shape", missing)
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
            response_type="list[DbVersionSummary]")

    def reinstate_data_guard_association(self, database_id, data_guard_association_id, reinstate_data_guard_association_details, **kwargs):
        """
        Reinstates a database to a Data Guard association standby role.
        Reinstates the database identified by the `databaseId` parameter into the standby role in a Data Guard association.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param ReinstateDataGuardAssociationDetails reinstate_data_guard_association_details: (required)
            A request to reinstate a database in a standby role.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DataGuardAssociation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/dataGuardAssociations/{dataGuardAssociationId}/actions/reinstate"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "reinstate_data_guard_association got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id,
            "dataGuardAssociationId": data_guard_association_id
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
            body=reinstate_data_guard_association_details,
            response_type="DataGuardAssociation")

    def restore_database(self, database_id, restore_database_details, **kwargs):
        """
        RestoreDatabase
        Restore a Database based on the request parameters you provide.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param RestoreDatabaseDetails restore_database_details: (required)
            Request to perform database restore.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Database`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/actions/restore"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "restore_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id
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
            body=restore_database_details,
            response_type="Database")

    def switchover_data_guard_association(self, database_id, data_guard_association_id, switchover_data_guard_association_details, **kwargs):
        """
        Performs a switchover to transition the primary database of a Data Guard association into a standby role.
        Performs a switchover to transition the primary database of a Data Guard association into a standby role. The
        standby database associated with the `dataGuardAssociationId` assumes the primary database role.

        A switchover guarantees no data loss.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param SwitchoverDataGuardAssociationDetails switchover_data_guard_association_details: (required)
            Request to swtichover a primary to a standby.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DataGuardAssociation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/dataGuardAssociations/{dataGuardAssociationId}/actions/switchover"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "switchover_data_guard_association got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id,
            "dataGuardAssociationId": data_guard_association_id
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
            body=switchover_data_guard_association_details,
            response_type="DataGuardAssociation")

    def terminate_db_system(self, db_system_id, **kwargs):
        """
        TerminateDbSystem
        Terminates a DB System and permanently deletes it and any databases running on it, and any storage volumes attached to it. The database data is local to the DB System and will be lost when the system is terminated. Oracle recommends that you back up any data in the DB System prior to terminating it.


        :param str db_system_id: (required)
            The DB System `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "terminate_db_system got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id
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

    def update_database(self, database_id, update_database_details, **kwargs):
        """
        UpdateDatabase
        Update a Database based on the request parameters you provide.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param UpdateDatabaseDetails update_database_details: (required)
            Request to perform database update.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Database`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id
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
            body=update_database_details,
            response_type="Database")

    def update_db_home(self, db_home_id, update_db_home_details, **kwargs):
        """
        UpdateDbHome
        Patches the specified dbHome.


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param UpdateDbHomeDetails update_db_home_details: (required)
            Request to update the properties of a DB Home.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbHome`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_db_home got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbHomeId": db_home_id
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
            body=update_db_home_details,
            response_type="DbHome")

    def update_db_system(self, db_system_id, update_db_system_details, **kwargs):
        """
        UpdateDbSystem
        Updates the properties of a DB System, such as the CPU core count.


        :param str db_system_id: (required)
            The DB System `OCID`__.

            __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm

        :param UpdateDbSystemDetails update_db_system_details: (required)
            Request to update the properties of a DB System.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbSystem`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_db_system got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id
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
            body=update_db_system_details,
            response_type="DbSystem")
