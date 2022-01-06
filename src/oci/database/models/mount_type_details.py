# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MountTypeDetails(object):
    """
    Mount type details for backup destination.
    """

    #: A constant which can be used with the mount_type property of a MountTypeDetails.
    #: This constant has a value of "SELF_MOUNT"
    MOUNT_TYPE_SELF_MOUNT = "SELF_MOUNT"

    #: A constant which can be used with the mount_type property of a MountTypeDetails.
    #: This constant has a value of "AUTOMATED_MOUNT"
    MOUNT_TYPE_AUTOMATED_MOUNT = "AUTOMATED_MOUNT"

    def __init__(self, **kwargs):
        """
        Initializes a new MountTypeDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.SelfMountDetails`
        * :class:`~oci.database.models.AutomatedMountDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mount_type:
            The value to assign to the mount_type property of this MountTypeDetails.
            Allowed values for this property are: "SELF_MOUNT", "AUTOMATED_MOUNT"
        :type mount_type: str

        """
        self.swagger_types = {
            'mount_type': 'str'
        }

        self.attribute_map = {
            'mount_type': 'mountType'
        }

        self._mount_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['mountType']

        if type == 'SELF_MOUNT':
            return 'SelfMountDetails'

        if type == 'AUTOMATED_MOUNT':
            return 'AutomatedMountDetails'
        else:
            return 'MountTypeDetails'

    @property
    def mount_type(self):
        """
        **[Required]** Gets the mount_type of this MountTypeDetails.
        Mount type for backup destination.

        Allowed values for this property are: "SELF_MOUNT", "AUTOMATED_MOUNT"


        :return: The mount_type of this MountTypeDetails.
        :rtype: str
        """
        return self._mount_type

    @mount_type.setter
    def mount_type(self, mount_type):
        """
        Sets the mount_type of this MountTypeDetails.
        Mount type for backup destination.


        :param mount_type: The mount_type of this MountTypeDetails.
        :type: str
        """
        allowed_values = ["SELF_MOUNT", "AUTOMATED_MOUNT"]
        if not value_allowed_none_or_none_sentinel(mount_type, allowed_values):
            raise ValueError(
                "Invalid value for `mount_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._mount_type = mount_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
