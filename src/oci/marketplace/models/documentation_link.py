# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DocumentationLink(object):
    """
    A link to a documentation resource on the internet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DocumentationLink object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DocumentationLink.
        :type name: str

        :param url:
            The value to assign to the url property of this DocumentationLink.
        :type url: str

        :param document_category:
            The value to assign to the document_category property of this DocumentationLink.
        :type document_category: str

        """
        self.swagger_types = {
            'name': 'str',
            'url': 'str',
            'document_category': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'url': 'url',
            'document_category': 'documentCategory'
        }

        self._name = None
        self._url = None
        self._document_category = None

    @property
    def name(self):
        """
        Gets the name of this DocumentationLink.
        Text that describes the resource.


        :return: The name of this DocumentationLink.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DocumentationLink.
        Text that describes the resource.


        :param name: The name of this DocumentationLink.
        :type: str
        """
        self._name = name

    @property
    def url(self):
        """
        Gets the url of this DocumentationLink.
        The URL of the resource.


        :return: The url of this DocumentationLink.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this DocumentationLink.
        The URL of the resource.


        :param url: The url of this DocumentationLink.
        :type: str
        """
        self._url = url

    @property
    def document_category(self):
        """
        Gets the document_category of this DocumentationLink.
        The category that the document belongs to.


        :return: The document_category of this DocumentationLink.
        :rtype: str
        """
        return self._document_category

    @document_category.setter
    def document_category(self, document_category):
        """
        Sets the document_category of this DocumentationLink.
        The category that the document belongs to.


        :param document_category: The document_category of this DocumentationLink.
        :type: str
        """
        self._document_category = document_category

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
