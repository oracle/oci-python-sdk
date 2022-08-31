# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .typed_object import TypedObject
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OutputPort(TypedObject):
    """
    The output port details.
    """

    #: A constant which can be used with the port_type property of a OutputPort.
    #: This constant has a value of "DATA"
    PORT_TYPE_DATA = "DATA"

    #: A constant which can be used with the port_type property of a OutputPort.
    #: This constant has a value of "CONTROL"
    PORT_TYPE_CONTROL = "CONTROL"

    #: A constant which can be used with the port_type property of a OutputPort.
    #: This constant has a value of "MODEL"
    PORT_TYPE_MODEL = "MODEL"

    def __init__(self, **kwargs):
        """
        Initializes a new OutputPort object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.OutputPort.model_type` attribute
        of this class is ``OUTPUT_PORT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this OutputPort.
            Allowed values for this property are: "SHAPE", "SHAPE_FIELD", "NATIVE_SHAPE_FIELD"
        :type model_type: str

        :param key:
            The value to assign to the key property of this OutputPort.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this OutputPort.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this OutputPort.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param config_values:
            The value to assign to the config_values property of this OutputPort.
        :type config_values: oci.data_connectivity.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this OutputPort.
        :type object_status: int

        :param name:
            The value to assign to the name property of this OutputPort.
        :type name: str

        :param description:
            The value to assign to the description property of this OutputPort.
        :type description: str

        :param port_type:
            The value to assign to the port_type property of this OutputPort.
            Allowed values for this property are: "DATA", "CONTROL", "MODEL"
        :type port_type: str

        :param fields:
            The value to assign to the fields property of this OutputPort.
        :type fields: list[oci.data_connectivity.models.TypedObject]

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'config_values': 'ConfigValues',
            'object_status': 'int',
            'name': 'str',
            'description': 'str',
            'port_type': 'str',
            'fields': 'list[TypedObject]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'config_values': 'configValues',
            'object_status': 'objectStatus',
            'name': 'name',
            'description': 'description',
            'port_type': 'portType',
            'fields': 'fields'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._config_values = None
        self._object_status = None
        self._name = None
        self._description = None
        self._port_type = None
        self._fields = None
        self._model_type = 'OUTPUT_PORT'

    @property
    def port_type(self):
        """
        Gets the port_type of this OutputPort.
        The port details of the data asset type.

        Allowed values for this property are: "DATA", "CONTROL", "MODEL"


        :return: The port_type of this OutputPort.
        :rtype: str
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        """
        Sets the port_type of this OutputPort.
        The port details of the data asset type.


        :param port_type: The port_type of this OutputPort.
        :type: str
        """
        allowed_values = ["DATA", "CONTROL", "MODEL"]
        if not value_allowed_none_or_none_sentinel(port_type, allowed_values):
            raise ValueError(
                "Invalid value for `port_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._port_type = port_type

    @property
    def fields(self):
        """
        Gets the fields of this OutputPort.
        An array of fields.


        :return: The fields of this OutputPort.
        :rtype: list[oci.data_connectivity.models.TypedObject]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this OutputPort.
        An array of fields.


        :param fields: The fields of this OutputPort.
        :type: list[oci.data_connectivity.models.TypedObject]
        """
        self._fields = fields

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
