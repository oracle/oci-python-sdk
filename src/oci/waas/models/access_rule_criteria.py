# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessRuleCriteria(object):
    """
    AccessRuleCriteria model.
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
    #: This constant has a value of "IP_IS"
    CONDITION_IP_IS = "IP_IS"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "IP_IS_NOT"
    CONDITION_IP_IS_NOT = "IP_IS_NOT"

    #: A constant which can be used with the condition property of a AccessRuleCriteria.
    #: This constant has a value of "HTTP_HEADER_CONTAINS"
    CONDITION_HTTP_HEADER_CONTAINS = "HTTP_HEADER_CONTAINS"

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
            Allowed values for this property are: "URL_IS", "URL_IS_NOT", "URL_STARTS_WITH", "URL_PART_ENDS_WITH", "URL_PART_CONTAINS", "URL_REGEX", "IP_IS", "IP_IS_NOT", "HTTP_HEADER_CONTAINS", "COUNTRY_IS", "COUNTRY_IS_NOT", "USER_AGENT_IS", "USER_AGENT_IS_NOT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type condition: str

        :param value:
            The value to assign to the value property of this AccessRuleCriteria.
        :type value: str

        """
        self.swagger_types = {
            'condition': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'condition': 'condition',
            'value': 'value'
        }

        self._condition = None
        self._value = None

    @property
    def condition(self):
        """
        **[Required]** Gets the condition of this AccessRuleCriteria.
        The criteria the access rule uses to determine if action should be taken on a request.
        - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field.

        - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the `value` field.

        - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field.

        - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value` field.

        - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field.

        - **URL_REGEX:** Matches if the request is described by the regular expression in the `value` field.

        - **IP_IS:** Matches if the request originates from an IP address in the `value` field.

        - **IP_IS_NOT:** Matches if the request does not originate from an IP address in the `value` field.

        - **HTTP_HEADER_CONTAINS:** The HTTP_HEADER_CONTAINS criteria is defined using a compound value separated by a colon: a header field name and a header field value. `host:test.example.com` is an example of a criteria value where `host` is the header field name and `test.example.com` is the header field value. A request matches when the header field name is a case insensitive match and the header field value is a case insensitive, substring match.
        *Example:* With a criteria value of `host:test.example.com`, where `host` is the name of the field and `test.example.com` is the value of the host field, a request with the header values, `Host: www.test.example.com` will match, where as a request with header values of `host: www.example.com` or `host: test.sub.example.com` will not match.

        - **COUNTRY_IS:** Matches if the request originates from a country in the `value` field. Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see `ISO's website`__.

        - **COUNTRY_IS_NOT:** Matches if the request does not originate from a country in the `value` field. Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see `ISO's website`__.

        - **USER_AGENT_IS:** Matches if the requesting user agent is identical to the contents of the `value` field. Example: `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`

        - **USER_AGENT_IS_NOT:** Matches if the requesting user agent is not identical to the contents of the `value` field. Example: `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`

        __ https://www.iso.org/obp/ui/#search/code/
        __ https://www.iso.org/obp/ui/#search/code/

        Allowed values for this property are: "URL_IS", "URL_IS_NOT", "URL_STARTS_WITH", "URL_PART_ENDS_WITH", "URL_PART_CONTAINS", "URL_REGEX", "IP_IS", "IP_IS_NOT", "HTTP_HEADER_CONTAINS", "COUNTRY_IS", "COUNTRY_IS_NOT", "USER_AGENT_IS", "USER_AGENT_IS_NOT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The condition of this AccessRuleCriteria.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this AccessRuleCriteria.
        The criteria the access rule uses to determine if action should be taken on a request.
        - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field.

        - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the `value` field.

        - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field.

        - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value` field.

        - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field.

        - **URL_REGEX:** Matches if the request is described by the regular expression in the `value` field.

        - **IP_IS:** Matches if the request originates from an IP address in the `value` field.

        - **IP_IS_NOT:** Matches if the request does not originate from an IP address in the `value` field.

        - **HTTP_HEADER_CONTAINS:** The HTTP_HEADER_CONTAINS criteria is defined using a compound value separated by a colon: a header field name and a header field value. `host:test.example.com` is an example of a criteria value where `host` is the header field name and `test.example.com` is the header field value. A request matches when the header field name is a case insensitive match and the header field value is a case insensitive, substring match.
        *Example:* With a criteria value of `host:test.example.com`, where `host` is the name of the field and `test.example.com` is the value of the host field, a request with the header values, `Host: www.test.example.com` will match, where as a request with header values of `host: www.example.com` or `host: test.sub.example.com` will not match.

        - **COUNTRY_IS:** Matches if the request originates from a country in the `value` field. Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see `ISO's website`__.

        - **COUNTRY_IS_NOT:** Matches if the request does not originate from a country in the `value` field. Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see `ISO's website`__.

        - **USER_AGENT_IS:** Matches if the requesting user agent is identical to the contents of the `value` field. Example: `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`

        - **USER_AGENT_IS_NOT:** Matches if the requesting user agent is not identical to the contents of the `value` field. Example: `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`

        __ https://www.iso.org/obp/ui/#search/code/
        __ https://www.iso.org/obp/ui/#search/code/


        :param condition: The condition of this AccessRuleCriteria.
        :type: str
        """
        allowed_values = ["URL_IS", "URL_IS_NOT", "URL_STARTS_WITH", "URL_PART_ENDS_WITH", "URL_PART_CONTAINS", "URL_REGEX", "IP_IS", "IP_IS_NOT", "HTTP_HEADER_CONTAINS", "COUNTRY_IS", "COUNTRY_IS_NOT", "USER_AGENT_IS", "USER_AGENT_IS_NOT"]
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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
