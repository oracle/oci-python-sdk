# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .drg_route_distribution_match_criteria import DrgRouteDistributionMatchCriteria
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrgAttachmentIdDrgRouteDistributionMatchCriteria(DrgRouteDistributionMatchCriteria):
    """
    The criteria by which a specific attachment will import routes to the DRG.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DrgAttachmentIdDrgRouteDistributionMatchCriteria object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.DrgAttachmentIdDrgRouteDistributionMatchCriteria.match_type` attribute
        of this class is ``DRG_ATTACHMENT_ID`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param match_type:
            The value to assign to the match_type property of this DrgAttachmentIdDrgRouteDistributionMatchCriteria.
            Allowed values for this property are: "DRG_ATTACHMENT_TYPE", "DRG_ATTACHMENT_ID"
        :type match_type: str

        :param drg_attachment_id:
            The value to assign to the drg_attachment_id property of this DrgAttachmentIdDrgRouteDistributionMatchCriteria.
        :type drg_attachment_id: str

        """
        self.swagger_types = {
            'match_type': 'str',
            'drg_attachment_id': 'str'
        }

        self.attribute_map = {
            'match_type': 'matchType',
            'drg_attachment_id': 'drgAttachmentId'
        }

        self._match_type = None
        self._drg_attachment_id = None
        self._match_type = 'DRG_ATTACHMENT_ID'

    @property
    def drg_attachment_id(self):
        """
        **[Required]** Gets the drg_attachment_id of this DrgAttachmentIdDrgRouteDistributionMatchCriteria.
        The `OCID`__ of the DRG attachment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The drg_attachment_id of this DrgAttachmentIdDrgRouteDistributionMatchCriteria.
        :rtype: str
        """
        return self._drg_attachment_id

    @drg_attachment_id.setter
    def drg_attachment_id(self, drg_attachment_id):
        """
        Sets the drg_attachment_id of this DrgAttachmentIdDrgRouteDistributionMatchCriteria.
        The `OCID`__ of the DRG attachment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param drg_attachment_id: The drg_attachment_id of this DrgAttachmentIdDrgRouteDistributionMatchCriteria.
        :type: str
        """
        self._drg_attachment_id = drg_attachment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
