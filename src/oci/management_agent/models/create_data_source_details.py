# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200202


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataSourceDetails(object):
    """
    A new data source.
    """

    #: A constant which can be used with the type property of a CreateDataSourceDetails.
    #: This constant has a value of "KUBERNETES_CLUSTER"
    TYPE_KUBERNETES_CLUSTER = "KUBERNETES_CLUSTER"

    #: A constant which can be used with the type property of a CreateDataSourceDetails.
    #: This constant has a value of "PROMETHEUS_EMITTER"
    TYPE_PROMETHEUS_EMITTER = "PROMETHEUS_EMITTER"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.management_agent.models.CreatePrometheusEmitterDataSourceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CreateDataSourceDetails.
            Allowed values for this property are: "KUBERNETES_CLUSTER", "PROMETHEUS_EMITTER"
        :type type: str

        :param name:
            The value to assign to the name property of this CreateDataSourceDetails.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDataSourceDetails.
        :type compartment_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'compartment_id': 'str'
        }
        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'compartment_id': 'compartmentId'
        }
        self._type = None
        self._name = None
        self._compartment_id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'PROMETHEUS_EMITTER':
            return 'CreatePrometheusEmitterDataSourceDetails'
        else:
            return 'CreateDataSourceDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateDataSourceDetails.
        The type of the DataSource.

        Allowed values for this property are: "KUBERNETES_CLUSTER", "PROMETHEUS_EMITTER"


        :return: The type of this CreateDataSourceDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateDataSourceDetails.
        The type of the DataSource.


        :param type: The type of this CreateDataSourceDetails.
        :type: str
        """
        allowed_values = ["KUBERNETES_CLUSTER", "PROMETHEUS_EMITTER"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateDataSourceDetails.
        Unique name of the DataSource.


        :return: The name of this CreateDataSourceDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateDataSourceDetails.
        Unique name of the DataSource.


        :param name: The name of this CreateDataSourceDetails.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDataSourceDetails.
        Compartment owning this DataSource.


        :return: The compartment_id of this CreateDataSourceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDataSourceDetails.
        Compartment owning this DataSource.


        :param compartment_id: The compartment_id of this CreateDataSourceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
