# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTicketDetails(object):
    """
    Details of Ticket updated
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTicketDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource:
            The value to assign to the resource property of this UpdateTicketDetails.
        :type resource: object

        """
        self.swagger_types = {
            'resource': 'object'
        }

        self.attribute_map = {
            'resource': 'resource'
        }

        self._resource = None

    @property
    def resource(self):
        """
        **[Required]** Gets the resource of this UpdateTicketDetails.
        List of resources


        :return: The resource of this UpdateTicketDetails.
        :rtype: object
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this UpdateTicketDetails.
        List of resources


        :param resource: The resource of this UpdateTicketDetails.
        :type: object
        """
        self._resource = resource

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
