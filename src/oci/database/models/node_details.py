# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodeDetails(object):
    """
    Node details associated with a network.
    """

    #: A constant which can be used with the lifecycle_state property of a NodeDetails.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a NodeDetails.
    #: This constant has a value of "REQUIRES_VALIDATION"
    LIFECYCLE_STATE_REQUIRES_VALIDATION = "REQUIRES_VALIDATION"

    #: A constant which can be used with the lifecycle_state property of a NodeDetails.
    #: This constant has a value of "VALIDATING"
    LIFECYCLE_STATE_VALIDATING = "VALIDATING"

    #: A constant which can be used with the lifecycle_state property of a NodeDetails.
    #: This constant has a value of "VALIDATED"
    LIFECYCLE_STATE_VALIDATED = "VALIDATED"

    #: A constant which can be used with the lifecycle_state property of a NodeDetails.
    #: This constant has a value of "VALIDATION_FAILED"
    LIFECYCLE_STATE_VALIDATION_FAILED = "VALIDATION_FAILED"

    #: A constant which can be used with the lifecycle_state property of a NodeDetails.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a NodeDetails.
    #: This constant has a value of "ALLOCATED"
    LIFECYCLE_STATE_ALLOCATED = "ALLOCATED"

    #: A constant which can be used with the lifecycle_state property of a NodeDetails.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a NodeDetails.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a NodeDetails.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new NodeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hostname:
            The value to assign to the hostname property of this NodeDetails.
        :type hostname: str

        :param ip:
            The value to assign to the ip property of this NodeDetails.
        :type ip: str

        :param vip_hostname:
            The value to assign to the vip_hostname property of this NodeDetails.
        :type vip_hostname: str

        :param vip:
            The value to assign to the vip property of this NodeDetails.
        :type vip: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this NodeDetails.
            Allowed values for this property are: "CREATING", "REQUIRES_VALIDATION", "VALIDATING", "VALIDATED", "VALIDATION_FAILED", "UPDATING", "ALLOCATED", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param db_server_id:
            The value to assign to the db_server_id property of this NodeDetails.
        :type db_server_id: str

        """
        self.swagger_types = {
            'hostname': 'str',
            'ip': 'str',
            'vip_hostname': 'str',
            'vip': 'str',
            'lifecycle_state': 'str',
            'db_server_id': 'str'
        }

        self.attribute_map = {
            'hostname': 'hostname',
            'ip': 'ip',
            'vip_hostname': 'vipHostname',
            'vip': 'vip',
            'lifecycle_state': 'lifecycleState',
            'db_server_id': 'dbServerId'
        }

        self._hostname = None
        self._ip = None
        self._vip_hostname = None
        self._vip = None
        self._lifecycle_state = None
        self._db_server_id = None

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this NodeDetails.
        The node host name.


        :return: The hostname of this NodeDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this NodeDetails.
        The node host name.


        :param hostname: The hostname of this NodeDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def ip(self):
        """
        **[Required]** Gets the ip of this NodeDetails.
        The node IP address.


        :return: The ip of this NodeDetails.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this NodeDetails.
        The node IP address.


        :param ip: The ip of this NodeDetails.
        :type: str
        """
        self._ip = ip

    @property
    def vip_hostname(self):
        """
        Gets the vip_hostname of this NodeDetails.
        The node virtual IP (VIP) host name.


        :return: The vip_hostname of this NodeDetails.
        :rtype: str
        """
        return self._vip_hostname

    @vip_hostname.setter
    def vip_hostname(self, vip_hostname):
        """
        Sets the vip_hostname of this NodeDetails.
        The node virtual IP (VIP) host name.


        :param vip_hostname: The vip_hostname of this NodeDetails.
        :type: str
        """
        self._vip_hostname = vip_hostname

    @property
    def vip(self):
        """
        Gets the vip of this NodeDetails.
        The node virtual IP (VIP) address.


        :return: The vip of this NodeDetails.
        :rtype: str
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        """
        Sets the vip of this NodeDetails.
        The node virtual IP (VIP) address.


        :param vip: The vip of this NodeDetails.
        :type: str
        """
        self._vip = vip

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this NodeDetails.
        The current state of the VM cluster network nodes.
        CREATING - The resource is being created
        REQUIRES_VALIDATION - The resource is created and may not be usable until it is validated.
        VALIDATING - The resource is being validated and not available to use.
        VALIDATED - The resource is validated and is available for consumption by VM cluster.
        VALIDATION_FAILED - The resource validation has failed and might require user input to be corrected.
        UPDATING - The resource is being updated and not available to use.
        ALLOCATED - The resource is currently being used by VM cluster.
        TERMINATING - The resource is being deleted and not available to use.
        TERMINATED - The resource is deleted and unavailable.
        FAILED - The resource is in a failed state due to validation or other errors.

        Allowed values for this property are: "CREATING", "REQUIRES_VALIDATION", "VALIDATING", "VALIDATED", "VALIDATION_FAILED", "UPDATING", "ALLOCATED", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this NodeDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this NodeDetails.
        The current state of the VM cluster network nodes.
        CREATING - The resource is being created
        REQUIRES_VALIDATION - The resource is created and may not be usable until it is validated.
        VALIDATING - The resource is being validated and not available to use.
        VALIDATED - The resource is validated and is available for consumption by VM cluster.
        VALIDATION_FAILED - The resource validation has failed and might require user input to be corrected.
        UPDATING - The resource is being updated and not available to use.
        ALLOCATED - The resource is currently being used by VM cluster.
        TERMINATING - The resource is being deleted and not available to use.
        TERMINATED - The resource is deleted and unavailable.
        FAILED - The resource is in a failed state due to validation or other errors.


        :param lifecycle_state: The lifecycle_state of this NodeDetails.
        :type: str
        """
        allowed_values = ["CREATING", "REQUIRES_VALIDATION", "VALIDATING", "VALIDATED", "VALIDATION_FAILED", "UPDATING", "ALLOCATED", "TERMINATING", "TERMINATED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def db_server_id(self):
        """
        Gets the db_server_id of this NodeDetails.
        The Db server associated with the node.


        :return: The db_server_id of this NodeDetails.
        :rtype: str
        """
        return self._db_server_id

    @db_server_id.setter
    def db_server_id(self, db_server_id):
        """
        Sets the db_server_id of this NodeDetails.
        The Db server associated with the node.


        :param db_server_id: The db_server_id of this NodeDetails.
        :type: str
        """
        self._db_server_id = db_server_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
