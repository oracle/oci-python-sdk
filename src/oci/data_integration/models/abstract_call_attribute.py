# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AbstractCallAttribute(object):
    """
    The abstract write attribute.
    """

    #: A constant which can be used with the model_type property of a AbstractCallAttribute.
    #: This constant has a value of "BIP_CALL_ATTRIBUTE"
    MODEL_TYPE_BIP_CALL_ATTRIBUTE = "BIP_CALL_ATTRIBUTE"

    #: A constant which can be used with the model_type property of a AbstractCallAttribute.
    #: This constant has a value of "GENERIC_REST_CALL_ATTRIBUTE"
    MODEL_TYPE_GENERIC_REST_CALL_ATTRIBUTE = "GENERIC_REST_CALL_ATTRIBUTE"

    def __init__(self, **kwargs):
        """
        Initializes a new AbstractCallAttribute object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.BipCallAttribute`
        * :class:`~oci.data_integration.models.GenericRestCallAttribute`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this AbstractCallAttribute.
            Allowed values for this property are: "BIP_CALL_ATTRIBUTE", "GENERIC_REST_CALL_ATTRIBUTE"
        :type model_type: str

        :param fetch_size:
            The value to assign to the fetch_size property of this AbstractCallAttribute.
        :type fetch_size: int

        """
        self.swagger_types = {
            'model_type': 'str',
            'fetch_size': 'int'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'fetch_size': 'fetchSize'
        }

        self._model_type = None
        self._fetch_size = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'BIP_CALL_ATTRIBUTE':
            return 'BipCallAttribute'

        if type == 'GENERIC_REST_CALL_ATTRIBUTE':
            return 'GenericRestCallAttribute'
        else:
            return 'AbstractCallAttribute'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this AbstractCallAttribute.
        The type of the abstract call attribute.

        Allowed values for this property are: "BIP_CALL_ATTRIBUTE", "GENERIC_REST_CALL_ATTRIBUTE"


        :return: The model_type of this AbstractCallAttribute.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this AbstractCallAttribute.
        The type of the abstract call attribute.


        :param model_type: The model_type of this AbstractCallAttribute.
        :type: str
        """
        allowed_values = ["BIP_CALL_ATTRIBUTE", "GENERIC_REST_CALL_ATTRIBUTE"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            raise ValueError(
                "Invalid value for `model_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._model_type = model_type

    @property
    def fetch_size(self):
        """
        Gets the fetch_size of this AbstractCallAttribute.
        The fetch size for reading.


        :return: The fetch_size of this AbstractCallAttribute.
        :rtype: int
        """
        return self._fetch_size

    @fetch_size.setter
    def fetch_size(self, fetch_size):
        """
        Sets the fetch_size of this AbstractCallAttribute.
        The fetch size for reading.


        :param fetch_size: The fetch_size of this AbstractCallAttribute.
        :type: int
        """
        self._fetch_size = fetch_size

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
