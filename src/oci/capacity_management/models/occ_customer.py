# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OccCustomer(object):
    """
    The details about the customer.
    """

    #: A constant which can be used with the status property of a OccCustomer.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a OccCustomer.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new OccCustomer object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param occ_customer_group_id:
            The value to assign to the occ_customer_group_id property of this OccCustomer.
        :type occ_customer_group_id: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this OccCustomer.
        :type tenancy_id: str

        :param display_name:
            The value to assign to the display_name property of this OccCustomer.
        :type display_name: str

        :param description:
            The value to assign to the description property of this OccCustomer.
        :type description: str

        :param status:
            The value to assign to the status property of this OccCustomer.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'occ_customer_group_id': 'str',
            'tenancy_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'status': 'str'
        }
        self.attribute_map = {
            'occ_customer_group_id': 'occCustomerGroupId',
            'tenancy_id': 'tenancyId',
            'display_name': 'displayName',
            'description': 'description',
            'status': 'status'
        }
        self._occ_customer_group_id = None
        self._tenancy_id = None
        self._display_name = None
        self._description = None
        self._status = None

    @property
    def occ_customer_group_id(self):
        """
        **[Required]** Gets the occ_customer_group_id of this OccCustomer.
        The OCID of the customer group.


        :return: The occ_customer_group_id of this OccCustomer.
        :rtype: str
        """
        return self._occ_customer_group_id

    @occ_customer_group_id.setter
    def occ_customer_group_id(self, occ_customer_group_id):
        """
        Sets the occ_customer_group_id of this OccCustomer.
        The OCID of the customer group.


        :param occ_customer_group_id: The occ_customer_group_id of this OccCustomer.
        :type: str
        """
        self._occ_customer_group_id = occ_customer_group_id

    @property
    def tenancy_id(self):
        """
        **[Required]** Gets the tenancy_id of this OccCustomer.
        The OCID of the tenancy belonging to the customer.


        :return: The tenancy_id of this OccCustomer.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this OccCustomer.
        The OCID of the tenancy belonging to the customer.


        :param tenancy_id: The tenancy_id of this OccCustomer.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OccCustomer.
        The display name for the customer


        :return: The display_name of this OccCustomer.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OccCustomer.
        The display name for the customer


        :param display_name: The display_name of this OccCustomer.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this OccCustomer.
        The description about the customer group.


        :return: The description of this OccCustomer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OccCustomer.
        The description about the customer group.


        :param description: The description of this OccCustomer.
        :type: str
        """
        self._description = description

    @property
    def status(self):
        """
        **[Required]** Gets the status of this OccCustomer.
        To determine whether the customer is enabled/disabled.`

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this OccCustomer.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this OccCustomer.
        To determine whether the customer is enabled/disabled.`


        :param status: The status of this OccCustomer.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
