# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InfrastructureTargetVersionSummary(object):
    """
    The target Exadata Infrastructure system software version for an infrastructure resource. Applies to Exadata Cloud@Customer and Exadata Cloud instances only.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access,
    see `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the target_resource_type property of a InfrastructureTargetVersionSummary.
    #: This constant has a value of "EXADATA_DB_SYSTEM"
    TARGET_RESOURCE_TYPE_EXADATA_DB_SYSTEM = "EXADATA_DB_SYSTEM"

    #: A constant which can be used with the target_resource_type property of a InfrastructureTargetVersionSummary.
    #: This constant has a value of "CLOUD_EXADATA_INFRASTRUCTURE"
    TARGET_RESOURCE_TYPE_CLOUD_EXADATA_INFRASTRUCTURE = "CLOUD_EXADATA_INFRASTRUCTURE"

    #: A constant which can be used with the target_resource_type property of a InfrastructureTargetVersionSummary.
    #: This constant has a value of "EXACC_INFRASTRUCTURE"
    TARGET_RESOURCE_TYPE_EXACC_INFRASTRUCTURE = "EXACC_INFRASTRUCTURE"

    def __init__(self, **kwargs):
        """
        Initializes a new InfrastructureTargetVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_db_version_history_entry:
            The value to assign to the target_db_version_history_entry property of this InfrastructureTargetVersionSummary.
        :type target_db_version_history_entry: list[str]

        :param target_storage_version_history_entry:
            The value to assign to the target_storage_version_history_entry property of this InfrastructureTargetVersionSummary.
        :type target_storage_version_history_entry: list[str]

        :param target_resource_type:
            The value to assign to the target_resource_type property of this InfrastructureTargetVersionSummary.
            Allowed values for this property are: "EXADATA_DB_SYSTEM", "CLOUD_EXADATA_INFRASTRUCTURE", "EXACC_INFRASTRUCTURE"
        :type target_resource_type: str

        :param target_resource_id:
            The value to assign to the target_resource_id property of this InfrastructureTargetVersionSummary.
        :type target_resource_id: str

        """
        self.swagger_types = {
            'target_db_version_history_entry': 'list[str]',
            'target_storage_version_history_entry': 'list[str]',
            'target_resource_type': 'str',
            'target_resource_id': 'str'
        }

        self.attribute_map = {
            'target_db_version_history_entry': 'targetDbVersionHistoryEntry',
            'target_storage_version_history_entry': 'targetStorageVersionHistoryEntry',
            'target_resource_type': 'targetResourceType',
            'target_resource_id': 'targetResourceId'
        }

        self._target_db_version_history_entry = None
        self._target_storage_version_history_entry = None
        self._target_resource_type = None
        self._target_resource_id = None

    @property
    def target_db_version_history_entry(self):
        """
        **[Required]** Gets the target_db_version_history_entry of this InfrastructureTargetVersionSummary.
        The history entry of the target system software version for the database server patching operation.


        :return: The target_db_version_history_entry of this InfrastructureTargetVersionSummary.
        :rtype: list[str]
        """
        return self._target_db_version_history_entry

    @target_db_version_history_entry.setter
    def target_db_version_history_entry(self, target_db_version_history_entry):
        """
        Sets the target_db_version_history_entry of this InfrastructureTargetVersionSummary.
        The history entry of the target system software version for the database server patching operation.


        :param target_db_version_history_entry: The target_db_version_history_entry of this InfrastructureTargetVersionSummary.
        :type: list[str]
        """
        self._target_db_version_history_entry = target_db_version_history_entry

    @property
    def target_storage_version_history_entry(self):
        """
        **[Required]** Gets the target_storage_version_history_entry of this InfrastructureTargetVersionSummary.
        The history entry of the target storage cell system software version for the storage cell patching operation.


        :return: The target_storage_version_history_entry of this InfrastructureTargetVersionSummary.
        :rtype: list[str]
        """
        return self._target_storage_version_history_entry

    @target_storage_version_history_entry.setter
    def target_storage_version_history_entry(self, target_storage_version_history_entry):
        """
        Sets the target_storage_version_history_entry of this InfrastructureTargetVersionSummary.
        The history entry of the target storage cell system software version for the storage cell patching operation.


        :param target_storage_version_history_entry: The target_storage_version_history_entry of this InfrastructureTargetVersionSummary.
        :type: list[str]
        """
        self._target_storage_version_history_entry = target_storage_version_history_entry

    @property
    def target_resource_type(self):
        """
        Gets the target_resource_type of this InfrastructureTargetVersionSummary.
        The resource type of the target Exadata infrastructure resource that will receive the system software update.

        Allowed values for this property are: "EXADATA_DB_SYSTEM", "CLOUD_EXADATA_INFRASTRUCTURE", "EXACC_INFRASTRUCTURE"


        :return: The target_resource_type of this InfrastructureTargetVersionSummary.
        :rtype: str
        """
        return self._target_resource_type

    @target_resource_type.setter
    def target_resource_type(self, target_resource_type):
        """
        Sets the target_resource_type of this InfrastructureTargetVersionSummary.
        The resource type of the target Exadata infrastructure resource that will receive the system software update.


        :param target_resource_type: The target_resource_type of this InfrastructureTargetVersionSummary.
        :type: str
        """
        allowed_values = ["EXADATA_DB_SYSTEM", "CLOUD_EXADATA_INFRASTRUCTURE", "EXACC_INFRASTRUCTURE"]
        if not value_allowed_none_or_none_sentinel(target_resource_type, allowed_values):
            raise ValueError(
                "Invalid value for `target_resource_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._target_resource_type = target_resource_type

    @property
    def target_resource_id(self):
        """
        Gets the target_resource_id of this InfrastructureTargetVersionSummary.
        The OCID of the target Exadata Infrastructure resource that will receive the maintenance update.


        :return: The target_resource_id of this InfrastructureTargetVersionSummary.
        :rtype: str
        """
        return self._target_resource_id

    @target_resource_id.setter
    def target_resource_id(self, target_resource_id):
        """
        Sets the target_resource_id of this InfrastructureTargetVersionSummary.
        The OCID of the target Exadata Infrastructure resource that will receive the maintenance update.


        :param target_resource_id: The target_resource_id of this InfrastructureTargetVersionSummary.
        :type: str
        """
        self._target_resource_id = target_resource_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
