# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudDatabaseManagementConfig(object):
    """
    The configuration of the Database Management service.
    """

    #: A constant which can be used with the management_status property of a CloudDatabaseManagementConfig.
    #: This constant has a value of "ENABLING"
    MANAGEMENT_STATUS_ENABLING = "ENABLING"

    #: A constant which can be used with the management_status property of a CloudDatabaseManagementConfig.
    #: This constant has a value of "ENABLED"
    MANAGEMENT_STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the management_status property of a CloudDatabaseManagementConfig.
    #: This constant has a value of "DISABLING"
    MANAGEMENT_STATUS_DISABLING = "DISABLING"

    #: A constant which can be used with the management_status property of a CloudDatabaseManagementConfig.
    #: This constant has a value of "DISABLED"
    MANAGEMENT_STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the management_status property of a CloudDatabaseManagementConfig.
    #: This constant has a value of "UPDATING"
    MANAGEMENT_STATUS_UPDATING = "UPDATING"

    #: A constant which can be used with the management_status property of a CloudDatabaseManagementConfig.
    #: This constant has a value of "FAILED_ENABLING"
    MANAGEMENT_STATUS_FAILED_ENABLING = "FAILED_ENABLING"

    #: A constant which can be used with the management_status property of a CloudDatabaseManagementConfig.
    #: This constant has a value of "FAILED_DISABLING"
    MANAGEMENT_STATUS_FAILED_DISABLING = "FAILED_DISABLING"

    #: A constant which can be used with the management_status property of a CloudDatabaseManagementConfig.
    #: This constant has a value of "FAILED_UPDATING"
    MANAGEMENT_STATUS_FAILED_UPDATING = "FAILED_UPDATING"

    #: A constant which can be used with the management_type property of a CloudDatabaseManagementConfig.
    #: This constant has a value of "BASIC"
    MANAGEMENT_TYPE_BASIC = "BASIC"

    #: A constant which can be used with the management_type property of a CloudDatabaseManagementConfig.
    #: This constant has a value of "ADVANCED"
    MANAGEMENT_TYPE_ADVANCED = "ADVANCED"

    def __init__(self, **kwargs):
        """
        Initializes a new CloudDatabaseManagementConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param management_status:
            The value to assign to the management_status property of this CloudDatabaseManagementConfig.
            Allowed values for this property are: "ENABLING", "ENABLED", "DISABLING", "DISABLED", "UPDATING", "FAILED_ENABLING", "FAILED_DISABLING", "FAILED_UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type management_status: str

        :param management_type:
            The value to assign to the management_type property of this CloudDatabaseManagementConfig.
            Allowed values for this property are: "BASIC", "ADVANCED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type management_type: str

        """
        self.swagger_types = {
            'management_status': 'str',
            'management_type': 'str'
        }

        self.attribute_map = {
            'management_status': 'managementStatus',
            'management_type': 'managementType'
        }

        self._management_status = None
        self._management_type = None

    @property
    def management_status(self):
        """
        **[Required]** Gets the management_status of this CloudDatabaseManagementConfig.
        The status of the Database Management service.

        Allowed values for this property are: "ENABLING", "ENABLED", "DISABLING", "DISABLED", "UPDATING", "FAILED_ENABLING", "FAILED_DISABLING", "FAILED_UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The management_status of this CloudDatabaseManagementConfig.
        :rtype: str
        """
        return self._management_status

    @management_status.setter
    def management_status(self, management_status):
        """
        Sets the management_status of this CloudDatabaseManagementConfig.
        The status of the Database Management service.


        :param management_status: The management_status of this CloudDatabaseManagementConfig.
        :type: str
        """
        allowed_values = ["ENABLING", "ENABLED", "DISABLING", "DISABLED", "UPDATING", "FAILED_ENABLING", "FAILED_DISABLING", "FAILED_UPDATING"]
        if not value_allowed_none_or_none_sentinel(management_status, allowed_values):
            management_status = 'UNKNOWN_ENUM_VALUE'
        self._management_status = management_status

    @property
    def management_type(self):
        """
        **[Required]** Gets the management_type of this CloudDatabaseManagementConfig.
        The Database Management type.

        Allowed values for this property are: "BASIC", "ADVANCED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The management_type of this CloudDatabaseManagementConfig.
        :rtype: str
        """
        return self._management_type

    @management_type.setter
    def management_type(self, management_type):
        """
        Sets the management_type of this CloudDatabaseManagementConfig.
        The Database Management type.


        :param management_type: The management_type of this CloudDatabaseManagementConfig.
        :type: str
        """
        allowed_values = ["BASIC", "ADVANCED"]
        if not value_allowed_none_or_none_sentinel(management_type, allowed_values):
            management_type = 'UNKNOWN_ENUM_VALUE'
        self._management_type = management_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
