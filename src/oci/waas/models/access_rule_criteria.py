# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessRuleCriteria(object):
    """
    When defined, the parent challenge would be applied only for the requests that matched all the listed conditions.
    """

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "URL_IS"
    CONDITION_URL_IS = "URL_IS"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "URL_IS_NOT"
    CONDITION_URL_IS_NOT = "URL_IS_NOT"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "URL_STARTS_WITH"
    CONDITION_URL_STARTS_WITH = "URL_STARTS_WITH"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "URL_PART_ENDS_WITH"
    CONDITION_URL_PART_ENDS_WITH = "URL_PART_ENDS_WITH"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "URL_PART_CONTAINS"
    CONDITION_URL_PART_CONTAINS = "URL_PART_CONTAINS"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "URL_REGEX"
    CONDITION_URL_REGEX = "URL_REGEX"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "URL_DOES_NOT_MATCH_REGEX"
    CONDITION_URL_DOES_NOT_MATCH_REGEX = "URL_DOES_NOT_MATCH_REGEX"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "URL_DOES_NOT_START_WITH"
    CONDITION_URL_DOES_NOT_START_WITH = "URL_DOES_NOT_START_WITH"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "URL_PART_DOES_NOT_CONTAIN"
    CONDITION_URL_PART_DOES_NOT_CONTAIN = "URL_PART_DOES_NOT_CONTAIN"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "URL_PART_DOES_NOT_END_WITH"
    CONDITION_URL_PART_DOES_NOT_END_WITH = "URL_PART_DOES_NOT_END_WITH"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "IP_IS"
    CONDITION_IP_IS = "IP_IS"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "IP_IS_NOT"
    CONDITION_IP_IS_NOT = "IP_IS_NOT"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "IP_IN_LIST"
    CONDITION_IP_IN_LIST = "IP_IN_LIST"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "IP_NOT_IN_LIST"
    CONDITION_IP_NOT_IN_LIST = "IP_NOT_IN_LIST"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "HTTP_HEADER_CONTAINS"
    CONDITION_HTTP_HEADER_CONTAINS = "HTTP_HEADER_CONTAINS"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "HTTP_METHOD_IS"
    CONDITION_HTTP_METHOD_IS = "HTTP_METHOD_IS"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "HTTP_METHOD_IS_NOT"
    CONDITION_HTTP_METHOD_IS_NOT = "HTTP_METHOD_IS_NOT"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "COUNTRY_IS"
    CONDITION_COUNTRY_IS = "COUNTRY_IS"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "COUNTRY_IS_NOT"
    CONDITION_COUNTRY_IS_NOT = "COUNTRY_IS_NOT"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "USER_AGENT_IS"
    CONDITION_USER_AGENT_IS = "USER_AGENT_IS"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "USER_AGENT_IS_NOT"
    CONDITION_USER_AGENT_IS_NOT = "USER_AGENT_IS_NOT"

    def __init__(self, **kwargs):
        """
        Initializes a new AccessRuleCriteria object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param condition:
            The value to assign to the condition property of this AccessRuleCriteria.
            Allowed values for this property are: "URL_IS", "URL_IS_NOT", "URL_STARTS_WITH", "URL_PART_ENDS_WITH", "URL_PART_CONTAINS", "URL_REGEX", "URL_DOES_NOT_MATCH_REGEX", "URL_DOES_NOT_START_WITH", "URL_PART_DOES_NOT_CONTAIN", "URL_PART_DOES_NOT_END_WITH", "IP_IS", "IP_IS_NOT", "IP_IN_LIST", "IP_NOT_IN_LIST", "HTTP_HEADER_CONTAINS", "HTTP_METHOD_IS", "HTTP_METHOD_IS_NOT", "COUNTRY_IS", "COUNTRY_IS_NOT", "USER_AGENT_IS", "USER_AGENT_IS_NOT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type condition: str

        :param value:
            The value to assign to the value property of this AccessRuleCriteria.
        :type value: str

        :param is_case_sensitive:
            The value to assign to the is_case_sensitive property of this AccessRuleCriteria.
        :type is_case_sensitive: bool

        """
        self.swagger_types = {
            'condition': 'str',
            'value': 'str',
            'is_case_sensitive': 'bool'
        }

        self.attribute_map = {
            'condition': 'condition',
            'value': 'value',
            'is_case_sensitive': 'isCaseSensitive'
        }

        self._condition = None
        self._value = None
        self._is_case_sensitive = None

    @property
    def condition(self):
        """
        **[Required]** Gets the condition of this AccessRuleCriteria.
        The criteria the access rule and JavaScript Challenge uses to determine if action should be taken on a request.
        - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field. URL must start with a `/`.
        - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the `value` field. URL must start with a `/`.
        - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field. URL must start with a `/`.
        - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value` field.
        - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field.
        - **URL_REGEX:** Matches if the concatenation of request URL path and query is described by the regular expression in the value field. The value must be a valid regular expression recognized by the PCRE library in Nginx (https://www.pcre.org).
        - **URL_DOES_NOT_MATCH_REGEX:** Matches if the concatenation of request URL path and query is not described by the regular expression in the `value` field. The value must be a valid regular expression recognized by the PCRE library in Nginx (https://www.pcre.org).
        - **URL_DOES_NOT_START_WITH:** Matches if the concatenation of request URL path and query does not start with the contents of the `value` field.
        - **URL_PART_DOES_NOT_CONTAIN:** Matches if the concatenation of request URL path and query does not contain the contents of the `value` field.
        - **URL_PART_DOES_NOT_END_WITH:** Matches if the concatenation of request URL path and query does not end with the contents of the `value` field.
        - **IP_IS:** Matches if the request originates from one of the IP addresses contained in the defined address list. The `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \

        *Example:* \"1.1.1.1\
        1.1.1.2\
        1.2.2.1/30\"
        - **IP_IS_NOT:** Matches if the request does not originate from any of the IP addresses contained in the defined address list. The `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \

        *Example:* \"1.1.1.1\
        1.1.1.2\
        1.2.2.1/30\"
        - **IP_IN_LIST:** Matches if the request originates from one of the IP addresses contained in the referenced address list. The `value` in this case is OCID of the address list.
        - **IP_NOT_IN_LIST:** Matches if the request does not originate from any IP address contained in the referenced address list. The `value` field in this case is OCID of the address list.
        - **HTTP_HEADER_CONTAINS:** The HTTP_HEADER_CONTAINS criteria is defined using a compound value separated by a colon: a header field name and a header field value. `host:test.example.com` is an example of a criteria value where `host` is the header field name and `test.example.com` is the header field value. A request matches when the header field name is a case insensitive match and the header field value is a case insensitive, substring match.
        *Example:* With a criteria value of `host:test.example.com`, where `host` is the name of the field and `test.example.com` is the value of the host field, a request with the header values, `Host: www.test.example.com` will match, where as a request with header values of `host: www.example.com` or `host: test.sub.example.com` will not match.
        - **HTTP_METHOD_IS:** Matches if the request method is identical to one of the values listed in field. The `value` in this case is string with one or multiple HTTP methods separated by new line symbol \
         The list of available methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`

         *Example:* \"GET\
        POST\"

        - **HTTP_METHOD_IS_NOT:** Matches if the request is not identical to any of the contents of the `value` field. The `value` in this case is string with one or multiple HTTP methods separated by new line symbol \
         The list of available methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`

         *Example:* \"GET\
        POST\"

        - **COUNTRY_IS:** Matches if the request originates from one of countries in the `value` field. The `value` in this case is string with one or multiple countries separated by new line symbol \
         Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see `ISO's website`__.
        *Example:* \"AL\
        DZ\
        AM\"
        - **COUNTRY_IS_NOT:** Matches if the request does not originate from any of countries in the `value` field. The `value` in this case is string with one or multiple countries separated by new line symbol \
         Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see `ISO's website`__.
        *Example:* \"AL\
        DZ\
        AM\"
        - **USER_AGENT_IS:** Matches if the requesting user agent is identical to the contents of the `value` field.
        *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`
        - **USER_AGENT_IS_NOT:** Matches if the requesting user agent is not identical to the contents of the `value` field.
        *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`

        __ https://www.iso.org/obp/ui/#search/code/
        __ https://www.iso.org/obp/ui/#search/code/

        Allowed values for this property are: "URL_IS", "URL_IS_NOT", "URL_STARTS_WITH", "URL_PART_ENDS_WITH", "URL_PART_CONTAINS", "URL_REGEX", "URL_DOES_NOT_MATCH_REGEX", "URL_DOES_NOT_START_WITH", "URL_PART_DOES_NOT_CONTAIN", "URL_PART_DOES_NOT_END_WITH", "IP_IS", "IP_IS_NOT", "IP_IN_LIST", "IP_NOT_IN_LIST", "HTTP_HEADER_CONTAINS", "HTTP_METHOD_IS", "HTTP_METHOD_IS_NOT", "COUNTRY_IS", "COUNTRY_IS_NOT", "USER_AGENT_IS", "USER_AGENT_IS_NOT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The condition of this AccessRuleCriteria.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this AccessRuleCriteria.
        The criteria the access rule and JavaScript Challenge uses to determine if action should be taken on a request.
        - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field. URL must start with a `/`.
        - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the `value` field. URL must start with a `/`.
        - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field. URL must start with a `/`.
        - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value` field.
        - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field.
        - **URL_REGEX:** Matches if the concatenation of request URL path and query is described by the regular expression in the value field. The value must be a valid regular expression recognized by the PCRE library in Nginx (https://www.pcre.org).
        - **URL_DOES_NOT_MATCH_REGEX:** Matches if the concatenation of request URL path and query is not described by the regular expression in the `value` field. The value must be a valid regular expression recognized by the PCRE library in Nginx (https://www.pcre.org).
        - **URL_DOES_NOT_START_WITH:** Matches if the concatenation of request URL path and query does not start with the contents of the `value` field.
        - **URL_PART_DOES_NOT_CONTAIN:** Matches if the concatenation of request URL path and query does not contain the contents of the `value` field.
        - **URL_PART_DOES_NOT_END_WITH:** Matches if the concatenation of request URL path and query does not end with the contents of the `value` field.
        - **IP_IS:** Matches if the request originates from one of the IP addresses contained in the defined address list. The `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \

        *Example:* \"1.1.1.1\
        1.1.1.2\
        1.2.2.1/30\"
        - **IP_IS_NOT:** Matches if the request does not originate from any of the IP addresses contained in the defined address list. The `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \

        *Example:* \"1.1.1.1\
        1.1.1.2\
        1.2.2.1/30\"
        - **IP_IN_LIST:** Matches if the request originates from one of the IP addresses contained in the referenced address list. The `value` in this case is OCID of the address list.
        - **IP_NOT_IN_LIST:** Matches if the request does not originate from any IP address contained in the referenced address list. The `value` field in this case is OCID of the address list.
        - **HTTP_HEADER_CONTAINS:** The HTTP_HEADER_CONTAINS criteria is defined using a compound value separated by a colon: a header field name and a header field value. `host:test.example.com` is an example of a criteria value where `host` is the header field name and `test.example.com` is the header field value. A request matches when the header field name is a case insensitive match and the header field value is a case insensitive, substring match.
        *Example:* With a criteria value of `host:test.example.com`, where `host` is the name of the field and `test.example.com` is the value of the host field, a request with the header values, `Host: www.test.example.com` will match, where as a request with header values of `host: www.example.com` or `host: test.sub.example.com` will not match.
        - **HTTP_METHOD_IS:** Matches if the request method is identical to one of the values listed in field. The `value` in this case is string with one or multiple HTTP methods separated by new line symbol \
         The list of available methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`

         *Example:* \"GET\
        POST\"

        - **HTTP_METHOD_IS_NOT:** Matches if the request is not identical to any of the contents of the `value` field. The `value` in this case is string with one or multiple HTTP methods separated by new line symbol \
         The list of available methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`

         *Example:* \"GET\
        POST\"

        - **COUNTRY_IS:** Matches if the request originates from one of countries in the `value` field. The `value` in this case is string with one or multiple countries separated by new line symbol \
         Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see `ISO's website`__.
        *Example:* \"AL\
        DZ\
        AM\"
        - **COUNTRY_IS_NOT:** Matches if the request does not originate from any of countries in the `value` field. The `value` in this case is string with one or multiple countries separated by new line symbol \
         Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see `ISO's website`__.
        *Example:* \"AL\
        DZ\
        AM\"
        - **USER_AGENT_IS:** Matches if the requesting user agent is identical to the contents of the `value` field.
        *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`
        - **USER_AGENT_IS_NOT:** Matches if the requesting user agent is not identical to the contents of the `value` field.
        *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`

        __ https://www.iso.org/obp/ui/#search/code/
        __ https://www.iso.org/obp/ui/#search/code/


        :param condition: The condition of this AccessRuleCriteria.
        :type: str
        """
        allowed_values = ["URL_IS", "URL_IS_NOT", "URL_STARTS_WITH", "URL_PART_ENDS_WITH", "URL_PART_CONTAINS", "URL_REGEX", "URL_DOES_NOT_MATCH_REGEX", "URL_DOES_NOT_START_WITH", "URL_PART_DOES_NOT_CONTAIN", "URL_PART_DOES_NOT_END_WITH", "IP_IS", "IP_IS_NOT", "IP_IN_LIST", "IP_NOT_IN_LIST", "HTTP_HEADER_CONTAINS", "HTTP_METHOD_IS", "HTTP_METHOD_IS_NOT", "COUNTRY_IS", "COUNTRY_IS_NOT", "USER_AGENT_IS", "USER_AGENT_IS_NOT"]
        if not value_allowed_none_or_none_sentinel(condition, allowed_values):
            condition = 'UNKNOWN_ENUM_VALUE'
        self._condition = condition

    @property
    def value(self):
        """
        **[Required]** Gets the value of this AccessRuleCriteria.
        The criteria value.


        :return: The value of this AccessRuleCriteria.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AccessRuleCriteria.
        The criteria value.


        :param value: The value of this AccessRuleCriteria.
        :type: str
        """
        self._value = value

    @property
    def is_case_sensitive(self):
        """
        Gets the is_case_sensitive of this AccessRuleCriteria.
        When enabled, the condition will be matched with case-sensitive rules.


        :return: The is_case_sensitive of this AccessRuleCriteria.
        :rtype: bool
        """
        return self._is_case_sensitive

    @is_case_sensitive.setter
    def is_case_sensitive(self, is_case_sensitive):
        """
        Sets the is_case_sensitive of this AccessRuleCriteria.
        When enabled, the condition will be matched with case-sensitive rules.


        :param is_case_sensitive: The is_case_sensitive of this AccessRuleCriteria.
        :type: bool
        """
        self._is_case_sensitive = is_case_sensitive

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
