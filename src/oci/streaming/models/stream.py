# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Stream(object):
    """
    Detailed representation of a stream, including all its partitions.
    """

    #: A constant which can be used with the lifecycle_state property of a Stream.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Stream.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Stream.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Stream.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Stream.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Stream.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new Stream object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Stream.
        :type name: str

        :param id:
            The value to assign to the id property of this Stream.
        :type id: str

        :param partitions:
            The value to assign to the partitions property of this Stream.
        :type partitions: int

        :param retention_in_hours:
            The value to assign to the retention_in_hours property of this Stream.
        :type retention_in_hours: int

        :param compartment_id:
            The value to assign to the compartment_id property of this Stream.
        :type compartment_id: str

        :param stream_pool_id:
            The value to assign to the stream_pool_id property of this Stream.
        :type stream_pool_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Stream.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this Stream.
        :type lifecycle_state_details: str

        :param time_created:
            The value to assign to the time_created property of this Stream.
        :type time_created: datetime

        :param messages_endpoint:
            The value to assign to the messages_endpoint property of this Stream.
        :type messages_endpoint: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Stream.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Stream.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'id': 'str',
            'partitions': 'int',
            'retention_in_hours': 'int',
            'compartment_id': 'str',
            'stream_pool_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'time_created': 'datetime',
            'messages_endpoint': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'partitions': 'partitions',
            'retention_in_hours': 'retentionInHours',
            'compartment_id': 'compartmentId',
            'stream_pool_id': 'streamPoolId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'time_created': 'timeCreated',
            'messages_endpoint': 'messagesEndpoint',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._id = None
        self._partitions = None
        self._retention_in_hours = None
        self._compartment_id = None
        self._stream_pool_id = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._time_created = None
        self._messages_endpoint = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Stream.
        The name of the stream. Avoid entering confidential information.

        Example: `TelemetryEvents`


        :return: The name of this Stream.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Stream.
        The name of the stream. Avoid entering confidential information.

        Example: `TelemetryEvents`


        :param name: The name of this Stream.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Stream.
        The OCID of the stream.


        :return: The id of this Stream.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Stream.
        The OCID of the stream.


        :param id: The id of this Stream.
        :type: str
        """
        self._id = id

    @property
    def partitions(self):
        """
        **[Required]** Gets the partitions of this Stream.
        The number of partitions in the stream.


        :return: The partitions of this Stream.
        :rtype: int
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """
        Sets the partitions of this Stream.
        The number of partitions in the stream.


        :param partitions: The partitions of this Stream.
        :type: int
        """
        self._partitions = partitions

    @property
    def retention_in_hours(self):
        """
        **[Required]** Gets the retention_in_hours of this Stream.
        The retention period of the stream, in hours. This property is read-only.


        :return: The retention_in_hours of this Stream.
        :rtype: int
        """
        return self._retention_in_hours

    @retention_in_hours.setter
    def retention_in_hours(self, retention_in_hours):
        """
        Sets the retention_in_hours of this Stream.
        The retention period of the stream, in hours. This property is read-only.


        :param retention_in_hours: The retention_in_hours of this Stream.
        :type: int
        """
        self._retention_in_hours = retention_in_hours

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Stream.
        The OCID of the stream.


        :return: The compartment_id of this Stream.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Stream.
        The OCID of the stream.


        :param compartment_id: The compartment_id of this Stream.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def stream_pool_id(self):
        """
        **[Required]** Gets the stream_pool_id of this Stream.
        The OCID of the stream pool that contains the stream.


        :return: The stream_pool_id of this Stream.
        :rtype: str
        """
        return self._stream_pool_id

    @stream_pool_id.setter
    def stream_pool_id(self, stream_pool_id):
        """
        Sets the stream_pool_id of this Stream.
        The OCID of the stream pool that contains the stream.


        :param stream_pool_id: The stream_pool_id of this Stream.
        :type: str
        """
        self._stream_pool_id = stream_pool_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Stream.
        The current state of the stream.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Stream.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Stream.
        The current state of the stream.


        :param lifecycle_state: The lifecycle_state of this Stream.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_state_details(self):
        """
        Gets the lifecycle_state_details of this Stream.
        Any additional details about the current state of the stream.


        :return: The lifecycle_state_details of this Stream.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this Stream.
        Any additional details about the current state of the stream.


        :param lifecycle_state_details: The lifecycle_state_details of this Stream.
        :type: str
        """
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Stream.
        The date and time the stream was created, expressed in in `RFC 3339`__ timestamp format.

        Example: `2018-04-20T00:00:07.405Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this Stream.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Stream.
        The date and time the stream was created, expressed in in `RFC 3339`__ timestamp format.

        Example: `2018-04-20T00:00:07.405Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this Stream.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def messages_endpoint(self):
        """
        **[Required]** Gets the messages_endpoint of this Stream.
        The endpoint to use when creating the StreamClient to consume or publish messages in the stream.
        If the associated stream pool is private, the endpoint is also private and can only be accessed from inside the stream pool's associated subnet.


        :return: The messages_endpoint of this Stream.
        :rtype: str
        """
        return self._messages_endpoint

    @messages_endpoint.setter
    def messages_endpoint(self, messages_endpoint):
        """
        Sets the messages_endpoint of this Stream.
        The endpoint to use when creating the StreamClient to consume or publish messages in the stream.
        If the associated stream pool is private, the endpoint is also private and can only be accessed from inside the stream pool's associated subnet.


        :param messages_endpoint: The messages_endpoint of this Stream.
        :type: str
        """
        self._messages_endpoint = messages_endpoint

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Stream.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Stream.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Stream.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Stream.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Stream.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}'

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Stream.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Stream.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}'

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Stream.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
