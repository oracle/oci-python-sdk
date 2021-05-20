# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_repository_details import UpdateRepositoryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateGenericRepositoryDetails(UpdateRepositoryDetails):
    """
    Details for updating an artifact repository.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateGenericRepositoryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.artifacts.models.UpdateGenericRepositoryDetails.repository_type` attribute
        of this class is ``GENERIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateGenericRepositoryDetails.
        :type display_name: str

        :param repository_type:
            The value to assign to the repository_type property of this UpdateGenericRepositoryDetails.
        :type repository_type: str

        :param description:
            The value to assign to the description property of this UpdateGenericRepositoryDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateGenericRepositoryDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateGenericRepositoryDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'repository_type': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'repository_type': 'repositoryType',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._repository_type = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._repository_type = 'GENERIC'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
