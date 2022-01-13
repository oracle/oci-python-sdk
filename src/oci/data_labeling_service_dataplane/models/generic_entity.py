# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .entity import Entity
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenericEntity(Entity):
    """
    This is an extensible entity type for users, and the base entity type for some annotation formats.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenericEntity object with values from keyword arguments. The default value of the :py:attr:`~oci.data_labeling_service_dataplane.models.GenericEntity.entity_type` attribute
        of this class is ``GENERIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_type:
            The value to assign to the entity_type property of this GenericEntity.
            Allowed values for this property are: "GENERIC", "IMAGEOBJECTSELECTION", "TEXTSELECTION"
        :type entity_type: str

        :param labels:
            The value to assign to the labels property of this GenericEntity.
        :type labels: list[oci.data_labeling_service_dataplane.models.Label]

        :param extended_metadata:
            The value to assign to the extended_metadata property of this GenericEntity.
        :type extended_metadata: dict(str, str)

        """
        self.swagger_types = {
            'entity_type': 'str',
            'labels': 'list[Label]',
            'extended_metadata': 'dict(str, str)'
        }

        self.attribute_map = {
            'entity_type': 'entityType',
            'labels': 'labels',
            'extended_metadata': 'extendedMetadata'
        }

        self._entity_type = None
        self._labels = None
        self._extended_metadata = None
        self._entity_type = 'GENERIC'

    @property
    def labels(self):
        """
        **[Required]** Gets the labels of this GenericEntity.
        A collection of label entities.


        :return: The labels of this GenericEntity.
        :rtype: list[oci.data_labeling_service_dataplane.models.Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this GenericEntity.
        A collection of label entities.


        :param labels: The labels of this GenericEntity.
        :type: list[oci.data_labeling_service_dataplane.models.Label]
        """
        self._labels = labels

    @property
    def extended_metadata(self):
        """
        Gets the extended_metadata of this GenericEntity.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :return: The extended_metadata of this GenericEntity.
        :rtype: dict(str, str)
        """
        return self._extended_metadata

    @extended_metadata.setter
    def extended_metadata(self, extended_metadata):
        """
        Sets the extended_metadata of this GenericEntity.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :param extended_metadata: The extended_metadata of this GenericEntity.
        :type: dict(str, str)
        """
        self._extended_metadata = extended_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
