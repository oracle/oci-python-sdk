# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dvp_stack_details import DvpStackDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OracleRMStack(DvpStackDetails):
    """
    DVP details of Oracle RM stack.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OracleRMStack object with values from keyword arguments. The default value of the :py:attr:`~oci.apm_synthetics.models.OracleRMStack.dvp_stack_type` attribute
        of this class is ``ORACLE_RM_STACK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dvp_stack_type:
            The value to assign to the dvp_stack_type property of this OracleRMStack.
            Allowed values for this property are: "ORACLE_RM_STACK"
        :type dvp_stack_type: str

        :param dvp_version:
            The value to assign to the dvp_version property of this OracleRMStack.
        :type dvp_version: str

        :param dvp_stack_id:
            The value to assign to the dvp_stack_id property of this OracleRMStack.
        :type dvp_stack_id: str

        :param dvp_stream_id:
            The value to assign to the dvp_stream_id property of this OracleRMStack.
        :type dvp_stream_id: str

        """
        self.swagger_types = {
            'dvp_stack_type': 'str',
            'dvp_version': 'str',
            'dvp_stack_id': 'str',
            'dvp_stream_id': 'str'
        }

        self.attribute_map = {
            'dvp_stack_type': 'dvpStackType',
            'dvp_version': 'dvpVersion',
            'dvp_stack_id': 'dvpStackId',
            'dvp_stream_id': 'dvpStreamId'
        }

        self._dvp_stack_type = None
        self._dvp_version = None
        self._dvp_stack_id = None
        self._dvp_stream_id = None
        self._dvp_stack_type = 'ORACLE_RM_STACK'

    @property
    def dvp_stack_id(self):
        """
        **[Required]** Gets the dvp_stack_id of this OracleRMStack.
        Stack `OCID`__ of DVP RM stack.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The dvp_stack_id of this OracleRMStack.
        :rtype: str
        """
        return self._dvp_stack_id

    @dvp_stack_id.setter
    def dvp_stack_id(self, dvp_stack_id):
        """
        Sets the dvp_stack_id of this OracleRMStack.
        Stack `OCID`__ of DVP RM stack.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param dvp_stack_id: The dvp_stack_id of this OracleRMStack.
        :type: str
        """
        self._dvp_stack_id = dvp_stack_id

    @property
    def dvp_stream_id(self):
        """
        **[Required]** Gets the dvp_stream_id of this OracleRMStack.
        Stream `OCID`__ of DVP RM stack.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The dvp_stream_id of this OracleRMStack.
        :rtype: str
        """
        return self._dvp_stream_id

    @dvp_stream_id.setter
    def dvp_stream_id(self, dvp_stream_id):
        """
        Sets the dvp_stream_id of this OracleRMStack.
        Stream `OCID`__ of DVP RM stack.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param dvp_stream_id: The dvp_stream_id of this OracleRMStack.
        :type: str
        """
        self._dvp_stream_id = dvp_stream_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
