# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpsiConfigurations(object):
    """
    An OPSI configuration resource is a container for storing custom values for customizable configuration items exposed by Operations Insights.

    Operations Insights exposes different sets of customizable configuration items through different OPSI configuration types.
    UX_CONFIGURATION: OPSI configuration resource of this type can be created only once in each compartment. It is a compartment level singleton resource.

    When configuration values, for an OPSI configuration type that supports compartment level singleton (e.g: UX_CONFIGURATION) resource, are queried for a compartment,
    following will be the order of preference.
    1. If the specified compartment has an OPSI configuration resource, first preference will be given to the custom values inside that.
    2. If the root compartment has an OPSI configuration resource, it will be considered as applicable to all compartments of that tenency,
    hence second preference will be given to the custom values inside that.
    3. Default configuration will be considered as a final fallback option.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OpsiConfigurations object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param opsi_configurations:
            The value to assign to the opsi_configurations property of this OpsiConfigurations.
        :type opsi_configurations: object

        """
        self.swagger_types = {
            'opsi_configurations': 'object'
        }

        self.attribute_map = {
            'opsi_configurations': 'opsiConfigurations'
        }

        self._opsi_configurations = None

    @property
    def opsi_configurations(self):
        """
        Gets the opsi_configurations of this OpsiConfigurations.
        OPSI Configuration Object.


        :return: The opsi_configurations of this OpsiConfigurations.
        :rtype: object
        """
        return self._opsi_configurations

    @opsi_configurations.setter
    def opsi_configurations(self, opsi_configurations):
        """
        Sets the opsi_configurations of this OpsiConfigurations.
        OPSI Configuration Object.


        :param opsi_configurations: The opsi_configurations of this OpsiConfigurations.
        :type: object
        """
        self._opsi_configurations = opsi_configurations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
