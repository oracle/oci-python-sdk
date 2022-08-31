# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataEntity(object):
    """
    The data entity object.
    """

    #: A constant which can be used with the model_type property of a DataEntity.
    #: This constant has a value of "VIEW_ENTITY"
    MODEL_TYPE_VIEW_ENTITY = "VIEW_ENTITY"

    #: A constant which can be used with the model_type property of a DataEntity.
    #: This constant has a value of "TABLE_ENTITY"
    MODEL_TYPE_TABLE_ENTITY = "TABLE_ENTITY"

    #: A constant which can be used with the model_type property of a DataEntity.
    #: This constant has a value of "FILE_ENTITY"
    MODEL_TYPE_FILE_ENTITY = "FILE_ENTITY"

    #: A constant which can be used with the model_type property of a DataEntity.
    #: This constant has a value of "DATA_STORE_ENTITY"
    MODEL_TYPE_DATA_STORE_ENTITY = "DATA_STORE_ENTITY"

    #: A constant which can be used with the model_type property of a DataEntity.
    #: This constant has a value of "SQL_ENTITY"
    MODEL_TYPE_SQL_ENTITY = "SQL_ENTITY"

    #: A constant which can be used with the model_type property of a DataEntity.
    #: This constant has a value of "DERIVED_ENTITY"
    MODEL_TYPE_DERIVED_ENTITY = "DERIVED_ENTITY"

    #: A constant which can be used with the model_type property of a DataEntity.
    #: This constant has a value of "MESSAGE_ENTITY"
    MODEL_TYPE_MESSAGE_ENTITY = "MESSAGE_ENTITY"

    def __init__(self, **kwargs):
        """
        Initializes a new DataEntity object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_connectivity.models.DataEntityFromTable`
        * :class:`~oci.data_connectivity.models.DataEntityFromDataStore`
        * :class:`~oci.data_connectivity.models.DataEntityFromView`
        * :class:`~oci.data_connectivity.models.DataEntityFromSql`
        * :class:`~oci.data_connectivity.models.DataEntityFromFile`
        * :class:`~oci.data_connectivity.models.DerivedEntity`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_properties:
            The value to assign to the entity_properties property of this DataEntity.
        :type entity_properties: dict(str, str)

        :param model_type:
            The value to assign to the model_type property of this DataEntity.
            Allowed values for this property are: "VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "DATA_STORE_ENTITY", "SQL_ENTITY", "DERIVED_ENTITY", "MESSAGE_ENTITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param metadata:
            The value to assign to the metadata property of this DataEntity.
        :type metadata: oci.data_connectivity.models.ObjectMetadata

        """
        self.swagger_types = {
            'entity_properties': 'dict(str, str)',
            'model_type': 'str',
            'metadata': 'ObjectMetadata'
        }

        self.attribute_map = {
            'entity_properties': 'entityProperties',
            'model_type': 'modelType',
            'metadata': 'metadata'
        }

        self._entity_properties = None
        self._model_type = None
        self._metadata = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'TABLE_ENTITY':
            return 'DataEntityFromTable'

        if type == 'DATA_STORE_ENTITY':
            return 'DataEntityFromDataStore'

        if type == 'VIEW_ENTITY':
            return 'DataEntityFromView'

        if type == 'SQL_ENTITY':
            return 'DataEntityFromSql'

        if type == 'FILE_ENTITY':
            return 'DataEntityFromFile'

        if type == 'DERIVED_ENTITY':
            return 'DerivedEntity'
        else:
            return 'DataEntity'

    @property
    def entity_properties(self):
        """
        Gets the entity_properties of this DataEntity.
        Map<String, String> for entity properties


        :return: The entity_properties of this DataEntity.
        :rtype: dict(str, str)
        """
        return self._entity_properties

    @entity_properties.setter
    def entity_properties(self, entity_properties):
        """
        Sets the entity_properties of this DataEntity.
        Map<String, String> for entity properties


        :param entity_properties: The entity_properties of this DataEntity.
        :type: dict(str, str)
        """
        self._entity_properties = entity_properties

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this DataEntity.
        The data entity type.

        Allowed values for this property are: "VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "DATA_STORE_ENTITY", "SQL_ENTITY", "DERIVED_ENTITY", "MESSAGE_ENTITY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this DataEntity.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this DataEntity.
        The data entity type.


        :param model_type: The model_type of this DataEntity.
        :type: str
        """
        allowed_values = ["VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "DATA_STORE_ENTITY", "SQL_ENTITY", "DERIVED_ENTITY", "MESSAGE_ENTITY"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def metadata(self):
        """
        Gets the metadata of this DataEntity.

        :return: The metadata of this DataEntity.
        :rtype: oci.data_connectivity.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this DataEntity.

        :param metadata: The metadata of this DataEntity.
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
