# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_insight import HostInsight
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmManagedExternalHostInsight(HostInsight):
    """
    EM-managed external host insight resource.
    """

    #: A constant which can be used with the platform_type property of a EmManagedExternalHostInsight.
    #: This constant has a value of "LINUX"
    PLATFORM_TYPE_LINUX = "LINUX"

    #: A constant which can be used with the platform_type property of a EmManagedExternalHostInsight.
    #: This constant has a value of "SOLARIS"
    PLATFORM_TYPE_SOLARIS = "SOLARIS"

    #: A constant which can be used with the platform_type property of a EmManagedExternalHostInsight.
    #: This constant has a value of "SUNOS"
    PLATFORM_TYPE_SUNOS = "SUNOS"

    #: A constant which can be used with the platform_type property of a EmManagedExternalHostInsight.
    #: This constant has a value of "ZLINUX"
    PLATFORM_TYPE_ZLINUX = "ZLINUX"

    def __init__(self, **kwargs):
        """
        Initializes a new EmManagedExternalHostInsight object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.EmManagedExternalHostInsight.entity_source` attribute
        of this class is ``EM_MANAGED_EXTERNAL_HOST`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this EmManagedExternalHostInsight.
            Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_source: str

        :param id:
            The value to assign to the id property of this EmManagedExternalHostInsight.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EmManagedExternalHostInsight.
        :type compartment_id: str

        :param host_name:
            The value to assign to the host_name property of this EmManagedExternalHostInsight.
        :type host_name: str

        :param host_display_name:
            The value to assign to the host_display_name property of this EmManagedExternalHostInsight.
        :type host_display_name: str

        :param host_type:
            The value to assign to the host_type property of this EmManagedExternalHostInsight.
        :type host_type: str

        :param processor_count:
            The value to assign to the processor_count property of this EmManagedExternalHostInsight.
        :type processor_count: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EmManagedExternalHostInsight.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EmManagedExternalHostInsight.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this EmManagedExternalHostInsight.
        :type system_tags: dict(str, dict(str, object))

        :param status:
            The value to assign to the status property of this EmManagedExternalHostInsight.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this EmManagedExternalHostInsight.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EmManagedExternalHostInsight.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EmManagedExternalHostInsight.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this EmManagedExternalHostInsight.
        :type lifecycle_details: str

        :param enterprise_manager_identifier:
            The value to assign to the enterprise_manager_identifier property of this EmManagedExternalHostInsight.
        :type enterprise_manager_identifier: str

        :param enterprise_manager_entity_name:
            The value to assign to the enterprise_manager_entity_name property of this EmManagedExternalHostInsight.
        :type enterprise_manager_entity_name: str

        :param enterprise_manager_entity_type:
            The value to assign to the enterprise_manager_entity_type property of this EmManagedExternalHostInsight.
        :type enterprise_manager_entity_type: str

        :param enterprise_manager_entity_identifier:
            The value to assign to the enterprise_manager_entity_identifier property of this EmManagedExternalHostInsight.
        :type enterprise_manager_entity_identifier: str

        :param enterprise_manager_entity_display_name:
            The value to assign to the enterprise_manager_entity_display_name property of this EmManagedExternalHostInsight.
        :type enterprise_manager_entity_display_name: str

        :param enterprise_manager_bridge_id:
            The value to assign to the enterprise_manager_bridge_id property of this EmManagedExternalHostInsight.
        :type enterprise_manager_bridge_id: str

        :param platform_type:
            The value to assign to the platform_type property of this EmManagedExternalHostInsight.
            Allowed values for this property are: "LINUX", "SOLARIS", "SUNOS", "ZLINUX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type platform_type: str

        :param platform_name:
            The value to assign to the platform_name property of this EmManagedExternalHostInsight.
        :type platform_name: str

        :param platform_version:
            The value to assign to the platform_version property of this EmManagedExternalHostInsight.
        :type platform_version: str

        :param exadata_insight_id:
            The value to assign to the exadata_insight_id property of this EmManagedExternalHostInsight.
        :type exadata_insight_id: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'host_name': 'str',
            'host_display_name': 'str',
            'host_type': 'str',
            'processor_count': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'status': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'enterprise_manager_identifier': 'str',
            'enterprise_manager_entity_name': 'str',
            'enterprise_manager_entity_type': 'str',
            'enterprise_manager_entity_identifier': 'str',
            'enterprise_manager_entity_display_name': 'str',
            'enterprise_manager_bridge_id': 'str',
            'platform_type': 'str',
            'platform_name': 'str',
            'platform_version': 'str',
            'exadata_insight_id': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'host_name': 'hostName',
            'host_display_name': 'hostDisplayName',
            'host_type': 'hostType',
            'processor_count': 'processorCount',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'status': 'status',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'enterprise_manager_identifier': 'enterpriseManagerIdentifier',
            'enterprise_manager_entity_name': 'enterpriseManagerEntityName',
            'enterprise_manager_entity_type': 'enterpriseManagerEntityType',
            'enterprise_manager_entity_identifier': 'enterpriseManagerEntityIdentifier',
            'enterprise_manager_entity_display_name': 'enterpriseManagerEntityDisplayName',
            'enterprise_manager_bridge_id': 'enterpriseManagerBridgeId',
            'platform_type': 'platformType',
            'platform_name': 'platformName',
            'platform_version': 'platformVersion',
            'exadata_insight_id': 'exadataInsightId'
        }

        self._entity_source = None
        self._id = None
        self._compartment_id = None
        self._host_name = None
        self._host_display_name = None
        self._host_type = None
        self._processor_count = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._status = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._enterprise_manager_identifier = None
        self._enterprise_manager_entity_name = None
        self._enterprise_manager_entity_type = None
        self._enterprise_manager_entity_identifier = None
        self._enterprise_manager_entity_display_name = None
        self._enterprise_manager_bridge_id = None
        self._platform_type = None
        self._platform_name = None
        self._platform_version = None
        self._exadata_insight_id = None
        self._entity_source = 'EM_MANAGED_EXTERNAL_HOST'

    @property
    def enterprise_manager_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_identifier of this EmManagedExternalHostInsight.
        Enterprise Manager Unique Identifier


        :return: The enterprise_manager_identifier of this EmManagedExternalHostInsight.
        :rtype: str
        """
        return self._enterprise_manager_identifier

    @enterprise_manager_identifier.setter
    def enterprise_manager_identifier(self, enterprise_manager_identifier):
        """
        Sets the enterprise_manager_identifier of this EmManagedExternalHostInsight.
        Enterprise Manager Unique Identifier


        :param enterprise_manager_identifier: The enterprise_manager_identifier of this EmManagedExternalHostInsight.
        :type: str
        """
        self._enterprise_manager_identifier = enterprise_manager_identifier

    @property
    def enterprise_manager_entity_name(self):
        """
        **[Required]** Gets the enterprise_manager_entity_name of this EmManagedExternalHostInsight.
        Enterprise Manager Entity Name


        :return: The enterprise_manager_entity_name of this EmManagedExternalHostInsight.
        :rtype: str
        """
        return self._enterprise_manager_entity_name

    @enterprise_manager_entity_name.setter
    def enterprise_manager_entity_name(self, enterprise_manager_entity_name):
        """
        Sets the enterprise_manager_entity_name of this EmManagedExternalHostInsight.
        Enterprise Manager Entity Name


        :param enterprise_manager_entity_name: The enterprise_manager_entity_name of this EmManagedExternalHostInsight.
        :type: str
        """
        self._enterprise_manager_entity_name = enterprise_manager_entity_name

    @property
    def enterprise_manager_entity_type(self):
        """
        **[Required]** Gets the enterprise_manager_entity_type of this EmManagedExternalHostInsight.
        Enterprise Manager Entity Type


        :return: The enterprise_manager_entity_type of this EmManagedExternalHostInsight.
        :rtype: str
        """
        return self._enterprise_manager_entity_type

    @enterprise_manager_entity_type.setter
    def enterprise_manager_entity_type(self, enterprise_manager_entity_type):
        """
        Sets the enterprise_manager_entity_type of this EmManagedExternalHostInsight.
        Enterprise Manager Entity Type


        :param enterprise_manager_entity_type: The enterprise_manager_entity_type of this EmManagedExternalHostInsight.
        :type: str
        """
        self._enterprise_manager_entity_type = enterprise_manager_entity_type

    @property
    def enterprise_manager_entity_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_entity_identifier of this EmManagedExternalHostInsight.
        Enterprise Manager Entity Unique Identifier


        :return: The enterprise_manager_entity_identifier of this EmManagedExternalHostInsight.
        :rtype: str
        """
        return self._enterprise_manager_entity_identifier

    @enterprise_manager_entity_identifier.setter
    def enterprise_manager_entity_identifier(self, enterprise_manager_entity_identifier):
        """
        Sets the enterprise_manager_entity_identifier of this EmManagedExternalHostInsight.
        Enterprise Manager Entity Unique Identifier


        :param enterprise_manager_entity_identifier: The enterprise_manager_entity_identifier of this EmManagedExternalHostInsight.
        :type: str
        """
        self._enterprise_manager_entity_identifier = enterprise_manager_entity_identifier

    @property
    def enterprise_manager_entity_display_name(self):
        """
        Gets the enterprise_manager_entity_display_name of this EmManagedExternalHostInsight.
        Enterprise Manager Entity Display Name


        :return: The enterprise_manager_entity_display_name of this EmManagedExternalHostInsight.
        :rtype: str
        """
        return self._enterprise_manager_entity_display_name

    @enterprise_manager_entity_display_name.setter
    def enterprise_manager_entity_display_name(self, enterprise_manager_entity_display_name):
        """
        Sets the enterprise_manager_entity_display_name of this EmManagedExternalHostInsight.
        Enterprise Manager Entity Display Name


        :param enterprise_manager_entity_display_name: The enterprise_manager_entity_display_name of this EmManagedExternalHostInsight.
        :type: str
        """
        self._enterprise_manager_entity_display_name = enterprise_manager_entity_display_name

    @property
    def enterprise_manager_bridge_id(self):
        """
        **[Required]** Gets the enterprise_manager_bridge_id of this EmManagedExternalHostInsight.
        OPSI Enterprise Manager Bridge OCID


        :return: The enterprise_manager_bridge_id of this EmManagedExternalHostInsight.
        :rtype: str
        """
        return self._enterprise_manager_bridge_id

    @enterprise_manager_bridge_id.setter
    def enterprise_manager_bridge_id(self, enterprise_manager_bridge_id):
        """
        Sets the enterprise_manager_bridge_id of this EmManagedExternalHostInsight.
        OPSI Enterprise Manager Bridge OCID


        :param enterprise_manager_bridge_id: The enterprise_manager_bridge_id of this EmManagedExternalHostInsight.
        :type: str
        """
        self._enterprise_manager_bridge_id = enterprise_manager_bridge_id

    @property
    def platform_type(self):
        """
        Gets the platform_type of this EmManagedExternalHostInsight.
        Platform type.
        Supported platformType(s) for MACS-managed external host insight: [LINUX].
        Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].

        Allowed values for this property are: "LINUX", "SOLARIS", "SUNOS", "ZLINUX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The platform_type of this EmManagedExternalHostInsight.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this EmManagedExternalHostInsight.
        Platform type.
        Supported platformType(s) for MACS-managed external host insight: [LINUX].
        Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].


        :param platform_type: The platform_type of this EmManagedExternalHostInsight.
        :type: str
        """
        allowed_values = ["LINUX", "SOLARIS", "SUNOS", "ZLINUX"]
        if not value_allowed_none_or_none_sentinel(platform_type, allowed_values):
            platform_type = 'UNKNOWN_ENUM_VALUE'
        self._platform_type = platform_type

    @property
    def platform_name(self):
        """
        Gets the platform_name of this EmManagedExternalHostInsight.
        Platform name.


        :return: The platform_name of this EmManagedExternalHostInsight.
        :rtype: str
        """
        return self._platform_name

    @platform_name.setter
    def platform_name(self, platform_name):
        """
        Sets the platform_name of this EmManagedExternalHostInsight.
        Platform name.


        :param platform_name: The platform_name of this EmManagedExternalHostInsight.
        :type: str
        """
        self._platform_name = platform_name

    @property
    def platform_version(self):
        """
        Gets the platform_version of this EmManagedExternalHostInsight.
        Platform version.


        :return: The platform_version of this EmManagedExternalHostInsight.
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """
        Sets the platform_version of this EmManagedExternalHostInsight.
        Platform version.


        :param platform_version: The platform_version of this EmManagedExternalHostInsight.
        :type: str
        """
        self._platform_version = platform_version

    @property
    def exadata_insight_id(self):
        """
        Gets the exadata_insight_id of this EmManagedExternalHostInsight.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The exadata_insight_id of this EmManagedExternalHostInsight.
        :rtype: str
        """
        return self._exadata_insight_id

    @exadata_insight_id.setter
    def exadata_insight_id(self, exadata_insight_id):
        """
        Sets the exadata_insight_id of this EmManagedExternalHostInsight.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param exadata_insight_id: The exadata_insight_id of this EmManagedExternalHostInsight.
        :type: str
        """
        self._exadata_insight_id = exadata_insight_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
