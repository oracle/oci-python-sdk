# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateIdentityProviderDetails(object):
    """
    CreateIdentityProviderDetails model.
    """

    #: A constant which can be used with the product_type property of a CreateIdentityProviderDetails.
    #: This constant has a value of "IDCS"
    PRODUCT_TYPE_IDCS = "IDCS"

    #: A constant which can be used with the product_type property of a CreateIdentityProviderDetails.
    #: This constant has a value of "ADFS"
    PRODUCT_TYPE_ADFS = "ADFS"

    #: A constant which can be used with the protocol property of a CreateIdentityProviderDetails.
    #: This constant has a value of "SAML2"
    PROTOCOL_SAML2 = "SAML2"

    #: A constant which can be used with the protocol property of a CreateIdentityProviderDetails.
    #: This constant has a value of "ADFS"
    PROTOCOL_ADFS = "ADFS"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateIdentityProviderDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.identity.models.CreateSaml2IdentityProviderDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateIdentityProviderDetails.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this CreateIdentityProviderDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateIdentityProviderDetails.
        :type description: str

        :param product_type:
            The value to assign to the product_type property of this CreateIdentityProviderDetails.
            Allowed values for this property are: "IDCS", "ADFS"
        :type product_type: str

        :param protocol:
            The value to assign to the protocol property of this CreateIdentityProviderDetails.
            Allowed values for this property are: "SAML2", "ADFS"
        :type protocol: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateIdentityProviderDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateIdentityProviderDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'product_type': 'str',
            'protocol': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'product_type': 'productType',
            'protocol': 'protocol',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._name = None
        self._description = None
        self._product_type = None
        self._protocol = None
        self._freeform_tags = None
        self._defined_tags = None

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
        **[Required]** Gets the compartment_id of this CreateIdentityProviderDetails.
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
        **[Required]** Gets the name of this CreateIdentityProviderDetails.
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
        **[Required]** Gets the description of this CreateIdentityProviderDetails.
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
        **[Required]** Gets the product_type of this CreateIdentityProviderDetails.
        The identity provider service or product.
        Supported identity providers are Oracle Identity Cloud Service (IDCS) and Microsoft
        Active Directory Federation Services (ADFS).

        Example: `IDCS`

        Allowed values for this property are: "IDCS", "ADFS"


        :return: The product_type of this CreateIdentityProviderDetails.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """
        Sets the product_type of this CreateIdentityProviderDetails.
        The identity provider service or product.
        Supported identity providers are Oracle Identity Cloud Service (IDCS) and Microsoft
        Active Directory Federation Services (ADFS).

        Example: `IDCS`


        :param product_type: The product_type of this CreateIdentityProviderDetails.
        :type: str
        """
        allowed_values = ["IDCS", "ADFS"]
        if not value_allowed_none_or_none_sentinel(product_type, allowed_values):
            raise ValueError(
                "Invalid value for `product_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._product_type = product_type

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this CreateIdentityProviderDetails.
        The protocol used for federation.

        Example: `SAML2`

        Allowed values for this property are: "SAML2", "ADFS"


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
        allowed_values = ["SAML2", "ADFS"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            raise ValueError(
                "Invalid value for `protocol`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._protocol = protocol

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateIdentityProviderDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateIdentityProviderDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateIdentityProviderDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateIdentityProviderDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateIdentityProviderDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateIdentityProviderDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateIdentityProviderDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateIdentityProviderDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
