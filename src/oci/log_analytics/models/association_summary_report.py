# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociationSummaryReport(object):
    """
    AssociationSummaryReport
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AssociationSummaryReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param association_count:
            The value to assign to the association_count property of this AssociationSummaryReport.
        :type association_count: int

        """
        self.swagger_types = {
            'association_count': 'int'
        }

        self.attribute_map = {
            'association_count': 'associationCount'
        }

        self._association_count = None

    @property
    def association_count(self):
        """
        Gets the association_count of this AssociationSummaryReport.
        association count


        :return: The association_count of this AssociationSummaryReport.
        :rtype: int
        """
        return self._association_count

    @association_count.setter
    def association_count(self, association_count):
        """
        Sets the association_count of this AssociationSummaryReport.
        association count


        :param association_count: The association_count of this AssociationSummaryReport.
        :type: int
        """
        self._association_count = association_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
