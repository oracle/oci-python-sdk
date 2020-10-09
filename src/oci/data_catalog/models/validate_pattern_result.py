# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidatePatternResult(object):
    """
    Details regarding the validation of a pattern resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValidatePatternResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message:
            The value to assign to the message property of this ValidatePatternResult.
        :type message: str

        :param status:
            The value to assign to the status property of this ValidatePatternResult.
        :type status: str

        :param expression:
            The value to assign to the expression property of this ValidatePatternResult.
        :type expression: str

        :param derived_logical_entities:
            The value to assign to the derived_logical_entities property of this ValidatePatternResult.
        :type derived_logical_entities: list[DerivedLogicalEntities]

        """
        self.swagger_types = {
            'message': 'str',
            'status': 'str',
            'expression': 'str',
            'derived_logical_entities': 'list[DerivedLogicalEntities]'
        }

        self.attribute_map = {
            'message': 'message',
            'status': 'status',
            'expression': 'expression',
            'derived_logical_entities': 'derivedLogicalEntities'
        }

        self._message = None
        self._status = None
        self._expression = None
        self._derived_logical_entities = None

    @property
    def message(self):
        """
        Gets the message of this ValidatePatternResult.
        The message from the pattern validation.


        :return: The message of this ValidatePatternResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ValidatePatternResult.
        The message from the pattern validation.


        :param message: The message of this ValidatePatternResult.
        :type: str
        """
        self._message = message

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ValidatePatternResult.
        The status returned from the pattern validation.


        :return: The status of this ValidatePatternResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ValidatePatternResult.
        The status returned from the pattern validation.


        :param status: The status of this ValidatePatternResult.
        :type: str
        """
        self._status = status

    @property
    def expression(self):
        """
        Gets the expression of this ValidatePatternResult.
        The expression used in the pattern validation.


        :return: The expression of this ValidatePatternResult.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this ValidatePatternResult.
        The expression used in the pattern validation.


        :param expression: The expression of this ValidatePatternResult.
        :type: str
        """
        self._expression = expression

    @property
    def derived_logical_entities(self):
        """
        Gets the derived_logical_entities of this ValidatePatternResult.
        Collection of logical entities derived from the expression applied to a list of file paths.


        :return: The derived_logical_entities of this ValidatePatternResult.
        :rtype: list[DerivedLogicalEntities]
        """
        return self._derived_logical_entities

    @derived_logical_entities.setter
    def derived_logical_entities(self, derived_logical_entities):
        """
        Sets the derived_logical_entities of this ValidatePatternResult.
        Collection of logical entities derived from the expression applied to a list of file paths.


        :param derived_logical_entities: The derived_logical_entities of this ValidatePatternResult.
        :type: list[DerivedLogicalEntities]
        """
        self._derived_logical_entities = derived_logical_entities

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
