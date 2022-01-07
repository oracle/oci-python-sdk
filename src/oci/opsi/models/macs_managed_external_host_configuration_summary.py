# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_configuration_summary import HostConfigurationSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MacsManagedExternalHostConfigurationSummary(HostConfigurationSummary):
    """
    Configuration Summary of a Macs Managed External host.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MacsManagedExternalHostConfigurationSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.MacsManagedExternalHostConfigurationSummary.entity_source` attribute
        of this class is ``MACS_MANAGED_EXTERNAL_HOST`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host_insight_id:
            The value to assign to the host_insight_id property of this MacsManagedExternalHostConfigurationSummary.
        :type host_insight_id: str

        :param entity_source:
            The value to assign to the entity_source property of this MacsManagedExternalHostConfigurationSummary.
            Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST"
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MacsManagedExternalHostConfigurationSummary.
        :type compartment_id: str

        :param host_name:
            The value to assign to the host_name property of this MacsManagedExternalHostConfigurationSummary.
        :type host_name: str

        :param platform_type:
            The value to assign to the platform_type property of this MacsManagedExternalHostConfigurationSummary.
            Allowed values for this property are: "LINUX", "SOLARIS", "SUNOS"
        :type platform_type: str

        :param platform_version:
            The value to assign to the platform_version property of this MacsManagedExternalHostConfigurationSummary.
        :type platform_version: str

        :param platform_vendor:
            The value to assign to the platform_vendor property of this MacsManagedExternalHostConfigurationSummary.
        :type platform_vendor: str

        :param total_cpus:
            The value to assign to the total_cpus property of this MacsManagedExternalHostConfigurationSummary.
        :type total_cpus: int

        :param total_memory_in_gbs:
            The value to assign to the total_memory_in_gbs property of this MacsManagedExternalHostConfigurationSummary.
        :type total_memory_in_gbs: float

        :param cpu_architecture:
            The value to assign to the cpu_architecture property of this MacsManagedExternalHostConfigurationSummary.
        :type cpu_architecture: str

        :param cpu_cache_in_mbs:
            The value to assign to the cpu_cache_in_mbs property of this MacsManagedExternalHostConfigurationSummary.
        :type cpu_cache_in_mbs: float

        :param cpu_vendor:
            The value to assign to the cpu_vendor property of this MacsManagedExternalHostConfigurationSummary.
        :type cpu_vendor: str

        :param cpu_frequency_in_mhz:
            The value to assign to the cpu_frequency_in_mhz property of this MacsManagedExternalHostConfigurationSummary.
        :type cpu_frequency_in_mhz: float

        :param cpu_implementation:
            The value to assign to the cpu_implementation property of this MacsManagedExternalHostConfigurationSummary.
        :type cpu_implementation: str

        :param cores_per_socket:
            The value to assign to the cores_per_socket property of this MacsManagedExternalHostConfigurationSummary.
        :type cores_per_socket: int

        :param total_sockets:
            The value to assign to the total_sockets property of this MacsManagedExternalHostConfigurationSummary.
        :type total_sockets: int

        :param threads_per_socket:
            The value to assign to the threads_per_socket property of this MacsManagedExternalHostConfigurationSummary.
        :type threads_per_socket: int

        :param is_hyper_threading_enabled:
            The value to assign to the is_hyper_threading_enabled property of this MacsManagedExternalHostConfigurationSummary.
        :type is_hyper_threading_enabled: bool

        :param defined_tags:
            The value to assign to the defined_tags property of this MacsManagedExternalHostConfigurationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MacsManagedExternalHostConfigurationSummary.
        :type freeform_tags: dict(str, str)

        :param management_agent_id:
            The value to assign to the management_agent_id property of this MacsManagedExternalHostConfigurationSummary.
        :type management_agent_id: str

        :param connector_id:
            The value to assign to the connector_id property of this MacsManagedExternalHostConfigurationSummary.
        :type connector_id: str

        """
        self.swagger_types = {
            'host_insight_id': 'str',
            'entity_source': 'str',
            'compartment_id': 'str',
            'host_name': 'str',
            'platform_type': 'str',
            'platform_version': 'str',
            'platform_vendor': 'str',
            'total_cpus': 'int',
            'total_memory_in_gbs': 'float',
            'cpu_architecture': 'str',
            'cpu_cache_in_mbs': 'float',
            'cpu_vendor': 'str',
            'cpu_frequency_in_mhz': 'float',
            'cpu_implementation': 'str',
            'cores_per_socket': 'int',
            'total_sockets': 'int',
            'threads_per_socket': 'int',
            'is_hyper_threading_enabled': 'bool',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'management_agent_id': 'str',
            'connector_id': 'str'
        }

        self.attribute_map = {
            'host_insight_id': 'hostInsightId',
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'host_name': 'hostName',
            'platform_type': 'platformType',
            'platform_version': 'platformVersion',
            'platform_vendor': 'platformVendor',
            'total_cpus': 'totalCpus',
            'total_memory_in_gbs': 'totalMemoryInGBs',
            'cpu_architecture': 'cpuArchitecture',
            'cpu_cache_in_mbs': 'cpuCacheInMBs',
            'cpu_vendor': 'cpuVendor',
            'cpu_frequency_in_mhz': 'cpuFrequencyInMhz',
            'cpu_implementation': 'cpuImplementation',
            'cores_per_socket': 'coresPerSocket',
            'total_sockets': 'totalSockets',
            'threads_per_socket': 'threadsPerSocket',
            'is_hyper_threading_enabled': 'isHyperThreadingEnabled',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'management_agent_id': 'managementAgentId',
            'connector_id': 'connectorId'
        }

        self._host_insight_id = None
        self._entity_source = None
        self._compartment_id = None
        self._host_name = None
        self._platform_type = None
        self._platform_version = None
        self._platform_vendor = None
        self._total_cpus = None
        self._total_memory_in_gbs = None
        self._cpu_architecture = None
        self._cpu_cache_in_mbs = None
        self._cpu_vendor = None
        self._cpu_frequency_in_mhz = None
        self._cpu_implementation = None
        self._cores_per_socket = None
        self._total_sockets = None
        self._threads_per_socket = None
        self._is_hyper_threading_enabled = None
        self._defined_tags = None
        self._freeform_tags = None
        self._management_agent_id = None
        self._connector_id = None
        self._entity_source = 'MACS_MANAGED_EXTERNAL_HOST'

    @property
    def management_agent_id(self):
        """
        **[Required]** Gets the management_agent_id of this MacsManagedExternalHostConfigurationSummary.
        The `OCID`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this MacsManagedExternalHostConfigurationSummary.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this MacsManagedExternalHostConfigurationSummary.
        The `OCID`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this MacsManagedExternalHostConfigurationSummary.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def connector_id(self):
        """
        Gets the connector_id of this MacsManagedExternalHostConfigurationSummary.
        The `OCID`__ of External Database Connector

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The connector_id of this MacsManagedExternalHostConfigurationSummary.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """
        Sets the connector_id of this MacsManagedExternalHostConfigurationSummary.
        The `OCID`__ of External Database Connector

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param connector_id: The connector_id of this MacsManagedExternalHostConfigurationSummary.
        :type: str
        """
        self._connector_id = connector_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
