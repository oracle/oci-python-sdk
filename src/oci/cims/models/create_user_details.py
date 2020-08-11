# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateUserDetails(object):
    """
    Details about creation of user.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateUserDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateUserDetails.
        :type compartment_id: str

        :param first_name:
            The value to assign to the first_name property of this CreateUserDetails.
        :type first_name: str

        :param last_name:
            The value to assign to the last_name property of this CreateUserDetails.
        :type last_name: str

        :param country:
            The value to assign to the country property of this CreateUserDetails.
        :type country: str

        :param csi:
            The value to assign to the csi property of this CreateUserDetails.
        :type csi: str

        :param phone:
            The value to assign to the phone property of this CreateUserDetails.
        :type phone: str

        :param timezone:
            The value to assign to the timezone property of this CreateUserDetails.
        :type timezone: str

        :param organization_name:
            The value to assign to the organization_name property of this CreateUserDetails.
        :type organization_name: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'country': 'str',
            'csi': 'str',
            'phone': 'str',
            'timezone': 'str',
            'organization_name': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'country': 'country',
            'csi': 'csi',
            'phone': 'phone',
            'timezone': 'timezone',
            'organization_name': 'organizationName'
        }

        self._compartment_id = None
        self._first_name = None
        self._last_name = None
        self._country = None
        self._csi = None
        self._phone = None
        self._timezone = None
        self._organization_name = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateUserDetails.
        The OCID of the tenancy.


        :return: The compartment_id of this CreateUserDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateUserDetails.
        The OCID of the tenancy.


        :param compartment_id: The compartment_id of this CreateUserDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def first_name(self):
        """
        **[Required]** Gets the first_name of this CreateUserDetails.
        First name of the user.


        :return: The first_name of this CreateUserDetails.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this CreateUserDetails.
        First name of the user.


        :param first_name: The first_name of this CreateUserDetails.
        :type: str
        """
        self._first_name = first_name

    @property
    def last_name(self):
        """
        **[Required]** Gets the last_name of this CreateUserDetails.
        Last name of the user.


        :return: The last_name of this CreateUserDetails.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this CreateUserDetails.
        Last name of the user.


        :param last_name: The last_name of this CreateUserDetails.
        :type: str
        """
        self._last_name = last_name

    @property
    def country(self):
        """
        **[Required]** Gets the country of this CreateUserDetails.
        Country of the user.


        :return: The country of this CreateUserDetails.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this CreateUserDetails.
        Country of the user.


        :param country: The country of this CreateUserDetails.
        :type: str
        """
        self._country = country

    @property
    def csi(self):
        """
        **[Required]** Gets the csi of this CreateUserDetails.
        CSI to be associated to the user.


        :return: The csi of this CreateUserDetails.
        :rtype: str
        """
        return self._csi

    @csi.setter
    def csi(self, csi):
        """
        Sets the csi of this CreateUserDetails.
        CSI to be associated to the user.


        :param csi: The csi of this CreateUserDetails.
        :type: str
        """
        self._csi = csi

    @property
    def phone(self):
        """
        **[Required]** Gets the phone of this CreateUserDetails.
        Contact number of the user.


        :return: The phone of this CreateUserDetails.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this CreateUserDetails.
        Contact number of the user.


        :param phone: The phone of this CreateUserDetails.
        :type: str
        """
        self._phone = phone

    @property
    def timezone(self):
        """
        **[Required]** Gets the timezone of this CreateUserDetails.
        Timezone of the user.


        :return: The timezone of this CreateUserDetails.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this CreateUserDetails.
        Timezone of the user.


        :param timezone: The timezone of this CreateUserDetails.
        :type: str
        """
        self._timezone = timezone

    @property
    def organization_name(self):
        """
        **[Required]** Gets the organization_name of this CreateUserDetails.
        Organization of the user.


        :return: The organization_name of this CreateUserDetails.
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """
        Sets the organization_name of this CreateUserDetails.
        Organization of the user.


        :param organization_name: The organization_name of this CreateUserDetails.
        :type: str
        """
        self._organization_name = organization_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
