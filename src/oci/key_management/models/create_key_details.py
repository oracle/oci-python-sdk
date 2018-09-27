# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateKeyDetails(object):
    """
    CreateKeyDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateKeyDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateKeyDetails.
        :type display_name: str

        :param key_shape:
            The value to assign to the key_shape property of this CreateKeyDetails.
        :type key_shape: KeyShape

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'key_shape': 'KeyShape'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'key_shape': 'keyShape'
        }

        self._compartment_id = None
        self._display_name = None
        self._key_shape = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateKeyDetails.
        The OCID of the compartment that contains this key.


        :return: The compartment_id of this CreateKeyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateKeyDetails.
        The OCID of the compartment that contains this key.


        :param compartment_id: The compartment_id of this CreateKeyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateKeyDetails.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateKeyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateKeyDetails.
        A user-friendly name for the key. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateKeyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def key_shape(self):
        """
        **[Required]** Gets the key_shape of this CreateKeyDetails.

        :return: The key_shape of this CreateKeyDetails.
        :rtype: KeyShape
        """
        return self._key_shape

    @key_shape.setter
    def key_shape(self, key_shape):
        """
        Sets the key_shape of this CreateKeyDetails.

        :param key_shape: The key_shape of this CreateKeyDetails.
        :type: KeyShape
        """
        self._key_shape = key_shape

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
