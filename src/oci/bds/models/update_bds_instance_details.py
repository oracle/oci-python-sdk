# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBdsInstanceDetails(object):
    """
    The information about to-be-updated Big Data Service cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBdsInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateBdsInstanceDetails.
        :type display_name: str

        :param bootstrap_script_url:
            The value to assign to the bootstrap_script_url property of this UpdateBdsInstanceDetails.
        :type bootstrap_script_url: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateBdsInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateBdsInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'bootstrap_script_url': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'bootstrap_script_url': 'bootstrapScriptUrl',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._bootstrap_script_url = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateBdsInstanceDetails.
        Name of the cluster.


        :return: The display_name of this UpdateBdsInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateBdsInstanceDetails.
        Name of the cluster.


        :param display_name: The display_name of this UpdateBdsInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def bootstrap_script_url(self):
        """
        Gets the bootstrap_script_url of this UpdateBdsInstanceDetails.
        Pre-authenticated URL of the bootstrap script in Object Store that can be downloaded and executed..


        :return: The bootstrap_script_url of this UpdateBdsInstanceDetails.
        :rtype: str
        """
        return self._bootstrap_script_url

    @bootstrap_script_url.setter
    def bootstrap_script_url(self, bootstrap_script_url):
        """
        Sets the bootstrap_script_url of this UpdateBdsInstanceDetails.
        Pre-authenticated URL of the bootstrap script in Object Store that can be downloaded and executed..


        :param bootstrap_script_url: The bootstrap_script_url of this UpdateBdsInstanceDetails.
        :type: str
        """
        self._bootstrap_script_url = bootstrap_script_url

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateBdsInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only. For example, `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateBdsInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateBdsInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only. For example, `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateBdsInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateBdsInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example, `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateBdsInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateBdsInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example, `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateBdsInstanceDetails.
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
