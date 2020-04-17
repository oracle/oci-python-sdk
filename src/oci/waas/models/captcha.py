# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Captcha(object):
    """
    The settings of the CAPTCHA challenge. If a specific URL should be accessed only by a human, a CAPTCHA challenge can be placed at the URL to protect the web application from bots.

    *Warning:* Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Captcha object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param url:
            The value to assign to the url property of this Captcha.
        :type url: str

        :param session_expiration_in_seconds:
            The value to assign to the session_expiration_in_seconds property of this Captcha.
        :type session_expiration_in_seconds: int

        :param title:
            The value to assign to the title property of this Captcha.
        :type title: str

        :param header_text:
            The value to assign to the header_text property of this Captcha.
        :type header_text: str

        :param footer_text:
            The value to assign to the footer_text property of this Captcha.
        :type footer_text: str

        :param failure_message:
            The value to assign to the failure_message property of this Captcha.
        :type failure_message: str

        :param submit_label:
            The value to assign to the submit_label property of this Captcha.
        :type submit_label: str

        """
        self.swagger_types = {
            'url': 'str',
            'session_expiration_in_seconds': 'int',
            'title': 'str',
            'header_text': 'str',
            'footer_text': 'str',
            'failure_message': 'str',
            'submit_label': 'str'
        }

        self.attribute_map = {
            'url': 'url',
            'session_expiration_in_seconds': 'sessionExpirationInSeconds',
            'title': 'title',
            'header_text': 'headerText',
            'footer_text': 'footerText',
            'failure_message': 'failureMessage',
            'submit_label': 'submitLabel'
        }

        self._url = None
        self._session_expiration_in_seconds = None
        self._title = None
        self._header_text = None
        self._footer_text = None
        self._failure_message = None
        self._submit_label = None

    @property
    def url(self):
        """
        **[Required]** Gets the url of this Captcha.
        The unique URL path at which to show the CAPTCHA challenge.


        :return: The url of this Captcha.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Captcha.
        The unique URL path at which to show the CAPTCHA challenge.


        :param url: The url of this Captcha.
        :type: str
        """
        self._url = url

    @property
    def session_expiration_in_seconds(self):
        """
        **[Required]** Gets the session_expiration_in_seconds of this Captcha.
        The amount of time before the CAPTCHA expires, in seconds. If unspecified, defaults to `300`.


        :return: The session_expiration_in_seconds of this Captcha.
        :rtype: int
        """
        return self._session_expiration_in_seconds

    @session_expiration_in_seconds.setter
    def session_expiration_in_seconds(self, session_expiration_in_seconds):
        """
        Sets the session_expiration_in_seconds of this Captcha.
        The amount of time before the CAPTCHA expires, in seconds. If unspecified, defaults to `300`.


        :param session_expiration_in_seconds: The session_expiration_in_seconds of this Captcha.
        :type: int
        """
        self._session_expiration_in_seconds = session_expiration_in_seconds

    @property
    def title(self):
        """
        **[Required]** Gets the title of this Captcha.
        The title used when displaying a CAPTCHA challenge. If unspecified, defaults to `Are you human?`


        :return: The title of this Captcha.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Captcha.
        The title used when displaying a CAPTCHA challenge. If unspecified, defaults to `Are you human?`


        :param title: The title of this Captcha.
        :type: str
        """
        self._title = title

    @property
    def header_text(self):
        """
        Gets the header_text of this Captcha.
        The text to show in the header when showing a CAPTCHA challenge. If unspecified, defaults to 'We have detected an increased number of attempts to access this website. To help us keep this site secure, please let us know that you are not a robot by entering the text from the image below.'


        :return: The header_text of this Captcha.
        :rtype: str
        """
        return self._header_text

    @header_text.setter
    def header_text(self, header_text):
        """
        Sets the header_text of this Captcha.
        The text to show in the header when showing a CAPTCHA challenge. If unspecified, defaults to 'We have detected an increased number of attempts to access this website. To help us keep this site secure, please let us know that you are not a robot by entering the text from the image below.'


        :param header_text: The header_text of this Captcha.
        :type: str
        """
        self._header_text = header_text

    @property
    def footer_text(self):
        """
        Gets the footer_text of this Captcha.
        The text to show in the footer when showing a CAPTCHA challenge. If unspecified, defaults to 'Enter the letters and numbers as they are shown in the image above.'


        :return: The footer_text of this Captcha.
        :rtype: str
        """
        return self._footer_text

    @footer_text.setter
    def footer_text(self, footer_text):
        """
        Sets the footer_text of this Captcha.
        The text to show in the footer when showing a CAPTCHA challenge. If unspecified, defaults to 'Enter the letters and numbers as they are shown in the image above.'


        :param footer_text: The footer_text of this Captcha.
        :type: str
        """
        self._footer_text = footer_text

    @property
    def failure_message(self):
        """
        **[Required]** Gets the failure_message of this Captcha.
        The text to show when incorrect CAPTCHA text is entered. If unspecified, defaults to `The CAPTCHA was incorrect. Try again.`


        :return: The failure_message of this Captcha.
        :rtype: str
        """
        return self._failure_message

    @failure_message.setter
    def failure_message(self, failure_message):
        """
        Sets the failure_message of this Captcha.
        The text to show when incorrect CAPTCHA text is entered. If unspecified, defaults to `The CAPTCHA was incorrect. Try again.`


        :param failure_message: The failure_message of this Captcha.
        :type: str
        """
        self._failure_message = failure_message

    @property
    def submit_label(self):
        """
        **[Required]** Gets the submit_label of this Captcha.
        The text to show on the label of the CAPTCHA challenge submit button. If unspecified, defaults to `Yes, I am human`.


        :return: The submit_label of this Captcha.
        :rtype: str
        """
        return self._submit_label

    @submit_label.setter
    def submit_label(self, submit_label):
        """
        Sets the submit_label of this Captcha.
        The text to show on the label of the CAPTCHA challenge submit button. If unspecified, defaults to `Yes, I am human`.


        :param submit_label: The submit_label of this Captcha.
        :type: str
        """
        self._submit_label = submit_label

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
