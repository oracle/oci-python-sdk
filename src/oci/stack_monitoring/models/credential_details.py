# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CredentialDetails(object):
    """
    DiscoveryJob Credential Details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CredentialDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_name:
            The value to assign to the credential_name property of this CredentialDetails.
        :type credential_name: str

        :param credential_type:
            The value to assign to the credential_type property of this CredentialDetails.
        :type credential_type: str

        :param properties:
            The value to assign to the properties property of this CredentialDetails.
        :type properties: oci.stack_monitoring.models.PropertyDetails

        """
        self.swagger_types = {
            'credential_name': 'str',
            'credential_type': 'str',
            'properties': 'PropertyDetails'
        }

        self.attribute_map = {
            'credential_name': 'credentialName',
            'credential_type': 'credentialType',
            'properties': 'properties'
        }

        self._credential_name = None
        self._credential_type = None
        self._properties = None

    @property
    def credential_name(self):
        """
        **[Required]** Gets the credential_name of this CredentialDetails.
        Name of Credential


        :return: The credential_name of this CredentialDetails.
        :rtype: str
        """
        return self._credential_name

    @credential_name.setter
    def credential_name(self, credential_name):
        """
        Sets the credential_name of this CredentialDetails.
        Name of Credential


        :param credential_name: The credential_name of this CredentialDetails.
        :type: str
        """
        self._credential_name = credential_name

    @property
    def credential_type(self):
        """
        **[Required]** Gets the credential_type of this CredentialDetails.
        Name of Credential Type


        :return: The credential_type of this CredentialDetails.
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """
        Sets the credential_type of this CredentialDetails.
        Name of Credential Type


        :param credential_type: The credential_type of this CredentialDetails.
        :type: str
        """
        self._credential_type = credential_type

    @property
    def properties(self):
        """
        **[Required]** Gets the properties of this CredentialDetails.

        :return: The properties of this CredentialDetails.
        :rtype: oci.stack_monitoring.models.PropertyDetails
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CredentialDetails.

        :param properties: The properties of this CredentialDetails.
        :type: oci.stack_monitoring.models.PropertyDetails
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
