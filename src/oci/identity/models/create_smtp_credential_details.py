# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSmtpCredentialDetails(object):
    """
    CreateSmtpCredentialDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSmtpCredentialDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateSmtpCredentialDetails.
        :type description: str

        """
        self.swagger_types = {
            'description': 'str'
        }

        self.attribute_map = {
            'description': 'description'
        }

        self._description = None

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CreateSmtpCredentialDetails.
        The description you assign to the SMTP credentials during creation. Does not have to be unique, and it's changeable.


        :return: The description of this CreateSmtpCredentialDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateSmtpCredentialDetails.
        The description you assign to the SMTP credentials during creation. Does not have to be unique, and it's changeable.


        :param description: The description of this CreateSmtpCredentialDetails.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
