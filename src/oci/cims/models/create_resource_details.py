# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateResourceDetails(object):
    """
    Details of Ticket Item
    """

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "DEV"
    REGION_DEV = "DEV"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "SEA"
    REGION_SEA = "SEA"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "INTEG_NEXT"
    REGION_INTEG_NEXT = "INTEG_NEXT"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "INTEG_STABLE"
    REGION_INTEG_STABLE = "INTEG_STABLE"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "PHX"
    REGION_PHX = "PHX"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "IAD"
    REGION_IAD = "IAD"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "FRA"
    REGION_FRA = "FRA"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "EU_FRANKFURT_1"
    REGION_EU_FRANKFURT_1 = "EU_FRANKFURT_1"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "LHR"
    REGION_LHR = "LHR"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "YYZ"
    REGION_YYZ = "YYZ"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "NRT"
    REGION_NRT = "NRT"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "US_LANGLEY_1"
    REGION_US_LANGLEY_1 = "US_LANGLEY_1"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "US_LUKE_1"
    REGION_US_LUKE_1 = "US_LUKE_1"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "ICN"
    REGION_ICN = "ICN"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "BOM"
    REGION_BOM = "BOM"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "GRU"
    REGION_GRU = "GRU"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "US_GOV_ASHBURN_1"
    REGION_US_GOV_ASHBURN_1 = "US_GOV_ASHBURN_1"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "US_GOV_PHOENIX_1"
    REGION_US_GOV_PHOENIX_1 = "US_GOV_PHOENIX_1"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "US_GOV_CHICAGO_1"
    REGION_US_GOV_CHICAGO_1 = "US_GOV_CHICAGO_1"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "SYD"
    REGION_SYD = "SYD"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "ZRH"
    REGION_ZRH = "ZRH"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "JED"
    REGION_JED = "JED"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "AMS"
    REGION_AMS = "AMS"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "KIX"
    REGION_KIX = "KIX"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "MEL"
    REGION_MEL = "MEL"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "YUL"
    REGION_YUL = "YUL"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "HYD"
    REGION_HYD = "HYD"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "YNY"
    REGION_YNY = "YNY"

    #: A constant which can be used with the region property of a CreateResourceDetails.
    #: This constant has a value of "TIW"
    REGION_TIW = "TIW"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "DEV_1"
    AVAILABILITY_DOMAIN_DEV_1 = "DEV_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "DEV_2"
    AVAILABILITY_DOMAIN_DEV_2 = "DEV_2"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "DEV_3"
    AVAILABILITY_DOMAIN_DEV_3 = "DEV_3"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "INTEG_NEXT_1"
    AVAILABILITY_DOMAIN_INTEG_NEXT_1 = "INTEG_NEXT_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "INTEG_STABLE_1"
    AVAILABILITY_DOMAIN_INTEG_STABLE_1 = "INTEG_STABLE_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "SEA_AD_1"
    AVAILABILITY_DOMAIN_SEA_AD_1 = "SEA_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "SEA_AD_2"
    AVAILABILITY_DOMAIN_SEA_AD_2 = "SEA_AD_2"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "SEA_AD_3"
    AVAILABILITY_DOMAIN_SEA_AD_3 = "SEA_AD_3"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "PHX_AD_1"
    AVAILABILITY_DOMAIN_PHX_AD_1 = "PHX_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "PHX_AD_2"
    AVAILABILITY_DOMAIN_PHX_AD_2 = "PHX_AD_2"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "PHX_AD_3"
    AVAILABILITY_DOMAIN_PHX_AD_3 = "PHX_AD_3"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "US_ASHBURN_AD_1"
    AVAILABILITY_DOMAIN_US_ASHBURN_AD_1 = "US_ASHBURN_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "US_ASHBURN_AD_2"
    AVAILABILITY_DOMAIN_US_ASHBURN_AD_2 = "US_ASHBURN_AD_2"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "US_ASHBURN_AD_3"
    AVAILABILITY_DOMAIN_US_ASHBURN_AD_3 = "US_ASHBURN_AD_3"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "US_ASHBURN_AD_4"
    AVAILABILITY_DOMAIN_US_ASHBURN_AD_4 = "US_ASHBURN_AD_4"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "EU_FRANKFURT_1_AD_1"
    AVAILABILITY_DOMAIN_EU_FRANKFURT_1_AD_1 = "EU_FRANKFURT_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "EU_FRANKFURT_1_AD_2"
    AVAILABILITY_DOMAIN_EU_FRANKFURT_1_AD_2 = "EU_FRANKFURT_1_AD_2"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "EU_FRANKFURT_1_AD_3"
    AVAILABILITY_DOMAIN_EU_FRANKFURT_1_AD_3 = "EU_FRANKFURT_1_AD_3"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "UK_LONDON_1_AD_1"
    AVAILABILITY_DOMAIN_UK_LONDON_1_AD_1 = "UK_LONDON_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "UK_LONDON_1_AD_2"
    AVAILABILITY_DOMAIN_UK_LONDON_1_AD_2 = "UK_LONDON_1_AD_2"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "UK_LONDON_1_AD_3"
    AVAILABILITY_DOMAIN_UK_LONDON_1_AD_3 = "UK_LONDON_1_AD_3"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "CA_TORONTO_1_AD_1"
    AVAILABILITY_DOMAIN_CA_TORONTO_1_AD_1 = "CA_TORONTO_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "AP_TOKYO_1_AD_1"
    AVAILABILITY_DOMAIN_AP_TOKYO_1_AD_1 = "AP_TOKYO_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "AP_SEOUL_1_AD_1"
    AVAILABILITY_DOMAIN_AP_SEOUL_1_AD_1 = "AP_SEOUL_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "AP_MUMBAI_1_AD_1"
    AVAILABILITY_DOMAIN_AP_MUMBAI_1_AD_1 = "AP_MUMBAI_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "SA_SAOPAULO_1_AD_1"
    AVAILABILITY_DOMAIN_SA_SAOPAULO_1_AD_1 = "SA_SAOPAULO_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "US_LUKE_1_AD_1"
    AVAILABILITY_DOMAIN_US_LUKE_1_AD_1 = "US_LUKE_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "US_LANGLEY_1_AD_1"
    AVAILABILITY_DOMAIN_US_LANGLEY_1_AD_1 = "US_LANGLEY_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "ME_JEDDAH_1_AD_1"
    AVAILABILITY_DOMAIN_ME_JEDDAH_1_AD_1 = "ME_JEDDAH_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "AP_OSAKA_1_AD_1"
    AVAILABILITY_DOMAIN_AP_OSAKA_1_AD_1 = "AP_OSAKA_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "AP_SYDNEY_1_AD_1"
    AVAILABILITY_DOMAIN_AP_SYDNEY_1_AD_1 = "AP_SYDNEY_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "EU_ZURICH_1_AD_1"
    AVAILABILITY_DOMAIN_EU_ZURICH_1_AD_1 = "EU_ZURICH_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "EU_AMSTERDAM_1_AD_1"
    AVAILABILITY_DOMAIN_EU_AMSTERDAM_1_AD_1 = "EU_AMSTERDAM_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "AP_MELBOURNE_1_AD_1"
    AVAILABILITY_DOMAIN_AP_MELBOURNE_1_AD_1 = "AP_MELBOURNE_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "CA_MONTREAL_1_AD_1"
    AVAILABILITY_DOMAIN_CA_MONTREAL_1_AD_1 = "CA_MONTREAL_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "AP_HYDERABAD_1_AD_1"
    AVAILABILITY_DOMAIN_AP_HYDERABAD_1_AD_1 = "AP_HYDERABAD_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "AP_CHUNCHEON_1_AD_1"
    AVAILABILITY_DOMAIN_AP_CHUNCHEON_1_AD_1 = "AP_CHUNCHEON_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "US_TACOMA_1_AD_1"
    AVAILABILITY_DOMAIN_US_TACOMA_1_AD_1 = "US_TACOMA_1_AD_1"

    #: A constant which can be used with the availability_domain property of a CreateResourceDetails.
    #: This constant has a value of "NO_AD"
    AVAILABILITY_DOMAIN_NO_AD = "NO_AD"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateResourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param item:
            The value to assign to the item property of this CreateResourceDetails.
        :type item: CreateItemDetails

        :param region:
            The value to assign to the region property of this CreateResourceDetails.
            Allowed values for this property are: "DEV", "SEA", "INTEG_NEXT", "INTEG_STABLE", "PHX", "IAD", "FRA", "EU_FRANKFURT_1", "LHR", "YYZ", "NRT", "US_LANGLEY_1", "US_LUKE_1", "ICN", "BOM", "GRU", "US_GOV_ASHBURN_1", "US_GOV_PHOENIX_1", "US_GOV_CHICAGO_1", "SYD", "ZRH", "JED", "AMS", "KIX", "MEL", "YUL", "HYD", "YNY", "TIW"
        :type region: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateResourceDetails.
            Allowed values for this property are: "DEV_1", "DEV_2", "DEV_3", "INTEG_NEXT_1", "INTEG_STABLE_1", "SEA_AD_1", "SEA_AD_2", "SEA_AD_3", "PHX_AD_1", "PHX_AD_2", "PHX_AD_3", "US_ASHBURN_AD_1", "US_ASHBURN_AD_2", "US_ASHBURN_AD_3", "US_ASHBURN_AD_4", "EU_FRANKFURT_1_AD_1", "EU_FRANKFURT_1_AD_2", "EU_FRANKFURT_1_AD_3", "UK_LONDON_1_AD_1", "UK_LONDON_1_AD_2", "UK_LONDON_1_AD_3", "CA_TORONTO_1_AD_1", "AP_TOKYO_1_AD_1", "AP_SEOUL_1_AD_1", "AP_MUMBAI_1_AD_1", "SA_SAOPAULO_1_AD_1", "US_LUKE_1_AD_1", "US_LANGLEY_1_AD_1", "ME_JEDDAH_1_AD_1", "AP_OSAKA_1_AD_1", "AP_SYDNEY_1_AD_1", "EU_ZURICH_1_AD_1", "EU_AMSTERDAM_1_AD_1", "AP_MELBOURNE_1_AD_1", "CA_MONTREAL_1_AD_1", "AP_HYDERABAD_1_AD_1", "AP_CHUNCHEON_1_AD_1", "US_TACOMA_1_AD_1", "NO_AD"
        :type availability_domain: str

        """
        self.swagger_types = {
            'item': 'CreateItemDetails',
            'region': 'str',
            'availability_domain': 'str'
        }

        self.attribute_map = {
            'item': 'item',
            'region': 'region',
            'availability_domain': 'availabilityDomain'
        }

        self._item = None
        self._region = None
        self._availability_domain = None

    @property
    def item(self):
        """
        Gets the item of this CreateResourceDetails.

        :return: The item of this CreateResourceDetails.
        :rtype: CreateItemDetails
        """
        return self._item

    @item.setter
    def item(self, item):
        """
        Sets the item of this CreateResourceDetails.

        :param item: The item of this CreateResourceDetails.
        :type: CreateItemDetails
        """
        self._item = item

    @property
    def region(self):
        """
        Gets the region of this CreateResourceDetails.
        List of OCI regions

        Allowed values for this property are: "DEV", "SEA", "INTEG_NEXT", "INTEG_STABLE", "PHX", "IAD", "FRA", "EU_FRANKFURT_1", "LHR", "YYZ", "NRT", "US_LANGLEY_1", "US_LUKE_1", "ICN", "BOM", "GRU", "US_GOV_ASHBURN_1", "US_GOV_PHOENIX_1", "US_GOV_CHICAGO_1", "SYD", "ZRH", "JED", "AMS", "KIX", "MEL", "YUL", "HYD", "YNY", "TIW"


        :return: The region of this CreateResourceDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this CreateResourceDetails.
        List of OCI regions


        :param region: The region of this CreateResourceDetails.
        :type: str
        """
        allowed_values = ["DEV", "SEA", "INTEG_NEXT", "INTEG_STABLE", "PHX", "IAD", "FRA", "EU_FRANKFURT_1", "LHR", "YYZ", "NRT", "US_LANGLEY_1", "US_LUKE_1", "ICN", "BOM", "GRU", "US_GOV_ASHBURN_1", "US_GOV_PHOENIX_1", "US_GOV_CHICAGO_1", "SYD", "ZRH", "JED", "AMS", "KIX", "MEL", "YUL", "HYD", "YNY", "TIW"]
        if not value_allowed_none_or_none_sentinel(region, allowed_values):
            raise ValueError(
                "Invalid value for `region`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._region = region

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this CreateResourceDetails.
        List of OCI ADs

        Allowed values for this property are: "DEV_1", "DEV_2", "DEV_3", "INTEG_NEXT_1", "INTEG_STABLE_1", "SEA_AD_1", "SEA_AD_2", "SEA_AD_3", "PHX_AD_1", "PHX_AD_2", "PHX_AD_3", "US_ASHBURN_AD_1", "US_ASHBURN_AD_2", "US_ASHBURN_AD_3", "US_ASHBURN_AD_4", "EU_FRANKFURT_1_AD_1", "EU_FRANKFURT_1_AD_2", "EU_FRANKFURT_1_AD_3", "UK_LONDON_1_AD_1", "UK_LONDON_1_AD_2", "UK_LONDON_1_AD_3", "CA_TORONTO_1_AD_1", "AP_TOKYO_1_AD_1", "AP_SEOUL_1_AD_1", "AP_MUMBAI_1_AD_1", "SA_SAOPAULO_1_AD_1", "US_LUKE_1_AD_1", "US_LANGLEY_1_AD_1", "ME_JEDDAH_1_AD_1", "AP_OSAKA_1_AD_1", "AP_SYDNEY_1_AD_1", "EU_ZURICH_1_AD_1", "EU_AMSTERDAM_1_AD_1", "AP_MELBOURNE_1_AD_1", "CA_MONTREAL_1_AD_1", "AP_HYDERABAD_1_AD_1", "AP_CHUNCHEON_1_AD_1", "US_TACOMA_1_AD_1", "NO_AD"


        :return: The availability_domain of this CreateResourceDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateResourceDetails.
        List of OCI ADs


        :param availability_domain: The availability_domain of this CreateResourceDetails.
        :type: str
        """
        allowed_values = ["DEV_1", "DEV_2", "DEV_3", "INTEG_NEXT_1", "INTEG_STABLE_1", "SEA_AD_1", "SEA_AD_2", "SEA_AD_3", "PHX_AD_1", "PHX_AD_2", "PHX_AD_3", "US_ASHBURN_AD_1", "US_ASHBURN_AD_2", "US_ASHBURN_AD_3", "US_ASHBURN_AD_4", "EU_FRANKFURT_1_AD_1", "EU_FRANKFURT_1_AD_2", "EU_FRANKFURT_1_AD_3", "UK_LONDON_1_AD_1", "UK_LONDON_1_AD_2", "UK_LONDON_1_AD_3", "CA_TORONTO_1_AD_1", "AP_TOKYO_1_AD_1", "AP_SEOUL_1_AD_1", "AP_MUMBAI_1_AD_1", "SA_SAOPAULO_1_AD_1", "US_LUKE_1_AD_1", "US_LANGLEY_1_AD_1", "ME_JEDDAH_1_AD_1", "AP_OSAKA_1_AD_1", "AP_SYDNEY_1_AD_1", "EU_ZURICH_1_AD_1", "EU_AMSTERDAM_1_AD_1", "AP_MELBOURNE_1_AD_1", "CA_MONTREAL_1_AD_1", "AP_HYDERABAD_1_AD_1", "AP_CHUNCHEON_1_AD_1", "US_TACOMA_1_AD_1", "NO_AD"]
        if not value_allowed_none_or_none_sentinel(availability_domain, allowed_values):
            raise ValueError(
                "Invalid value for `availability_domain`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._availability_domain = availability_domain

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
