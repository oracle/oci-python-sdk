# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationAttachVolumeDetails(object):
    """
    Volume attachmentDetails. Please see :class:`AttachVolumeDetails`
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationAttachVolumeDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.InstanceConfigurationIscsiAttachVolumeDetails`
        * :class:`~oci.core.models.InstanceConfigurationParavirtualizedAttachVolumeDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this InstanceConfigurationAttachVolumeDetails.
        :type display_name: str

        :param is_read_only:
            The value to assign to the is_read_only property of this InstanceConfigurationAttachVolumeDetails.
        :type is_read_only: bool

        :param type:
            The value to assign to the type property of this InstanceConfigurationAttachVolumeDetails.
        :type type: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'is_read_only': 'bool',
            'type': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'is_read_only': 'isReadOnly',
            'type': 'type'
        }

        self._display_name = None
        self._is_read_only = None
        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'iscsi':
            return 'InstanceConfigurationIscsiAttachVolumeDetails'

        if type == 'paravirtualized':
            return 'InstanceConfigurationParavirtualizedAttachVolumeDetails'
        else:
            return 'InstanceConfigurationAttachVolumeDetails'

    @property
    def display_name(self):
        """
        Gets the display_name of this InstanceConfigurationAttachVolumeDetails.
        A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.


        :return: The display_name of this InstanceConfigurationAttachVolumeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstanceConfigurationAttachVolumeDetails.
        A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.


        :param display_name: The display_name of this InstanceConfigurationAttachVolumeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_read_only(self):
        """
        Gets the is_read_only of this InstanceConfigurationAttachVolumeDetails.
        Whether the attachment should be created in read-only mode.


        :return: The is_read_only of this InstanceConfigurationAttachVolumeDetails.
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """
        Sets the is_read_only of this InstanceConfigurationAttachVolumeDetails.
        Whether the attachment should be created in read-only mode.


        :param is_read_only: The is_read_only of this InstanceConfigurationAttachVolumeDetails.
        :type: bool
        """
        self._is_read_only = is_read_only

    @property
    def type(self):
        """
        **[Required]** Gets the type of this InstanceConfigurationAttachVolumeDetails.
        The type of volume. The only supported values are \"iscsi\" and \"paravirtualized\".


        :return: The type of this InstanceConfigurationAttachVolumeDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this InstanceConfigurationAttachVolumeDetails.
        The type of volume. The only supported values are \"iscsi\" and \"paravirtualized\".


        :param type: The type of this InstanceConfigurationAttachVolumeDetails.
        :type: str
        """
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
