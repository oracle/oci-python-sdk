# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateSessionTokenDetails(object):
    """
    Information about the new session token.
    """

    #: A constant which can be used with the scopes property of a GenerateSessionTokenDetails.
    #: This constant has a value of "PLAYLIST"
    SCOPES_PLAYLIST = "PLAYLIST"

    #: A constant which can be used with the scopes property of a GenerateSessionTokenDetails.
    #: This constant has a value of "EDGE"
    SCOPES_EDGE = "EDGE"

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateSessionTokenDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_expires:
            The value to assign to the time_expires property of this GenerateSessionTokenDetails.
        :type time_expires: datetime

        :param scopes:
            The value to assign to the scopes property of this GenerateSessionTokenDetails.
            Allowed values for items in this list are: "PLAYLIST", "EDGE"
        :type scopes: list[str]

        :param packaging_config_id:
            The value to assign to the packaging_config_id property of this GenerateSessionTokenDetails.
        :type packaging_config_id: str

        :param asset_ids:
            The value to assign to the asset_ids property of this GenerateSessionTokenDetails.
        :type asset_ids: list[str]

        """
        self.swagger_types = {
            'time_expires': 'datetime',
            'scopes': 'list[str]',
            'packaging_config_id': 'str',
            'asset_ids': 'list[str]'
        }

        self.attribute_map = {
            'time_expires': 'timeExpires',
            'scopes': 'scopes',
            'packaging_config_id': 'packagingConfigId',
            'asset_ids': 'assetIds'
        }

        self._time_expires = None
        self._scopes = None
        self._packaging_config_id = None
        self._asset_ids = None

    @property
    def time_expires(self):
        """
        Gets the time_expires of this GenerateSessionTokenDetails.
        Token expiry time. An RFC3339 formatted datetime string.


        :return: The time_expires of this GenerateSessionTokenDetails.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this GenerateSessionTokenDetails.
        Token expiry time. An RFC3339 formatted datetime string.


        :param time_expires: The time_expires of this GenerateSessionTokenDetails.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def scopes(self):
        """
        **[Required]** Gets the scopes of this GenerateSessionTokenDetails.
        Array of scopes the token can act upon.

        Allowed values for items in this list are: "PLAYLIST", "EDGE"


        :return: The scopes of this GenerateSessionTokenDetails.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this GenerateSessionTokenDetails.
        Array of scopes the token can act upon.


        :param scopes: The scopes of this GenerateSessionTokenDetails.
        :type: list[str]
        """
        allowed_values = ["PLAYLIST", "EDGE"]

        if scopes and scopes is not NONE_SENTINEL:
            for value in scopes:
                if not value_allowed_none_or_none_sentinel(value, allowed_values):
                    raise ValueError(
                        "Invalid value for `scopes`, must be None or one of {0}"
                        .format(allowed_values)
                    )
        self._scopes = scopes

    @property
    def packaging_config_id(self):
        """
        **[Required]** Gets the packaging_config_id of this GenerateSessionTokenDetails.
        The packaging config resource identifier used to limit the scope of the token.


        :return: The packaging_config_id of this GenerateSessionTokenDetails.
        :rtype: str
        """
        return self._packaging_config_id

    @packaging_config_id.setter
    def packaging_config_id(self, packaging_config_id):
        """
        Sets the packaging_config_id of this GenerateSessionTokenDetails.
        The packaging config resource identifier used to limit the scope of the token.


        :param packaging_config_id: The packaging_config_id of this GenerateSessionTokenDetails.
        :type: str
        """
        self._packaging_config_id = packaging_config_id

    @property
    def asset_ids(self):
        """
        Gets the asset_ids of this GenerateSessionTokenDetails.
        Array of asset resource IDs used to limit the scope of the token.


        :return: The asset_ids of this GenerateSessionTokenDetails.
        :rtype: list[str]
        """
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, asset_ids):
        """
        Sets the asset_ids of this GenerateSessionTokenDetails.
        Array of asset resource IDs used to limit the scope of the token.


        :param asset_ids: The asset_ids of this GenerateSessionTokenDetails.
        :type: list[str]
        """
        self._asset_ids = asset_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
