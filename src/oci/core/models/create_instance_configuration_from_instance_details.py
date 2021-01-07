# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_instance_configuration_base import CreateInstanceConfigurationBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateInstanceConfigurationFromInstanceDetails(CreateInstanceConfigurationBase):
    """
    Details for creating an instance configuration using an existing instance as a template.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateInstanceConfigurationFromInstanceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.CreateInstanceConfigurationFromInstanceDetails.source` attribute
        of this class is ``INSTANCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateInstanceConfigurationFromInstanceDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateInstanceConfigurationFromInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateInstanceConfigurationFromInstanceDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateInstanceConfigurationFromInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param source:
            The value to assign to the source property of this CreateInstanceConfigurationFromInstanceDetails.
            Allowed values for this property are: "NONE", "INSTANCE"
        :type source: str

        :param instance_id:
            The value to assign to the instance_id property of this CreateInstanceConfigurationFromInstanceDetails.
        :type instance_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'source': 'str',
            'instance_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'source': 'source',
            'instance_id': 'instanceId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._source = None
        self._instance_id = None
        self._source = 'INSTANCE'

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this CreateInstanceConfigurationFromInstanceDetails.
        The `OCID`__ of the instance to use to create the
        instance configuration.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The instance_id of this CreateInstanceConfigurationFromInstanceDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this CreateInstanceConfigurationFromInstanceDetails.
        The `OCID`__ of the instance to use to create the
        instance configuration.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param instance_id: The instance_id of this CreateInstanceConfigurationFromInstanceDetails.
        :type: str
        """
        self._instance_id = instance_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
