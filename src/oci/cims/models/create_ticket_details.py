# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTicketDetails(object):
    """
    Details relevant to the support ticket.

    **Caution:** Avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the severity property of a CreateTicketDetails.
    #: This constant has a value of "HIGHEST"
    SEVERITY_HIGHEST = "HIGHEST"

    #: A constant which can be used with the severity property of a CreateTicketDetails.
    #: This constant has a value of "HIGH"
    SEVERITY_HIGH = "HIGH"

    #: A constant which can be used with the severity property of a CreateTicketDetails.
    #: This constant has a value of "MEDIUM"
    SEVERITY_MEDIUM = "MEDIUM"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTicketDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param severity:
            The value to assign to the severity property of this CreateTicketDetails.
            Allowed values for this property are: "HIGHEST", "HIGH", "MEDIUM"
        :type severity: str

        :param resource_list:
            The value to assign to the resource_list property of this CreateTicketDetails.
        :type resource_list: list[oci.cims.models.CreateResourceDetails]

        :param title:
            The value to assign to the title property of this CreateTicketDetails.
        :type title: str

        :param description:
            The value to assign to the description property of this CreateTicketDetails.
        :type description: str

        :param contextual_data:
            The value to assign to the contextual_data property of this CreateTicketDetails.
        :type contextual_data: oci.cims.models.ContextualData

        """
        self.swagger_types = {
            'severity': 'str',
            'resource_list': 'list[CreateResourceDetails]',
            'title': 'str',
            'description': 'str',
            'contextual_data': 'ContextualData'
        }

        self.attribute_map = {
            'severity': 'severity',
            'resource_list': 'resourceList',
            'title': 'title',
            'description': 'description',
            'contextual_data': 'contextualData'
        }

        self._severity = None
        self._resource_list = None
        self._title = None
        self._description = None
        self._contextual_data = None

    @property
    def severity(self):
        """
        **[Required]** Gets the severity of this CreateTicketDetails.
        The severity of the support ticket.

        Allowed values for this property are: "HIGHEST", "HIGH", "MEDIUM"


        :return: The severity of this CreateTicketDetails.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this CreateTicketDetails.
        The severity of the support ticket.


        :param severity: The severity of this CreateTicketDetails.
        :type: str
        """
        allowed_values = ["HIGHEST", "HIGH", "MEDIUM"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            raise ValueError(
                "Invalid value for `severity`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._severity = severity

    @property
    def resource_list(self):
        """
        Gets the resource_list of this CreateTicketDetails.
        The list of resources.


        :return: The resource_list of this CreateTicketDetails.
        :rtype: list[oci.cims.models.CreateResourceDetails]
        """
        return self._resource_list

    @resource_list.setter
    def resource_list(self, resource_list):
        """
        Sets the resource_list of this CreateTicketDetails.
        The list of resources.


        :param resource_list: The resource_list of this CreateTicketDetails.
        :type: list[oci.cims.models.CreateResourceDetails]
        """
        self._resource_list = resource_list

    @property
    def title(self):
        """
        **[Required]** Gets the title of this CreateTicketDetails.
        The title of the support ticket.


        :return: The title of this CreateTicketDetails.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CreateTicketDetails.
        The title of the support ticket.


        :param title: The title of this CreateTicketDetails.
        :type: str
        """
        self._title = title

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CreateTicketDetails.
        The description of the support ticket.


        :return: The description of this CreateTicketDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateTicketDetails.
        The description of the support ticket.


        :param description: The description of this CreateTicketDetails.
        :type: str
        """
        self._description = description

    @property
    def contextual_data(self):
        """
        Gets the contextual_data of this CreateTicketDetails.
        The context from where the ticket is getting created.


        :return: The contextual_data of this CreateTicketDetails.
        :rtype: oci.cims.models.ContextualData
        """
        return self._contextual_data

    @contextual_data.setter
    def contextual_data(self, contextual_data):
        """
        Sets the contextual_data of this CreateTicketDetails.
        The context from where the ticket is getting created.


        :param contextual_data: The contextual_data of this CreateTicketDetails.
        :type: oci.cims.models.ContextualData
        """
        self._contextual_data = contextual_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
