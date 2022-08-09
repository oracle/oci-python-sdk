# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBlocklistDetails(object):
    """
    The blocklist record details.
    """

    #: A constant which can be used with the operation property of a CreateBlocklistDetails.
    #: This constant has a value of "CREATE_FLEET"
    OPERATION_CREATE_FLEET = "CREATE_FLEET"

    #: A constant which can be used with the operation property of a CreateBlocklistDetails.
    #: This constant has a value of "DELETE_FLEET"
    OPERATION_DELETE_FLEET = "DELETE_FLEET"

    #: A constant which can be used with the operation property of a CreateBlocklistDetails.
    #: This constant has a value of "MOVE_FLEET"
    OPERATION_MOVE_FLEET = "MOVE_FLEET"

    #: A constant which can be used with the operation property of a CreateBlocklistDetails.
    #: This constant has a value of "UPDATE_FLEET"
    OPERATION_UPDATE_FLEET = "UPDATE_FLEET"

    #: A constant which can be used with the operation property of a CreateBlocklistDetails.
    #: This constant has a value of "UPDATE_FLEET_AGENT_CONFIGURATION"
    OPERATION_UPDATE_FLEET_AGENT_CONFIGURATION = "UPDATE_FLEET_AGENT_CONFIGURATION"

    #: A constant which can be used with the operation property of a CreateBlocklistDetails.
    #: This constant has a value of "DELETE_JAVA_INSTALLATION"
    OPERATION_DELETE_JAVA_INSTALLATION = "DELETE_JAVA_INSTALLATION"

    #: A constant which can be used with the operation property of a CreateBlocklistDetails.
    #: This constant has a value of "CREATE_JAVA_INSTALLATION"
    OPERATION_CREATE_JAVA_INSTALLATION = "CREATE_JAVA_INSTALLATION"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBlocklistDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target:
            The value to assign to the target property of this CreateBlocklistDetails.
        :type target: oci.jms.models.BlocklistTarget

        :param operation:
            The value to assign to the operation property of this CreateBlocklistDetails.
            Allowed values for this property are: "CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION", "CREATE_JAVA_INSTALLATION"
        :type operation: str

        :param reason:
            The value to assign to the reason property of this CreateBlocklistDetails.
        :type reason: str

        """
        self.swagger_types = {
            'target': 'BlocklistTarget',
            'operation': 'str',
            'reason': 'str'
        }

        self.attribute_map = {
            'target': 'target',
            'operation': 'operation',
            'reason': 'reason'
        }

        self._target = None
        self._operation = None
        self._reason = None

    @property
    def target(self):
        """
        **[Required]** Gets the target of this CreateBlocklistDetails.

        :return: The target of this CreateBlocklistDetails.
        :rtype: oci.jms.models.BlocklistTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this CreateBlocklistDetails.

        :param target: The target of this CreateBlocklistDetails.
        :type: oci.jms.models.BlocklistTarget
        """
        self._target = target

    @property
    def operation(self):
        """
        **[Required]** Gets the operation of this CreateBlocklistDetails.
        The operation type

        Allowed values for this property are: "CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION", "CREATE_JAVA_INSTALLATION"


        :return: The operation of this CreateBlocklistDetails.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this CreateBlocklistDetails.
        The operation type


        :param operation: The operation of this CreateBlocklistDetails.
        :type: str
        """
        allowed_values = ["CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION", "CREATE_JAVA_INSTALLATION"]
        if not value_allowed_none_or_none_sentinel(operation, allowed_values):
            raise ValueError(
                "Invalid value for `operation`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._operation = operation

    @property
    def reason(self):
        """
        Gets the reason of this CreateBlocklistDetails.
        The reason for why the operation is blocklisted


        :return: The reason of this CreateBlocklistDetails.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this CreateBlocklistDetails.
        The reason for why the operation is blocklisted


        :param reason: The reason of this CreateBlocklistDetails.
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
