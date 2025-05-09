# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180828


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOpensearchClusterDetails(object):
    """
    The configuration to update on an existing OpenSearch cluster. Software version
    and security config are not allowed to be updated at the same time.
    """

    #: A constant which can be used with the security_mode property of a UpdateOpensearchClusterDetails.
    #: This constant has a value of "DISABLED"
    SECURITY_MODE_DISABLED = "DISABLED"

    #: A constant which can be used with the security_mode property of a UpdateOpensearchClusterDetails.
    #: This constant has a value of "PERMISSIVE"
    SECURITY_MODE_PERMISSIVE = "PERMISSIVE"

    #: A constant which can be used with the security_mode property of a UpdateOpensearchClusterDetails.
    #: This constant has a value of "ENFORCING"
    SECURITY_MODE_ENFORCING = "ENFORCING"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOpensearchClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateOpensearchClusterDetails.
        :type display_name: str

        :param software_version:
            The value to assign to the software_version property of this UpdateOpensearchClusterDetails.
        :type software_version: str

        :param security_mode:
            The value to assign to the security_mode property of this UpdateOpensearchClusterDetails.
            Allowed values for this property are: "DISABLED", "PERMISSIVE", "ENFORCING"
        :type security_mode: str

        :param security_master_user_name:
            The value to assign to the security_master_user_name property of this UpdateOpensearchClusterDetails.
        :type security_master_user_name: str

        :param security_master_user_password_hash:
            The value to assign to the security_master_user_password_hash property of this UpdateOpensearchClusterDetails.
        :type security_master_user_password_hash: str

        :param security_saml_config:
            The value to assign to the security_saml_config property of this UpdateOpensearchClusterDetails.
        :type security_saml_config: oci.opensearch.models.SecuritySamlConfig

        :param backup_policy:
            The value to assign to the backup_policy property of this UpdateOpensearchClusterDetails.
        :type backup_policy: oci.opensearch.models.BackupPolicy

        :param reverse_connection_endpoint_customer_ips:
            The value to assign to the reverse_connection_endpoint_customer_ips property of this UpdateOpensearchClusterDetails.
        :type reverse_connection_endpoint_customer_ips: list[str]

        :param outbound_cluster_config:
            The value to assign to the outbound_cluster_config property of this UpdateOpensearchClusterDetails.
        :type outbound_cluster_config: oci.opensearch.models.OutboundClusterConfig

        :param maintenance_details:
            The value to assign to the maintenance_details property of this UpdateOpensearchClusterDetails.
        :type maintenance_details: oci.opensearch.models.UpdateMaintenanceDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOpensearchClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOpensearchClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'software_version': 'str',
            'security_mode': 'str',
            'security_master_user_name': 'str',
            'security_master_user_password_hash': 'str',
            'security_saml_config': 'SecuritySamlConfig',
            'backup_policy': 'BackupPolicy',
            'reverse_connection_endpoint_customer_ips': 'list[str]',
            'outbound_cluster_config': 'OutboundClusterConfig',
            'maintenance_details': 'UpdateMaintenanceDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'software_version': 'softwareVersion',
            'security_mode': 'securityMode',
            'security_master_user_name': 'securityMasterUserName',
            'security_master_user_password_hash': 'securityMasterUserPasswordHash',
            'security_saml_config': 'securitySamlConfig',
            'backup_policy': 'backupPolicy',
            'reverse_connection_endpoint_customer_ips': 'reverseConnectionEndpointCustomerIps',
            'outbound_cluster_config': 'outboundClusterConfig',
            'maintenance_details': 'maintenanceDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._software_version = None
        self._security_mode = None
        self._security_master_user_name = None
        self._security_master_user_password_hash = None
        self._security_saml_config = None
        self._backup_policy = None
        self._reverse_connection_endpoint_customer_ips = None
        self._outbound_cluster_config = None
        self._maintenance_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this UpdateOpensearchClusterDetails.
        The name of the cluster. Avoid entering confidential information.


        :return: The display_name of this UpdateOpensearchClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateOpensearchClusterDetails.
        The name of the cluster. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateOpensearchClusterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def software_version(self):
        """
        Gets the software_version of this UpdateOpensearchClusterDetails.

        :return: The software_version of this UpdateOpensearchClusterDetails.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """
        Sets the software_version of this UpdateOpensearchClusterDetails.

        :param software_version: The software_version of this UpdateOpensearchClusterDetails.
        :type: str
        """
        self._software_version = software_version

    @property
    def security_mode(self):
        """
        Gets the security_mode of this UpdateOpensearchClusterDetails.
        The security mode of the cluster.

        Allowed values for this property are: "DISABLED", "PERMISSIVE", "ENFORCING"


        :return: The security_mode of this UpdateOpensearchClusterDetails.
        :rtype: str
        """
        return self._security_mode

    @security_mode.setter
    def security_mode(self, security_mode):
        """
        Sets the security_mode of this UpdateOpensearchClusterDetails.
        The security mode of the cluster.


        :param security_mode: The security_mode of this UpdateOpensearchClusterDetails.
        :type: str
        """
        allowed_values = ["DISABLED", "PERMISSIVE", "ENFORCING"]
        if not value_allowed_none_or_none_sentinel(security_mode, allowed_values):
            raise ValueError(
                f"Invalid value for `security_mode`, must be None or one of {allowed_values}"
            )
        self._security_mode = security_mode

    @property
    def security_master_user_name(self):
        """
        Gets the security_master_user_name of this UpdateOpensearchClusterDetails.
        The name of the master user that are used to manage security config


        :return: The security_master_user_name of this UpdateOpensearchClusterDetails.
        :rtype: str
        """
        return self._security_master_user_name

    @security_master_user_name.setter
    def security_master_user_name(self, security_master_user_name):
        """
        Sets the security_master_user_name of this UpdateOpensearchClusterDetails.
        The name of the master user that are used to manage security config


        :param security_master_user_name: The security_master_user_name of this UpdateOpensearchClusterDetails.
        :type: str
        """
        self._security_master_user_name = security_master_user_name

    @property
    def security_master_user_password_hash(self):
        """
        Gets the security_master_user_password_hash of this UpdateOpensearchClusterDetails.
        The password hash of the master user that are used to manage security config


        :return: The security_master_user_password_hash of this UpdateOpensearchClusterDetails.
        :rtype: str
        """
        return self._security_master_user_password_hash

    @security_master_user_password_hash.setter
    def security_master_user_password_hash(self, security_master_user_password_hash):
        """
        Sets the security_master_user_password_hash of this UpdateOpensearchClusterDetails.
        The password hash of the master user that are used to manage security config


        :param security_master_user_password_hash: The security_master_user_password_hash of this UpdateOpensearchClusterDetails.
        :type: str
        """
        self._security_master_user_password_hash = security_master_user_password_hash

    @property
    def security_saml_config(self):
        """
        Gets the security_saml_config of this UpdateOpensearchClusterDetails.

        :return: The security_saml_config of this UpdateOpensearchClusterDetails.
        :rtype: oci.opensearch.models.SecuritySamlConfig
        """
        return self._security_saml_config

    @security_saml_config.setter
    def security_saml_config(self, security_saml_config):
        """
        Sets the security_saml_config of this UpdateOpensearchClusterDetails.

        :param security_saml_config: The security_saml_config of this UpdateOpensearchClusterDetails.
        :type: oci.opensearch.models.SecuritySamlConfig
        """
        self._security_saml_config = security_saml_config

    @property
    def backup_policy(self):
        """
        Gets the backup_policy of this UpdateOpensearchClusterDetails.

        :return: The backup_policy of this UpdateOpensearchClusterDetails.
        :rtype: oci.opensearch.models.BackupPolicy
        """
        return self._backup_policy

    @backup_policy.setter
    def backup_policy(self, backup_policy):
        """
        Sets the backup_policy of this UpdateOpensearchClusterDetails.

        :param backup_policy: The backup_policy of this UpdateOpensearchClusterDetails.
        :type: oci.opensearch.models.BackupPolicy
        """
        self._backup_policy = backup_policy

    @property
    def reverse_connection_endpoint_customer_ips(self):
        """
        Gets the reverse_connection_endpoint_customer_ips of this UpdateOpensearchClusterDetails.
        The customer IP addresses of the endpoint in customer VCN


        :return: The reverse_connection_endpoint_customer_ips of this UpdateOpensearchClusterDetails.
        :rtype: list[str]
        """
        return self._reverse_connection_endpoint_customer_ips

    @reverse_connection_endpoint_customer_ips.setter
    def reverse_connection_endpoint_customer_ips(self, reverse_connection_endpoint_customer_ips):
        """
        Sets the reverse_connection_endpoint_customer_ips of this UpdateOpensearchClusterDetails.
        The customer IP addresses of the endpoint in customer VCN


        :param reverse_connection_endpoint_customer_ips: The reverse_connection_endpoint_customer_ips of this UpdateOpensearchClusterDetails.
        :type: list[str]
        """
        self._reverse_connection_endpoint_customer_ips = reverse_connection_endpoint_customer_ips

    @property
    def outbound_cluster_config(self):
        """
        Gets the outbound_cluster_config of this UpdateOpensearchClusterDetails.

        :return: The outbound_cluster_config of this UpdateOpensearchClusterDetails.
        :rtype: oci.opensearch.models.OutboundClusterConfig
        """
        return self._outbound_cluster_config

    @outbound_cluster_config.setter
    def outbound_cluster_config(self, outbound_cluster_config):
        """
        Sets the outbound_cluster_config of this UpdateOpensearchClusterDetails.

        :param outbound_cluster_config: The outbound_cluster_config of this UpdateOpensearchClusterDetails.
        :type: oci.opensearch.models.OutboundClusterConfig
        """
        self._outbound_cluster_config = outbound_cluster_config

    @property
    def maintenance_details(self):
        """
        Gets the maintenance_details of this UpdateOpensearchClusterDetails.

        :return: The maintenance_details of this UpdateOpensearchClusterDetails.
        :rtype: oci.opensearch.models.UpdateMaintenanceDetails
        """
        return self._maintenance_details

    @maintenance_details.setter
    def maintenance_details(self, maintenance_details):
        """
        Sets the maintenance_details of this UpdateOpensearchClusterDetails.

        :param maintenance_details: The maintenance_details of this UpdateOpensearchClusterDetails.
        :type: oci.opensearch.models.UpdateMaintenanceDetails
        """
        self._maintenance_details = maintenance_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateOpensearchClusterDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateOpensearchClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateOpensearchClusterDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateOpensearchClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateOpensearchClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateOpensearchClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateOpensearchClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateOpensearchClusterDetails.
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
