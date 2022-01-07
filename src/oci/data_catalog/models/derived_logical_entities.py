# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DerivedLogicalEntities(object):
    """
    Entities derived from the application of a pattern to a list of file paths.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DerivedLogicalEntities object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DerivedLogicalEntities.
        :type name: str

        :param realized_expression:
            The value to assign to the realized_expression property of this DerivedLogicalEntities.
        :type realized_expression: str

        :param files_in_logical_grouping:
            The value to assign to the files_in_logical_grouping property of this DerivedLogicalEntities.
        :type files_in_logical_grouping: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'realized_expression': 'str',
            'files_in_logical_grouping': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'realized_expression': 'realizedExpression',
            'files_in_logical_grouping': 'filesInLogicalGrouping'
        }

        self._name = None
        self._realized_expression = None
        self._files_in_logical_grouping = None

    @property
    def name(self):
        """
        Gets the name of this DerivedLogicalEntities.
        The name of the derived logical entity. The group name of the unmatched files will be UNMATCHED


        :return: The name of this DerivedLogicalEntities.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DerivedLogicalEntities.
        The name of the derived logical entity. The group name of the unmatched files will be UNMATCHED


        :param name: The name of this DerivedLogicalEntities.
        :type: str
        """
        self._name = name

    @property
    def realized_expression(self):
        """
        Gets the realized_expression of this DerivedLogicalEntities.
        The expression realized after resolving qualifiers . Used in deriving this logical entity


        :return: The realized_expression of this DerivedLogicalEntities.
        :rtype: str
        """
        return self._realized_expression

    @realized_expression.setter
    def realized_expression(self, realized_expression):
        """
        Sets the realized_expression of this DerivedLogicalEntities.
        The expression realized after resolving qualifiers . Used in deriving this logical entity


        :param realized_expression: The realized_expression of this DerivedLogicalEntities.
        :type: str
        """
        self._realized_expression = realized_expression

    @property
    def files_in_logical_grouping(self):
        """
        Gets the files_in_logical_grouping of this DerivedLogicalEntities.
        The list of file paths that belong to the grouping of logical entity or UNMATCHED for which realizedExpression is a selector.


        :return: The files_in_logical_grouping of this DerivedLogicalEntities.
        :rtype: list[str]
        """
        return self._files_in_logical_grouping

    @files_in_logical_grouping.setter
    def files_in_logical_grouping(self, files_in_logical_grouping):
        """
        Sets the files_in_logical_grouping of this DerivedLogicalEntities.
        The list of file paths that belong to the grouping of logical entity or UNMATCHED for which realizedExpression is a selector.


        :param files_in_logical_grouping: The files_in_logical_grouping of this DerivedLogicalEntities.
        :type: list[str]
        """
        self._files_in_logical_grouping = files_in_logical_grouping

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
