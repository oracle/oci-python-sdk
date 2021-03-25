# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoAssociationState(object):
    """
    Auto association state of the source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutoAssociationState object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this AutoAssociationState.
        :type is_enabled: bool

        :param log_group_id:
            The value to assign to the log_group_id property of this AutoAssociationState.
        :type log_group_id: str

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'log_group_id': 'str'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'log_group_id': 'logGroupId'
        }

        self._is_enabled = None
        self._log_group_id = None

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this AutoAssociationState.
        A flag indicating whether or not auto association is enabled.


        :return: The is_enabled of this AutoAssociationState.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this AutoAssociationState.
        A flag indicating whether or not auto association is enabled.


        :param is_enabled: The is_enabled of this AutoAssociationState.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def log_group_id(self):
        """
        Gets the log_group_id of this AutoAssociationState.
        The unique identifier of the log group to use for auto association.


        :return: The log_group_id of this AutoAssociationState.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """
        Sets the log_group_id of this AutoAssociationState.
        The unique identifier of the log group to use for auto association.


        :param log_group_id: The log_group_id of this AutoAssociationState.
        :type: str
        """
        self._log_group_id = log_group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
