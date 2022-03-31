# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .drg_route_distribution_match_criteria import DrgRouteDistributionMatchCriteria
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrgAttachmentMatchAllDrgRouteDistributionMatchCriteria(DrgRouteDistributionMatchCriteria):
    """
    All routes are imported or exported.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DrgAttachmentMatchAllDrgRouteDistributionMatchCriteria object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.DrgAttachmentMatchAllDrgRouteDistributionMatchCriteria.match_type` attribute
        of this class is ``MATCH_ALL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param match_type:
            The value to assign to the match_type property of this DrgAttachmentMatchAllDrgRouteDistributionMatchCriteria.
            Allowed values for this property are: "DRG_ATTACHMENT_TYPE", "DRG_ATTACHMENT_ID", "MATCH_ALL"
        :type match_type: str

        """
        self.swagger_types = {
            'match_type': 'str'
        }

        self.attribute_map = {
            'match_type': 'matchType'
        }

        self._match_type = None
        self._match_type = 'MATCH_ALL'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
