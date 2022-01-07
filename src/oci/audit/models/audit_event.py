# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuditEvent(object):
    """
    All the attributes of an audit event. For more information, see `Viewing Audit Log Events`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AuditEvent object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param event_type:
            The value to assign to the event_type property of this AuditEvent.
        :type event_type: str

        :param cloud_events_version:
            The value to assign to the cloud_events_version property of this AuditEvent.
        :type cloud_events_version: str

        :param event_type_version:
            The value to assign to the event_type_version property of this AuditEvent.
        :type event_type_version: str

        :param source:
            The value to assign to the source property of this AuditEvent.
        :type source: str

        :param event_id:
            The value to assign to the event_id property of this AuditEvent.
        :type event_id: str

        :param event_time:
            The value to assign to the event_time property of this AuditEvent.
        :type event_time: datetime

        :param content_type:
            The value to assign to the content_type property of this AuditEvent.
        :type content_type: str

        :param data:
            The value to assign to the data property of this AuditEvent.
        :type data: oci.audit.models.Data

        """
        self.swagger_types = {
            'event_type': 'str',
            'cloud_events_version': 'str',
            'event_type_version': 'str',
            'source': 'str',
            'event_id': 'str',
            'event_time': 'datetime',
            'content_type': 'str',
            'data': 'Data'
        }

        self.attribute_map = {
            'event_type': 'eventType',
            'cloud_events_version': 'cloudEventsVersion',
            'event_type_version': 'eventTypeVersion',
            'source': 'source',
            'event_id': 'eventId',
            'event_time': 'eventTime',
            'content_type': 'contentType',
            'data': 'data'
        }

        self._event_type = None
        self._cloud_events_version = None
        self._event_type_version = None
        self._source = None
        self._event_id = None
        self._event_time = None
        self._content_type = None
        self._data = None

    @property
    def event_type(self):
        """
        **[Required]** Gets the event_type of this AuditEvent.
        The type of event that happened.

        The service that produces the event can also add, remove, or change the meaning of a field.
        A service implementing these type changes would publish a new version of an `eventType` and
        revise the `eventTypeVersion` field.

        Example: `com.oraclecloud.ComputeApi.GetInstance`


        :return: The event_type of this AuditEvent.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this AuditEvent.
        The type of event that happened.

        The service that produces the event can also add, remove, or change the meaning of a field.
        A service implementing these type changes would publish a new version of an `eventType` and
        revise the `eventTypeVersion` field.

        Example: `com.oraclecloud.ComputeApi.GetInstance`


        :param event_type: The event_type of this AuditEvent.
        :type: str
        """
        self._event_type = event_type

    @property
    def cloud_events_version(self):
        """
        **[Required]** Gets the cloud_events_version of this AuditEvent.
        The version of the CloudEvents specification. The structure of the envelope follows the
        `CloudEvents`__ industry standard format hosted by the
        `Cloud Native Computing Foundation ( CNCF)`__.

        Audit uses version 0.1 specification of the CloudEvents event envelope.

        Example: `0.1`

        __ https://github.com/cloudevents/spec
        __ https://www.cncf.io/


        :return: The cloud_events_version of this AuditEvent.
        :rtype: str
        """
        return self._cloud_events_version

    @cloud_events_version.setter
    def cloud_events_version(self, cloud_events_version):
        """
        Sets the cloud_events_version of this AuditEvent.
        The version of the CloudEvents specification. The structure of the envelope follows the
        `CloudEvents`__ industry standard format hosted by the
        `Cloud Native Computing Foundation ( CNCF)`__.

        Audit uses version 0.1 specification of the CloudEvents event envelope.

        Example: `0.1`

        __ https://github.com/cloudevents/spec
        __ https://www.cncf.io/


        :param cloud_events_version: The cloud_events_version of this AuditEvent.
        :type: str
        """
        self._cloud_events_version = cloud_events_version

    @property
    def event_type_version(self):
        """
        **[Required]** Gets the event_type_version of this AuditEvent.
        The version of the event type. This version applies to the payload of the event, not the envelope.
        Use `cloudEventsVersion` to determine the version of the envelope.

        Example: `2.0`


        :return: The event_type_version of this AuditEvent.
        :rtype: str
        """
        return self._event_type_version

    @event_type_version.setter
    def event_type_version(self, event_type_version):
        """
        Sets the event_type_version of this AuditEvent.
        The version of the event type. This version applies to the payload of the event, not the envelope.
        Use `cloudEventsVersion` to determine the version of the envelope.

        Example: `2.0`


        :param event_type_version: The event_type_version of this AuditEvent.
        :type: str
        """
        self._event_type_version = event_type_version

    @property
    def source(self):
        """
        **[Required]** Gets the source of this AuditEvent.
        The source of the event.

        Example: `ComputeApi`


        :return: The source of this AuditEvent.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this AuditEvent.
        The source of the event.

        Example: `ComputeApi`


        :param source: The source of this AuditEvent.
        :type: str
        """
        self._source = source

    @property
    def event_id(self):
        """
        **[Required]** Gets the event_id of this AuditEvent.
        The GUID of the event.


        :return: The event_id of this AuditEvent.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this AuditEvent.
        The GUID of the event.


        :param event_id: The event_id of this AuditEvent.
        :type: str
        """
        self._event_id = event_id

    @property
    def event_time(self):
        """
        **[Required]** Gets the event_time of this AuditEvent.
        The time the event occurred, expressed in `RFC 3339`__ timestamp format.

        Example: `2019-09-18T00:10:59.252Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The event_time of this AuditEvent.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """
        Sets the event_time of this AuditEvent.
        The time the event occurred, expressed in `RFC 3339`__ timestamp format.

        Example: `2019-09-18T00:10:59.252Z`

        __ https://tools.ietf.org/html/rfc3339


        :param event_time: The event_time of this AuditEvent.
        :type: datetime
        """
        self._event_time = event_time

    @property
    def content_type(self):
        """
        **[Required]** Gets the content_type of this AuditEvent.
        The content type of the data contained in `data`.

        Example: `application/json`


        :return: The content_type of this AuditEvent.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this AuditEvent.
        The content type of the data contained in `data`.

        Example: `application/json`


        :param content_type: The content_type of this AuditEvent.
        :type: str
        """
        self._content_type = content_type

    @property
    def data(self):
        """
        **[Required]** Gets the data of this AuditEvent.

        :return: The data of this AuditEvent.
        :rtype: oci.audit.models.Data
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this AuditEvent.

        :param data: The data of this AuditEvent.
        :type: oci.audit.models.Data
        """
        self._data = data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
