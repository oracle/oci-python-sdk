# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningTaskSqlDetail(object):
    """
    The details of the SQL statements on which SQL tuning is performed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningTaskSqlDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_id:
            The value to assign to the sql_id property of this SqlTuningTaskSqlDetail.
        :type sql_id: str

        """
        self.swagger_types = {
            'sql_id': 'str'
        }

        self.attribute_map = {
            'sql_id': 'sqlId'
        }

        self._sql_id = None

    @property
    def sql_id(self):
        """
        **[Required]** Gets the sql_id of this SqlTuningTaskSqlDetail.
        The identifier of a SQL statement.


        :return: The sql_id of this SqlTuningTaskSqlDetail.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        """
        Sets the sql_id of this SqlTuningTaskSqlDetail.
        The identifier of a SQL statement.


        :param sql_id: The sql_id of this SqlTuningTaskSqlDetail.
        :type: str
        """
        self._sql_id = sql_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
