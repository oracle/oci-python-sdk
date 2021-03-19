# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .eula import Eula
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TextBasedEula(Eula):
    """
    An EULA that is provided as text
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TextBasedEula object with values from keyword arguments. The default value of the :py:attr:`~oci.marketplace.models.TextBasedEula.eula_type` attribute
        of this class is ``TEXT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param eula_type:
            The value to assign to the eula_type property of this TextBasedEula.
            Allowed values for this property are: "TEXT"
        :type eula_type: str

        :param license_text:
            The value to assign to the license_text property of this TextBasedEula.
        :type license_text: str

        """
        self.swagger_types = {
            'eula_type': 'str',
            'license_text': 'str'
        }

        self.attribute_map = {
            'eula_type': 'eulaType',
            'license_text': 'licenseText'
        }

        self._eula_type = None
        self._license_text = None
        self._eula_type = 'TEXT'

    @property
    def license_text(self):
        """
        Gets the license_text of this TextBasedEula.
        text of the eula


        :return: The license_text of this TextBasedEula.
        :rtype: str
        """
        return self._license_text

    @license_text.setter
    def license_text(self, license_text):
        """
        Sets the license_text of this TextBasedEula.
        text of the eula


        :param license_text: The license_text of this TextBasedEula.
        :type: str
        """
        self._license_text = license_text

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
