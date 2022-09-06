# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AbstractDataOperationConfig(object):
    """
    The information about the data operation.
    """

    #: A constant which can be used with the model_type property of a AbstractDataOperationConfig.
    #: This constant has a value of "READ_OPERATION_CONFIG"
    MODEL_TYPE_READ_OPERATION_CONFIG = "READ_OPERATION_CONFIG"

    #: A constant which can be used with the model_type property of a AbstractDataOperationConfig.
    #: This constant has a value of "WRITE_OPERATION_CONFIG"
    MODEL_TYPE_WRITE_OPERATION_CONFIG = "WRITE_OPERATION_CONFIG"

    def __init__(self, **kwargs):
        """
        Initializes a new AbstractDataOperationConfig object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_connectivity.models.WriteOperationConfig`
        * :class:`~oci.data_connectivity.models.ReadOperationConfig`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this AbstractDataOperationConfig.
            Allowed values for this property are: "READ_OPERATION_CONFIG", "WRITE_OPERATION_CONFIG"
        :type model_type: str

        :param derived_attributes:
            The value to assign to the derived_attributes property of this AbstractDataOperationConfig.
        :type derived_attributes: dict(str, str)

        """
        self.swagger_types = {
            'model_type': 'str',
            'derived_attributes': 'dict(str, str)'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'derived_attributes': 'derivedAttributes'
        }

        self._model_type = None
        self._derived_attributes = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'WRITE_OPERATION_CONFIG':
            return 'WriteOperationConfig'

        if type == 'READ_OPERATION_CONFIG':
            return 'ReadOperationConfig'
        else:
            return 'AbstractDataOperationConfig'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this AbstractDataOperationConfig.
        The type of data operation.

        Allowed values for this property are: "READ_OPERATION_CONFIG", "WRITE_OPERATION_CONFIG"


        :return: The model_type of this AbstractDataOperationConfig.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this AbstractDataOperationConfig.
        The type of data operation.


        :param model_type: The model_type of this AbstractDataOperationConfig.
        :type: str
        """
        allowed_values = ["READ_OPERATION_CONFIG", "WRITE_OPERATION_CONFIG"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            raise ValueError(
                "Invalid value for `model_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._model_type = model_type

    @property
    def derived_attributes(self):
        """
        Gets the derived_attributes of this AbstractDataOperationConfig.
        this map is used for passing BIP report/REST parameter values.


        :return: The derived_attributes of this AbstractDataOperationConfig.
        :rtype: dict(str, str)
        """
        return self._derived_attributes

    @derived_attributes.setter
    def derived_attributes(self, derived_attributes):
        """
        Sets the derived_attributes of this AbstractDataOperationConfig.
        this map is used for passing BIP report/REST parameter values.


        :param derived_attributes: The derived_attributes of this AbstractDataOperationConfig.
        :type: dict(str, str)
        """
        self._derived_attributes = derived_attributes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
