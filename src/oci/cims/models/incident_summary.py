# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


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

        :param problem_type:
            The value to assign to the problem_type property of this IncidentSummary.
            Allowed values for this property are: "LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT", 'UNKNOWN_ENUM_VALUE'.
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
            'problem_type': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'compartment_id': 'compartmentId',
            'contact_list': 'contactList',
            'tenancy_information': 'tenancyInformation',
            'ticket': 'ticket',
            'incident_type': 'incidentType',
            'problem_type': 'problemType'
        }

        self._key = None
        self._compartment_id = None
        self._contact_list = None
        self._tenancy_information = None
        self._ticket = None
        self._incident_type = None
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
    def problem_type(self):
        """
        **[Required]** Gets the problem_type of this IncidentSummary.
        The kind of support ticket, such as a technical support request.

        Allowed values for this property are: "LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The problem_type of this IncidentSummary.
        :rtype: str
        """
        return self._problem_type

    @problem_type.setter
    def problem_type(self, problem_type):
        """
        Sets the problem_type of this IncidentSummary.
        The kind of support ticket, such as a technical support request.


        :param problem_type: The problem_type of this IncidentSummary.
        :type: str
        """
        allowed_values = ["LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT"]
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
