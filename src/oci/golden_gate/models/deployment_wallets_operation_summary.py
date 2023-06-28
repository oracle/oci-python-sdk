# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeploymentWalletsOperationSummary(object):
    """
    Summary of the deployment wallets operations.
    """

    #: A constant which can be used with the deployment_wallet_operation_type property of a DeploymentWalletsOperationSummary.
    #: This constant has a value of "EXPORT"
    DEPLOYMENT_WALLET_OPERATION_TYPE_EXPORT = "EXPORT"

    #: A constant which can be used with the deployment_wallet_operation_type property of a DeploymentWalletsOperationSummary.
    #: This constant has a value of "IMPORT"
    DEPLOYMENT_WALLET_OPERATION_TYPE_IMPORT = "IMPORT"

    #: A constant which can be used with the deployment_wallet_operation_status property of a DeploymentWalletsOperationSummary.
    #: This constant has a value of "EXPORTING"
    DEPLOYMENT_WALLET_OPERATION_STATUS_EXPORTING = "EXPORTING"

    #: A constant which can be used with the deployment_wallet_operation_status property of a DeploymentWalletsOperationSummary.
    #: This constant has a value of "EXPORTED"
    DEPLOYMENT_WALLET_OPERATION_STATUS_EXPORTED = "EXPORTED"

    #: A constant which can be used with the deployment_wallet_operation_status property of a DeploymentWalletsOperationSummary.
    #: This constant has a value of "IMPORTED"
    DEPLOYMENT_WALLET_OPERATION_STATUS_IMPORTED = "IMPORTED"

    #: A constant which can be used with the deployment_wallet_operation_status property of a DeploymentWalletsOperationSummary.
    #: This constant has a value of "IMPORTING"
    DEPLOYMENT_WALLET_OPERATION_STATUS_IMPORTING = "IMPORTING"

    #: A constant which can be used with the deployment_wallet_operation_status property of a DeploymentWalletsOperationSummary.
    #: This constant has a value of "FAILED"
    DEPLOYMENT_WALLET_OPERATION_STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DeploymentWalletsOperationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param wallet_operation_id:
            The value to assign to the wallet_operation_id property of this DeploymentWalletsOperationSummary.
        :type wallet_operation_id: str

        :param wallet_secret_id:
            The value to assign to the wallet_secret_id property of this DeploymentWalletsOperationSummary.
        :type wallet_secret_id: str

        :param deployment_wallet_operation_type:
            The value to assign to the deployment_wallet_operation_type property of this DeploymentWalletsOperationSummary.
            Allowed values for this property are: "EXPORT", "IMPORT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_wallet_operation_type: str

        :param deployment_wallet_operation_status:
            The value to assign to the deployment_wallet_operation_status property of this DeploymentWalletsOperationSummary.
            Allowed values for this property are: "EXPORTING", "EXPORTED", "IMPORTED", "IMPORTING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_wallet_operation_status: str

        :param time_started:
            The value to assign to the time_started property of this DeploymentWalletsOperationSummary.
        :type time_started: datetime

        :param time_completed:
            The value to assign to the time_completed property of this DeploymentWalletsOperationSummary.
        :type time_completed: datetime

        """
        self.swagger_types = {
            'wallet_operation_id': 'str',
            'wallet_secret_id': 'str',
            'deployment_wallet_operation_type': 'str',
            'deployment_wallet_operation_status': 'str',
            'time_started': 'datetime',
            'time_completed': 'datetime'
        }

        self.attribute_map = {
            'wallet_operation_id': 'walletOperationId',
            'wallet_secret_id': 'walletSecretId',
            'deployment_wallet_operation_type': 'deploymentWalletOperationType',
            'deployment_wallet_operation_status': 'deploymentWalletOperationStatus',
            'time_started': 'timeStarted',
            'time_completed': 'timeCompleted'
        }

        self._wallet_operation_id = None
        self._wallet_secret_id = None
        self._deployment_wallet_operation_type = None
        self._deployment_wallet_operation_status = None
        self._time_started = None
        self._time_completed = None

    @property
    def wallet_operation_id(self):
        """
        **[Required]** Gets the wallet_operation_id of this DeploymentWalletsOperationSummary.
        The UUID of the wallet operation performed by the customer.
        If provided, this will reference a key which the customer can use to query or search a particular wallet operation


        :return: The wallet_operation_id of this DeploymentWalletsOperationSummary.
        :rtype: str
        """
        return self._wallet_operation_id

    @wallet_operation_id.setter
    def wallet_operation_id(self, wallet_operation_id):
        """
        Sets the wallet_operation_id of this DeploymentWalletsOperationSummary.
        The UUID of the wallet operation performed by the customer.
        If provided, this will reference a key which the customer can use to query or search a particular wallet operation


        :param wallet_operation_id: The wallet_operation_id of this DeploymentWalletsOperationSummary.
        :type: str
        """
        self._wallet_operation_id = wallet_operation_id

    @property
    def wallet_secret_id(self):
        """
        **[Required]** Gets the wallet_secret_id of this DeploymentWalletsOperationSummary.
        The OCID of the customer's GoldenGate Service Secret.
        If provided, it references a key that customers will be required to ensure the policies are established
        to permit GoldenGate to use this Secret.


        :return: The wallet_secret_id of this DeploymentWalletsOperationSummary.
        :rtype: str
        """
        return self._wallet_secret_id

    @wallet_secret_id.setter
    def wallet_secret_id(self, wallet_secret_id):
        """
        Sets the wallet_secret_id of this DeploymentWalletsOperationSummary.
        The OCID of the customer's GoldenGate Service Secret.
        If provided, it references a key that customers will be required to ensure the policies are established
        to permit GoldenGate to use this Secret.


        :param wallet_secret_id: The wallet_secret_id of this DeploymentWalletsOperationSummary.
        :type: str
        """
        self._wallet_secret_id = wallet_secret_id

    @property
    def deployment_wallet_operation_type(self):
        """
        **[Required]** Gets the deployment_wallet_operation_type of this DeploymentWalletsOperationSummary.
        The operation type of the deployment wallet.

        Allowed values for this property are: "EXPORT", "IMPORT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_wallet_operation_type of this DeploymentWalletsOperationSummary.
        :rtype: str
        """
        return self._deployment_wallet_operation_type

    @deployment_wallet_operation_type.setter
    def deployment_wallet_operation_type(self, deployment_wallet_operation_type):
        """
        Sets the deployment_wallet_operation_type of this DeploymentWalletsOperationSummary.
        The operation type of the deployment wallet.


        :param deployment_wallet_operation_type: The deployment_wallet_operation_type of this DeploymentWalletsOperationSummary.
        :type: str
        """
        allowed_values = ["EXPORT", "IMPORT"]
        if not value_allowed_none_or_none_sentinel(deployment_wallet_operation_type, allowed_values):
            deployment_wallet_operation_type = 'UNKNOWN_ENUM_VALUE'
        self._deployment_wallet_operation_type = deployment_wallet_operation_type

    @property
    def deployment_wallet_operation_status(self):
        """
        **[Required]** Gets the deployment_wallet_operation_status of this DeploymentWalletsOperationSummary.
        The status of the deployment wallet.

        Allowed values for this property are: "EXPORTING", "EXPORTED", "IMPORTED", "IMPORTING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_wallet_operation_status of this DeploymentWalletsOperationSummary.
        :rtype: str
        """
        return self._deployment_wallet_operation_status

    @deployment_wallet_operation_status.setter
    def deployment_wallet_operation_status(self, deployment_wallet_operation_status):
        """
        Sets the deployment_wallet_operation_status of this DeploymentWalletsOperationSummary.
        The status of the deployment wallet.


        :param deployment_wallet_operation_status: The deployment_wallet_operation_status of this DeploymentWalletsOperationSummary.
        :type: str
        """
        allowed_values = ["EXPORTING", "EXPORTED", "IMPORTED", "IMPORTING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(deployment_wallet_operation_status, allowed_values):
            deployment_wallet_operation_status = 'UNKNOWN_ENUM_VALUE'
        self._deployment_wallet_operation_status = deployment_wallet_operation_status

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this DeploymentWalletsOperationSummary.
        The date and time the request was started. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_started of this DeploymentWalletsOperationSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this DeploymentWalletsOperationSummary.
        The date and time the request was started. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_started: The time_started of this DeploymentWalletsOperationSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_completed(self):
        """
        Gets the time_completed of this DeploymentWalletsOperationSummary.
        The date and time the request was finished. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_completed of this DeploymentWalletsOperationSummary.
        :rtype: datetime
        """
        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """
        Sets the time_completed of this DeploymentWalletsOperationSummary.
        The date and time the request was finished. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_completed: The time_completed of this DeploymentWalletsOperationSummary.
        :type: datetime
        """
        self._time_completed = time_completed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
