# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateStreamCdnConfigDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateStreamCdnConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateStreamCdnConfigDetails.
        :type display_name: str

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateStreamCdnConfigDetails.
        :type is_enabled: bool

        :param config:
            The value to assign to the config property of this UpdateStreamCdnConfigDetails.
        :type config: oci.media_services.models.StreamCdnConfigSection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateStreamCdnConfigDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateStreamCdnConfigDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'is_enabled': 'bool',
            'config': 'StreamCdnConfigSection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'is_enabled': 'isEnabled',
            'config': 'config',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._is_enabled = None
        self._config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateStreamCdnConfigDetails.
        CDN Config display name.


        :return: The display_name of this UpdateStreamCdnConfigDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateStreamCdnConfigDetails.
        CDN Config display name.


        :param display_name: The display_name of this UpdateStreamCdnConfigDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdateStreamCdnConfigDetails.
        Whether CDN is enabled for publishing.


        :return: The is_enabled of this UpdateStreamCdnConfigDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateStreamCdnConfigDetails.
        Whether CDN is enabled for publishing.


        :param is_enabled: The is_enabled of this UpdateStreamCdnConfigDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def config(self):
        """
        Gets the config of this UpdateStreamCdnConfigDetails.

        :return: The config of this UpdateStreamCdnConfigDetails.
        :rtype: oci.media_services.models.StreamCdnConfigSection
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this UpdateStreamCdnConfigDetails.

        :param config: The config of this UpdateStreamCdnConfigDetails.
        :type: oci.media_services.models.StreamCdnConfigSection
        """
        self._config = config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateStreamCdnConfigDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateStreamCdnConfigDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateStreamCdnConfigDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateStreamCdnConfigDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateStreamCdnConfigDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateStreamCdnConfigDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateStreamCdnConfigDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateStreamCdnConfigDetails.
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
