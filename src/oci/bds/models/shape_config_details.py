# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapeConfigDetails(object):
    """
    The shape configuration requested for the node.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ShapeConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ocpus:
            The value to assign to the ocpus property of this ShapeConfigDetails.
        :type ocpus: int

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this ShapeConfigDetails.
        :type memory_in_gbs: int

        """
        self.swagger_types = {
            'ocpus': 'int',
            'memory_in_gbs': 'int'
        }

        self.attribute_map = {
            'ocpus': 'ocpus',
            'memory_in_gbs': 'memoryInGBs'
        }

        self._ocpus = None
        self._memory_in_gbs = None

    @property
    def ocpus(self):
        """
        Gets the ocpus of this ShapeConfigDetails.
        The total number of OCPUs available to the node.


        :return: The ocpus of this ShapeConfigDetails.
        :rtype: int
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this ShapeConfigDetails.
        The total number of OCPUs available to the node.


        :param ocpus: The ocpus of this ShapeConfigDetails.
        :type: int
        """
        self._ocpus = ocpus

    @property
    def memory_in_gbs(self):
        """
        Gets the memory_in_gbs of this ShapeConfigDetails.
        The total amount of memory available to the node, in gigabytes


        :return: The memory_in_gbs of this ShapeConfigDetails.
        :rtype: int
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this ShapeConfigDetails.
        The total amount of memory available to the node, in gigabytes


        :param memory_in_gbs: The memory_in_gbs of this ShapeConfigDetails.
        :type: int
        """
        self._memory_in_gbs = memory_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
