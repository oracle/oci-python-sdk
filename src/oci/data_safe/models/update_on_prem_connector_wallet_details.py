# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOnPremConnectorWalletDetails(object):
    """
    The details used to update an on-premises connector's wallet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOnPremConnectorWalletDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_update:
            The value to assign to the is_update property of this UpdateOnPremConnectorWalletDetails.
        :type is_update: bool

        """
        self.swagger_types = {
            'is_update': 'bool'
        }

        self.attribute_map = {
            'is_update': 'isUpdate'
        }

        self._is_update = None

    @property
    def is_update(self):
        """
        Gets the is_update of this UpdateOnPremConnectorWalletDetails.
        Indicates whether to update or not. If false, the wallet will not be updated. Default is false.


        :return: The is_update of this UpdateOnPremConnectorWalletDetails.
        :rtype: bool
        """
        return self._is_update

    @is_update.setter
    def is_update(self, is_update):
        """
        Sets the is_update of this UpdateOnPremConnectorWalletDetails.
        Indicates whether to update or not. If false, the wallet will not be updated. Default is false.


        :param is_update: The is_update of this UpdateOnPremConnectorWalletDetails.
        :type: bool
        """
        self._is_update = is_update

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
