# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180828


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaintenanceNotificationFailure(object):
    """
    Failed maintenance notification for a cluster
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MaintenanceNotificationFailure object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_ids:
            The value to assign to the cluster_ids property of this MaintenanceNotificationFailure.
        :type cluster_ids: list[str]

        :param tenant_id:
            The value to assign to the tenant_id property of this MaintenanceNotificationFailure.
        :type tenant_id: str

        :param error_code:
            The value to assign to the error_code property of this MaintenanceNotificationFailure.
        :type error_code: str

        :param error_description:
            The value to assign to the error_description property of this MaintenanceNotificationFailure.
        :type error_description: str

        """
        self.swagger_types = {
            'cluster_ids': 'list[str]',
            'tenant_id': 'str',
            'error_code': 'str',
            'error_description': 'str'
        }
        self.attribute_map = {
            'cluster_ids': 'clusterIds',
            'tenant_id': 'tenantId',
            'error_code': 'errorCode',
            'error_description': 'errorDescription'
        }
        self._cluster_ids = None
        self._tenant_id = None
        self._error_code = None
        self._error_description = None

    @property
    def cluster_ids(self):
        """
        **[Required]** Gets the cluster_ids of this MaintenanceNotificationFailure.
        IDs of clusters


        :return: The cluster_ids of this MaintenanceNotificationFailure.
        :rtype: list[str]
        """
        return self._cluster_ids

    @cluster_ids.setter
    def cluster_ids(self, cluster_ids):
        """
        Sets the cluster_ids of this MaintenanceNotificationFailure.
        IDs of clusters


        :param cluster_ids: The cluster_ids of this MaintenanceNotificationFailure.
        :type: list[str]
        """
        self._cluster_ids = cluster_ids

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this MaintenanceNotificationFailure.
        Tenant ID of the cluster


        :return: The tenant_id of this MaintenanceNotificationFailure.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this MaintenanceNotificationFailure.
        Tenant ID of the cluster


        :param tenant_id: The tenant_id of this MaintenanceNotificationFailure.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def error_code(self):
        """
        **[Required]** Gets the error_code of this MaintenanceNotificationFailure.
        Error Code


        :return: The error_code of this MaintenanceNotificationFailure.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this MaintenanceNotificationFailure.
        Error Code


        :param error_code: The error_code of this MaintenanceNotificationFailure.
        :type: str
        """
        self._error_code = error_code

    @property
    def error_description(self):
        """
        **[Required]** Gets the error_description of this MaintenanceNotificationFailure.
        Error Description


        :return: The error_description of this MaintenanceNotificationFailure.
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """
        Sets the error_description of this MaintenanceNotificationFailure.
        Error Description


        :param error_description: The error_description of this MaintenanceNotificationFailure.
        :type: str
        """
        self._error_description = error_description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
