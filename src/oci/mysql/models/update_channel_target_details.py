# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateChannelTargetDetails(object):
    """
    Parameters detailing how to provision the target for the given Channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateChannelTargetDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.mysql.models.UpdateChannelTargetFromDbSystemDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_type:
            The value to assign to the target_type property of this UpdateChannelTargetDetails.
        :type target_type: str

        """
        self.swagger_types = {
            'target_type': 'str'
        }

        self.attribute_map = {
            'target_type': 'targetType'
        }

        self._target_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['targetType']

        if type == 'DBSYSTEM':
            return 'UpdateChannelTargetFromDbSystemDetails'
        else:
            return 'UpdateChannelTargetDetails'

    @property
    def target_type(self):
        """
        **[Required]** Gets the target_type of this UpdateChannelTargetDetails.
        The specific targetType identifier.


        :return: The target_type of this UpdateChannelTargetDetails.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """
        Sets the target_type of this UpdateChannelTargetDetails.
        The specific targetType identifier.


        :param target_type: The target_type of this UpdateChannelTargetDetails.
        :type: str
        """
        self._target_type = target_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
