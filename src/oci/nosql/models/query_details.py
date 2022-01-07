# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryDetails(object):
    """
    All the information surrounding a query, including the query statement,
    limits, consistency, and so forth.
    """

    #: A constant which can be used with the consistency property of a QueryDetails.
    #: This constant has a value of "EVENTUAL"
    CONSISTENCY_EVENTUAL = "EVENTUAL"

    #: A constant which can be used with the consistency property of a QueryDetails.
    #: This constant has a value of "ABSOLUTE"
    CONSISTENCY_ABSOLUTE = "ABSOLUTE"

    def __init__(self, **kwargs):
        """
        Initializes a new QueryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this QueryDetails.
        :type compartment_id: str

        :param statement:
            The value to assign to the statement property of this QueryDetails.
        :type statement: str

        :param is_prepared:
            The value to assign to the is_prepared property of this QueryDetails.
        :type is_prepared: bool

        :param consistency:
            The value to assign to the consistency property of this QueryDetails.
            Allowed values for this property are: "EVENTUAL", "ABSOLUTE"
        :type consistency: str

        :param max_read_in_k_bs:
            The value to assign to the max_read_in_k_bs property of this QueryDetails.
        :type max_read_in_k_bs: int

        :param variables:
            The value to assign to the variables property of this QueryDetails.
        :type variables: dict(str, object)

        :param timeout_in_ms:
            The value to assign to the timeout_in_ms property of this QueryDetails.
        :type timeout_in_ms: int

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'statement': 'str',
            'is_prepared': 'bool',
            'consistency': 'str',
            'max_read_in_k_bs': 'int',
            'variables': 'dict(str, object)',
            'timeout_in_ms': 'int'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'statement': 'statement',
            'is_prepared': 'isPrepared',
            'consistency': 'consistency',
            'max_read_in_k_bs': 'maxReadInKBs',
            'variables': 'variables',
            'timeout_in_ms': 'timeoutInMs'
        }

        self._compartment_id = None
        self._statement = None
        self._is_prepared = None
        self._consistency = None
        self._max_read_in_k_bs = None
        self._variables = None
        self._timeout_in_ms = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this QueryDetails.
        Compartment OCID, to provide context for a table name in
        the given statement.


        :return: The compartment_id of this QueryDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this QueryDetails.
        Compartment OCID, to provide context for a table name in
        the given statement.


        :param compartment_id: The compartment_id of this QueryDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def statement(self):
        """
        **[Required]** Gets the statement of this QueryDetails.
        A NoSQL SQL query statement; or a Base64-encoded prepared statement.


        :return: The statement of this QueryDetails.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """
        Sets the statement of this QueryDetails.
        A NoSQL SQL query statement; or a Base64-encoded prepared statement.


        :param statement: The statement of this QueryDetails.
        :type: str
        """
        self._statement = statement

    @property
    def is_prepared(self):
        """
        Gets the is_prepared of this QueryDetails.
        If true, the statement is a prepared statement.


        :return: The is_prepared of this QueryDetails.
        :rtype: bool
        """
        return self._is_prepared

    @is_prepared.setter
    def is_prepared(self, is_prepared):
        """
        Sets the is_prepared of this QueryDetails.
        If true, the statement is a prepared statement.


        :param is_prepared: The is_prepared of this QueryDetails.
        :type: bool
        """
        self._is_prepared = is_prepared

    @property
    def consistency(self):
        """
        Gets the consistency of this QueryDetails.
        Consistency requirement for a read operation.

        Allowed values for this property are: "EVENTUAL", "ABSOLUTE"


        :return: The consistency of this QueryDetails.
        :rtype: str
        """
        return self._consistency

    @consistency.setter
    def consistency(self, consistency):
        """
        Sets the consistency of this QueryDetails.
        Consistency requirement for a read operation.


        :param consistency: The consistency of this QueryDetails.
        :type: str
        """
        allowed_values = ["EVENTUAL", "ABSOLUTE"]
        if not value_allowed_none_or_none_sentinel(consistency, allowed_values):
            raise ValueError(
                "Invalid value for `consistency`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._consistency = consistency

    @property
    def max_read_in_k_bs(self):
        """
        Gets the max_read_in_k_bs of this QueryDetails.
        A limit on the total amount of data read during this operation, in KB.


        :return: The max_read_in_k_bs of this QueryDetails.
        :rtype: int
        """
        return self._max_read_in_k_bs

    @max_read_in_k_bs.setter
    def max_read_in_k_bs(self, max_read_in_k_bs):
        """
        Sets the max_read_in_k_bs of this QueryDetails.
        A limit on the total amount of data read during this operation, in KB.


        :param max_read_in_k_bs: The max_read_in_k_bs of this QueryDetails.
        :type: int
        """
        self._max_read_in_k_bs = max_read_in_k_bs

    @property
    def variables(self):
        """
        Gets the variables of this QueryDetails.
        A map of prepared statement variables to values.


        :return: The variables of this QueryDetails.
        :rtype: dict(str, object)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this QueryDetails.
        A map of prepared statement variables to values.


        :param variables: The variables of this QueryDetails.
        :type: dict(str, object)
        """
        self._variables = variables

    @property
    def timeout_in_ms(self):
        """
        Gets the timeout_in_ms of this QueryDetails.
        Timeout setting for the query.


        :return: The timeout_in_ms of this QueryDetails.
        :rtype: int
        """
        return self._timeout_in_ms

    @timeout_in_ms.setter
    def timeout_in_ms(self, timeout_in_ms):
        """
        Sets the timeout_in_ms of this QueryDetails.
        Timeout setting for the query.


        :param timeout_in_ms: The timeout_in_ms of this QueryDetails.
        :type: int
        """
        self._timeout_in_ms = timeout_in_ms

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
