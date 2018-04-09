# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PathMatchType(object):
    """
    The type of matching to apply to incoming URIs.
    """

    #: A constant which can be used with the match_type property of a PathMatchType.
    #: This constant has a value of "EXACT_MATCH"
    MATCH_TYPE_EXACT_MATCH = "EXACT_MATCH"

    #: A constant which can be used with the match_type property of a PathMatchType.
    #: This constant has a value of "FORCE_LONGEST_PREFIX_MATCH"
    MATCH_TYPE_FORCE_LONGEST_PREFIX_MATCH = "FORCE_LONGEST_PREFIX_MATCH"

    #: A constant which can be used with the match_type property of a PathMatchType.
    #: This constant has a value of "PREFIX_MATCH"
    MATCH_TYPE_PREFIX_MATCH = "PREFIX_MATCH"

    #: A constant which can be used with the match_type property of a PathMatchType.
    #: This constant has a value of "SUFFIX_MATCH"
    MATCH_TYPE_SUFFIX_MATCH = "SUFFIX_MATCH"

    def __init__(self, **kwargs):
        """
        Initializes a new PathMatchType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param match_type:
            The value to assign to the match_type property of this PathMatchType.
            Allowed values for this property are: "EXACT_MATCH", "FORCE_LONGEST_PREFIX_MATCH", "PREFIX_MATCH", "SUFFIX_MATCH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type match_type: str

        """
        self.swagger_types = {
            'match_type': 'str'
        }

        self.attribute_map = {
            'match_type': 'matchType'
        }

        self._match_type = None

    @property
    def match_type(self):
        """
        **[Required]** Gets the match_type of this PathMatchType.
        Specifies how the load balancing service compares a :func:`path_route`
        object's `path` string against the incoming URI.

        *  **EXACT_MATCH** - Looks for a `path` string that exactly matches the incoming URI path.

        *  **FORCE_LONGEST_PREFIX_MATCH** - Looks for the `path` string with the best, longest match of the beginning
           portion of the incoming URI path.

        *  **PREFIX_MATCH** - Looks for a `path` string that matches the beginning portion of the incoming URI path.

        *  **SUFFIX_MATCH** - Looks for a `path` string that matches the ending portion of the incoming URI path.

        For a full description of how the system handles `matchType` in a path route set containing multiple rules, see
        `Managing Request Routing`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Balance/Tasks/managingrequest.htm

        Allowed values for this property are: "EXACT_MATCH", "FORCE_LONGEST_PREFIX_MATCH", "PREFIX_MATCH", "SUFFIX_MATCH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The match_type of this PathMatchType.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """
        Sets the match_type of this PathMatchType.
        Specifies how the load balancing service compares a :func:`path_route`
        object's `path` string against the incoming URI.

        *  **EXACT_MATCH** - Looks for a `path` string that exactly matches the incoming URI path.

        *  **FORCE_LONGEST_PREFIX_MATCH** - Looks for the `path` string with the best, longest match of the beginning
           portion of the incoming URI path.

        *  **PREFIX_MATCH** - Looks for a `path` string that matches the beginning portion of the incoming URI path.

        *  **SUFFIX_MATCH** - Looks for a `path` string that matches the ending portion of the incoming URI path.

        For a full description of how the system handles `matchType` in a path route set containing multiple rules, see
        `Managing Request Routing`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Balance/Tasks/managingrequest.htm


        :param match_type: The match_type of this PathMatchType.
        :type: str
        """
        allowed_values = ["EXACT_MATCH", "FORCE_LONGEST_PREFIX_MATCH", "PREFIX_MATCH", "SUFFIX_MATCH"]
        if not value_allowed_none_or_none_sentinel(match_type, allowed_values):
            match_type = 'UNKNOWN_ENUM_VALUE'
        self._match_type = match_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
