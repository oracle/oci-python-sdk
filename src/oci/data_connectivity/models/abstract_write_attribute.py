# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AbstractWriteAttribute(object):
    """
    The abstract write attribute.
    """

    #: A constant which can be used with the model_type property of a AbstractWriteAttribute.
    #: This constant has a value of "ORACLE_WRITE_ATTRIBUTE"
    MODEL_TYPE_ORACLE_WRITE_ATTRIBUTE = "ORACLE_WRITE_ATTRIBUTE"

    #: A constant which can be used with the model_type property of a AbstractWriteAttribute.
    #: This constant has a value of "ORACLE_ATP_WRITE_ATTRIBUTE"
    MODEL_TYPE_ORACLE_ATP_WRITE_ATTRIBUTE = "ORACLE_ATP_WRITE_ATTRIBUTE"

    #: A constant which can be used with the model_type property of a AbstractWriteAttribute.
    #: This constant has a value of "ORACLE_ADWC_WRITE_ATTRIBUTE"
    MODEL_TYPE_ORACLE_ADWC_WRITE_ATTRIBUTE = "ORACLE_ADWC_WRITE_ATTRIBUTE"

    #: A constant which can be used with the model_type property of a AbstractWriteAttribute.
    #: This constant has a value of "OBJECT_STORAGE_WRITE_ATTRIBUTE"
    MODEL_TYPE_OBJECT_STORAGE_WRITE_ATTRIBUTE = "OBJECT_STORAGE_WRITE_ATTRIBUTE"

    #: A constant which can be used with the model_type property of a AbstractWriteAttribute.
    #: This constant has a value of "HDFS_WRITE_ATTRIBUTE"
    MODEL_TYPE_HDFS_WRITE_ATTRIBUTE = "HDFS_WRITE_ATTRIBUTE"

    def __init__(self, **kwargs):
        """
        Initializes a new AbstractWriteAttribute object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_connectivity.models.OracleAtpWriteAttributes`
        * :class:`~oci.data_connectivity.models.HdfsWriteAttributes`
        * :class:`~oci.data_connectivity.models.OracleWriteAttributes`
        * :class:`~oci.data_connectivity.models.OracleAdwcWriteAttributes`
        * :class:`~oci.data_connectivity.models.ObjectStorageWriteAttributes`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this AbstractWriteAttribute.
            Allowed values for this property are: "ORACLE_WRITE_ATTRIBUTE", "ORACLE_ATP_WRITE_ATTRIBUTE", "ORACLE_ADWC_WRITE_ATTRIBUTE", "OBJECT_STORAGE_WRITE_ATTRIBUTE", "HDFS_WRITE_ATTRIBUTE"
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

        if type == 'ORACLE_ATP_WRITE_ATTRIBUTE':
            return 'OracleAtpWriteAttributes'

        if type == 'HDFS_WRITE_ATTRIBUTE':
            return 'HdfsWriteAttributes'

        if type == 'ORACLE_WRITE_ATTRIBUTE':
            return 'OracleWriteAttributes'

        if type == 'ORACLE_ADWC_WRITE_ATTRIBUTE':
            return 'OracleAdwcWriteAttributes'

        if type == 'OBJECT_STORAGE_WRITE_ATTRIBUTE':
            return 'ObjectStorageWriteAttributes'
        else:
            return 'AbstractWriteAttribute'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this AbstractWriteAttribute.
        The type of the abstract write attribute.

        Allowed values for this property are: "ORACLE_WRITE_ATTRIBUTE", "ORACLE_ATP_WRITE_ATTRIBUTE", "ORACLE_ADWC_WRITE_ATTRIBUTE", "OBJECT_STORAGE_WRITE_ATTRIBUTE", "HDFS_WRITE_ATTRIBUTE"


        :return: The model_type of this AbstractWriteAttribute.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this AbstractWriteAttribute.
        The type of the abstract write attribute.


        :param model_type: The model_type of this AbstractWriteAttribute.
        :type: str
        """
        allowed_values = ["ORACLE_WRITE_ATTRIBUTE", "ORACLE_ATP_WRITE_ATTRIBUTE", "ORACLE_ADWC_WRITE_ATTRIBUTE", "OBJECT_STORAGE_WRITE_ATTRIBUTE", "HDFS_WRITE_ATTRIBUTE"]
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
