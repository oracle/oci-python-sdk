# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TypeSummary(object):
    """
    Summary data catalog type information. All types are statically defined in the system and are immutable.
    It isn't possible to create new types or update existing types via the API.
    """

    #: A constant which can be used with the lifecycle_state property of a TypeSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a TypeSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TypeSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TypeSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a TypeSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a TypeSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TypeSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a TypeSummary.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new TypeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this TypeSummary.
        :type key: str

        :param name:
            The value to assign to the name property of this TypeSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this TypeSummary.
        :type description: str

        :param catalog_id:
            The value to assign to the catalog_id property of this TypeSummary.
        :type catalog_id: str

        :param type_category:
            The value to assign to the type_category property of this TypeSummary.
        :type type_category: str

        :param uri:
            The value to assign to the uri property of this TypeSummary.
        :type uri: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TypeSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'description': 'str',
            'catalog_id': 'str',
            'type_category': 'str',
            'uri': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'description': 'description',
            'catalog_id': 'catalogId',
            'type_category': 'typeCategory',
            'uri': 'uri',
            'lifecycle_state': 'lifecycleState'
        }

        self._key = None
        self._name = None
        self._description = None
        self._catalog_id = None
        self._type_category = None
        self._uri = None
        self._lifecycle_state = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this TypeSummary.
        Unique type key that is immutable.


        :return: The key of this TypeSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TypeSummary.
        Unique type key that is immutable.


        :param key: The key of this TypeSummary.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this TypeSummary.
        The immutable name of the type.


        :return: The name of this TypeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TypeSummary.
        The immutable name of the type.


        :param name: The name of this TypeSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TypeSummary.
        Detailed description of the type.


        :return: The description of this TypeSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TypeSummary.
        Detailed description of the type.


        :param description: The description of this TypeSummary.
        :type: str
        """
        self._description = description

    @property
    def catalog_id(self):
        """
        Gets the catalog_id of this TypeSummary.
        The data catalog's OCID.


        :return: The catalog_id of this TypeSummary.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """
        Sets the catalog_id of this TypeSummary.
        The data catalog's OCID.


        :param catalog_id: The catalog_id of this TypeSummary.
        :type: str
        """
        self._catalog_id = catalog_id

    @property
    def type_category(self):
        """
        Gets the type_category of this TypeSummary.
        Indicates the category this type belongs to. For instance, data assets, connections.


        :return: The type_category of this TypeSummary.
        :rtype: str
        """
        return self._type_category

    @type_category.setter
    def type_category(self, type_category):
        """
        Sets the type_category of this TypeSummary.
        Indicates the category this type belongs to. For instance, data assets, connections.


        :param type_category: The type_category of this TypeSummary.
        :type: str
        """
        self._type_category = type_category

    @property
    def uri(self):
        """
        Gets the uri of this TypeSummary.
        URI to the type instance in the API.


        :return: The uri of this TypeSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this TypeSummary.
        URI to the type instance in the API.


        :param uri: The uri of this TypeSummary.
        :type: str
        """
        self._uri = uri

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TypeSummary.
        State of the folder.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TypeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TypeSummary.
        State of the folder.


        :param lifecycle_state: The lifecycle_state of this TypeSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
