# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_insight_summary import DatabaseInsightSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PeComanagedDatabaseInsightSummary(DatabaseInsightSummary):
    """
    Summary of a database insight resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PeComanagedDatabaseInsightSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.PeComanagedDatabaseInsightSummary.entity_source` attribute
        of this class is ``PE_COMANAGED_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PeComanagedDatabaseInsightSummary.
        :type id: str

        :param database_id:
            The value to assign to the database_id property of this PeComanagedDatabaseInsightSummary.
        :type database_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PeComanagedDatabaseInsightSummary.
        :type compartment_id: str

        :param database_name:
            The value to assign to the database_name property of this PeComanagedDatabaseInsightSummary.
        :type database_name: str

        :param database_display_name:
            The value to assign to the database_display_name property of this PeComanagedDatabaseInsightSummary.
        :type database_display_name: str

        :param database_type:
            The value to assign to the database_type property of this PeComanagedDatabaseInsightSummary.
        :type database_type: str

        :param database_version:
            The value to assign to the database_version property of this PeComanagedDatabaseInsightSummary.
        :type database_version: str

        :param database_host_names:
            The value to assign to the database_host_names property of this PeComanagedDatabaseInsightSummary.
        :type database_host_names: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PeComanagedDatabaseInsightSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this PeComanagedDatabaseInsightSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this PeComanagedDatabaseInsightSummary.
        :type system_tags: dict(str, dict(str, object))

        :param entity_source:
            The value to assign to the entity_source property of this PeComanagedDatabaseInsightSummary.
            Allowed values for this property are: "AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"
        :type entity_source: str

        :param processor_count:
            The value to assign to the processor_count property of this PeComanagedDatabaseInsightSummary.
        :type processor_count: int

        :param status:
            The value to assign to the status property of this PeComanagedDatabaseInsightSummary.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED"
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this PeComanagedDatabaseInsightSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this PeComanagedDatabaseInsightSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PeComanagedDatabaseInsightSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this PeComanagedDatabaseInsightSummary.
        :type lifecycle_details: str

        :param database_connection_status_details:
            The value to assign to the database_connection_status_details property of this PeComanagedDatabaseInsightSummary.
        :type database_connection_status_details: str

        :param database_resource_type:
            The value to assign to the database_resource_type property of this PeComanagedDatabaseInsightSummary.
        :type database_resource_type: str

        :param opsi_private_endpoint_id:
            The value to assign to the opsi_private_endpoint_id property of this PeComanagedDatabaseInsightSummary.
        :type opsi_private_endpoint_id: str

        :param parent_id:
            The value to assign to the parent_id property of this PeComanagedDatabaseInsightSummary.
        :type parent_id: str

        :param root_id:
            The value to assign to the root_id property of this PeComanagedDatabaseInsightSummary.
        :type root_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'database_id': 'str',
            'compartment_id': 'str',
            'database_name': 'str',
            'database_display_name': 'str',
            'database_type': 'str',
            'database_version': 'str',
            'database_host_names': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'entity_source': 'str',
            'processor_count': 'int',
            'status': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'database_connection_status_details': 'str',
            'database_resource_type': 'str',
            'opsi_private_endpoint_id': 'str',
            'parent_id': 'str',
            'root_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'database_id': 'databaseId',
            'compartment_id': 'compartmentId',
            'database_name': 'databaseName',
            'database_display_name': 'databaseDisplayName',
            'database_type': 'databaseType',
            'database_version': 'databaseVersion',
            'database_host_names': 'databaseHostNames',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'entity_source': 'entitySource',
            'processor_count': 'processorCount',
            'status': 'status',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'database_connection_status_details': 'databaseConnectionStatusDetails',
            'database_resource_type': 'databaseResourceType',
            'opsi_private_endpoint_id': 'opsiPrivateEndpointId',
            'parent_id': 'parentId',
            'root_id': 'rootId'
        }

        self._id = None
        self._database_id = None
        self._compartment_id = None
        self._database_name = None
        self._database_display_name = None
        self._database_type = None
        self._database_version = None
        self._database_host_names = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._entity_source = None
        self._processor_count = None
        self._status = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._database_connection_status_details = None
        self._database_resource_type = None
        self._opsi_private_endpoint_id = None
        self._parent_id = None
        self._root_id = None
        self._entity_source = 'PE_COMANAGED_DATABASE'

    @property
    def database_resource_type(self):
        """
        Gets the database_resource_type of this PeComanagedDatabaseInsightSummary.
        OCI database resource type


        :return: The database_resource_type of this PeComanagedDatabaseInsightSummary.
        :rtype: str
        """
        return self._database_resource_type

    @database_resource_type.setter
    def database_resource_type(self, database_resource_type):
        """
        Sets the database_resource_type of this PeComanagedDatabaseInsightSummary.
        OCI database resource type


        :param database_resource_type: The database_resource_type of this PeComanagedDatabaseInsightSummary.
        :type: str
        """
        self._database_resource_type = database_resource_type

    @property
    def opsi_private_endpoint_id(self):
        """
        Gets the opsi_private_endpoint_id of this PeComanagedDatabaseInsightSummary.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The opsi_private_endpoint_id of this PeComanagedDatabaseInsightSummary.
        :rtype: str
        """
        return self._opsi_private_endpoint_id

    @opsi_private_endpoint_id.setter
    def opsi_private_endpoint_id(self, opsi_private_endpoint_id):
        """
        Sets the opsi_private_endpoint_id of this PeComanagedDatabaseInsightSummary.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param opsi_private_endpoint_id: The opsi_private_endpoint_id of this PeComanagedDatabaseInsightSummary.
        :type: str
        """
        self._opsi_private_endpoint_id = opsi_private_endpoint_id

    @property
    def parent_id(self):
        """
        Gets the parent_id of this PeComanagedDatabaseInsightSummary.
        The `OCID`__ of the VM Cluster or DB System ID, depending on which configuration the resource belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The parent_id of this PeComanagedDatabaseInsightSummary.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this PeComanagedDatabaseInsightSummary.
        The `OCID`__ of the VM Cluster or DB System ID, depending on which configuration the resource belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param parent_id: The parent_id of this PeComanagedDatabaseInsightSummary.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def root_id(self):
        """
        Gets the root_id of this PeComanagedDatabaseInsightSummary.
        The `OCID`__ of the root resource for a composite target. e.g. for ExaCS members the rootId will be the OCID of the Exadata Infrastructure resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The root_id of this PeComanagedDatabaseInsightSummary.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        """
        Sets the root_id of this PeComanagedDatabaseInsightSummary.
        The `OCID`__ of the root resource for a composite target. e.g. for ExaCS members the rootId will be the OCID of the Exadata Infrastructure resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param root_id: The root_id of this PeComanagedDatabaseInsightSummary.
        :type: str
        """
        self._root_id = root_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
