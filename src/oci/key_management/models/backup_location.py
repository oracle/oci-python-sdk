# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupLocation(object):
    """
    Backup upload location
    """

    #: A constant which can be used with the destination property of a BackupLocation.
    #: This constant has a value of "BUCKET"
    DESTINATION_BUCKET = "BUCKET"

    #: A constant which can be used with the destination property of a BackupLocation.
    #: This constant has a value of "PRE_AUTHENTICATED_REQUEST_URI"
    DESTINATION_PRE_AUTHENTICATED_REQUEST_URI = "PRE_AUTHENTICATED_REQUEST_URI"

    def __init__(self, **kwargs):
        """
        Initializes a new BackupLocation object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.key_management.models.BackupLocationBucket`
        * :class:`~oci.key_management.models.BackupLocationURI`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination:
            The value to assign to the destination property of this BackupLocation.
            Allowed values for this property are: "BUCKET", "PRE_AUTHENTICATED_REQUEST_URI"
        :type destination: str

        """
        self.swagger_types = {
            'destination': 'str'
        }

        self.attribute_map = {
            'destination': 'destination'
        }

        self._destination = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['destination']

        if type == 'BUCKET':
            return 'BackupLocationBucket'

        if type == 'PRE_AUTHENTICATED_REQUEST_URI':
            return 'BackupLocationURI'
        else:
            return 'BackupLocation'

    @property
    def destination(self):
        """
        **[Required]** Gets the destination of this BackupLocation.
        'Backup location destination:
        BUCKET - Uploading or downloading backup via object store bucket
        PRE_AUTHENTICATED_REQUEST_URI - Uploading or downloading backup via a PreAuthenticated object store URI'

        Allowed values for this property are: "BUCKET", "PRE_AUTHENTICATED_REQUEST_URI"


        :return: The destination of this BackupLocation.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this BackupLocation.
        'Backup location destination:
        BUCKET - Uploading or downloading backup via object store bucket
        PRE_AUTHENTICATED_REQUEST_URI - Uploading or downloading backup via a PreAuthenticated object store URI'


        :param destination: The destination of this BackupLocation.
        :type: str
        """
        allowed_values = ["BUCKET", "PRE_AUTHENTICATED_REQUEST_URI"]
        if not value_allowed_none_or_none_sentinel(destination, allowed_values):
            raise ValueError(
                "Invalid value for `destination`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._destination = destination

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
