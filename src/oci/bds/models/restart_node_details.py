# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RestartNodeDetails(object):
    """
    The information about restarted node
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RestartNodeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param node_id:
            The value to assign to the node_id property of this RestartNodeDetails.
        :type node_id: str

        """
        self.swagger_types = {
            'node_id': 'str'
        }

        self.attribute_map = {
            'node_id': 'nodeId'
        }

        self._node_id = None

    @property
    def node_id(self):
        """
        **[Required]** Gets the node_id of this RestartNodeDetails.
        OCID of the BDS node which should be restarted


        :return: The node_id of this RestartNodeDetails.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this RestartNodeDetails.
        OCID of the BDS node which should be restarted


        :param node_id: The node_id of this RestartNodeDetails.
        :type: str
        """
        self._node_id = node_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
