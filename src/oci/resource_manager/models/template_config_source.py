# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TemplateConfigSource(object):
    """
    Information about the Template.
    """

    #: A constant which can be used with the template_config_source_type property of a TemplateConfigSource.
    #: This constant has a value of "ZIP_UPLOAD"
    TEMPLATE_CONFIG_SOURCE_TYPE_ZIP_UPLOAD = "ZIP_UPLOAD"

    def __init__(self, **kwargs):
        """
        Initializes a new TemplateConfigSource object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.resource_manager.models.TemplateZipUploadConfigSource`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param template_config_source_type:
            The value to assign to the template_config_source_type property of this TemplateConfigSource.
            Allowed values for this property are: "ZIP_UPLOAD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type template_config_source_type: str

        """
        self.swagger_types = {
            'template_config_source_type': 'str'
        }

        self.attribute_map = {
            'template_config_source_type': 'templateConfigSourceType'
        }

        self._template_config_source_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['templateConfigSourceType']

        if type == 'ZIP_UPLOAD':
            return 'TemplateZipUploadConfigSource'
        else:
            return 'TemplateConfigSource'

    @property
    def template_config_source_type(self):
        """
        **[Required]** Gets the template_config_source_type of this TemplateConfigSource.
        The type of configuration source to use for the template configuration.

        Allowed values for this property are: "ZIP_UPLOAD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The template_config_source_type of this TemplateConfigSource.
        :rtype: str
        """
        return self._template_config_source_type

    @template_config_source_type.setter
    def template_config_source_type(self, template_config_source_type):
        """
        Sets the template_config_source_type of this TemplateConfigSource.
        The type of configuration source to use for the template configuration.


        :param template_config_source_type: The template_config_source_type of this TemplateConfigSource.
        :type: str
        """
        allowed_values = ["ZIP_UPLOAD"]
        if not value_allowed_none_or_none_sentinel(template_config_source_type, allowed_values):
            template_config_source_type = 'UNKNOWN_ENUM_VALUE'
        self._template_config_source_type = template_config_source_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
