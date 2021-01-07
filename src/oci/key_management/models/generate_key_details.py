# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateKeyDetails(object):
    """
    GenerateKeyDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param associated_data:
            The value to assign to the associated_data property of this GenerateKeyDetails.
        :type associated_data: dict(str, str)

        :param include_plaintext_key:
            The value to assign to the include_plaintext_key property of this GenerateKeyDetails.
        :type include_plaintext_key: bool

        :param key_id:
            The value to assign to the key_id property of this GenerateKeyDetails.
        :type key_id: str

        :param key_shape:
            The value to assign to the key_shape property of this GenerateKeyDetails.
        :type key_shape: oci.key_management.models.KeyShape

        :param logging_context:
            The value to assign to the logging_context property of this GenerateKeyDetails.
        :type logging_context: dict(str, str)

        """
        self.swagger_types = {
            'associated_data': 'dict(str, str)',
            'include_plaintext_key': 'bool',
            'key_id': 'str',
            'key_shape': 'KeyShape',
            'logging_context': 'dict(str, str)'
        }

        self.attribute_map = {
            'associated_data': 'associatedData',
            'include_plaintext_key': 'includePlaintextKey',
            'key_id': 'keyId',
            'key_shape': 'keyShape',
            'logging_context': 'loggingContext'
        }

        self._associated_data = None
        self._include_plaintext_key = None
        self._key_id = None
        self._key_shape = None
        self._logging_context = None

    @property
    def associated_data(self):
        """
        Gets the associated_data of this GenerateKeyDetails.
        Information that can be used to provide an encryption context for the encrypted data.
        The length of the string representation of the associated data must be fewer than 4096
        characters.


        :return: The associated_data of this GenerateKeyDetails.
        :rtype: dict(str, str)
        """
        return self._associated_data

    @associated_data.setter
    def associated_data(self, associated_data):
        """
        Sets the associated_data of this GenerateKeyDetails.
        Information that can be used to provide an encryption context for the encrypted data.
        The length of the string representation of the associated data must be fewer than 4096
        characters.


        :param associated_data: The associated_data of this GenerateKeyDetails.
        :type: dict(str, str)
        """
        self._associated_data = associated_data

    @property
    def include_plaintext_key(self):
        """
        **[Required]** Gets the include_plaintext_key of this GenerateKeyDetails.
        If true, the generated key is also returned unencrypted.


        :return: The include_plaintext_key of this GenerateKeyDetails.
        :rtype: bool
        """
        return self._include_plaintext_key

    @include_plaintext_key.setter
    def include_plaintext_key(self, include_plaintext_key):
        """
        Sets the include_plaintext_key of this GenerateKeyDetails.
        If true, the generated key is also returned unencrypted.


        :param include_plaintext_key: The include_plaintext_key of this GenerateKeyDetails.
        :type: bool
        """
        self._include_plaintext_key = include_plaintext_key

    @property
    def key_id(self):
        """
        **[Required]** Gets the key_id of this GenerateKeyDetails.
        The OCID of the master encryption key to encrypt the generated data encryption key with.


        :return: The key_id of this GenerateKeyDetails.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this GenerateKeyDetails.
        The OCID of the master encryption key to encrypt the generated data encryption key with.


        :param key_id: The key_id of this GenerateKeyDetails.
        :type: str
        """
        self._key_id = key_id

    @property
    def key_shape(self):
        """
        **[Required]** Gets the key_shape of this GenerateKeyDetails.

        :return: The key_shape of this GenerateKeyDetails.
        :rtype: oci.key_management.models.KeyShape
        """
        return self._key_shape

    @key_shape.setter
    def key_shape(self, key_shape):
        """
        Sets the key_shape of this GenerateKeyDetails.

        :param key_shape: The key_shape of this GenerateKeyDetails.
        :type: oci.key_management.models.KeyShape
        """
        self._key_shape = key_shape

    @property
    def logging_context(self):
        """
        Gets the logging_context of this GenerateKeyDetails.
        Information that provides context for audit logging. You can provide this additional
        data by formatting it as key-value pairs to include in audit logs when audit logging is enabled.


        :return: The logging_context of this GenerateKeyDetails.
        :rtype: dict(str, str)
        """
        return self._logging_context

    @logging_context.setter
    def logging_context(self, logging_context):
        """
        Sets the logging_context of this GenerateKeyDetails.
        Information that provides context for audit logging. You can provide this additional
        data by formatting it as key-value pairs to include in audit logs when audit logging is enabled.


        :param logging_context: The logging_context of this GenerateKeyDetails.
        :type: dict(str, str)
        """
        self._logging_context = logging_context

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
