# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateInstanceConfigurationBase(object):
    """
    Creation details for an instance configuration.
    """

    #: A constant which can be used with the source property of a CreateInstanceConfigurationBase.
    #: This constant has a value of "NONE"
    SOURCE_NONE = "NONE"

    #: A constant which can be used with the source property of a CreateInstanceConfigurationBase.
    #: This constant has a value of "INSTANCE"
    SOURCE_INSTANCE = "INSTANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateInstanceConfigurationBase object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.CreateInstanceConfigurationDetails`
        * :class:`~oci.core.models.CreateInstanceConfigurationFromInstanceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateInstanceConfigurationBase.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateInstanceConfigurationBase.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateInstanceConfigurationBase.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateInstanceConfigurationBase.
        :type freeform_tags: dict(str, str)

        :param source:
            The value to assign to the source property of this CreateInstanceConfigurationBase.
            Allowed values for this property are: "NONE", "INSTANCE"
        :type source: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'source': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'source': 'source'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._source = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['source']

        if type == 'NONE':
            return 'CreateInstanceConfigurationDetails'

        if type == 'INSTANCE':
            return 'CreateInstanceConfigurationFromInstanceDetails'
        else:
            return 'CreateInstanceConfigurationBase'

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateInstanceConfigurationBase.
        The `OCID`__ of the compartment
        containing the instance configuration.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateInstanceConfigurationBase.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateInstanceConfigurationBase.
        The `OCID`__ of the compartment
        containing the instance configuration.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateInstanceConfigurationBase.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateInstanceConfigurationBase.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateInstanceConfigurationBase.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateInstanceConfigurationBase.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateInstanceConfigurationBase.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateInstanceConfigurationBase.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateInstanceConfigurationBase.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateInstanceConfigurationBase.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateInstanceConfigurationBase.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateInstanceConfigurationBase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateInstanceConfigurationBase.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateInstanceConfigurationBase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateInstanceConfigurationBase.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def source(self):
        """
        Gets the source of this CreateInstanceConfigurationBase.
        The source of the instance configuration. An instance configuration defines the
        settings to use when creating Compute instances, including details
        such as the base image, shape, and metadata. You can also specify the associated resources for the
        instance, such as block volume attachments and network configuration.

        When you create an instance configuration using an existing instance as a template, the instance
        configuration does not include any information from the source instance's boot volume, such as installed
        applications, binaries, and files on the instance. It also does not include the contents of
        any block volumes that are attached to the instance.

        To create an instance configuration that includes the custom setup from an instance's boot volume, you
        must first create a custom image from the instance (see :func:`create_image`).
        Then, use the custom image to launch a new instance
        (see :func:`launch_instance`). Finally, create the instance
        configuration based on the instance that you created from the custom image.

        To include block volume contents with an instance configuration, first create a backup of the attached block volumes
        (see :func:`create_volume_backup`). Then, create the instance
        configuration by specifying the list of settings, using
        :func:`instance_configuration_volume_source_from_volume_backup_details`
        to include the block volume backups in the list of settings.

        The following values are supported:

        * `NONE`: Creates an instance configuration using the list of settings that you specify.

        * `INSTANCE`: Creates an instance configuration using an existing instance as a template.

        Allowed values for this property are: "NONE", "INSTANCE"


        :return: The source of this CreateInstanceConfigurationBase.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CreateInstanceConfigurationBase.
        The source of the instance configuration. An instance configuration defines the
        settings to use when creating Compute instances, including details
        such as the base image, shape, and metadata. You can also specify the associated resources for the
        instance, such as block volume attachments and network configuration.

        When you create an instance configuration using an existing instance as a template, the instance
        configuration does not include any information from the source instance's boot volume, such as installed
        applications, binaries, and files on the instance. It also does not include the contents of
        any block volumes that are attached to the instance.

        To create an instance configuration that includes the custom setup from an instance's boot volume, you
        must first create a custom image from the instance (see :func:`create_image`).
        Then, use the custom image to launch a new instance
        (see :func:`launch_instance`). Finally, create the instance
        configuration based on the instance that you created from the custom image.

        To include block volume contents with an instance configuration, first create a backup of the attached block volumes
        (see :func:`create_volume_backup`). Then, create the instance
        configuration by specifying the list of settings, using
        :func:`instance_configuration_volume_source_from_volume_backup_details`
        to include the block volume backups in the list of settings.

        The following values are supported:

        * `NONE`: Creates an instance configuration using the list of settings that you specify.

        * `INSTANCE`: Creates an instance configuration using an existing instance as a template.


        :param source: The source of this CreateInstanceConfigurationBase.
        :type: str
        """
        allowed_values = ["NONE", "INSTANCE"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            raise ValueError(
                "Invalid value for `source`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._source = source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
