# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntityDocumentResult(object):
    """
    The document response for entities detect call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EntityDocumentResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this EntityDocumentResult.
        :type key: str

        :param entities:
            The value to assign to the entities property of this EntityDocumentResult.
        :type entities: list[oci.ai_language.models.HierarchicalEntity]

        :param language_code:
            The value to assign to the language_code property of this EntityDocumentResult.
        :type language_code: str

        """
        self.swagger_types = {
            'key': 'str',
            'entities': 'list[HierarchicalEntity]',
            'language_code': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'entities': 'entities',
            'language_code': 'languageCode'
        }

        self._key = None
        self._entities = None
        self._language_code = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this EntityDocumentResult.
        Document unique identifier defined by the user.


        :return: The key of this EntityDocumentResult.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this EntityDocumentResult.
        Document unique identifier defined by the user.


        :param key: The key of this EntityDocumentResult.
        :type: str
        """
        self._key = key

    @property
    def entities(self):
        """
        **[Required]** Gets the entities of this EntityDocumentResult.
        List of detected entities.


        :return: The entities of this EntityDocumentResult.
        :rtype: list[oci.ai_language.models.HierarchicalEntity]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """
        Sets the entities of this EntityDocumentResult.
        List of detected entities.


        :param entities: The entities of this EntityDocumentResult.
        :type: list[oci.ai_language.models.HierarchicalEntity]
        """
        self._entities = entities

    @property
    def language_code(self):
        """
        **[Required]** Gets the language_code of this EntityDocumentResult.
        Language code as per `ISO 639-1`__ standard.

        __ https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


        :return: The language_code of this EntityDocumentResult.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this EntityDocumentResult.
        Language code as per `ISO 639-1`__ standard.

        __ https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


        :param language_code: The language_code of this EntityDocumentResult.
        :type: str
        """
        self._language_code = language_code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
