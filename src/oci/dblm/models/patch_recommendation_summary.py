# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240102


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchRecommendationSummary(object):
    """
    Total count summary of patch recommendations for databases.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PatchRecommendationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total:
            The value to assign to the total property of this PatchRecommendationSummary.
        :type total: int

        :param up_to_date:
            The value to assign to the up_to_date property of this PatchRecommendationSummary.
        :type up_to_date: int

        :param patch_available:
            The value to assign to the patch_available property of this PatchRecommendationSummary.
        :type patch_available: int

        """
        self.swagger_types = {
            'total': 'int',
            'up_to_date': 'int',
            'patch_available': 'int'
        }
        self.attribute_map = {
            'total': 'total',
            'up_to_date': 'upToDate',
            'patch_available': 'patchAvailable'
        }
        self._total = None
        self._up_to_date = None
        self._patch_available = None

    @property
    def total(self):
        """
        **[Required]** Gets the total of this PatchRecommendationSummary.
        Total number of databases pending to be updated and/or with latest patches.


        :return: The total of this PatchRecommendationSummary.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this PatchRecommendationSummary.
        Total number of databases pending to be updated and/or with latest patches.


        :param total: The total of this PatchRecommendationSummary.
        :type: int
        """
        self._total = total

    @property
    def up_to_date(self):
        """
        **[Required]** Gets the up_to_date of this PatchRecommendationSummary.
        Number of databases with latest patches.


        :return: The up_to_date of this PatchRecommendationSummary.
        :rtype: int
        """
        return self._up_to_date

    @up_to_date.setter
    def up_to_date(self, up_to_date):
        """
        Sets the up_to_date of this PatchRecommendationSummary.
        Number of databases with latest patches.


        :param up_to_date: The up_to_date of this PatchRecommendationSummary.
        :type: int
        """
        self._up_to_date = up_to_date

    @property
    def patch_available(self):
        """
        **[Required]** Gets the patch_available of this PatchRecommendationSummary.
        Number of databases pending to be updated.


        :return: The patch_available of this PatchRecommendationSummary.
        :rtype: int
        """
        return self._patch_available

    @patch_available.setter
    def patch_available(self, patch_available):
        """
        Sets the patch_available of this PatchRecommendationSummary.
        Number of databases pending to be updated.


        :param patch_available: The patch_available of this PatchRecommendationSummary.
        :type: int
        """
        self._patch_available = patch_available

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
