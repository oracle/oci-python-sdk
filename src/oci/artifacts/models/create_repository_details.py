# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRepositoryDetails(object):
    """
    Parameters needed to create an artifact repository.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRepositoryDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.artifacts.models.CreateGenericRepositoryDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateRepositoryDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateRepositoryDetails.
        :type compartment_id: str

        :param repository_type:
            The value to assign to the repository_type property of this CreateRepositoryDetails.
        :type repository_type: str

        :param description:
            The value to assign to the description property of this CreateRepositoryDetails.
        :type description: str

        :param is_immutable:
            The value to assign to the is_immutable property of this CreateRepositoryDetails.
        :type is_immutable: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateRepositoryDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateRepositoryDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'repository_type': 'str',
            'description': 'str',
            'is_immutable': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'repository_type': 'repositoryType',
            'description': 'description',
            'is_immutable': 'isImmutable',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._repository_type = None
        self._description = None
        self._is_immutable = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['repositoryType']

        if type == 'GENERIC':
            return 'CreateGenericRepositoryDetails'
        else:
            return 'CreateRepositoryDetails'

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateRepositoryDetails.
        A user-friendly display name for the repository. If not present, will be auto-generated. It can be modified later. Avoid entering confidential information.


        :return: The display_name of this CreateRepositoryDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateRepositoryDetails.
        A user-friendly display name for the repository. If not present, will be auto-generated. It can be modified later. Avoid entering confidential information.


        :param display_name: The display_name of this CreateRepositoryDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateRepositoryDetails.
        The `OCID`__ of the repository's compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateRepositoryDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateRepositoryDetails.
        The `OCID`__ of the repository's compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateRepositoryDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def repository_type(self):
        """
        **[Required]** Gets the repository_type of this CreateRepositoryDetails.
        The repository's supported artifact type.


        :return: The repository_type of this CreateRepositoryDetails.
        :rtype: str
        """
        return self._repository_type

    @repository_type.setter
    def repository_type(self, repository_type):
        """
        Sets the repository_type of this CreateRepositoryDetails.
        The repository's supported artifact type.


        :param repository_type: The repository_type of this CreateRepositoryDetails.
        :type: str
        """
        self._repository_type = repository_type

    @property
    def description(self):
        """
        Gets the description of this CreateRepositoryDetails.
        A short description of the repository. It can be updated later.


        :return: The description of this CreateRepositoryDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateRepositoryDetails.
        A short description of the repository. It can be updated later.


        :param description: The description of this CreateRepositoryDetails.
        :type: str
        """
        self._description = description

    @property
    def is_immutable(self):
        """
        **[Required]** Gets the is_immutable of this CreateRepositoryDetails.
        Whether to make the repository immutable. The artifacts of an immutable repository cannot be overwritten.


        :return: The is_immutable of this CreateRepositoryDetails.
        :rtype: bool
        """
        return self._is_immutable

    @is_immutable.setter
    def is_immutable(self, is_immutable):
        """
        Sets the is_immutable of this CreateRepositoryDetails.
        Whether to make the repository immutable. The artifacts of an immutable repository cannot be overwritten.


        :param is_immutable: The is_immutable of this CreateRepositoryDetails.
        :type: bool
        """
        self._is_immutable = is_immutable

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateRepositoryDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateRepositoryDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateRepositoryDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateRepositoryDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateRepositoryDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateRepositoryDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateRepositoryDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateRepositoryDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
