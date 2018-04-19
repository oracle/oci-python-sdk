# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFileSystemDetails(object):
    """
    UpdateFileSystemDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFileSystemDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateFileSystemDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'display_name': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName'
        }

        self._display_name = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateFileSystemDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My file system`


        :return: The display_name of this UpdateFileSystemDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateFileSystemDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My file system`


        :param display_name: The display_name of this UpdateFileSystemDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
