# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetResourceDetails(object):
    """
    Details about a bastion session's target resource.
    """

    #: A constant which can be used with the session_type property of a TargetResourceDetails.
    #: This constant has a value of "MANAGED_SSH"
    SESSION_TYPE_MANAGED_SSH = "MANAGED_SSH"

    #: A constant which can be used with the session_type property of a TargetResourceDetails.
    #: This constant has a value of "PORT_FORWARDING"
    SESSION_TYPE_PORT_FORWARDING = "PORT_FORWARDING"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetResourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.bastion.models.ManagedSshSessionTargetResourceDetails`
        * :class:`~oci.bastion.models.PortForwardingSessionTargetResourceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param session_type:
            The value to assign to the session_type property of this TargetResourceDetails.
            Allowed values for this property are: "MANAGED_SSH", "PORT_FORWARDING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type session_type: str

        :param target_resource_port:
            The value to assign to the target_resource_port property of this TargetResourceDetails.
        :type target_resource_port: int

        """
        self.swagger_types = {
            'session_type': 'str',
            'target_resource_port': 'int'
        }

        self.attribute_map = {
            'session_type': 'sessionType',
            'target_resource_port': 'targetResourcePort'
        }

        self._session_type = None
        self._target_resource_port = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['sessionType']

        if type == 'MANAGED_SSH':
            return 'ManagedSshSessionTargetResourceDetails'

        if type == 'PORT_FORWARDING':
            return 'PortForwardingSessionTargetResourceDetails'
        else:
            return 'TargetResourceDetails'

    @property
    def session_type(self):
        """
        **[Required]** Gets the session_type of this TargetResourceDetails.
        The Bastion service recognizes two types of sessions, managed SSH sessions and SSH port forwarding sessions. Managed SSH sessions require that the target resource has an OpenSSH server and the Oracle Cloud Agent both running.

        Allowed values for this property are: "MANAGED_SSH", "PORT_FORWARDING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The session_type of this TargetResourceDetails.
        :rtype: str
        """
        return self._session_type

    @session_type.setter
    def session_type(self, session_type):
        """
        Sets the session_type of this TargetResourceDetails.
        The Bastion service recognizes two types of sessions, managed SSH sessions and SSH port forwarding sessions. Managed SSH sessions require that the target resource has an OpenSSH server and the Oracle Cloud Agent both running.


        :param session_type: The session_type of this TargetResourceDetails.
        :type: str
        """
        allowed_values = ["MANAGED_SSH", "PORT_FORWARDING"]
        if not value_allowed_none_or_none_sentinel(session_type, allowed_values):
            session_type = 'UNKNOWN_ENUM_VALUE'
        self._session_type = session_type

    @property
    def target_resource_port(self):
        """
        **[Required]** Gets the target_resource_port of this TargetResourceDetails.
        The port number to connect to on the target resource.


        :return: The target_resource_port of this TargetResourceDetails.
        :rtype: int
        """
        return self._target_resource_port

    @target_resource_port.setter
    def target_resource_port(self, target_resource_port):
        """
        Sets the target_resource_port of this TargetResourceDetails.
        The port number to connect to on the target resource.


        :param target_resource_port: The target_resource_port of this TargetResourceDetails.
        :type: int
        """
        self._target_resource_port = target_resource_port

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
