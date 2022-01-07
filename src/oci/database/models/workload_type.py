# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkloadType(object):
    """
    The number of consumed OCPUs, by database workload type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkloadType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param atp:
            The value to assign to the atp property of this WorkloadType.
        :type atp: float

        :param adw:
            The value to assign to the adw property of this WorkloadType.
        :type adw: float

        """
        self.swagger_types = {
            'atp': 'float',
            'adw': 'float'
        }

        self.attribute_map = {
            'atp': 'atp',
            'adw': 'adw'
        }

        self._atp = None
        self._adw = None

    @property
    def atp(self):
        """
        Gets the atp of this WorkloadType.
        The total number of OCPU cores in use for Autonomous Transaction Processing databases in the infrastructure instance.


        :return: The atp of this WorkloadType.
        :rtype: float
        """
        return self._atp

    @atp.setter
    def atp(self, atp):
        """
        Sets the atp of this WorkloadType.
        The total number of OCPU cores in use for Autonomous Transaction Processing databases in the infrastructure instance.


        :param atp: The atp of this WorkloadType.
        :type: float
        """
        self._atp = atp

    @property
    def adw(self):
        """
        Gets the adw of this WorkloadType.
        The total number of OCPU cores in use for Autonomous Data Warehouse databases in the infrastructure instance.


        :return: The adw of this WorkloadType.
        :rtype: float
        """
        return self._adw

    @adw.setter
    def adw(self, adw):
        """
        Sets the adw of this WorkloadType.
        The total number of OCPU cores in use for Autonomous Data Warehouse databases in the infrastructure instance.


        :param adw: The adw of this WorkloadType.
        :type: float
        """
        self._adw = adw

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
