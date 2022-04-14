# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .monitored_resource_credential import MonitoredResourceCredential
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PlainTextCredentials(MonitoredResourceCredential):
    """
    Plain text credentials [indicated by the type property in CredentialStore].
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PlainTextCredentials object with values from keyword arguments. The default value of the :py:attr:`~oci.stack_monitoring.models.PlainTextCredentials.credential_type` attribute
        of this class is ``PLAINTEXT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this PlainTextCredentials.
        :type source: str

        :param name:
            The value to assign to the name property of this PlainTextCredentials.
        :type name: str

        :param type:
            The value to assign to the type property of this PlainTextCredentials.
        :type type: str

        :param description:
            The value to assign to the description property of this PlainTextCredentials.
        :type description: str

        :param credential_type:
            The value to assign to the credential_type property of this PlainTextCredentials.
            Allowed values for this property are: "EXISTING", "PLAINTEXT", "ENCRYPTED"
        :type credential_type: str

        :param properties:
            The value to assign to the properties property of this PlainTextCredentials.
        :type properties: list[oci.stack_monitoring.models.CredentialProperty]

        """
        self.swagger_types = {
            'source': 'str',
            'name': 'str',
            'type': 'str',
            'description': 'str',
            'credential_type': 'str',
            'properties': 'list[CredentialProperty]'
        }

        self.attribute_map = {
            'source': 'source',
            'name': 'name',
            'type': 'type',
            'description': 'description',
            'credential_type': 'credentialType',
            'properties': 'properties'
        }

        self._source = None
        self._name = None
        self._type = None
        self._description = None
        self._credential_type = None
        self._properties = None
        self._credential_type = 'PLAINTEXT'

    @property
    def properties(self):
        """
        **[Required]** Gets the properties of this PlainTextCredentials.
        The credential properties list. Credential property values will be either in plain text format.


        :return: The properties of this PlainTextCredentials.
        :rtype: list[oci.stack_monitoring.models.CredentialProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this PlainTextCredentials.
        The credential properties list. Credential property values will be either in plain text format.


        :param properties: The properties of this PlainTextCredentials.
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
