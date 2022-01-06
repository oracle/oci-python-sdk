# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateIncident(object):
    """
    Details gathered during the creation of the support ticket.

    **Caution:** Avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the problem_type property of a CreateIncident.
    #: This constant has a value of "LIMIT"
    PROBLEM_TYPE_LIMIT = "LIMIT"

    #: A constant which can be used with the problem_type property of a CreateIncident.
    #: This constant has a value of "LEGACY_LIMIT"
    PROBLEM_TYPE_LEGACY_LIMIT = "LEGACY_LIMIT"

    #: A constant which can be used with the problem_type property of a CreateIncident.
    #: This constant has a value of "TECH"
    PROBLEM_TYPE_TECH = "TECH"

    #: A constant which can be used with the problem_type property of a CreateIncident.
    #: This constant has a value of "ACCOUNT"
    PROBLEM_TYPE_ACCOUNT = "ACCOUNT"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateIncident object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateIncident.
        :type compartment_id: str

        :param ticket:
            The value to assign to the ticket property of this CreateIncident.
        :type ticket: oci.cims.models.CreateTicketDetails

        :param csi:
            The value to assign to the csi property of this CreateIncident.
        :type csi: str

        :param problem_type:
            The value to assign to the problem_type property of this CreateIncident.
            Allowed values for this property are: "LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT"
        :type problem_type: str

        :param contacts:
            The value to assign to the contacts property of this CreateIncident.
        :type contacts: list[oci.cims.models.Contact]

        :param referrer:
            The value to assign to the referrer property of this CreateIncident.
        :type referrer: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'ticket': 'CreateTicketDetails',
            'csi': 'str',
            'problem_type': 'str',
            'contacts': 'list[Contact]',
            'referrer': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'ticket': 'ticket',
            'csi': 'csi',
            'problem_type': 'problemType',
            'contacts': 'contacts',
            'referrer': 'referrer'
        }

        self._compartment_id = None
        self._ticket = None
        self._csi = None
        self._problem_type = None
        self._contacts = None
        self._referrer = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateIncident.
        The OCID of the tenancy.


        :return: The compartment_id of this CreateIncident.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateIncident.
        The OCID of the tenancy.


        :param compartment_id: The compartment_id of this CreateIncident.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def ticket(self):
        """
        **[Required]** Gets the ticket of this CreateIncident.

        :return: The ticket of this CreateIncident.
        :rtype: oci.cims.models.CreateTicketDetails
        """
        return self._ticket

    @ticket.setter
    def ticket(self, ticket):
        """
        Sets the ticket of this CreateIncident.

        :param ticket: The ticket of this CreateIncident.
        :type: oci.cims.models.CreateTicketDetails
        """
        self._ticket = ticket

    @property
    def csi(self):
        """
        Gets the csi of this CreateIncident.
        The Customer Support Identifier number for the support account.


        :return: The csi of this CreateIncident.
        :rtype: str
        """
        return self._csi

    @csi.setter
    def csi(self, csi):
        """
        Sets the csi of this CreateIncident.
        The Customer Support Identifier number for the support account.


        :param csi: The csi of this CreateIncident.
        :type: str
        """
        self._csi = csi

    @property
    def problem_type(self):
        """
        **[Required]** Gets the problem_type of this CreateIncident.
        The kind of support ticket, such as a technical issue request.

        Allowed values for this property are: "LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT"


        :return: The problem_type of this CreateIncident.
        :rtype: str
        """
        return self._problem_type

    @problem_type.setter
    def problem_type(self, problem_type):
        """
        Sets the problem_type of this CreateIncident.
        The kind of support ticket, such as a technical issue request.


        :param problem_type: The problem_type of this CreateIncident.
        :type: str
        """
        allowed_values = ["LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT"]
        if not value_allowed_none_or_none_sentinel(problem_type, allowed_values):
            raise ValueError(
                "Invalid value for `problem_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._problem_type = problem_type

    @property
    def contacts(self):
        """
        Gets the contacts of this CreateIncident.
        The list of contacts.


        :return: The contacts of this CreateIncident.
        :rtype: list[oci.cims.models.Contact]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """
        Sets the contacts of this CreateIncident.
        The list of contacts.


        :param contacts: The contacts of this CreateIncident.
        :type: list[oci.cims.models.Contact]
        """
        self._contacts = contacts

    @property
    def referrer(self):
        """
        Gets the referrer of this CreateIncident.
        The incident referrer. This value is often the URL that the customer used when creating the support ticket.


        :return: The referrer of this CreateIncident.
        :rtype: str
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer):
        """
        Sets the referrer of this CreateIncident.
        The incident referrer. This value is often the URL that the customer used when creating the support ticket.


        :param referrer: The referrer of this CreateIncident.
        :type: str
        """
        self._referrer = referrer

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
