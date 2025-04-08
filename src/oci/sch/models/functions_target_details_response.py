# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200909

from .target_details_response import TargetDetailsResponse
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FunctionsTargetDetailsResponse(TargetDetailsResponse):
    """
    The destination function for data transferred from the source.
    For configuration instructions, see
    `Creating a Connector`__.

    __ https://docs.cloud.oracle.com/iaas/Content/connector-hub/create-service-connector.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FunctionsTargetDetailsResponse object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.FunctionsTargetDetailsResponse.kind` attribute
        of this class is ``functions`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param private_endpoint_metadata:
            The value to assign to the private_endpoint_metadata property of this FunctionsTargetDetailsResponse.
        :type private_endpoint_metadata: oci.sch.models.PrivateEndpointMetadata

        :param kind:
            The value to assign to the kind property of this FunctionsTargetDetailsResponse.
            Allowed values for this property are: "functions", "loggingAnalytics", "monitoring", "notifications", "objectStorage", "streaming"
        :type kind: str

        :param function_id:
            The value to assign to the function_id property of this FunctionsTargetDetailsResponse.
        :type function_id: str

        :param batch_size_in_kbs:
            The value to assign to the batch_size_in_kbs property of this FunctionsTargetDetailsResponse.
        :type batch_size_in_kbs: int

        :param batch_size_in_num:
            The value to assign to the batch_size_in_num property of this FunctionsTargetDetailsResponse.
        :type batch_size_in_num: int

        :param batch_time_in_sec:
            The value to assign to the batch_time_in_sec property of this FunctionsTargetDetailsResponse.
        :type batch_time_in_sec: int

        """
        self.swagger_types = {
            'private_endpoint_metadata': 'PrivateEndpointMetadata',
            'kind': 'str',
            'function_id': 'str',
            'batch_size_in_kbs': 'int',
            'batch_size_in_num': 'int',
            'batch_time_in_sec': 'int'
        }
        self.attribute_map = {
            'private_endpoint_metadata': 'privateEndpointMetadata',
            'kind': 'kind',
            'function_id': 'functionId',
            'batch_size_in_kbs': 'batchSizeInKbs',
            'batch_size_in_num': 'batchSizeInNum',
            'batch_time_in_sec': 'batchTimeInSec'
        }
        self._private_endpoint_metadata = None
        self._kind = None
        self._function_id = None
        self._batch_size_in_kbs = None
        self._batch_size_in_num = None
        self._batch_time_in_sec = None
        self._kind = 'functions'

    @property
    def function_id(self):
        """
        **[Required]** Gets the function_id of this FunctionsTargetDetailsResponse.
        The `OCID`__ of the function.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The function_id of this FunctionsTargetDetailsResponse.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this FunctionsTargetDetailsResponse.
        The `OCID`__ of the function.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param function_id: The function_id of this FunctionsTargetDetailsResponse.
        :type: str
        """
        self._function_id = function_id

    @property
    def batch_size_in_kbs(self):
        """
        Gets the batch_size_in_kbs of this FunctionsTargetDetailsResponse.
        The batch rollover size in kilobytes.
        Only one size option can be specified: `batchSizeInKbs` or `batchSizeInNum`.


        :return: The batch_size_in_kbs of this FunctionsTargetDetailsResponse.
        :rtype: int
        """
        return self._batch_size_in_kbs

    @batch_size_in_kbs.setter
    def batch_size_in_kbs(self, batch_size_in_kbs):
        """
        Sets the batch_size_in_kbs of this FunctionsTargetDetailsResponse.
        The batch rollover size in kilobytes.
        Only one size option can be specified: `batchSizeInKbs` or `batchSizeInNum`.


        :param batch_size_in_kbs: The batch_size_in_kbs of this FunctionsTargetDetailsResponse.
        :type: int
        """
        self._batch_size_in_kbs = batch_size_in_kbs

    @property
    def batch_size_in_num(self):
        """
        Gets the batch_size_in_num of this FunctionsTargetDetailsResponse.
        The batch rollover size in number of messages.
        Only one size option can be specified: `batchSizeInKbs` or `batchSizeInNum`.


        :return: The batch_size_in_num of this FunctionsTargetDetailsResponse.
        :rtype: int
        """
        return self._batch_size_in_num

    @batch_size_in_num.setter
    def batch_size_in_num(self, batch_size_in_num):
        """
        Sets the batch_size_in_num of this FunctionsTargetDetailsResponse.
        The batch rollover size in number of messages.
        Only one size option can be specified: `batchSizeInKbs` or `batchSizeInNum`.


        :param batch_size_in_num: The batch_size_in_num of this FunctionsTargetDetailsResponse.
        :type: int
        """
        self._batch_size_in_num = batch_size_in_num

    @property
    def batch_time_in_sec(self):
        """
        Gets the batch_time_in_sec of this FunctionsTargetDetailsResponse.
        The batch rollover time in seconds.


        :return: The batch_time_in_sec of this FunctionsTargetDetailsResponse.
        :rtype: int
        """
        return self._batch_time_in_sec

    @batch_time_in_sec.setter
    def batch_time_in_sec(self, batch_time_in_sec):
        """
        Sets the batch_time_in_sec of this FunctionsTargetDetailsResponse.
        The batch rollover time in seconds.


        :param batch_time_in_sec: The batch_time_in_sec of this FunctionsTargetDetailsResponse.
        :type: int
        """
        self._batch_time_in_sec = batch_time_in_sec

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
