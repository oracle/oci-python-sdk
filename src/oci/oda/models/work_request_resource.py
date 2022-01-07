# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestResource(object):
    """
    A resource created or operated on by a work request.
    """

    #: A constant which can be used with the resource_action property of a WorkRequestResource.
    #: This constant has a value of "CREATE"
    RESOURCE_ACTION_CREATE = "CREATE"

    #: A constant which can be used with the resource_action property of a WorkRequestResource.
    #: This constant has a value of "DELETE"
    RESOURCE_ACTION_DELETE = "DELETE"

    #: A constant which can be used with the resource_action property of a WorkRequestResource.
    #: This constant has a value of "PURGE"
    RESOURCE_ACTION_PURGE = "PURGE"

    #: A constant which can be used with the resource_action property of a WorkRequestResource.
    #: This constant has a value of "RECOVER"
    RESOURCE_ACTION_RECOVER = "RECOVER"

    #: A constant which can be used with the resource_action property of a WorkRequestResource.
    #: This constant has a value of "STOP"
    RESOURCE_ACTION_STOP = "STOP"

    #: A constant which can be used with the resource_action property of a WorkRequestResource.
    #: This constant has a value of "START"
    RESOURCE_ACTION_START = "START"

    #: A constant which can be used with the resource_action property of a WorkRequestResource.
    #: This constant has a value of "CHANGE_COMPARTMENT"
    RESOURCE_ACTION_CHANGE_COMPARTMENT = "CHANGE_COMPARTMENT"

    #: A constant which can be used with the resource_action property of a WorkRequestResource.
    #: This constant has a value of "CREATE_ASSOCIATION"
    RESOURCE_ACTION_CREATE_ASSOCIATION = "CREATE_ASSOCIATION"

    #: A constant which can be used with the resource_action property of a WorkRequestResource.
    #: This constant has a value of "DELETE_ASSOCIATION"
    RESOURCE_ACTION_DELETE_ASSOCIATION = "DELETE_ASSOCIATION"

    #: A constant which can be used with the resource_action property of a WorkRequestResource.
    #: This constant has a value of "UPDATE_ENTITLEMENTS_FOR_CACCT"
    RESOURCE_ACTION_UPDATE_ENTITLEMENTS_FOR_CACCT = "UPDATE_ENTITLEMENTS_FOR_CACCT"

    #: A constant which can be used with the status property of a WorkRequestResource.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequestResource.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequestResource.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a WorkRequestResource.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a WorkRequestResource.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a WorkRequestResource.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestResource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_action:
            The value to assign to the resource_action property of this WorkRequestResource.
            Allowed values for this property are: "CREATE", "DELETE", "PURGE", "RECOVER", "STOP", "START", "CHANGE_COMPARTMENT", "CREATE_ASSOCIATION", "DELETE_ASSOCIATION", "UPDATE_ENTITLEMENTS_FOR_CACCT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_action: str

        :param resource_type:
            The value to assign to the resource_type property of this WorkRequestResource.
        :type resource_type: str

        :param resource_id:
            The value to assign to the resource_id property of this WorkRequestResource.
        :type resource_id: str

        :param status:
            The value to assign to the status property of this WorkRequestResource.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param status_message:
            The value to assign to the status_message property of this WorkRequestResource.
        :type status_message: str

        :param resource_uri:
            The value to assign to the resource_uri property of this WorkRequestResource.
        :type resource_uri: str

        """
        self.swagger_types = {
            'resource_action': 'str',
            'resource_type': 'str',
            'resource_id': 'str',
            'status': 'str',
            'status_message': 'str',
            'resource_uri': 'str'
        }

        self.attribute_map = {
            'resource_action': 'resourceAction',
            'resource_type': 'resourceType',
            'resource_id': 'resourceId',
            'status': 'status',
            'status_message': 'statusMessage',
            'resource_uri': 'resourceUri'
        }

        self._resource_action = None
        self._resource_type = None
        self._resource_id = None
        self._status = None
        self._status_message = None
        self._resource_uri = None

    @property
    def resource_action(self):
        """
        **[Required]** Gets the resource_action of this WorkRequestResource.
        The action to take against the Digital Assistant instance.

        Allowed values for this property are: "CREATE", "DELETE", "PURGE", "RECOVER", "STOP", "START", "CHANGE_COMPARTMENT", "CREATE_ASSOCIATION", "DELETE_ASSOCIATION", "UPDATE_ENTITLEMENTS_FOR_CACCT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_action of this WorkRequestResource.
        :rtype: str
        """
        return self._resource_action

    @resource_action.setter
    def resource_action(self, resource_action):
        """
        Sets the resource_action of this WorkRequestResource.
        The action to take against the Digital Assistant instance.


        :param resource_action: The resource_action of this WorkRequestResource.
        :type: str
        """
        allowed_values = ["CREATE", "DELETE", "PURGE", "RECOVER", "STOP", "START", "CHANGE_COMPARTMENT", "CREATE_ASSOCIATION", "DELETE_ASSOCIATION", "UPDATE_ENTITLEMENTS_FOR_CACCT"]
        if not value_allowed_none_or_none_sentinel(resource_action, allowed_values):
            resource_action = 'UNKNOWN_ENUM_VALUE'
        self._resource_action = resource_action

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this WorkRequestResource.
        The resource type that the work request affects.


        :return: The resource_type of this WorkRequestResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this WorkRequestResource.
        The resource type that the work request affects.


        :param resource_type: The resource_type of this WorkRequestResource.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this WorkRequestResource.
        The identifier of the Digital Assistant instance that is the subject of the request.


        :return: The resource_id of this WorkRequestResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this WorkRequestResource.
        The identifier of the Digital Assistant instance that is the subject of the request.


        :param resource_id: The resource_id of this WorkRequestResource.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequestResource.
        The current state of the work request. The `SUCCEEDED`, `FAILED`, AND `CANCELED` states
        correspond to the action being performed.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequestResource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequestResource.
        The current state of the work request. The `SUCCEEDED`, `FAILED`, AND `CANCELED` states
        correspond to the action being performed.


        :param status: The status of this WorkRequestResource.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def status_message(self):
        """
        Gets the status_message of this WorkRequestResource.
        Short message providing more detail for the current status. For example, if an operation fails
        this may include information about the reason for the failure and a possible resolution.


        :return: The status_message of this WorkRequestResource.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this WorkRequestResource.
        Short message providing more detail for the current status. For example, if an operation fails
        this may include information about the reason for the failure and a possible resolution.


        :param status_message: The status_message of this WorkRequestResource.
        :type: str
        """
        self._status_message = status_message

    @property
    def resource_uri(self):
        """
        Gets the resource_uri of this WorkRequestResource.
        The URI path that the user can do a GET on to access the resource metadata.


        :return: The resource_uri of this WorkRequestResource.
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """
        Sets the resource_uri of this WorkRequestResource.
        The URI path that the user can do a GET on to access the resource metadata.


        :param resource_uri: The resource_uri of this WorkRequestResource.
        :type: str
        """
        self._resource_uri = resource_uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
