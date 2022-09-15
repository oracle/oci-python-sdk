# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSourceApplicationInfo(object):
    """
    The information about the application.
    """

    #: A constant which can be used with the copy_type property of a CreateSourceApplicationInfo.
    #: This constant has a value of "CONNECTED"
    COPY_TYPE_CONNECTED = "CONNECTED"

    #: A constant which can be used with the copy_type property of a CreateSourceApplicationInfo.
    #: This constant has a value of "DISCONNECTED"
    COPY_TYPE_DISCONNECTED = "DISCONNECTED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSourceApplicationInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param workspace_id:
            The value to assign to the workspace_id property of this CreateSourceApplicationInfo.
        :type workspace_id: str

        :param application_key:
            The value to assign to the application_key property of this CreateSourceApplicationInfo.
        :type application_key: str

        :param copy_type:
            The value to assign to the copy_type property of this CreateSourceApplicationInfo.
            Allowed values for this property are: "CONNECTED", "DISCONNECTED"
        :type copy_type: str

        """
        self.swagger_types = {
            'workspace_id': 'str',
            'application_key': 'str',
            'copy_type': 'str'
        }

        self.attribute_map = {
            'workspace_id': 'workspaceId',
            'application_key': 'applicationKey',
            'copy_type': 'copyType'
        }

        self._workspace_id = None
        self._application_key = None
        self._copy_type = None

    @property
    def workspace_id(self):
        """
        Gets the workspace_id of this CreateSourceApplicationInfo.
        The OCID of the workspace containing the application. This allows cross workspace deployment to publish an application from a different workspace into the current workspace specified in this operation.


        :return: The workspace_id of this CreateSourceApplicationInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """
        Sets the workspace_id of this CreateSourceApplicationInfo.
        The OCID of the workspace containing the application. This allows cross workspace deployment to publish an application from a different workspace into the current workspace specified in this operation.


        :param workspace_id: The workspace_id of this CreateSourceApplicationInfo.
        :type: str
        """
        self._workspace_id = workspace_id

    @property
    def application_key(self):
        """
        Gets the application_key of this CreateSourceApplicationInfo.
        The source application key to use when creating the application.


        :return: The application_key of this CreateSourceApplicationInfo.
        :rtype: str
        """
        return self._application_key

    @application_key.setter
    def application_key(self, application_key):
        """
        Sets the application_key of this CreateSourceApplicationInfo.
        The source application key to use when creating the application.


        :param application_key: The application_key of this CreateSourceApplicationInfo.
        :type: str
        """
        self._application_key = application_key

    @property
    def copy_type(self):
        """
        Gets the copy_type of this CreateSourceApplicationInfo.
        Parameter to specify the link between SOURCE and TARGET application after copying. CONNECTED    - Indicate that TARGET application is conneced to SOURCE and can be synced after copy. DISCONNECTED - Indicate that TARGET application is not conneced to SOURCE and can evolve independently.

        Allowed values for this property are: "CONNECTED", "DISCONNECTED"


        :return: The copy_type of this CreateSourceApplicationInfo.
        :rtype: str
        """
        return self._copy_type

    @copy_type.setter
    def copy_type(self, copy_type):
        """
        Sets the copy_type of this CreateSourceApplicationInfo.
        Parameter to specify the link between SOURCE and TARGET application after copying. CONNECTED    - Indicate that TARGET application is conneced to SOURCE and can be synced after copy. DISCONNECTED - Indicate that TARGET application is not conneced to SOURCE and can evolve independently.


        :param copy_type: The copy_type of this CreateSourceApplicationInfo.
        :type: str
        """
        allowed_values = ["CONNECTED", "DISCONNECTED"]
        if not value_allowed_none_or_none_sentinel(copy_type, allowed_values):
            raise ValueError(
                "Invalid value for `copy_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._copy_type = copy_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
