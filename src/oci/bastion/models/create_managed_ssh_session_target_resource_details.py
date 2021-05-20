# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_session_target_resource_details import CreateSessionTargetResourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateManagedSshSessionTargetResourceDetails(CreateSessionTargetResourceDetails):
    """
    Details about a managed SSH session for a target resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateManagedSshSessionTargetResourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.bastion.models.CreateManagedSshSessionTargetResourceDetails.session_type` attribute
        of this class is ``MANAGED_SSH`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param session_type:
            The value to assign to the session_type property of this CreateManagedSshSessionTargetResourceDetails.
            Allowed values for this property are: "MANAGED_SSH", "PORT_FORWARDING"
        :type session_type: str

        :param target_resource_port:
            The value to assign to the target_resource_port property of this CreateManagedSshSessionTargetResourceDetails.
        :type target_resource_port: int

        :param target_resource_operating_system_user_name:
            The value to assign to the target_resource_operating_system_user_name property of this CreateManagedSshSessionTargetResourceDetails.
        :type target_resource_operating_system_user_name: str

        :param target_resource_id:
            The value to assign to the target_resource_id property of this CreateManagedSshSessionTargetResourceDetails.
        :type target_resource_id: str

        :param target_resource_private_ip_address:
            The value to assign to the target_resource_private_ip_address property of this CreateManagedSshSessionTargetResourceDetails.
        :type target_resource_private_ip_address: str

        """
        self.swagger_types = {
            'session_type': 'str',
            'target_resource_port': 'int',
            'target_resource_operating_system_user_name': 'str',
            'target_resource_id': 'str',
            'target_resource_private_ip_address': 'str'
        }

        self.attribute_map = {
            'session_type': 'sessionType',
            'target_resource_port': 'targetResourcePort',
            'target_resource_operating_system_user_name': 'targetResourceOperatingSystemUserName',
            'target_resource_id': 'targetResourceId',
            'target_resource_private_ip_address': 'targetResourcePrivateIpAddress'
        }

        self._session_type = None
        self._target_resource_port = None
        self._target_resource_operating_system_user_name = None
        self._target_resource_id = None
        self._target_resource_private_ip_address = None
        self._session_type = 'MANAGED_SSH'

    @property
    def target_resource_operating_system_user_name(self):
        """
        **[Required]** Gets the target_resource_operating_system_user_name of this CreateManagedSshSessionTargetResourceDetails.
        The name of the user on the target resource operating system that the session uses for the connection.


        :return: The target_resource_operating_system_user_name of this CreateManagedSshSessionTargetResourceDetails.
        :rtype: str
        """
        return self._target_resource_operating_system_user_name

    @target_resource_operating_system_user_name.setter
    def target_resource_operating_system_user_name(self, target_resource_operating_system_user_name):
        """
        Sets the target_resource_operating_system_user_name of this CreateManagedSshSessionTargetResourceDetails.
        The name of the user on the target resource operating system that the session uses for the connection.


        :param target_resource_operating_system_user_name: The target_resource_operating_system_user_name of this CreateManagedSshSessionTargetResourceDetails.
        :type: str
        """
        self._target_resource_operating_system_user_name = target_resource_operating_system_user_name

    @property
    def target_resource_id(self):
        """
        **[Required]** Gets the target_resource_id of this CreateManagedSshSessionTargetResourceDetails.
        The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.


        :return: The target_resource_id of this CreateManagedSshSessionTargetResourceDetails.
        :rtype: str
        """
        return self._target_resource_id

    @target_resource_id.setter
    def target_resource_id(self, target_resource_id):
        """
        Sets the target_resource_id of this CreateManagedSshSessionTargetResourceDetails.
        The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.


        :param target_resource_id: The target_resource_id of this CreateManagedSshSessionTargetResourceDetails.
        :type: str
        """
        self._target_resource_id = target_resource_id

    @property
    def target_resource_private_ip_address(self):
        """
        Gets the target_resource_private_ip_address of this CreateManagedSshSessionTargetResourceDetails.
        The private IP address of the target resource that the session connects to.


        :return: The target_resource_private_ip_address of this CreateManagedSshSessionTargetResourceDetails.
        :rtype: str
        """
        return self._target_resource_private_ip_address

    @target_resource_private_ip_address.setter
    def target_resource_private_ip_address(self, target_resource_private_ip_address):
        """
        Sets the target_resource_private_ip_address of this CreateManagedSshSessionTargetResourceDetails.
        The private IP address of the target resource that the session connects to.


        :param target_resource_private_ip_address: The target_resource_private_ip_address of this CreateManagedSshSessionTargetResourceDetails.
        :type: str
        """
        self._target_resource_private_ip_address = target_resource_private_ip_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
