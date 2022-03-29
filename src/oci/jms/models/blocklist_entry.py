# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BlocklistEntry(object):
    """
    An entry for blocklist to describe blocked operation and reason.
    """

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "CREATE_FLEET"
    OPERATION_CREATE_FLEET = "CREATE_FLEET"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "DELETE_FLEET"
    OPERATION_DELETE_FLEET = "DELETE_FLEET"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "MOVE_FLEET"
    OPERATION_MOVE_FLEET = "MOVE_FLEET"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "UPDATE_FLEET"
    OPERATION_UPDATE_FLEET = "UPDATE_FLEET"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "UPDATE_FLEET_AGENT_CONFIGURATION"
    OPERATION_UPDATE_FLEET_AGENT_CONFIGURATION = "UPDATE_FLEET_AGENT_CONFIGURATION"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "DELETE_JAVA_INSTALLATION"
    OPERATION_DELETE_JAVA_INSTALLATION = "DELETE_JAVA_INSTALLATION"

    def __init__(self, **kwargs):
        """
        Initializes a new BlocklistEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this BlocklistEntry.
            Allowed values for this property are: "CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation: str

        :param reason:
            The value to assign to the reason property of this BlocklistEntry.
        :type reason: str

        """
        self.swagger_types = {
            'operation': 'str',
            'reason': 'str'
        }

        self.attribute_map = {
            'operation': 'operation',
            'reason': 'reason'
        }

        self._operation = None
        self._reason = None

    @property
    def operation(self):
        """
        **[Required]** Gets the operation of this BlocklistEntry.
        The operation type.

        Allowed values for this property are: "CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation of this BlocklistEntry.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this BlocklistEntry.
        The operation type.


        :param operation: The operation of this BlocklistEntry.
        :type: str
        """
        allowed_values = ["CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION"]
        if not value_allowed_none_or_none_sentinel(operation, allowed_values):
            operation = 'UNKNOWN_ENUM_VALUE'
        self._operation = operation

    @property
    def reason(self):
        """
        **[Required]** Gets the reason of this BlocklistEntry.
        The reason why the operation is blocklisted.


        :return: The reason of this BlocklistEntry.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this BlocklistEntry.
        The reason why the operation is blocklisted.


        :param reason: The reason of this BlocklistEntry.
        :type: str
        """
        self._reason = reason

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
