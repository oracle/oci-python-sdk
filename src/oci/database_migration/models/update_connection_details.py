# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConnectionDetails(object):
    """
    Details to update in a Database Connection resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateConnectionDetails.
        :type display_name: str

        :param database_id:
            The value to assign to the database_id property of this UpdateConnectionDetails.
        :type database_id: str

        :param connect_descriptor:
            The value to assign to the connect_descriptor property of this UpdateConnectionDetails.
        :type connect_descriptor: oci.database_migration.models.UpdateConnectDescriptor

        :param certificate_tdn:
            The value to assign to the certificate_tdn property of this UpdateConnectionDetails.
        :type certificate_tdn: str

        :param tls_wallet:
            The value to assign to the tls_wallet property of this UpdateConnectionDetails.
        :type tls_wallet: str

        :param tls_keystore:
            The value to assign to the tls_keystore property of this UpdateConnectionDetails.
        :type tls_keystore: str

        :param ssh_details:
            The value to assign to the ssh_details property of this UpdateConnectionDetails.
        :type ssh_details: oci.database_migration.models.UpdateSshDetails

        :param admin_credentials:
            The value to assign to the admin_credentials property of this UpdateConnectionDetails.
        :type admin_credentials: oci.database_migration.models.UpdateAdminCredentials

        :param private_endpoint:
            The value to assign to the private_endpoint property of this UpdateConnectionDetails.
        :type private_endpoint: oci.database_migration.models.UpdatePrivateEndpoint

        :param vault_details:
            The value to assign to the vault_details property of this UpdateConnectionDetails.
        :type vault_details: oci.database_migration.models.UpdateVaultDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'database_id': 'str',
            'connect_descriptor': 'UpdateConnectDescriptor',
            'certificate_tdn': 'str',
            'tls_wallet': 'str',
            'tls_keystore': 'str',
            'ssh_details': 'UpdateSshDetails',
            'admin_credentials': 'UpdateAdminCredentials',
            'private_endpoint': 'UpdatePrivateEndpoint',
            'vault_details': 'UpdateVaultDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'database_id': 'databaseId',
            'connect_descriptor': 'connectDescriptor',
            'certificate_tdn': 'certificateTdn',
            'tls_wallet': 'tlsWallet',
            'tls_keystore': 'tlsKeystore',
            'ssh_details': 'sshDetails',
            'admin_credentials': 'adminCredentials',
            'private_endpoint': 'privateEndpoint',
            'vault_details': 'vaultDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._database_id = None
        self._connect_descriptor = None
        self._certificate_tdn = None
        self._tls_wallet = None
        self._tls_keystore = None
        self._ssh_details = None
        self._admin_credentials = None
        self._private_endpoint = None
        self._vault_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateConnectionDetails.
        Database Connection display name identifier.


        :return: The display_name of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateConnectionDetails.
        Database Connection display name identifier.


        :param display_name: The display_name of this UpdateConnectionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def database_id(self):
        """
        Gets the database_id of this UpdateConnectionDetails.
        The OCID of the cloud database.


        :return: The database_id of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this UpdateConnectionDetails.
        The OCID of the cloud database.


        :param database_id: The database_id of this UpdateConnectionDetails.
        :type: str
        """
        self._database_id = database_id

    @property
    def connect_descriptor(self):
        """
        Gets the connect_descriptor of this UpdateConnectionDetails.

        :return: The connect_descriptor of this UpdateConnectionDetails.
        :rtype: oci.database_migration.models.UpdateConnectDescriptor
        """
        return self._connect_descriptor

    @connect_descriptor.setter
    def connect_descriptor(self, connect_descriptor):
        """
        Sets the connect_descriptor of this UpdateConnectionDetails.

        :param connect_descriptor: The connect_descriptor of this UpdateConnectionDetails.
        :type: oci.database_migration.models.UpdateConnectDescriptor
        """
        self._connect_descriptor = connect_descriptor

    @property
    def certificate_tdn(self):
        """
        Gets the certificate_tdn of this UpdateConnectionDetails.
        This name is the distinguished name used while creating the certificate on target database. Not required for source container database connections.


        :return: The certificate_tdn of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._certificate_tdn

    @certificate_tdn.setter
    def certificate_tdn(self, certificate_tdn):
        """
        Sets the certificate_tdn of this UpdateConnectionDetails.
        This name is the distinguished name used while creating the certificate on target database. Not required for source container database connections.


        :param certificate_tdn: The certificate_tdn of this UpdateConnectionDetails.
        :type: str
        """
        self._certificate_tdn = certificate_tdn

    @property
    def tls_wallet(self):
        """
        Gets the tls_wallet of this UpdateConnectionDetails.
        cwallet.sso containing containing the TCPS/SSL certificate; base64 encoded String. Not required for source container database connections.


        :return: The tls_wallet of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._tls_wallet

    @tls_wallet.setter
    def tls_wallet(self, tls_wallet):
        """
        Sets the tls_wallet of this UpdateConnectionDetails.
        cwallet.sso containing containing the TCPS/SSL certificate; base64 encoded String. Not required for source container database connections.


        :param tls_wallet: The tls_wallet of this UpdateConnectionDetails.
        :type: str
        """
        self._tls_wallet = tls_wallet

    @property
    def tls_keystore(self):
        """
        Gets the tls_keystore of this UpdateConnectionDetails.
        keystore.jks file contents; base64 encoded String. Not required for source container database connections.


        :return: The tls_keystore of this UpdateConnectionDetails.
        :rtype: str
        """
        return self._tls_keystore

    @tls_keystore.setter
    def tls_keystore(self, tls_keystore):
        """
        Sets the tls_keystore of this UpdateConnectionDetails.
        keystore.jks file contents; base64 encoded String. Not required for source container database connections.


        :param tls_keystore: The tls_keystore of this UpdateConnectionDetails.
        :type: str
        """
        self._tls_keystore = tls_keystore

    @property
    def ssh_details(self):
        """
        Gets the ssh_details of this UpdateConnectionDetails.

        :return: The ssh_details of this UpdateConnectionDetails.
        :rtype: oci.database_migration.models.UpdateSshDetails
        """
        return self._ssh_details

    @ssh_details.setter
    def ssh_details(self, ssh_details):
        """
        Sets the ssh_details of this UpdateConnectionDetails.

        :param ssh_details: The ssh_details of this UpdateConnectionDetails.
        :type: oci.database_migration.models.UpdateSshDetails
        """
        self._ssh_details = ssh_details

    @property
    def admin_credentials(self):
        """
        Gets the admin_credentials of this UpdateConnectionDetails.

        :return: The admin_credentials of this UpdateConnectionDetails.
        :rtype: oci.database_migration.models.UpdateAdminCredentials
        """
        return self._admin_credentials

    @admin_credentials.setter
    def admin_credentials(self, admin_credentials):
        """
        Sets the admin_credentials of this UpdateConnectionDetails.

        :param admin_credentials: The admin_credentials of this UpdateConnectionDetails.
        :type: oci.database_migration.models.UpdateAdminCredentials
        """
        self._admin_credentials = admin_credentials

    @property
    def private_endpoint(self):
        """
        Gets the private_endpoint of this UpdateConnectionDetails.

        :return: The private_endpoint of this UpdateConnectionDetails.
        :rtype: oci.database_migration.models.UpdatePrivateEndpoint
        """
        return self._private_endpoint

    @private_endpoint.setter
    def private_endpoint(self, private_endpoint):
        """
        Sets the private_endpoint of this UpdateConnectionDetails.

        :param private_endpoint: The private_endpoint of this UpdateConnectionDetails.
        :type: oci.database_migration.models.UpdatePrivateEndpoint
        """
        self._private_endpoint = private_endpoint

    @property
    def vault_details(self):
        """
        Gets the vault_details of this UpdateConnectionDetails.

        :return: The vault_details of this UpdateConnectionDetails.
        :rtype: oci.database_migration.models.UpdateVaultDetails
        """
        return self._vault_details

    @vault_details.setter
    def vault_details(self, vault_details):
        """
        Sets the vault_details of this UpdateConnectionDetails.

        :param vault_details: The vault_details of this UpdateConnectionDetails.
        :type: oci.database_migration.models.UpdateVaultDetails
        """
        self._vault_details = vault_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateConnectionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateConnectionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateConnectionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateConnectionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateConnectionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateConnectionDetails.
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
