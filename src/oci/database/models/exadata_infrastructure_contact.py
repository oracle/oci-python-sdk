# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataInfrastructureContact(object):
    """
    Contact details for Exadata Infrastructure.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataInfrastructureContact object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ExadataInfrastructureContact.
        :type name: str

        :param phone_number:
            The value to assign to the phone_number property of this ExadataInfrastructureContact.
        :type phone_number: str

        :param email:
            The value to assign to the email property of this ExadataInfrastructureContact.
        :type email: str

        :param is_primary:
            The value to assign to the is_primary property of this ExadataInfrastructureContact.
        :type is_primary: bool

        :param is_contact_mos_validated:
            The value to assign to the is_contact_mos_validated property of this ExadataInfrastructureContact.
        :type is_contact_mos_validated: bool

        """
        self.swagger_types = {
            'name': 'str',
            'phone_number': 'str',
            'email': 'str',
            'is_primary': 'bool',
            'is_contact_mos_validated': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'phone_number': 'phoneNumber',
            'email': 'email',
            'is_primary': 'isPrimary',
            'is_contact_mos_validated': 'isContactMosValidated'
        }

        self._name = None
        self._phone_number = None
        self._email = None
        self._is_primary = None
        self._is_contact_mos_validated = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ExadataInfrastructureContact.
        The name of the Exadata Infrastructure contact.


        :return: The name of this ExadataInfrastructureContact.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExadataInfrastructureContact.
        The name of the Exadata Infrastructure contact.


        :param name: The name of this ExadataInfrastructureContact.
        :type: str
        """
        self._name = name

    @property
    def phone_number(self):
        """
        Gets the phone_number of this ExadataInfrastructureContact.
        The phone number for the Exadata Infrastructure contact.


        :return: The phone_number of this ExadataInfrastructureContact.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this ExadataInfrastructureContact.
        The phone number for the Exadata Infrastructure contact.


        :param phone_number: The phone_number of this ExadataInfrastructureContact.
        :type: str
        """
        self._phone_number = phone_number

    @property
    def email(self):
        """
        **[Required]** Gets the email of this ExadataInfrastructureContact.
        The email for the Exadata Infrastructure contact.


        :return: The email of this ExadataInfrastructureContact.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ExadataInfrastructureContact.
        The email for the Exadata Infrastructure contact.


        :param email: The email of this ExadataInfrastructureContact.
        :type: str
        """
        self._email = email

    @property
    def is_primary(self):
        """
        **[Required]** Gets the is_primary of this ExadataInfrastructureContact.
        If `true`, this Exadata Infrastructure contact is a primary contact. If `false`, this Exadata Infrastructure is a secondary contact.


        :return: The is_primary of this ExadataInfrastructureContact.
        :rtype: bool
        """
        return self._is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        """
        Sets the is_primary of this ExadataInfrastructureContact.
        If `true`, this Exadata Infrastructure contact is a primary contact. If `false`, this Exadata Infrastructure is a secondary contact.


        :param is_primary: The is_primary of this ExadataInfrastructureContact.
        :type: bool
        """
        self._is_primary = is_primary

    @property
    def is_contact_mos_validated(self):
        """
        Gets the is_contact_mos_validated of this ExadataInfrastructureContact.
        If `true`, this Exadata Infrastructure contact is a valid My Oracle Support (MOS) contact. If `false`, this Exadata Infrastructure contact is not a valid MOS contact.


        :return: The is_contact_mos_validated of this ExadataInfrastructureContact.
        :rtype: bool
        """
        return self._is_contact_mos_validated

    @is_contact_mos_validated.setter
    def is_contact_mos_validated(self, is_contact_mos_validated):
        """
        Sets the is_contact_mos_validated of this ExadataInfrastructureContact.
        If `true`, this Exadata Infrastructure contact is a valid My Oracle Support (MOS) contact. If `false`, this Exadata Infrastructure contact is not a valid MOS contact.


        :param is_contact_mos_validated: The is_contact_mos_validated of this ExadataInfrastructureContact.
        :type: bool
        """
        self._is_contact_mos_validated = is_contact_mos_validated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
