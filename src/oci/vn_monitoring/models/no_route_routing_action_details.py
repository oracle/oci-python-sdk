# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NoRouteRoutingActionDetails(object):
    """
    Defines the routing action taken on traffic flow with no route found.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NoRouteRoutingActionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_restricted_or_partial:
            The value to assign to the is_restricted_or_partial property of this NoRouteRoutingActionDetails.
        :type is_restricted_or_partial: bool

        :param evaluated_vcn_route_table_id:
            The value to assign to the evaluated_vcn_route_table_id property of this NoRouteRoutingActionDetails.
        :type evaluated_vcn_route_table_id: str

        :param evaluated_drg_route_table_id:
            The value to assign to the evaluated_drg_route_table_id property of this NoRouteRoutingActionDetails.
        :type evaluated_drg_route_table_id: str

        """
        self.swagger_types = {
            'is_restricted_or_partial': 'bool',
            'evaluated_vcn_route_table_id': 'str',
            'evaluated_drg_route_table_id': 'str'
        }

        self.attribute_map = {
            'is_restricted_or_partial': 'isRestrictedOrPartial',
            'evaluated_vcn_route_table_id': 'evaluatedVcnRouteTableId',
            'evaluated_drg_route_table_id': 'evaluatedDrgRouteTableId'
        }

        self._is_restricted_or_partial = None
        self._evaluated_vcn_route_table_id = None
        self._evaluated_drg_route_table_id = None

    @property
    def is_restricted_or_partial(self):
        """
        **[Required]** Gets the is_restricted_or_partial of this NoRouteRoutingActionDetails.
        If true, the evaluated route table details are incomplete.


        :return: The is_restricted_or_partial of this NoRouteRoutingActionDetails.
        :rtype: bool
        """
        return self._is_restricted_or_partial

    @is_restricted_or_partial.setter
    def is_restricted_or_partial(self, is_restricted_or_partial):
        """
        Sets the is_restricted_or_partial of this NoRouteRoutingActionDetails.
        If true, the evaluated route table details are incomplete.


        :param is_restricted_or_partial: The is_restricted_or_partial of this NoRouteRoutingActionDetails.
        :type: bool
        """
        self._is_restricted_or_partial = is_restricted_or_partial

    @property
    def evaluated_vcn_route_table_id(self):
        """
        Gets the evaluated_vcn_route_table_id of this NoRouteRoutingActionDetails.
        `OCIDs`__ of the evaluated VCN route table.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The evaluated_vcn_route_table_id of this NoRouteRoutingActionDetails.
        :rtype: str
        """
        return self._evaluated_vcn_route_table_id

    @evaluated_vcn_route_table_id.setter
    def evaluated_vcn_route_table_id(self, evaluated_vcn_route_table_id):
        """
        Sets the evaluated_vcn_route_table_id of this NoRouteRoutingActionDetails.
        `OCIDs`__ of the evaluated VCN route table.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param evaluated_vcn_route_table_id: The evaluated_vcn_route_table_id of this NoRouteRoutingActionDetails.
        :type: str
        """
        self._evaluated_vcn_route_table_id = evaluated_vcn_route_table_id

    @property
    def evaluated_drg_route_table_id(self):
        """
        Gets the evaluated_drg_route_table_id of this NoRouteRoutingActionDetails.
        `OCIDs`__ of evaluated DRG route table.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The evaluated_drg_route_table_id of this NoRouteRoutingActionDetails.
        :rtype: str
        """
        return self._evaluated_drg_route_table_id

    @evaluated_drg_route_table_id.setter
    def evaluated_drg_route_table_id(self, evaluated_drg_route_table_id):
        """
        Sets the evaluated_drg_route_table_id of this NoRouteRoutingActionDetails.
        `OCIDs`__ of evaluated DRG route table.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param evaluated_drg_route_table_id: The evaluated_drg_route_table_id of this NoRouteRoutingActionDetails.
        :type: str
        """
        self._evaluated_drg_route_table_id = evaluated_drg_route_table_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
