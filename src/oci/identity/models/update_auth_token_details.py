# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAuthTokenDetails(object):
    """
    UpdateAuthTokenDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAuthTokenDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateAuthTokenDetails.
        :type description: str

        """
        self.swagger_types = {
            'description': 'str'
        }
        self.attribute_map = {
            'description': 'description'
        }
        self._description = None

    @property
    def description(self):
        """
        Gets the description of this UpdateAuthTokenDetails.
        The description you assign to the auth token. Does not have to be unique, and it's changeable.

        (For tenancies that support identity domains) You can have an empty description.


        :return: The description of this UpdateAuthTokenDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateAuthTokenDetails.
        The description you assign to the auth token. Does not have to be unique, and it's changeable.

        (For tenancies that support identity domains) You can have an empty description.


        :param description: The description of this UpdateAuthTokenDetails.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
