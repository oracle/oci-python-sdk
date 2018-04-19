# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSenderDetails(object):
    """
    The details needed for creating a sender.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSenderDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSenderDetails.
        :type compartment_id: str

        :param email_address:
            The value to assign to the email_address property of this CreateSenderDetails.
        :type email_address: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'email_address': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'email_address': 'emailAddress'
        }

        self._compartment_id = None
        self._email_address = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateSenderDetails.
        The OCID of the compartment that contains the sender.


        :return: The compartment_id of this CreateSenderDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSenderDetails.
        The OCID of the compartment that contains the sender.


        :param compartment_id: The compartment_id of this CreateSenderDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def email_address(self):
        """
        Gets the email_address of this CreateSenderDetails.
        The email address of the sender.


        :return: The email_address of this CreateSenderDetails.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this CreateSenderDetails.
        The email address of the sender.


        :param email_address: The email_address of this CreateSenderDetails.
        :type: str
        """
        self._email_address = email_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
