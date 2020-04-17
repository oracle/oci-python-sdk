# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActionDetailsList(object):
    """
    A list of ActionDetails objects to create for a rule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ActionDetailsList object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param actions:
            The value to assign to the actions property of this ActionDetailsList.
        :type actions: list[ActionDetails]

        """
        self.swagger_types = {
            'actions': 'list[ActionDetails]'
        }

        self.attribute_map = {
            'actions': 'actions'
        }

        self._actions = None

    @property
    def actions(self):
        """
        **[Required]** Gets the actions of this ActionDetailsList.
        A list of one or more ActionDetails objects.


        :return: The actions of this ActionDetailsList.
        :rtype: list[ActionDetails]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this ActionDetailsList.
        A list of one or more ActionDetails objects.


        :param actions: The actions of this ActionDetailsList.
        :type: list[ActionDetails]
        """
        self._actions = actions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
