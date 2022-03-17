# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_database_insight_details import UpdateDatabaseInsightDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateEmManagedExternalDatabaseInsightDetails(UpdateDatabaseInsightDetails):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateEmManagedExternalDatabaseInsightDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.UpdateEmManagedExternalDatabaseInsightDetails.entity_source` attribute
        of this class is ``EM_MANAGED_EXTERNAL_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this UpdateEmManagedExternalDatabaseInsightDetails.
            Allowed values for this property are: "AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"
        :type entity_source: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateEmManagedExternalDatabaseInsightDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateEmManagedExternalDatabaseInsightDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'entity_source': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._entity_source = None
        self._freeform_tags = None
        self._defined_tags = None
        self._entity_source = 'EM_MANAGED_EXTERNAL_DATABASE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
