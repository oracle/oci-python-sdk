# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessRule(object):
    """
    A content access rule. An access rule specifies an action to take if a set of criteria is matched by a request.
    """

    #: A constant which can be used with the action property of a AccessRule.
    #: This constant has a value of "ALLOW"
    ACTION_ALLOW = "ALLOW"

    #: A constant which can be used with the action property of a AccessRule.
    #: This constant has a value of "DETECT"
    ACTION_DETECT = "DETECT"

    #: A constant which can be used with the action property of a AccessRule.
    #: This constant has a value of "BLOCK"
    ACTION_BLOCK = "BLOCK"

    #: A constant which can be used with the action property of a AccessRule.
    #: This constant has a value of "BYPASS"
    ACTION_BYPASS = "BYPASS"

    #: A constant which can be used with the action property of a AccessRule.
    #: This constant has a value of "REDIRECT"
    ACTION_REDIRECT = "REDIRECT"

    #: A constant which can be used with the action property of a AccessRule.
    #: This constant has a value of "SHOW_CAPTCHA"
    ACTION_SHOW_CAPTCHA = "SHOW_CAPTCHA"

    #: A constant which can be used with the block_action property of a AccessRule.
    #: This constant has a value of "SET_RESPONSE_CODE"
    BLOCK_ACTION_SET_RESPONSE_CODE = "SET_RESPONSE_CODE"

    #: A constant which can be used with the block_action property of a AccessRule.
    #: This constant has a value of "SHOW_ERROR_PAGE"
    BLOCK_ACTION_SHOW_ERROR_PAGE = "SHOW_ERROR_PAGE"

    #: A constant which can be used with the bypass_challenges property of a AccessRule.
    #: This constant has a value of "JS_CHALLENGE"
    BYPASS_CHALLENGES_JS_CHALLENGE = "JS_CHALLENGE"

    #: A constant which can be used with the bypass_challenges property of a AccessRule.
    #: This constant has a value of "DEVICE_FINGERPRINT_CHALLENGE"
    BYPASS_CHALLENGES_DEVICE_FINGERPRINT_CHALLENGE = "DEVICE_FINGERPRINT_CHALLENGE"

    #: A constant which can be used with the bypass_challenges property of a AccessRule.
    #: This constant has a value of "HUMAN_INTERACTION_CHALLENGE"
    BYPASS_CHALLENGES_HUMAN_INTERACTION_CHALLENGE = "HUMAN_INTERACTION_CHALLENGE"

    #: A constant which can be used with the bypass_challenges property of a AccessRule.
    #: This constant has a value of "CAPTCHA"
    BYPASS_CHALLENGES_CAPTCHA = "CAPTCHA"

    #: A constant which can be used with the redirect_response_code property of a AccessRule.
    #: This constant has a value of "MOVED_PERMANENTLY"
    REDIRECT_RESPONSE_CODE_MOVED_PERMANENTLY = "MOVED_PERMANENTLY"

    #: A constant which can be used with the redirect_response_code property of a AccessRule.
    #: This constant has a value of "FOUND"
    REDIRECT_RESPONSE_CODE_FOUND = "FOUND"

    def __init__(self, **kwargs):
        """
        Initializes a new AccessRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AccessRule.
        :type name: str

        :param criteria:
            The value to assign to the criteria property of this AccessRule.
        :type criteria: list[oci.waas.models.AccessRuleCriteria]

        :param action:
            The value to assign to the action property of this AccessRule.
            Allowed values for this property are: "ALLOW", "DETECT", "BLOCK", "BYPASS", "REDIRECT", "SHOW_CAPTCHA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param block_action:
            The value to assign to the block_action property of this AccessRule.
            Allowed values for this property are: "SET_RESPONSE_CODE", "SHOW_ERROR_PAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type block_action: str

        :param block_response_code:
            The value to assign to the block_response_code property of this AccessRule.
        :type block_response_code: int

        :param block_error_page_message:
            The value to assign to the block_error_page_message property of this AccessRule.
        :type block_error_page_message: str

        :param block_error_page_code:
            The value to assign to the block_error_page_code property of this AccessRule.
        :type block_error_page_code: str

        :param block_error_page_description:
            The value to assign to the block_error_page_description property of this AccessRule.
        :type block_error_page_description: str

        :param bypass_challenges:
            The value to assign to the bypass_challenges property of this AccessRule.
            Allowed values for items in this list are: "JS_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "HUMAN_INTERACTION_CHALLENGE", "CAPTCHA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type bypass_challenges: list[str]

        :param redirect_url:
            The value to assign to the redirect_url property of this AccessRule.
        :type redirect_url: str

        :param redirect_response_code:
            The value to assign to the redirect_response_code property of this AccessRule.
            Allowed values for this property are: "MOVED_PERMANENTLY", "FOUND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type redirect_response_code: str

        :param captcha_title:
            The value to assign to the captcha_title property of this AccessRule.
        :type captcha_title: str

        :param captcha_header:
            The value to assign to the captcha_header property of this AccessRule.
        :type captcha_header: str

        :param captcha_footer:
            The value to assign to the captcha_footer property of this AccessRule.
        :type captcha_footer: str

        :param captcha_submit_label:
            The value to assign to the captcha_submit_label property of this AccessRule.
        :type captcha_submit_label: str

        :param response_header_manipulation:
            The value to assign to the response_header_manipulation property of this AccessRule.
        :type response_header_manipulation: list[oci.waas.models.HeaderManipulationAction]

        """
        self.swagger_types = {
            'name': 'str',
            'criteria': 'list[AccessRuleCriteria]',
            'action': 'str',
            'block_action': 'str',
            'block_response_code': 'int',
            'block_error_page_message': 'str',
            'block_error_page_code': 'str',
            'block_error_page_description': 'str',
            'bypass_challenges': 'list[str]',
            'redirect_url': 'str',
            'redirect_response_code': 'str',
            'captcha_title': 'str',
            'captcha_header': 'str',
            'captcha_footer': 'str',
            'captcha_submit_label': 'str',
            'response_header_manipulation': 'list[HeaderManipulationAction]'
        }

        self.attribute_map = {
            'name': 'name',
            'criteria': 'criteria',
            'action': 'action',
            'block_action': 'blockAction',
            'block_response_code': 'blockResponseCode',
            'block_error_page_message': 'blockErrorPageMessage',
            'block_error_page_code': 'blockErrorPageCode',
            'block_error_page_description': 'blockErrorPageDescription',
            'bypass_challenges': 'bypassChallenges',
            'redirect_url': 'redirectUrl',
            'redirect_response_code': 'redirectResponseCode',
            'captcha_title': 'captchaTitle',
            'captcha_header': 'captchaHeader',
            'captcha_footer': 'captchaFooter',
            'captcha_submit_label': 'captchaSubmitLabel',
            'response_header_manipulation': 'responseHeaderManipulation'
        }

        self._name = None
        self._criteria = None
        self._action = None
        self._block_action = None
        self._block_response_code = None
        self._block_error_page_message = None
        self._block_error_page_code = None
        self._block_error_page_description = None
        self._bypass_challenges = None
        self._redirect_url = None
        self._redirect_response_code = None
        self._captcha_title = None
        self._captcha_header = None
        self._captcha_footer = None
        self._captcha_submit_label = None
        self._response_header_manipulation = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AccessRule.
        The unique name of the access rule.


        :return: The name of this AccessRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AccessRule.
        The unique name of the access rule.


        :param name: The name of this AccessRule.
        :type: str
        """
        self._name = name

    @property
    def criteria(self):
        """
        **[Required]** Gets the criteria of this AccessRule.
        The list of access rule criteria. The rule would be applied only for the requests that matched all the listed conditions.


        :return: The criteria of this AccessRule.
        :rtype: list[oci.waas.models.AccessRuleCriteria]
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """
        Sets the criteria of this AccessRule.
        The list of access rule criteria. The rule would be applied only for the requests that matched all the listed conditions.


        :param criteria: The criteria of this AccessRule.
        :type: list[oci.waas.models.AccessRuleCriteria]
        """
        self._criteria = criteria

    @property
    def action(self):
        """
        **[Required]** Gets the action of this AccessRule.
        The action to take when the access criteria are met for a rule. If unspecified, defaults to `ALLOW`.

        - **ALLOW:** Takes no action, just logs the request.

        - **DETECT:** Takes no action, but creates an alert for the request.

        - **BLOCK:** Blocks the request by returning specified response code or showing error page.

        - **BYPASS:** Bypasses some or all challenges.

        - **REDIRECT:** Redirects the request to the specified URL. These fields are required when `REDIRECT` is selected: `redirectUrl`, `redirectResponseCode`.

        - **SHOW_CAPTCHA:** Show a CAPTCHA Challenge page instead of the requested page.

        Regardless of action, no further rules are processed once a rule is matched.

        Allowed values for this property are: "ALLOW", "DETECT", "BLOCK", "BYPASS", "REDIRECT", "SHOW_CAPTCHA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this AccessRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this AccessRule.
        The action to take when the access criteria are met for a rule. If unspecified, defaults to `ALLOW`.

        - **ALLOW:** Takes no action, just logs the request.

        - **DETECT:** Takes no action, but creates an alert for the request.

        - **BLOCK:** Blocks the request by returning specified response code or showing error page.

        - **BYPASS:** Bypasses some or all challenges.

        - **REDIRECT:** Redirects the request to the specified URL. These fields are required when `REDIRECT` is selected: `redirectUrl`, `redirectResponseCode`.

        - **SHOW_CAPTCHA:** Show a CAPTCHA Challenge page instead of the requested page.

        Regardless of action, no further rules are processed once a rule is matched.


        :param action: The action of this AccessRule.
        :type: str
        """
        allowed_values = ["ALLOW", "DETECT", "BLOCK", "BYPASS", "REDIRECT", "SHOW_CAPTCHA"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def block_action(self):
        """
        Gets the block_action of this AccessRule.
        The method used to block requests if `action` is set to `BLOCK` and the access criteria are met. If unspecified, defaults to `SET_RESPONSE_CODE`.

        Allowed values for this property are: "SET_RESPONSE_CODE", "SHOW_ERROR_PAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The block_action of this AccessRule.
        :rtype: str
        """
        return self._block_action

    @block_action.setter
    def block_action(self, block_action):
        """
        Sets the block_action of this AccessRule.
        The method used to block requests if `action` is set to `BLOCK` and the access criteria are met. If unspecified, defaults to `SET_RESPONSE_CODE`.


        :param block_action: The block_action of this AccessRule.
        :type: str
        """
        allowed_values = ["SET_RESPONSE_CODE", "SHOW_ERROR_PAGE"]
        if not value_allowed_none_or_none_sentinel(block_action, allowed_values):
            block_action = 'UNKNOWN_ENUM_VALUE'
        self._block_action = block_action

    @property
    def block_response_code(self):
        """
        Gets the block_response_code of this AccessRule.
        The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the access criteria are met. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.


        :return: The block_response_code of this AccessRule.
        :rtype: int
        """
        return self._block_response_code

    @block_response_code.setter
    def block_response_code(self, block_response_code):
        """
        Sets the block_response_code of this AccessRule.
        The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the access criteria are met. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.


        :param block_response_code: The block_response_code of this AccessRule.
        :type: int
        """
        self._block_response_code = block_response_code

    @property
    def block_error_page_message(self):
        """
        Gets the block_error_page_message of this AccessRule.
        The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access to the website is blocked.'


        :return: The block_error_page_message of this AccessRule.
        :rtype: str
        """
        return self._block_error_page_message

    @block_error_page_message.setter
    def block_error_page_message(self, block_error_page_message):
        """
        Sets the block_error_page_message of this AccessRule.
        The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access to the website is blocked.'


        :param block_error_page_message: The block_error_page_message of this AccessRule.
        :type: str
        """
        self._block_error_page_message = block_error_page_message

    @property
    def block_error_page_code(self):
        """
        Gets the block_error_page_code of this AccessRule.
        The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access rules'.


        :return: The block_error_page_code of this AccessRule.
        :rtype: str
        """
        return self._block_error_page_code

    @block_error_page_code.setter
    def block_error_page_code(self, block_error_page_code):
        """
        Sets the block_error_page_code of this AccessRule.
        The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access rules'.


        :param block_error_page_code: The block_error_page_code of this AccessRule.
        :type: str
        """
        self._block_error_page_code = block_error_page_code

    @property
    def block_error_page_description(self):
        """
        Gets the block_error_page_description of this AccessRule.
        The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access blocked by website owner. Please contact support.'


        :return: The block_error_page_description of this AccessRule.
        :rtype: str
        """
        return self._block_error_page_description

    @block_error_page_description.setter
    def block_error_page_description(self, block_error_page_description):
        """
        Sets the block_error_page_description of this AccessRule.
        The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access criteria are met. If unspecified, defaults to 'Access blocked by website owner. Please contact support.'


        :param block_error_page_description: The block_error_page_description of this AccessRule.
        :type: str
        """
        self._block_error_page_description = block_error_page_description

    @property
    def bypass_challenges(self):
        """
        Gets the bypass_challenges of this AccessRule.
        The list of challenges to bypass when `action` is set to `BYPASS`. If unspecified or empty, all challenges are bypassed.

        - **JS_CHALLENGE:** Bypasses JavaScript Challenge.

        - **DEVICE_FINGERPRINT_CHALLENGE:** Bypasses Device Fingerprint Challenge.

        - **HUMAN_INTERACTION_CHALLENGE:** Bypasses Human Interaction Challenge.

        - **CAPTCHA:** Bypasses CAPTCHA Challenge.

        Allowed values for items in this list are: "JS_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "HUMAN_INTERACTION_CHALLENGE", "CAPTCHA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The bypass_challenges of this AccessRule.
        :rtype: list[str]
        """
        return self._bypass_challenges

    @bypass_challenges.setter
    def bypass_challenges(self, bypass_challenges):
        """
        Sets the bypass_challenges of this AccessRule.
        The list of challenges to bypass when `action` is set to `BYPASS`. If unspecified or empty, all challenges are bypassed.

        - **JS_CHALLENGE:** Bypasses JavaScript Challenge.

        - **DEVICE_FINGERPRINT_CHALLENGE:** Bypasses Device Fingerprint Challenge.

        - **HUMAN_INTERACTION_CHALLENGE:** Bypasses Human Interaction Challenge.

        - **CAPTCHA:** Bypasses CAPTCHA Challenge.


        :param bypass_challenges: The bypass_challenges of this AccessRule.
        :type: list[str]
        """
        allowed_values = ["JS_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "HUMAN_INTERACTION_CHALLENGE", "CAPTCHA"]
        if bypass_challenges:
            bypass_challenges[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in bypass_challenges]
        self._bypass_challenges = bypass_challenges

    @property
    def redirect_url(self):
        """
        Gets the redirect_url of this AccessRule.
        The target to which the request should be redirected, represented as a URI reference. Required when `action` is `REDIRECT`.


        :return: The redirect_url of this AccessRule.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """
        Sets the redirect_url of this AccessRule.
        The target to which the request should be redirected, represented as a URI reference. Required when `action` is `REDIRECT`.


        :param redirect_url: The redirect_url of this AccessRule.
        :type: str
        """
        self._redirect_url = redirect_url

    @property
    def redirect_response_code(self):
        """
        Gets the redirect_response_code of this AccessRule.
        The response status code to return when `action` is set to `REDIRECT`.

        - **MOVED_PERMANENTLY:** Used for designating the permanent movement of a page (numerical code - 301).

        - **FOUND:** Used for designating the temporary movement of a page (numerical code - 302).

        Allowed values for this property are: "MOVED_PERMANENTLY", "FOUND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The redirect_response_code of this AccessRule.
        :rtype: str
        """
        return self._redirect_response_code

    @redirect_response_code.setter
    def redirect_response_code(self, redirect_response_code):
        """
        Sets the redirect_response_code of this AccessRule.
        The response status code to return when `action` is set to `REDIRECT`.

        - **MOVED_PERMANENTLY:** Used for designating the permanent movement of a page (numerical code - 301).

        - **FOUND:** Used for designating the temporary movement of a page (numerical code - 302).


        :param redirect_response_code: The redirect_response_code of this AccessRule.
        :type: str
        """
        allowed_values = ["MOVED_PERMANENTLY", "FOUND"]
        if not value_allowed_none_or_none_sentinel(redirect_response_code, allowed_values):
            redirect_response_code = 'UNKNOWN_ENUM_VALUE'
        self._redirect_response_code = redirect_response_code

    @property
    def captcha_title(self):
        """
        Gets the captcha_title of this AccessRule.
        The title used when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.


        :return: The captcha_title of this AccessRule.
        :rtype: str
        """
        return self._captcha_title

    @captcha_title.setter
    def captcha_title(self, captcha_title):
        """
        Sets the captcha_title of this AccessRule.
        The title used when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.


        :param captcha_title: The captcha_title of this AccessRule.
        :type: str
        """
        self._captcha_title = captcha_title

    @property
    def captcha_header(self):
        """
        Gets the captcha_header of this AccessRule.
        The text to show in the header when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.


        :return: The captcha_header of this AccessRule.
        :rtype: str
        """
        return self._captcha_header

    @captcha_header.setter
    def captcha_header(self, captcha_header):
        """
        Sets the captcha_header of this AccessRule.
        The text to show in the header when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.


        :param captcha_header: The captcha_header of this AccessRule.
        :type: str
        """
        self._captcha_header = captcha_header

    @property
    def captcha_footer(self):
        """
        Gets the captcha_footer of this AccessRule.
        The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.


        :return: The captcha_footer of this AccessRule.
        :rtype: str
        """
        return self._captcha_footer

    @captcha_footer.setter
    def captcha_footer(self, captcha_footer):
        """
        Sets the captcha_footer of this AccessRule.
        The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.


        :param captcha_footer: The captcha_footer of this AccessRule.
        :type: str
        """
        self._captcha_footer = captcha_footer

    @property
    def captcha_submit_label(self):
        """
        Gets the captcha_submit_label of this AccessRule.
        The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `SHOW_CAPTCHA` and the request is challenged.


        :return: The captcha_submit_label of this AccessRule.
        :rtype: str
        """
        return self._captcha_submit_label

    @captcha_submit_label.setter
    def captcha_submit_label(self, captcha_submit_label):
        """
        Sets the captcha_submit_label of this AccessRule.
        The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `SHOW_CAPTCHA` and the request is challenged.


        :param captcha_submit_label: The captcha_submit_label of this AccessRule.
        :type: str
        """
        self._captcha_submit_label = captcha_submit_label

    @property
    def response_header_manipulation(self):
        """
        Gets the response_header_manipulation of this AccessRule.
        An object that represents an action to apply to an HTTP response headers if all rule criteria will be matched regardless of `action` value.


        :return: The response_header_manipulation of this AccessRule.
        :rtype: list[oci.waas.models.HeaderManipulationAction]
        """
        return self._response_header_manipulation

    @response_header_manipulation.setter
    def response_header_manipulation(self, response_header_manipulation):
        """
        Sets the response_header_manipulation of this AccessRule.
        An object that represents an action to apply to an HTTP response headers if all rule criteria will be matched regardless of `action` value.


        :param response_header_manipulation: The response_header_manipulation of this AccessRule.
        :type: list[oci.waas.models.HeaderManipulationAction]
        """
        self._response_header_manipulation = response_header_manipulation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
