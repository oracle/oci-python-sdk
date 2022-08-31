# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Operation(object):
    """
    The operation object.
    """

    #: A constant which can be used with the model_type property of a Operation.
    #: This constant has a value of "PROCEDURE"
    MODEL_TYPE_PROCEDURE = "PROCEDURE"

    #: A constant which can be used with the model_type property of a Operation.
    #: This constant has a value of "API"
    MODEL_TYPE_API = "API"

    def __init__(self, **kwargs):
        """
        Initializes a new Operation object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_connectivity.models.OperationFromProcedure`
        * :class:`~oci.data_connectivity.models.OperationFromApi`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_attributes:
            The value to assign to the operation_attributes property of this Operation.
        :type operation_attributes: oci.data_connectivity.models.AbstractOperationAttributes

        :param model_type:
            The value to assign to the model_type property of this Operation.
            Allowed values for this property are: "PROCEDURE", "API", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param metadata:
            The value to assign to the metadata property of this Operation.
        :type metadata: oci.data_connectivity.models.ObjectMetadata

        """
        self.swagger_types = {
            'operation_attributes': 'AbstractOperationAttributes',
            'model_type': 'str',
            'metadata': 'ObjectMetadata'
        }

        self.attribute_map = {
            'operation_attributes': 'operationAttributes',
            'model_type': 'modelType',
            'metadata': 'metadata'
        }

        self._operation_attributes = None
        self._model_type = None
        self._metadata = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'PROCEDURE':
            return 'OperationFromProcedure'

        if type == 'API':
            return 'OperationFromApi'
        else:
            return 'Operation'

    @property
    def operation_attributes(self):
        """
        Gets the operation_attributes of this Operation.

        :return: The operation_attributes of this Operation.
        :rtype: oci.data_connectivity.models.AbstractOperationAttributes
        """
        return self._operation_attributes

    @operation_attributes.setter
    def operation_attributes(self, operation_attributes):
        """
        Sets the operation_attributes of this Operation.

        :param operation_attributes: The operation_attributes of this Operation.
        :type: oci.data_connectivity.models.AbstractOperationAttributes
        """
        self._operation_attributes = operation_attributes

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this Operation.
        The operation type.

        Allowed values for this property are: "PROCEDURE", "API", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this Operation.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this Operation.
        The operation type.


        :param model_type: The model_type of this Operation.
        :type: str
        """
        allowed_values = ["PROCEDURE", "API"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def metadata(self):
        """
        Gets the metadata of this Operation.

        :return: The metadata of this Operation.
        :rtype: oci.data_connectivity.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Operation.

        :param metadata: The metadata of this Operation.
        :type: oci.data_connectivity.models.ObjectMetadata
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
