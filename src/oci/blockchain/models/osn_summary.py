# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OsnSummary(object):
    """
    OSN summary information for returning in a list.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OsnSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param osn_key:
            The value to assign to the osn_key property of this OsnSummary.
        :type osn_key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OsnSummary.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'osn_key': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'osn_key': 'osnKey',
            'lifecycle_state': 'lifecycleState'
        }

        self._osn_key = None
        self._lifecycle_state = None

    @property
    def osn_key(self):
        """
        Gets the osn_key of this OsnSummary.
        OSN identifier


        :return: The osn_key of this OsnSummary.
        :rtype: str
        """
        return self._osn_key

    @osn_key.setter
    def osn_key(self, osn_key):
        """
        Sets the osn_key of this OsnSummary.
        OSN identifier


        :param osn_key: The osn_key of this OsnSummary.
        :type: str
        """
        self._osn_key = osn_key

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OsnSummary.
        The current state of the OSN.


        :return: The lifecycle_state of this OsnSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OsnSummary.
        The current state of the OSN.


        :param lifecycle_state: The lifecycle_state of this OsnSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
