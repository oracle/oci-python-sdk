# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20170115

from .action import Action
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ForwardToBackendSet(Action):
    """
    Action to forward requests to a given backend set.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ForwardToBackendSet object with values from keyword arguments. The default value of the :py:attr:`~oci.load_balancer.models.ForwardToBackendSet.name` attribute
        of this class is ``FORWARD_TO_BACKENDSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ForwardToBackendSet.
            Allowed values for this property are: "FORWARD_TO_BACKENDSET"
        :type name: str

        :param backend_set_name:
            The value to assign to the backend_set_name property of this ForwardToBackendSet.
        :type backend_set_name: str

        """
        self.swagger_types = {
            'name': 'str',
            'backend_set_name': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'backend_set_name': 'backendSetName'
        }
        self._name = None
        self._backend_set_name = None
        self._name = 'FORWARD_TO_BACKENDSET'

    @property
    def backend_set_name(self):
        """
        **[Required]** Gets the backend_set_name of this ForwardToBackendSet.
        Name of the backend set the listener will forward the traffic to.

        Example: `backendSetForImages`


        :return: The backend_set_name of this ForwardToBackendSet.
        :rtype: str
        """
        return self._backend_set_name

    @backend_set_name.setter
    def backend_set_name(self, backend_set_name):
        """
        Sets the backend_set_name of this ForwardToBackendSet.
        Name of the backend set the listener will forward the traffic to.

        Example: `backendSetForImages`


        :param backend_set_name: The backend_set_name of this ForwardToBackendSet.
        :type: str
        """
        self._backend_set_name = backend_set_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
