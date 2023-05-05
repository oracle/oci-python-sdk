# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DownloadOneoffPatch(object):
    """
    Data to download one-off patch.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DownloadOneoffPatch object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param access_uri:
            The value to assign to the access_uri property of this DownloadOneoffPatch.
        :type access_uri: str

        :param time_created:
            The value to assign to the time_created property of this DownloadOneoffPatch.
        :type time_created: datetime

        :param time_expires:
            The value to assign to the time_expires property of this DownloadOneoffPatch.
        :type time_expires: datetime

        """
        self.swagger_types = {
            'access_uri': 'str',
            'time_created': 'datetime',
            'time_expires': 'datetime'
        }

        self.attribute_map = {
            'access_uri': 'accessUri',
            'time_created': 'timeCreated',
            'time_expires': 'timeExpires'
        }

        self._access_uri = None
        self._time_created = None
        self._time_expires = None

    @property
    def access_uri(self):
        """
        **[Required]** Gets the access_uri of this DownloadOneoffPatch.
        URI to download one-off patch.


        :return: The access_uri of this DownloadOneoffPatch.
        :rtype: str
        """
        return self._access_uri

    @access_uri.setter
    def access_uri(self, access_uri):
        """
        Sets the access_uri of this DownloadOneoffPatch.
        URI to download one-off patch.


        :param access_uri: The access_uri of this DownloadOneoffPatch.
        :type: str
        """
        self._access_uri = access_uri

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DownloadOneoffPatch.
        The date and time one-off patch URI was created.


        :return: The time_created of this DownloadOneoffPatch.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DownloadOneoffPatch.
        The date and time one-off patch URI was created.


        :param time_created: The time_created of this DownloadOneoffPatch.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_expires(self):
        """
        **[Required]** Gets the time_expires of this DownloadOneoffPatch.
        The date and time until which the one-off patch URI will be available for download.


        :return: The time_expires of this DownloadOneoffPatch.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this DownloadOneoffPatch.
        The date and time until which the one-off patch URI will be available for download.


        :param time_expires: The time_expires of this DownloadOneoffPatch.
        :type: datetime
        """
        self._time_expires = time_expires

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
