# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CpeDeviceConfigQuestion(object):
    """
    An individual question that the customer can answer about the CPE device.

    The customer provides answers to these questions in
    :func:`update_tunnel_cpe_device_config`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CpeDeviceConfigQuestion object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CpeDeviceConfigQuestion.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this CpeDeviceConfigQuestion.
        :type display_name: str

        :param explanation:
            The value to assign to the explanation property of this CpeDeviceConfigQuestion.
        :type explanation: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'explanation': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'explanation': 'explanation'
        }

        self._key = None
        self._display_name = None
        self._explanation = None

    @property
    def key(self):
        """
        Gets the key of this CpeDeviceConfigQuestion.
        A string that identifies the question.


        :return: The key of this CpeDeviceConfigQuestion.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CpeDeviceConfigQuestion.
        A string that identifies the question.


        :param key: The key of this CpeDeviceConfigQuestion.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this CpeDeviceConfigQuestion.
        A descriptive label for the question (for example, to display in a form in a graphical interface).


        :return: The display_name of this CpeDeviceConfigQuestion.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CpeDeviceConfigQuestion.
        A descriptive label for the question (for example, to display in a form in a graphical interface).


        :param display_name: The display_name of this CpeDeviceConfigQuestion.
        :type: str
        """
        self._display_name = display_name

    @property
    def explanation(self):
        """
        Gets the explanation of this CpeDeviceConfigQuestion.
        A description or explanation of the question, to help the customer answer accurately.


        :return: The explanation of this CpeDeviceConfigQuestion.
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """
        Sets the explanation of this CpeDeviceConfigQuestion.
        A description or explanation of the question, to help the customer answer accurately.


        :param explanation: The explanation of this CpeDeviceConfigQuestion.
        :type: str
        """
        self._explanation = explanation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
