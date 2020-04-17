# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwareSource(object):
    """
    A software source contains a collection of packages
    """

    #: A constant which can be used with the arch_type property of a SoftwareSource.
    #: This constant has a value of "IA_32"
    ARCH_TYPE_IA_32 = "IA_32"

    #: A constant which can be used with the arch_type property of a SoftwareSource.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a SoftwareSource.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a SoftwareSource.
    #: This constant has a value of "SPARC"
    ARCH_TYPE_SPARC = "SPARC"

    #: A constant which can be used with the arch_type property of a SoftwareSource.
    #: This constant has a value of "AMD64_DEBIAN"
    ARCH_TYPE_AMD64_DEBIAN = "AMD64_DEBIAN"

    #: A constant which can be used with the checksum_type property of a SoftwareSource.
    #: This constant has a value of "SHA1"
    CHECKSUM_TYPE_SHA1 = "SHA1"

    #: A constant which can be used with the checksum_type property of a SoftwareSource.
    #: This constant has a value of "SHA256"
    CHECKSUM_TYPE_SHA256 = "SHA256"

    #: A constant which can be used with the checksum_type property of a SoftwareSource.
    #: This constant has a value of "SHA384"
    CHECKSUM_TYPE_SHA384 = "SHA384"

    #: A constant which can be used with the checksum_type property of a SoftwareSource.
    #: This constant has a value of "SHA512"
    CHECKSUM_TYPE_SHA512 = "SHA512"

    #: A constant which can be used with the status property of a SoftwareSource.
    #: This constant has a value of "NORMAL"
    STATUS_NORMAL = "NORMAL"

    #: A constant which can be used with the status property of a SoftwareSource.
    #: This constant has a value of "UNREACHABLE"
    STATUS_UNREACHABLE = "UNREACHABLE"

    #: A constant which can be used with the status property of a SoftwareSource.
    #: This constant has a value of "ERROR"
    STATUS_ERROR = "ERROR"

    #: A constant which can be used with the status property of a SoftwareSource.
    #: This constant has a value of "WARNING"
    STATUS_WARNING = "WARNING"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSource.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwareSource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SoftwareSource.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SoftwareSource.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this SoftwareSource.
        :type display_name: str

        :param description:
            The value to assign to the description property of this SoftwareSource.
        :type description: str

        :param repo_type:
            The value to assign to the repo_type property of this SoftwareSource.
        :type repo_type: str

        :param arch_type:
            The value to assign to the arch_type property of this SoftwareSource.
            Allowed values for this property are: "IA_32", "X86_64", "AARCH64", "SPARC", "AMD64_DEBIAN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type arch_type: str

        :param url:
            The value to assign to the url property of this SoftwareSource.
        :type url: str

        :param parent_id:
            The value to assign to the parent_id property of this SoftwareSource.
        :type parent_id: str

        :param parent_name:
            The value to assign to the parent_name property of this SoftwareSource.
        :type parent_name: str

        :param checksum_type:
            The value to assign to the checksum_type property of this SoftwareSource.
            Allowed values for this property are: "SHA1", "SHA256", "SHA384", "SHA512", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type checksum_type: str

        :param maintainer_name:
            The value to assign to the maintainer_name property of this SoftwareSource.
        :type maintainer_name: str

        :param maintainer_email:
            The value to assign to the maintainer_email property of this SoftwareSource.
        :type maintainer_email: str

        :param maintainer_phone:
            The value to assign to the maintainer_phone property of this SoftwareSource.
        :type maintainer_phone: str

        :param gpg_key_url:
            The value to assign to the gpg_key_url property of this SoftwareSource.
        :type gpg_key_url: str

        :param gpg_key_id:
            The value to assign to the gpg_key_id property of this SoftwareSource.
        :type gpg_key_id: str

        :param gpg_key_fingerprint:
            The value to assign to the gpg_key_fingerprint property of this SoftwareSource.
        :type gpg_key_fingerprint: str

        :param status:
            The value to assign to the status property of this SoftwareSource.
            Allowed values for this property are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SoftwareSource.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param packages:
            The value to assign to the packages property of this SoftwareSource.
        :type packages: int

        :param associated_managed_instances:
            The value to assign to the associated_managed_instances property of this SoftwareSource.
        :type associated_managed_instances: list[Id]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SoftwareSource.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SoftwareSource.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'repo_type': 'str',
            'arch_type': 'str',
            'url': 'str',
            'parent_id': 'str',
            'parent_name': 'str',
            'checksum_type': 'str',
            'maintainer_name': 'str',
            'maintainer_email': 'str',
            'maintainer_phone': 'str',
            'gpg_key_url': 'str',
            'gpg_key_id': 'str',
            'gpg_key_fingerprint': 'str',
            'status': 'str',
            'lifecycle_state': 'str',
            'packages': 'int',
            'associated_managed_instances': 'list[Id]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'repo_type': 'repoType',
            'arch_type': 'archType',
            'url': 'url',
            'parent_id': 'parentId',
            'parent_name': 'parentName',
            'checksum_type': 'checksumType',
            'maintainer_name': 'maintainerName',
            'maintainer_email': 'maintainerEmail',
            'maintainer_phone': 'maintainerPhone',
            'gpg_key_url': 'gpgKeyUrl',
            'gpg_key_id': 'gpgKeyId',
            'gpg_key_fingerprint': 'gpgKeyFingerprint',
            'status': 'status',
            'lifecycle_state': 'lifecycleState',
            'packages': 'packages',
            'associated_managed_instances': 'associatedManagedInstances',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._repo_type = None
        self._arch_type = None
        self._url = None
        self._parent_id = None
        self._parent_name = None
        self._checksum_type = None
        self._maintainer_name = None
        self._maintainer_email = None
        self._maintainer_phone = None
        self._gpg_key_url = None
        self._gpg_key_id = None
        self._gpg_key_fingerprint = None
        self._status = None
        self._lifecycle_state = None
        self._packages = None
        self._associated_managed_instances = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SoftwareSource.
        OCID for the Software Source


        :return: The id of this SoftwareSource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SoftwareSource.
        OCID for the Software Source


        :param id: The id of this SoftwareSource.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SoftwareSource.
        OCID for the Compartment


        :return: The compartment_id of this SoftwareSource.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SoftwareSource.
        OCID for the Compartment


        :param compartment_id: The compartment_id of this SoftwareSource.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SoftwareSource.
        User friendly name for the software source


        :return: The display_name of this SoftwareSource.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SoftwareSource.
        User friendly name for the software source


        :param display_name: The display_name of this SoftwareSource.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this SoftwareSource.
        Information specified by the user about the software source


        :return: The description of this SoftwareSource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SoftwareSource.
        Information specified by the user about the software source


        :param description: The description of this SoftwareSource.
        :type: str
        """
        self._description = description

    @property
    def repo_type(self):
        """
        **[Required]** Gets the repo_type of this SoftwareSource.
        Type of the Software Source


        :return: The repo_type of this SoftwareSource.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        """
        Sets the repo_type of this SoftwareSource.
        Type of the Software Source


        :param repo_type: The repo_type of this SoftwareSource.
        :type: str
        """
        self._repo_type = repo_type

    @property
    def arch_type(self):
        """
        Gets the arch_type of this SoftwareSource.
        The architecture type supported by the Software Source

        Allowed values for this property are: "IA_32", "X86_64", "AARCH64", "SPARC", "AMD64_DEBIAN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The arch_type of this SoftwareSource.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this SoftwareSource.
        The architecture type supported by the Software Source


        :param arch_type: The arch_type of this SoftwareSource.
        :type: str
        """
        allowed_values = ["IA_32", "X86_64", "AARCH64", "SPARC", "AMD64_DEBIAN"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            arch_type = 'UNKNOWN_ENUM_VALUE'
        self._arch_type = arch_type

    @property
    def url(self):
        """
        **[Required]** Gets the url of this SoftwareSource.
        URL for the repostiory


        :return: The url of this SoftwareSource.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this SoftwareSource.
        URL for the repostiory


        :param url: The url of this SoftwareSource.
        :type: str
        """
        self._url = url

    @property
    def parent_id(self):
        """
        Gets the parent_id of this SoftwareSource.
        OCID for the parent software source, if there is one


        :return: The parent_id of this SoftwareSource.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this SoftwareSource.
        OCID for the parent software source, if there is one


        :param parent_id: The parent_id of this SoftwareSource.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def parent_name(self):
        """
        Gets the parent_name of this SoftwareSource.
        Display name the parent software source, if there is one


        :return: The parent_name of this SoftwareSource.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """
        Sets the parent_name of this SoftwareSource.
        Display name the parent software source, if there is one


        :param parent_name: The parent_name of this SoftwareSource.
        :type: str
        """
        self._parent_name = parent_name

    @property
    def checksum_type(self):
        """
        Gets the checksum_type of this SoftwareSource.
        The yum repository checksum type used by this software source

        Allowed values for this property are: "SHA1", "SHA256", "SHA384", "SHA512", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The checksum_type of this SoftwareSource.
        :rtype: str
        """
        return self._checksum_type

    @checksum_type.setter
    def checksum_type(self, checksum_type):
        """
        Sets the checksum_type of this SoftwareSource.
        The yum repository checksum type used by this software source


        :param checksum_type: The checksum_type of this SoftwareSource.
        :type: str
        """
        allowed_values = ["SHA1", "SHA256", "SHA384", "SHA512"]
        if not value_allowed_none_or_none_sentinel(checksum_type, allowed_values):
            checksum_type = 'UNKNOWN_ENUM_VALUE'
        self._checksum_type = checksum_type

    @property
    def maintainer_name(self):
        """
        Gets the maintainer_name of this SoftwareSource.
        Name of the person maintaining this software source


        :return: The maintainer_name of this SoftwareSource.
        :rtype: str
        """
        return self._maintainer_name

    @maintainer_name.setter
    def maintainer_name(self, maintainer_name):
        """
        Sets the maintainer_name of this SoftwareSource.
        Name of the person maintaining this software source


        :param maintainer_name: The maintainer_name of this SoftwareSource.
        :type: str
        """
        self._maintainer_name = maintainer_name

    @property
    def maintainer_email(self):
        """
        Gets the maintainer_email of this SoftwareSource.
        Email address of the person maintaining this software source


        :return: The maintainer_email of this SoftwareSource.
        :rtype: str
        """
        return self._maintainer_email

    @maintainer_email.setter
    def maintainer_email(self, maintainer_email):
        """
        Sets the maintainer_email of this SoftwareSource.
        Email address of the person maintaining this software source


        :param maintainer_email: The maintainer_email of this SoftwareSource.
        :type: str
        """
        self._maintainer_email = maintainer_email

    @property
    def maintainer_phone(self):
        """
        Gets the maintainer_phone of this SoftwareSource.
        Phone number of the person maintaining this software source


        :return: The maintainer_phone of this SoftwareSource.
        :rtype: str
        """
        return self._maintainer_phone

    @maintainer_phone.setter
    def maintainer_phone(self, maintainer_phone):
        """
        Sets the maintainer_phone of this SoftwareSource.
        Phone number of the person maintaining this software source


        :param maintainer_phone: The maintainer_phone of this SoftwareSource.
        :type: str
        """
        self._maintainer_phone = maintainer_phone

    @property
    def gpg_key_url(self):
        """
        Gets the gpg_key_url of this SoftwareSource.
        URL of the GPG key for this software source


        :return: The gpg_key_url of this SoftwareSource.
        :rtype: str
        """
        return self._gpg_key_url

    @gpg_key_url.setter
    def gpg_key_url(self, gpg_key_url):
        """
        Sets the gpg_key_url of this SoftwareSource.
        URL of the GPG key for this software source


        :param gpg_key_url: The gpg_key_url of this SoftwareSource.
        :type: str
        """
        self._gpg_key_url = gpg_key_url

    @property
    def gpg_key_id(self):
        """
        Gets the gpg_key_id of this SoftwareSource.
        ID of the GPG key for this software source


        :return: The gpg_key_id of this SoftwareSource.
        :rtype: str
        """
        return self._gpg_key_id

    @gpg_key_id.setter
    def gpg_key_id(self, gpg_key_id):
        """
        Sets the gpg_key_id of this SoftwareSource.
        ID of the GPG key for this software source


        :param gpg_key_id: The gpg_key_id of this SoftwareSource.
        :type: str
        """
        self._gpg_key_id = gpg_key_id

    @property
    def gpg_key_fingerprint(self):
        """
        Gets the gpg_key_fingerprint of this SoftwareSource.
        Fingerprint of the GPG key for this software source


        :return: The gpg_key_fingerprint of this SoftwareSource.
        :rtype: str
        """
        return self._gpg_key_fingerprint

    @gpg_key_fingerprint.setter
    def gpg_key_fingerprint(self, gpg_key_fingerprint):
        """
        Sets the gpg_key_fingerprint of this SoftwareSource.
        Fingerprint of the GPG key for this software source


        :param gpg_key_fingerprint: The gpg_key_fingerprint of this SoftwareSource.
        :type: str
        """
        self._gpg_key_fingerprint = gpg_key_fingerprint

    @property
    def status(self):
        """
        Gets the status of this SoftwareSource.
        status of the software source.

        Allowed values for this property are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this SoftwareSource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SoftwareSource.
        status of the software source.


        :param status: The status of this SoftwareSource.
        :type: str
        """
        allowed_values = ["NORMAL", "UNREACHABLE", "ERROR", "WARNING"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SoftwareSource.
        The current state of the Software Source.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SoftwareSource.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SoftwareSource.
        The current state of the Software Source.


        :param lifecycle_state: The lifecycle_state of this SoftwareSource.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def packages(self):
        """
        Gets the packages of this SoftwareSource.
        Number of packages


        :return: The packages of this SoftwareSource.
        :rtype: int
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """
        Sets the packages of this SoftwareSource.
        Number of packages


        :param packages: The packages of this SoftwareSource.
        :type: int
        """
        self._packages = packages

    @property
    def associated_managed_instances(self):
        """
        Gets the associated_managed_instances of this SoftwareSource.
        list of the Managed Instances associated with this Software Sources


        :return: The associated_managed_instances of this SoftwareSource.
        :rtype: list[Id]
        """
        return self._associated_managed_instances

    @associated_managed_instances.setter
    def associated_managed_instances(self, associated_managed_instances):
        """
        Sets the associated_managed_instances of this SoftwareSource.
        list of the Managed Instances associated with this Software Sources


        :param associated_managed_instances: The associated_managed_instances of this SoftwareSource.
        :type: list[Id]
        """
        self._associated_managed_instances = associated_managed_instances

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SoftwareSource.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this SoftwareSource.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SoftwareSource.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this SoftwareSource.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SoftwareSource.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this SoftwareSource.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SoftwareSource.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this SoftwareSource.
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
