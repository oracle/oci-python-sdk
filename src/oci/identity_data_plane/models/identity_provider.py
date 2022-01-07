# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IdentityProvider(object):
    """
    IdentityProvider model.
    """

    #: A constant which can be used with the protocol property of a IdentityProvider.
    #: This constant has a value of "SAML2"
    PROTOCOL_SAML2 = "SAML2"

    def __init__(self, **kwargs):
        """
        Initializes a new IdentityProvider object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this IdentityProvider.
        :type id: str

        :param name:
            The value to assign to the name property of this IdentityProvider.
        :type name: str

        :param tenant_name:
            The value to assign to the tenant_name property of this IdentityProvider.
        :type tenant_name: str

        :param tenant_id:
            The value to assign to the tenant_id property of this IdentityProvider.
        :type tenant_id: str

        :param redirect_uri:
            The value to assign to the redirect_uri property of this IdentityProvider.
        :type redirect_uri: str

        :param signing_certificate:
            The value to assign to the signing_certificate property of this IdentityProvider.
        :type signing_certificate: str

        :param protocol:
            The value to assign to the protocol property of this IdentityProvider.
            Allowed values for this property are: "SAML2"
        :type protocol: str

        :param service_provider_entity_id:
            The value to assign to the service_provider_entity_id property of this IdentityProvider.
        :type service_provider_entity_id: str

        :param force_authentication:
            The value to assign to the force_authentication property of this IdentityProvider.
        :type force_authentication: bool

        :param authn_context_class_refs:
            The value to assign to the authn_context_class_refs property of this IdentityProvider.
        :type authn_context_class_refs: list[str]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'tenant_name': 'str',
            'tenant_id': 'str',
            'redirect_uri': 'str',
            'signing_certificate': 'str',
            'protocol': 'str',
            'service_provider_entity_id': 'str',
            'force_authentication': 'bool',
            'authn_context_class_refs': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'tenant_name': 'tenantName',
            'tenant_id': 'tenantId',
            'redirect_uri': 'redirectUri',
            'signing_certificate': 'signingCertificate',
            'protocol': 'protocol',
            'service_provider_entity_id': 'serviceProviderEntityId',
            'force_authentication': 'forceAuthentication',
            'authn_context_class_refs': 'authnContextClassRefs'
        }

        self._id = None
        self._name = None
        self._tenant_name = None
        self._tenant_id = None
        self._redirect_uri = None
        self._signing_certificate = None
        self._protocol = None
        self._service_provider_entity_id = None
        self._force_authentication = None
        self._authn_context_class_refs = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IdentityProvider.
        The id of the provider.


        :return: The id of this IdentityProvider.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IdentityProvider.
        The id of the provider.


        :param id: The id of this IdentityProvider.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this IdentityProvider.
        The name of the provider.


        :return: The name of this IdentityProvider.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IdentityProvider.
        The name of the provider.


        :param name: The name of this IdentityProvider.
        :type: str
        """
        self._name = name

    @property
    def tenant_name(self):
        """
        **[Required]** Gets the tenant_name of this IdentityProvider.
        The name of the tenant.


        :return: The tenant_name of this IdentityProvider.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """
        Sets the tenant_name of this IdentityProvider.
        The name of the tenant.


        :param tenant_name: The tenant_name of this IdentityProvider.
        :type: str
        """
        self._tenant_name = tenant_name

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this IdentityProvider.
        The id of the tenant.


        :return: The tenant_id of this IdentityProvider.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this IdentityProvider.
        The id of the tenant.


        :param tenant_id: The tenant_id of this IdentityProvider.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def redirect_uri(self):
        """
        **[Required]** Gets the redirect_uri of this IdentityProvider.
        The SAML endpoint where user will be redirected.


        :return: The redirect_uri of this IdentityProvider.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """
        Sets the redirect_uri of this IdentityProvider.
        The SAML endpoint where user will be redirected.


        :param redirect_uri: The redirect_uri of this IdentityProvider.
        :type: str
        """
        self._redirect_uri = redirect_uri

    @property
    def signing_certificate(self):
        """
        **[Required]** Gets the signing_certificate of this IdentityProvider.
        The signing certificate of the provider.


        :return: The signing_certificate of this IdentityProvider.
        :rtype: str
        """
        return self._signing_certificate

    @signing_certificate.setter
    def signing_certificate(self, signing_certificate):
        """
        Sets the signing_certificate of this IdentityProvider.
        The signing certificate of the provider.


        :param signing_certificate: The signing_certificate of this IdentityProvider.
        :type: str
        """
        self._signing_certificate = signing_certificate

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this IdentityProvider.
        The type of the provider.

        Allowed values for this property are: "SAML2"


        :return: The protocol of this IdentityProvider.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this IdentityProvider.
        The type of the provider.


        :param protocol: The protocol of this IdentityProvider.
        :type: str
        """
        allowed_values = ["SAML2"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            raise ValueError(
                "Invalid value for `protocol`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._protocol = protocol

    @property
    def service_provider_entity_id(self):
        """
        **[Required]** Gets the service_provider_entity_id of this IdentityProvider.
        The id of the service provider entity.


        :return: The service_provider_entity_id of this IdentityProvider.
        :rtype: str
        """
        return self._service_provider_entity_id

    @service_provider_entity_id.setter
    def service_provider_entity_id(self, service_provider_entity_id):
        """
        Sets the service_provider_entity_id of this IdentityProvider.
        The id of the service provider entity.


        :param service_provider_entity_id: The service_provider_entity_id of this IdentityProvider.
        :type: str
        """
        self._service_provider_entity_id = service_provider_entity_id

    @property
    def force_authentication(self):
        """
        **[Required]** Gets the force_authentication of this IdentityProvider.
        Whether to force authentication.


        :return: The force_authentication of this IdentityProvider.
        :rtype: bool
        """
        return self._force_authentication

    @force_authentication.setter
    def force_authentication(self, force_authentication):
        """
        Sets the force_authentication of this IdentityProvider.
        Whether to force authentication.


        :param force_authentication: The force_authentication of this IdentityProvider.
        :type: bool
        """
        self._force_authentication = force_authentication

    @property
    def authn_context_class_refs(self):
        """
        **[Required]** Gets the authn_context_class_refs of this IdentityProvider.
        Authentication context class refs.


        :return: The authn_context_class_refs of this IdentityProvider.
        :rtype: list[str]
        """
        return self._authn_context_class_refs

    @authn_context_class_refs.setter
    def authn_context_class_refs(self, authn_context_class_refs):
        """
        Sets the authn_context_class_refs of this IdentityProvider.
        Authentication context class refs.


        :param authn_context_class_refs: The authn_context_class_refs of this IdentityProvider.
        :type: list[str]
        """
        self._authn_context_class_refs = authn_context_class_refs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
