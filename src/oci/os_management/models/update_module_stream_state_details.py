# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateModuleStreamStateDetails(object):
    """
    A complete description of the state of modules on a managed instance
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateModuleStreamStateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param modules:
            The value to assign to the modules property of this UpdateModuleStreamStateDetails.
        :type modules: list[oci.os_management.models.UpdateModuleDetails]

        """
        self.swagger_types = {
            'modules': 'list[UpdateModuleDetails]'
        }

        self.attribute_map = {
            'modules': 'modules'
        }

        self._modules = None

    @property
    def modules(self):
        """
        Gets the modules of this UpdateModuleStreamStateDetails.
        The modules known to a managed instance


        :return: The modules of this UpdateModuleStreamStateDetails.
        :rtype: list[oci.os_management.models.UpdateModuleDetails]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        """
        Sets the modules of this UpdateModuleStreamStateDetails.
        The modules known to a managed instance


        :param modules: The modules of this UpdateModuleStreamStateDetails.
        :type: list[oci.os_management.models.UpdateModuleDetails]
        """
        self._modules = modules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
