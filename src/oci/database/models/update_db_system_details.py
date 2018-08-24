# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDbSystemDetails(object):
    """
    Describes the parameters for updating the DB system.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDbSystemDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this UpdateDbSystemDetails.
        :type cpu_core_count: int

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this UpdateDbSystemDetails.
        :type data_storage_size_in_gbs: int

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDbSystemDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDbSystemDetails.
        :type freeform_tags: dict(str, str)

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this UpdateDbSystemDetails.
        :type ssh_public_keys: list[str]

        :param version:
            The value to assign to the version property of this UpdateDbSystemDetails.
        :type version: PatchDetails

        """
        self.swagger_types = {
            'cpu_core_count': 'int',
            'data_storage_size_in_gbs': 'int',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'ssh_public_keys': 'list[str]',
            'version': 'PatchDetails'
        }

        self.attribute_map = {
            'cpu_core_count': 'cpuCoreCount',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'ssh_public_keys': 'sshPublicKeys',
            'version': 'version'
        }

        self._cpu_core_count = None
        self._data_storage_size_in_gbs = None
        self._defined_tags = None
        self._freeform_tags = None
        self._ssh_public_keys = None
        self._version = None

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this UpdateDbSystemDetails.
        The new number of CPU cores to set for the DB system. Not applicable for virtual machine DB systems.


        :return: The cpu_core_count of this UpdateDbSystemDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this UpdateDbSystemDetails.
        The new number of CPU cores to set for the DB system. Not applicable for virtual machine DB systems.


        :param cpu_core_count: The cpu_core_count of this UpdateDbSystemDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this UpdateDbSystemDetails.
        The size, in gigabytes, to scale the attached storage up to for this virtual machine DB system. This value must be greater than current storage size. Note that the resulting total storage size attached will be greater than the amount requested to allow for REDO/RECO space and software volume. Applies only to virtual machine DB systems.


        :return: The data_storage_size_in_gbs of this UpdateDbSystemDetails.
        :rtype: int
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this UpdateDbSystemDetails.
        The size, in gigabytes, to scale the attached storage up to for this virtual machine DB system. This value must be greater than current storage size. Note that the resulting total storage size attached will be greater than the amount requested to allow for REDO/RECO space and software volume. Applies only to virtual machine DB systems.


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this UpdateDbSystemDetails.
        :type: int
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateDbSystemDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDbSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateDbSystemDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDbSystemDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateDbSystemDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDbSystemDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateDbSystemDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def ssh_public_keys(self):
        """
        Gets the ssh_public_keys of this UpdateDbSystemDetails.
        The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.


        :return: The ssh_public_keys of this UpdateDbSystemDetails.
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """
        Sets the ssh_public_keys of this UpdateDbSystemDetails.
        The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.


        :param ssh_public_keys: The ssh_public_keys of this UpdateDbSystemDetails.
        :type: list[str]
        """
        self._ssh_public_keys = ssh_public_keys

    @property
    def version(self):
        """
        Gets the version of this UpdateDbSystemDetails.

        :return: The version of this UpdateDbSystemDetails.
        :rtype: PatchDetails
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this UpdateDbSystemDetails.

        :param version: The version of this UpdateDbSystemDetails.
        :type: PatchDetails
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
