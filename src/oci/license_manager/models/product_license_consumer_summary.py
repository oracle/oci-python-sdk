# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProductLicenseConsumerSummary(object):
    """
    Details of a resource that is consuming a particular product license.
    """

    #: A constant which can be used with the resource_unit_type property of a ProductLicenseConsumerSummary.
    #: This constant has a value of "OCPU"
    RESOURCE_UNIT_TYPE_OCPU = "OCPU"

    #: A constant which can be used with the license_unit_type property of a ProductLicenseConsumerSummary.
    #: This constant has a value of "OCPU"
    LICENSE_UNIT_TYPE_OCPU = "OCPU"

    #: A constant which can be used with the license_unit_type property of a ProductLicenseConsumerSummary.
    #: This constant has a value of "NAMED_USER_PLUS"
    LICENSE_UNIT_TYPE_NAMED_USER_PLUS = "NAMED_USER_PLUS"

    #: A constant which can be used with the license_unit_type property of a ProductLicenseConsumerSummary.
    #: This constant has a value of "PROCESSORS"
    LICENSE_UNIT_TYPE_PROCESSORS = "PROCESSORS"

    def __init__(self, **kwargs):
        """
        Initializes a new ProductLicenseConsumerSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_id:
            The value to assign to the resource_id property of this ProductLicenseConsumerSummary.
        :type resource_id: str

        :param resource_name:
            The value to assign to the resource_name property of this ProductLicenseConsumerSummary.
        :type resource_name: str

        :param product_name:
            The value to assign to the product_name property of this ProductLicenseConsumerSummary.
        :type product_name: str

        :param resource_compartment_id:
            The value to assign to the resource_compartment_id property of this ProductLicenseConsumerSummary.
        :type resource_compartment_id: str

        :param resource_compartment_name:
            The value to assign to the resource_compartment_name property of this ProductLicenseConsumerSummary.
        :type resource_compartment_name: str

        :param resource_unit_type:
            The value to assign to the resource_unit_type property of this ProductLicenseConsumerSummary.
            Allowed values for this property are: "OCPU", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_unit_type: str

        :param resource_unit_count:
            The value to assign to the resource_unit_count property of this ProductLicenseConsumerSummary.
        :type resource_unit_count: float

        :param license_unit_type:
            The value to assign to the license_unit_type property of this ProductLicenseConsumerSummary.
            Allowed values for this property are: "OCPU", "NAMED_USER_PLUS", "PROCESSORS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_unit_type: str

        :param license_units_consumed:
            The value to assign to the license_units_consumed property of this ProductLicenseConsumerSummary.
        :type license_units_consumed: float

        :param is_base_license_available:
            The value to assign to the is_base_license_available property of this ProductLicenseConsumerSummary.
        :type is_base_license_available: bool

        :param are_all_options_available:
            The value to assign to the are_all_options_available property of this ProductLicenseConsumerSummary.
        :type are_all_options_available: bool

        :param missing_products:
            The value to assign to the missing_products property of this ProductLicenseConsumerSummary.
        :type missing_products: list[oci.license_manager.models.Product]

        """
        self.swagger_types = {
            'resource_id': 'str',
            'resource_name': 'str',
            'product_name': 'str',
            'resource_compartment_id': 'str',
            'resource_compartment_name': 'str',
            'resource_unit_type': 'str',
            'resource_unit_count': 'float',
            'license_unit_type': 'str',
            'license_units_consumed': 'float',
            'is_base_license_available': 'bool',
            'are_all_options_available': 'bool',
            'missing_products': 'list[Product]'
        }

        self.attribute_map = {
            'resource_id': 'resourceId',
            'resource_name': 'resourceName',
            'product_name': 'productName',
            'resource_compartment_id': 'resourceCompartmentId',
            'resource_compartment_name': 'resourceCompartmentName',
            'resource_unit_type': 'resourceUnitType',
            'resource_unit_count': 'resourceUnitCount',
            'license_unit_type': 'licenseUnitType',
            'license_units_consumed': 'licenseUnitsConsumed',
            'is_base_license_available': 'isBaseLicenseAvailable',
            'are_all_options_available': 'areAllOptionsAvailable',
            'missing_products': 'missingProducts'
        }

        self._resource_id = None
        self._resource_name = None
        self._product_name = None
        self._resource_compartment_id = None
        self._resource_compartment_name = None
        self._resource_unit_type = None
        self._resource_unit_count = None
        self._license_unit_type = None
        self._license_units_consumed = None
        self._is_base_license_available = None
        self._are_all_options_available = None
        self._missing_products = None

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this ProductLicenseConsumerSummary.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The resource_id of this ProductLicenseConsumerSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this ProductLicenseConsumerSummary.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param resource_id: The resource_id of this ProductLicenseConsumerSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this ProductLicenseConsumerSummary.
        The display name of the resource.


        :return: The resource_name of this ProductLicenseConsumerSummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this ProductLicenseConsumerSummary.
        The display name of the resource.


        :param resource_name: The resource_name of this ProductLicenseConsumerSummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def product_name(self):
        """
        **[Required]** Gets the product_name of this ProductLicenseConsumerSummary.
        The resource product name.


        :return: The product_name of this ProductLicenseConsumerSummary.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this ProductLicenseConsumerSummary.
        The resource product name.


        :param product_name: The product_name of this ProductLicenseConsumerSummary.
        :type: str
        """
        self._product_name = product_name

    @property
    def resource_compartment_id(self):
        """
        **[Required]** Gets the resource_compartment_id of this ProductLicenseConsumerSummary.
        The `OCID`__ of the compartment that contains the resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The resource_compartment_id of this ProductLicenseConsumerSummary.
        :rtype: str
        """
        return self._resource_compartment_id

    @resource_compartment_id.setter
    def resource_compartment_id(self, resource_compartment_id):
        """
        Sets the resource_compartment_id of this ProductLicenseConsumerSummary.
        The `OCID`__ of the compartment that contains the resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param resource_compartment_id: The resource_compartment_id of this ProductLicenseConsumerSummary.
        :type: str
        """
        self._resource_compartment_id = resource_compartment_id

    @property
    def resource_compartment_name(self):
        """
        **[Required]** Gets the resource_compartment_name of this ProductLicenseConsumerSummary.
        The display name of the compartment that contains the resource.


        :return: The resource_compartment_name of this ProductLicenseConsumerSummary.
        :rtype: str
        """
        return self._resource_compartment_name

    @resource_compartment_name.setter
    def resource_compartment_name(self, resource_compartment_name):
        """
        Sets the resource_compartment_name of this ProductLicenseConsumerSummary.
        The display name of the compartment that contains the resource.


        :param resource_compartment_name: The resource_compartment_name of this ProductLicenseConsumerSummary.
        :type: str
        """
        self._resource_compartment_name = resource_compartment_name

    @property
    def resource_unit_type(self):
        """
        **[Required]** Gets the resource_unit_type of this ProductLicenseConsumerSummary.
        The unit type for the resource.

        Allowed values for this property are: "OCPU", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_unit_type of this ProductLicenseConsumerSummary.
        :rtype: str
        """
        return self._resource_unit_type

    @resource_unit_type.setter
    def resource_unit_type(self, resource_unit_type):
        """
        Sets the resource_unit_type of this ProductLicenseConsumerSummary.
        The unit type for the resource.


        :param resource_unit_type: The resource_unit_type of this ProductLicenseConsumerSummary.
        :type: str
        """
        allowed_values = ["OCPU"]
        if not value_allowed_none_or_none_sentinel(resource_unit_type, allowed_values):
            resource_unit_type = 'UNKNOWN_ENUM_VALUE'
        self._resource_unit_type = resource_unit_type

    @property
    def resource_unit_count(self):
        """
        **[Required]** Gets the resource_unit_count of this ProductLicenseConsumerSummary.
        Number of units of the resource


        :return: The resource_unit_count of this ProductLicenseConsumerSummary.
        :rtype: float
        """
        return self._resource_unit_count

    @resource_unit_count.setter
    def resource_unit_count(self, resource_unit_count):
        """
        Sets the resource_unit_count of this ProductLicenseConsumerSummary.
        Number of units of the resource


        :param resource_unit_count: The resource_unit_count of this ProductLicenseConsumerSummary.
        :type: float
        """
        self._resource_unit_count = resource_unit_count

    @property
    def license_unit_type(self):
        """
        **[Required]** Gets the license_unit_type of this ProductLicenseConsumerSummary.
        The product license unit.

        Allowed values for this property are: "OCPU", "NAMED_USER_PLUS", "PROCESSORS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_unit_type of this ProductLicenseConsumerSummary.
        :rtype: str
        """
        return self._license_unit_type

    @license_unit_type.setter
    def license_unit_type(self, license_unit_type):
        """
        Sets the license_unit_type of this ProductLicenseConsumerSummary.
        The product license unit.


        :param license_unit_type: The license_unit_type of this ProductLicenseConsumerSummary.
        :type: str
        """
        allowed_values = ["OCPU", "NAMED_USER_PLUS", "PROCESSORS"]
        if not value_allowed_none_or_none_sentinel(license_unit_type, allowed_values):
            license_unit_type = 'UNKNOWN_ENUM_VALUE'
        self._license_unit_type = license_unit_type

    @property
    def license_units_consumed(self):
        """
        **[Required]** Gets the license_units_consumed of this ProductLicenseConsumerSummary.
        Number of license units consumed by the resource.


        :return: The license_units_consumed of this ProductLicenseConsumerSummary.
        :rtype: float
        """
        return self._license_units_consumed

    @license_units_consumed.setter
    def license_units_consumed(self, license_units_consumed):
        """
        Sets the license_units_consumed of this ProductLicenseConsumerSummary.
        Number of license units consumed by the resource.


        :param license_units_consumed: The license_units_consumed of this ProductLicenseConsumerSummary.
        :type: float
        """
        self._license_units_consumed = license_units_consumed

    @property
    def is_base_license_available(self):
        """
        **[Required]** Gets the is_base_license_available of this ProductLicenseConsumerSummary.
        Specifies if the base license is available.


        :return: The is_base_license_available of this ProductLicenseConsumerSummary.
        :rtype: bool
        """
        return self._is_base_license_available

    @is_base_license_available.setter
    def is_base_license_available(self, is_base_license_available):
        """
        Sets the is_base_license_available of this ProductLicenseConsumerSummary.
        Specifies if the base license is available.


        :param is_base_license_available: The is_base_license_available of this ProductLicenseConsumerSummary.
        :type: bool
        """
        self._is_base_license_available = is_base_license_available

    @property
    def are_all_options_available(self):
        """
        **[Required]** Gets the are_all_options_available of this ProductLicenseConsumerSummary.
        Specifies if all options are available.


        :return: The are_all_options_available of this ProductLicenseConsumerSummary.
        :rtype: bool
        """
        return self._are_all_options_available

    @are_all_options_available.setter
    def are_all_options_available(self, are_all_options_available):
        """
        Sets the are_all_options_available of this ProductLicenseConsumerSummary.
        Specifies if all options are available.


        :param are_all_options_available: The are_all_options_available of this ProductLicenseConsumerSummary.
        :type: bool
        """
        self._are_all_options_available = are_all_options_available

    @property
    def missing_products(self):
        """
        **[Required]** Gets the missing_products of this ProductLicenseConsumerSummary.
        Collection of missing product licenses.


        :return: The missing_products of this ProductLicenseConsumerSummary.
        :rtype: list[oci.license_manager.models.Product]
        """
        return self._missing_products

    @missing_products.setter
    def missing_products(self, missing_products):
        """
        Sets the missing_products of this ProductLicenseConsumerSummary.
        Collection of missing product licenses.


        :param missing_products: The missing_products of this ProductLicenseConsumerSummary.
        :type: list[oci.license_manager.models.Product]
        """
        self._missing_products = missing_products

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
