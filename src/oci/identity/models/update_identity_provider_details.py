# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIdentityProviderDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIdentityProviderDetails object with values from values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.identity.models.UpdateSaml2IdentityProviderDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param protocol:
            The value to assign to the protocol property of this UpdateIdentityProviderDetails.
            Allowed values for this property are: "SAML2"
        :type protocol: str

        :param description:
            The value to assign to the description property of this UpdateIdentityProviderDetails.
        :type description: str

        """
        self.swagger_types = {
            'protocol': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'description': 'description'
        }

        self._protocol = None
        self._description = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['protocol']

        if type == 'SAML2':
            return 'UpdateSaml2IdentityProviderDetails'
        else:
            return 'UpdateIdentityProviderDetails'

    @property
    def protocol(self):
        """
        Gets the protocol of this UpdateIdentityProviderDetails.
        The protocol used for federation.

        Example: `SAML2`

        Allowed values for this property are: "SAML2"


        :return: The protocol of this UpdateIdentityProviderDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this UpdateIdentityProviderDetails.
        The protocol used for federation.

        Example: `SAML2`


        :param protocol: The protocol of this UpdateIdentityProviderDetails.
        :type: str
        """
        allowed_values = ["SAML2"]
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol`, must be one of {0}"
                .format(allowed_values)
            )
        self._protocol = protocol

    @property
    def description(self):
        """
        Gets the description of this UpdateIdentityProviderDetails.
        The description you assign to the `IdentityProvider`. Does not have to
        be unique, and it's changeable.


        :return: The description of this UpdateIdentityProviderDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateIdentityProviderDetails.
        The description you assign to the `IdentityProvider`. Does not have to
        be unique, and it's changeable.


        :param description: The description of this UpdateIdentityProviderDetails.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
