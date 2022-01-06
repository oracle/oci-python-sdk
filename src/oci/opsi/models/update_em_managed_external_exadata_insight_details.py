# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_exadata_insight_details import UpdateExadataInsightDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateEmManagedExternalExadataInsightDetails(UpdateExadataInsightDetails):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateEmManagedExternalExadataInsightDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.UpdateEmManagedExternalExadataInsightDetails.entity_source` attribute
        of this class is ``EM_MANAGED_EXTERNAL_EXADATA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this UpdateEmManagedExternalExadataInsightDetails.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_EXADATA"
        :type entity_source: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateEmManagedExternalExadataInsightDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateEmManagedExternalExadataInsightDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param is_auto_sync_enabled:
            The value to assign to the is_auto_sync_enabled property of this UpdateEmManagedExternalExadataInsightDetails.
        :type is_auto_sync_enabled: bool

        """
        self.swagger_types = {
            'entity_source': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_auto_sync_enabled': 'bool'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_auto_sync_enabled': 'isAutoSyncEnabled'
        }

        self._entity_source = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_auto_sync_enabled = None
        self._entity_source = 'EM_MANAGED_EXTERNAL_EXADATA'

    @property
    def is_auto_sync_enabled(self):
        """
        Gets the is_auto_sync_enabled of this UpdateEmManagedExternalExadataInsightDetails.
        Set to true to enable automatic enablement and disablement of related targets from Enterprise Manager. New resources (e.g. Database Insights) will be placed in the same compartment as the related Exadata Insight.


        :return: The is_auto_sync_enabled of this UpdateEmManagedExternalExadataInsightDetails.
        :rtype: bool
        """
        return self._is_auto_sync_enabled

    @is_auto_sync_enabled.setter
    def is_auto_sync_enabled(self, is_auto_sync_enabled):
        """
        Sets the is_auto_sync_enabled of this UpdateEmManagedExternalExadataInsightDetails.
        Set to true to enable automatic enablement and disablement of related targets from Enterprise Manager. New resources (e.g. Database Insights) will be placed in the same compartment as the related Exadata Insight.


        :param is_auto_sync_enabled: The is_auto_sync_enabled of this UpdateEmManagedExternalExadataInsightDetails.
        :type: bool
        """
        self._is_auto_sync_enabled = is_auto_sync_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
