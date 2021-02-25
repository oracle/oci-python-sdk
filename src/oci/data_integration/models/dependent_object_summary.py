# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DependentObjectSummary(object):
    """
    Details of the dependent object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DependentObjectSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param created_by:
            The value to assign to the created_by property of this DependentObjectSummary.
        :type created_by: str

        :param created_by_name:
            The value to assign to the created_by_name property of this DependentObjectSummary.
        :type created_by_name: str

        :param updated_by:
            The value to assign to the updated_by property of this DependentObjectSummary.
        :type updated_by: str

        :param updated_by_name:
            The value to assign to the updated_by_name property of this DependentObjectSummary.
        :type updated_by_name: str

        :param time_created:
            The value to assign to the time_created property of this DependentObjectSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DependentObjectSummary.
        :type time_updated: datetime

        :param aggregator_key:
            The value to assign to the aggregator_key property of this DependentObjectSummary.
        :type aggregator_key: str

        :param aggregator:
            The value to assign to the aggregator property of this DependentObjectSummary.
        :type aggregator: oci.data_integration.models.AggregatorSummary

        :param identifier_path:
            The value to assign to the identifier_path property of this DependentObjectSummary.
        :type identifier_path: str

        :param info_fields:
            The value to assign to the info_fields property of this DependentObjectSummary.
        :type info_fields: dict(str, str)

        :param registry_version:
            The value to assign to the registry_version property of this DependentObjectSummary.
        :type registry_version: int

        :param labels:
            The value to assign to the labels property of this DependentObjectSummary.
        :type labels: list[str]

        :param is_favorite:
            The value to assign to the is_favorite property of this DependentObjectSummary.
        :type is_favorite: bool

        """
        self.swagger_types = {
            'created_by': 'str',
            'created_by_name': 'str',
            'updated_by': 'str',
            'updated_by_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'aggregator_key': 'str',
            'aggregator': 'AggregatorSummary',
            'identifier_path': 'str',
            'info_fields': 'dict(str, str)',
            'registry_version': 'int',
            'labels': 'list[str]',
            'is_favorite': 'bool'
        }

        self.attribute_map = {
            'created_by': 'createdBy',
            'created_by_name': 'createdByName',
            'updated_by': 'updatedBy',
            'updated_by_name': 'updatedByName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'aggregator_key': 'aggregatorKey',
            'aggregator': 'aggregator',
            'identifier_path': 'identifierPath',
            'info_fields': 'infoFields',
            'registry_version': 'registryVersion',
            'labels': 'labels',
            'is_favorite': 'isFavorite'
        }

        self._created_by = None
        self._created_by_name = None
        self._updated_by = None
        self._updated_by_name = None
        self._time_created = None
        self._time_updated = None
        self._aggregator_key = None
        self._aggregator = None
        self._identifier_path = None
        self._info_fields = None
        self._registry_version = None
        self._labels = None
        self._is_favorite = None

    @property
    def created_by(self):
        """
        Gets the created_by of this DependentObjectSummary.
        The user that created the object.


        :return: The created_by of this DependentObjectSummary.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this DependentObjectSummary.
        The user that created the object.


        :param created_by: The created_by of this DependentObjectSummary.
        :type: str
        """
        self._created_by = created_by

    @property
    def created_by_name(self):
        """
        Gets the created_by_name of this DependentObjectSummary.
        The user that created the object.


        :return: The created_by_name of this DependentObjectSummary.
        :rtype: str
        """
        return self._created_by_name

    @created_by_name.setter
    def created_by_name(self, created_by_name):
        """
        Sets the created_by_name of this DependentObjectSummary.
        The user that created the object.


        :param created_by_name: The created_by_name of this DependentObjectSummary.
        :type: str
        """
        self._created_by_name = created_by_name

    @property
    def updated_by(self):
        """
        Gets the updated_by of this DependentObjectSummary.
        The user that updated the object.


        :return: The updated_by of this DependentObjectSummary.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """
        Sets the updated_by of this DependentObjectSummary.
        The user that updated the object.


        :param updated_by: The updated_by of this DependentObjectSummary.
        :type: str
        """
        self._updated_by = updated_by

    @property
    def updated_by_name(self):
        """
        Gets the updated_by_name of this DependentObjectSummary.
        The user that updated the object.


        :return: The updated_by_name of this DependentObjectSummary.
        :rtype: str
        """
        return self._updated_by_name

    @updated_by_name.setter
    def updated_by_name(self, updated_by_name):
        """
        Sets the updated_by_name of this DependentObjectSummary.
        The user that updated the object.


        :param updated_by_name: The updated_by_name of this DependentObjectSummary.
        :type: str
        """
        self._updated_by_name = updated_by_name

    @property
    def time_created(self):
        """
        Gets the time_created of this DependentObjectSummary.
        The date and time that the object was created.


        :return: The time_created of this DependentObjectSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DependentObjectSummary.
        The date and time that the object was created.


        :param time_created: The time_created of this DependentObjectSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DependentObjectSummary.
        The date and time that the object was updated.


        :return: The time_updated of this DependentObjectSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DependentObjectSummary.
        The date and time that the object was updated.


        :param time_updated: The time_updated of this DependentObjectSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def aggregator_key(self):
        """
        Gets the aggregator_key of this DependentObjectSummary.
        The owning object key for this object.


        :return: The aggregator_key of this DependentObjectSummary.
        :rtype: str
        """
        return self._aggregator_key

    @aggregator_key.setter
    def aggregator_key(self, aggregator_key):
        """
        Sets the aggregator_key of this DependentObjectSummary.
        The owning object key for this object.


        :param aggregator_key: The aggregator_key of this DependentObjectSummary.
        :type: str
        """
        self._aggregator_key = aggregator_key

    @property
    def aggregator(self):
        """
        Gets the aggregator of this DependentObjectSummary.

        :return: The aggregator of this DependentObjectSummary.
        :rtype: oci.data_integration.models.AggregatorSummary
        """
        return self._aggregator

    @aggregator.setter
    def aggregator(self, aggregator):
        """
        Sets the aggregator of this DependentObjectSummary.

        :param aggregator: The aggregator of this DependentObjectSummary.
        :type: oci.data_integration.models.AggregatorSummary
        """
        self._aggregator = aggregator

    @property
    def identifier_path(self):
        """
        Gets the identifier_path of this DependentObjectSummary.
        The full path to identify this object.


        :return: The identifier_path of this DependentObjectSummary.
        :rtype: str
        """
        return self._identifier_path

    @identifier_path.setter
    def identifier_path(self, identifier_path):
        """
        Sets the identifier_path of this DependentObjectSummary.
        The full path to identify this object.


        :param identifier_path: The identifier_path of this DependentObjectSummary.
        :type: str
        """
        self._identifier_path = identifier_path

    @property
    def info_fields(self):
        """
        Gets the info_fields of this DependentObjectSummary.
        Information property fields.


        :return: The info_fields of this DependentObjectSummary.
        :rtype: dict(str, str)
        """
        return self._info_fields

    @info_fields.setter
    def info_fields(self, info_fields):
        """
        Sets the info_fields of this DependentObjectSummary.
        Information property fields.


        :param info_fields: The info_fields of this DependentObjectSummary.
        :type: dict(str, str)
        """
        self._info_fields = info_fields

    @property
    def registry_version(self):
        """
        Gets the registry_version of this DependentObjectSummary.
        The registry version of the object.


        :return: The registry_version of this DependentObjectSummary.
        :rtype: int
        """
        return self._registry_version

    @registry_version.setter
    def registry_version(self, registry_version):
        """
        Sets the registry_version of this DependentObjectSummary.
        The registry version of the object.


        :param registry_version: The registry_version of this DependentObjectSummary.
        :type: int
        """
        self._registry_version = registry_version

    @property
    def labels(self):
        """
        Gets the labels of this DependentObjectSummary.
        Labels are keywords or tags that you can add to data assets, dataflows and so on. You can define your own labels and use them to categorize content.


        :return: The labels of this DependentObjectSummary.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this DependentObjectSummary.
        Labels are keywords or tags that you can add to data assets, dataflows and so on. You can define your own labels and use them to categorize content.


        :param labels: The labels of this DependentObjectSummary.
        :type: list[str]
        """
        self._labels = labels

    @property
    def is_favorite(self):
        """
        Gets the is_favorite of this DependentObjectSummary.
        Specifies whether this object is a favorite or not.


        :return: The is_favorite of this DependentObjectSummary.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """
        Sets the is_favorite of this DependentObjectSummary.
        Specifies whether this object is a favorite or not.


        :param is_favorite: The is_favorite of this DependentObjectSummary.
        :type: bool
        """
        self._is_favorite = is_favorite

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
