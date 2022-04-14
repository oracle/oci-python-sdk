# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .monitored_resource_credential import MonitoredResourceCredential
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EncryptedCredentials(MonitoredResourceCredential):
    """
    Encypted credentials [indicated by the type property in CredentialStore].
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EncryptedCredentials object with values from keyword arguments. The default value of the :py:attr:`~oci.stack_monitoring.models.EncryptedCredentials.credential_type` attribute
        of this class is ``ENCRYPTED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this EncryptedCredentials.
        :type source: str

        :param name:
            The value to assign to the name property of this EncryptedCredentials.
        :type name: str

        :param type:
            The value to assign to the type property of this EncryptedCredentials.
        :type type: str

        :param description:
            The value to assign to the description property of this EncryptedCredentials.
        :type description: str

        :param credential_type:
            The value to assign to the credential_type property of this EncryptedCredentials.
            Allowed values for this property are: "EXISTING", "PLAINTEXT", "ENCRYPTED"
        :type credential_type: str

        :param key_id:
            The value to assign to the key_id property of this EncryptedCredentials.
        :type key_id: str

        :param properties:
            The value to assign to the properties property of this EncryptedCredentials.
        :type properties: list[oci.stack_monitoring.models.CredentialProperty]

        """
        self.swagger_types = {
            'source': 'str',
            'name': 'str',
            'type': 'str',
            'description': 'str',
            'credential_type': 'str',
            'key_id': 'str',
            'properties': 'list[CredentialProperty]'
        }

        self.attribute_map = {
            'source': 'source',
            'name': 'name',
            'type': 'type',
            'description': 'description',
            'credential_type': 'credentialType',
            'key_id': 'keyId',
            'properties': 'properties'
        }

        self._source = None
        self._name = None
        self._type = None
        self._description = None
        self._credential_type = None
        self._key_id = None
        self._properties = None
        self._credential_type = 'ENCRYPTED'

    @property
    def key_id(self):
        """
        **[Required]** Gets the key_id of this EncryptedCredentials.
        The master key OCID and applicable only for property value type ENCRYPTION. Key OCID is passed as input to Key management service decrypt API to retrieve the encrypted property value text.


        :return: The key_id of this EncryptedCredentials.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this EncryptedCredentials.
        The master key OCID and applicable only for property value type ENCRYPTION. Key OCID is passed as input to Key management service decrypt API to retrieve the encrypted property value text.


        :param key_id: The key_id of this EncryptedCredentials.
        :type: str
        """
        self._key_id = key_id

    @property
    def properties(self):
        """
        **[Required]** Gets the properties of this EncryptedCredentials.
        The credential properties list. Credential property values will be encrypted format.


        :return: The properties of this EncryptedCredentials.
        :rtype: list[oci.stack_monitoring.models.CredentialProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this EncryptedCredentials.
        The credential properties list. Credential property values will be encrypted format.


        :param properties: The properties of this EncryptedCredentials.
        :type: list[oci.stack_monitoring.models.CredentialProperty]
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
