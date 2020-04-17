# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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

        """
        self.swagger_types = {
            'should_rotate': 'bool'
        }

        self.attribute_map = {
            'should_rotate': 'shouldRotate'
        }

        self._should_rotate = None

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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
