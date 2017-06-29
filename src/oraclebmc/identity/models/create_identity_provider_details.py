# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateIdentityProviderDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'product_type': 'str',
            'protocol': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'product_type': 'productType',
            'protocol': 'protocol'
        }

        self._compartment_id = None
        self._name = None
        self._description = None
        self._product_type = None
        self._protocol = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['protocol']

        if type == 'SAML2':
            return 'CreateSaml2IdentityProviderDetails'
        else:
            return 'CreateIdentityProviderDetails'

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateIdentityProviderDetails.
        The OCID of your tenancy.


        :return: The compartment_id of this CreateIdentityProviderDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateIdentityProviderDetails.
        The OCID of your tenancy.


        :param compartment_id: The compartment_id of this CreateIdentityProviderDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this CreateIdentityProviderDetails.
        The name you assign to the `IdentityProvider` during creation.
        The name must be unique across all `IdentityProvider` objects in the
        tenancy and cannot be changed.


        :return: The name of this CreateIdentityProviderDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateIdentityProviderDetails.
        The name you assign to the `IdentityProvider` during creation.
        The name must be unique across all `IdentityProvider` objects in the
        tenancy and cannot be changed.


        :param name: The name of this CreateIdentityProviderDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateIdentityProviderDetails.
        The description you assign to the `IdentityProvider` during creation.
        Does not have to be unique, and it's changeable.


        :return: The description of this CreateIdentityProviderDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateIdentityProviderDetails.
        The description you assign to the `IdentityProvider` during creation.
        Does not have to be unique, and it's changeable.


        :param description: The description of this CreateIdentityProviderDetails.
        :type: str
        """
        self._description = description

    @property
    def product_type(self):
        """
        Gets the product_type of this CreateIdentityProviderDetails.
        The identity provider service or product (e.g., Oracle Identity Cloud Service).

        Example: `IDCS`

        Allowed values for this property are: "IDCS"


        :return: The product_type of this CreateIdentityProviderDetails.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """
        Sets the product_type of this CreateIdentityProviderDetails.
        The identity provider service or product (e.g., Oracle Identity Cloud Service).

        Example: `IDCS`


        :param product_type: The product_type of this CreateIdentityProviderDetails.
        :type: str
        """
        allowed_values = ["IDCS"]
        if product_type not in allowed_values:
            raise ValueError(
                "Invalid value for `product_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._product_type = product_type

    @property
    def protocol(self):
        """
        Gets the protocol of this CreateIdentityProviderDetails.
        The protocol used for federation.

        Example: `SAML2`

        Allowed values for this property are: "SAML2"


        :return: The protocol of this CreateIdentityProviderDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this CreateIdentityProviderDetails.
        The protocol used for federation.

        Example: `SAML2`


        :param protocol: The protocol of this CreateIdentityProviderDetails.
        :type: str
        """
        allowed_values = ["SAML2"]
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol`, must be one of {0}"
                .format(allowed_values)
            )
        self._protocol = protocol

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
