# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .backup_location import BackupLocation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupLocationURI(BackupLocation):
    """
    PreAuthenticated object storage URI to upload or download the backup
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BackupLocationURI object with values from keyword arguments. The default value of the :py:attr:`~oci.key_management.models.BackupLocationURI.destination` attribute
        of this class is ``PRE_AUTHENTICATED_REQUEST_URI`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination:
            The value to assign to the destination property of this BackupLocationURI.
            Allowed values for this property are: "BUCKET", "PRE_AUTHENTICATED_REQUEST_URI"
        :type destination: str

        :param uri:
            The value to assign to the uri property of this BackupLocationURI.
        :type uri: str

        """
        self.swagger_types = {
            'destination': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'destination': 'destination',
            'uri': 'uri'
        }

        self._destination = None
        self._uri = None
        self._destination = 'PRE_AUTHENTICATED_REQUEST_URI'

    @property
    def uri(self):
        """
        **[Required]** Gets the uri of this BackupLocationURI.

        :return: The uri of this BackupLocationURI.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this BackupLocationURI.

        :param uri: The uri of this BackupLocationURI.
        :type: str
        """
        self._uri = uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
