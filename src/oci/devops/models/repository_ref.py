# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RepositoryRef(object):
    """
    Reference object with name and commit ID.
    """

    #: A constant which can be used with the ref_type property of a RepositoryRef.
    #: This constant has a value of "BRANCH"
    REF_TYPE_BRANCH = "BRANCH"

    #: A constant which can be used with the ref_type property of a RepositoryRef.
    #: This constant has a value of "TAG"
    REF_TYPE_TAG = "TAG"

    def __init__(self, **kwargs):
        """
        Initializes a new RepositoryRef object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.RepositoryBranch`
        * :class:`~oci.devops.models.RepositoryTag`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ref_name:
            The value to assign to the ref_name property of this RepositoryRef.
        :type ref_name: str

        :param ref_type:
            The value to assign to the ref_type property of this RepositoryRef.
            Allowed values for this property are: "BRANCH", "TAG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type ref_type: str

        :param full_ref_name:
            The value to assign to the full_ref_name property of this RepositoryRef.
        :type full_ref_name: str

        :param repository_id:
            The value to assign to the repository_id property of this RepositoryRef.
        :type repository_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RepositoryRef.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RepositoryRef.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'ref_name': 'str',
            'ref_type': 'str',
            'full_ref_name': 'str',
            'repository_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'ref_name': 'refName',
            'ref_type': 'refType',
            'full_ref_name': 'fullRefName',
            'repository_id': 'repositoryId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._ref_name = None
        self._ref_type = None
        self._full_ref_name = None
        self._repository_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['refType']

        if type == 'BRANCH':
            return 'RepositoryBranch'

        if type == 'TAG':
            return 'RepositoryTag'
        else:
            return 'RepositoryRef'

    @property
    def ref_name(self):
        """
        **[Required]** Gets the ref_name of this RepositoryRef.
        Unique reference name inside a repository.


        :return: The ref_name of this RepositoryRef.
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        """
        Sets the ref_name of this RepositoryRef.
        Unique reference name inside a repository.


        :param ref_name: The ref_name of this RepositoryRef.
        :type: str
        """
        self._ref_name = ref_name

    @property
    def ref_type(self):
        """
        **[Required]** Gets the ref_type of this RepositoryRef.
        The type of reference (BRANCH or TAG).

        Allowed values for this property are: "BRANCH", "TAG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The ref_type of this RepositoryRef.
        :rtype: str
        """
        return self._ref_type

    @ref_type.setter
    def ref_type(self, ref_type):
        """
        Sets the ref_type of this RepositoryRef.
        The type of reference (BRANCH or TAG).


        :param ref_type: The ref_type of this RepositoryRef.
        :type: str
        """
        allowed_values = ["BRANCH", "TAG"]
        if not value_allowed_none_or_none_sentinel(ref_type, allowed_values):
            ref_type = 'UNKNOWN_ENUM_VALUE'
        self._ref_type = ref_type

    @property
    def full_ref_name(self):
        """
        **[Required]** Gets the full_ref_name of this RepositoryRef.
        Unique full reference name inside a repository.


        :return: The full_ref_name of this RepositoryRef.
        :rtype: str
        """
        return self._full_ref_name

    @full_ref_name.setter
    def full_ref_name(self, full_ref_name):
        """
        Sets the full_ref_name of this RepositoryRef.
        Unique full reference name inside a repository.


        :param full_ref_name: The full_ref_name of this RepositoryRef.
        :type: str
        """
        self._full_ref_name = full_ref_name

    @property
    def repository_id(self):
        """
        **[Required]** Gets the repository_id of this RepositoryRef.
        The OCID of the repository containing the reference.


        :return: The repository_id of this RepositoryRef.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this RepositoryRef.
        The OCID of the repository containing the reference.


        :param repository_id: The repository_id of this RepositoryRef.
        :type: str
        """
        self._repository_id = repository_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this RepositoryRef.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this RepositoryRef.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RepositoryRef.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this RepositoryRef.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this RepositoryRef.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this RepositoryRef.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RepositoryRef.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this RepositoryRef.
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
