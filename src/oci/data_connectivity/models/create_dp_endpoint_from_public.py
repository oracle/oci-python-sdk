# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_dp_endpoint_details import CreateDpEndpointDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDpEndpointFromPublic(CreateDpEndpointDetails):
    """
    The details to create a public endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDpEndpointFromPublic object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.CreateDpEndpointFromPublic.model_type` attribute
        of this class is ``PUBLIC_END_POINT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateDpEndpointFromPublic.
            Allowed values for this property are: "PRIVATE_END_POINT", "PUBLIC_END_POINT"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateDpEndpointFromPublic.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateDpEndpointFromPublic.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateDpEndpointFromPublic.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateDpEndpointFromPublic.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateDpEndpointFromPublic.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateDpEndpointFromPublic.
        :type object_status: int

        :param object_version:
            The value to assign to the object_version property of this CreateDpEndpointFromPublic.
        :type object_version: int

        :param identifier:
            The value to assign to the identifier property of this CreateDpEndpointFromPublic.
        :type identifier: str

        :param data_assets:
            The value to assign to the data_assets property of this CreateDpEndpointFromPublic.
        :type data_assets: list[oci.data_connectivity.models.DataAsset]

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'object_version': 'int',
            'identifier': 'str',
            'data_assets': 'list[DataAsset]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'object_version': 'objectVersion',
            'identifier': 'identifier',
            'data_assets': 'dataAssets'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_status = None
        self._object_version = None
        self._identifier = None
        self._data_assets = None
        self._model_type = 'PUBLIC_END_POINT'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
