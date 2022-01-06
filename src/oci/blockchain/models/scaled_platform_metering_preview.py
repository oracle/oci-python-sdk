# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScaledPlatformMeteringPreview(object):
    """
    Blockchain Platform Metering Preview after Scaling
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScaledPlatformMeteringPreview object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total_ocpu_allocation:
            The value to assign to the total_ocpu_allocation property of this ScaledPlatformMeteringPreview.
        :type total_ocpu_allocation: float

        :param total_ocpu_allocation_post_scaling:
            The value to assign to the total_ocpu_allocation_post_scaling property of this ScaledPlatformMeteringPreview.
        :type total_ocpu_allocation_post_scaling: float

        :param storage_metered_units:
            The value to assign to the storage_metered_units property of this ScaledPlatformMeteringPreview.
        :type storage_metered_units: float

        :param extra_storage_metered_units:
            The value to assign to the extra_storage_metered_units property of this ScaledPlatformMeteringPreview.
        :type extra_storage_metered_units: float

        :param storage_metered_units_post_scaling:
            The value to assign to the storage_metered_units_post_scaling property of this ScaledPlatformMeteringPreview.
        :type storage_metered_units_post_scaling: float

        """
        self.swagger_types = {
            'total_ocpu_allocation': 'float',
            'total_ocpu_allocation_post_scaling': 'float',
            'storage_metered_units': 'float',
            'extra_storage_metered_units': 'float',
            'storage_metered_units_post_scaling': 'float'
        }

        self.attribute_map = {
            'total_ocpu_allocation': 'totalOcpuAllocation',
            'total_ocpu_allocation_post_scaling': 'totalOcpuAllocationPostScaling',
            'storage_metered_units': 'storageMeteredUnits',
            'extra_storage_metered_units': 'extraStorageMeteredUnits',
            'storage_metered_units_post_scaling': 'storageMeteredUnitsPostScaling'
        }

        self._total_ocpu_allocation = None
        self._total_ocpu_allocation_post_scaling = None
        self._storage_metered_units = None
        self._extra_storage_metered_units = None
        self._storage_metered_units_post_scaling = None

    @property
    def total_ocpu_allocation(self):
        """
        Gets the total_ocpu_allocation of this ScaledPlatformMeteringPreview.
        Number of total OCPU allocation for the blockchain platform


        :return: The total_ocpu_allocation of this ScaledPlatformMeteringPreview.
        :rtype: float
        """
        return self._total_ocpu_allocation

    @total_ocpu_allocation.setter
    def total_ocpu_allocation(self, total_ocpu_allocation):
        """
        Sets the total_ocpu_allocation of this ScaledPlatformMeteringPreview.
        Number of total OCPU allocation for the blockchain platform


        :param total_ocpu_allocation: The total_ocpu_allocation of this ScaledPlatformMeteringPreview.
        :type: float
        """
        self._total_ocpu_allocation = total_ocpu_allocation

    @property
    def total_ocpu_allocation_post_scaling(self):
        """
        Gets the total_ocpu_allocation_post_scaling of this ScaledPlatformMeteringPreview.
        Number of total OCPU allocation for the blockchain platform after Scaling


        :return: The total_ocpu_allocation_post_scaling of this ScaledPlatformMeteringPreview.
        :rtype: float
        """
        return self._total_ocpu_allocation_post_scaling

    @total_ocpu_allocation_post_scaling.setter
    def total_ocpu_allocation_post_scaling(self, total_ocpu_allocation_post_scaling):
        """
        Sets the total_ocpu_allocation_post_scaling of this ScaledPlatformMeteringPreview.
        Number of total OCPU allocation for the blockchain platform after Scaling


        :param total_ocpu_allocation_post_scaling: The total_ocpu_allocation_post_scaling of this ScaledPlatformMeteringPreview.
        :type: float
        """
        self._total_ocpu_allocation_post_scaling = total_ocpu_allocation_post_scaling

    @property
    def storage_metered_units(self):
        """
        Gets the storage_metered_units of this ScaledPlatformMeteringPreview.
        Current Storage metered units in TBs


        :return: The storage_metered_units of this ScaledPlatformMeteringPreview.
        :rtype: float
        """
        return self._storage_metered_units

    @storage_metered_units.setter
    def storage_metered_units(self, storage_metered_units):
        """
        Sets the storage_metered_units of this ScaledPlatformMeteringPreview.
        Current Storage metered units in TBs


        :param storage_metered_units: The storage_metered_units of this ScaledPlatformMeteringPreview.
        :type: float
        """
        self._storage_metered_units = storage_metered_units

    @property
    def extra_storage_metered_units(self):
        """
        Gets the extra_storage_metered_units of this ScaledPlatformMeteringPreview.
        Extra Storage units required in TBs


        :return: The extra_storage_metered_units of this ScaledPlatformMeteringPreview.
        :rtype: float
        """
        return self._extra_storage_metered_units

    @extra_storage_metered_units.setter
    def extra_storage_metered_units(self, extra_storage_metered_units):
        """
        Sets the extra_storage_metered_units of this ScaledPlatformMeteringPreview.
        Extra Storage units required in TBs


        :param extra_storage_metered_units: The extra_storage_metered_units of this ScaledPlatformMeteringPreview.
        :type: float
        """
        self._extra_storage_metered_units = extra_storage_metered_units

    @property
    def storage_metered_units_post_scaling(self):
        """
        Gets the storage_metered_units_post_scaling of this ScaledPlatformMeteringPreview.
        Total Post Scaling Storage metered units in TBs


        :return: The storage_metered_units_post_scaling of this ScaledPlatformMeteringPreview.
        :rtype: float
        """
        return self._storage_metered_units_post_scaling

    @storage_metered_units_post_scaling.setter
    def storage_metered_units_post_scaling(self, storage_metered_units_post_scaling):
        """
        Sets the storage_metered_units_post_scaling of this ScaledPlatformMeteringPreview.
        Total Post Scaling Storage metered units in TBs


        :param storage_metered_units_post_scaling: The storage_metered_units_post_scaling of this ScaledPlatformMeteringPreview.
        :type: float
        """
        self._storage_metered_units_post_scaling = storage_metered_units_post_scaling

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
