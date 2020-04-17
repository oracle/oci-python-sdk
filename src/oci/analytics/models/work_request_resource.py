# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestResource(object):
    """
    WorkRequestResource model.
    """

    #: A constant which can be used with the action_result property of a WorkRequestResource.
    #: This constant has a value of "COMPARTMENT_CHANGED"
    ACTION_RESULT_COMPARTMENT_CHANGED = "COMPARTMENT_CHANGED"

    #: A constant which can be used with the action_result property of a WorkRequestResource.
    #: This constant has a value of "CREATED"
    ACTION_RESULT_CREATED = "CREATED"

    #: A constant which can be used with the action_result property of a WorkRequestResource.
    #: This constant has a value of "DELETED"
    ACTION_RESULT_DELETED = "DELETED"

    #: A constant which can be used with the action_result property of a WorkRequestResource.
    #: This constant has a value of "STARTED"
    ACTION_RESULT_STARTED = "STARTED"

    #: A constant which can be used with the action_result property of a WorkRequestResource.
    #: This constant has a value of "STOPPED"
    ACTION_RESULT_STOPPED = "STOPPED"

    #: A constant which can be used with the action_result property of a WorkRequestResource.
    #: This constant has a value of "SCALED"
    ACTION_RESULT_SCALED = "SCALED"

    #: A constant which can be used with the action_result property of a WorkRequestResource.
    #: This constant has a value of "NONE"
    ACTION_RESULT_NONE = "NONE"

    #: A constant which can be used with the resource_type property of a WorkRequestResource.
    #: This constant has a value of "ANALYTICS_INSTANCE"
    RESOURCE_TYPE_ANALYTICS_INSTANCE = "ANALYTICS_INSTANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestResource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_result:
            The value to assign to the action_result property of this WorkRequestResource.
            Allowed values for this property are: "COMPARTMENT_CHANGED", "CREATED", "DELETED", "STARTED", "STOPPED", "SCALED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action_result: str

        :param resource_type:
            The value to assign to the resource_type property of this WorkRequestResource.
            Allowed values for this property are: "ANALYTICS_INSTANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param identifier:
            The value to assign to the identifier property of this WorkRequestResource.
        :type identifier: str

        :param resource_uri:
            The value to assign to the resource_uri property of this WorkRequestResource.
        :type resource_uri: str

        :param metadata:
            The value to assign to the metadata property of this WorkRequestResource.
        :type metadata: dict(str, str)

        """
        self.swagger_types = {
            'action_result': 'str',
            'resource_type': 'str',
            'identifier': 'str',
            'resource_uri': 'str',
            'metadata': 'dict(str, str)'
        }

        self.attribute_map = {
            'action_result': 'actionResult',
            'resource_type': 'resourceType',
            'identifier': 'identifier',
            'resource_uri': 'resourceUri',
            'metadata': 'metadata'
        }

        self._action_result = None
        self._resource_type = None
        self._identifier = None
        self._resource_uri = None
        self._metadata = None

    @property
    def action_result(self):
        """
        **[Required]** Gets the action_result of this WorkRequestResource.
        The way in which this resource was affected by this work request.

        Allowed values for this property are: "COMPARTMENT_CHANGED", "CREATED", "DELETED", "STARTED", "STOPPED", "SCALED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action_result of this WorkRequestResource.
        :rtype: str
        """
        return self._action_result

    @action_result.setter
    def action_result(self, action_result):
        """
        Sets the action_result of this WorkRequestResource.
        The way in which this resource was affected by this work request.


        :param action_result: The action_result of this WorkRequestResource.
        :type: str
        """
        allowed_values = ["COMPARTMENT_CHANGED", "CREATED", "DELETED", "STARTED", "STOPPED", "SCALED", "NONE"]
        if not value_allowed_none_or_none_sentinel(action_result, allowed_values):
            action_result = 'UNKNOWN_ENUM_VALUE'
        self._action_result = action_result

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this WorkRequestResource.
        The type of the resource the work request is affecting.

        Allowed values for this property are: "ANALYTICS_INSTANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_type of this WorkRequestResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this WorkRequestResource.
        The type of the resource the work request is affecting.


        :param resource_type: The resource_type of this WorkRequestResource.
        :type: str
        """
        allowed_values = ["ANALYTICS_INSTANCE"]
        if not value_allowed_none_or_none_sentinel(resource_type, allowed_values):
            resource_type = 'UNKNOWN_ENUM_VALUE'
        self._resource_type = resource_type

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this WorkRequestResource.
        The OCID of the resource the work request is affecting.


        :return: The identifier of this WorkRequestResource.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this WorkRequestResource.
        The OCID of the resource the work request is affecting.


        :param identifier: The identifier of this WorkRequestResource.
        :type: str
        """
        self._identifier = identifier

    @property
    def resource_uri(self):
        """
        **[Required]** Gets the resource_uri of this WorkRequestResource.
        The URI of the affected resource.


        :return: The resource_uri of this WorkRequestResource.
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """
        Sets the resource_uri of this WorkRequestResource.
        The URI of the affected resource.


        :param resource_uri: The resource_uri of this WorkRequestResource.
        :type: str
        """
        self._resource_uri = resource_uri

    @property
    def metadata(self):
        """
        Gets the metadata of this WorkRequestResource.
        Additional metadata of the resource.


        :return: The metadata of this WorkRequestResource.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this WorkRequestResource.
        Additional metadata of the resource.


        :param metadata: The metadata of this WorkRequestResource.
        :type: dict(str, str)
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
