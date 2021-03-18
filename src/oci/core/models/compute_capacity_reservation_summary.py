# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeCapacityReservationSummary(object):
    """
    Summary information for a compute capacity reservation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeCapacityReservationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ComputeCapacityReservationSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ComputeCapacityReservationSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ComputeCapacityReservationSummary.
        :type display_name: str

        :param defined_tags:
            The value to assign to the defined_tags property of this ComputeCapacityReservationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ComputeCapacityReservationSummary.
        :type freeform_tags: dict(str, str)

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ComputeCapacityReservationSummary.
        :type lifecycle_state: str

        :param availability_domain:
            The value to assign to the availability_domain property of this ComputeCapacityReservationSummary.
        :type availability_domain: str

        :param reserved_instance_count:
            The value to assign to the reserved_instance_count property of this ComputeCapacityReservationSummary.
        :type reserved_instance_count: int

        :param used_instance_count:
            The value to assign to the used_instance_count property of this ComputeCapacityReservationSummary.
        :type used_instance_count: int

        :param is_default_reservation:
            The value to assign to the is_default_reservation property of this ComputeCapacityReservationSummary.
        :type is_default_reservation: bool

        :param time_created:
            The value to assign to the time_created property of this ComputeCapacityReservationSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'lifecycle_state': 'str',
            'availability_domain': 'str',
            'reserved_instance_count': 'int',
            'used_instance_count': 'int',
            'is_default_reservation': 'bool',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'lifecycle_state': 'lifecycleState',
            'availability_domain': 'availabilityDomain',
            'reserved_instance_count': 'reservedInstanceCount',
            'used_instance_count': 'usedInstanceCount',
            'is_default_reservation': 'isDefaultReservation',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._defined_tags = None
        self._freeform_tags = None
        self._lifecycle_state = None
        self._availability_domain = None
        self._reserved_instance_count = None
        self._used_instance_count = None
        self._is_default_reservation = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ComputeCapacityReservationSummary.
        The OCID of the instance reservation configuration.


        :return: The id of this ComputeCapacityReservationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ComputeCapacityReservationSummary.
        The OCID of the instance reservation configuration.


        :param id: The id of this ComputeCapacityReservationSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ComputeCapacityReservationSummary.
        The OCID of the compartment.


        :return: The compartment_id of this ComputeCapacityReservationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ComputeCapacityReservationSummary.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this ComputeCapacityReservationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this ComputeCapacityReservationSummary.
        A user-friendly name for the capacity reservation. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My Reservation`


        :return: The display_name of this ComputeCapacityReservationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ComputeCapacityReservationSummary.
        A user-friendly name for the capacity reservation. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My Reservation`


        :param display_name: The display_name of this ComputeCapacityReservationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ComputeCapacityReservationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ComputeCapacityReservationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ComputeCapacityReservationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ComputeCapacityReservationSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ComputeCapacityReservationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ComputeCapacityReservationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ComputeCapacityReservationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ComputeCapacityReservationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ComputeCapacityReservationSummary.
        The current state of the capacity reservation.


        :return: The lifecycle_state of this ComputeCapacityReservationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ComputeCapacityReservationSummary.
        The current state of the capacity reservation.


        :param lifecycle_state: The lifecycle_state of this ComputeCapacityReservationSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this ComputeCapacityReservationSummary.
        The availability domain of the capacity reservation.


        :return: The availability_domain of this ComputeCapacityReservationSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ComputeCapacityReservationSummary.
        The availability domain of the capacity reservation.


        :param availability_domain: The availability_domain of this ComputeCapacityReservationSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def reserved_instance_count(self):
        """
        Gets the reserved_instance_count of this ComputeCapacityReservationSummary.
        The number of instances for which capacity will be held in this
        compute capacity reservation. This number is the sum of the values of the `reservedCount` fields
        for all of the instance reservation configurations under this reservation.
        The purpose of this field is to calculate the percentage usage of the reservation.


        :return: The reserved_instance_count of this ComputeCapacityReservationSummary.
        :rtype: int
        """
        return self._reserved_instance_count

    @reserved_instance_count.setter
    def reserved_instance_count(self, reserved_instance_count):
        """
        Sets the reserved_instance_count of this ComputeCapacityReservationSummary.
        The number of instances for which capacity will be held in this
        compute capacity reservation. This number is the sum of the values of the `reservedCount` fields
        for all of the instance reservation configurations under this reservation.
        The purpose of this field is to calculate the percentage usage of the reservation.


        :param reserved_instance_count: The reserved_instance_count of this ComputeCapacityReservationSummary.
        :type: int
        """
        self._reserved_instance_count = reserved_instance_count

    @property
    def used_instance_count(self):
        """
        Gets the used_instance_count of this ComputeCapacityReservationSummary.
        The total number of instances currently consuming space in
        this compute capacity reservation. This number is the sum of the values of the `usedCount` fields
        for all of the instance reservation configurations under this reservation.
        The purpose of this field is to calculate the percentage usage of the reservation.


        :return: The used_instance_count of this ComputeCapacityReservationSummary.
        :rtype: int
        """
        return self._used_instance_count

    @used_instance_count.setter
    def used_instance_count(self, used_instance_count):
        """
        Sets the used_instance_count of this ComputeCapacityReservationSummary.
        The total number of instances currently consuming space in
        this compute capacity reservation. This number is the sum of the values of the `usedCount` fields
        for all of the instance reservation configurations under this reservation.
        The purpose of this field is to calculate the percentage usage of the reservation.


        :param used_instance_count: The used_instance_count of this ComputeCapacityReservationSummary.
        :type: int
        """
        self._used_instance_count = used_instance_count

    @property
    def is_default_reservation(self):
        """
        Gets the is_default_reservation of this ComputeCapacityReservationSummary.
        Whether this capacity reservation is the default.
        For more information, see `Capacity Reservations`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default


        :return: The is_default_reservation of this ComputeCapacityReservationSummary.
        :rtype: bool
        """
        return self._is_default_reservation

    @is_default_reservation.setter
    def is_default_reservation(self, is_default_reservation):
        """
        Sets the is_default_reservation of this ComputeCapacityReservationSummary.
        Whether this capacity reservation is the default.
        For more information, see `Capacity Reservations`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default


        :param is_default_reservation: The is_default_reservation of this ComputeCapacityReservationSummary.
        :type: bool
        """
        self._is_default_reservation = is_default_reservation

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ComputeCapacityReservationSummary.
        The date and time the capacity reservation was created, in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ComputeCapacityReservationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ComputeCapacityReservationSummary.
        The date and time the capacity reservation was created, in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ComputeCapacityReservationSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
