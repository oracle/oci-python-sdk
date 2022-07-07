# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstancePowerActionDetails(object):
    """
    A base object for all types of instance power action requests.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstancePowerActionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.ResetActionDetails`
        * :class:`~oci.core.models.RebootMigrateActionDetails`
        * :class:`~oci.core.models.SoftResetActionDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this InstancePowerActionDetails.
        :type action_type: str

        """
        self.swagger_types = {
            'action_type': 'str'
        }

        self.attribute_map = {
            'action_type': 'actionType'
        }

        self._action_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['actionType']

        if type == 'reset':
            return 'ResetActionDetails'

        if type == 'rebootMigrate':
            return 'RebootMigrateActionDetails'

        if type == 'softreset':
            return 'SoftResetActionDetails'
        else:
            return 'InstancePowerActionDetails'

    @property
    def action_type(self):
        """
        **[Required]** Gets the action_type of this InstancePowerActionDetails.
        The type of power action to perform.


        :return: The action_type of this InstancePowerActionDetails.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this InstancePowerActionDetails.
        The type of power action to perform.


        :param action_type: The action_type of this InstancePowerActionDetails.
        :type: str
        """
        self._action_type = action_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
