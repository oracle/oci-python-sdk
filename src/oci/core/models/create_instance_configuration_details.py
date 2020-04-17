# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_instance_configuration_base import CreateInstanceConfigurationBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateInstanceConfigurationDetails(CreateInstanceConfigurationBase):
    """
    Details for creating an instance configuration by providing a list of configuration settings.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateInstanceConfigurationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.CreateInstanceConfigurationDetails.source` attribute
        of this class is ``NONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateInstanceConfigurationDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateInstanceConfigurationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateInstanceConfigurationDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateInstanceConfigurationDetails.
        :type freeform_tags: dict(str, str)

        :param source:
            The value to assign to the source property of this CreateInstanceConfigurationDetails.
            Allowed values for this property are: "NONE", "INSTANCE"
        :type source: str

        :param instance_details:
            The value to assign to the instance_details property of this CreateInstanceConfigurationDetails.
        :type instance_details: InstanceConfigurationInstanceDetails

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'source': 'str',
            'instance_details': 'InstanceConfigurationInstanceDetails'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'source': 'source',
            'instance_details': 'instanceDetails'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._source = None
        self._instance_details = None
        self._source = 'NONE'

    @property
    def instance_details(self):
        """
        **[Required]** Gets the instance_details of this CreateInstanceConfigurationDetails.

        :return: The instance_details of this CreateInstanceConfigurationDetails.
        :rtype: InstanceConfigurationInstanceDetails
        """
        return self._instance_details

    @instance_details.setter
    def instance_details(self, instance_details):
        """
        Sets the instance_details of this CreateInstanceConfigurationDetails.

        :param instance_details: The instance_details of this CreateInstanceConfigurationDetails.
        :type: InstanceConfigurationInstanceDetails
        """
        self._instance_details = instance_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
