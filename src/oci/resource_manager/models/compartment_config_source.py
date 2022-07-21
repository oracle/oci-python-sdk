# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .config_source import ConfigSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CompartmentConfigSource(ConfigSource):
    """
    Compartment to use for creating the stack.
    The new stack will include definitions for supported resource types in this compartment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CompartmentConfigSource object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.CompartmentConfigSource.config_source_type` attribute
        of this class is ``COMPARTMENT_CONFIG_SOURCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_type:
            The value to assign to the config_source_type property of this CompartmentConfigSource.
            Allowed values for this property are: "COMPARTMENT_CONFIG_SOURCE", "GIT_CONFIG_SOURCE", "OBJECT_STORAGE_CONFIG_SOURCE", "ZIP_UPLOAD"
        :type config_source_type: str

        :param working_directory:
            The value to assign to the working_directory property of this CompartmentConfigSource.
        :type working_directory: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CompartmentConfigSource.
        :type compartment_id: str

        :param region:
            The value to assign to the region property of this CompartmentConfigSource.
        :type region: str

        :param services_to_discover:
            The value to assign to the services_to_discover property of this CompartmentConfigSource.
        :type services_to_discover: list[str]

        """
        self.swagger_types = {
            'config_source_type': 'str',
            'working_directory': 'str',
            'compartment_id': 'str',
            'region': 'str',
            'services_to_discover': 'list[str]'
        }

        self.attribute_map = {
            'config_source_type': 'configSourceType',
            'working_directory': 'workingDirectory',
            'compartment_id': 'compartmentId',
            'region': 'region',
            'services_to_discover': 'servicesToDiscover'
        }

        self._config_source_type = None
        self._working_directory = None
        self._compartment_id = None
        self._region = None
        self._services_to_discover = None
        self._config_source_type = 'COMPARTMENT_CONFIG_SOURCE'

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CompartmentConfigSource.
        The `OCID`__ of the compartment to use
        for creating the stack. The new stack will include definitions for supported
        resource types in this compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CompartmentConfigSource.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CompartmentConfigSource.
        The `OCID`__ of the compartment to use
        for creating the stack. The new stack will include definitions for supported
        resource types in this compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CompartmentConfigSource.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def region(self):
        """
        **[Required]** Gets the region of this CompartmentConfigSource.
        The region to use for creating the stack. The new stack will include definitions for
        supported resource types in this region.


        :return: The region of this CompartmentConfigSource.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this CompartmentConfigSource.
        The region to use for creating the stack. The new stack will include definitions for
        supported resource types in this region.


        :param region: The region of this CompartmentConfigSource.
        :type: str
        """
        self._region = region

    @property
    def services_to_discover(self):
        """
        Gets the services_to_discover of this CompartmentConfigSource.
        Filter for `services to use with Resource Discovery`__.
        For example, \"database\" limits resource discovery to resource types within the Database service.
        The specified services must be in scope of the given compartment OCID (tenancy level for root compartment, compartment level otherwise).
        If not specified, then all services at the scope of the given compartment OCID are used.

        __ https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services


        :return: The services_to_discover of this CompartmentConfigSource.
        :rtype: list[str]
        """
        return self._services_to_discover

    @services_to_discover.setter
    def services_to_discover(self, services_to_discover):
        """
        Sets the services_to_discover of this CompartmentConfigSource.
        Filter for `services to use with Resource Discovery`__.
        For example, \"database\" limits resource discovery to resource types within the Database service.
        The specified services must be in scope of the given compartment OCID (tenancy level for root compartment, compartment level otherwise).
        If not specified, then all services at the scope of the given compartment OCID are used.

        __ https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services


        :param services_to_discover: The services_to_discover of this CompartmentConfigSource.
        :type: list[str]
        """
        self._services_to_discover = services_to_discover

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
