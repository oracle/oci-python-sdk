# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeriveEntitiesItem(object):
    """
    The request object for single derived Entity.
    """

    #: A constant which can be used with the mode property of a DeriveEntitiesItem.
    #: This constant has a value of "IN"
    MODE_IN = "IN"

    #: A constant which can be used with the mode property of a DeriveEntitiesItem.
    #: This constant has a value of "OUT"
    MODE_OUT = "OUT"

    def __init__(self, **kwargs):
        """
        Initializes a new DeriveEntitiesItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DeriveEntitiesItem.
        :type model_type: str

        :param mode:
            The value to assign to the mode property of this DeriveEntitiesItem.
            Allowed values for this property are: "IN", "OUT"
        :type mode: str

        :param referenced_data_object:
            The value to assign to the referenced_data_object property of this DeriveEntitiesItem.
        :type referenced_data_object: oci.data_connectivity.models.ReferencedDataObject

        """
        self.swagger_types = {
            'model_type': 'str',
            'mode': 'str',
            'referenced_data_object': 'ReferencedDataObject'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'mode': 'mode',
            'referenced_data_object': 'referencedDataObject'
        }

        self._model_type = None
        self._mode = None
        self._referenced_data_object = None

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this DeriveEntitiesItem.
        The model type of DeriveEntitiesRequestItem


        :return: The model_type of this DeriveEntitiesItem.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this DeriveEntitiesItem.
        The model type of DeriveEntitiesRequestItem


        :param model_type: The model_type of this DeriveEntitiesItem.
        :type: str
        """
        self._model_type = model_type

    @property
    def mode(self):
        """
        **[Required]** Gets the mode of this DeriveEntitiesItem.
        Determines whether derived entity is treated as source or target

        Allowed values for this property are: "IN", "OUT"


        :return: The mode of this DeriveEntitiesItem.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this DeriveEntitiesItem.
        Determines whether derived entity is treated as source or target


        :param mode: The mode of this DeriveEntitiesItem.
        :type: str
        """
        allowed_values = ["IN", "OUT"]
        if not value_allowed_none_or_none_sentinel(mode, allowed_values):
            raise ValueError(
                "Invalid value for `mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._mode = mode

    @property
    def referenced_data_object(self):
        """
        **[Required]** Gets the referenced_data_object of this DeriveEntitiesItem.

        :return: The referenced_data_object of this DeriveEntitiesItem.
        :rtype: oci.data_connectivity.models.ReferencedDataObject
        """
        return self._referenced_data_object

    @referenced_data_object.setter
    def referenced_data_object(self, referenced_data_object):
        """
        Sets the referenced_data_object of this DeriveEntitiesItem.

        :param referenced_data_object: The referenced_data_object of this DeriveEntitiesItem.
        :type: oci.data_connectivity.models.ReferencedDataObject
        """
        self._referenced_data_object = referenced_data_object

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
