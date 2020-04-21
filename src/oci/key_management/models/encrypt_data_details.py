# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EncryptDataDetails(object):
    """
    EncryptDataDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EncryptDataDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param associated_data:
            The value to assign to the associated_data property of this EncryptDataDetails.
        :type associated_data: dict(str, str)

        :param key_id:
            The value to assign to the key_id property of this EncryptDataDetails.
        :type key_id: str

        :param logging_context:
            The value to assign to the logging_context property of this EncryptDataDetails.
        :type logging_context: dict(str, str)

        :param plaintext:
            The value to assign to the plaintext property of this EncryptDataDetails.
        :type plaintext: str

        """
        self.swagger_types = {
            'associated_data': 'dict(str, str)',
            'key_id': 'str',
            'logging_context': 'dict(str, str)',
            'plaintext': 'str'
        }

        self.attribute_map = {
            'associated_data': 'associatedData',
            'key_id': 'keyId',
            'logging_context': 'loggingContext',
            'plaintext': 'plaintext'
        }

        self._associated_data = None
        self._key_id = None
        self._logging_context = None
        self._plaintext = None

    @property
    def associated_data(self):
        """
        Gets the associated_data of this EncryptDataDetails.
        Information that can be used to provide an encryption context for the
        encrypted data. The length of the string representation of the associated data
        must be fewer than 4096 characters.


        :return: The associated_data of this EncryptDataDetails.
        :rtype: dict(str, str)
        """
        return self._associated_data

    @associated_data.setter
    def associated_data(self, associated_data):
        """
        Sets the associated_data of this EncryptDataDetails.
        Information that can be used to provide an encryption context for the
        encrypted data. The length of the string representation of the associated data
        must be fewer than 4096 characters.


        :param associated_data: The associated_data of this EncryptDataDetails.
        :type: dict(str, str)
        """
        self._associated_data = associated_data

    @property
    def key_id(self):
        """
        **[Required]** Gets the key_id of this EncryptDataDetails.
        The OCID of the key to encrypt with.


        :return: The key_id of this EncryptDataDetails.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this EncryptDataDetails.
        The OCID of the key to encrypt with.


        :param key_id: The key_id of this EncryptDataDetails.
        :type: str
        """
        self._key_id = key_id

    @property
    def logging_context(self):
        """
        Gets the logging_context of this EncryptDataDetails.
        Information that provides context for audit logging. You can provide this additional
        data as key-value pairs to include in the audit logs when audit logging is enabled.


        :return: The logging_context of this EncryptDataDetails.
        :rtype: dict(str, str)
        """
        return self._logging_context

    @logging_context.setter
    def logging_context(self, logging_context):
        """
        Sets the logging_context of this EncryptDataDetails.
        Information that provides context for audit logging. You can provide this additional
        data as key-value pairs to include in the audit logs when audit logging is enabled.


        :param logging_context: The logging_context of this EncryptDataDetails.
        :type: dict(str, str)
        """
        self._logging_context = logging_context

    @property
    def plaintext(self):
        """
        **[Required]** Gets the plaintext of this EncryptDataDetails.
        The plaintext data to encrypt.


        :return: The plaintext of this EncryptDataDetails.
        :rtype: str
        """
        return self._plaintext

    @plaintext.setter
    def plaintext(self, plaintext):
        """
        Sets the plaintext of this EncryptDataDetails.
        The plaintext data to encrypt.


        :param plaintext: The plaintext of this EncryptDataDetails.
        :type: str
        """
        self._plaintext = plaintext

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
