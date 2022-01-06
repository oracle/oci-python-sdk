# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_session_target_resource_details import CreateSessionTargetResourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePortForwardingSessionTargetResourceDetails(CreateSessionTargetResourceDetails):
    """
    Details about a port forwarding session for a target resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePortForwardingSessionTargetResourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.bastion.models.CreatePortForwardingSessionTargetResourceDetails.session_type` attribute
        of this class is ``PORT_FORWARDING`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param session_type:
            The value to assign to the session_type property of this CreatePortForwardingSessionTargetResourceDetails.
            Allowed values for this property are: "MANAGED_SSH", "PORT_FORWARDING"
        :type session_type: str

        :param target_resource_port:
            The value to assign to the target_resource_port property of this CreatePortForwardingSessionTargetResourceDetails.
        :type target_resource_port: int

        :param target_resource_id:
            The value to assign to the target_resource_id property of this CreatePortForwardingSessionTargetResourceDetails.
        :type target_resource_id: str

        :param target_resource_private_ip_address:
            The value to assign to the target_resource_private_ip_address property of this CreatePortForwardingSessionTargetResourceDetails.
        :type target_resource_private_ip_address: str

        """
        self.swagger_types = {
            'session_type': 'str',
            'target_resource_port': 'int',
            'target_resource_id': 'str',
            'target_resource_private_ip_address': 'str'
        }

        self.attribute_map = {
            'session_type': 'sessionType',
            'target_resource_port': 'targetResourcePort',
            'target_resource_id': 'targetResourceId',
            'target_resource_private_ip_address': 'targetResourcePrivateIpAddress'
        }

        self._session_type = None
        self._target_resource_port = None
        self._target_resource_id = None
        self._target_resource_private_ip_address = None
        self._session_type = 'PORT_FORWARDING'

    @property
    def target_resource_id(self):
        """
        Gets the target_resource_id of this CreatePortForwardingSessionTargetResourceDetails.
        The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.


        :return: The target_resource_id of this CreatePortForwardingSessionTargetResourceDetails.
        :rtype: str
        """
        return self._target_resource_id

    @target_resource_id.setter
    def target_resource_id(self, target_resource_id):
        """
        Sets the target_resource_id of this CreatePortForwardingSessionTargetResourceDetails.
        The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.


        :param target_resource_id: The target_resource_id of this CreatePortForwardingSessionTargetResourceDetails.
        :type: str
        """
        self._target_resource_id = target_resource_id

    @property
    def target_resource_private_ip_address(self):
        """
        Gets the target_resource_private_ip_address of this CreatePortForwardingSessionTargetResourceDetails.
        The private IP address of the target resource that the session connects to.


        :return: The target_resource_private_ip_address of this CreatePortForwardingSessionTargetResourceDetails.
        :rtype: str
        """
        return self._target_resource_private_ip_address

    @target_resource_private_ip_address.setter
    def target_resource_private_ip_address(self, target_resource_private_ip_address):
        """
        Sets the target_resource_private_ip_address of this CreatePortForwardingSessionTargetResourceDetails.
        The private IP address of the target resource that the session connects to.


        :param target_resource_private_ip_address: The target_resource_private_ip_address of this CreatePortForwardingSessionTargetResourceDetails.
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
