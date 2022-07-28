# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RestoreOpensearchClusterDetails(object):
    """
    Information about the OpenSearch cluster backup to restore.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RestoreOpensearchClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param opensearch_cluster_backup_id:
            The value to assign to the opensearch_cluster_backup_id property of this RestoreOpensearchClusterDetails.
        :type opensearch_cluster_backup_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RestoreOpensearchClusterDetails.
        :type compartment_id: str

        :param prefix:
            The value to assign to the prefix property of this RestoreOpensearchClusterDetails.
        :type prefix: str

        """
        self.swagger_types = {
            'opensearch_cluster_backup_id': 'str',
            'compartment_id': 'str',
            'prefix': 'str'
        }

        self.attribute_map = {
            'opensearch_cluster_backup_id': 'opensearchClusterBackupId',
            'compartment_id': 'compartmentId',
            'prefix': 'prefix'
        }

        self._opensearch_cluster_backup_id = None
        self._compartment_id = None
        self._prefix = None

    @property
    def opensearch_cluster_backup_id(self):
        """
        **[Required]** Gets the opensearch_cluster_backup_id of this RestoreOpensearchClusterDetails.
        The OCID of the cluster backup to restore.


        :return: The opensearch_cluster_backup_id of this RestoreOpensearchClusterDetails.
        :rtype: str
        """
        return self._opensearch_cluster_backup_id

    @opensearch_cluster_backup_id.setter
    def opensearch_cluster_backup_id(self, opensearch_cluster_backup_id):
        """
        Sets the opensearch_cluster_backup_id of this RestoreOpensearchClusterDetails.
        The OCID of the cluster backup to restore.


        :param opensearch_cluster_backup_id: The opensearch_cluster_backup_id of this RestoreOpensearchClusterDetails.
        :type: str
        """
        self._opensearch_cluster_backup_id = opensearch_cluster_backup_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RestoreOpensearchClusterDetails.
        The OCID of the compartment where the cluster backup is located.


        :return: The compartment_id of this RestoreOpensearchClusterDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RestoreOpensearchClusterDetails.
        The OCID of the compartment where the cluster backup is located.


        :param compartment_id: The compartment_id of this RestoreOpensearchClusterDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def prefix(self):
        """
        Gets the prefix of this RestoreOpensearchClusterDetails.
        The prefix for the indices in the cluster backup.


        :return: The prefix of this RestoreOpensearchClusterDetails.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this RestoreOpensearchClusterDetails.
        The prefix for the indices in the cluster backup.


        :param prefix: The prefix of this RestoreOpensearchClusterDetails.
        :type: str
        """
        self._prefix = prefix

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
