# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAutonomousDatabaseWalletDetails(object):
    """
    Details to update an Autonomous Database wallet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAutonomousDatabaseWalletDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param should_rotate:
            The value to assign to the should_rotate property of this UpdateAutonomousDatabaseWalletDetails.
        :type should_rotate: bool

        :param grace_period:
            The value to assign to the grace_period property of this UpdateAutonomousDatabaseWalletDetails.
        :type grace_period: int

        """
        self.swagger_types = {
            'should_rotate': 'bool',
            'grace_period': 'int'
        }

        self.attribute_map = {
            'should_rotate': 'shouldRotate',
            'grace_period': 'gracePeriod'
        }

        self._should_rotate = None
        self._grace_period = None

    @property
    def should_rotate(self):
        """
        Gets the should_rotate of this UpdateAutonomousDatabaseWalletDetails.
        Indicates whether to rotate the wallet or not. If `false`, the wallet will not be rotated. The default is `false`.


        :return: The should_rotate of this UpdateAutonomousDatabaseWalletDetails.
        :rtype: bool
        """
        return self._should_rotate

    @should_rotate.setter
    def should_rotate(self, should_rotate):
        """
        Sets the should_rotate of this UpdateAutonomousDatabaseWalletDetails.
        Indicates whether to rotate the wallet or not. If `false`, the wallet will not be rotated. The default is `false`.


        :param should_rotate: The should_rotate of this UpdateAutonomousDatabaseWalletDetails.
        :type: bool
        """
        self._should_rotate = should_rotate

    @property
    def grace_period(self):
        """
        Gets the grace_period of this UpdateAutonomousDatabaseWalletDetails.
        Grace period in hours to keep the existing wallet valid after rotation.


        :return: The grace_period of this UpdateAutonomousDatabaseWalletDetails.
        :rtype: int
        """
        return self._grace_period

    @grace_period.setter
    def grace_period(self, grace_period):
        """
        Sets the grace_period of this UpdateAutonomousDatabaseWalletDetails.
        Grace period in hours to keep the existing wallet valid after rotation.


        :param grace_period: The grace_period of this UpdateAutonomousDatabaseWalletDetails.
        :type: int
        """
        self._grace_period = grace_period

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
