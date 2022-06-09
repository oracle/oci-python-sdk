# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .template import Template
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TagTemplate(Template):
    """
    Template for governance rules of type tag.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TagTemplate object with values from keyword arguments. The default value of the :py:attr:`~oci.governance_rules_control_plane.models.TagTemplate.type` attribute
        of this class is ``TAG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TagTemplate.
            Allowed values for this property are: "QUOTA", "TAG", "ALLOWED_REGIONS"
        :type type: str

        :param name:
            The value to assign to the name property of this TagTemplate.
        :type name: str

        :param description:
            The value to assign to the description property of this TagTemplate.
        :type description: str

        :param tags:
            The value to assign to the tags property of this TagTemplate.
        :type tags: list[oci.governance_rules_control_plane.models.Tag]

        :param tag_defaults:
            The value to assign to the tag_defaults property of this TagTemplate.
        :type tag_defaults: list[oci.governance_rules_control_plane.models.TagDefault]

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'description': 'str',
            'tags': 'list[Tag]',
            'tag_defaults': 'list[TagDefault]'
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'description': 'description',
            'tags': 'tags',
            'tag_defaults': 'tagDefaults'
        }

        self._type = None
        self._name = None
        self._description = None
        self._tags = None
        self._tag_defaults = None
        self._type = 'TAG'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this TagTemplate.
        The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.


        :return: The name of this TagTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TagTemplate.
        The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.


        :param name: The name of this TagTemplate.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TagTemplate.
        Description of the tag namespace.


        :return: The description of this TagTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TagTemplate.
        Description of the tag namespace.


        :param description: The description of this TagTemplate.
        :type: str
        """
        self._description = description

    @property
    def tags(self):
        """
        Gets the tags of this TagTemplate.
        Represents an array of tags for tag namespace.


        :return: The tags of this TagTemplate.
        :rtype: list[oci.governance_rules_control_plane.models.Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this TagTemplate.
        Represents an array of tags for tag namespace.


        :param tags: The tags of this TagTemplate.
        :type: list[oci.governance_rules_control_plane.models.Tag]
        """
        self._tags = tags

    @property
    def tag_defaults(self):
        """
        Gets the tag_defaults of this TagTemplate.

        :return: The tag_defaults of this TagTemplate.
        :rtype: list[oci.governance_rules_control_plane.models.TagDefault]
        """
        return self._tag_defaults

    @tag_defaults.setter
    def tag_defaults(self, tag_defaults):
        """
        Sets the tag_defaults of this TagTemplate.

        :param tag_defaults: The tag_defaults of this TagTemplate.
        :type: list[oci.governance_rules_control_plane.models.TagDefault]
        """
        self._tag_defaults = tag_defaults

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
