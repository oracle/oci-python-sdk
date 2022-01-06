# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalPublicationValidation(object):
    """
    The information about external published task validation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalPublicationValidation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total_message_count:
            The value to assign to the total_message_count property of this ExternalPublicationValidation.
        :type total_message_count: int

        :param error_message_count:
            The value to assign to the error_message_count property of this ExternalPublicationValidation.
        :type error_message_count: int

        :param warn_message_count:
            The value to assign to the warn_message_count property of this ExternalPublicationValidation.
        :type warn_message_count: int

        :param info_message_count:
            The value to assign to the info_message_count property of this ExternalPublicationValidation.
        :type info_message_count: int

        :param validation_messages:
            The value to assign to the validation_messages property of this ExternalPublicationValidation.
        :type validation_messages: dict(str, list[ValidationMessage])

        :param key:
            The value to assign to the key property of this ExternalPublicationValidation.
        :type key: str

        """
        self.swagger_types = {
            'total_message_count': 'int',
            'error_message_count': 'int',
            'warn_message_count': 'int',
            'info_message_count': 'int',
            'validation_messages': 'dict(str, list[ValidationMessage])',
            'key': 'str'
        }

        self.attribute_map = {
            'total_message_count': 'totalMessageCount',
            'error_message_count': 'errorMessageCount',
            'warn_message_count': 'warnMessageCount',
            'info_message_count': 'infoMessageCount',
            'validation_messages': 'validationMessages',
            'key': 'key'
        }

        self._total_message_count = None
        self._error_message_count = None
        self._warn_message_count = None
        self._info_message_count = None
        self._validation_messages = None
        self._key = None

    @property
    def total_message_count(self):
        """
        Gets the total_message_count of this ExternalPublicationValidation.
        Total number of validation messages.


        :return: The total_message_count of this ExternalPublicationValidation.
        :rtype: int
        """
        return self._total_message_count

    @total_message_count.setter
    def total_message_count(self, total_message_count):
        """
        Sets the total_message_count of this ExternalPublicationValidation.
        Total number of validation messages.


        :param total_message_count: The total_message_count of this ExternalPublicationValidation.
        :type: int
        """
        self._total_message_count = total_message_count

    @property
    def error_message_count(self):
        """
        Gets the error_message_count of this ExternalPublicationValidation.
        Total number of validation error messages.


        :return: The error_message_count of this ExternalPublicationValidation.
        :rtype: int
        """
        return self._error_message_count

    @error_message_count.setter
    def error_message_count(self, error_message_count):
        """
        Sets the error_message_count of this ExternalPublicationValidation.
        Total number of validation error messages.


        :param error_message_count: The error_message_count of this ExternalPublicationValidation.
        :type: int
        """
        self._error_message_count = error_message_count

    @property
    def warn_message_count(self):
        """
        Gets the warn_message_count of this ExternalPublicationValidation.
        Total number of validation warning messages.


        :return: The warn_message_count of this ExternalPublicationValidation.
        :rtype: int
        """
        return self._warn_message_count

    @warn_message_count.setter
    def warn_message_count(self, warn_message_count):
        """
        Sets the warn_message_count of this ExternalPublicationValidation.
        Total number of validation warning messages.


        :param warn_message_count: The warn_message_count of this ExternalPublicationValidation.
        :type: int
        """
        self._warn_message_count = warn_message_count

    @property
    def info_message_count(self):
        """
        Gets the info_message_count of this ExternalPublicationValidation.
        Total number of validation information messages.


        :return: The info_message_count of this ExternalPublicationValidation.
        :rtype: int
        """
        return self._info_message_count

    @info_message_count.setter
    def info_message_count(self, info_message_count):
        """
        Sets the info_message_count of this ExternalPublicationValidation.
        Total number of validation information messages.


        :param info_message_count: The info_message_count of this ExternalPublicationValidation.
        :type: int
        """
        self._info_message_count = info_message_count

    @property
    def validation_messages(self):
        """
        Gets the validation_messages of this ExternalPublicationValidation.
        Detailed information of the data flow object validation.


        :return: The validation_messages of this ExternalPublicationValidation.
        :rtype: dict(str, list[ValidationMessage])
        """
        return self._validation_messages

    @validation_messages.setter
    def validation_messages(self, validation_messages):
        """
        Sets the validation_messages of this ExternalPublicationValidation.
        Detailed information of the data flow object validation.


        :param validation_messages: The validation_messages of this ExternalPublicationValidation.
        :type: dict(str, list[ValidationMessage])
        """
        self._validation_messages = validation_messages

    @property
    def key(self):
        """
        Gets the key of this ExternalPublicationValidation.
        Objects use a 36 character key as unique ID. It is system generated and cannot be modified.


        :return: The key of this ExternalPublicationValidation.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ExternalPublicationValidation.
        Objects use a 36 character key as unique ID. It is system generated and cannot be modified.


        :param key: The key of this ExternalPublicationValidation.
        :type: str
        """
        self._key = key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
