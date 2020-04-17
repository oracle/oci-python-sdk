# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppCatalogListingResourceVersionAgreements(object):
    """
    Agreements for a listing resource version.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppCatalogListingResourceVersionAgreements object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param listing_id:
            The value to assign to the listing_id property of this AppCatalogListingResourceVersionAgreements.
        :type listing_id: str

        :param listing_resource_version:
            The value to assign to the listing_resource_version property of this AppCatalogListingResourceVersionAgreements.
        :type listing_resource_version: str

        :param oracle_terms_of_use_link:
            The value to assign to the oracle_terms_of_use_link property of this AppCatalogListingResourceVersionAgreements.
        :type oracle_terms_of_use_link: str

        :param eula_link:
            The value to assign to the eula_link property of this AppCatalogListingResourceVersionAgreements.
        :type eula_link: str

        :param time_retrieved:
            The value to assign to the time_retrieved property of this AppCatalogListingResourceVersionAgreements.
        :type time_retrieved: datetime

        :param signature:
            The value to assign to the signature property of this AppCatalogListingResourceVersionAgreements.
        :type signature: str

        """
        self.swagger_types = {
            'listing_id': 'str',
            'listing_resource_version': 'str',
            'oracle_terms_of_use_link': 'str',
            'eula_link': 'str',
            'time_retrieved': 'datetime',
            'signature': 'str'
        }

        self.attribute_map = {
            'listing_id': 'listingId',
            'listing_resource_version': 'listingResourceVersion',
            'oracle_terms_of_use_link': 'oracleTermsOfUseLink',
            'eula_link': 'eulaLink',
            'time_retrieved': 'timeRetrieved',
            'signature': 'signature'
        }

        self._listing_id = None
        self._listing_resource_version = None
        self._oracle_terms_of_use_link = None
        self._eula_link = None
        self._time_retrieved = None
        self._signature = None

    @property
    def listing_id(self):
        """
        Gets the listing_id of this AppCatalogListingResourceVersionAgreements.
        The OCID of the listing associated with these agreements.


        :return: The listing_id of this AppCatalogListingResourceVersionAgreements.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this AppCatalogListingResourceVersionAgreements.
        The OCID of the listing associated with these agreements.


        :param listing_id: The listing_id of this AppCatalogListingResourceVersionAgreements.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def listing_resource_version(self):
        """
        Gets the listing_resource_version of this AppCatalogListingResourceVersionAgreements.
        Listing resource version associated with these agreements.


        :return: The listing_resource_version of this AppCatalogListingResourceVersionAgreements.
        :rtype: str
        """
        return self._listing_resource_version

    @listing_resource_version.setter
    def listing_resource_version(self, listing_resource_version):
        """
        Sets the listing_resource_version of this AppCatalogListingResourceVersionAgreements.
        Listing resource version associated with these agreements.


        :param listing_resource_version: The listing_resource_version of this AppCatalogListingResourceVersionAgreements.
        :type: str
        """
        self._listing_resource_version = listing_resource_version

    @property
    def oracle_terms_of_use_link(self):
        """
        Gets the oracle_terms_of_use_link of this AppCatalogListingResourceVersionAgreements.
        Oracle TOU link


        :return: The oracle_terms_of_use_link of this AppCatalogListingResourceVersionAgreements.
        :rtype: str
        """
        return self._oracle_terms_of_use_link

    @oracle_terms_of_use_link.setter
    def oracle_terms_of_use_link(self, oracle_terms_of_use_link):
        """
        Sets the oracle_terms_of_use_link of this AppCatalogListingResourceVersionAgreements.
        Oracle TOU link


        :param oracle_terms_of_use_link: The oracle_terms_of_use_link of this AppCatalogListingResourceVersionAgreements.
        :type: str
        """
        self._oracle_terms_of_use_link = oracle_terms_of_use_link

    @property
    def eula_link(self):
        """
        Gets the eula_link of this AppCatalogListingResourceVersionAgreements.
        EULA link


        :return: The eula_link of this AppCatalogListingResourceVersionAgreements.
        :rtype: str
        """
        return self._eula_link

    @eula_link.setter
    def eula_link(self, eula_link):
        """
        Sets the eula_link of this AppCatalogListingResourceVersionAgreements.
        EULA link


        :param eula_link: The eula_link of this AppCatalogListingResourceVersionAgreements.
        :type: str
        """
        self._eula_link = eula_link

    @property
    def time_retrieved(self):
        """
        Gets the time_retrieved of this AppCatalogListingResourceVersionAgreements.
        Date and time the agreements were retrieved, in RFC3339 format.
        Example: `2018-03-20T12:32:53.532Z`


        :return: The time_retrieved of this AppCatalogListingResourceVersionAgreements.
        :rtype: datetime
        """
        return self._time_retrieved

    @time_retrieved.setter
    def time_retrieved(self, time_retrieved):
        """
        Sets the time_retrieved of this AppCatalogListingResourceVersionAgreements.
        Date and time the agreements were retrieved, in RFC3339 format.
        Example: `2018-03-20T12:32:53.532Z`


        :param time_retrieved: The time_retrieved of this AppCatalogListingResourceVersionAgreements.
        :type: datetime
        """
        self._time_retrieved = time_retrieved

    @property
    def signature(self):
        """
        Gets the signature of this AppCatalogListingResourceVersionAgreements.
        A generated signature for this agreement retrieval operation which should be used in the create subscription call.


        :return: The signature of this AppCatalogListingResourceVersionAgreements.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this AppCatalogListingResourceVersionAgreements.
        A generated signature for this agreement retrieval operation which should be used in the create subscription call.


        :param signature: The signature of this AppCatalogListingResourceVersionAgreements.
        :type: str
        """
        self._signature = signature

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
