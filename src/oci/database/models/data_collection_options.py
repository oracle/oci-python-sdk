# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataCollectionOptions(object):
    """
    Indicates user preferences for the various diagnostic collection options for the VM cluster/Cloud VM cluster/VMBM DBCS.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataCollectionOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_diagnostics_events_enabled:
            The value to assign to the is_diagnostics_events_enabled property of this DataCollectionOptions.
        :type is_diagnostics_events_enabled: bool

        """
        self.swagger_types = {
            'is_diagnostics_events_enabled': 'bool'
        }

        self.attribute_map = {
            'is_diagnostics_events_enabled': 'isDiagnosticsEventsEnabled'
        }

        self._is_diagnostics_events_enabled = None

    @property
    def is_diagnostics_events_enabled(self):
        """
        Gets the is_diagnostics_events_enabled of this DataCollectionOptions.
        Indicates whether diagnostic collection is enabled for the VM cluster/Cloud VM cluster/VMBM DBCS. Enabling diagnostic collection allows you to receive Events service notifications for guest VM issues. Diagnostic collection also allows Oracle to provide enhanced service and proactive support for your Exadata system. You can enable diagnostic collection during VM cluster/Cloud VM cluster provisioning. You can also disable or enable it at any time using the `UpdateVmCluster` or `updateCloudVmCluster` API.


        :return: The is_diagnostics_events_enabled of this DataCollectionOptions.
        :rtype: bool
        """
        return self._is_diagnostics_events_enabled

    @is_diagnostics_events_enabled.setter
    def is_diagnostics_events_enabled(self, is_diagnostics_events_enabled):
        """
        Sets the is_diagnostics_events_enabled of this DataCollectionOptions.
        Indicates whether diagnostic collection is enabled for the VM cluster/Cloud VM cluster/VMBM DBCS. Enabling diagnostic collection allows you to receive Events service notifications for guest VM issues. Diagnostic collection also allows Oracle to provide enhanced service and proactive support for your Exadata system. You can enable diagnostic collection during VM cluster/Cloud VM cluster provisioning. You can also disable or enable it at any time using the `UpdateVmCluster` or `updateCloudVmCluster` API.


        :param is_diagnostics_events_enabled: The is_diagnostics_events_enabled of this DataCollectionOptions.
        :type: bool
        """
        self._is_diagnostics_events_enabled = is_diagnostics_events_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
