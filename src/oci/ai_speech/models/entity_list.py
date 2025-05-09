# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntityList(object):
    """
    List of entities of a given type, to be used to train a customization.
    Note: If multiple EntityLists are provided, a separate Customization resource will be created for each EntityList.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EntityList object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param alias:
            The value to assign to the alias property of this EntityList.
        :type alias: str

        :param id:
            The value to assign to the id property of this EntityList.
        :type id: str

        :param entity_type:
            The value to assign to the entity_type property of this EntityList.
        :type entity_type: str

        :param entities:
            The value to assign to the entities property of this EntityList.
        :type entities: list[oci.ai_speech.models.Entity]

        """
        self.swagger_types = {
            'alias': 'str',
            'id': 'str',
            'entity_type': 'str',
            'entities': 'list[Entity]'
        }
        self.attribute_map = {
            'alias': 'alias',
            'id': 'id',
            'entity_type': 'entityType',
            'entities': 'entities'
        }
        self._alias = None
        self._id = None
        self._entity_type = None
        self._entities = None

    @property
    def alias(self):
        """
        Gets the alias of this EntityList.
        Alias of existing customization or to associate with new customization created from entityList.


        :return: The alias of this EntityList.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this EntityList.
        Alias of existing customization or to associate with new customization created from entityList.


        :param alias: The alias of this EntityList.
        :type: str
        """
        self._alias = alias

    @property
    def id(self):
        """
        Gets the id of this EntityList.
        Entity type OCID


        :return: The id of this EntityList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EntityList.
        Entity type OCID


        :param id: The id of this EntityList.
        :type: str
        """
        self._id = id

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this EntityList.
        Entity Type


        :return: The entity_type of this EntityList.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this EntityList.
        Entity Type


        :param entity_type: The entity_type of this EntityList.
        :type: str
        """
        self._entity_type = entity_type

    @property
    def entities(self):
        """
        Gets the entities of this EntityList.
        List of entities such as names, words or phrases matching the given entityType to add recognition support for


        :return: The entities of this EntityList.
        :rtype: list[oci.ai_speech.models.Entity]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """
        Sets the entities of this EntityList.
        List of entities such as names, words or phrases matching the given entityType to add recognition support for


        :param entities: The entities of this EntityList.
        :type: list[oci.ai_speech.models.Entity]
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
