# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .compute_instance_group_selector import ComputeInstanceGroupSelector
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceGroupByQuerySelector(ComputeInstanceGroupSelector):
    """
    Specifies the Compute instance group environment filtered by the RQS query expression.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceGroupByQuerySelector object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ComputeInstanceGroupByQuerySelector.selector_type` attribute
        of this class is ``INSTANCE_QUERY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param selector_type:
            The value to assign to the selector_type property of this ComputeInstanceGroupByQuerySelector.
            Allowed values for this property are: "INSTANCE_IDS", "INSTANCE_QUERY"
        :type selector_type: str

        :param region:
            The value to assign to the region property of this ComputeInstanceGroupByQuerySelector.
        :type region: str

        :param query:
            The value to assign to the query property of this ComputeInstanceGroupByQuerySelector.
        :type query: str

        """
        self.swagger_types = {
            'selector_type': 'str',
            'region': 'str',
            'query': 'str'
        }

        self.attribute_map = {
            'selector_type': 'selectorType',
            'region': 'region',
            'query': 'query'
        }

        self._selector_type = None
        self._region = None
        self._query = None
        self._selector_type = 'INSTANCE_QUERY'

    @property
    def region(self):
        """
        **[Required]** Gets the region of this ComputeInstanceGroupByQuerySelector.
        Region identifier referred by the deployment environment. Region identifiers are listed at https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm


        :return: The region of this ComputeInstanceGroupByQuerySelector.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this ComputeInstanceGroupByQuerySelector.
        Region identifier referred by the deployment environment. Region identifiers are listed at https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm


        :param region: The region of this ComputeInstanceGroupByQuerySelector.
        :type: str
        """
        self._region = region

    @property
    def query(self):
        """
        **[Required]** Gets the query of this ComputeInstanceGroupByQuerySelector.
        Query expression confirming to the OCI Search Language syntax to select compute instances for the group. The language is documented at https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm


        :return: The query of this ComputeInstanceGroupByQuerySelector.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this ComputeInstanceGroupByQuerySelector.
        Query expression confirming to the OCI Search Language syntax to select compute instances for the group. The language is documented at https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm


        :param query: The query of this ComputeInstanceGroupByQuerySelector.
        :type: str
        """
        self._query = query

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
