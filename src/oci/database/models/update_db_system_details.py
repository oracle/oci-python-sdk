# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDbSystemDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDbSystemDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this UpdateDbSystemDetails.
        :type cpu_core_count: int

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this UpdateDbSystemDetails.
        :type data_storage_size_in_gbs: int

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
            'ssh_public_keys': 'list[str]',
            'version': 'PatchDetails'
        }

        self.attribute_map = {
            'cpu_core_count': 'cpuCoreCount',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'ssh_public_keys': 'sshPublicKeys',
            'version': 'version'
        }

        self._cpu_core_count = None
        self._data_storage_size_in_gbs = None
        self._ssh_public_keys = None
        self._version = None

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this UpdateDbSystemDetails.
        The number of CPU Cores to be set on the DB System. Applicable only for non-VM based DB systems.


        :return: The cpu_core_count of this UpdateDbSystemDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this UpdateDbSystemDetails.
        The number of CPU Cores to be set on the DB System. Applicable only for non-VM based DB systems.


        :param cpu_core_count: The cpu_core_count of this UpdateDbSystemDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this UpdateDbSystemDetails.
        Size, in GBs, to which the currently attached storage needs to be scaled up to for VM based DB system. This must be greater than current storage size. Note that the total storage size attached will be more than what is requested, to account for REDO/RECO space and software volume.


        :return: The data_storage_size_in_gbs of this UpdateDbSystemDetails.
        :rtype: int
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this UpdateDbSystemDetails.
        Size, in GBs, to which the currently attached storage needs to be scaled up to for VM based DB system. This must be greater than current storage size. Note that the total storage size attached will be more than what is requested, to account for REDO/RECO space and software volume.


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this UpdateDbSystemDetails.
        :type: int
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def ssh_public_keys(self):
        """
        Gets the ssh_public_keys of this UpdateDbSystemDetails.
        The public key portion of the key pair to use for SSH access to the DB System. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.


        :return: The ssh_public_keys of this UpdateDbSystemDetails.
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """
        Sets the ssh_public_keys of this UpdateDbSystemDetails.
        The public key portion of the key pair to use for SSH access to the DB System. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.


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
