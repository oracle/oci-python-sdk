# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningAdvisorTaskFindingSummary(object):
    """
    A summary of the findings of the objects in a tuning task that match a given filter.
    This includes the kind of findings that were reported, whether the benefits were analyzed, and the number of benefits obtained.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningAdvisorTaskFindingSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_tuning_advisor_task_id:
            The value to assign to the sql_tuning_advisor_task_id property of this SqlTuningAdvisorTaskFindingSummary.
        :type sql_tuning_advisor_task_id: int

        :param sql_tuning_advisor_task_object_id:
            The value to assign to the sql_tuning_advisor_task_object_id property of this SqlTuningAdvisorTaskFindingSummary.
        :type sql_tuning_advisor_task_object_id: int

        :param sql_tuning_advisor_task_object_execution_id:
            The value to assign to the sql_tuning_advisor_task_object_execution_id property of this SqlTuningAdvisorTaskFindingSummary.
        :type sql_tuning_advisor_task_object_execution_id: int

        :param sql_text:
            The value to assign to the sql_text property of this SqlTuningAdvisorTaskFindingSummary.
        :type sql_text: str

        :param parsing_schema:
            The value to assign to the parsing_schema property of this SqlTuningAdvisorTaskFindingSummary.
        :type parsing_schema: str

        :param sql_key:
            The value to assign to the sql_key property of this SqlTuningAdvisorTaskFindingSummary.
        :type sql_key: str

        :param db_time_benefit:
            The value to assign to the db_time_benefit property of this SqlTuningAdvisorTaskFindingSummary.
        :type db_time_benefit: float

        :param per_execution_percentage:
            The value to assign to the per_execution_percentage property of this SqlTuningAdvisorTaskFindingSummary.
        :type per_execution_percentage: int

        :param is_stats_finding_present:
            The value to assign to the is_stats_finding_present property of this SqlTuningAdvisorTaskFindingSummary.
        :type is_stats_finding_present: bool

        :param is_sql_profile_finding_present:
            The value to assign to the is_sql_profile_finding_present property of this SqlTuningAdvisorTaskFindingSummary.
        :type is_sql_profile_finding_present: bool

        :param is_sql_profile_finding_implemented:
            The value to assign to the is_sql_profile_finding_implemented property of this SqlTuningAdvisorTaskFindingSummary.
        :type is_sql_profile_finding_implemented: bool

        :param is_index_finding_present:
            The value to assign to the is_index_finding_present property of this SqlTuningAdvisorTaskFindingSummary.
        :type is_index_finding_present: bool

        :param is_restructure_sql_finding_present:
            The value to assign to the is_restructure_sql_finding_present property of this SqlTuningAdvisorTaskFindingSummary.
        :type is_restructure_sql_finding_present: bool

        :param is_alternative_plan_finding_present:
            The value to assign to the is_alternative_plan_finding_present property of this SqlTuningAdvisorTaskFindingSummary.
        :type is_alternative_plan_finding_present: bool

        :param is_miscellaneous_finding_present:
            The value to assign to the is_miscellaneous_finding_present property of this SqlTuningAdvisorTaskFindingSummary.
        :type is_miscellaneous_finding_present: bool

        :param is_error_finding_present:
            The value to assign to the is_error_finding_present property of this SqlTuningAdvisorTaskFindingSummary.
        :type is_error_finding_present: bool

        :param is_timeout_finding_present:
            The value to assign to the is_timeout_finding_present property of this SqlTuningAdvisorTaskFindingSummary.
        :type is_timeout_finding_present: bool

        """
        self.swagger_types = {
            'sql_tuning_advisor_task_id': 'int',
            'sql_tuning_advisor_task_object_id': 'int',
            'sql_tuning_advisor_task_object_execution_id': 'int',
            'sql_text': 'str',
            'parsing_schema': 'str',
            'sql_key': 'str',
            'db_time_benefit': 'float',
            'per_execution_percentage': 'int',
            'is_stats_finding_present': 'bool',
            'is_sql_profile_finding_present': 'bool',
            'is_sql_profile_finding_implemented': 'bool',
            'is_index_finding_present': 'bool',
            'is_restructure_sql_finding_present': 'bool',
            'is_alternative_plan_finding_present': 'bool',
            'is_miscellaneous_finding_present': 'bool',
            'is_error_finding_present': 'bool',
            'is_timeout_finding_present': 'bool'
        }

        self.attribute_map = {
            'sql_tuning_advisor_task_id': 'sqlTuningAdvisorTaskId',
            'sql_tuning_advisor_task_object_id': 'sqlTuningAdvisorTaskObjectId',
            'sql_tuning_advisor_task_object_execution_id': 'sqlTuningAdvisorTaskObjectExecutionId',
            'sql_text': 'sqlText',
            'parsing_schema': 'parsingSchema',
            'sql_key': 'sqlKey',
            'db_time_benefit': 'dbTimeBenefit',
            'per_execution_percentage': 'perExecutionPercentage',
            'is_stats_finding_present': 'isStatsFindingPresent',
            'is_sql_profile_finding_present': 'isSqlProfileFindingPresent',
            'is_sql_profile_finding_implemented': 'isSqlProfileFindingImplemented',
            'is_index_finding_present': 'isIndexFindingPresent',
            'is_restructure_sql_finding_present': 'isRestructureSqlFindingPresent',
            'is_alternative_plan_finding_present': 'isAlternativePlanFindingPresent',
            'is_miscellaneous_finding_present': 'isMiscellaneousFindingPresent',
            'is_error_finding_present': 'isErrorFindingPresent',
            'is_timeout_finding_present': 'isTimeoutFindingPresent'
        }

        self._sql_tuning_advisor_task_id = None
        self._sql_tuning_advisor_task_object_id = None
        self._sql_tuning_advisor_task_object_execution_id = None
        self._sql_text = None
        self._parsing_schema = None
        self._sql_key = None
        self._db_time_benefit = None
        self._per_execution_percentage = None
        self._is_stats_finding_present = None
        self._is_sql_profile_finding_present = None
        self._is_sql_profile_finding_implemented = None
        self._is_index_finding_present = None
        self._is_restructure_sql_finding_present = None
        self._is_alternative_plan_finding_present = None
        self._is_miscellaneous_finding_present = None
        self._is_error_finding_present = None
        self._is_timeout_finding_present = None

    @property
    def sql_tuning_advisor_task_id(self):
        """
        **[Required]** Gets the sql_tuning_advisor_task_id of this SqlTuningAdvisorTaskFindingSummary.
        The unique identifier of the SQL Tuning Advisor task. This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The sql_tuning_advisor_task_id of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: int
        """
        return self._sql_tuning_advisor_task_id

    @sql_tuning_advisor_task_id.setter
    def sql_tuning_advisor_task_id(self, sql_tuning_advisor_task_id):
        """
        Sets the sql_tuning_advisor_task_id of this SqlTuningAdvisorTaskFindingSummary.
        The unique identifier of the SQL Tuning Advisor task. This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param sql_tuning_advisor_task_id: The sql_tuning_advisor_task_id of this SqlTuningAdvisorTaskFindingSummary.
        :type: int
        """
        self._sql_tuning_advisor_task_id = sql_tuning_advisor_task_id

    @property
    def sql_tuning_advisor_task_object_id(self):
        """
        **[Required]** Gets the sql_tuning_advisor_task_object_id of this SqlTuningAdvisorTaskFindingSummary.
        The key of the object to which these recommendations apply.
        This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The sql_tuning_advisor_task_object_id of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: int
        """
        return self._sql_tuning_advisor_task_object_id

    @sql_tuning_advisor_task_object_id.setter
    def sql_tuning_advisor_task_object_id(self, sql_tuning_advisor_task_object_id):
        """
        Sets the sql_tuning_advisor_task_object_id of this SqlTuningAdvisorTaskFindingSummary.
        The key of the object to which these recommendations apply.
        This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param sql_tuning_advisor_task_object_id: The sql_tuning_advisor_task_object_id of this SqlTuningAdvisorTaskFindingSummary.
        :type: int
        """
        self._sql_tuning_advisor_task_object_id = sql_tuning_advisor_task_object_id

    @property
    def sql_tuning_advisor_task_object_execution_id(self):
        """
        **[Required]** Gets the sql_tuning_advisor_task_object_execution_id of this SqlTuningAdvisorTaskFindingSummary.
        The execution id of the analyzed SQL object. This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The sql_tuning_advisor_task_object_execution_id of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: int
        """
        return self._sql_tuning_advisor_task_object_execution_id

    @sql_tuning_advisor_task_object_execution_id.setter
    def sql_tuning_advisor_task_object_execution_id(self, sql_tuning_advisor_task_object_execution_id):
        """
        Sets the sql_tuning_advisor_task_object_execution_id of this SqlTuningAdvisorTaskFindingSummary.
        The execution id of the analyzed SQL object. This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param sql_tuning_advisor_task_object_execution_id: The sql_tuning_advisor_task_object_execution_id of this SqlTuningAdvisorTaskFindingSummary.
        :type: int
        """
        self._sql_tuning_advisor_task_object_execution_id = sql_tuning_advisor_task_object_execution_id

    @property
    def sql_text(self):
        """
        **[Required]** Gets the sql_text of this SqlTuningAdvisorTaskFindingSummary.
        The text of the SQL statement.


        :return: The sql_text of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        """
        Sets the sql_text of this SqlTuningAdvisorTaskFindingSummary.
        The text of the SQL statement.


        :param sql_text: The sql_text of this SqlTuningAdvisorTaskFindingSummary.
        :type: str
        """
        self._sql_text = sql_text

    @property
    def parsing_schema(self):
        """
        **[Required]** Gets the parsing_schema of this SqlTuningAdvisorTaskFindingSummary.
        The parsing schema of the object.


        :return: The parsing_schema of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: str
        """
        return self._parsing_schema

    @parsing_schema.setter
    def parsing_schema(self, parsing_schema):
        """
        Sets the parsing_schema of this SqlTuningAdvisorTaskFindingSummary.
        The parsing schema of the object.


        :param parsing_schema: The parsing_schema of this SqlTuningAdvisorTaskFindingSummary.
        :type: str
        """
        self._parsing_schema = parsing_schema

    @property
    def sql_key(self):
        """
        **[Required]** Gets the sql_key of this SqlTuningAdvisorTaskFindingSummary.
        The unique key of this SQL statement.


        :return: The sql_key of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: str
        """
        return self._sql_key

    @sql_key.setter
    def sql_key(self, sql_key):
        """
        Sets the sql_key of this SqlTuningAdvisorTaskFindingSummary.
        The unique key of this SQL statement.


        :param sql_key: The sql_key of this SqlTuningAdvisorTaskFindingSummary.
        :type: str
        """
        self._sql_key = sql_key

    @property
    def db_time_benefit(self):
        """
        Gets the db_time_benefit of this SqlTuningAdvisorTaskFindingSummary.
        The time benefit (in seconds) for the highest-rated finding for this object.


        :return: The db_time_benefit of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: float
        """
        return self._db_time_benefit

    @db_time_benefit.setter
    def db_time_benefit(self, db_time_benefit):
        """
        Sets the db_time_benefit of this SqlTuningAdvisorTaskFindingSummary.
        The time benefit (in seconds) for the highest-rated finding for this object.


        :param db_time_benefit: The db_time_benefit of this SqlTuningAdvisorTaskFindingSummary.
        :type: float
        """
        self._db_time_benefit = db_time_benefit

    @property
    def per_execution_percentage(self):
        """
        Gets the per_execution_percentage of this SqlTuningAdvisorTaskFindingSummary.
        The per-execution percentage benefit.


        :return: The per_execution_percentage of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: int
        """
        return self._per_execution_percentage

    @per_execution_percentage.setter
    def per_execution_percentage(self, per_execution_percentage):
        """
        Sets the per_execution_percentage of this SqlTuningAdvisorTaskFindingSummary.
        The per-execution percentage benefit.


        :param per_execution_percentage: The per_execution_percentage of this SqlTuningAdvisorTaskFindingSummary.
        :type: int
        """
        self._per_execution_percentage = per_execution_percentage

    @property
    def is_stats_finding_present(self):
        """
        Gets the is_stats_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether a statistics recommendation was reported for this SQL statement.


        :return: The is_stats_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: bool
        """
        return self._is_stats_finding_present

    @is_stats_finding_present.setter
    def is_stats_finding_present(self, is_stats_finding_present):
        """
        Sets the is_stats_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether a statistics recommendation was reported for this SQL statement.


        :param is_stats_finding_present: The is_stats_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :type: bool
        """
        self._is_stats_finding_present = is_stats_finding_present

    @property
    def is_sql_profile_finding_present(self):
        """
        Gets the is_sql_profile_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether a SQL Profile recommendation was reported for this SQL statement.


        :return: The is_sql_profile_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: bool
        """
        return self._is_sql_profile_finding_present

    @is_sql_profile_finding_present.setter
    def is_sql_profile_finding_present(self, is_sql_profile_finding_present):
        """
        Sets the is_sql_profile_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether a SQL Profile recommendation was reported for this SQL statement.


        :param is_sql_profile_finding_present: The is_sql_profile_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :type: bool
        """
        self._is_sql_profile_finding_present = is_sql_profile_finding_present

    @property
    def is_sql_profile_finding_implemented(self):
        """
        Gets the is_sql_profile_finding_implemented of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether a SQL Profile recommendation has been implemented for this SQL statement.


        :return: The is_sql_profile_finding_implemented of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: bool
        """
        return self._is_sql_profile_finding_implemented

    @is_sql_profile_finding_implemented.setter
    def is_sql_profile_finding_implemented(self, is_sql_profile_finding_implemented):
        """
        Sets the is_sql_profile_finding_implemented of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether a SQL Profile recommendation has been implemented for this SQL statement.


        :param is_sql_profile_finding_implemented: The is_sql_profile_finding_implemented of this SqlTuningAdvisorTaskFindingSummary.
        :type: bool
        """
        self._is_sql_profile_finding_implemented = is_sql_profile_finding_implemented

    @property
    def is_index_finding_present(self):
        """
        Gets the is_index_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether an index recommendation was reported for this SQL statement.


        :return: The is_index_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: bool
        """
        return self._is_index_finding_present

    @is_index_finding_present.setter
    def is_index_finding_present(self, is_index_finding_present):
        """
        Sets the is_index_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether an index recommendation was reported for this SQL statement.


        :param is_index_finding_present: The is_index_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :type: bool
        """
        self._is_index_finding_present = is_index_finding_present

    @property
    def is_restructure_sql_finding_present(self):
        """
        Gets the is_restructure_sql_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether a restructure SQL recommendation was reported for this SQL statement.


        :return: The is_restructure_sql_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: bool
        """
        return self._is_restructure_sql_finding_present

    @is_restructure_sql_finding_present.setter
    def is_restructure_sql_finding_present(self, is_restructure_sql_finding_present):
        """
        Sets the is_restructure_sql_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether a restructure SQL recommendation was reported for this SQL statement.


        :param is_restructure_sql_finding_present: The is_restructure_sql_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :type: bool
        """
        self._is_restructure_sql_finding_present = is_restructure_sql_finding_present

    @property
    def is_alternative_plan_finding_present(self):
        """
        Gets the is_alternative_plan_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether an alternative execution plan was reported for this SQL statement.


        :return: The is_alternative_plan_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: bool
        """
        return self._is_alternative_plan_finding_present

    @is_alternative_plan_finding_present.setter
    def is_alternative_plan_finding_present(self, is_alternative_plan_finding_present):
        """
        Sets the is_alternative_plan_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether an alternative execution plan was reported for this SQL statement.


        :param is_alternative_plan_finding_present: The is_alternative_plan_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :type: bool
        """
        self._is_alternative_plan_finding_present = is_alternative_plan_finding_present

    @property
    def is_miscellaneous_finding_present(self):
        """
        Gets the is_miscellaneous_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether a miscellaneous finding was reported for this SQL statement.


        :return: The is_miscellaneous_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: bool
        """
        return self._is_miscellaneous_finding_present

    @is_miscellaneous_finding_present.setter
    def is_miscellaneous_finding_present(self, is_miscellaneous_finding_present):
        """
        Sets the is_miscellaneous_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether a miscellaneous finding was reported for this SQL statement.


        :param is_miscellaneous_finding_present: The is_miscellaneous_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :type: bool
        """
        self._is_miscellaneous_finding_present = is_miscellaneous_finding_present

    @property
    def is_error_finding_present(self):
        """
        Gets the is_error_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether there is an error in this SQL statement.


        :return: The is_error_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: bool
        """
        return self._is_error_finding_present

    @is_error_finding_present.setter
    def is_error_finding_present(self, is_error_finding_present):
        """
        Sets the is_error_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether there is an error in this SQL statement.


        :param is_error_finding_present: The is_error_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :type: bool
        """
        self._is_error_finding_present = is_error_finding_present

    @property
    def is_timeout_finding_present(self):
        """
        Gets the is_timeout_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether the task timed out.


        :return: The is_timeout_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :rtype: bool
        """
        return self._is_timeout_finding_present

    @is_timeout_finding_present.setter
    def is_timeout_finding_present(self, is_timeout_finding_present):
        """
        Sets the is_timeout_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        Indicates whether the task timed out.


        :param is_timeout_finding_present: The is_timeout_finding_present of this SqlTuningAdvisorTaskFindingSummary.
        :type: bool
        """
        self._is_timeout_finding_present = is_timeout_finding_present

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
