# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RegistryMetadata(object):
    """
    Information about the object and its parent.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RegistryMetadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param aggregator_key:
            The value to assign to the aggregator_key property of this RegistryMetadata.
        :type aggregator_key: str

        :param labels:
            The value to assign to the labels property of this RegistryMetadata.
        :type labels: list[str]

        :param registry_version:
            The value to assign to the registry_version property of this RegistryMetadata.
        :type registry_version: int

        :param key:
            The value to assign to the key property of this RegistryMetadata.
        :type key: str

        :param is_favorite:
            The value to assign to the is_favorite property of this RegistryMetadata.
        :type is_favorite: bool

        :param created_by_user_id:
            The value to assign to the created_by_user_id property of this RegistryMetadata.
        :type created_by_user_id: str

        :param created_by_user_name:
            The value to assign to the created_by_user_name property of this RegistryMetadata.
        :type created_by_user_name: str

        :param updated_by_user_id:
            The value to assign to the updated_by_user_id property of this RegistryMetadata.
        :type updated_by_user_id: str

        :param updated_by_user_name:
            The value to assign to the updated_by_user_name property of this RegistryMetadata.
        :type updated_by_user_name: str

        :param time_created:
            The value to assign to the time_created property of this RegistryMetadata.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RegistryMetadata.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'aggregator_key': 'str',
            'labels': 'list[str]',
            'registry_version': 'int',
            'key': 'str',
            'is_favorite': 'bool',
            'created_by_user_id': 'str',
            'created_by_user_name': 'str',
            'updated_by_user_id': 'str',
            'updated_by_user_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'aggregator_key': 'aggregatorKey',
            'labels': 'labels',
            'registry_version': 'registryVersion',
            'key': 'key',
            'is_favorite': 'isFavorite',
            'created_by_user_id': 'createdByUserId',
            'created_by_user_name': 'createdByUserName',
            'updated_by_user_id': 'updatedByUserId',
            'updated_by_user_name': 'updatedByUserName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._aggregator_key = None
        self._labels = None
        self._registry_version = None
        self._key = None
        self._is_favorite = None
        self._created_by_user_id = None
        self._created_by_user_name = None
        self._updated_by_user_id = None
        self._updated_by_user_name = None
        self._time_created = None
        self._time_updated = None

    @property
    def aggregator_key(self):
        """
        Gets the aggregator_key of this RegistryMetadata.
        The owning object's key for this object.


        :return: The aggregator_key of this RegistryMetadata.
        :rtype: str
        """
        return self._aggregator_key

    @aggregator_key.setter
    def aggregator_key(self, aggregator_key):
        """
        Sets the aggregator_key of this RegistryMetadata.
        The owning object's key for this object.


        :param aggregator_key: The aggregator_key of this RegistryMetadata.
        :type: str
        """
        self._aggregator_key = aggregator_key

    @property
    def labels(self):
        """
        Gets the labels of this RegistryMetadata.
        Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and use them to categorize content.


        :return: The labels of this RegistryMetadata.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this RegistryMetadata.
        Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and use them to categorize content.


        :param labels: The labels of this RegistryMetadata.
        :type: list[str]
        """
        self._labels = labels

    @property
    def registry_version(self):
        """
        Gets the registry_version of this RegistryMetadata.
        The registry version.


        :return: The registry_version of this RegistryMetadata.
        :rtype: int
        """
        return self._registry_version

    @registry_version.setter
    def registry_version(self, registry_version):
        """
        Sets the registry_version of this RegistryMetadata.
        The registry version.


        :param registry_version: The registry_version of this RegistryMetadata.
        :type: int
        """
        self._registry_version = registry_version

    @property
    def key(self):
        """
        Gets the key of this RegistryMetadata.
        The identifying key for the object.


        :return: The key of this RegistryMetadata.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this RegistryMetadata.
        The identifying key for the object.


        :param key: The key of this RegistryMetadata.
        :type: str
        """
        self._key = key

    @property
    def is_favorite(self):
        """
        Gets the is_favorite of this RegistryMetadata.
        Specifies whether this object is a favorite or not.


        :return: The is_favorite of this RegistryMetadata.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """
        Sets the is_favorite of this RegistryMetadata.
        Specifies whether this object is a favorite or not.


        :param is_favorite: The is_favorite of this RegistryMetadata.
        :type: bool
        """
        self._is_favorite = is_favorite

    @property
    def created_by_user_id(self):
        """
        Gets the created_by_user_id of this RegistryMetadata.
        The id of the user who created the object.


        :return: The created_by_user_id of this RegistryMetadata.
        :rtype: str
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """
        Sets the created_by_user_id of this RegistryMetadata.
        The id of the user who created the object.


        :param created_by_user_id: The created_by_user_id of this RegistryMetadata.
        :type: str
        """
        self._created_by_user_id = created_by_user_id

    @property
    def created_by_user_name(self):
        """
        Gets the created_by_user_name of this RegistryMetadata.
        The name of the user who created the object.


        :return: The created_by_user_name of this RegistryMetadata.
        :rtype: str
        """
        return self._created_by_user_name

    @created_by_user_name.setter
    def created_by_user_name(self, created_by_user_name):
        """
        Sets the created_by_user_name of this RegistryMetadata.
        The name of the user who created the object.


        :param created_by_user_name: The created_by_user_name of this RegistryMetadata.
        :type: str
        """
        self._created_by_user_name = created_by_user_name

    @property
    def updated_by_user_id(self):
        """
        Gets the updated_by_user_id of this RegistryMetadata.
        The id of the user who updated the object.


        :return: The updated_by_user_id of this RegistryMetadata.
        :rtype: str
        """
        return self._updated_by_user_id

    @updated_by_user_id.setter
    def updated_by_user_id(self, updated_by_user_id):
        """
        Sets the updated_by_user_id of this RegistryMetadata.
        The id of the user who updated the object.


        :param updated_by_user_id: The updated_by_user_id of this RegistryMetadata.
        :type: str
        """
        self._updated_by_user_id = updated_by_user_id

    @property
    def updated_by_user_name(self):
        """
        Gets the updated_by_user_name of this RegistryMetadata.
        The name of the user who updated the object.


        :return: The updated_by_user_name of this RegistryMetadata.
        :rtype: str
        """
        return self._updated_by_user_name

    @updated_by_user_name.setter
    def updated_by_user_name(self, updated_by_user_name):
        """
        Sets the updated_by_user_name of this RegistryMetadata.
        The name of the user who updated the object.


        :param updated_by_user_name: The updated_by_user_name of this RegistryMetadata.
        :type: str
        """
        self._updated_by_user_name = updated_by_user_name

    @property
    def time_created(self):
        """
        Gets the time_created of this RegistryMetadata.
        The date and time that the object was created.


        :return: The time_created of this RegistryMetadata.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RegistryMetadata.
        The date and time that the object was created.


        :param time_created: The time_created of this RegistryMetadata.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this RegistryMetadata.
        The date and time that the object was updated.


        :return: The time_updated of this RegistryMetadata.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RegistryMetadata.
        The date and time that the object was updated.


        :param time_updated: The time_updated of this RegistryMetadata.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
