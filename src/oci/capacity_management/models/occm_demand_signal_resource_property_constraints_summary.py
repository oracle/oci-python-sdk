# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OccmDemandSignalResourcePropertyConstraintsSummary(object):
    """
    A summary model for the Occm demand signal resource property constraints.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OccmDemandSignalResourcePropertyConstraintsSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param constraint_name:
            The value to assign to the constraint_name property of this OccmDemandSignalResourcePropertyConstraintsSummary.
        :type constraint_name: str

        :param constraint_value:
            The value to assign to the constraint_value property of this OccmDemandSignalResourcePropertyConstraintsSummary.
        :type constraint_value: str

        """
        self.swagger_types = {
            'constraint_name': 'str',
            'constraint_value': 'str'
        }
        self.attribute_map = {
            'constraint_name': 'constraintName',
            'constraint_value': 'constraintValue'
        }
        self._constraint_name = None
        self._constraint_value = None

    @property
    def constraint_name(self):
        """
        **[Required]** Gets the constraint_name of this OccmDemandSignalResourcePropertyConstraintsSummary.
        The name of demand signal resource's property constraint.


        :return: The constraint_name of this OccmDemandSignalResourcePropertyConstraintsSummary.
        :rtype: str
        """
        return self._constraint_name

    @constraint_name.setter
    def constraint_name(self, constraint_name):
        """
        Sets the constraint_name of this OccmDemandSignalResourcePropertyConstraintsSummary.
        The name of demand signal resource's property constraint.


        :param constraint_name: The constraint_name of this OccmDemandSignalResourcePropertyConstraintsSummary.
        :type: str
        """
        self._constraint_name = constraint_name

    @property
    def constraint_value(self):
        """
        **[Required]** Gets the constraint_value of this OccmDemandSignalResourcePropertyConstraintsSummary.
        The value of demand signal resource's property constraint.


        :return: The constraint_value of this OccmDemandSignalResourcePropertyConstraintsSummary.
        :rtype: str
        """
        return self._constraint_value

    @constraint_value.setter
    def constraint_value(self, constraint_value):
        """
        Sets the constraint_value of this OccmDemandSignalResourcePropertyConstraintsSummary.
        The value of demand signal resource's property constraint.


        :param constraint_value: The constraint_value of this OccmDemandSignalResourcePropertyConstraintsSummary.
        :type: str
        """
        self._constraint_value = constraint_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
