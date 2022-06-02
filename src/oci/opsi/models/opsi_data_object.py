# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpsiDataObject(object):
    """
    OPSI data object.
    """

    #: A constant which can be used with the data_object_type property of a OpsiDataObject.
    #: This constant has a value of "DATABASE_INSIGHTS_DATA_OBJECT"
    DATA_OBJECT_TYPE_DATABASE_INSIGHTS_DATA_OBJECT = "DATABASE_INSIGHTS_DATA_OBJECT"

    #: A constant which can be used with the data_object_type property of a OpsiDataObject.
    #: This constant has a value of "HOST_INSIGHTS_DATA_OBJECT"
    DATA_OBJECT_TYPE_HOST_INSIGHTS_DATA_OBJECT = "HOST_INSIGHTS_DATA_OBJECT"

    #: A constant which can be used with the data_object_type property of a OpsiDataObject.
    #: This constant has a value of "EXADATA_INSIGHTS_DATA_OBJECT"
    DATA_OBJECT_TYPE_EXADATA_INSIGHTS_DATA_OBJECT = "EXADATA_INSIGHTS_DATA_OBJECT"

    def __init__(self, **kwargs):
        """
        Initializes a new OpsiDataObject object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.HostInsightsDataObject`
        * :class:`~oci.opsi.models.ExadataInsightsDataObject`
        * :class:`~oci.opsi.models.DatabaseInsightsDataObject`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param identifier:
            The value to assign to the identifier property of this OpsiDataObject.
        :type identifier: str

        :param data_object_type:
            The value to assign to the data_object_type property of this OpsiDataObject.
            Allowed values for this property are: "DATABASE_INSIGHTS_DATA_OBJECT", "HOST_INSIGHTS_DATA_OBJECT", "EXADATA_INSIGHTS_DATA_OBJECT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_object_type: str

        :param display_name:
            The value to assign to the display_name property of this OpsiDataObject.
        :type display_name: str

        :param description:
            The value to assign to the description property of this OpsiDataObject.
        :type description: str

        :param columns_metadata:
            The value to assign to the columns_metadata property of this OpsiDataObject.
        :type columns_metadata: list[oci.opsi.models.DataObjectColumnMetadata]

        """
        self.swagger_types = {
            'identifier': 'str',
            'data_object_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'columns_metadata': 'list[DataObjectColumnMetadata]'
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'data_object_type': 'dataObjectType',
            'display_name': 'displayName',
            'description': 'description',
            'columns_metadata': 'columnsMetadata'
        }

        self._identifier = None
        self._data_object_type = None
        self._display_name = None
        self._description = None
        self._columns_metadata = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['dataObjectType']

        if type == 'HOST_INSIGHTS_DATA_OBJECT':
            return 'HostInsightsDataObject'

        if type == 'EXADATA_INSIGHTS_DATA_OBJECT':
            return 'ExadataInsightsDataObject'

        if type == 'DATABASE_INSIGHTS_DATA_OBJECT':
            return 'DatabaseInsightsDataObject'
        else:
            return 'OpsiDataObject'

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this OpsiDataObject.
        Unique identifier of OPSI data object.


        :return: The identifier of this OpsiDataObject.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this OpsiDataObject.
        Unique identifier of OPSI data object.


        :param identifier: The identifier of this OpsiDataObject.
        :type: str
        """
        self._identifier = identifier

    @property
    def data_object_type(self):
        """
        **[Required]** Gets the data_object_type of this OpsiDataObject.
        Type of OPSI data object.

        Allowed values for this property are: "DATABASE_INSIGHTS_DATA_OBJECT", "HOST_INSIGHTS_DATA_OBJECT", "EXADATA_INSIGHTS_DATA_OBJECT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_object_type of this OpsiDataObject.
        :rtype: str
        """
        return self._data_object_type

    @data_object_type.setter
    def data_object_type(self, data_object_type):
        """
        Sets the data_object_type of this OpsiDataObject.
        Type of OPSI data object.


        :param data_object_type: The data_object_type of this OpsiDataObject.
        :type: str
        """
        allowed_values = ["DATABASE_INSIGHTS_DATA_OBJECT", "HOST_INSIGHTS_DATA_OBJECT", "EXADATA_INSIGHTS_DATA_OBJECT"]
        if not value_allowed_none_or_none_sentinel(data_object_type, allowed_values):
            data_object_type = 'UNKNOWN_ENUM_VALUE'
        self._data_object_type = data_object_type

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OpsiDataObject.
        User-friendly name of OPSI data object.


        :return: The display_name of this OpsiDataObject.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OpsiDataObject.
        User-friendly name of OPSI data object.


        :param display_name: The display_name of this OpsiDataObject.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this OpsiDataObject.
        Description of OPSI data object.


        :return: The description of this OpsiDataObject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OpsiDataObject.
        Description of OPSI data object.


        :param description: The description of this OpsiDataObject.
        :type: str
        """
        self._description = description

    @property
    def columns_metadata(self):
        """
        **[Required]** Gets the columns_metadata of this OpsiDataObject.
        Metadata of columns in a data object.


        :return: The columns_metadata of this OpsiDataObject.
        :rtype: list[oci.opsi.models.DataObjectColumnMetadata]
        """
        return self._columns_metadata

    @columns_metadata.setter
    def columns_metadata(self, columns_metadata):
        """
        Sets the columns_metadata of this OpsiDataObject.
        Metadata of columns in a data object.


        :param columns_metadata: The columns_metadata of this OpsiDataObject.
        :type: list[oci.opsi.models.DataObjectColumnMetadata]
        """
        self._columns_metadata = columns_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
