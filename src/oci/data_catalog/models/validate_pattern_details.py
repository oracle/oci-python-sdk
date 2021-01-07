# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidatePatternDetails(object):
    """
    Validate pattern using the expression and file list.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValidatePatternDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param expression:
            The value to assign to the expression property of this ValidatePatternDetails.
        :type expression: str

        :param check_file_path_list:
            The value to assign to the check_file_path_list property of this ValidatePatternDetails.
        :type check_file_path_list: list[str]

        :param check_failure_limit:
            The value to assign to the check_failure_limit property of this ValidatePatternDetails.
        :type check_failure_limit: int

        """
        self.swagger_types = {
            'expression': 'str',
            'check_file_path_list': 'list[str]',
            'check_failure_limit': 'int'
        }

        self.attribute_map = {
            'expression': 'expression',
            'check_file_path_list': 'checkFilePathList',
            'check_failure_limit': 'checkFailureLimit'
        }

        self._expression = None
        self._check_file_path_list = None
        self._check_failure_limit = None

    @property
    def expression(self):
        """
        Gets the expression of this ValidatePatternDetails.
        The expression used in the pattern that may include qualifiers. Refer to the user documentation for details of the format and examples.


        :return: The expression of this ValidatePatternDetails.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this ValidatePatternDetails.
        The expression used in the pattern that may include qualifiers. Refer to the user documentation for details of the format and examples.


        :param expression: The expression of this ValidatePatternDetails.
        :type: str
        """
        self._expression = expression

    @property
    def check_file_path_list(self):
        """
        Gets the check_file_path_list of this ValidatePatternDetails.
        List of file paths against which the expression can be tried, as a check. This documents, for reference
        purposes, some example objects a pattern is meant to work with.

        If provided with the request,this overrides the list which already exists as part of the pattern, if any.


        :return: The check_file_path_list of this ValidatePatternDetails.
        :rtype: list[str]
        """
        return self._check_file_path_list

    @check_file_path_list.setter
    def check_file_path_list(self, check_file_path_list):
        """
        Sets the check_file_path_list of this ValidatePatternDetails.
        List of file paths against which the expression can be tried, as a check. This documents, for reference
        purposes, some example objects a pattern is meant to work with.

        If provided with the request,this overrides the list which already exists as part of the pattern, if any.


        :param check_file_path_list: The check_file_path_list of this ValidatePatternDetails.
        :type: list[str]
        """
        self._check_file_path_list = check_file_path_list

    @property
    def check_failure_limit(self):
        """
        Gets the check_failure_limit of this ValidatePatternDetails.
        The maximum number of UNMATCHED files, in checkFilePathList, above which the check fails.
        Optional, if checkFilePathList is provided.

        If provided with the request, this overrides the value which already exists as part of the pattern, if any.


        :return: The check_failure_limit of this ValidatePatternDetails.
        :rtype: int
        """
        return self._check_failure_limit

    @check_failure_limit.setter
    def check_failure_limit(self, check_failure_limit):
        """
        Sets the check_failure_limit of this ValidatePatternDetails.
        The maximum number of UNMATCHED files, in checkFilePathList, above which the check fails.
        Optional, if checkFilePathList is provided.

        If provided with the request, this overrides the value which already exists as part of the pattern, if any.


        :param check_failure_limit: The check_failure_limit of this ValidatePatternDetails.
        :type: int
        """
        self._check_failure_limit = check_failure_limit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
