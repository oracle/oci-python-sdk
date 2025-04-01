# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .instance_component import InstanceComponent
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MlApplicationInstanceInternalTrigger(InstanceComponent):
    """
    Trigger details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MlApplicationInstanceInternalTrigger object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.MlApplicationInstanceInternalTrigger.type` attribute
        of this class is ``ML_APPLICATION_INSTANCE_INTERNAL_TRIGGER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this MlApplicationInstanceInternalTrigger.
            Allowed values for this property are: "DATA_SCIENCE_MODEL_DEPLOYMENT", "OBJECT_STORAGE_BUCKET", "OBJECT_STORAGE_OBJECT", "ML_APPLICATION_INSTANCE_INTERNAL_TRIGGER", "DATA_SCIENCE_SCHEDULE", "GENERIC_OCI_RESOURCE"
        :type type: str

        :param name:
            The value to assign to the name property of this MlApplicationInstanceInternalTrigger.
        :type name: str

        :param component_name:
            The value to assign to the component_name property of this MlApplicationInstanceInternalTrigger.
        :type component_name: str

        :param trigger_definition:
            The value to assign to the trigger_definition property of this MlApplicationInstanceInternalTrigger.
        :type trigger_definition: str

        :param is_enabled:
            The value to assign to the is_enabled property of this MlApplicationInstanceInternalTrigger.
        :type is_enabled: bool

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'component_name': 'str',
            'trigger_definition': 'str',
            'is_enabled': 'bool'
        }
        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'component_name': 'componentName',
            'trigger_definition': 'triggerDefinition',
            'is_enabled': 'isEnabled'
        }
        self._type = None
        self._name = None
        self._component_name = None
        self._trigger_definition = None
        self._is_enabled = None
        self._type = 'ML_APPLICATION_INSTANCE_INTERNAL_TRIGGER'

    @property
    def trigger_definition(self):
        """
        **[Required]** Gets the trigger_definition of this MlApplicationInstanceInternalTrigger.
        Trigger definition for given ML Application Instance


        :return: The trigger_definition of this MlApplicationInstanceInternalTrigger.
        :rtype: str
        """
        return self._trigger_definition

    @trigger_definition.setter
    def trigger_definition(self, trigger_definition):
        """
        Sets the trigger_definition of this MlApplicationInstanceInternalTrigger.
        Trigger definition for given ML Application Instance


        :param trigger_definition: The trigger_definition of this MlApplicationInstanceInternalTrigger.
        :type: str
        """
        self._trigger_definition = trigger_definition

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this MlApplicationInstanceInternalTrigger.
        Indicates whether the trigger is enabled. If it is false trigger does not fire even when the trigger condition is met.


        :return: The is_enabled of this MlApplicationInstanceInternalTrigger.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this MlApplicationInstanceInternalTrigger.
        Indicates whether the trigger is enabled. If it is false trigger does not fire even when the trigger condition is met.


        :param is_enabled: The is_enabled of this MlApplicationInstanceInternalTrigger.
        :type: bool
        """
        self._is_enabled = is_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
