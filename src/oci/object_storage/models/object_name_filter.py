# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectNameFilter(object):
    """
    A filter that compares object names to a set of prefixes or patterns to determine if a rule applies to a
    given object. The filter can contain include glob patterns, exclude glob patterns and inclusion prefixes.
    The inclusion prefixes property is kept for backward compatibility. It is recommended to use inclusion patterns
    instead of prefixes. Exclusions take precedence over inclusions.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectNameFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param inclusion_prefixes:
            The value to assign to the inclusion_prefixes property of this ObjectNameFilter.
        :type inclusion_prefixes: list[str]

        :param inclusion_patterns:
            The value to assign to the inclusion_patterns property of this ObjectNameFilter.
        :type inclusion_patterns: list[str]

        :param exclusion_patterns:
            The value to assign to the exclusion_patterns property of this ObjectNameFilter.
        :type exclusion_patterns: list[str]

        """
        self.swagger_types = {
            'inclusion_prefixes': 'list[str]',
            'inclusion_patterns': 'list[str]',
            'exclusion_patterns': 'list[str]'
        }

        self.attribute_map = {
            'inclusion_prefixes': 'inclusionPrefixes',
            'inclusion_patterns': 'inclusionPatterns',
            'exclusion_patterns': 'exclusionPatterns'
        }

        self._inclusion_prefixes = None
        self._inclusion_patterns = None
        self._exclusion_patterns = None

    @property
    def inclusion_prefixes(self):
        """
        Gets the inclusion_prefixes of this ObjectNameFilter.
        An array of object name prefixes that the rule will apply to. An empty array means to include all objects.


        :return: The inclusion_prefixes of this ObjectNameFilter.
        :rtype: list[str]
        """
        return self._inclusion_prefixes

    @inclusion_prefixes.setter
    def inclusion_prefixes(self, inclusion_prefixes):
        """
        Sets the inclusion_prefixes of this ObjectNameFilter.
        An array of object name prefixes that the rule will apply to. An empty array means to include all objects.


        :param inclusion_prefixes: The inclusion_prefixes of this ObjectNameFilter.
        :type: list[str]
        """
        self._inclusion_prefixes = inclusion_prefixes

    @property
    def inclusion_patterns(self):
        """
        Gets the inclusion_patterns of this ObjectNameFilter.
        An array of glob patterns to match the object names to include. An empty array includes all objects in the
        bucket. Exclusion patterns take precedence over inclusion patterns.
        A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other
        than the special pattern characters described below, matches itself.
            Glob patterns must be between 1 and 1024 characters.

            The special pattern characters have the following meanings:

            \\           Escapes the following character
            *           Matches any string of characters.
            ?           Matches any single character .
            [...]       Matches a group of characters. A group of characters can be:
                            A set of characters, for example: [Zafg9@]. This matches any character in the brackets.
                            A range of characters, for example: [a-z]. This matches any character in the range.
                                [a-f] is equivalent to [abcdef].
                                For character ranges only the CHARACTER-CHARACTER pattern is supported.
                                    [ab-yz] is not valid
                                    [a-mn-z] is not valid
                                Character ranges can not start with ^ or :
                                To include a '-' in the range, make it the first or last character.


        :return: The inclusion_patterns of this ObjectNameFilter.
        :rtype: list[str]
        """
        return self._inclusion_patterns

    @inclusion_patterns.setter
    def inclusion_patterns(self, inclusion_patterns):
        """
        Sets the inclusion_patterns of this ObjectNameFilter.
        An array of glob patterns to match the object names to include. An empty array includes all objects in the
        bucket. Exclusion patterns take precedence over inclusion patterns.
        A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other
        than the special pattern characters described below, matches itself.
            Glob patterns must be between 1 and 1024 characters.

            The special pattern characters have the following meanings:

            \\           Escapes the following character
            *           Matches any string of characters.
            ?           Matches any single character .
            [...]       Matches a group of characters. A group of characters can be:
                            A set of characters, for example: [Zafg9@]. This matches any character in the brackets.
                            A range of characters, for example: [a-z]. This matches any character in the range.
                                [a-f] is equivalent to [abcdef].
                                For character ranges only the CHARACTER-CHARACTER pattern is supported.
                                    [ab-yz] is not valid
                                    [a-mn-z] is not valid
                                Character ranges can not start with ^ or :
                                To include a '-' in the range, make it the first or last character.


        :param inclusion_patterns: The inclusion_patterns of this ObjectNameFilter.
        :type: list[str]
        """
        self._inclusion_patterns = inclusion_patterns

    @property
    def exclusion_patterns(self):
        """
        Gets the exclusion_patterns of this ObjectNameFilter.
        An array of glob patterns to match the object names to exclude. An empty array is ignored. Exclusion
        patterns take precedence over inclusion patterns.
        A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other
        than the special pattern characters described below, matches itself.
            Glob patterns must be between 1 and 1024 characters.

            The special pattern characters have the following meanings:

            \\           Escapes the following character
            *           Matches any string of characters.
            ?           Matches any single character .
            [...]       Matches a group of characters. A group of characters can be:
                            A set of characters, for example: [Zafg9@]. This matches any character in the brackets.
                            A range of characters, for example: [a-z]. This matches any character in the range.
                                [a-f] is equivalent to [abcdef].
                                For character ranges only the CHARACTER-CHARACTER pattern is supported.
                                    [ab-yz] is not valid
                                    [a-mn-z] is not valid
                                Character ranges can not start with ^ or :
                                To include a '-' in the range, make it the first or last character.


        :return: The exclusion_patterns of this ObjectNameFilter.
        :rtype: list[str]
        """
        return self._exclusion_patterns

    @exclusion_patterns.setter
    def exclusion_patterns(self, exclusion_patterns):
        """
        Sets the exclusion_patterns of this ObjectNameFilter.
        An array of glob patterns to match the object names to exclude. An empty array is ignored. Exclusion
        patterns take precedence over inclusion patterns.
        A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other
        than the special pattern characters described below, matches itself.
            Glob patterns must be between 1 and 1024 characters.

            The special pattern characters have the following meanings:

            \\           Escapes the following character
            *           Matches any string of characters.
            ?           Matches any single character .
            [...]       Matches a group of characters. A group of characters can be:
                            A set of characters, for example: [Zafg9@]. This matches any character in the brackets.
                            A range of characters, for example: [a-z]. This matches any character in the range.
                                [a-f] is equivalent to [abcdef].
                                For character ranges only the CHARACTER-CHARACTER pattern is supported.
                                    [ab-yz] is not valid
                                    [a-mn-z] is not valid
                                Character ranges can not start with ^ or :
                                To include a '-' in the range, make it the first or last character.


        :param exclusion_patterns: The exclusion_patterns of this ObjectNameFilter.
        :type: list[str]
        """
        self._exclusion_patterns = exclusion_patterns

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
