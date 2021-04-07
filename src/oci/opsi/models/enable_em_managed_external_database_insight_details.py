# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .enable_database_insight_details import EnableDatabaseInsightDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableEmManagedExternalDatabaseInsightDetails(EnableDatabaseInsightDetails):
    """
    The information about database to be analyzed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnableEmManagedExternalDatabaseInsightDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.EnableEmManagedExternalDatabaseInsightDetails.entity_source` attribute
        of this class is ``EM_MANAGED_EXTERNAL_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this EnableEmManagedExternalDatabaseInsightDetails.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_DATABASE"
        :type entity_source: str

        """
        self.swagger_types = {
            'entity_source': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource'
        }

        self._entity_source = None
        self._entity_source = 'EM_MANAGED_EXTERNAL_DATABASE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
