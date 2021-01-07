# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StateChange(object):
    """
    A container object for state change attributes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StateChange object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param previous:
            The value to assign to the previous property of this StateChange.
        :type previous: dict(str, object)

        :param current:
            The value to assign to the current property of this StateChange.
        :type current: dict(str, object)

        """
        self.swagger_types = {
            'previous': 'dict(str, object)',
            'current': 'dict(str, object)'
        }

        self.attribute_map = {
            'previous': 'previous',
            'current': 'current'
        }

        self._previous = None
        self._current = None

    @property
    def previous(self):
        """
        Gets the previous of this StateChange.
        Provides the previous state of fields that may have changed during an operation. To determine
        how the current operation changed a resource, compare the information in this attribute to
        `current`.


        :return: The previous of this StateChange.
        :rtype: dict(str, object)
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """
        Sets the previous of this StateChange.
        Provides the previous state of fields that may have changed during an operation. To determine
        how the current operation changed a resource, compare the information in this attribute to
        `current`.


        :param previous: The previous of this StateChange.
        :type: dict(str, object)
        """
        self._previous = previous

    @property
    def current(self):
        """
        Gets the current of this StateChange.
        Provides the current state of fields that may have changed during an operation. To determine
        how the current operation changed a resource, compare the information in this attribute to
        `previous`.


        :return: The current of this StateChange.
        :rtype: dict(str, object)
        """
        return self._current

    @current.setter
    def current(self, current):
        """
        Sets the current of this StateChange.
        Provides the current state of fields that may have changed during an operation. To determine
        how the current operation changed a resource, compare the information in this attribute to
        `previous`.


        :param current: The current of this StateChange.
        :type: dict(str, object)
        """
        self._current = current

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
