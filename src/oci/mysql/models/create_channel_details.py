# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateChannelDetails(object):
    """
    Details required to create a Channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateChannelDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateChannelDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateChannelDetails.
        :type display_name: str

        :param is_enabled:
            The value to assign to the is_enabled property of this CreateChannelDetails.
        :type is_enabled: bool

        :param source:
            The value to assign to the source property of this CreateChannelDetails.
        :type source: oci.mysql.models.CreateChannelSourceDetails

        :param target:
            The value to assign to the target property of this CreateChannelDetails.
        :type target: oci.mysql.models.CreateChannelTargetDetails

        :param description:
            The value to assign to the description property of this CreateChannelDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateChannelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateChannelDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'is_enabled': 'bool',
            'source': 'CreateChannelSourceDetails',
            'target': 'CreateChannelTargetDetails',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'is_enabled': 'isEnabled',
            'source': 'source',
            'target': 'target',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._is_enabled = None
        self._source = None
        self._target = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateChannelDetails.
        The OCID of the compartment.


        :return: The compartment_id of this CreateChannelDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateChannelDetails.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this CreateChannelDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateChannelDetails.
        The user-friendly name for the Channel. It does not have to be unique.


        :return: The display_name of this CreateChannelDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateChannelDetails.
        The user-friendly name for the Channel. It does not have to be unique.


        :param display_name: The display_name of this CreateChannelDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this CreateChannelDetails.
        Whether the Channel should be enabled upon creation. If set to true, the Channel
        will be asynchronously started as a result of the create Channel operation.


        :return: The is_enabled of this CreateChannelDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this CreateChannelDetails.
        Whether the Channel should be enabled upon creation. If set to true, the Channel
        will be asynchronously started as a result of the create Channel operation.


        :param is_enabled: The is_enabled of this CreateChannelDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def source(self):
        """
        **[Required]** Gets the source of this CreateChannelDetails.

        :return: The source of this CreateChannelDetails.
        :rtype: oci.mysql.models.CreateChannelSourceDetails
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CreateChannelDetails.

        :param source: The source of this CreateChannelDetails.
        :type: oci.mysql.models.CreateChannelSourceDetails
        """
        self._source = source

    @property
    def target(self):
        """
        **[Required]** Gets the target of this CreateChannelDetails.

        :return: The target of this CreateChannelDetails.
        :rtype: oci.mysql.models.CreateChannelTargetDetails
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this CreateChannelDetails.

        :param target: The target of this CreateChannelDetails.
        :type: oci.mysql.models.CreateChannelTargetDetails
        """
        self._target = target

    @property
    def description(self):
        """
        Gets the description of this CreateChannelDetails.
        User provided information about the Channel.


        :return: The description of this CreateChannelDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateChannelDetails.
        User provided information about the Channel.


        :param description: The description of this CreateChannelDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateChannelDetails.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateChannelDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateChannelDetails.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateChannelDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateChannelDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateChannelDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateChannelDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateChannelDetails.
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
