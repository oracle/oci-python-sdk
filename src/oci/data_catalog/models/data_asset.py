# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAsset(object):
    """
    Data asset representation. A physical store, or stream, of data known to the data catalog and containing
    one or many data entities, possibly in an organized structure of folders. A data asset is often synonymous
    with a 'System', such as a database, or may be a file container or a message stream.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataAsset object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this DataAsset.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this DataAsset.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DataAsset.
        :type description: str

        :param catalog_id:
            The value to assign to the catalog_id property of this DataAsset.
        :type catalog_id: str

        :param external_key:
            The value to assign to the external_key property of this DataAsset.
        :type external_key: str

        :param type_key:
            The value to assign to the type_key property of this DataAsset.
        :type type_key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DataAsset.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this DataAsset.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DataAsset.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this DataAsset.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this DataAsset.
        :type updated_by_id: str

        :param uri:
            The value to assign to the uri property of this DataAsset.
        :type uri: str

        :param properties:
            The value to assign to the properties property of this DataAsset.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'catalog_id': 'str',
            'external_key': 'str',
            'type_key': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str',
            'uri': 'str',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'catalog_id': 'catalogId',
            'external_key': 'externalKey',
            'type_key': 'typeKey',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById',
            'uri': 'uri',
            'properties': 'properties'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._catalog_id = None
        self._external_key = None
        self._type_key = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None
        self._uri = None
        self._properties = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this DataAsset.
        Unique data asset key that is immutable.


        :return: The key of this DataAsset.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DataAsset.
        Unique data asset key that is immutable.


        :param key: The key of this DataAsset.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this DataAsset.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this DataAsset.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DataAsset.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this DataAsset.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DataAsset.
        Detailed description of the data asset.


        :return: The description of this DataAsset.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataAsset.
        Detailed description of the data asset.


        :param description: The description of this DataAsset.
        :type: str
        """
        self._description = description

    @property
    def catalog_id(self):
        """
        Gets the catalog_id of this DataAsset.
        The data catalog's OCID.


        :return: The catalog_id of this DataAsset.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """
        Sets the catalog_id of this DataAsset.
        The data catalog's OCID.


        :param catalog_id: The catalog_id of this DataAsset.
        :type: str
        """
        self._catalog_id = catalog_id

    @property
    def external_key(self):
        """
        Gets the external_key of this DataAsset.
        External URI that can be used to reference the object. Format will differ based on the type of object.


        :return: The external_key of this DataAsset.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this DataAsset.
        External URI that can be used to reference the object. Format will differ based on the type of object.


        :param external_key: The external_key of this DataAsset.
        :type: str
        """
        self._external_key = external_key

    @property
    def type_key(self):
        """
        Gets the type_key of this DataAsset.
        The key of the object type. Type key's can be found via the '/types' endpoint.


        :return: The type_key of this DataAsset.
        :rtype: str
        """
        return self._type_key

    @type_key.setter
    def type_key(self, type_key):
        """
        Sets the type_key of this DataAsset.
        The key of the object type. Type key's can be found via the '/types' endpoint.


        :param type_key: The type_key of this DataAsset.
        :type: str
        """
        self._type_key = type_key

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DataAsset.
        The current state of the data asset.


        :return: The lifecycle_state of this DataAsset.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DataAsset.
        The current state of the data asset.


        :param lifecycle_state: The lifecycle_state of this DataAsset.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this DataAsset.
        The date and time the data asset was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DataAsset.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DataAsset.
        The date and time the data asset was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DataAsset.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DataAsset.
        The last time that any change was made to the data asset. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this DataAsset.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DataAsset.
        The last time that any change was made to the data asset. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this DataAsset.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this DataAsset.
        OCID of the user who created the data asset.


        :return: The created_by_id of this DataAsset.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this DataAsset.
        OCID of the user who created the data asset.


        :param created_by_id: The created_by_id of this DataAsset.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this DataAsset.
        OCID of the user who last modified the data asset.


        :return: The updated_by_id of this DataAsset.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this DataAsset.
        OCID of the user who last modified the data asset.


        :param updated_by_id: The updated_by_id of this DataAsset.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def uri(self):
        """
        Gets the uri of this DataAsset.
        URI to the data asset instance in the API.


        :return: The uri of this DataAsset.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this DataAsset.
        URI to the data asset instance in the API.


        :param uri: The uri of this DataAsset.
        :type: str
        """
        self._uri = uri

    @property
    def properties(self):
        """
        Gets the properties of this DataAsset.
        A map of maps that contains the properties which are specific to the asset type. Each data asset type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        data assets have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :return: The properties of this DataAsset.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this DataAsset.
        A map of maps that contains the properties which are specific to the asset type. Each data asset type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        data assets have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :param properties: The properties of this DataAsset.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
