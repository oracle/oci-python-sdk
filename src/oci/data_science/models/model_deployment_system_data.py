# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModelDeploymentSystemData(object):
    """
    Model deployment system data.
    """

    #: A constant which can be used with the system_infra_type property of a ModelDeploymentSystemData.
    #: This constant has a value of "INSTANCE_POOL"
    SYSTEM_INFRA_TYPE_INSTANCE_POOL = "INSTANCE_POOL"

    def __init__(self, **kwargs):
        """
        Initializes a new ModelDeploymentSystemData object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_science.models.InstancePoolModelDeploymentSystemData`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param system_infra_type:
            The value to assign to the system_infra_type property of this ModelDeploymentSystemData.
            Allowed values for this property are: "INSTANCE_POOL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type system_infra_type: str

        """
        self.swagger_types = {
            'system_infra_type': 'str'
        }
        self.attribute_map = {
            'system_infra_type': 'systemInfraType'
        }
        self._system_infra_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['systemInfraType']

        if type == 'INSTANCE_POOL':
            return 'InstancePoolModelDeploymentSystemData'
        else:
            return 'ModelDeploymentSystemData'

    @property
    def system_infra_type(self):
        """
        Gets the system_infra_type of this ModelDeploymentSystemData.
        The infrastructure type of the model deployment.

        Allowed values for this property are: "INSTANCE_POOL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The system_infra_type of this ModelDeploymentSystemData.
        :rtype: str
        """
        return self._system_infra_type

    @system_infra_type.setter
    def system_infra_type(self, system_infra_type):
        """
        Sets the system_infra_type of this ModelDeploymentSystemData.
        The infrastructure type of the model deployment.


        :param system_infra_type: The system_infra_type of this ModelDeploymentSystemData.
        :type: str
        """
        allowed_values = ["INSTANCE_POOL"]
        if not value_allowed_none_or_none_sentinel(system_infra_type, allowed_values):
            system_infra_type = 'UNKNOWN_ENUM_VALUE'
        self._system_infra_type = system_infra_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
