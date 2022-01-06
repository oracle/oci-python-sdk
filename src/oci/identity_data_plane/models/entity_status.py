# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntityStatus(object):
    """
    EntityStatus model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EntityStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this EntityStatus.
        :type status: str

        :param inactive_bit_mask:
            The value to assign to the inactive_bit_mask property of this EntityStatus.
        :type inactive_bit_mask: int

        """
        self.swagger_types = {
            'status': 'str',
            'inactive_bit_mask': 'int'
        }

        self.attribute_map = {
            'status': 'status',
            'inactive_bit_mask': 'inactiveBitMask'
        }

        self._status = None
        self._inactive_bit_mask = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this EntityStatus.
        The entity status.


        :return: The status of this EntityStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this EntityStatus.
        The entity status.


        :param status: The status of this EntityStatus.
        :type: str
        """
        self._status = status

    @property
    def inactive_bit_mask(self):
        """
        **[Required]** Gets the inactive_bit_mask of this EntityStatus.
        A bit mask showing the reason why the entity is inactive:
        - bit 0: ACTIVE
        - bit 1: SUSPENDED
        - bit 2: DISABLED
        - bit 3: BLOCKED
        - bit 4: LOCKED


        :return: The inactive_bit_mask of this EntityStatus.
        :rtype: int
        """
        return self._inactive_bit_mask

    @inactive_bit_mask.setter
    def inactive_bit_mask(self, inactive_bit_mask):
        """
        Sets the inactive_bit_mask of this EntityStatus.
        A bit mask showing the reason why the entity is inactive:
        - bit 0: ACTIVE
        - bit 1: SUSPENDED
        - bit 2: DISABLED
        - bit 3: BLOCKED
        - bit 4: LOCKED


        :param inactive_bit_mask: The inactive_bit_mask of this EntityStatus.
        :type: int
        """
        self._inactive_bit_mask = inactive_bit_mask

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
