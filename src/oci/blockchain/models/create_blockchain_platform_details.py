# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBlockchainPlatformDetails(object):
    """
    Blockchain Platform details for creating a new service.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBlockchainPlatformDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateBlockchainPlatformDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateBlockchainPlatformDetails.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this CreateBlockchainPlatformDetails.
        :type description: str

        :param platform_role:
            The value to assign to the platform_role property of this CreateBlockchainPlatformDetails.
        :type platform_role: str

        :param compute_shape:
            The value to assign to the compute_shape property of this CreateBlockchainPlatformDetails.
        :type compute_shape: str

        :param is_byol:
            The value to assign to the is_byol property of this CreateBlockchainPlatformDetails.
        :type is_byol: bool

        :param platform_version:
            The value to assign to the platform_version property of this CreateBlockchainPlatformDetails.
        :type platform_version: str

        :param idcs_access_token:
            The value to assign to the idcs_access_token property of this CreateBlockchainPlatformDetails.
        :type idcs_access_token: str

        :param federated_user_id:
            The value to assign to the federated_user_id property of this CreateBlockchainPlatformDetails.
        :type federated_user_id: str

        :param ca_cert_archive_text:
            The value to assign to the ca_cert_archive_text property of this CreateBlockchainPlatformDetails.
        :type ca_cert_archive_text: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBlockchainPlatformDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBlockchainPlatformDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'platform_role': 'str',
            'compute_shape': 'str',
            'is_byol': 'bool',
            'platform_version': 'str',
            'idcs_access_token': 'str',
            'federated_user_id': 'str',
            'ca_cert_archive_text': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'platform_role': 'platformRole',
            'compute_shape': 'computeShape',
            'is_byol': 'isByol',
            'platform_version': 'platformVersion',
            'idcs_access_token': 'idcsAccessToken',
            'federated_user_id': 'federatedUserId',
            'ca_cert_archive_text': 'caCertArchiveText',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._platform_role = None
        self._compute_shape = None
        self._is_byol = None
        self._platform_version = None
        self._idcs_access_token = None
        self._federated_user_id = None
        self._ca_cert_archive_text = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateBlockchainPlatformDetails.
        Platform Instance Display name, can be renamed


        :return: The display_name of this CreateBlockchainPlatformDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateBlockchainPlatformDetails.
        Platform Instance Display name, can be renamed


        :param display_name: The display_name of this CreateBlockchainPlatformDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateBlockchainPlatformDetails.
        Compartment Identifier


        :return: The compartment_id of this CreateBlockchainPlatformDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateBlockchainPlatformDetails.
        Compartment Identifier


        :param compartment_id: The compartment_id of this CreateBlockchainPlatformDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this CreateBlockchainPlatformDetails.
        Platform Instance Description


        :return: The description of this CreateBlockchainPlatformDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateBlockchainPlatformDetails.
        Platform Instance Description


        :param description: The description of this CreateBlockchainPlatformDetails.
        :type: str
        """
        self._description = description

    @property
    def platform_role(self):
        """
        **[Required]** Gets the platform_role of this CreateBlockchainPlatformDetails.
        Role of platform - founder or participant


        :return: The platform_role of this CreateBlockchainPlatformDetails.
        :rtype: str
        """
        return self._platform_role

    @platform_role.setter
    def platform_role(self, platform_role):
        """
        Sets the platform_role of this CreateBlockchainPlatformDetails.
        Role of platform - founder or participant


        :param platform_role: The platform_role of this CreateBlockchainPlatformDetails.
        :type: str
        """
        self._platform_role = platform_role

    @property
    def compute_shape(self):
        """
        **[Required]** Gets the compute_shape of this CreateBlockchainPlatformDetails.
        Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE


        :return: The compute_shape of this CreateBlockchainPlatformDetails.
        :rtype: str
        """
        return self._compute_shape

    @compute_shape.setter
    def compute_shape(self, compute_shape):
        """
        Sets the compute_shape of this CreateBlockchainPlatformDetails.
        Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE


        :param compute_shape: The compute_shape of this CreateBlockchainPlatformDetails.
        :type: str
        """
        self._compute_shape = compute_shape

    @property
    def is_byol(self):
        """
        Gets the is_byol of this CreateBlockchainPlatformDetails.
        Bring your own license


        :return: The is_byol of this CreateBlockchainPlatformDetails.
        :rtype: bool
        """
        return self._is_byol

    @is_byol.setter
    def is_byol(self, is_byol):
        """
        Sets the is_byol of this CreateBlockchainPlatformDetails.
        Bring your own license


        :param is_byol: The is_byol of this CreateBlockchainPlatformDetails.
        :type: bool
        """
        self._is_byol = is_byol

    @property
    def platform_version(self):
        """
        Gets the platform_version of this CreateBlockchainPlatformDetails.
        Platform version


        :return: The platform_version of this CreateBlockchainPlatformDetails.
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """
        Sets the platform_version of this CreateBlockchainPlatformDetails.
        Platform version


        :param platform_version: The platform_version of this CreateBlockchainPlatformDetails.
        :type: str
        """
        self._platform_version = platform_version

    @property
    def idcs_access_token(self):
        """
        **[Required]** Gets the idcs_access_token of this CreateBlockchainPlatformDetails.
        IDCS access token with Identity Domain Administrator role


        :return: The idcs_access_token of this CreateBlockchainPlatformDetails.
        :rtype: str
        """
        return self._idcs_access_token

    @idcs_access_token.setter
    def idcs_access_token(self, idcs_access_token):
        """
        Sets the idcs_access_token of this CreateBlockchainPlatformDetails.
        IDCS access token with Identity Domain Administrator role


        :param idcs_access_token: The idcs_access_token of this CreateBlockchainPlatformDetails.
        :type: str
        """
        self._idcs_access_token = idcs_access_token

    @property
    def federated_user_id(self):
        """
        Gets the federated_user_id of this CreateBlockchainPlatformDetails.
        Identifier for a federated user


        :return: The federated_user_id of this CreateBlockchainPlatformDetails.
        :rtype: str
        """
        return self._federated_user_id

    @federated_user_id.setter
    def federated_user_id(self, federated_user_id):
        """
        Sets the federated_user_id of this CreateBlockchainPlatformDetails.
        Identifier for a federated user


        :param federated_user_id: The federated_user_id of this CreateBlockchainPlatformDetails.
        :type: str
        """
        self._federated_user_id = federated_user_id

    @property
    def ca_cert_archive_text(self):
        """
        Gets the ca_cert_archive_text of this CreateBlockchainPlatformDetails.
        Base64 encoded text in ASCII character set of a Thirdparty CA Certificates archive file.
        The Archive file is a zip file containing third part CA Certificates,
        the ca key and certificate files used when issuing enrollment certificates
        (ECerts) and transaction certificates (TCerts). The chainfile (if it exists)
        contains the certificate chain which should be trusted for this CA, where
        the 1st in the chain is always the root CA certificate.
        File list in zip file [ca-cert.pem,ca-key.pem,ca-chain.pem(optional)].


        :return: The ca_cert_archive_text of this CreateBlockchainPlatformDetails.
        :rtype: str
        """
        return self._ca_cert_archive_text

    @ca_cert_archive_text.setter
    def ca_cert_archive_text(self, ca_cert_archive_text):
        """
        Sets the ca_cert_archive_text of this CreateBlockchainPlatformDetails.
        Base64 encoded text in ASCII character set of a Thirdparty CA Certificates archive file.
        The Archive file is a zip file containing third part CA Certificates,
        the ca key and certificate files used when issuing enrollment certificates
        (ECerts) and transaction certificates (TCerts). The chainfile (if it exists)
        contains the certificate chain which should be trusted for this CA, where
        the 1st in the chain is always the root CA certificate.
        File list in zip file [ca-cert.pem,ca-key.pem,ca-chain.pem(optional)].


        :param ca_cert_archive_text: The ca_cert_archive_text of this CreateBlockchainPlatformDetails.
        :type: str
        """
        self._ca_cert_archive_text = ca_cert_archive_text

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateBlockchainPlatformDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateBlockchainPlatformDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateBlockchainPlatformDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateBlockchainPlatformDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateBlockchainPlatformDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateBlockchainPlatformDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateBlockchainPlatformDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateBlockchainPlatformDetails.
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
