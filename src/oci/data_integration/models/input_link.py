# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .flow_port_link import FlowPortLink
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InputLink(FlowPortLink):
    """
    Details about the incoming data to an operator in a data flow design.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InputLink object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.InputLink.model_type` attribute
        of this class is ``INPUT_LINK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this InputLink.
            Allowed values for this property are: "CONDITIONAL_INPUT_LINK", "OUTPUT_LINK", "INPUT_LINK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this InputLink.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this InputLink.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this InputLink.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param object_status:
            The value to assign to the object_status property of this InputLink.
        :type object_status: int

        :param description:
            The value to assign to the description property of this InputLink.
        :type description: str

        :param port:
            The value to assign to the port property of this InputLink.
        :type port: str

        :param from_link:
            The value to assign to the from_link property of this InputLink.
        :type from_link: str

        :param field_map:
            The value to assign to the field_map property of this InputLink.
        :type field_map: oci.data_integration.models.FieldMap

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'object_status': 'int',
            'description': 'str',
            'port': 'str',
            'from_link': 'str',
            'field_map': 'FieldMap'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'object_status': 'objectStatus',
            'description': 'description',
            'port': 'port',
            'from_link': 'fromLink',
            'field_map': 'fieldMap'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._object_status = None
        self._description = None
        self._port = None
        self._from_link = None
        self._field_map = None
        self._model_type = 'INPUT_LINK'

    @property
    def from_link(self):
        """
        Gets the from_link of this InputLink.
        The from link reference.


        :return: The from_link of this InputLink.
        :rtype: str
        """
        return self._from_link

    @from_link.setter
    def from_link(self, from_link):
        """
        Sets the from_link of this InputLink.
        The from link reference.


        :param from_link: The from_link of this InputLink.
        :type: str
        """
        self._from_link = from_link

    @property
    def field_map(self):
        """
        Gets the field_map of this InputLink.

        :return: The field_map of this InputLink.
        :rtype: oci.data_integration.models.FieldMap
        """
        return self._field_map

    @field_map.setter
    def field_map(self, field_map):
        """
        Sets the field_map of this InputLink.

        :param field_map: The field_map of this InputLink.
        :type: oci.data_integration.models.FieldMap
        """
        self._field_map = field_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
