# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchTermSummary(object):
    """
    Summary of a term associated with an object. This is a brief summary returned as part of the search result.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SearchTermSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this SearchTermSummary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this SearchTermSummary.
        :type display_name: str

        :param glossary_key:
            The value to assign to the glossary_key property of this SearchTermSummary.
        :type glossary_key: str

        :param glossary_name:
            The value to assign to the glossary_name property of this SearchTermSummary.
        :type glossary_name: str

        :param parent_term_key:
            The value to assign to the parent_term_key property of this SearchTermSummary.
        :type parent_term_key: str

        :param parent_term_name:
            The value to assign to the parent_term_name property of this SearchTermSummary.
        :type parent_term_name: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'glossary_key': 'str',
            'glossary_name': 'str',
            'parent_term_key': 'str',
            'parent_term_name': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'glossary_key': 'glossaryKey',
            'glossary_name': 'glossaryName',
            'parent_term_key': 'parentTermKey',
            'parent_term_name': 'parentTermName'
        }

        self._key = None
        self._display_name = None
        self._glossary_key = None
        self._glossary_name = None
        self._parent_term_key = None
        self._parent_term_name = None

    @property
    def key(self):
        """
        Gets the key of this SearchTermSummary.
        Unique term key that is immutable.


        :return: The key of this SearchTermSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this SearchTermSummary.
        Unique term key that is immutable.


        :param key: The key of this SearchTermSummary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SearchTermSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this SearchTermSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SearchTermSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this SearchTermSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def glossary_key(self):
        """
        Gets the glossary_key of this SearchTermSummary.
        Unique id of the parent glossary.


        :return: The glossary_key of this SearchTermSummary.
        :rtype: str
        """
        return self._glossary_key

    @glossary_key.setter
    def glossary_key(self, glossary_key):
        """
        Sets the glossary_key of this SearchTermSummary.
        Unique id of the parent glossary.


        :param glossary_key: The glossary_key of this SearchTermSummary.
        :type: str
        """
        self._glossary_key = glossary_key

    @property
    def glossary_name(self):
        """
        Gets the glossary_name of this SearchTermSummary.
        Name of the parent glossary.


        :return: The glossary_name of this SearchTermSummary.
        :rtype: str
        """
        return self._glossary_name

    @glossary_name.setter
    def glossary_name(self, glossary_name):
        """
        Sets the glossary_name of this SearchTermSummary.
        Name of the parent glossary.


        :param glossary_name: The glossary_name of this SearchTermSummary.
        :type: str
        """
        self._glossary_name = glossary_name

    @property
    def parent_term_key(self):
        """
        Gets the parent_term_key of this SearchTermSummary.
        This terms parent term key. Will be null if the term has no parent term.


        :return: The parent_term_key of this SearchTermSummary.
        :rtype: str
        """
        return self._parent_term_key

    @parent_term_key.setter
    def parent_term_key(self, parent_term_key):
        """
        Sets the parent_term_key of this SearchTermSummary.
        This terms parent term key. Will be null if the term has no parent term.


        :param parent_term_key: The parent_term_key of this SearchTermSummary.
        :type: str
        """
        self._parent_term_key = parent_term_key

    @property
    def parent_term_name(self):
        """
        Gets the parent_term_name of this SearchTermSummary.
        Name of the parent term key. Will be null if the term has no parent term.


        :return: The parent_term_name of this SearchTermSummary.
        :rtype: str
        """
        return self._parent_term_name

    @parent_term_name.setter
    def parent_term_name(self, parent_term_name):
        """
        Sets the parent_term_name of this SearchTermSummary.
        Name of the parent term key. Will be null if the term has no parent term.


        :param parent_term_name: The parent_term_name of this SearchTermSummary.
        :type: str
        """
        self._parent_term_name = parent_term_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
