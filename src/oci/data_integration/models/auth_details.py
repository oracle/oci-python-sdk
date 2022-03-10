# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthDetails(object):
    """
    Authentication type to be used for Generic REST invocation. This is deprecated.
    """

    #: A constant which can be used with the model_type property of a AuthDetails.
    #: This constant has a value of "NO_AUTH_DETAILS"
    MODEL_TYPE_NO_AUTH_DETAILS = "NO_AUTH_DETAILS"

    #: A constant which can be used with the model_type property of a AuthDetails.
    #: This constant has a value of "RESOURCE_PRINCIPAL_AUTH_DETAILS"
    MODEL_TYPE_RESOURCE_PRINCIPAL_AUTH_DETAILS = "RESOURCE_PRINCIPAL_AUTH_DETAILS"

    def __init__(self, **kwargs):
        """
        Initializes a new AuthDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this AuthDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this AuthDetails.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this AuthDetails.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param model_type:
            The value to assign to the model_type property of this AuthDetails.
            Allowed values for this property are: "NO_AUTH_DETAILS", "RESOURCE_PRINCIPAL_AUTH_DETAILS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        """
        self.swagger_types = {
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'model_type': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'model_type': 'modelType'
        }

        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._model_type = None

    @property
    def key(self):
        """
        Gets the key of this AuthDetails.
        Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.


        :return: The key of this AuthDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this AuthDetails.
        Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.


        :param key: The key of this AuthDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this AuthDetails.
        The model version of an object.


        :return: The model_version of this AuthDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this AuthDetails.
        The model version of an object.


        :param model_version: The model_version of this AuthDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this AuthDetails.

        :return: The parent_ref of this AuthDetails.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this AuthDetails.

        :param parent_ref: The parent_ref of this AuthDetails.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def model_type(self):
        """
        Gets the model_type of this AuthDetails.
        The authentication mode to be used for Generic REST invocation.

        Allowed values for this property are: "NO_AUTH_DETAILS", "RESOURCE_PRINCIPAL_AUTH_DETAILS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this AuthDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this AuthDetails.
        The authentication mode to be used for Generic REST invocation.


        :param model_type: The model_type of this AuthDetails.
        :type: str
        """
        allowed_values = ["NO_AUTH_DETAILS", "RESOURCE_PRINCIPAL_AUTH_DETAILS"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
