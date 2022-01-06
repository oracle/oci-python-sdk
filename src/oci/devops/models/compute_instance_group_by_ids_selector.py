# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .compute_instance_group_selector import ComputeInstanceGroupSelector
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceGroupByIdsSelector(ComputeInstanceGroupSelector):
    """
    Specifies the Compute instance group environment by listing the OCIDs of the compute instances.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceGroupByIdsSelector object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ComputeInstanceGroupByIdsSelector.selector_type` attribute
        of this class is ``INSTANCE_IDS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param selector_type:
            The value to assign to the selector_type property of this ComputeInstanceGroupByIdsSelector.
            Allowed values for this property are: "INSTANCE_IDS", "INSTANCE_QUERY"
        :type selector_type: str

        :param compute_instance_ids:
            The value to assign to the compute_instance_ids property of this ComputeInstanceGroupByIdsSelector.
        :type compute_instance_ids: list[str]

        """
        self.swagger_types = {
            'selector_type': 'str',
            'compute_instance_ids': 'list[str]'
        }

        self.attribute_map = {
            'selector_type': 'selectorType',
            'compute_instance_ids': 'computeInstanceIds'
        }

        self._selector_type = None
        self._compute_instance_ids = None
        self._selector_type = 'INSTANCE_IDS'

    @property
    def compute_instance_ids(self):
        """
        **[Required]** Gets the compute_instance_ids of this ComputeInstanceGroupByIdsSelector.
        Compute instance OCID identifiers that are members of this group.


        :return: The compute_instance_ids of this ComputeInstanceGroupByIdsSelector.
        :rtype: list[str]
        """
        return self._compute_instance_ids

    @compute_instance_ids.setter
    def compute_instance_ids(self, compute_instance_ids):
        """
        Sets the compute_instance_ids of this ComputeInstanceGroupByIdsSelector.
        Compute instance OCID identifiers that are members of this group.


        :param compute_instance_ids: The compute_instance_ids of this ComputeInstanceGroupByIdsSelector.
        :type: list[str]
        """
        self._compute_instance_ids = compute_instance_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
