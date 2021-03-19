# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateComputeCapacityReservationDetails(object):
    """
    Details for updating the compute capacity reservation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateComputeCapacityReservationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateComputeCapacityReservationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateComputeCapacityReservationDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateComputeCapacityReservationDetails.
        :type freeform_tags: dict(str, str)

        :param is_default_reservation:
            The value to assign to the is_default_reservation property of this UpdateComputeCapacityReservationDetails.
        :type is_default_reservation: bool

        :param instance_reservation_configs:
            The value to assign to the instance_reservation_configs property of this UpdateComputeCapacityReservationDetails.
        :type instance_reservation_configs: list[oci.core.models.InstanceReservationConfigDetails]

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'is_default_reservation': 'bool',
            'instance_reservation_configs': 'list[InstanceReservationConfigDetails]'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'is_default_reservation': 'isDefaultReservation',
            'instance_reservation_configs': 'instanceReservationConfigs'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._is_default_reservation = None
        self._instance_reservation_configs = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateComputeCapacityReservationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateComputeCapacityReservationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateComputeCapacityReservationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateComputeCapacityReservationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateComputeCapacityReservationDetails.
        A user-friendly name for the compute capacity reservation. Does not have to be unique, and it's
        changeable. Avoid entering confidential information.


        :return: The display_name of this UpdateComputeCapacityReservationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateComputeCapacityReservationDetails.
        A user-friendly name for the compute capacity reservation. Does not have to be unique, and it's
        changeable. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateComputeCapacityReservationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateComputeCapacityReservationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateComputeCapacityReservationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateComputeCapacityReservationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateComputeCapacityReservationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def is_default_reservation(self):
        """
        Gets the is_default_reservation of this UpdateComputeCapacityReservationDetails.
        Whether this capacity reservation is the default.
        For more information, see `Capacity Reservations`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default


        :return: The is_default_reservation of this UpdateComputeCapacityReservationDetails.
        :rtype: bool
        """
        return self._is_default_reservation

    @is_default_reservation.setter
    def is_default_reservation(self, is_default_reservation):
        """
        Sets the is_default_reservation of this UpdateComputeCapacityReservationDetails.
        Whether this capacity reservation is the default.
        For more information, see `Capacity Reservations`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default


        :param is_default_reservation: The is_default_reservation of this UpdateComputeCapacityReservationDetails.
        :type: bool
        """
        self._is_default_reservation = is_default_reservation

    @property
    def instance_reservation_configs(self):
        """
        Gets the instance_reservation_configs of this UpdateComputeCapacityReservationDetails.
        The reservation configurations for the capacity reservation.

        To use the reservation for the desired shape, specify the shape, count, and
        optionally the fault domain where you want this configuration.


        :return: The instance_reservation_configs of this UpdateComputeCapacityReservationDetails.
        :rtype: list[oci.core.models.InstanceReservationConfigDetails]
        """
        return self._instance_reservation_configs

    @instance_reservation_configs.setter
    def instance_reservation_configs(self, instance_reservation_configs):
        """
        Sets the instance_reservation_configs of this UpdateComputeCapacityReservationDetails.
        The reservation configurations for the capacity reservation.

        To use the reservation for the desired shape, specify the shape, count, and
        optionally the fault domain where you want this configuration.


        :param instance_reservation_configs: The instance_reservation_configs of this UpdateComputeCapacityReservationDetails.
        :type: list[oci.core.models.InstanceReservationConfigDetails]
        """
        self._instance_reservation_configs = instance_reservation_configs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
