# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DvpStackDetails(object):
    """
    Details of DVP Stack.
    """

    #: A constant which can be used with the dvp_stack_type property of a DvpStackDetails.
    #: This constant has a value of "ORACLE_RM_STACK"
    DVP_STACK_TYPE_ORACLE_RM_STACK = "ORACLE_RM_STACK"

    def __init__(self, **kwargs):
        """
        Initializes a new DvpStackDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.apm_synthetics.models.OracleRMStack`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dvp_stack_type:
            The value to assign to the dvp_stack_type property of this DvpStackDetails.
            Allowed values for this property are: "ORACLE_RM_STACK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type dvp_stack_type: str

        :param dvp_version:
            The value to assign to the dvp_version property of this DvpStackDetails.
        :type dvp_version: str

        """
        self.swagger_types = {
            'dvp_stack_type': 'str',
            'dvp_version': 'str'
        }

        self.attribute_map = {
            'dvp_stack_type': 'dvpStackType',
            'dvp_version': 'dvpVersion'
        }

        self._dvp_stack_type = None
        self._dvp_version = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['dvpStackType']

        if type == 'ORACLE_RM_STACK':
            return 'OracleRMStack'
        else:
            return 'DvpStackDetails'

    @property
    def dvp_stack_type(self):
        """
        **[Required]** Gets the dvp_stack_type of this DvpStackDetails.
        Type of stack.

        Allowed values for this property are: "ORACLE_RM_STACK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The dvp_stack_type of this DvpStackDetails.
        :rtype: str
        """
        return self._dvp_stack_type

    @dvp_stack_type.setter
    def dvp_stack_type(self, dvp_stack_type):
        """
        Sets the dvp_stack_type of this DvpStackDetails.
        Type of stack.


        :param dvp_stack_type: The dvp_stack_type of this DvpStackDetails.
        :type: str
        """
        allowed_values = ["ORACLE_RM_STACK"]
        if not value_allowed_none_or_none_sentinel(dvp_stack_type, allowed_values):
            dvp_stack_type = 'UNKNOWN_ENUM_VALUE'
        self._dvp_stack_type = dvp_stack_type

    @property
    def dvp_version(self):
        """
        **[Required]** Gets the dvp_version of this DvpStackDetails.
        Version of DVP.


        :return: The dvp_version of this DvpStackDetails.
        :rtype: str
        """
        return self._dvp_version

    @dvp_version.setter
    def dvp_version(self, dvp_version):
        """
        Sets the dvp_version of this DvpStackDetails.
        Version of DVP.


        :param dvp_version: The dvp_version of this DvpStackDetails.
        :type: str
        """
        self._dvp_version = dvp_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
