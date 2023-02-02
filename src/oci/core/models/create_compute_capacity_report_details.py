# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateComputeCapacityReportDetails(object):
    """
    The details for creating a new compute capacity availability report.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateComputeCapacityReportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateComputeCapacityReportDetails.
        :type compartment_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateComputeCapacityReportDetails.
        :type availability_domain: str

        :param shape_availabilities:
            The value to assign to the shape_availabilities property of this CreateComputeCapacityReportDetails.
        :type shape_availabilities: list[oci.core.models.CreateCapacityReportShapeAvailabilityDetails]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'availability_domain': 'str',
            'shape_availabilities': 'list[CreateCapacityReportShapeAvailabilityDetails]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'availability_domain': 'availabilityDomain',
            'shape_availabilities': 'shapeAvailabilities'
        }

        self._compartment_id = None
        self._availability_domain = None
        self._shape_availabilities = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateComputeCapacityReportDetails.
        The `OCID`__ for the compartment. This should always be the root
        compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateComputeCapacityReportDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateComputeCapacityReportDetails.
        The `OCID`__ for the compartment. This should always be the root
        compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateComputeCapacityReportDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateComputeCapacityReportDetails.
        The availability domain of this compute capacity report.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this CreateComputeCapacityReportDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateComputeCapacityReportDetails.
        The availability domain of this compute capacity report.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this CreateComputeCapacityReportDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def shape_availabilities(self):
        """
        **[Required]** Gets the shape_availabilities of this CreateComputeCapacityReportDetails.
        The capacity configurations for the capacity report.


        :return: The shape_availabilities of this CreateComputeCapacityReportDetails.
        :rtype: list[oci.core.models.CreateCapacityReportShapeAvailabilityDetails]
        """
        return self._shape_availabilities

    @shape_availabilities.setter
    def shape_availabilities(self, shape_availabilities):
        """
        Sets the shape_availabilities of this CreateComputeCapacityReportDetails.
        The capacity configurations for the capacity report.


        :param shape_availabilities: The shape_availabilities of this CreateComputeCapacityReportDetails.
        :type: list[oci.core.models.CreateCapacityReportShapeAvailabilityDetails]
        """
        self._shape_availabilities = shape_availabilities

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
