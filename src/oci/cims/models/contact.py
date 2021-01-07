# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Contact(object):
    """
    Contact details for the customer.
    """

    #: A constant which can be used with the contact_type property of a Contact.
    #: This constant has a value of "PRIMARY"
    CONTACT_TYPE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the contact_type property of a Contact.
    #: This constant has a value of "ALTERNATE"
    CONTACT_TYPE_ALTERNATE = "ALTERNATE"

    #: A constant which can be used with the contact_type property of a Contact.
    #: This constant has a value of "SECONDARY"
    CONTACT_TYPE_SECONDARY = "SECONDARY"

    #: A constant which can be used with the contact_type property of a Contact.
    #: This constant has a value of "ADMIN"
    CONTACT_TYPE_ADMIN = "ADMIN"

    #: A constant which can be used with the contact_type property of a Contact.
    #: This constant has a value of "MANAGER"
    CONTACT_TYPE_MANAGER = "MANAGER"

    def __init__(self, **kwargs):
        """
        Initializes a new Contact object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param contact_name:
            The value to assign to the contact_name property of this Contact.
        :type contact_name: str

        :param contact_email:
            The value to assign to the contact_email property of this Contact.
        :type contact_email: str

        :param contact_phone:
            The value to assign to the contact_phone property of this Contact.
        :type contact_phone: str

        :param contact_type:
            The value to assign to the contact_type property of this Contact.
            Allowed values for this property are: "PRIMARY", "ALTERNATE", "SECONDARY", "ADMIN", "MANAGER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type contact_type: str

        """
        self.swagger_types = {
            'contact_name': 'str',
            'contact_email': 'str',
            'contact_phone': 'str',
            'contact_type': 'str'
        }

        self.attribute_map = {
            'contact_name': 'contactName',
            'contact_email': 'contactEmail',
            'contact_phone': 'contactPhone',
            'contact_type': 'contactType'
        }

        self._contact_name = None
        self._contact_email = None
        self._contact_phone = None
        self._contact_type = None

    @property
    def contact_name(self):
        """
        Gets the contact_name of this Contact.
        The name of the contact person.


        :return: The contact_name of this Contact.
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """
        Sets the contact_name of this Contact.
        The name of the contact person.


        :param contact_name: The contact_name of this Contact.
        :type: str
        """
        self._contact_name = contact_name

    @property
    def contact_email(self):
        """
        Gets the contact_email of this Contact.
        The email of the contact person.


        :return: The contact_email of this Contact.
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """
        Sets the contact_email of this Contact.
        The email of the contact person.


        :param contact_email: The contact_email of this Contact.
        :type: str
        """
        self._contact_email = contact_email

    @property
    def contact_phone(self):
        """
        Gets the contact_phone of this Contact.
        The phone number of the contact person.


        :return: The contact_phone of this Contact.
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """
        Sets the contact_phone of this Contact.
        The phone number of the contact person.


        :param contact_phone: The contact_phone of this Contact.
        :type: str
        """
        self._contact_phone = contact_phone

    @property
    def contact_type(self):
        """
        Gets the contact_type of this Contact.
        The type of contact, such as primary or alternate.

        Allowed values for this property are: "PRIMARY", "ALTERNATE", "SECONDARY", "ADMIN", "MANAGER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The contact_type of this Contact.
        :rtype: str
        """
        return self._contact_type

    @contact_type.setter
    def contact_type(self, contact_type):
        """
        Sets the contact_type of this Contact.
        The type of contact, such as primary or alternate.


        :param contact_type: The contact_type of this Contact.
        :type: str
        """
        allowed_values = ["PRIMARY", "ALTERNATE", "SECONDARY", "ADMIN", "MANAGER"]
        if not value_allowed_none_or_none_sentinel(contact_type, allowed_values):
            contact_type = 'UNKNOWN_ENUM_VALUE'
        self._contact_type = contact_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
