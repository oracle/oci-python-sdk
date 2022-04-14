# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoredResourceCredential(object):
    """
    Monitored Resource Credential Details
    """

    #: A constant which can be used with the credential_type property of a MonitoredResourceCredential.
    #: This constant has a value of "EXISTING"
    CREDENTIAL_TYPE_EXISTING = "EXISTING"

    #: A constant which can be used with the credential_type property of a MonitoredResourceCredential.
    #: This constant has a value of "PLAINTEXT"
    CREDENTIAL_TYPE_PLAINTEXT = "PLAINTEXT"

    #: A constant which can be used with the credential_type property of a MonitoredResourceCredential.
    #: This constant has a value of "ENCRYPTED"
    CREDENTIAL_TYPE_ENCRYPTED = "ENCRYPTED"

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoredResourceCredential object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.stack_monitoring.models.PreExistingCredentials`
        * :class:`~oci.stack_monitoring.models.EncryptedCredentials`
        * :class:`~oci.stack_monitoring.models.PlainTextCredentials`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this MonitoredResourceCredential.
        :type source: str

        :param name:
            The value to assign to the name property of this MonitoredResourceCredential.
        :type name: str

        :param type:
            The value to assign to the type property of this MonitoredResourceCredential.
        :type type: str

        :param description:
            The value to assign to the description property of this MonitoredResourceCredential.
        :type description: str

        :param credential_type:
            The value to assign to the credential_type property of this MonitoredResourceCredential.
            Allowed values for this property are: "EXISTING", "PLAINTEXT", "ENCRYPTED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type credential_type: str

        """
        self.swagger_types = {
            'source': 'str',
            'name': 'str',
            'type': 'str',
            'description': 'str',
            'credential_type': 'str'
        }

        self.attribute_map = {
            'source': 'source',
            'name': 'name',
            'type': 'type',
            'description': 'description',
            'credential_type': 'credentialType'
        }

        self._source = None
        self._name = None
        self._type = None
        self._description = None
        self._credential_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['credentialType']

        if type == 'EXISTING':
            return 'PreExistingCredentials'

        if type == 'ENCRYPTED':
            return 'EncryptedCredentials'

        if type == 'PLAINTEXT':
            return 'PlainTextCredentials'
        else:
            return 'MonitoredResourceCredential'

    @property
    def source(self):
        """
        Gets the source of this MonitoredResourceCredential.
        The source type and source name combination,delimited with (.) separator. {source type}.{source name} and source type max char limit is 63.


        :return: The source of this MonitoredResourceCredential.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this MonitoredResourceCredential.
        The source type and source name combination,delimited with (.) separator. {source type}.{source name} and source type max char limit is 63.


        :param source: The source of this MonitoredResourceCredential.
        :type: str
        """
        self._source = source

    @property
    def name(self):
        """
        Gets the name of this MonitoredResourceCredential.
        The name of the credential, within the context of the source.


        :return: The name of this MonitoredResourceCredential.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MonitoredResourceCredential.
        The name of the credential, within the context of the source.


        :param name: The name of this MonitoredResourceCredential.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this MonitoredResourceCredential.
        The type of the credential ( ex. JMXCreds,DBCreds).


        :return: The type of this MonitoredResourceCredential.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MonitoredResourceCredential.
        The type of the credential ( ex. JMXCreds,DBCreds).


        :param type: The type of this MonitoredResourceCredential.
        :type: str
        """
        self._type = type

    @property
    def description(self):
        """
        Gets the description of this MonitoredResourceCredential.
        The user-specified textual description of the credential.


        :return: The description of this MonitoredResourceCredential.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MonitoredResourceCredential.
        The user-specified textual description of the credential.


        :param description: The description of this MonitoredResourceCredential.
        :type: str
        """
        self._description = description

    @property
    def credential_type(self):
        """
        Gets the credential_type of this MonitoredResourceCredential.
        Type of credentials specified in the credentials element. Three possible values - EXISTING, PLAINTEXT and ENCRYPTED. * EXISTING  - Credential is already stored in agent and only credential name need to be passed for existing credential. * PLAINTEXT - The credential properties will have credentials in plain text format. * ENCRYPTED - The credential properties will have credentials stored in vault in encrypted format using KMS client which uses master key for encryption. The same master key will be used to decrypt the credentials before passing on to the management agent.

        Allowed values for this property are: "EXISTING", "PLAINTEXT", "ENCRYPTED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The credential_type of this MonitoredResourceCredential.
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """
        Sets the credential_type of this MonitoredResourceCredential.
        Type of credentials specified in the credentials element. Three possible values - EXISTING, PLAINTEXT and ENCRYPTED. * EXISTING  - Credential is already stored in agent and only credential name need to be passed for existing credential. * PLAINTEXT - The credential properties will have credentials in plain text format. * ENCRYPTED - The credential properties will have credentials stored in vault in encrypted format using KMS client which uses master key for encryption. The same master key will be used to decrypt the credentials before passing on to the management agent.


        :param credential_type: The credential_type of this MonitoredResourceCredential.
        :type: str
        """
        allowed_values = ["EXISTING", "PLAINTEXT", "ENCRYPTED"]
        if not value_allowed_none_or_none_sentinel(credential_type, allowed_values):
            credential_type = 'UNKNOWN_ENUM_VALUE'
        self._credential_type = credential_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
