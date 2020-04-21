# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddImageShapeCompatibilityEntryDetails(object):
    """
    Image shape compatibility details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddImageShapeCompatibilityEntryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ocpu_constraints:
            The value to assign to the ocpu_constraints property of this AddImageShapeCompatibilityEntryDetails.
        :type ocpu_constraints: ImageOcpuConstraints

        """
        self.swagger_types = {
            'ocpu_constraints': 'ImageOcpuConstraints'
        }

        self.attribute_map = {
            'ocpu_constraints': 'ocpuConstraints'
        }

        self._ocpu_constraints = None

    @property
    def ocpu_constraints(self):
        """
        Gets the ocpu_constraints of this AddImageShapeCompatibilityEntryDetails.

        :return: The ocpu_constraints of this AddImageShapeCompatibilityEntryDetails.
        :rtype: ImageOcpuConstraints
        """
        return self._ocpu_constraints

    @ocpu_constraints.setter
    def ocpu_constraints(self, ocpu_constraints):
        """
        Sets the ocpu_constraints of this AddImageShapeCompatibilityEntryDetails.

        :param ocpu_constraints: The ocpu_constraints of this AddImageShapeCompatibilityEntryDetails.
        :type: ImageOcpuConstraints
        """
        self._ocpu_constraints = ocpu_constraints

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
