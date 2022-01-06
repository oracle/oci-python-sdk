# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KernelVmCoreInformation(object):
    """
    VMcore information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KernelVmCoreInformation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param component:
            The value to assign to the component property of this KernelVmCoreInformation.
        :type component: str

        :param backtrace:
            The value to assign to the backtrace property of this KernelVmCoreInformation.
        :type backtrace: str

        """
        self.swagger_types = {
            'component': 'str',
            'backtrace': 'str'
        }

        self.attribute_map = {
            'component': 'component',
            'backtrace': 'backtrace'
        }

        self._component = None
        self._backtrace = None

    @property
    def component(self):
        """
        Gets the component of this KernelVmCoreInformation.
        Kernel module responsible of the crash.


        :return: The component of this KernelVmCoreInformation.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """
        Sets the component of this KernelVmCoreInformation.
        Kernel module responsible of the crash.


        :param component: The component of this KernelVmCoreInformation.
        :type: str
        """
        self._component = component

    @property
    def backtrace(self):
        """
        Gets the backtrace of this KernelVmCoreInformation.
        Crash backtrace.


        :return: The backtrace of this KernelVmCoreInformation.
        :rtype: str
        """
        return self._backtrace

    @backtrace.setter
    def backtrace(self, backtrace):
        """
        Sets the backtrace of this KernelVmCoreInformation.
        Crash backtrace.


        :param backtrace: The backtrace of this KernelVmCoreInformation.
        :type: str
        """
        self._backtrace = backtrace

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
