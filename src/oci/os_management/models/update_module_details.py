# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateModuleDetails(object):
    """
    A description of a module and its stream
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateModuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param module_name:
            The value to assign to the module_name property of this UpdateModuleDetails.
        :type module_name: str

        :param streams:
            The value to assign to the streams property of this UpdateModuleDetails.
        :type streams: list[oci.os_management.models.UpdateModuleStreamDetails]

        """
        self.swagger_types = {
            'module_name': 'str',
            'streams': 'list[UpdateModuleStreamDetails]'
        }

        self.attribute_map = {
            'module_name': 'moduleName',
            'streams': 'streams'
        }

        self._module_name = None
        self._streams = None

    @property
    def module_name(self):
        """
        **[Required]** Gets the module_name of this UpdateModuleDetails.
        The name of a module


        :return: The module_name of this UpdateModuleDetails.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this UpdateModuleDetails.
        The name of a module


        :param module_name: The module_name of this UpdateModuleDetails.
        :type: str
        """
        self._module_name = module_name

    @property
    def streams(self):
        """
        Gets the streams of this UpdateModuleDetails.
        The streams of the module


        :return: The streams of this UpdateModuleDetails.
        :rtype: list[oci.os_management.models.UpdateModuleStreamDetails]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        """
        Sets the streams of this UpdateModuleDetails.
        The streams of the module


        :param streams: The streams of this UpdateModuleDetails.
        :type: list[oci.os_management.models.UpdateModuleStreamDetails]
        """
        self._streams = streams

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
