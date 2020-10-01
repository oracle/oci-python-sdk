# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnrichedEntity(object):
    """
    This is used to specify runtime parameters for data entities such as files that need both the data entity and the format.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnrichedEntity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity:
            The value to assign to the entity property of this EnrichedEntity.
        :type entity: DataEntity

        :param data_format:
            The value to assign to the data_format property of this EnrichedEntity.
        :type data_format: DataFormat

        """
        self.swagger_types = {
            'entity': 'DataEntity',
            'data_format': 'DataFormat'
        }

        self.attribute_map = {
            'entity': 'entity',
            'data_format': 'dataFormat'
        }

        self._entity = None
        self._data_format = None

    @property
    def entity(self):
        """
        Gets the entity of this EnrichedEntity.

        :return: The entity of this EnrichedEntity.
        :rtype: DataEntity
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this EnrichedEntity.

        :param entity: The entity of this EnrichedEntity.
        :type: DataEntity
        """
        self._entity = entity

    @property
    def data_format(self):
        """
        Gets the data_format of this EnrichedEntity.

        :return: The data_format of this EnrichedEntity.
        :rtype: DataFormat
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """
        Sets the data_format of this EnrichedEntity.

        :param data_format: The data_format of this EnrichedEntity.
        :type: DataFormat
        """
        self._data_format = data_format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
