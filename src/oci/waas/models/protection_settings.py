# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProtectionSettings(object):
    """
    The settings used for protection rules.
    """

    #: A constant which can be used with the block_action property of a ProtectionSettings.
    #: This constant has a value of "SHOW_ERROR_PAGE"
    BLOCK_ACTION_SHOW_ERROR_PAGE = "SHOW_ERROR_PAGE"

    #: A constant which can be used with the block_action property of a ProtectionSettings.
    #: This constant has a value of "SET_RESPONSE_CODE"
    BLOCK_ACTION_SET_RESPONSE_CODE = "SET_RESPONSE_CODE"

    #: A constant which can be used with the allowed_http_methods property of a ProtectionSettings.
    #: This constant has a value of "OPTIONS"
    ALLOWED_HTTP_METHODS_OPTIONS = "OPTIONS"

    #: A constant which can be used with the allowed_http_methods property of a ProtectionSettings.
    #: This constant has a value of "GET"
    ALLOWED_HTTP_METHODS_GET = "GET"

    #: A constant which can be used with the allowed_http_methods property of a ProtectionSettings.
    #: This constant has a value of "HEAD"
    ALLOWED_HTTP_METHODS_HEAD = "HEAD"

    #: A constant which can be used with the allowed_http_methods property of a ProtectionSettings.
    #: This constant has a value of "POST"
    ALLOWED_HTTP_METHODS_POST = "POST"

    #: A constant which can be used with the allowed_http_methods property of a ProtectionSettings.
    #: This constant has a value of "PUT"
    ALLOWED_HTTP_METHODS_PUT = "PUT"

    #: A constant which can be used with the allowed_http_methods property of a ProtectionSettings.
    #: This constant has a value of "DELETE"
    ALLOWED_HTTP_METHODS_DELETE = "DELETE"

    #: A constant which can be used with the allowed_http_methods property of a ProtectionSettings.
    #: This constant has a value of "TRACE"
    ALLOWED_HTTP_METHODS_TRACE = "TRACE"

    #: A constant which can be used with the allowed_http_methods property of a ProtectionSettings.
    #: This constant has a value of "CONNECT"
    ALLOWED_HTTP_METHODS_CONNECT = "CONNECT"

    #: A constant which can be used with the allowed_http_methods property of a ProtectionSettings.
    #: This constant has a value of "PATCH"
    ALLOWED_HTTP_METHODS_PATCH = "PATCH"

    #: A constant which can be used with the allowed_http_methods property of a ProtectionSettings.
    #: This constant has a value of "PROPFIND"
    ALLOWED_HTTP_METHODS_PROPFIND = "PROPFIND"

    def __init__(self, **kwargs):
        """
        Initializes a new ProtectionSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param block_action:
            The value to assign to the block_action property of this ProtectionSettings.
            Allowed values for this property are: "SHOW_ERROR_PAGE", "SET_RESPONSE_CODE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type block_action: str

        :param block_response_code:
            The value to assign to the block_response_code property of this ProtectionSettings.
        :type block_response_code: int

        :param block_error_page_message:
            The value to assign to the block_error_page_message property of this ProtectionSettings.
        :type block_error_page_message: str

        :param block_error_page_code:
            The value to assign to the block_error_page_code property of this ProtectionSettings.
        :type block_error_page_code: str

        :param block_error_page_description:
            The value to assign to the block_error_page_description property of this ProtectionSettings.
        :type block_error_page_description: str

        :param max_argument_count:
            The value to assign to the max_argument_count property of this ProtectionSettings.
        :type max_argument_count: int

        :param max_name_length_per_argument:
            The value to assign to the max_name_length_per_argument property of this ProtectionSettings.
        :type max_name_length_per_argument: int

        :param max_total_name_length_of_arguments:
            The value to assign to the max_total_name_length_of_arguments property of this ProtectionSettings.
        :type max_total_name_length_of_arguments: int

        :param recommendations_period_in_days:
            The value to assign to the recommendations_period_in_days property of this ProtectionSettings.
        :type recommendations_period_in_days: int

        :param is_response_inspected:
            The value to assign to the is_response_inspected property of this ProtectionSettings.
        :type is_response_inspected: bool

        :param max_response_size_in_ki_b:
            The value to assign to the max_response_size_in_ki_b property of this ProtectionSettings.
        :type max_response_size_in_ki_b: int

        :param allowed_http_methods:
            The value to assign to the allowed_http_methods property of this ProtectionSettings.
            Allowed values for items in this list are: "OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT", "PATCH", "PROPFIND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type allowed_http_methods: list[str]

        :param media_types:
            The value to assign to the media_types property of this ProtectionSettings.
        :type media_types: list[str]

        """
        self.swagger_types = {
            'block_action': 'str',
            'block_response_code': 'int',
            'block_error_page_message': 'str',
            'block_error_page_code': 'str',
            'block_error_page_description': 'str',
            'max_argument_count': 'int',
            'max_name_length_per_argument': 'int',
            'max_total_name_length_of_arguments': 'int',
            'recommendations_period_in_days': 'int',
            'is_response_inspected': 'bool',
            'max_response_size_in_ki_b': 'int',
            'allowed_http_methods': 'list[str]',
            'media_types': 'list[str]'
        }

        self.attribute_map = {
            'block_action': 'blockAction',
            'block_response_code': 'blockResponseCode',
            'block_error_page_message': 'blockErrorPageMessage',
            'block_error_page_code': 'blockErrorPageCode',
            'block_error_page_description': 'blockErrorPageDescription',
            'max_argument_count': 'maxArgumentCount',
            'max_name_length_per_argument': 'maxNameLengthPerArgument',
            'max_total_name_length_of_arguments': 'maxTotalNameLengthOfArguments',
            'recommendations_period_in_days': 'recommendationsPeriodInDays',
            'is_response_inspected': 'isResponseInspected',
            'max_response_size_in_ki_b': 'maxResponseSizeInKiB',
            'allowed_http_methods': 'allowedHttpMethods',
            'media_types': 'mediaTypes'
        }

        self._block_action = None
        self._block_response_code = None
        self._block_error_page_message = None
        self._block_error_page_code = None
        self._block_error_page_description = None
        self._max_argument_count = None
        self._max_name_length_per_argument = None
        self._max_total_name_length_of_arguments = None
        self._recommendations_period_in_days = None
        self._is_response_inspected = None
        self._max_response_size_in_ki_b = None
        self._allowed_http_methods = None
        self._media_types = None

    @property
    def block_action(self):
        """
        Gets the block_action of this ProtectionSettings.
        If `action` is set to `BLOCK`, this specifies how the traffic is blocked when detected as malicious by a protection rule. If unspecified, defaults to `SET_RESPONSE_CODE`.

        Allowed values for this property are: "SHOW_ERROR_PAGE", "SET_RESPONSE_CODE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The block_action of this ProtectionSettings.
        :rtype: str
        """
        return self._block_action

    @block_action.setter
    def block_action(self, block_action):
        """
        Sets the block_action of this ProtectionSettings.
        If `action` is set to `BLOCK`, this specifies how the traffic is blocked when detected as malicious by a protection rule. If unspecified, defaults to `SET_RESPONSE_CODE`.


        :param block_action: The block_action of this ProtectionSettings.
        :type: str
        """
        allowed_values = ["SHOW_ERROR_PAGE", "SET_RESPONSE_CODE"]
        if not value_allowed_none_or_none_sentinel(block_action, allowed_values):
            block_action = 'UNKNOWN_ENUM_VALUE'
        self._block_action = block_action

    @property
    def block_response_code(self):
        """
        Gets the block_response_code of this ProtectionSettings.
        The response code returned when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`. The list of available response codes: `400`, `401`, `403`, `405`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `500`, `501`, `502`, `503`, `504`, `507`.


        :return: The block_response_code of this ProtectionSettings.
        :rtype: int
        """
        return self._block_response_code

    @block_response_code.setter
    def block_response_code(self, block_response_code):
        """
        Sets the block_response_code of this ProtectionSettings.
        The response code returned when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`. The list of available response codes: `400`, `401`, `403`, `405`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `500`, `501`, `502`, `503`, `504`, `507`.


        :param block_response_code: The block_response_code of this ProtectionSettings.
        :type: int
        """
        self._block_response_code = block_response_code

    @property
    def block_error_page_message(self):
        """
        Gets the block_error_page_message of this ProtectionSettings.
        The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to 'Access to the website is blocked.'


        :return: The block_error_page_message of this ProtectionSettings.
        :rtype: str
        """
        return self._block_error_page_message

    @block_error_page_message.setter
    def block_error_page_message(self, block_error_page_message):
        """
        Sets the block_error_page_message of this ProtectionSettings.
        The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to 'Access to the website is blocked.'


        :param block_error_page_message: The block_error_page_message of this ProtectionSettings.
        :type: str
        """
        self._block_error_page_message = block_error_page_message

    @property
    def block_error_page_code(self):
        """
        Gets the block_error_page_code of this ProtectionSettings.
        The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`.


        :return: The block_error_page_code of this ProtectionSettings.
        :rtype: str
        """
        return self._block_error_page_code

    @block_error_page_code.setter
    def block_error_page_code(self, block_error_page_code):
        """
        Sets the block_error_page_code of this ProtectionSettings.
        The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`.


        :param block_error_page_code: The block_error_page_code of this ProtectionSettings.
        :type: str
        """
        self._block_error_page_code = block_error_page_code

    @property
    def block_error_page_description(self):
        """
        Gets the block_error_page_description of this ProtectionSettings.
        The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `Access blocked by website owner. Please contact support.`


        :return: The block_error_page_description of this ProtectionSettings.
        :rtype: str
        """
        return self._block_error_page_description

    @block_error_page_description.setter
    def block_error_page_description(self, block_error_page_description):
        """
        Sets the block_error_page_description of this ProtectionSettings.
        The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `Access blocked by website owner. Please contact support.`


        :param block_error_page_description: The block_error_page_description of this ProtectionSettings.
        :type: str
        """
        self._block_error_page_description = block_error_page_description

    @property
    def max_argument_count(self):
        """
        Gets the max_argument_count of this ProtectionSettings.
        The maximum number of arguments allowed to be passed to your application before an action is taken. Arguements are query parameters or body parameters in a PUT or POST request. If unspecified, defaults to `255`. This setting only applies if a corresponding protection rule is enabled, such as the \"Number of Arguments Limits\" rule (key: 960335).

        Example: If `maxArgumentCount` to `2` for the Max Number of Arguments protection rule (key: 960335), the following requests would be blocked:
        `GET /myapp/path?query=one&query=two&query=three`
        `POST /myapp/path` with Body `{\"argument1\":\"one\",\"argument2\":\"two\",\"argument3\":\"three\"}`


        :return: The max_argument_count of this ProtectionSettings.
        :rtype: int
        """
        return self._max_argument_count

    @max_argument_count.setter
    def max_argument_count(self, max_argument_count):
        """
        Sets the max_argument_count of this ProtectionSettings.
        The maximum number of arguments allowed to be passed to your application before an action is taken. Arguements are query parameters or body parameters in a PUT or POST request. If unspecified, defaults to `255`. This setting only applies if a corresponding protection rule is enabled, such as the \"Number of Arguments Limits\" rule (key: 960335).

        Example: If `maxArgumentCount` to `2` for the Max Number of Arguments protection rule (key: 960335), the following requests would be blocked:
        `GET /myapp/path?query=one&query=two&query=three`
        `POST /myapp/path` with Body `{\"argument1\":\"one\",\"argument2\":\"two\",\"argument3\":\"three\"}`


        :param max_argument_count: The max_argument_count of this ProtectionSettings.
        :type: int
        """
        self._max_argument_count = max_argument_count

    @property
    def max_name_length_per_argument(self):
        """
        Gets the max_name_length_per_argument of this ProtectionSettings.
        The maximum length allowed for each argument name, in characters. Arguements are query parameters or body parameters in a PUT or POST request. If unspecified, defaults to `400`. This setting only applies if a corresponding protection rule is enabled, such as the \"Values Limits\" rule (key: 960208).


        :return: The max_name_length_per_argument of this ProtectionSettings.
        :rtype: int
        """
        return self._max_name_length_per_argument

    @max_name_length_per_argument.setter
    def max_name_length_per_argument(self, max_name_length_per_argument):
        """
        Sets the max_name_length_per_argument of this ProtectionSettings.
        The maximum length allowed for each argument name, in characters. Arguements are query parameters or body parameters in a PUT or POST request. If unspecified, defaults to `400`. This setting only applies if a corresponding protection rule is enabled, such as the \"Values Limits\" rule (key: 960208).


        :param max_name_length_per_argument: The max_name_length_per_argument of this ProtectionSettings.
        :type: int
        """
        self._max_name_length_per_argument = max_name_length_per_argument

    @property
    def max_total_name_length_of_arguments(self):
        """
        Gets the max_total_name_length_of_arguments of this ProtectionSettings.
        The maximum length allowed for the sum of the argument name and value, in characters. Arguements are query parameters or body parameters in a PUT or POST request. If unspecified, defaults to `64000`. This setting only applies if a corresponding protection rule is enabled, such as the \"Total Arguments Limits\" rule (key: 960341).


        :return: The max_total_name_length_of_arguments of this ProtectionSettings.
        :rtype: int
        """
        return self._max_total_name_length_of_arguments

    @max_total_name_length_of_arguments.setter
    def max_total_name_length_of_arguments(self, max_total_name_length_of_arguments):
        """
        Sets the max_total_name_length_of_arguments of this ProtectionSettings.
        The maximum length allowed for the sum of the argument name and value, in characters. Arguements are query parameters or body parameters in a PUT or POST request. If unspecified, defaults to `64000`. This setting only applies if a corresponding protection rule is enabled, such as the \"Total Arguments Limits\" rule (key: 960341).


        :param max_total_name_length_of_arguments: The max_total_name_length_of_arguments of this ProtectionSettings.
        :type: int
        """
        self._max_total_name_length_of_arguments = max_total_name_length_of_arguments

    @property
    def recommendations_period_in_days(self):
        """
        Gets the recommendations_period_in_days of this ProtectionSettings.
        The length of time to analyze traffic traffic, in days. After the analysis period, `WafRecommendations` will be populated. If unspecified, defaults to `10`.

        Use `GET /waasPolicies/{waasPolicyId}/wafRecommendations` to view WAF recommendations.


        :return: The recommendations_period_in_days of this ProtectionSettings.
        :rtype: int
        """
        return self._recommendations_period_in_days

    @recommendations_period_in_days.setter
    def recommendations_period_in_days(self, recommendations_period_in_days):
        """
        Sets the recommendations_period_in_days of this ProtectionSettings.
        The length of time to analyze traffic traffic, in days. After the analysis period, `WafRecommendations` will be populated. If unspecified, defaults to `10`.

        Use `GET /waasPolicies/{waasPolicyId}/wafRecommendations` to view WAF recommendations.


        :param recommendations_period_in_days: The recommendations_period_in_days of this ProtectionSettings.
        :type: int
        """
        self._recommendations_period_in_days = recommendations_period_in_days

    @property
    def is_response_inspected(self):
        """
        Gets the is_response_inspected of this ProtectionSettings.
        Inspects the response body of origin responses. Can be used to detect leakage of sensitive data. If unspecified, defaults to `false`.

        **Note:** Only origin responses with a Content-Type matching a value in `mediaTypes` will be inspected.


        :return: The is_response_inspected of this ProtectionSettings.
        :rtype: bool
        """
        return self._is_response_inspected

    @is_response_inspected.setter
    def is_response_inspected(self, is_response_inspected):
        """
        Sets the is_response_inspected of this ProtectionSettings.
        Inspects the response body of origin responses. Can be used to detect leakage of sensitive data. If unspecified, defaults to `false`.

        **Note:** Only origin responses with a Content-Type matching a value in `mediaTypes` will be inspected.


        :param is_response_inspected: The is_response_inspected of this ProtectionSettings.
        :type: bool
        """
        self._is_response_inspected = is_response_inspected

    @property
    def max_response_size_in_ki_b(self):
        """
        Gets the max_response_size_in_ki_b of this ProtectionSettings.
        The maximum response size to be fully inspected, in binary kilobytes (KiB). Anything over this limit will be partially inspected. If unspecified, defaults to `1024`.


        :return: The max_response_size_in_ki_b of this ProtectionSettings.
        :rtype: int
        """
        return self._max_response_size_in_ki_b

    @max_response_size_in_ki_b.setter
    def max_response_size_in_ki_b(self, max_response_size_in_ki_b):
        """
        Sets the max_response_size_in_ki_b of this ProtectionSettings.
        The maximum response size to be fully inspected, in binary kilobytes (KiB). Anything over this limit will be partially inspected. If unspecified, defaults to `1024`.


        :param max_response_size_in_ki_b: The max_response_size_in_ki_b of this ProtectionSettings.
        :type: int
        """
        self._max_response_size_in_ki_b = max_response_size_in_ki_b

    @property
    def allowed_http_methods(self):
        """
        Gets the allowed_http_methods of this ProtectionSettings.
        The list of allowed HTTP methods. If unspecified, default to `[OPTIONS, GET, HEAD, POST]`. This setting only applies if a corresponding protection rule is enabled, such as the \"Restrict HTTP Request Methods\" rule (key: 911100).

        Allowed values for items in this list are: "OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT", "PATCH", "PROPFIND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The allowed_http_methods of this ProtectionSettings.
        :rtype: list[str]
        """
        return self._allowed_http_methods

    @allowed_http_methods.setter
    def allowed_http_methods(self, allowed_http_methods):
        """
        Sets the allowed_http_methods of this ProtectionSettings.
        The list of allowed HTTP methods. If unspecified, default to `[OPTIONS, GET, HEAD, POST]`. This setting only applies if a corresponding protection rule is enabled, such as the \"Restrict HTTP Request Methods\" rule (key: 911100).


        :param allowed_http_methods: The allowed_http_methods of this ProtectionSettings.
        :type: list[str]
        """
        allowed_values = ["OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT", "PATCH", "PROPFIND"]
        if allowed_http_methods:
            allowed_http_methods[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in allowed_http_methods]
        self._allowed_http_methods = allowed_http_methods

    @property
    def media_types(self):
        """
        Gets the media_types of this ProtectionSettings.
        The list of media types to allow for inspection, if `isResponseInspected` is enabled. Only responses with MIME types in this list will be inspected. If unspecified, defaults to `[\"text/html\", \"text/plain\", \"text/xml\"]`.

            Supported MIME types include:

            - text/html
            - text/plain
            - text/asp
            - text/css
            - text/x-script
            - application/json
            - text/webviewhtml
            - text/x-java-source
            - application/x-javascript
            - application/javascript
            - application/ecmascript
            - text/javascript
            - text/ecmascript
            - text/x-script.perl
            - text/x-script.phyton
            - application/plain
            - application/xml
            - text/xml


        :return: The media_types of this ProtectionSettings.
        :rtype: list[str]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """
        Sets the media_types of this ProtectionSettings.
        The list of media types to allow for inspection, if `isResponseInspected` is enabled. Only responses with MIME types in this list will be inspected. If unspecified, defaults to `[\"text/html\", \"text/plain\", \"text/xml\"]`.

            Supported MIME types include:

            - text/html
            - text/plain
            - text/asp
            - text/css
            - text/x-script
            - application/json
            - text/webviewhtml
            - text/x-java-source
            - application/x-javascript
            - application/javascript
            - application/ecmascript
            - text/javascript
            - text/ecmascript
            - text/x-script.perl
            - text/x-script.phyton
            - application/plain
            - application/xml
            - text/xml


        :param media_types: The media_types of this ProtectionSettings.
        :type: list[str]
        """
        self._media_types = media_types

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
