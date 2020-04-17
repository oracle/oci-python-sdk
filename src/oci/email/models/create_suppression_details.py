# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSuppressionDetails(object):
    """
    The details needed for creating a single suppression.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSuppressionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSuppressionDetails.
        :type compartment_id: str

        :param email_address:
            The value to assign to the email_address property of this CreateSuppressionDetails.
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
        **[Required]** Gets the compartment_id of this CreateSuppressionDetails.
        The OCID of the compartment to contain the suppression. Since
        suppressions are at the customer level, this must be the tenancy
        OCID.


        :return: The compartment_id of this CreateSuppressionDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSuppressionDetails.
        The OCID of the compartment to contain the suppression. Since
        suppressions are at the customer level, this must be the tenancy
        OCID.


        :param compartment_id: The compartment_id of this CreateSuppressionDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def email_address(self):
        """
        **[Required]** Gets the email_address of this CreateSuppressionDetails.
        The recipient email address of the suppression.


        :return: The email_address of this CreateSuppressionDetails.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this CreateSuppressionDetails.
        The recipient email address of the suppression.


        :param email_address: The email_address of this CreateSuppressionDetails.
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
