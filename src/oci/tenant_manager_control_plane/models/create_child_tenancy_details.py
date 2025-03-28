# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230401


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateChildTenancyDetails(object):
    """
    The parameters for creating a child tenancy.
    """

    #: A constant which can be used with the governance_status property of a CreateChildTenancyDetails.
    #: This constant has a value of "OPTED_IN"
    GOVERNANCE_STATUS_OPTED_IN = "OPTED_IN"

    #: A constant which can be used with the governance_status property of a CreateChildTenancyDetails.
    #: This constant has a value of "OPTED_OUT"
    GOVERNANCE_STATUS_OPTED_OUT = "OPTED_OUT"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateChildTenancyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateChildTenancyDetails.
        :type compartment_id: str

        :param tenancy_name:
            The value to assign to the tenancy_name property of this CreateChildTenancyDetails.
        :type tenancy_name: str

        :param home_region:
            The value to assign to the home_region property of this CreateChildTenancyDetails.
        :type home_region: str

        :param admin_email:
            The value to assign to the admin_email property of this CreateChildTenancyDetails.
        :type admin_email: str

        :param policy_name:
            The value to assign to the policy_name property of this CreateChildTenancyDetails.
        :type policy_name: str

        :param governance_status:
            The value to assign to the governance_status property of this CreateChildTenancyDetails.
            Allowed values for this property are: "OPTED_IN", "OPTED_OUT"
        :type governance_status: str

        :param subscription_id:
            The value to assign to the subscription_id property of this CreateChildTenancyDetails.
        :type subscription_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'tenancy_name': 'str',
            'home_region': 'str',
            'admin_email': 'str',
            'policy_name': 'str',
            'governance_status': 'str',
            'subscription_id': 'str'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'tenancy_name': 'tenancyName',
            'home_region': 'homeRegion',
            'admin_email': 'adminEmail',
            'policy_name': 'policyName',
            'governance_status': 'governanceStatus',
            'subscription_id': 'subscriptionId'
        }
        self._compartment_id = None
        self._tenancy_name = None
        self._home_region = None
        self._admin_email = None
        self._policy_name = None
        self._governance_status = None
        self._subscription_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateChildTenancyDetails.
        The tenancy ID of the parent tenancy.


        :return: The compartment_id of this CreateChildTenancyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateChildTenancyDetails.
        The tenancy ID of the parent tenancy.


        :param compartment_id: The compartment_id of this CreateChildTenancyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tenancy_name(self):
        """
        **[Required]** Gets the tenancy_name of this CreateChildTenancyDetails.
        The tenancy name to use for the child tenancy.


        :return: The tenancy_name of this CreateChildTenancyDetails.
        :rtype: str
        """
        return self._tenancy_name

    @tenancy_name.setter
    def tenancy_name(self, tenancy_name):
        """
        Sets the tenancy_name of this CreateChildTenancyDetails.
        The tenancy name to use for the child tenancy.


        :param tenancy_name: The tenancy_name of this CreateChildTenancyDetails.
        :type: str
        """
        self._tenancy_name = tenancy_name

    @property
    def home_region(self):
        """
        **[Required]** Gets the home_region of this CreateChildTenancyDetails.
        The home region to use for the child tenancy. This must be a region where the parent tenancy is subscribed.


        :return: The home_region of this CreateChildTenancyDetails.
        :rtype: str
        """
        return self._home_region

    @home_region.setter
    def home_region(self, home_region):
        """
        Sets the home_region of this CreateChildTenancyDetails.
        The home region to use for the child tenancy. This must be a region where the parent tenancy is subscribed.


        :param home_region: The home_region of this CreateChildTenancyDetails.
        :type: str
        """
        self._home_region = home_region

    @property
    def admin_email(self):
        """
        **[Required]** Gets the admin_email of this CreateChildTenancyDetails.
        Email address of the child tenancy administrator.


        :return: The admin_email of this CreateChildTenancyDetails.
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """
        Sets the admin_email of this CreateChildTenancyDetails.
        Email address of the child tenancy administrator.


        :param admin_email: The admin_email of this CreateChildTenancyDetails.
        :type: str
        """
        self._admin_email = admin_email

    @property
    def policy_name(self):
        """
        Gets the policy_name of this CreateChildTenancyDetails.
        The name to use for the administrator policy in the child tenancy. Must contain only letters and underscores.


        :return: The policy_name of this CreateChildTenancyDetails.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """
        Sets the policy_name of this CreateChildTenancyDetails.
        The name to use for the administrator policy in the child tenancy. Must contain only letters and underscores.


        :param policy_name: The policy_name of this CreateChildTenancyDetails.
        :type: str
        """
        self._policy_name = policy_name

    @property
    def governance_status(self):
        """
        Gets the governance_status of this CreateChildTenancyDetails.
        The governance status of the child tenancy.

        Allowed values for this property are: "OPTED_IN", "OPTED_OUT"


        :return: The governance_status of this CreateChildTenancyDetails.
        :rtype: str
        """
        return self._governance_status

    @governance_status.setter
    def governance_status(self, governance_status):
        """
        Sets the governance_status of this CreateChildTenancyDetails.
        The governance status of the child tenancy.


        :param governance_status: The governance_status of this CreateChildTenancyDetails.
        :type: str
        """
        allowed_values = ["OPTED_IN", "OPTED_OUT"]
        if not value_allowed_none_or_none_sentinel(governance_status, allowed_values):
            raise ValueError(
                f"Invalid value for `governance_status`, must be None or one of {allowed_values}"
            )
        self._governance_status = governance_status

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this CreateChildTenancyDetails.
        OCID of the subscription that needs to be assigned to the child tenancy.


        :return: The subscription_id of this CreateChildTenancyDetails.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this CreateChildTenancyDetails.
        OCID of the subscription that needs to be assigned to the child tenancy.


        :param subscription_id: The subscription_id of this CreateChildTenancyDetails.
        :type: str
        """
        self._subscription_id = subscription_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
