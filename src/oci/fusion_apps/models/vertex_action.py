# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .action import Action
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VertexAction(Action):
    """
    Vertex update action
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VertexAction object with values from keyword arguments. The default value of the :py:attr:`~oci.fusion_apps.models.VertexAction.action_type` attribute
        of this class is ``VERTEX`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reference_key:
            The value to assign to the reference_key property of this VertexAction.
        :type reference_key: str

        :param action_type:
            The value to assign to the action_type property of this VertexAction.
            Allowed values for this property are: "QUARTERLY_UPGRADE", "PATCH", "VERTEX"
        :type action_type: str

        :param state:
            The value to assign to the state property of this VertexAction.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED"
        :type state: str

        :param description:
            The value to assign to the description property of this VertexAction.
        :type description: str

        :param artifact:
            The value to assign to the artifact property of this VertexAction.
        :type artifact: str

        """
        self.swagger_types = {
            'reference_key': 'str',
            'action_type': 'str',
            'state': 'str',
            'description': 'str',
            'artifact': 'str'
        }

        self.attribute_map = {
            'reference_key': 'referenceKey',
            'action_type': 'actionType',
            'state': 'state',
            'description': 'description',
            'artifact': 'artifact'
        }

        self._reference_key = None
        self._action_type = None
        self._state = None
        self._description = None
        self._artifact = None
        self._action_type = 'VERTEX'

    @property
    def artifact(self):
        """
        Gets the artifact of this VertexAction.
        patch that delivered the vertex update prerequisite


        :return: The artifact of this VertexAction.
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """
        Sets the artifact of this VertexAction.
        patch that delivered the vertex update prerequisite


        :param artifact: The artifact of this VertexAction.
        :type: str
        """
        self._artifact = artifact

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
