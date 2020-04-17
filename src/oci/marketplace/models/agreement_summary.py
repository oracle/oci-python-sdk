# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AgreementSummary(object):
    """
    The model for a summary of an end user license agreement.
    """

    #: A constant which can be used with the author property of a AgreementSummary.
    #: This constant has a value of "ORACLE"
    AUTHOR_ORACLE = "ORACLE"

    #: A constant which can be used with the author property of a AgreementSummary.
    #: This constant has a value of "PARTNER"
    AUTHOR_PARTNER = "PARTNER"

    #: A constant which can be used with the author property of a AgreementSummary.
    #: This constant has a value of "PII"
    AUTHOR_PII = "PII"

    def __init__(self, **kwargs):
        """
        Initializes a new AgreementSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AgreementSummary.
        :type id: str

        :param content_url:
            The value to assign to the content_url property of this AgreementSummary.
        :type content_url: str

        :param author:
            The value to assign to the author property of this AgreementSummary.
            Allowed values for this property are: "ORACLE", "PARTNER", "PII", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type author: str

        :param prompt:
            The value to assign to the prompt property of this AgreementSummary.
        :type prompt: str

        """
        self.swagger_types = {
            'id': 'str',
            'content_url': 'str',
            'author': 'str',
            'prompt': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'content_url': 'contentUrl',
            'author': 'author',
            'prompt': 'prompt'
        }

        self._id = None
        self._content_url = None
        self._author = None
        self._prompt = None

    @property
    def id(self):
        """
        Gets the id of this AgreementSummary.
        The unique identifier for the agreement.


        :return: The id of this AgreementSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AgreementSummary.
        The unique identifier for the agreement.


        :param id: The id of this AgreementSummary.
        :type: str
        """
        self._id = id

    @property
    def content_url(self):
        """
        Gets the content_url of this AgreementSummary.
        The content URL of the agreement.


        :return: The content_url of this AgreementSummary.
        :rtype: str
        """
        return self._content_url

    @content_url.setter
    def content_url(self, content_url):
        """
        Sets the content_url of this AgreementSummary.
        The content URL of the agreement.


        :param content_url: The content_url of this AgreementSummary.
        :type: str
        """
        self._content_url = content_url

    @property
    def author(self):
        """
        Gets the author of this AgreementSummary.
        Who authored the agreement.

        Allowed values for this property are: "ORACLE", "PARTNER", "PII", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The author of this AgreementSummary.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this AgreementSummary.
        Who authored the agreement.


        :param author: The author of this AgreementSummary.
        :type: str
        """
        allowed_values = ["ORACLE", "PARTNER", "PII"]
        if not value_allowed_none_or_none_sentinel(author, allowed_values):
            author = 'UNKNOWN_ENUM_VALUE'
        self._author = author

    @property
    def prompt(self):
        """
        Gets the prompt of this AgreementSummary.
        Textual prompt to read and accept the agreement.


        :return: The prompt of this AgreementSummary.
        :rtype: str
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        """
        Sets the prompt of this AgreementSummary.
        Textual prompt to read and accept the agreement.


        :param prompt: The prompt of this AgreementSummary.
        :type: str
        """
        self._prompt = prompt

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
