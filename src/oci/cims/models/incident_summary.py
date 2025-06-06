# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181231


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IncidentSummary(object):
    """
    Details about the support ticket.
    """

    #: A constant which can be used with the problem_type property of a IncidentSummary.
    #: This constant has a value of "LIMIT"
    PROBLEM_TYPE_LIMIT = "LIMIT"

    #: A constant which can be used with the problem_type property of a IncidentSummary.
    #: This constant has a value of "LEGACY_LIMIT"
    PROBLEM_TYPE_LEGACY_LIMIT = "LEGACY_LIMIT"

    #: A constant which can be used with the problem_type property of a IncidentSummary.
    #: This constant has a value of "TECH"
    PROBLEM_TYPE_TECH = "TECH"

    #: A constant which can be used with the problem_type property of a IncidentSummary.
    #: This constant has a value of "ACCOUNT"
    PROBLEM_TYPE_ACCOUNT = "ACCOUNT"

    #: A constant which can be used with the problem_type property of a IncidentSummary.
    #: This constant has a value of "TAXONOMY"
    PROBLEM_TYPE_TAXONOMY = "TAXONOMY"

    def __init__(self, **kwargs):
        """
        Initializes a new IncidentSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this IncidentSummary.
        :type key: str

        :param compartment_id:
            The value to assign to the compartment_id property of this IncidentSummary.
        :type compartment_id: str

        :param contact_list:
            The value to assign to the contact_list property of this IncidentSummary.
        :type contact_list: oci.cims.models.ContactList

        :param tenancy_information:
            The value to assign to the tenancy_information property of this IncidentSummary.
        :type tenancy_information: oci.cims.models.TenancyInformation

        :param ticket:
            The value to assign to the ticket property of this IncidentSummary.
        :type ticket: oci.cims.models.Ticket

        :param incident_type:
            The value to assign to the incident_type property of this IncidentSummary.
        :type incident_type: oci.cims.models.IncidentResourceType

        :param user_group_id:
            The value to assign to the user_group_id property of this IncidentSummary.
        :type user_group_id: str

        :param user_group_name:
            The value to assign to the user_group_name property of this IncidentSummary.
        :type user_group_name: str

        :param primary_contact_party_id:
            The value to assign to the primary_contact_party_id property of this IncidentSummary.
        :type primary_contact_party_id: str

        :param primary_contact_party_name:
            The value to assign to the primary_contact_party_name property of this IncidentSummary.
        :type primary_contact_party_name: str

        :param is_write_permitted:
            The value to assign to the is_write_permitted property of this IncidentSummary.
        :type is_write_permitted: bool

        :param warn_message:
            The value to assign to the warn_message property of this IncidentSummary.
        :type warn_message: str

        :param problem_type:
            The value to assign to the problem_type property of this IncidentSummary.
            Allowed values for this property are: "LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT", "TAXONOMY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type problem_type: str

        """
        self.swagger_types = {
            'key': 'str',
            'compartment_id': 'str',
            'contact_list': 'ContactList',
            'tenancy_information': 'TenancyInformation',
            'ticket': 'Ticket',
            'incident_type': 'IncidentResourceType',
            'user_group_id': 'str',
            'user_group_name': 'str',
            'primary_contact_party_id': 'str',
            'primary_contact_party_name': 'str',
            'is_write_permitted': 'bool',
            'warn_message': 'str',
            'problem_type': 'str'
        }
        self.attribute_map = {
            'key': 'key',
            'compartment_id': 'compartmentId',
            'contact_list': 'contactList',
            'tenancy_information': 'tenancyInformation',
            'ticket': 'ticket',
            'incident_type': 'incidentType',
            'user_group_id': 'userGroupId',
            'user_group_name': 'userGroupName',
            'primary_contact_party_id': 'primaryContactPartyId',
            'primary_contact_party_name': 'primaryContactPartyName',
            'is_write_permitted': 'isWritePermitted',
            'warn_message': 'warnMessage',
            'problem_type': 'problemType'
        }
        self._key = None
        self._compartment_id = None
        self._contact_list = None
        self._tenancy_information = None
        self._ticket = None
        self._incident_type = None
        self._user_group_id = None
        self._user_group_name = None
        self._primary_contact_party_id = None
        self._primary_contact_party_name = None
        self._is_write_permitted = None
        self._warn_message = None
        self._problem_type = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this IncidentSummary.
        Unique identifier of the incident.


        :return: The key of this IncidentSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this IncidentSummary.
        Unique identifier of the incident.


        :param key: The key of this IncidentSummary.
        :type: str
        """
        self._key = key

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this IncidentSummary.
        The OCID of the tenancy.


        :return: The compartment_id of this IncidentSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IncidentSummary.
        The OCID of the tenancy.


        :param compartment_id: The compartment_id of this IncidentSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def contact_list(self):
        """
        Gets the contact_list of this IncidentSummary.

        :return: The contact_list of this IncidentSummary.
        :rtype: oci.cims.models.ContactList
        """
        return self._contact_list

    @contact_list.setter
    def contact_list(self, contact_list):
        """
        Sets the contact_list of this IncidentSummary.

        :param contact_list: The contact_list of this IncidentSummary.
        :type: oci.cims.models.ContactList
        """
        self._contact_list = contact_list

    @property
    def tenancy_information(self):
        """
        Gets the tenancy_information of this IncidentSummary.

        :return: The tenancy_information of this IncidentSummary.
        :rtype: oci.cims.models.TenancyInformation
        """
        return self._tenancy_information

    @tenancy_information.setter
    def tenancy_information(self, tenancy_information):
        """
        Sets the tenancy_information of this IncidentSummary.

        :param tenancy_information: The tenancy_information of this IncidentSummary.
        :type: oci.cims.models.TenancyInformation
        """
        self._tenancy_information = tenancy_information

    @property
    def ticket(self):
        """
        Gets the ticket of this IncidentSummary.

        :return: The ticket of this IncidentSummary.
        :rtype: oci.cims.models.Ticket
        """
        return self._ticket

    @ticket.setter
    def ticket(self, ticket):
        """
        Sets the ticket of this IncidentSummary.

        :param ticket: The ticket of this IncidentSummary.
        :type: oci.cims.models.Ticket
        """
        self._ticket = ticket

    @property
    def incident_type(self):
        """
        Gets the incident_type of this IncidentSummary.

        :return: The incident_type of this IncidentSummary.
        :rtype: oci.cims.models.IncidentResourceType
        """
        return self._incident_type

    @incident_type.setter
    def incident_type(self, incident_type):
        """
        Sets the incident_type of this IncidentSummary.

        :param incident_type: The incident_type of this IncidentSummary.
        :type: oci.cims.models.IncidentResourceType
        """
        self._incident_type = incident_type

    @property
    def user_group_id(self):
        """
        Gets the user_group_id of this IncidentSummary.
        Technical support type (`TECH`) only: The identifier of the support request's user group in My Oracle Cloud Support portal.


        :return: The user_group_id of this IncidentSummary.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """
        Sets the user_group_id of this IncidentSummary.
        Technical support type (`TECH`) only: The identifier of the support request's user group in My Oracle Cloud Support portal.


        :param user_group_id: The user_group_id of this IncidentSummary.
        :type: str
        """
        self._user_group_id = user_group_id

    @property
    def user_group_name(self):
        """
        Gets the user_group_name of this IncidentSummary.
        Technical support type (`TECH`) only: Name of the support request's user group in My Oracle Cloud Support portal.


        :return: The user_group_name of this IncidentSummary.
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        """
        Sets the user_group_name of this IncidentSummary.
        Technical support type (`TECH`) only: Name of the support request's user group in My Oracle Cloud Support portal.


        :param user_group_name: The user_group_name of this IncidentSummary.
        :type: str
        """
        self._user_group_name = user_group_name

    @property
    def primary_contact_party_id(self):
        """
        Gets the primary_contact_party_id of this IncidentSummary.
        Technical support type (`TECH`) only: The identifier of the support request's primary contact (`primaryContactPartyName`) in My Oracle Cloud Support portal.


        :return: The primary_contact_party_id of this IncidentSummary.
        :rtype: str
        """
        return self._primary_contact_party_id

    @primary_contact_party_id.setter
    def primary_contact_party_id(self, primary_contact_party_id):
        """
        Sets the primary_contact_party_id of this IncidentSummary.
        Technical support type (`TECH`) only: The identifier of the support request's primary contact (`primaryContactPartyName`) in My Oracle Cloud Support portal.


        :param primary_contact_party_id: The primary_contact_party_id of this IncidentSummary.
        :type: str
        """
        self._primary_contact_party_id = primary_contact_party_id

    @property
    def primary_contact_party_name(self):
        """
        Gets the primary_contact_party_name of this IncidentSummary.
        Technical support type (`TECH`) only: The name of the support request's primary contact in My Oracle Cloud Support portal.


        :return: The primary_contact_party_name of this IncidentSummary.
        :rtype: str
        """
        return self._primary_contact_party_name

    @primary_contact_party_name.setter
    def primary_contact_party_name(self, primary_contact_party_name):
        """
        Sets the primary_contact_party_name of this IncidentSummary.
        Technical support type (`TECH`) only: The name of the support request's primary contact in My Oracle Cloud Support portal.


        :param primary_contact_party_name: The primary_contact_party_name of this IncidentSummary.
        :type: str
        """
        self._primary_contact_party_name = primary_contact_party_name

    @property
    def is_write_permitted(self):
        """
        Gets the is_write_permitted of this IncidentSummary.
        Technical support type (`TECH`) only: Allows update of the support request in My Oracle Cloud Support portal,
        when the user has write permission to the support request's user group.


        :return: The is_write_permitted of this IncidentSummary.
        :rtype: bool
        """
        return self._is_write_permitted

    @is_write_permitted.setter
    def is_write_permitted(self, is_write_permitted):
        """
        Sets the is_write_permitted of this IncidentSummary.
        Technical support type (`TECH`) only: Allows update of the support request in My Oracle Cloud Support portal,
        when the user has write permission to the support request's user group.


        :param is_write_permitted: The is_write_permitted of this IncidentSummary.
        :type: bool
        """
        self._is_write_permitted = is_write_permitted

    @property
    def warn_message(self):
        """
        Gets the warn_message of this IncidentSummary.
        Technical support type (`TECH`) only: Message indicating the user group (`userGroupId`) that was auto-selected for a new support request. This message appears when no user group was specified in the create request for a new technical support request.


        :return: The warn_message of this IncidentSummary.
        :rtype: str
        """
        return self._warn_message

    @warn_message.setter
    def warn_message(self, warn_message):
        """
        Sets the warn_message of this IncidentSummary.
        Technical support type (`TECH`) only: Message indicating the user group (`userGroupId`) that was auto-selected for a new support request. This message appears when no user group was specified in the create request for a new technical support request.


        :param warn_message: The warn_message of this IncidentSummary.
        :type: str
        """
        self._warn_message = warn_message

    @property
    def problem_type(self):
        """
        **[Required]** Gets the problem_type of this IncidentSummary.
        The kind of support ticket (type of support request).
        For information about `ACCOUNT` support tickets, see
        `Creating a Billing Support Request`__.
        For information about `LIMIT` support tickets, see
        `Creating a Service Limit Increase Request`__.
        For information about `TECH` support tickets, see
        `Creating a Technical Support Request`__.

        __ https://docs.cloud.oracle.com/iaas/Content/GSG/support/create-incident-billing.htm
        __ https://docs.cloud.oracle.com/iaas/Content/GSG/support/create-incident-limit.htm
        __ https://docs.cloud.oracle.com/iaas/Content/GSG/support/create-incident-technical.htm

        Allowed values for this property are: "LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT", "TAXONOMY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The problem_type of this IncidentSummary.
        :rtype: str
        """
        return self._problem_type

    @problem_type.setter
    def problem_type(self, problem_type):
        """
        Sets the problem_type of this IncidentSummary.
        The kind of support ticket (type of support request).
        For information about `ACCOUNT` support tickets, see
        `Creating a Billing Support Request`__.
        For information about `LIMIT` support tickets, see
        `Creating a Service Limit Increase Request`__.
        For information about `TECH` support tickets, see
        `Creating a Technical Support Request`__.

        __ https://docs.cloud.oracle.com/iaas/Content/GSG/support/create-incident-billing.htm
        __ https://docs.cloud.oracle.com/iaas/Content/GSG/support/create-incident-limit.htm
        __ https://docs.cloud.oracle.com/iaas/Content/GSG/support/create-incident-technical.htm


        :param problem_type: The problem_type of this IncidentSummary.
        :type: str
        """
        allowed_values = ["LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT", "TAXONOMY"]
        if not value_allowed_none_or_none_sentinel(problem_type, allowed_values):
            problem_type = 'UNKNOWN_ENUM_VALUE'
        self._problem_type = problem_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
