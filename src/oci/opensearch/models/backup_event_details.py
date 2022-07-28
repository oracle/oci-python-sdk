# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupEventDetails(object):
    """
    Details about a cluster backup event.
    """

    #: A constant which can be used with the backup_state property of a BackupEventDetails.
    #: This constant has a value of "DELETED"
    BACKUP_STATE_DELETED = "DELETED"

    #: A constant which can be used with the backup_state property of a BackupEventDetails.
    #: This constant has a value of "SUCCESS"
    BACKUP_STATE_SUCCESS = "SUCCESS"

    #: A constant which can be used with the backup_state property of a BackupEventDetails.
    #: This constant has a value of "FAILED"
    BACKUP_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new BackupEventDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_id:
            The value to assign to the cluster_id property of this BackupEventDetails.
        :type cluster_id: str

        :param backup_state:
            The value to assign to the backup_state property of this BackupEventDetails.
            Allowed values for this property are: "DELETED", "SUCCESS", "FAILED"
        :type backup_state: str

        :param snapshot_name:
            The value to assign to the snapshot_name property of this BackupEventDetails.
        :type snapshot_name: str

        :param time_started:
            The value to assign to the time_started property of this BackupEventDetails.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this BackupEventDetails.
        :type time_ended: datetime

        :param backup_size:
            The value to assign to the backup_size property of this BackupEventDetails.
        :type backup_size: float

        """
        self.swagger_types = {
            'cluster_id': 'str',
            'backup_state': 'str',
            'snapshot_name': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'backup_size': 'float'
        }

        self.attribute_map = {
            'cluster_id': 'clusterId',
            'backup_state': 'backupState',
            'snapshot_name': 'snapshotName',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'backup_size': 'backupSize'
        }

        self._cluster_id = None
        self._backup_state = None
        self._snapshot_name = None
        self._time_started = None
        self._time_ended = None
        self._backup_size = None

    @property
    def cluster_id(self):
        """
        **[Required]** Gets the cluster_id of this BackupEventDetails.
        The OCID of the OpenSearch cluster for the cluster backup.


        :return: The cluster_id of this BackupEventDetails.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this BackupEventDetails.
        The OCID of the OpenSearch cluster for the cluster backup.


        :param cluster_id: The cluster_id of this BackupEventDetails.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def backup_state(self):
        """
        **[Required]** Gets the backup_state of this BackupEventDetails.
        The result of the cluster backup operation.

        Allowed values for this property are: "DELETED", "SUCCESS", "FAILED"


        :return: The backup_state of this BackupEventDetails.
        :rtype: str
        """
        return self._backup_state

    @backup_state.setter
    def backup_state(self, backup_state):
        """
        Sets the backup_state of this BackupEventDetails.
        The result of the cluster backup operation.


        :param backup_state: The backup_state of this BackupEventDetails.
        :type: str
        """
        allowed_values = ["DELETED", "SUCCESS", "FAILED"]
        if not value_allowed_none_or_none_sentinel(backup_state, allowed_values):
            raise ValueError(
                "Invalid value for `backup_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._backup_state = backup_state

    @property
    def snapshot_name(self):
        """
        Gets the snapshot_name of this BackupEventDetails.
        The name of the cluster backup.


        :return: The snapshot_name of this BackupEventDetails.
        :rtype: str
        """
        return self._snapshot_name

    @snapshot_name.setter
    def snapshot_name(self, snapshot_name):
        """
        Sets the snapshot_name of this BackupEventDetails.
        The name of the cluster backup.


        :param snapshot_name: The snapshot_name of this BackupEventDetails.
        :type: str
        """
        self._snapshot_name = snapshot_name

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this BackupEventDetails.
        The date and time the cluster backup event started. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_started of this BackupEventDetails.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this BackupEventDetails.
        The date and time the cluster backup event started. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_started: The time_started of this BackupEventDetails.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        **[Required]** Gets the time_ended of this BackupEventDetails.
        The date and time the cluster backup event started. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_ended of this BackupEventDetails.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this BackupEventDetails.
        The date and time the cluster backup event started. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_ended: The time_ended of this BackupEventDetails.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def backup_size(self):
        """
        Gets the backup_size of this BackupEventDetails.
        The cluster backup size in GB.


        :return: The backup_size of this BackupEventDetails.
        :rtype: float
        """
        return self._backup_size

    @backup_size.setter
    def backup_size(self, backup_size):
        """
        Sets the backup_size of this BackupEventDetails.
        The cluster backup size in GB.


        :param backup_size: The backup_size of this BackupEventDetails.
        :type: float
        """
        self._backup_size = backup_size

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
