# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CapacityReservationInstanceSummary(object):
    """
    Condensed instance data when listing instances in a compute capacity reservation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CapacityReservationInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CapacityReservationInstanceSummary.
        :type id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CapacityReservationInstanceSummary.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CapacityReservationInstanceSummary.
        :type compartment_id: str

        :param fault_domain:
            The value to assign to the fault_domain property of this CapacityReservationInstanceSummary.
        :type fault_domain: str

        :param shape_config:
            The value to assign to the shape_config property of this CapacityReservationInstanceSummary.
        :type shape_config: oci.core.models.InstanceReservationShapeConfigDetails

        :param shape:
            The value to assign to the shape property of this CapacityReservationInstanceSummary.
        :type shape: str

        """
        self.swagger_types = {
            'id': 'str',
            'availability_domain': 'str',
            'compartment_id': 'str',
            'fault_domain': 'str',
            'shape_config': 'InstanceReservationShapeConfigDetails',
            'shape': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'fault_domain': 'faultDomain',
            'shape_config': 'shapeConfig',
            'shape': 'shape'
        }

        self._id = None
        self._availability_domain = None
        self._compartment_id = None
        self._fault_domain = None
        self._shape_config = None
        self._shape = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CapacityReservationInstanceSummary.
        The OCID of the instance.


        :return: The id of this CapacityReservationInstanceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CapacityReservationInstanceSummary.
        The OCID of the instance.


        :param id: The id of this CapacityReservationInstanceSummary.
        :type: str
        """
        self._id = id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CapacityReservationInstanceSummary.
        The availability domain the instance is running in.


        :return: The availability_domain of this CapacityReservationInstanceSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CapacityReservationInstanceSummary.
        The availability domain the instance is running in.


        :param availability_domain: The availability_domain of this CapacityReservationInstanceSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CapacityReservationInstanceSummary.
        The OCID of the compartment that contains the instance.


        :return: The compartment_id of this CapacityReservationInstanceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CapacityReservationInstanceSummary.
        The OCID of the compartment that contains the instance.


        :param compartment_id: The compartment_id of this CapacityReservationInstanceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this CapacityReservationInstanceSummary.
        The fault domain the instance is running in.


        :return: The fault_domain of this CapacityReservationInstanceSummary.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this CapacityReservationInstanceSummary.
        The fault domain the instance is running in.


        :param fault_domain: The fault_domain of this CapacityReservationInstanceSummary.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def shape_config(self):
        """
        Gets the shape_config of this CapacityReservationInstanceSummary.

        :return: The shape_config of this CapacityReservationInstanceSummary.
        :rtype: oci.core.models.InstanceReservationShapeConfigDetails
        """
        return self._shape_config

    @shape_config.setter
    def shape_config(self, shape_config):
        """
        Sets the shape_config of this CapacityReservationInstanceSummary.

        :param shape_config: The shape_config of this CapacityReservationInstanceSummary.
        :type: oci.core.models.InstanceReservationShapeConfigDetails
        """
        self._shape_config = shape_config

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this CapacityReservationInstanceSummary.
        The shape of the instance. The shape determines the number of CPUs, amount of memory,
        and other resources allocated to the instance.

        You can enumerate all available shapes by calling :func:`list_compute_capacity_reservation_instance_shapes`.


        :return: The shape of this CapacityReservationInstanceSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CapacityReservationInstanceSummary.
        The shape of the instance. The shape determines the number of CPUs, amount of memory,
        and other resources allocated to the instance.

        You can enumerate all available shapes by calling :func:`list_compute_capacity_reservation_instance_shapes`.


        :param shape: The shape of this CapacityReservationInstanceSummary.
        :type: str
        """
        self._shape = shape

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
