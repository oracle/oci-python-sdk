# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIncident(object):
    """
    Details about the support ticket being updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIncident object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ticket:
            The value to assign to the ticket property of this UpdateIncident.
        :type ticket: UpdateTicketDetails

        """
        self.swagger_types = {
            'ticket': 'UpdateTicketDetails'
        }

        self.attribute_map = {
            'ticket': 'ticket'
        }

        self._ticket = None

    @property
    def ticket(self):
        """
        **[Required]** Gets the ticket of this UpdateIncident.

        :return: The ticket of this UpdateIncident.
        :rtype: UpdateTicketDetails
        """
        return self._ticket

    @ticket.setter
    def ticket(self, ticket):
        """
        Sets the ticket of this UpdateIncident.

        :param ticket: The ticket of this UpdateIncident.
        :type: UpdateTicketDetails
        """
        self._ticket = ticket

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
