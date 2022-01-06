# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectRelationship(object):
    """
    Details regarding a specific object and its relationship to the referencing object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectRelationship object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param relationship_type:
            The value to assign to the relationship_type property of this ObjectRelationship.
        :type relationship_type: str

        :param key:
            The value to assign to the key property of this ObjectRelationship.
        :type key: str

        :param name:
            The value to assign to the name property of this ObjectRelationship.
        :type name: str

        :param type_name:
            The value to assign to the type_name property of this ObjectRelationship.
        :type type_name: str

        :param type_key:
            The value to assign to the type_key property of this ObjectRelationship.
        :type type_key: str

        :param time_created:
            The value to assign to the time_created property of this ObjectRelationship.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ObjectRelationship.
        :type time_updated: datetime

        :param path:
            The value to assign to the path property of this ObjectRelationship.
        :type path: str

        :param parent_key:
            The value to assign to the parent_key property of this ObjectRelationship.
        :type parent_key: str

        :param parent_path:
            The value to assign to the parent_path property of this ObjectRelationship.
        :type parent_path: str

        """
        self.swagger_types = {
            'relationship_type': 'str',
            'key': 'str',
            'name': 'str',
            'type_name': 'str',
            'type_key': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'path': 'str',
            'parent_key': 'str',
            'parent_path': 'str'
        }

        self.attribute_map = {
            'relationship_type': 'relationshipType',
            'key': 'key',
            'name': 'name',
            'type_name': 'typeName',
            'type_key': 'typeKey',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'path': 'path',
            'parent_key': 'parentKey',
            'parent_path': 'parentPath'
        }

        self._relationship_type = None
        self._key = None
        self._name = None
        self._type_name = None
        self._type_key = None
        self._time_created = None
        self._time_updated = None
        self._path = None
        self._parent_key = None
        self._parent_path = None

    @property
    def relationship_type(self):
        """
        Gets the relationship_type of this ObjectRelationship.
        Type of relationship with the referencing object.


        :return: The relationship_type of this ObjectRelationship.
        :rtype: str
        """
        return self._relationship_type

    @relationship_type.setter
    def relationship_type(self, relationship_type):
        """
        Sets the relationship_type of this ObjectRelationship.
        Type of relationship with the referencing object.


        :param relationship_type: The relationship_type of this ObjectRelationship.
        :type: str
        """
        self._relationship_type = relationship_type

    @property
    def key(self):
        """
        Gets the key of this ObjectRelationship.
        Unique id of the object.


        :return: The key of this ObjectRelationship.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ObjectRelationship.
        Unique id of the object.


        :param key: The key of this ObjectRelationship.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this ObjectRelationship.
        Name of the object.


        :return: The name of this ObjectRelationship.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ObjectRelationship.
        Name of the object.


        :param name: The name of this ObjectRelationship.
        :type: str
        """
        self._name = name

    @property
    def type_name(self):
        """
        Gets the type_name of this ObjectRelationship.
        Type name of the object. Type names can be found via the '/types' endpoint.


        :return: The type_name of this ObjectRelationship.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """
        Sets the type_name of this ObjectRelationship.
        Type name of the object. Type names can be found via the '/types' endpoint.


        :param type_name: The type_name of this ObjectRelationship.
        :type: str
        """
        self._type_name = type_name

    @property
    def type_key(self):
        """
        Gets the type_key of this ObjectRelationship.
        Type key of the object. Type keys can be found via the '/types' endpoint.


        :return: The type_key of this ObjectRelationship.
        :rtype: str
        """
        return self._type_key

    @type_key.setter
    def type_key(self, type_key):
        """
        Sets the type_key of this ObjectRelationship.
        Type key of the object. Type keys can be found via the '/types' endpoint.


        :param type_key: The type_key of this ObjectRelationship.
        :type: str
        """
        self._type_key = type_key

    @property
    def time_created(self):
        """
        Gets the time_created of this ObjectRelationship.
        The date and time the relationship was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ObjectRelationship.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ObjectRelationship.
        The date and time the relationship was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ObjectRelationship.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ObjectRelationship.
        The last time a change was made to this reference. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ObjectRelationship.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ObjectRelationship.
        The last time a change was made to this reference. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ObjectRelationship.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def path(self):
        """
        Gets the path of this ObjectRelationship.
        Full path of the object.


        :return: The path of this ObjectRelationship.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ObjectRelationship.
        Full path of the object.


        :param path: The path of this ObjectRelationship.
        :type: str
        """
        self._path = path

    @property
    def parent_key(self):
        """
        Gets the parent_key of this ObjectRelationship.
        Key of the parent object for the resource.


        :return: The parent_key of this ObjectRelationship.
        :rtype: str
        """
        return self._parent_key

    @parent_key.setter
    def parent_key(self, parent_key):
        """
        Sets the parent_key of this ObjectRelationship.
        Key of the parent object for the resource.


        :param parent_key: The parent_key of this ObjectRelationship.
        :type: str
        """
        self._parent_key = parent_key

    @property
    def parent_path(self):
        """
        Gets the parent_path of this ObjectRelationship.
        Full path of the parent object.


        :return: The parent_path of this ObjectRelationship.
        :rtype: str
        """
        return self._parent_path

    @parent_path.setter
    def parent_path(self, parent_path):
        """
        Sets the parent_path of this ObjectRelationship.
        Full path of the parent object.


        :param parent_path: The parent_path of this ObjectRelationship.
        :type: str
        """
        self._parent_path = parent_path

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
