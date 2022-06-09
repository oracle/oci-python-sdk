# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubscribedServiceBusinessPartner(object):
    """
    Business partner.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubscribedServiceBusinessPartner object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SubscribedServiceBusinessPartner.
        :type name: str

        :param name_phonetic:
            The value to assign to the name_phonetic property of this SubscribedServiceBusinessPartner.
        :type name_phonetic: str

        :param tca_cust_account_number:
            The value to assign to the tca_cust_account_number property of this SubscribedServiceBusinessPartner.
        :type tca_cust_account_number: str

        :param is_public_sector:
            The value to assign to the is_public_sector property of this SubscribedServiceBusinessPartner.
        :type is_public_sector: bool

        :param is_chain_customer:
            The value to assign to the is_chain_customer property of this SubscribedServiceBusinessPartner.
        :type is_chain_customer: bool

        :param customer_chain_type:
            The value to assign to the customer_chain_type property of this SubscribedServiceBusinessPartner.
        :type customer_chain_type: str

        :param tca_party_number:
            The value to assign to the tca_party_number property of this SubscribedServiceBusinessPartner.
        :type tca_party_number: str

        :param tca_party_id:
            The value to assign to the tca_party_id property of this SubscribedServiceBusinessPartner.
        :type tca_party_id: int

        :param tca_customer_account_id:
            The value to assign to the tca_customer_account_id property of this SubscribedServiceBusinessPartner.
        :type tca_customer_account_id: int

        """
        self.swagger_types = {
            'name': 'str',
            'name_phonetic': 'str',
            'tca_cust_account_number': 'str',
            'is_public_sector': 'bool',
            'is_chain_customer': 'bool',
            'customer_chain_type': 'str',
            'tca_party_number': 'str',
            'tca_party_id': 'int',
            'tca_customer_account_id': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'name_phonetic': 'namePhonetic',
            'tca_cust_account_number': 'tcaCustAccountNumber',
            'is_public_sector': 'isPublicSector',
            'is_chain_customer': 'isChainCustomer',
            'customer_chain_type': 'customerChainType',
            'tca_party_number': 'tcaPartyNumber',
            'tca_party_id': 'tcaPartyId',
            'tca_customer_account_id': 'tcaCustomerAccountId'
        }

        self._name = None
        self._name_phonetic = None
        self._tca_cust_account_number = None
        self._is_public_sector = None
        self._is_chain_customer = None
        self._customer_chain_type = None
        self._tca_party_number = None
        self._tca_party_id = None
        self._tca_customer_account_id = None

    @property
    def name(self):
        """
        Gets the name of this SubscribedServiceBusinessPartner.
        Commercial name also called customer name.


        :return: The name of this SubscribedServiceBusinessPartner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SubscribedServiceBusinessPartner.
        Commercial name also called customer name.


        :param name: The name of this SubscribedServiceBusinessPartner.
        :type: str
        """
        self._name = name

    @property
    def name_phonetic(self):
        """
        Gets the name_phonetic of this SubscribedServiceBusinessPartner.
        Phonetic name.


        :return: The name_phonetic of this SubscribedServiceBusinessPartner.
        :rtype: str
        """
        return self._name_phonetic

    @name_phonetic.setter
    def name_phonetic(self, name_phonetic):
        """
        Sets the name_phonetic of this SubscribedServiceBusinessPartner.
        Phonetic name.


        :param name_phonetic: The name_phonetic of this SubscribedServiceBusinessPartner.
        :type: str
        """
        self._name_phonetic = name_phonetic

    @property
    def tca_cust_account_number(self):
        """
        Gets the tca_cust_account_number of this SubscribedServiceBusinessPartner.
        TCA customer account number.


        :return: The tca_cust_account_number of this SubscribedServiceBusinessPartner.
        :rtype: str
        """
        return self._tca_cust_account_number

    @tca_cust_account_number.setter
    def tca_cust_account_number(self, tca_cust_account_number):
        """
        Sets the tca_cust_account_number of this SubscribedServiceBusinessPartner.
        TCA customer account number.


        :param tca_cust_account_number: The tca_cust_account_number of this SubscribedServiceBusinessPartner.
        :type: str
        """
        self._tca_cust_account_number = tca_cust_account_number

    @property
    def is_public_sector(self):
        """
        Gets the is_public_sector of this SubscribedServiceBusinessPartner.
        The business partner is part of the public sector or not.


        :return: The is_public_sector of this SubscribedServiceBusinessPartner.
        :rtype: bool
        """
        return self._is_public_sector

    @is_public_sector.setter
    def is_public_sector(self, is_public_sector):
        """
        Sets the is_public_sector of this SubscribedServiceBusinessPartner.
        The business partner is part of the public sector or not.


        :param is_public_sector: The is_public_sector of this SubscribedServiceBusinessPartner.
        :type: bool
        """
        self._is_public_sector = is_public_sector

    @property
    def is_chain_customer(self):
        """
        Gets the is_chain_customer of this SubscribedServiceBusinessPartner.
        The business partner is chain customer or not.


        :return: The is_chain_customer of this SubscribedServiceBusinessPartner.
        :rtype: bool
        """
        return self._is_chain_customer

    @is_chain_customer.setter
    def is_chain_customer(self, is_chain_customer):
        """
        Sets the is_chain_customer of this SubscribedServiceBusinessPartner.
        The business partner is chain customer or not.


        :param is_chain_customer: The is_chain_customer of this SubscribedServiceBusinessPartner.
        :type: bool
        """
        self._is_chain_customer = is_chain_customer

    @property
    def customer_chain_type(self):
        """
        Gets the customer_chain_type of this SubscribedServiceBusinessPartner.
        Customer chain type.


        :return: The customer_chain_type of this SubscribedServiceBusinessPartner.
        :rtype: str
        """
        return self._customer_chain_type

    @customer_chain_type.setter
    def customer_chain_type(self, customer_chain_type):
        """
        Sets the customer_chain_type of this SubscribedServiceBusinessPartner.
        Customer chain type.


        :param customer_chain_type: The customer_chain_type of this SubscribedServiceBusinessPartner.
        :type: str
        """
        self._customer_chain_type = customer_chain_type

    @property
    def tca_party_number(self):
        """
        Gets the tca_party_number of this SubscribedServiceBusinessPartner.
        TCA party number.


        :return: The tca_party_number of this SubscribedServiceBusinessPartner.
        :rtype: str
        """
        return self._tca_party_number

    @tca_party_number.setter
    def tca_party_number(self, tca_party_number):
        """
        Sets the tca_party_number of this SubscribedServiceBusinessPartner.
        TCA party number.


        :param tca_party_number: The tca_party_number of this SubscribedServiceBusinessPartner.
        :type: str
        """
        self._tca_party_number = tca_party_number

    @property
    def tca_party_id(self):
        """
        Gets the tca_party_id of this SubscribedServiceBusinessPartner.
        TCA party ID.


        :return: The tca_party_id of this SubscribedServiceBusinessPartner.
        :rtype: int
        """
        return self._tca_party_id

    @tca_party_id.setter
    def tca_party_id(self, tca_party_id):
        """
        Sets the tca_party_id of this SubscribedServiceBusinessPartner.
        TCA party ID.


        :param tca_party_id: The tca_party_id of this SubscribedServiceBusinessPartner.
        :type: int
        """
        self._tca_party_id = tca_party_id

    @property
    def tca_customer_account_id(self):
        """
        Gets the tca_customer_account_id of this SubscribedServiceBusinessPartner.
        TCA customer account ID.


        :return: The tca_customer_account_id of this SubscribedServiceBusinessPartner.
        :rtype: int
        """
        return self._tca_customer_account_id

    @tca_customer_account_id.setter
    def tca_customer_account_id(self, tca_customer_account_id):
        """
        Sets the tca_customer_account_id of this SubscribedServiceBusinessPartner.
        TCA customer account ID.


        :param tca_customer_account_id: The tca_customer_account_id of this SubscribedServiceBusinessPartner.
        :type: int
        """
        self._tca_customer_account_id = tca_customer_account_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
