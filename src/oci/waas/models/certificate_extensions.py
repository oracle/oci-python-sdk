# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateExtensions(object):
    """
    CertificateExtensions model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateExtensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CertificateExtensions.
        :type name: str

        :param is_critical:
            The value to assign to the is_critical property of this CertificateExtensions.
        :type is_critical: bool

        :param value:
            The value to assign to the value property of this CertificateExtensions.
        :type value: str

        """
        self.swagger_types = {
            'name': 'str',
            'is_critical': 'bool',
            'value': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'is_critical': 'isCritical',
            'value': 'value'
        }

        self._name = None
        self._is_critical = None
        self._value = None

    @property
    def name(self):
        """
        Gets the name of this CertificateExtensions.
        The certificate extension name.


        :return: The name of this CertificateExtensions.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CertificateExtensions.
        The certificate extension name.


        :param name: The name of this CertificateExtensions.
        :type: str
        """
        self._name = name

    @property
    def is_critical(self):
        """
        Gets the is_critical of this CertificateExtensions.
        The critical flag of the extension. Critical extensions must be processed, non-critical extensions can be ignored.


        :return: The is_critical of this CertificateExtensions.
        :rtype: bool
        """
        return self._is_critical

    @is_critical.setter
    def is_critical(self, is_critical):
        """
        Sets the is_critical of this CertificateExtensions.
        The critical flag of the extension. Critical extensions must be processed, non-critical extensions can be ignored.


        :param is_critical: The is_critical of this CertificateExtensions.
        :type: bool
        """
        self._is_critical = is_critical

    @property
    def value(self):
        """
        Gets the value of this CertificateExtensions.
        The certificate extension value.


        :return: The value of this CertificateExtensions.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CertificateExtensions.
        The certificate extension value.


        :param value: The value of this CertificateExtensions.
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
