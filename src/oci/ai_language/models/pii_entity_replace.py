# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001

from .pii_entity_masking import PiiEntityMasking
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PiiEntityReplace(PiiEntityMasking):
    """
    Replace PII entities with a given sequence of characters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PiiEntityReplace object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_language.models.PiiEntityReplace.mode` attribute
        of this class is ``REPLACE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mode:
            The value to assign to the mode property of this PiiEntityReplace.
            Allowed values for this property are: "REPLACE", "MASK", "REMOVE"
        :type mode: str

        :param exclude:
            The value to assign to the exclude property of this PiiEntityReplace.
        :type exclude: list[str]

        :param should_detect:
            The value to assign to the should_detect property of this PiiEntityReplace.
        :type should_detect: bool

        :param replace_with:
            The value to assign to the replace_with property of this PiiEntityReplace.
        :type replace_with: str

        """
        self.swagger_types = {
            'mode': 'str',
            'exclude': 'list[str]',
            'should_detect': 'bool',
            'replace_with': 'str'
        }
        self.attribute_map = {
            'mode': 'mode',
            'exclude': 'exclude',
            'should_detect': 'shouldDetect',
            'replace_with': 'replaceWith'
        }
        self._mode = None
        self._exclude = None
        self._should_detect = None
        self._replace_with = None
        self._mode = 'REPLACE'

    @property
    def replace_with(self):
        """
        Gets the replace_with of this PiiEntityReplace.
        Replace entities with given sequence of characters. By default PII entity will be replaced with <ENTITY_TYPE>.


        :return: The replace_with of this PiiEntityReplace.
        :rtype: str
        """
        return self._replace_with

    @replace_with.setter
    def replace_with(self, replace_with):
        """
        Sets the replace_with of this PiiEntityReplace.
        Replace entities with given sequence of characters. By default PII entity will be replaced with <ENTITY_TYPE>.


        :param replace_with: The replace_with of this PiiEntityReplace.
        :type: str
        """
        self._replace_with = replace_with

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
