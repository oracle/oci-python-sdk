# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationCreateVnicDetails(object):
    """
    Please see :class:`CreateVnicDetails`
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationCreateVnicDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param assign_public_ip:
            The value to assign to the assign_public_ip property of this InstanceConfigurationCreateVnicDetails.
        :type assign_public_ip: bool

        :param display_name:
            The value to assign to the display_name property of this InstanceConfigurationCreateVnicDetails.
        :type display_name: str

        :param hostname_label:
            The value to assign to the hostname_label property of this InstanceConfigurationCreateVnicDetails.
        :type hostname_label: str

        :param private_ip:
            The value to assign to the private_ip property of this InstanceConfigurationCreateVnicDetails.
        :type private_ip: str

        :param skip_source_dest_check:
            The value to assign to the skip_source_dest_check property of this InstanceConfigurationCreateVnicDetails.
        :type skip_source_dest_check: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this InstanceConfigurationCreateVnicDetails.
        :type subnet_id: str

        """
        self.swagger_types = {
            'assign_public_ip': 'bool',
            'display_name': 'str',
            'hostname_label': 'str',
            'private_ip': 'str',
            'skip_source_dest_check': 'bool',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'assign_public_ip': 'assignPublicIp',
            'display_name': 'displayName',
            'hostname_label': 'hostnameLabel',
            'private_ip': 'privateIp',
            'skip_source_dest_check': 'skipSourceDestCheck',
            'subnet_id': 'subnetId'
        }

        self._assign_public_ip = None
        self._display_name = None
        self._hostname_label = None
        self._private_ip = None
        self._skip_source_dest_check = None
        self._subnet_id = None

    @property
    def assign_public_ip(self):
        """
        Gets the assign_public_ip of this InstanceConfigurationCreateVnicDetails.

        :return: The assign_public_ip of this InstanceConfigurationCreateVnicDetails.
        :rtype: bool
        """
        return self._assign_public_ip

    @assign_public_ip.setter
    def assign_public_ip(self, assign_public_ip):
        """
        Sets the assign_public_ip of this InstanceConfigurationCreateVnicDetails.

        :param assign_public_ip: The assign_public_ip of this InstanceConfigurationCreateVnicDetails.
        :type: bool
        """
        self._assign_public_ip = assign_public_ip

    @property
    def display_name(self):
        """
        Gets the display_name of this InstanceConfigurationCreateVnicDetails.
        A user-friendly name for the VNIC. Does not have to be unique.
        Avoid entering confidential information.


        :return: The display_name of this InstanceConfigurationCreateVnicDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstanceConfigurationCreateVnicDetails.
        A user-friendly name for the VNIC. Does not have to be unique.
        Avoid entering confidential information.


        :param display_name: The display_name of this InstanceConfigurationCreateVnicDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this InstanceConfigurationCreateVnicDetails.

        :return: The hostname_label of this InstanceConfigurationCreateVnicDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this InstanceConfigurationCreateVnicDetails.

        :param hostname_label: The hostname_label of this InstanceConfigurationCreateVnicDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def private_ip(self):
        """
        Gets the private_ip of this InstanceConfigurationCreateVnicDetails.

        :return: The private_ip of this InstanceConfigurationCreateVnicDetails.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this InstanceConfigurationCreateVnicDetails.

        :param private_ip: The private_ip of this InstanceConfigurationCreateVnicDetails.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def skip_source_dest_check(self):
        """
        Gets the skip_source_dest_check of this InstanceConfigurationCreateVnicDetails.

        :return: The skip_source_dest_check of this InstanceConfigurationCreateVnicDetails.
        :rtype: bool
        """
        return self._skip_source_dest_check

    @skip_source_dest_check.setter
    def skip_source_dest_check(self, skip_source_dest_check):
        """
        Sets the skip_source_dest_check of this InstanceConfigurationCreateVnicDetails.

        :param skip_source_dest_check: The skip_source_dest_check of this InstanceConfigurationCreateVnicDetails.
        :type: bool
        """
        self._skip_source_dest_check = skip_source_dest_check

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this InstanceConfigurationCreateVnicDetails.

        :return: The subnet_id of this InstanceConfigurationCreateVnicDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this InstanceConfigurationCreateVnicDetails.

        :param subnet_id: The subnet_id of this InstanceConfigurationCreateVnicDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
