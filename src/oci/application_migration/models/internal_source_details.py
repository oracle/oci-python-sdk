# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from .source_details import SourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InternalSourceDetails(SourceDetails):
    """
    Specifies configuration specific to the source environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InternalSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.application_migration.models.InternalSourceDetails.type` attribute
        of this class is ``INTERNAL_COMPUTE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this InternalSourceDetails.
            Allowed values for this property are: "OCIC", "INTERNAL_COMPUTE"
        :type type: str

        :param account_name:
            The value to assign to the account_name property of this InternalSourceDetails.
        :type account_name: str

        """
        self.swagger_types = {
            'type': 'str',
            'account_name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'account_name': 'accountName'
        }

        self._type = None
        self._account_name = None
        self._type = 'INTERNAL_COMPUTE'

    @property
    def account_name(self):
        """
        **[Required]** Gets the account_name of this InternalSourceDetails.
        The tradition cloud account name


        :return: The account_name of this InternalSourceDetails.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """
        Sets the account_name of this InternalSourceDetails.
        The tradition cloud account name


        :param account_name: The account_name of this InternalSourceDetails.
        :type: str
        """
        self._account_name = account_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
