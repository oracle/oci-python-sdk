# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportKeyDetails(object):
    """
    ImportKeyDetails model.
    """

    #: A constant which can be used with the protection_mode property of a ImportKeyDetails.
    #: This constant has a value of "HSM"
    PROTECTION_MODE_HSM = "HSM"

    #: A constant which can be used with the protection_mode property of a ImportKeyDetails.
    #: This constant has a value of "SOFTWARE"
    PROTECTION_MODE_SOFTWARE = "SOFTWARE"

    def __init__(self, **kwargs):
        """
        Initializes a new ImportKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ImportKeyDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this ImportKeyDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this ImportKeyDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ImportKeyDetails.
        :type freeform_tags: dict(str, str)

        :param key_shape:
            The value to assign to the key_shape property of this ImportKeyDetails.
        :type key_shape: oci.key_management.models.KeyShape

        :param wrapped_import_key:
            The value to assign to the wrapped_import_key property of this ImportKeyDetails.
        :type wrapped_import_key: oci.key_management.models.WrappedImportKey

        :param protection_mode:
            The value to assign to the protection_mode property of this ImportKeyDetails.
            Allowed values for this property are: "HSM", "SOFTWARE"
        :type protection_mode: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'key_shape': 'KeyShape',
            'wrapped_import_key': 'WrappedImportKey',
            'protection_mode': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'key_shape': 'keyShape',
            'wrapped_import_key': 'wrappedImportKey',
            'protection_mode': 'protectionMode'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._key_shape = None
        self._wrapped_import_key = None
        self._protection_mode = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ImportKeyDetails.
        The OCID of the compartment that contains this key.


        :return: The compartment_id of this ImportKeyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ImportKeyDetails.
        The OCID of the compartment that contains this key.


        :param compartment_id: The compartment_id of this ImportKeyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ImportKeyDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :return: The defined_tags of this ImportKeyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ImportKeyDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :param defined_tags: The defined_tags of this ImportKeyDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ImportKeyDetails.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this ImportKeyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ImportKeyDetails.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this ImportKeyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ImportKeyDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ImportKeyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ImportKeyDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ImportKeyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def key_shape(self):
        """
        **[Required]** Gets the key_shape of this ImportKeyDetails.

        :return: The key_shape of this ImportKeyDetails.
        :rtype: oci.key_management.models.KeyShape
        """
        return self._key_shape

    @key_shape.setter
    def key_shape(self, key_shape):
        """
        Sets the key_shape of this ImportKeyDetails.

        :param key_shape: The key_shape of this ImportKeyDetails.
        :type: oci.key_management.models.KeyShape
        """
        self._key_shape = key_shape

    @property
    def wrapped_import_key(self):
        """
        **[Required]** Gets the wrapped_import_key of this ImportKeyDetails.

        :return: The wrapped_import_key of this ImportKeyDetails.
        :rtype: oci.key_management.models.WrappedImportKey
        """
        return self._wrapped_import_key

    @wrapped_import_key.setter
    def wrapped_import_key(self, wrapped_import_key):
        """
        Sets the wrapped_import_key of this ImportKeyDetails.

        :param wrapped_import_key: The wrapped_import_key of this ImportKeyDetails.
        :type: oci.key_management.models.WrappedImportKey
        """
        self._wrapped_import_key = wrapped_import_key

    @property
    def protection_mode(self):
        """
        Gets the protection_mode of this ImportKeyDetails.
        The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed.
        A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside
        the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists
        on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default,
        a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.

        Allowed values for this property are: "HSM", "SOFTWARE"


        :return: The protection_mode of this ImportKeyDetails.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """
        Sets the protection_mode of this ImportKeyDetails.
        The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed.
        A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside
        the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists
        on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default,
        a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.


        :param protection_mode: The protection_mode of this ImportKeyDetails.
        :type: str
        """
        allowed_values = ["HSM", "SOFTWARE"]
        if not value_allowed_none_or_none_sentinel(protection_mode, allowed_values):
            raise ValueError(
                "Invalid value for `protection_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._protection_mode = protection_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
