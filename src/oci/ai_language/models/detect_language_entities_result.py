# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetectLanguageEntitiesResult(object):
    """
    Result of entities detect call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetectLanguageEntitiesResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entities:
            The value to assign to the entities property of this DetectLanguageEntitiesResult.
        :type entities: list[oci.ai_language.models.Entity]

        """
        self.swagger_types = {
            'entities': 'list[Entity]'
        }

        self.attribute_map = {
            'entities': 'entities'
        }

        self._entities = None

    @property
    def entities(self):
        """
        **[Required]** Gets the entities of this DetectLanguageEntitiesResult.
        List of detected entities.


        :return: The entities of this DetectLanguageEntitiesResult.
        :rtype: list[oci.ai_language.models.Entity]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """
        Sets the entities of this DetectLanguageEntitiesResult.
        List of detected entities.


        :param entities: The entities of this DetectLanguageEntitiesResult.
        :type: list[oci.ai_language.models.Entity]
        """
        self._entities = entities

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
