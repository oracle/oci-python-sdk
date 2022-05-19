# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PackageSummary(object):
    """
    Summary of `Package` object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PackageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PackageSummary.
        :type id: str

        :param publisher_id:
            The value to assign to the publisher_id property of this PackageSummary.
        :type publisher_id: str

        :param name:
            The value to assign to the name property of this PackageSummary.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this PackageSummary.
        :type display_name: str

        :param version:
            The value to assign to the version property of this PackageSummary.
        :type version: str

        :param time_published:
            The value to assign to the time_published property of this PackageSummary.
        :type time_published: datetime

        :param description:
            The value to assign to the description property of this PackageSummary.
        :type description: str

        :param resource_types:
            The value to assign to the resource_types property of this PackageSummary.
        :type resource_types: list[str]

        :param resource_types_metadata:
            The value to assign to the resource_types_metadata property of this PackageSummary.
        :type resource_types_metadata: list[oci.oda.models.ResourceTypeMetadata]

        :param publisher_metadata:
            The value to assign to the publisher_metadata property of this PackageSummary.
        :type publisher_metadata: list[oci.oda.models.MetadataProperty]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PackageSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this PackageSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'publisher_id': 'str',
            'name': 'str',
            'display_name': 'str',
            'version': 'str',
            'time_published': 'datetime',
            'description': 'str',
            'resource_types': 'list[str]',
            'resource_types_metadata': 'list[ResourceTypeMetadata]',
            'publisher_metadata': 'list[MetadataProperty]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'publisher_id': 'publisherId',
            'name': 'name',
            'display_name': 'displayName',
            'version': 'version',
            'time_published': 'timePublished',
            'description': 'description',
            'resource_types': 'resourceTypes',
            'resource_types_metadata': 'resourceTypesMetadata',
            'publisher_metadata': 'publisherMetadata',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._publisher_id = None
        self._name = None
        self._display_name = None
        self._version = None
        self._time_published = None
        self._description = None
        self._resource_types = None
        self._resource_types_metadata = None
        self._publisher_metadata = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PackageSummary.
        Unique immutable identifier that was assigned when the Package was registered.


        :return: The id of this PackageSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PackageSummary.
        Unique immutable identifier that was assigned when the Package was registered.


        :param id: The id of this PackageSummary.
        :type: str
        """
        self._id = id

    @property
    def publisher_id(self):
        """
        **[Required]** Gets the publisher_id of this PackageSummary.
        ID of the publisher providing the package.


        :return: The publisher_id of this PackageSummary.
        :rtype: str
        """
        return self._publisher_id

    @publisher_id.setter
    def publisher_id(self, publisher_id):
        """
        Sets the publisher_id of this PackageSummary.
        ID of the publisher providing the package.


        :param publisher_id: The publisher_id of this PackageSummary.
        :type: str
        """
        self._publisher_id = publisher_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PackageSummary.
        Name of package.


        :return: The name of this PackageSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PackageSummary.
        Name of package.


        :param name: The name of this PackageSummary.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this PackageSummary.
        Display name for the package (displayed in UI and user-facing applications).


        :return: The display_name of this PackageSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PackageSummary.
        Display name for the package (displayed in UI and user-facing applications).


        :param display_name: The display_name of this PackageSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def version(self):
        """
        **[Required]** Gets the version of this PackageSummary.
        Version of the package.


        :return: The version of this PackageSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PackageSummary.
        Version of the package.


        :param version: The version of this PackageSummary.
        :type: str
        """
        self._version = version

    @property
    def time_published(self):
        """
        **[Required]** Gets the time_published of this PackageSummary.
        When the package was last published. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_published of this PackageSummary.
        :rtype: datetime
        """
        return self._time_published

    @time_published.setter
    def time_published(self, time_published):
        """
        Sets the time_published of this PackageSummary.
        When the package was last published. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_published: The time_published of this PackageSummary.
        :type: datetime
        """
        self._time_published = time_published

    @property
    def description(self):
        """
        **[Required]** Gets the description of this PackageSummary.
        Description of the package.


        :return: The description of this PackageSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PackageSummary.
        Description of the package.


        :param description: The description of this PackageSummary.
        :type: str
        """
        self._description = description

    @property
    def resource_types(self):
        """
        **[Required]** Gets the resource_types of this PackageSummary.
        A list of resource types describing the content of the package.


        :return: The resource_types of this PackageSummary.
        :rtype: list[str]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """
        Sets the resource_types of this PackageSummary.
        A list of resource types describing the content of the package.


        :param resource_types: The resource_types of this PackageSummary.
        :type: list[str]
        """
        self._resource_types = resource_types

    @property
    def resource_types_metadata(self):
        """
        **[Required]** Gets the resource_types_metadata of this PackageSummary.
        A map of resource type to metadata key/value map that further describes the content for the resource types in this package.. Keys are resource type names, values are a map of name/value pairs per resource type.


        :return: The resource_types_metadata of this PackageSummary.
        :rtype: list[oci.oda.models.ResourceTypeMetadata]
        """
        return self._resource_types_metadata

    @resource_types_metadata.setter
    def resource_types_metadata(self, resource_types_metadata):
        """
        Sets the resource_types_metadata of this PackageSummary.
        A map of resource type to metadata key/value map that further describes the content for the resource types in this package.. Keys are resource type names, values are a map of name/value pairs per resource type.


        :param resource_types_metadata: The resource_types_metadata of this PackageSummary.
        :type: list[oci.oda.models.ResourceTypeMetadata]
        """
        self._resource_types_metadata = resource_types_metadata

    @property
    def publisher_metadata(self):
        """
        **[Required]** Gets the publisher_metadata of this PackageSummary.
        A map of metadata key/value pairs that further describes the publisher and the platform in which the package might be used.


        :return: The publisher_metadata of this PackageSummary.
        :rtype: list[oci.oda.models.MetadataProperty]
        """
        return self._publisher_metadata

    @publisher_metadata.setter
    def publisher_metadata(self, publisher_metadata):
        """
        Sets the publisher_metadata of this PackageSummary.
        A map of metadata key/value pairs that further describes the publisher and the platform in which the package might be used.


        :param publisher_metadata: The publisher_metadata of this PackageSummary.
        :type: list[oci.oda.models.MetadataProperty]
        """
        self._publisher_metadata = publisher_metadata

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PackageSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this PackageSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PackageSummary.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this PackageSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PackageSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this PackageSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PackageSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this PackageSummary.
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
