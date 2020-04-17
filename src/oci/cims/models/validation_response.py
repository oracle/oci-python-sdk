# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidationResponse(object):
    """
    Validation Response
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValidationResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_valid_user:
            The value to assign to the is_valid_user property of this ValidationResponse.
        :type is_valid_user: bool

        """
        self.swagger_types = {
            'is_valid_user': 'bool'
        }

        self.attribute_map = {
            'is_valid_user': 'isValidUser'
        }

        self._is_valid_user = None

    @property
    def is_valid_user(self):
        """
        Gets the is_valid_user of this ValidationResponse.
        Boolean value to check whether requested user is valid or not


        :return: The is_valid_user of this ValidationResponse.
        :rtype: bool
        """
        return self._is_valid_user

    @is_valid_user.setter
    def is_valid_user(self, is_valid_user):
        """
        Sets the is_valid_user of this ValidationResponse.
        Boolean value to check whether requested user is valid or not


        :param is_valid_user: The is_valid_user of this ValidationResponse.
        :type: bool
        """
        self._is_valid_user = is_valid_user

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
