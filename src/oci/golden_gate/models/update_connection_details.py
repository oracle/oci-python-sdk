# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConnectionDetails(object):
    """
    The information to update a Connection.
    """

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "GOLDENGATE"
    CONNECTION_TYPE_GOLDENGATE = "GOLDENGATE"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "KAFKA"
    CONNECTION_TYPE_KAFKA = "KAFKA"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "MYSQL"
    CONNECTION_TYPE_MYSQL = "MYSQL"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "OCI_OBJECT_STORAGE"
    CONNECTION_TYPE_OCI_OBJECT_STORAGE = "OCI_OBJECT_STORAGE"

    #: A constant which can be used with the connection_type property of a UpdateConnectionDetails.
    #: This constant has a value of "ORACLE"
    CONNECTION_TYPE_ORACLE = "ORACLE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConnectionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.golden_gate.models.UpdateOracleConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateOciObjectStorageConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateMysqlConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateKafkaConnectionDetails`
        * :class:`~oci.golden_gate.models.UpdateGoldenGateConnectionDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this UpdateConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateConnectionDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this UpdateConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateConnectionDetails.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'nsg_ids': 'nsgIds'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectionType']

        if type == 'ORACLE':
            return 'UpdateOracleConnectionDetails'

        if type == 'OCI_OBJECT_STORAGE':
            return 'UpdateOciObjectStorageConnectionDetails'

        if type == 'MYSQL':
            return 'UpdateMysqlConnectionDetails'

        if type == 'KAFKA':
            return 'UpdateKafkaConnectionDetails'

        if type == 'GOLDENGATE':
            return 'UpdateGoldenGateConnectionDetails'
        else:
            return 'UpdateConnectionDetails'

    @property
    def connection_type(self):
        """
        Gets the connection_type of this UpdateConnectionDetails.
        The connection type.

        Allowed values for this property are: "GOLDENGATE", "KAFKA", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE"


        :return: The connection_type of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """
        Sets the connection_type of this UpdateConnectionDetails.
        The connection type.


        :param connection_type: The connection_type of this UpdateConnectionDetails.
        :type: str
        """
        allowed_values = ["GOLDENGATE", "KAFKA", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(connection_type, allowed_values):
            raise ValueError(
                "Invalid value for `connection_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._connection_type = connection_type

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateConnectionDetails.
        An object's Display Name.


        :return: The display_name of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateConnectionDetails.
        An object's Display Name.


        :param display_name: The display_name of this UpdateConnectionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateConnectionDetails.
        Metadata about this specific object.


        :return: The description of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateConnectionDetails.
        Metadata about this specific object.


        :param description: The description of this UpdateConnectionDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateConnectionDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateConnectionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateConnectionDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateConnectionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateConnectionDetails.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateConnectionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateConnectionDetails.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateConnectionDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def vault_id(self):
        """
        Gets the vault_id of this UpdateConnectionDetails.
        The `OCID`__ of the customer vault being
        referenced.
        If provided, this will reference a vault which the customer will be required to ensure
        the policies are established to permit the GoldenGate Service to manage secrets contained
        within this vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vault_id of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this UpdateConnectionDetails.
        The `OCID`__ of the customer vault being
        referenced.
        If provided, this will reference a vault which the customer will be required to ensure
        the policies are established to permit the GoldenGate Service to manage secrets contained
        within this vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vault_id: The vault_id of this UpdateConnectionDetails.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def key_id(self):
        """
        Gets the key_id of this UpdateConnectionDetails.
        The `OCID`__ of the customer \"Master\" key being
        referenced.
        If provided, this will reference a key which the customer will be required to ensure
        the policies are established to permit the GoldenGate Service to utilize this key to
        manage secrets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_id of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this UpdateConnectionDetails.
        The `OCID`__ of the customer \"Master\" key being
        referenced.
        If provided, this will reference a key which the customer will be required to ensure
        the policies are established to permit the GoldenGate Service to utilize this key to
        manage secrets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_id: The key_id of this UpdateConnectionDetails.
        :type: str
        """
        self._key_id = key_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateConnectionDetails.
        An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.


        :return: The nsg_ids of this UpdateConnectionDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateConnectionDetails.
        An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.


        :param nsg_ids: The nsg_ids of this UpdateConnectionDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
