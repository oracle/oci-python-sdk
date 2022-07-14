# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MediaWorkflowTaskState(object):
    """
    Status of a task in a workflow job being run.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MediaWorkflowTaskState object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this MediaWorkflowTaskState.
        :type key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MediaWorkflowTaskState.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MediaWorkflowTaskState.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'key': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._key = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def key(self):
        """
        Gets the key of this MediaWorkflowTaskState.
        Unique key within a MediaWorkflowJob for the task.


        :return: The key of this MediaWorkflowTaskState.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this MediaWorkflowTaskState.
        Unique key within a MediaWorkflowJob for the task.


        :param key: The key of this MediaWorkflowTaskState.
        :type: str
        """
        self._key = key

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MediaWorkflowTaskState.
        The current state of the MediaWorkflowJob task.


        :return: The lifecycle_state of this MediaWorkflowTaskState.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MediaWorkflowTaskState.
        The current state of the MediaWorkflowJob task.


        :param lifecycle_state: The lifecycle_state of this MediaWorkflowTaskState.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this MediaWorkflowTaskState.
        The lifecycle details of MediaWorkflowJob task.


        :return: The lifecycle_details of this MediaWorkflowTaskState.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this MediaWorkflowTaskState.
        The lifecycle details of MediaWorkflowJob task.


        :param lifecycle_details: The lifecycle_details of this MediaWorkflowTaskState.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
