# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlText(object):
    """
    SQL Text type object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlText object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this SqlText.
        :type version: float

        :param sql_identifier:
            The value to assign to the sql_identifier property of this SqlText.
        :type sql_identifier: str

        :param time_collected:
            The value to assign to the time_collected property of this SqlText.
        :type time_collected: datetime

        :param sql_command:
            The value to assign to the sql_command property of this SqlText.
        :type sql_command: str

        :param exact_matching_signature:
            The value to assign to the exact_matching_signature property of this SqlText.
        :type exact_matching_signature: str

        :param force_matching_signature:
            The value to assign to the force_matching_signature property of this SqlText.
        :type force_matching_signature: str

        :param sql_full_text:
            The value to assign to the sql_full_text property of this SqlText.
        :type sql_full_text: str

        """
        self.swagger_types = {
            'version': 'float',
            'sql_identifier': 'str',
            'time_collected': 'datetime',
            'sql_command': 'str',
            'exact_matching_signature': 'str',
            'force_matching_signature': 'str',
            'sql_full_text': 'str'
        }

        self.attribute_map = {
            'version': 'version',
            'sql_identifier': 'sqlIdentifier',
            'time_collected': 'timeCollected',
            'sql_command': 'sqlCommand',
            'exact_matching_signature': 'exactMatchingSignature',
            'force_matching_signature': 'forceMatchingSignature',
            'sql_full_text': 'sqlFullText'
        }

        self._version = None
        self._sql_identifier = None
        self._time_collected = None
        self._sql_command = None
        self._exact_matching_signature = None
        self._force_matching_signature = None
        self._sql_full_text = None

    @property
    def version(self):
        """
        Gets the version of this SqlText.
        Version
        Example: `1`


        :return: The version of this SqlText.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SqlText.
        Version
        Example: `1`


        :param version: The version of this SqlText.
        :type: float
        """
        self._version = version

    @property
    def sql_identifier(self):
        """
        **[Required]** Gets the sql_identifier of this SqlText.
        Unique SQL_ID for a SQL Statement.


        :return: The sql_identifier of this SqlText.
        :rtype: str
        """
        return self._sql_identifier

    @sql_identifier.setter
    def sql_identifier(self, sql_identifier):
        """
        Sets the sql_identifier of this SqlText.
        Unique SQL_ID for a SQL Statement.


        :param sql_identifier: The sql_identifier of this SqlText.
        :type: str
        """
        self._sql_identifier = sql_identifier

    @property
    def time_collected(self):
        """
        **[Required]** Gets the time_collected of this SqlText.
        Collection timestamp
        Example: `\"2020-05-06T00:00:00.000Z\"`


        :return: The time_collected of this SqlText.
        :rtype: datetime
        """
        return self._time_collected

    @time_collected.setter
    def time_collected(self, time_collected):
        """
        Sets the time_collected of this SqlText.
        Collection timestamp
        Example: `\"2020-05-06T00:00:00.000Z\"`


        :param time_collected: The time_collected of this SqlText.
        :type: datetime
        """
        self._time_collected = time_collected

    @property
    def sql_command(self):
        """
        **[Required]** Gets the sql_command of this SqlText.
        SQL command
        Example: `\"SELECT\"`


        :return: The sql_command of this SqlText.
        :rtype: str
        """
        return self._sql_command

    @sql_command.setter
    def sql_command(self, sql_command):
        """
        Sets the sql_command of this SqlText.
        SQL command
        Example: `\"SELECT\"`


        :param sql_command: The sql_command of this SqlText.
        :type: str
        """
        self._sql_command = sql_command

    @property
    def exact_matching_signature(self):
        """
        Gets the exact_matching_signature of this SqlText.
        Exact matching signature
        Example: `\"18067345456756876713\"`


        :return: The exact_matching_signature of this SqlText.
        :rtype: str
        """
        return self._exact_matching_signature

    @exact_matching_signature.setter
    def exact_matching_signature(self, exact_matching_signature):
        """
        Sets the exact_matching_signature of this SqlText.
        Exact matching signature
        Example: `\"18067345456756876713\"`


        :param exact_matching_signature: The exact_matching_signature of this SqlText.
        :type: str
        """
        self._exact_matching_signature = exact_matching_signature

    @property
    def force_matching_signature(self):
        """
        Gets the force_matching_signature of this SqlText.
        Force matching signature
        Example: `\"18067345456756876713\"`


        :return: The force_matching_signature of this SqlText.
        :rtype: str
        """
        return self._force_matching_signature

    @force_matching_signature.setter
    def force_matching_signature(self, force_matching_signature):
        """
        Sets the force_matching_signature of this SqlText.
        Force matching signature
        Example: `\"18067345456756876713\"`


        :param force_matching_signature: The force_matching_signature of this SqlText.
        :type: str
        """
        self._force_matching_signature = force_matching_signature

    @property
    def sql_full_text(self):
        """
        **[Required]** Gets the sql_full_text of this SqlText.
        Full SQL Text
        Example: `\"SELECT username,profile,default_tablespace,temporary_tablespace FROM dba_users\"`
        Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should be masked prior to ingestion.


        :return: The sql_full_text of this SqlText.
        :rtype: str
        """
        return self._sql_full_text

    @sql_full_text.setter
    def sql_full_text(self, sql_full_text):
        """
        Sets the sql_full_text of this SqlText.
        Full SQL Text
        Example: `\"SELECT username,profile,default_tablespace,temporary_tablespace FROM dba_users\"`
        Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should be masked prior to ingestion.


        :param sql_full_text: The sql_full_text of this SqlText.
        :type: str
        """
        self._sql_full_text = sql_full_text

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
