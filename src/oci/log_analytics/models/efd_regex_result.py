# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EfdRegexResult(object):
    """
    EfdRegexResult
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EfdRegexResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param base_field_name:
            The value to assign to the base_field_name property of this EfdRegexResult.
        :type base_field_name: str

        :param id:
            The value to assign to the id property of this EfdRegexResult.
        :type id: int

        :param match_result:
            The value to assign to the match_result property of this EfdRegexResult.
        :type match_result: RegexMatchResult

        :param parsed_field_count:
            The value to assign to the parsed_field_count property of this EfdRegexResult.
        :type parsed_field_count: int

        :param parsed_fields:
            The value to assign to the parsed_fields property of this EfdRegexResult.
        :type parsed_fields: dict(str, str)

        :param regex:
            The value to assign to the regex property of this EfdRegexResult.
        :type regex: str

        :param status:
            The value to assign to the status property of this EfdRegexResult.
        :type status: str

        :param status_description:
            The value to assign to the status_description property of this EfdRegexResult.
        :type status_description: str

        :param is_valid_regex_syntax:
            The value to assign to the is_valid_regex_syntax property of this EfdRegexResult.
        :type is_valid_regex_syntax: bool

        :param violations:
            The value to assign to the violations property of this EfdRegexResult.
        :type violations: list[Violation]

        """
        self.swagger_types = {
            'base_field_name': 'str',
            'id': 'int',
            'match_result': 'RegexMatchResult',
            'parsed_field_count': 'int',
            'parsed_fields': 'dict(str, str)',
            'regex': 'str',
            'status': 'str',
            'status_description': 'str',
            'is_valid_regex_syntax': 'bool',
            'violations': 'list[Violation]'
        }

        self.attribute_map = {
            'base_field_name': 'baseFieldName',
            'id': 'id',
            'match_result': 'matchResult',
            'parsed_field_count': 'parsedFieldCount',
            'parsed_fields': 'parsedFields',
            'regex': 'regex',
            'status': 'status',
            'status_description': 'statusDescription',
            'is_valid_regex_syntax': 'isValidRegexSyntax',
            'violations': 'violations'
        }

        self._base_field_name = None
        self._id = None
        self._match_result = None
        self._parsed_field_count = None
        self._parsed_fields = None
        self._regex = None
        self._status = None
        self._status_description = None
        self._is_valid_regex_syntax = None
        self._violations = None

    @property
    def base_field_name(self):
        """
        Gets the base_field_name of this EfdRegexResult.
        baseFieldName


        :return: The base_field_name of this EfdRegexResult.
        :rtype: str
        """
        return self._base_field_name

    @base_field_name.setter
    def base_field_name(self, base_field_name):
        """
        Sets the base_field_name of this EfdRegexResult.
        baseFieldName


        :param base_field_name: The base_field_name of this EfdRegexResult.
        :type: str
        """
        self._base_field_name = base_field_name

    @property
    def id(self):
        """
        Gets the id of this EfdRegexResult.
        id


        :return: The id of this EfdRegexResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EfdRegexResult.
        id


        :param id: The id of this EfdRegexResult.
        :type: int
        """
        self._id = id

    @property
    def match_result(self):
        """
        Gets the match_result of this EfdRegexResult.

        :return: The match_result of this EfdRegexResult.
        :rtype: RegexMatchResult
        """
        return self._match_result

    @match_result.setter
    def match_result(self, match_result):
        """
        Sets the match_result of this EfdRegexResult.

        :param match_result: The match_result of this EfdRegexResult.
        :type: RegexMatchResult
        """
        self._match_result = match_result

    @property
    def parsed_field_count(self):
        """
        Gets the parsed_field_count of this EfdRegexResult.
        parsedFieldCount


        :return: The parsed_field_count of this EfdRegexResult.
        :rtype: int
        """
        return self._parsed_field_count

    @parsed_field_count.setter
    def parsed_field_count(self, parsed_field_count):
        """
        Sets the parsed_field_count of this EfdRegexResult.
        parsedFieldCount


        :param parsed_field_count: The parsed_field_count of this EfdRegexResult.
        :type: int
        """
        self._parsed_field_count = parsed_field_count

    @property
    def parsed_fields(self):
        """
        Gets the parsed_fields of this EfdRegexResult.
        parsedFields


        :return: The parsed_fields of this EfdRegexResult.
        :rtype: dict(str, str)
        """
        return self._parsed_fields

    @parsed_fields.setter
    def parsed_fields(self, parsed_fields):
        """
        Sets the parsed_fields of this EfdRegexResult.
        parsedFields


        :param parsed_fields: The parsed_fields of this EfdRegexResult.
        :type: dict(str, str)
        """
        self._parsed_fields = parsed_fields

    @property
    def regex(self):
        """
        Gets the regex of this EfdRegexResult.
        regex


        :return: The regex of this EfdRegexResult.
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """
        Sets the regex of this EfdRegexResult.
        regex


        :param regex: The regex of this EfdRegexResult.
        :type: str
        """
        self._regex = regex

    @property
    def status(self):
        """
        Gets the status of this EfdRegexResult.
        status


        :return: The status of this EfdRegexResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this EfdRegexResult.
        status


        :param status: The status of this EfdRegexResult.
        :type: str
        """
        self._status = status

    @property
    def status_description(self):
        """
        Gets the status_description of this EfdRegexResult.
        statusDescription


        :return: The status_description of this EfdRegexResult.
        :rtype: str
        """
        return self._status_description

    @status_description.setter
    def status_description(self, status_description):
        """
        Sets the status_description of this EfdRegexResult.
        statusDescription


        :param status_description: The status_description of this EfdRegexResult.
        :type: str
        """
        self._status_description = status_description

    @property
    def is_valid_regex_syntax(self):
        """
        Gets the is_valid_regex_syntax of this EfdRegexResult.
        isValidRegexSyntax


        :return: The is_valid_regex_syntax of this EfdRegexResult.
        :rtype: bool
        """
        return self._is_valid_regex_syntax

    @is_valid_regex_syntax.setter
    def is_valid_regex_syntax(self, is_valid_regex_syntax):
        """
        Sets the is_valid_regex_syntax of this EfdRegexResult.
        isValidRegexSyntax


        :param is_valid_regex_syntax: The is_valid_regex_syntax of this EfdRegexResult.
        :type: bool
        """
        self._is_valid_regex_syntax = is_valid_regex_syntax

    @property
    def violations(self):
        """
        Gets the violations of this EfdRegexResult.
        violations


        :return: The violations of this EfdRegexResult.
        :rtype: list[Violation]
        """
        return self._violations

    @violations.setter
    def violations(self, violations):
        """
        Sets the violations of this EfdRegexResult.
        violations


        :param violations: The violations of this EfdRegexResult.
        :type: list[Violation]
        """
        self._violations = violations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
