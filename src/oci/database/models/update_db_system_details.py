# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class UpdateDbSystemDetails(object):

    def __init__(self):

        self.swagger_types = {
            'cpu_core_count': 'int',
            'ssh_public_keys': 'list[str]'
        }

        self.attribute_map = {
            'cpu_core_count': 'cpuCoreCount',
            'ssh_public_keys': 'sshPublicKeys'
        }

        self._cpu_core_count = None
        self._ssh_public_keys = None

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this UpdateDbSystemDetails.
        The number of CPU Cores to be set on the DB System


        :return: The cpu_core_count of this UpdateDbSystemDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this UpdateDbSystemDetails.
        The number of CPU Cores to be set on the DB System


        :param cpu_core_count: The cpu_core_count of this UpdateDbSystemDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
