# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateKeyDetails(object):
    """
    CreateKeyDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateKeyDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateKeyDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateKeyDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateKeyDetails.
        :type freeform_tags: dict(str, str)

        :param key_shape:
            The value to assign to the key_shape property of this CreateKeyDetails.
        :type key_shape: KeyShape

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'key_shape': 'KeyShape'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'key_shape': 'keyShape'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._key_shape = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateKeyDetails.
        The OCID of the compartment that contains this key.


        :return: The compartment_id of this CreateKeyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateKeyDetails.
        The OCID of the compartment that contains this key.


        :param compartment_id: The compartment_id of this CreateKeyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateKeyDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :return: The defined_tags of this CreateKeyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateKeyDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :param defined_tags: The defined_tags of this CreateKeyDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateKeyDetails.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateKeyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateKeyDetails.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateKeyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateKeyDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateKeyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateKeyDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateKeyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def key_shape(self):
        """
        **[Required]** Gets the key_shape of this CreateKeyDetails.

        :return: The key_shape of this CreateKeyDetails.
        :rtype: KeyShape
        """
        return self._key_shape

    @key_shape.setter
    def key_shape(self, key_shape):
        """
        Sets the key_shape of this CreateKeyDetails.

        :param key_shape: The key_shape of this CreateKeyDetails.
        :type: KeyShape
        """
        self._key_shape = key_shape

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
