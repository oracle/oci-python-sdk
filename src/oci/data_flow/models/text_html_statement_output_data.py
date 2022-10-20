# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .statement_output_data import StatementOutputData
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TextHtmlStatementOutputData(StatementOutputData):
    """
    The statement output data in html format.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TextHtmlStatementOutputData object with values from keyword arguments. The default value of the :py:attr:`~oci.data_flow.models.TextHtmlStatementOutputData.type` attribute
        of this class is ``TEXT_HTML`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TextHtmlStatementOutputData.
            Allowed values for this property are: "TEXT_PLAIN", "TEXT_HTML", "IMAGE_PNG"
        :type type: str

        :param value:
            The value to assign to the value property of this TextHtmlStatementOutputData.
        :type value: str

        """
        self.swagger_types = {
            'type': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'value': 'value'
        }

        self._type = None
        self._value = None
        self._type = 'TEXT_HTML'

    @property
    def value(self):
        """
        **[Required]** Gets the value of this TextHtmlStatementOutputData.
        The statement code execution output in html format.


        :return: The value of this TextHtmlStatementOutputData.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this TextHtmlStatementOutputData.
        The statement code execution output in html format.


        :param value: The value of this TextHtmlStatementOutputData.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
