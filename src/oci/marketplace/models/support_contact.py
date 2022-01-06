# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SupportContact(object):
    """
    Contact information to use to get support.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SupportContact object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SupportContact.
        :type name: str

        :param phone:
            The value to assign to the phone property of this SupportContact.
        :type phone: str

        :param email:
            The value to assign to the email property of this SupportContact.
        :type email: str

        :param subject:
            The value to assign to the subject property of this SupportContact.
        :type subject: str

        """
        self.swagger_types = {
            'name': 'str',
            'phone': 'str',
            'email': 'str',
            'subject': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'phone': 'phone',
            'email': 'email',
            'subject': 'subject'
        }

        self._name = None
        self._phone = None
        self._email = None
        self._subject = None

    @property
    def name(self):
        """
        Gets the name of this SupportContact.
        The name of the contact.


        :return: The name of this SupportContact.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SupportContact.
        The name of the contact.


        :param name: The name of this SupportContact.
        :type: str
        """
        self._name = name

    @property
    def phone(self):
        """
        Gets the phone of this SupportContact.
        The phone number of the contact.


        :return: The phone of this SupportContact.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this SupportContact.
        The phone number of the contact.


        :param phone: The phone of this SupportContact.
        :type: str
        """
        self._phone = phone

    @property
    def email(self):
        """
        Gets the email of this SupportContact.
        The email of the contact.


        :return: The email of this SupportContact.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this SupportContact.
        The email of the contact.


        :param email: The email of this SupportContact.
        :type: str
        """
        self._email = email

    @property
    def subject(self):
        """
        Gets the subject of this SupportContact.
        The email subject line to use when contacting support.


        :return: The subject of this SupportContact.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this SupportContact.
        The email subject line to use when contacting support.


        :param subject: The subject of this SupportContact.
        :type: str
        """
        self._subject = subject

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
