# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnterpriseManagerBridges(object):
    """
    Logical grouping used for Operations Insights Enterprise Manager Bridge operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnterpriseManagerBridges object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param enterprise_manager_bridges:
            The value to assign to the enterprise_manager_bridges property of this EnterpriseManagerBridges.
        :type enterprise_manager_bridges: object

        """
        self.swagger_types = {
            'enterprise_manager_bridges': 'object'
        }

        self.attribute_map = {
            'enterprise_manager_bridges': 'enterpriseManagerBridges'
        }

        self._enterprise_manager_bridges = None

    @property
    def enterprise_manager_bridges(self):
        """
        Gets the enterprise_manager_bridges of this EnterpriseManagerBridges.
        Enterprise Manager Bridge Object.


        :return: The enterprise_manager_bridges of this EnterpriseManagerBridges.
        :rtype: object
        """
        return self._enterprise_manager_bridges

    @enterprise_manager_bridges.setter
    def enterprise_manager_bridges(self, enterprise_manager_bridges):
        """
        Sets the enterprise_manager_bridges of this EnterpriseManagerBridges.
        Enterprise Manager Bridge Object.


        :param enterprise_manager_bridges: The enterprise_manager_bridges of this EnterpriseManagerBridges.
        :type: object
        """
        self._enterprise_manager_bridges = enterprise_manager_bridges

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
