# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .repository import Repository
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenericRepository(Repository):
    """
    The metadata for the artifact repository.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenericRepository object with values from keyword arguments. The default value of the :py:attr:`~oci.artifacts.models.GenericRepository.repository_type` attribute
        of this class is ``GENERIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this GenericRepository.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this GenericRepository.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this GenericRepository.
        :type compartment_id: str

        :param repository_type:
            The value to assign to the repository_type property of this GenericRepository.
            Allowed values for this property are: "GENERIC"
        :type repository_type: str

        :param description:
            The value to assign to the description property of this GenericRepository.
        :type description: str

        :param is_immutable:
            The value to assign to the is_immutable property of this GenericRepository.
        :type is_immutable: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this GenericRepository.
            Allowed values for this property are: "AVAILABLE", "DELETING", "DELETED"
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this GenericRepository.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this GenericRepository.
        :type defined_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this GenericRepository.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'repository_type': 'str',
            'description': 'str',
            'is_immutable': 'bool',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'repository_type': 'repositoryType',
            'description': 'description',
            'is_immutable': 'isImmutable',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._repository_type = None
        self._description = None
        self._is_immutable = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._time_created = None
        self._repository_type = 'GENERIC'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
