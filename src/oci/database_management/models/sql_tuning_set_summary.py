# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningSetSummary(object):
    """
    The summary information of a SQL tuning set.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningSetSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SqlTuningSetSummary.
        :type name: str

        :param owner:
            The value to assign to the owner property of this SqlTuningSetSummary.
        :type owner: str

        :param description:
            The value to assign to the description property of this SqlTuningSetSummary.
        :type description: str

        :param statement_counts:
            The value to assign to the statement_counts property of this SqlTuningSetSummary.
        :type statement_counts: int

        """
        self.swagger_types = {
            'name': 'str',
            'owner': 'str',
            'description': 'str',
            'statement_counts': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'owner': 'owner',
            'description': 'description',
            'statement_counts': 'statementCounts'
        }

        self._name = None
        self._owner = None
        self._description = None
        self._statement_counts = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SqlTuningSetSummary.
        The name of the SQL tuning set.


        :return: The name of this SqlTuningSetSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SqlTuningSetSummary.
        The name of the SQL tuning set.


        :param name: The name of this SqlTuningSetSummary.
        :type: str
        """
        self._name = name

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this SqlTuningSetSummary.
        The owner of the SQL tuning set.


        :return: The owner of this SqlTuningSetSummary.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this SqlTuningSetSummary.
        The owner of the SQL tuning set.


        :param owner: The owner of this SqlTuningSetSummary.
        :type: str
        """
        self._owner = owner

    @property
    def description(self):
        """
        Gets the description of this SqlTuningSetSummary.
        The description of the SQL tuning set.


        :return: The description of this SqlTuningSetSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SqlTuningSetSummary.
        The description of the SQL tuning set.


        :param description: The description of this SqlTuningSetSummary.
        :type: str
        """
        self._description = description

    @property
    def statement_counts(self):
        """
        Gets the statement_counts of this SqlTuningSetSummary.
        The number of SQL statements in the SQL tuning set.


        :return: The statement_counts of this SqlTuningSetSummary.
        :rtype: int
        """
        return self._statement_counts

    @statement_counts.setter
    def statement_counts(self, statement_counts):
        """
        Sets the statement_counts of this SqlTuningSetSummary.
        The number of SQL statements in the SQL tuning set.


        :param statement_counts: The statement_counts of this SqlTuningSetSummary.
        :type: int
        """
        self._statement_counts = statement_counts

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
