# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverNodeSetKey(object):
    """
    Information about the success of setting a rover node's resource principal public key.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RoverNodeSetKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_successful:
            The value to assign to the is_successful property of this RoverNodeSetKey.
        :type is_successful: bool

        """
        self.swagger_types = {
            'is_successful': 'bool'
        }

        self.attribute_map = {
            'is_successful': 'isSuccessful'
        }

        self._is_successful = None

    @property
    def is_successful(self):
        """
        **[Required]** Gets the is_successful of this RoverNodeSetKey.
        Whether the node's resource principal public key was set correctly


        :return: The is_successful of this RoverNodeSetKey.
        :rtype: bool
        """
        return self._is_successful

    @is_successful.setter
    def is_successful(self, is_successful):
        """
        Sets the is_successful of this RoverNodeSetKey.
        Whether the node's resource principal public key was set correctly


        :param is_successful: The is_successful of this RoverNodeSetKey.
        :type: bool
        """
        self._is_successful = is_successful

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
