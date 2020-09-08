# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .action import Action
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StreamAction(Action):
    """
    Stream action for scheduled task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StreamAction object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.StreamAction.type` attribute
        of this class is ``STREAM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this StreamAction.
            Allowed values for this property are: "STREAM", "PURGE"
        :type type: str

        :param saved_search_id:
            The value to assign to the saved_search_id property of this StreamAction.
        :type saved_search_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'saved_search_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'saved_search_id': 'savedSearchId'
        }

        self._type = None
        self._saved_search_id = None
        self._type = 'STREAM'

    @property
    def saved_search_id(self):
        """
        Gets the saved_search_id of this StreamAction.
        The ManagementSavedSearch id [OCID] utilized in the action.


        :return: The saved_search_id of this StreamAction.
        :rtype: str
        """
        return self._saved_search_id

    @saved_search_id.setter
    def saved_search_id(self, saved_search_id):
        """
        Sets the saved_search_id of this StreamAction.
        The ManagementSavedSearch id [OCID] utilized in the action.


        :param saved_search_id: The saved_search_id of this StreamAction.
        :type: str
        """
        self._saved_search_id = saved_search_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
