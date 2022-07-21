# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBdsInstanceDetails(object):
    """
    The information about the new cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBdsInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateBdsInstanceDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateBdsInstanceDetails.
        :type display_name: str

        :param cluster_version:
            The value to assign to the cluster_version property of this CreateBdsInstanceDetails.
        :type cluster_version: str

        :param cluster_public_key:
            The value to assign to the cluster_public_key property of this CreateBdsInstanceDetails.
        :type cluster_public_key: str

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this CreateBdsInstanceDetails.
        :type cluster_admin_password: str

        :param is_high_availability:
            The value to assign to the is_high_availability property of this CreateBdsInstanceDetails.
        :type is_high_availability: bool

        :param is_secure:
            The value to assign to the is_secure property of this CreateBdsInstanceDetails.
        :type is_secure: bool

        :param network_config:
            The value to assign to the network_config property of this CreateBdsInstanceDetails.
        :type network_config: oci.bds.models.NetworkConfig

        :param bootstrap_script_url:
            The value to assign to the bootstrap_script_url property of this CreateBdsInstanceDetails.
        :type bootstrap_script_url: str

        :param nodes:
            The value to assign to the nodes property of this CreateBdsInstanceDetails.
        :type nodes: list[oci.bds.models.CreateNodeDetails]

        :param kerberos_realm_name:
            The value to assign to the kerberos_realm_name property of this CreateBdsInstanceDetails.
        :type kerberos_realm_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBdsInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBdsInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateBdsInstanceDetails.
        :type kms_key_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'cluster_version': 'str',
            'cluster_public_key': 'str',
            'cluster_admin_password': 'str',
            'is_high_availability': 'bool',
            'is_secure': 'bool',
            'network_config': 'NetworkConfig',
            'bootstrap_script_url': 'str',
            'nodes': 'list[CreateNodeDetails]',
            'kerberos_realm_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'kms_key_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'cluster_version': 'clusterVersion',
            'cluster_public_key': 'clusterPublicKey',
            'cluster_admin_password': 'clusterAdminPassword',
            'is_high_availability': 'isHighAvailability',
            'is_secure': 'isSecure',
            'network_config': 'networkConfig',
            'bootstrap_script_url': 'bootstrapScriptUrl',
            'nodes': 'nodes',
            'kerberos_realm_name': 'kerberosRealmName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'kms_key_id': 'kmsKeyId'
        }

        self._compartment_id = None
        self._display_name = None
        self._cluster_version = None
        self._cluster_public_key = None
        self._cluster_admin_password = None
        self._is_high_availability = None
        self._is_secure = None
        self._network_config = None
        self._bootstrap_script_url = None
        self._nodes = None
        self._kerberos_realm_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._kms_key_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateBdsInstanceDetails.
        The OCID of the compartment.


        :return: The compartment_id of this CreateBdsInstanceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateBdsInstanceDetails.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this CreateBdsInstanceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateBdsInstanceDetails.
        Name of the Big Data Service cluster.


        :return: The display_name of this CreateBdsInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateBdsInstanceDetails.
        Name of the Big Data Service cluster.


        :param display_name: The display_name of this CreateBdsInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def cluster_version(self):
        """
        **[Required]** Gets the cluster_version of this CreateBdsInstanceDetails.
        Version of the Hadoop distribution.


        :return: The cluster_version of this CreateBdsInstanceDetails.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        """
        Sets the cluster_version of this CreateBdsInstanceDetails.
        Version of the Hadoop distribution.


        :param cluster_version: The cluster_version of this CreateBdsInstanceDetails.
        :type: str
        """
        self._cluster_version = cluster_version

    @property
    def cluster_public_key(self):
        """
        **[Required]** Gets the cluster_public_key of this CreateBdsInstanceDetails.
        The SSH public key used to authenticate the cluster connection.


        :return: The cluster_public_key of this CreateBdsInstanceDetails.
        :rtype: str
        """
        return self._cluster_public_key

    @cluster_public_key.setter
    def cluster_public_key(self, cluster_public_key):
        """
        Sets the cluster_public_key of this CreateBdsInstanceDetails.
        The SSH public key used to authenticate the cluster connection.


        :param cluster_public_key: The cluster_public_key of this CreateBdsInstanceDetails.
        :type: str
        """
        self._cluster_public_key = cluster_public_key

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this CreateBdsInstanceDetails.
        Base-64 encoded password for the cluster (and Cloudera Manager) admin user.


        :return: The cluster_admin_password of this CreateBdsInstanceDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this CreateBdsInstanceDetails.
        Base-64 encoded password for the cluster (and Cloudera Manager) admin user.


        :param cluster_admin_password: The cluster_admin_password of this CreateBdsInstanceDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def is_high_availability(self):
        """
        **[Required]** Gets the is_high_availability of this CreateBdsInstanceDetails.
        Boolean flag specifying whether or not the cluster is highly available (HA).


        :return: The is_high_availability of this CreateBdsInstanceDetails.
        :rtype: bool
        """
        return self._is_high_availability

    @is_high_availability.setter
    def is_high_availability(self, is_high_availability):
        """
        Sets the is_high_availability of this CreateBdsInstanceDetails.
        Boolean flag specifying whether or not the cluster is highly available (HA).


        :param is_high_availability: The is_high_availability of this CreateBdsInstanceDetails.
        :type: bool
        """
        self._is_high_availability = is_high_availability

    @property
    def is_secure(self):
        """
        **[Required]** Gets the is_secure of this CreateBdsInstanceDetails.
        Boolean flag specifying whether or not the cluster should be set up as secure.


        :return: The is_secure of this CreateBdsInstanceDetails.
        :rtype: bool
        """
        return self._is_secure

    @is_secure.setter
    def is_secure(self, is_secure):
        """
        Sets the is_secure of this CreateBdsInstanceDetails.
        Boolean flag specifying whether or not the cluster should be set up as secure.


        :param is_secure: The is_secure of this CreateBdsInstanceDetails.
        :type: bool
        """
        self._is_secure = is_secure

    @property
    def network_config(self):
        """
        Gets the network_config of this CreateBdsInstanceDetails.

        :return: The network_config of this CreateBdsInstanceDetails.
        :rtype: oci.bds.models.NetworkConfig
        """
        return self._network_config

    @network_config.setter
    def network_config(self, network_config):
        """
        Sets the network_config of this CreateBdsInstanceDetails.

        :param network_config: The network_config of this CreateBdsInstanceDetails.
        :type: oci.bds.models.NetworkConfig
        """
        self._network_config = network_config

    @property
    def bootstrap_script_url(self):
        """
        Gets the bootstrap_script_url of this CreateBdsInstanceDetails.
        Pre-authenticated URL of the script in Object Store that is downloaded and executed.


        :return: The bootstrap_script_url of this CreateBdsInstanceDetails.
        :rtype: str
        """
        return self._bootstrap_script_url

    @bootstrap_script_url.setter
    def bootstrap_script_url(self, bootstrap_script_url):
        """
        Sets the bootstrap_script_url of this CreateBdsInstanceDetails.
        Pre-authenticated URL of the script in Object Store that is downloaded and executed.


        :param bootstrap_script_url: The bootstrap_script_url of this CreateBdsInstanceDetails.
        :type: str
        """
        self._bootstrap_script_url = bootstrap_script_url

    @property
    def nodes(self):
        """
        **[Required]** Gets the nodes of this CreateBdsInstanceDetails.
        The list of nodes in the Big Data Service cluster.


        :return: The nodes of this CreateBdsInstanceDetails.
        :rtype: list[oci.bds.models.CreateNodeDetails]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this CreateBdsInstanceDetails.
        The list of nodes in the Big Data Service cluster.


        :param nodes: The nodes of this CreateBdsInstanceDetails.
        :type: list[oci.bds.models.CreateNodeDetails]
        """
        self._nodes = nodes

    @property
    def kerberos_realm_name(self):
        """
        Gets the kerberos_realm_name of this CreateBdsInstanceDetails.
        The user-defined kerberos realm name.


        :return: The kerberos_realm_name of this CreateBdsInstanceDetails.
        :rtype: str
        """
        return self._kerberos_realm_name

    @kerberos_realm_name.setter
    def kerberos_realm_name(self, kerberos_realm_name):
        """
        Sets the kerberos_realm_name of this CreateBdsInstanceDetails.
        The user-defined kerberos realm name.


        :param kerberos_realm_name: The kerberos_realm_name of this CreateBdsInstanceDetails.
        :type: str
        """
        self._kerberos_realm_name = kerberos_realm_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateBdsInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only. For example, `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateBdsInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateBdsInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only. For example, `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateBdsInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateBdsInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example, `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateBdsInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateBdsInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example, `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateBdsInstanceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this CreateBdsInstanceDetails.
        The OCID of the Key Management master encryption key.


        :return: The kms_key_id of this CreateBdsInstanceDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this CreateBdsInstanceDetails.
        The OCID of the Key Management master encryption key.


        :param kms_key_id: The kms_key_id of this CreateBdsInstanceDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
