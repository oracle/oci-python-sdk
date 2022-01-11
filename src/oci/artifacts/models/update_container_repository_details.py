# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateContainerRepositoryDetails(object):
    """
    Update container repository request details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateContainerRepositoryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_immutable:
            The value to assign to the is_immutable property of this UpdateContainerRepositoryDetails.
        :type is_immutable: bool

        :param is_public:
            The value to assign to the is_public property of this UpdateContainerRepositoryDetails.
        :type is_public: bool

        :param readme:
            The value to assign to the readme property of this UpdateContainerRepositoryDetails.
        :type readme: oci.artifacts.models.ContainerRepositoryReadme

        """
        self.swagger_types = {
            'is_immutable': 'bool',
            'is_public': 'bool',
            'readme': 'ContainerRepositoryReadme'
        }

        self.attribute_map = {
            'is_immutable': 'isImmutable',
            'is_public': 'isPublic',
            'readme': 'readme'
        }

        self._is_immutable = None
        self._is_public = None
        self._readme = None

    @property
    def is_immutable(self):
        """
        Gets the is_immutable of this UpdateContainerRepositoryDetails.
        Whether the repository is immutable. Images cannot be overwritten in an immutable repository.


        :return: The is_immutable of this UpdateContainerRepositoryDetails.
        :rtype: bool
        """
        return self._is_immutable

    @is_immutable.setter
    def is_immutable(self, is_immutable):
        """
        Sets the is_immutable of this UpdateContainerRepositoryDetails.
        Whether the repository is immutable. Images cannot be overwritten in an immutable repository.


        :param is_immutable: The is_immutable of this UpdateContainerRepositoryDetails.
        :type: bool
        """
        self._is_immutable = is_immutable

    @property
    def is_public(self):
        """
        Gets the is_public of this UpdateContainerRepositoryDetails.
        Whether the repository is public. A public repository allows unauthenticated access.


        :return: The is_public of this UpdateContainerRepositoryDetails.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """
        Sets the is_public of this UpdateContainerRepositoryDetails.
        Whether the repository is public. A public repository allows unauthenticated access.


        :param is_public: The is_public of this UpdateContainerRepositoryDetails.
        :type: bool
        """
        self._is_public = is_public

    @property
    def readme(self):
        """
        Gets the readme of this UpdateContainerRepositoryDetails.

        :return: The readme of this UpdateContainerRepositoryDetails.
        :rtype: oci.artifacts.models.ContainerRepositoryReadme
        """
        return self._readme

    @readme.setter
    def readme(self, readme):
        """
        Sets the readme of this UpdateContainerRepositoryDetails.

        :param readme: The readme of this UpdateContainerRepositoryDetails.
        :type: oci.artifacts.models.ContainerRepositoryReadme
        """
        self._readme = readme

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
