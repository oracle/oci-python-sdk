# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningTaskReturn(object):
    """
    The returned object for starting or cloning a SQL tuning advisor task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningTaskReturn object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_tuning_task_id:
            The value to assign to the sql_tuning_task_id property of this SqlTuningTaskReturn.
        :type sql_tuning_task_id: int

        """
        self.swagger_types = {
            'sql_tuning_task_id': 'int'
        }

        self.attribute_map = {
            'sql_tuning_task_id': 'sqlTuningTaskId'
        }

        self._sql_tuning_task_id = None

    @property
    def sql_tuning_task_id(self):
        """
        **[Required]** Gets the sql_tuning_task_id of this SqlTuningTaskReturn.
        The identifier of the task being started or cloned. This is not the `OCID`__.
        It can be retrieved from the following endpoint
        :func:`list_sql_tuning_advisor_tasks`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The sql_tuning_task_id of this SqlTuningTaskReturn.
        :rtype: int
        """
        return self._sql_tuning_task_id

    @sql_tuning_task_id.setter
    def sql_tuning_task_id(self, sql_tuning_task_id):
        """
        Sets the sql_tuning_task_id of this SqlTuningTaskReturn.
        The identifier of the task being started or cloned. This is not the `OCID`__.
        It can be retrieved from the following endpoint
        :func:`list_sql_tuning_advisor_tasks`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param sql_tuning_task_id: The sql_tuning_task_id of this SqlTuningTaskReturn.
        :type: int
        """
        self._sql_tuning_task_id = sql_tuning_task_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
