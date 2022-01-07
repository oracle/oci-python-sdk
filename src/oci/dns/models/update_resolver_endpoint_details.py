# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateResolverEndpointDetails(object):
    """
    The body for updating an existing resolver endpoint.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the endpoint_type property of a UpdateResolverEndpointDetails.
    #: This constant has a value of "VNIC"
    ENDPOINT_TYPE_VNIC = "VNIC"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateResolverEndpointDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.dns.models.UpdateResolverVnicEndpointDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param endpoint_type:
            The value to assign to the endpoint_type property of this UpdateResolverEndpointDetails.
            Allowed values for this property are: "VNIC"
        :type endpoint_type: str

        """
        self.swagger_types = {
            'endpoint_type': 'str'
        }

        self.attribute_map = {
            'endpoint_type': 'endpointType'
        }

        self._endpoint_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['endpointType']

        if type == 'VNIC':
            return 'UpdateResolverVnicEndpointDetails'
        else:
            return 'UpdateResolverEndpointDetails'

    @property
    def endpoint_type(self):
        """
        Gets the endpoint_type of this UpdateResolverEndpointDetails.
        The type of resolver endpoint. VNIC is currently the only supported type.

        Allowed values for this property are: "VNIC"


        :return: The endpoint_type of this UpdateResolverEndpointDetails.
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """
        Sets the endpoint_type of this UpdateResolverEndpointDetails.
        The type of resolver endpoint. VNIC is currently the only supported type.


        :param endpoint_type: The endpoint_type of this UpdateResolverEndpointDetails.
        :type: str
        """
        allowed_values = ["VNIC"]
        if not value_allowed_none_or_none_sentinel(endpoint_type, allowed_values):
            raise ValueError(
                "Invalid value for `endpoint_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._endpoint_type = endpoint_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
