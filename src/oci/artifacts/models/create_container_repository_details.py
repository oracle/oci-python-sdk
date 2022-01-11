# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateContainerRepositoryDetails(object):
    """
    Create container repository details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateContainerRepositoryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateContainerRepositoryDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateContainerRepositoryDetails.
        :type display_name: str

        :param is_immutable:
            The value to assign to the is_immutable property of this CreateContainerRepositoryDetails.
        :type is_immutable: bool

        :param is_public:
            The value to assign to the is_public property of this CreateContainerRepositoryDetails.
        :type is_public: bool

        :param readme:
            The value to assign to the readme property of this CreateContainerRepositoryDetails.
        :type readme: oci.artifacts.models.ContainerRepositoryReadme

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'is_immutable': 'bool',
            'is_public': 'bool',
            'readme': 'ContainerRepositoryReadme'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'is_immutable': 'isImmutable',
            'is_public': 'isPublic',
            'readme': 'readme'
        }

        self._compartment_id = None
        self._display_name = None
        self._is_immutable = None
        self._is_public = None
        self._readme = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateContainerRepositoryDetails.
        The `OCID`__ of the compartment in which to create the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateContainerRepositoryDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateContainerRepositoryDetails.
        The `OCID`__ of the compartment in which to create the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateContainerRepositoryDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateContainerRepositoryDetails.
        The container repository name.


        :return: The display_name of this CreateContainerRepositoryDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateContainerRepositoryDetails.
        The container repository name.


        :param display_name: The display_name of this CreateContainerRepositoryDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_immutable(self):
        """
        Gets the is_immutable of this CreateContainerRepositoryDetails.
        Whether the repository is immutable. Images cannot be overwritten in an immutable repository.


        :return: The is_immutable of this CreateContainerRepositoryDetails.
        :rtype: bool
        """
        return self._is_immutable

    @is_immutable.setter
    def is_immutable(self, is_immutable):
        """
        Sets the is_immutable of this CreateContainerRepositoryDetails.
        Whether the repository is immutable. Images cannot be overwritten in an immutable repository.


        :param is_immutable: The is_immutable of this CreateContainerRepositoryDetails.
        :type: bool
        """
        self._is_immutable = is_immutable

    @property
    def is_public(self):
        """
        Gets the is_public of this CreateContainerRepositoryDetails.
        Whether the repository is public. A public repository allows unauthenticated access.


        :return: The is_public of this CreateContainerRepositoryDetails.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """
        Sets the is_public of this CreateContainerRepositoryDetails.
        Whether the repository is public. A public repository allows unauthenticated access.


        :param is_public: The is_public of this CreateContainerRepositoryDetails.
        :type: bool
        """
        self._is_public = is_public

    @property
    def readme(self):
        """
        Gets the readme of this CreateContainerRepositoryDetails.

        :return: The readme of this CreateContainerRepositoryDetails.
        :rtype: oci.artifacts.models.ContainerRepositoryReadme
        """
        return self._readme

    @readme.setter
    def readme(self, readme):
        """
        Sets the readme of this CreateContainerRepositoryDetails.

        :param readme: The readme of this CreateContainerRepositoryDetails.
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
