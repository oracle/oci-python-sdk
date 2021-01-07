# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtractLogHeaderDetails(object):
    """
    log header values
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExtractLogHeaderDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param log_key:
            The value to assign to the log_key property of this ExtractLogHeaderDetails.
        :type log_key: str

        :param header_values:
            The value to assign to the header_values property of this ExtractLogHeaderDetails.
        :type header_values: list[str]

        """
        self.swagger_types = {
            'log_key': 'str',
            'header_values': 'list[str]'
        }

        self.attribute_map = {
            'log_key': 'logKey',
            'header_values': 'headerValues'
        }

        self._log_key = None
        self._header_values = None

    @property
    def log_key(self):
        """
        Gets the log_key of this ExtractLogHeaderDetails.
        key


        :return: The log_key of this ExtractLogHeaderDetails.
        :rtype: str
        """
        return self._log_key

    @log_key.setter
    def log_key(self, log_key):
        """
        Sets the log_key of this ExtractLogHeaderDetails.
        key


        :param log_key: The log_key of this ExtractLogHeaderDetails.
        :type: str
        """
        self._log_key = log_key

    @property
    def header_values(self):
        """
        Gets the header_values of this ExtractLogHeaderDetails.
        log header values


        :return: The header_values of this ExtractLogHeaderDetails.
        :rtype: list[str]
        """
        return self._header_values

    @header_values.setter
    def header_values(self, header_values):
        """
        Sets the header_values of this ExtractLogHeaderDetails.
        log header values


        :param header_values: The header_values of this ExtractLogHeaderDetails.
        :type: list[str]
        """
        self._header_values = header_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
