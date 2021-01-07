# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataEntitySummary(object):
    """
    The data entity summary object.
    """

    #: A constant which can be used with the model_type property of a DataEntitySummary.
    #: This constant has a value of "VIEW_ENTITY"
    MODEL_TYPE_VIEW_ENTITY = "VIEW_ENTITY"

    #: A constant which can be used with the model_type property of a DataEntitySummary.
    #: This constant has a value of "TABLE_ENTITY"
    MODEL_TYPE_TABLE_ENTITY = "TABLE_ENTITY"

    #: A constant which can be used with the model_type property of a DataEntitySummary.
    #: This constant has a value of "FILE_ENTITY"
    MODEL_TYPE_FILE_ENTITY = "FILE_ENTITY"

    def __init__(self, **kwargs):
        """
        Initializes a new DataEntitySummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.DataEntitySummaryFromFile`
        * :class:`~oci.data_integration.models.DataEntitySummaryFromTable`
        * :class:`~oci.data_integration.models.DataEntitySummaryFromView`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataEntitySummary.
            Allowed values for this property are: "VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param metadata:
            The value to assign to the metadata property of this DataEntitySummary.
        :type metadata: oci.data_integration.models.ObjectMetadata

        """
        self.swagger_types = {
            'model_type': 'str',
            'metadata': 'ObjectMetadata'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'metadata': 'metadata'
        }

        self._model_type = None
        self._metadata = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'FILE_ENTITY':
            return 'DataEntitySummaryFromFile'

        if type == 'TABLE_ENTITY':
            return 'DataEntitySummaryFromTable'

        if type == 'VIEW_ENTITY':
            return 'DataEntitySummaryFromView'
        else:
            return 'DataEntitySummary'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this DataEntitySummary.
        The data entity type.

        Allowed values for this property are: "VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this DataEntitySummary.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this DataEntitySummary.
        The data entity type.


        :param model_type: The model_type of this DataEntitySummary.
        :type: str
        """
        allowed_values = ["VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def metadata(self):
        """
        Gets the metadata of this DataEntitySummary.

        :return: The metadata of this DataEntitySummary.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this DataEntitySummary.

        :param metadata: The metadata of this DataEntitySummary.
        :type: oci.data_integration.models.ObjectMetadata
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
