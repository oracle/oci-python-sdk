# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InvoicingAddress(object):
    """
    Address.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InvoicingAddress object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param location:
            The value to assign to the location property of this InvoicingAddress.
        :type location: oci.onesubscription.models.InvoicingLocation

        :param name:
            The value to assign to the name property of this InvoicingAddress.
        :type name: str

        :param phone:
            The value to assign to the phone property of this InvoicingAddress.
        :type phone: str

        :param is_bill_to:
            The value to assign to the is_bill_to property of this InvoicingAddress.
        :type is_bill_to: bool

        :param is_ship_to:
            The value to assign to the is_ship_to property of this InvoicingAddress.
        :type is_ship_to: bool

        :param bill_site_use_id:
            The value to assign to the bill_site_use_id property of this InvoicingAddress.
        :type bill_site_use_id: int

        :param service2_site_use_id:
            The value to assign to the service2_site_use_id property of this InvoicingAddress.
        :type service2_site_use_id: int

        :param tca_cust_acct_site_id:
            The value to assign to the tca_cust_acct_site_id property of this InvoicingAddress.
        :type tca_cust_acct_site_id: int

        :param tca_party_site_number:
            The value to assign to the tca_party_site_number property of this InvoicingAddress.
        :type tca_party_site_number: str

        """
        self.swagger_types = {
            'location': 'InvoicingLocation',
            'name': 'str',
            'phone': 'str',
            'is_bill_to': 'bool',
            'is_ship_to': 'bool',
            'bill_site_use_id': 'int',
            'service2_site_use_id': 'int',
            'tca_cust_acct_site_id': 'int',
            'tca_party_site_number': 'str'
        }

        self.attribute_map = {
            'location': 'location',
            'name': 'name',
            'phone': 'phone',
            'is_bill_to': 'isBillTo',
            'is_ship_to': 'isShipTo',
            'bill_site_use_id': 'billSiteUseId',
            'service2_site_use_id': 'service2SiteUseId',
            'tca_cust_acct_site_id': 'tcaCustAcctSiteId',
            'tca_party_site_number': 'tcaPartySiteNumber'
        }

        self._location = None
        self._name = None
        self._phone = None
        self._is_bill_to = None
        self._is_ship_to = None
        self._bill_site_use_id = None
        self._service2_site_use_id = None
        self._tca_cust_acct_site_id = None
        self._tca_party_site_number = None

    @property
    def location(self):
        """
        Gets the location of this InvoicingAddress.

        :return: The location of this InvoicingAddress.
        :rtype: oci.onesubscription.models.InvoicingLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this InvoicingAddress.

        :param location: The location of this InvoicingAddress.
        :type: oci.onesubscription.models.InvoicingLocation
        """
        self._location = location

    @property
    def name(self):
        """
        Gets the name of this InvoicingAddress.
        Address name identifier.


        :return: The name of this InvoicingAddress.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InvoicingAddress.
        Address name identifier.


        :param name: The name of this InvoicingAddress.
        :type: str
        """
        self._name = name

    @property
    def phone(self):
        """
        Gets the phone of this InvoicingAddress.
        Phone.


        :return: The phone of this InvoicingAddress.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this InvoicingAddress.
        Phone.


        :param phone: The phone of this InvoicingAddress.
        :type: str
        """
        self._phone = phone

    @property
    def is_bill_to(self):
        """
        Gets the is_bill_to of this InvoicingAddress.
        Identify as the customer's billing address.


        :return: The is_bill_to of this InvoicingAddress.
        :rtype: bool
        """
        return self._is_bill_to

    @is_bill_to.setter
    def is_bill_to(self, is_bill_to):
        """
        Sets the is_bill_to of this InvoicingAddress.
        Identify as the customer's billing address.


        :param is_bill_to: The is_bill_to of this InvoicingAddress.
        :type: bool
        """
        self._is_bill_to = is_bill_to

    @property
    def is_ship_to(self):
        """
        Gets the is_ship_to of this InvoicingAddress.
        Identify as the customer's shipping address.


        :return: The is_ship_to of this InvoicingAddress.
        :rtype: bool
        """
        return self._is_ship_to

    @is_ship_to.setter
    def is_ship_to(self, is_ship_to):
        """
        Sets the is_ship_to of this InvoicingAddress.
        Identify as the customer's shipping address.


        :param is_ship_to: The is_ship_to of this InvoicingAddress.
        :type: bool
        """
        self._is_ship_to = is_ship_to

    @property
    def bill_site_use_id(self):
        """
        Gets the bill_site_use_id of this InvoicingAddress.
        Bill to site use Id.


        :return: The bill_site_use_id of this InvoicingAddress.
        :rtype: int
        """
        return self._bill_site_use_id

    @bill_site_use_id.setter
    def bill_site_use_id(self, bill_site_use_id):
        """
        Sets the bill_site_use_id of this InvoicingAddress.
        Bill to site use Id.


        :param bill_site_use_id: The bill_site_use_id of this InvoicingAddress.
        :type: int
        """
        self._bill_site_use_id = bill_site_use_id

    @property
    def service2_site_use_id(self):
        """
        Gets the service2_site_use_id of this InvoicingAddress.
        Service to site use Id.


        :return: The service2_site_use_id of this InvoicingAddress.
        :rtype: int
        """
        return self._service2_site_use_id

    @service2_site_use_id.setter
    def service2_site_use_id(self, service2_site_use_id):
        """
        Sets the service2_site_use_id of this InvoicingAddress.
        Service to site use Id.


        :param service2_site_use_id: The service2_site_use_id of this InvoicingAddress.
        :type: int
        """
        self._service2_site_use_id = service2_site_use_id

    @property
    def tca_cust_acct_site_id(self):
        """
        Gets the tca_cust_acct_site_id of this InvoicingAddress.
        TCA customer account site Id.


        :return: The tca_cust_acct_site_id of this InvoicingAddress.
        :rtype: int
        """
        return self._tca_cust_acct_site_id

    @tca_cust_acct_site_id.setter
    def tca_cust_acct_site_id(self, tca_cust_acct_site_id):
        """
        Sets the tca_cust_acct_site_id of this InvoicingAddress.
        TCA customer account site Id.


        :param tca_cust_acct_site_id: The tca_cust_acct_site_id of this InvoicingAddress.
        :type: int
        """
        self._tca_cust_acct_site_id = tca_cust_acct_site_id

    @property
    def tca_party_site_number(self):
        """
        Gets the tca_party_site_number of this InvoicingAddress.
        Party site number.


        :return: The tca_party_site_number of this InvoicingAddress.
        :rtype: str
        """
        return self._tca_party_site_number

    @tca_party_site_number.setter
    def tca_party_site_number(self, tca_party_site_number):
        """
        Sets the tca_party_site_number of this InvoicingAddress.
        Party site number.


        :param tca_party_site_number: The tca_party_site_number of this InvoicingAddress.
        :type: str
        """
        self._tca_party_site_number = tca_party_site_number

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other