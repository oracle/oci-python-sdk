# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataEntityDetails(object):
    """
    The data entity details object.
    """

    #: A constant which can be used with the model_type property of a DataEntityDetails.
    #: This constant has a value of "VIEW_ENTITY"
    MODEL_TYPE_VIEW_ENTITY = "VIEW_ENTITY"

    #: A constant which can be used with the model_type property of a DataEntityDetails.
    #: This constant has a value of "TABLE_ENTITY"
    MODEL_TYPE_TABLE_ENTITY = "TABLE_ENTITY"

    #: A constant which can be used with the model_type property of a DataEntityDetails.
    #: This constant has a value of "FILE_ENTITY"
    MODEL_TYPE_FILE_ENTITY = "FILE_ENTITY"

    #: A constant which can be used with the model_type property of a DataEntityDetails.
    #: This constant has a value of "SQL_ENTITY"
    MODEL_TYPE_SQL_ENTITY = "SQL_ENTITY"

    #: A constant which can be used with the model_type property of a DataEntityDetails.
    #: This constant has a value of "DATA_STORE_ENTITY"
    MODEL_TYPE_DATA_STORE_ENTITY = "DATA_STORE_ENTITY"

    def __init__(self, **kwargs):
        """
        Initializes a new DataEntityDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.DataEntityFromFileEntityDetails`
        * :class:`~oci.data_integration.models.DataEntityFromViewEntityDetails`
        * :class:`~oci.data_integration.models.DataEntityFromSqlEntityDetails`
        * :class:`~oci.data_integration.models.DataEntityFromDataStoreEntityDetails`
        * :class:`~oci.data_integration.models.DataEntityFromTableEntityDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataEntityDetails.
            Allowed values for this property are: "VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "SQL_ENTITY", "DATA_STORE_ENTITY"
        :type model_type: str

        """
        self.swagger_types = {
            'model_type': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType'
        }

        self._model_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'FILE_ENTITY':
            return 'DataEntityFromFileEntityDetails'

        if type == 'VIEW_ENTITY':
            return 'DataEntityFromViewEntityDetails'

        if type == 'SQL_ENTITY':
            return 'DataEntityFromSqlEntityDetails'

        if type == 'DATA_STORE_ENTITY':
            return 'DataEntityFromDataStoreEntityDetails'

        if type == 'TABLE_ENTITY':
            return 'DataEntityFromTableEntityDetails'
        else:
            return 'DataEntityDetails'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this DataEntityDetails.
        The data entity type.

        Allowed values for this property are: "VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "SQL_ENTITY", "DATA_STORE_ENTITY"


        :return: The model_type of this DataEntityDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this DataEntityDetails.
        The data entity type.


        :param model_type: The model_type of this DataEntityDetails.
        :type: str
        """
        allowed_values = ["VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "SQL_ENTITY", "DATA_STORE_ENTITY"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            raise ValueError(
                "Invalid value for `model_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._model_type = model_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
