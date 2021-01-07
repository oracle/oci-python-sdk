# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateResolverEndpointDetails(object):
    """
    The body for defining a new resolver endpoint.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the endpoint_type property of a CreateResolverEndpointDetails.
    #: This constant has a value of "VNIC"
    ENDPOINT_TYPE_VNIC = "VNIC"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateResolverEndpointDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.dns.models.CreateResolverVnicEndpointDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateResolverEndpointDetails.
        :type name: str

        :param endpoint_type:
            The value to assign to the endpoint_type property of this CreateResolverEndpointDetails.
            Allowed values for this property are: "VNIC"
        :type endpoint_type: str

        :param forwarding_address:
            The value to assign to the forwarding_address property of this CreateResolverEndpointDetails.
        :type forwarding_address: str

        :param is_forwarding:
            The value to assign to the is_forwarding property of this CreateResolverEndpointDetails.
        :type is_forwarding: bool

        :param is_listening:
            The value to assign to the is_listening property of this CreateResolverEndpointDetails.
        :type is_listening: bool

        :param listening_address:
            The value to assign to the listening_address property of this CreateResolverEndpointDetails.
        :type listening_address: str

        """
        self.swagger_types = {
            'name': 'str',
            'endpoint_type': 'str',
            'forwarding_address': 'str',
            'is_forwarding': 'bool',
            'is_listening': 'bool',
            'listening_address': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'endpoint_type': 'endpointType',
            'forwarding_address': 'forwardingAddress',
            'is_forwarding': 'isForwarding',
            'is_listening': 'isListening',
            'listening_address': 'listeningAddress'
        }

        self._name = None
        self._endpoint_type = None
        self._forwarding_address = None
        self._is_forwarding = None
        self._is_listening = None
        self._listening_address = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['endpointType']

        if type == 'VNIC':
            return 'CreateResolverVnicEndpointDetails'
        else:
            return 'CreateResolverEndpointDetails'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateResolverEndpointDetails.
        The name of the resolver endpoint. Must be unique within the resolver.


        :return: The name of this CreateResolverEndpointDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateResolverEndpointDetails.
        The name of the resolver endpoint. Must be unique within the resolver.


        :param name: The name of this CreateResolverEndpointDetails.
        :type: str
        """
        self._name = name

    @property
    def endpoint_type(self):
        """
        Gets the endpoint_type of this CreateResolverEndpointDetails.
        The type of resolver endpoint. VNIC is currently the only supported type.

        Allowed values for this property are: "VNIC"


        :return: The endpoint_type of this CreateResolverEndpointDetails.
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """
        Sets the endpoint_type of this CreateResolverEndpointDetails.
        The type of resolver endpoint. VNIC is currently the only supported type.


        :param endpoint_type: The endpoint_type of this CreateResolverEndpointDetails.
        :type: str
        """
        allowed_values = ["VNIC"]
        if not value_allowed_none_or_none_sentinel(endpoint_type, allowed_values):
            raise ValueError(
                "Invalid value for `endpoint_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._endpoint_type = endpoint_type

    @property
    def forwarding_address(self):
        """
        Gets the forwarding_address of this CreateResolverEndpointDetails.
        An IP address from which forwarded queries may be sent. For VNIC endpoints, this IP address must be part
        of the subnet and will be assigned by the system if unspecified when isForwarding is true.


        :return: The forwarding_address of this CreateResolverEndpointDetails.
        :rtype: str
        """
        return self._forwarding_address

    @forwarding_address.setter
    def forwarding_address(self, forwarding_address):
        """
        Sets the forwarding_address of this CreateResolverEndpointDetails.
        An IP address from which forwarded queries may be sent. For VNIC endpoints, this IP address must be part
        of the subnet and will be assigned by the system if unspecified when isForwarding is true.


        :param forwarding_address: The forwarding_address of this CreateResolverEndpointDetails.
        :type: str
        """
        self._forwarding_address = forwarding_address

    @property
    def is_forwarding(self):
        """
        **[Required]** Gets the is_forwarding of this CreateResolverEndpointDetails.
        A Boolean flag indicating whether or not the resolver endpoint is for forwarding.


        :return: The is_forwarding of this CreateResolverEndpointDetails.
        :rtype: bool
        """
        return self._is_forwarding

    @is_forwarding.setter
    def is_forwarding(self, is_forwarding):
        """
        Sets the is_forwarding of this CreateResolverEndpointDetails.
        A Boolean flag indicating whether or not the resolver endpoint is for forwarding.


        :param is_forwarding: The is_forwarding of this CreateResolverEndpointDetails.
        :type: bool
        """
        self._is_forwarding = is_forwarding

    @property
    def is_listening(self):
        """
        **[Required]** Gets the is_listening of this CreateResolverEndpointDetails.
        A Boolean flag indicating whether or not the resolver endpoint is for listening.


        :return: The is_listening of this CreateResolverEndpointDetails.
        :rtype: bool
        """
        return self._is_listening

    @is_listening.setter
    def is_listening(self, is_listening):
        """
        Sets the is_listening of this CreateResolverEndpointDetails.
        A Boolean flag indicating whether or not the resolver endpoint is for listening.


        :param is_listening: The is_listening of this CreateResolverEndpointDetails.
        :type: bool
        """
        self._is_listening = is_listening

    @property
    def listening_address(self):
        """
        Gets the listening_address of this CreateResolverEndpointDetails.
        An IP address to listen to queries on. For VNIC endpoints this IP address must be part of the
        subnet and will be assigned by the system if unspecified.


        :return: The listening_address of this CreateResolverEndpointDetails.
        :rtype: str
        """
        return self._listening_address

    @listening_address.setter
    def listening_address(self, listening_address):
        """
        Sets the listening_address of this CreateResolverEndpointDetails.
        An IP address to listen to queries on. For VNIC endpoints this IP address must be part of the
        subnet and will be assigned by the system if unspecified.


        :param listening_address: The listening_address of this CreateResolverEndpointDetails.
        :type: str
        """
        self._listening_address = listening_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
