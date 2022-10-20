# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DocumentError(object):
    """
    Error response for document.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DocumentError object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this DocumentError.
        :type key: str

        :param error:
            The value to assign to the error property of this DocumentError.
        :type error: oci.ai_language.models.ErrorDetails

        """
        self.swagger_types = {
            'key': 'str',
            'error': 'ErrorDetails'
        }

        self.attribute_map = {
            'key': 'key',
            'error': 'error'
        }

        self._key = None
        self._error = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this DocumentError.
        Document unique identifier defined by the user.


        :return: The key of this DocumentError.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DocumentError.
        Document unique identifier defined by the user.


        :param key: The key of this DocumentError.
        :type: str
        """
        self._key = key

    @property
    def error(self):
        """
        **[Required]** Gets the error of this DocumentError.

        :return: The error of this DocumentError.
        :rtype: oci.ai_language.models.ErrorDetails
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this DocumentError.

        :param error: The error of this DocumentError.
        :type: oci.ai_language.models.ErrorDetails
        """
        self._error = error

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
