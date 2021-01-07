# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAppCatalogSubscriptionDetails(object):
    """
    details for creating a subscription for a listing resource version.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAppCatalogSubscriptionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAppCatalogSubscriptionDetails.
        :type compartment_id: str

        :param listing_id:
            The value to assign to the listing_id property of this CreateAppCatalogSubscriptionDetails.
        :type listing_id: str

        :param listing_resource_version:
            The value to assign to the listing_resource_version property of this CreateAppCatalogSubscriptionDetails.
        :type listing_resource_version: str

        :param oracle_terms_of_use_link:
            The value to assign to the oracle_terms_of_use_link property of this CreateAppCatalogSubscriptionDetails.
        :type oracle_terms_of_use_link: str

        :param eula_link:
            The value to assign to the eula_link property of this CreateAppCatalogSubscriptionDetails.
        :type eula_link: str

        :param time_retrieved:
            The value to assign to the time_retrieved property of this CreateAppCatalogSubscriptionDetails.
        :type time_retrieved: datetime

        :param signature:
            The value to assign to the signature property of this CreateAppCatalogSubscriptionDetails.
        :type signature: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'listing_id': 'str',
            'listing_resource_version': 'str',
            'oracle_terms_of_use_link': 'str',
            'eula_link': 'str',
            'time_retrieved': 'datetime',
            'signature': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'listing_id': 'listingId',
            'listing_resource_version': 'listingResourceVersion',
            'oracle_terms_of_use_link': 'oracleTermsOfUseLink',
            'eula_link': 'eulaLink',
            'time_retrieved': 'timeRetrieved',
            'signature': 'signature'
        }

        self._compartment_id = None
        self._listing_id = None
        self._listing_resource_version = None
        self._oracle_terms_of_use_link = None
        self._eula_link = None
        self._time_retrieved = None
        self._signature = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAppCatalogSubscriptionDetails.
        The compartmentID for the subscription.


        :return: The compartment_id of this CreateAppCatalogSubscriptionDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAppCatalogSubscriptionDetails.
        The compartmentID for the subscription.


        :param compartment_id: The compartment_id of this CreateAppCatalogSubscriptionDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def listing_id(self):
        """
        **[Required]** Gets the listing_id of this CreateAppCatalogSubscriptionDetails.
        The OCID of the listing.


        :return: The listing_id of this CreateAppCatalogSubscriptionDetails.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this CreateAppCatalogSubscriptionDetails.
        The OCID of the listing.


        :param listing_id: The listing_id of this CreateAppCatalogSubscriptionDetails.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def listing_resource_version(self):
        """
        **[Required]** Gets the listing_resource_version of this CreateAppCatalogSubscriptionDetails.
        Listing resource version.


        :return: The listing_resource_version of this CreateAppCatalogSubscriptionDetails.
        :rtype: str
        """
        return self._listing_resource_version

    @listing_resource_version.setter
    def listing_resource_version(self, listing_resource_version):
        """
        Sets the listing_resource_version of this CreateAppCatalogSubscriptionDetails.
        Listing resource version.


        :param listing_resource_version: The listing_resource_version of this CreateAppCatalogSubscriptionDetails.
        :type: str
        """
        self._listing_resource_version = listing_resource_version

    @property
    def oracle_terms_of_use_link(self):
        """
        **[Required]** Gets the oracle_terms_of_use_link of this CreateAppCatalogSubscriptionDetails.
        Oracle TOU link


        :return: The oracle_terms_of_use_link of this CreateAppCatalogSubscriptionDetails.
        :rtype: str
        """
        return self._oracle_terms_of_use_link

    @oracle_terms_of_use_link.setter
    def oracle_terms_of_use_link(self, oracle_terms_of_use_link):
        """
        Sets the oracle_terms_of_use_link of this CreateAppCatalogSubscriptionDetails.
        Oracle TOU link


        :param oracle_terms_of_use_link: The oracle_terms_of_use_link of this CreateAppCatalogSubscriptionDetails.
        :type: str
        """
        self._oracle_terms_of_use_link = oracle_terms_of_use_link

    @property
    def eula_link(self):
        """
        Gets the eula_link of this CreateAppCatalogSubscriptionDetails.
        EULA link


        :return: The eula_link of this CreateAppCatalogSubscriptionDetails.
        :rtype: str
        """
        return self._eula_link

    @eula_link.setter
    def eula_link(self, eula_link):
        """
        Sets the eula_link of this CreateAppCatalogSubscriptionDetails.
        EULA link


        :param eula_link: The eula_link of this CreateAppCatalogSubscriptionDetails.
        :type: str
        """
        self._eula_link = eula_link

    @property
    def time_retrieved(self):
        """
        **[Required]** Gets the time_retrieved of this CreateAppCatalogSubscriptionDetails.
        Date and time the agreements were retrieved, in `RFC3339`__ format.
        Example: `2018-03-20T12:32:53.532Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_retrieved of this CreateAppCatalogSubscriptionDetails.
        :rtype: datetime
        """
        return self._time_retrieved

    @time_retrieved.setter
    def time_retrieved(self, time_retrieved):
        """
        Sets the time_retrieved of this CreateAppCatalogSubscriptionDetails.
        Date and time the agreements were retrieved, in `RFC3339`__ format.
        Example: `2018-03-20T12:32:53.532Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_retrieved: The time_retrieved of this CreateAppCatalogSubscriptionDetails.
        :type: datetime
        """
        self._time_retrieved = time_retrieved

    @property
    def signature(self):
        """
        **[Required]** Gets the signature of this CreateAppCatalogSubscriptionDetails.
        A generated signature for this listing resource version retrieved the agreements API.


        :return: The signature of this CreateAppCatalogSubscriptionDetails.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this CreateAppCatalogSubscriptionDetails.
        A generated signature for this listing resource version retrieved the agreements API.


        :param signature: The signature of this CreateAppCatalogSubscriptionDetails.
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
