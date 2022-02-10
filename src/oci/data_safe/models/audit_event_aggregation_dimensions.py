# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuditEventAggregationDimensions(object):
    """
    Details of aggregation dimensions used for summarizing audit events.
    """

    #: A constant which can be used with the target_class property of a AuditEventAggregationDimensions.
    #: This constant has a value of "DATABASE"
    TARGET_CLASS_DATABASE = "DATABASE"

    #: A constant which can be used with the audit_type property of a AuditEventAggregationDimensions.
    #: This constant has a value of "STANDARD"
    AUDIT_TYPE_STANDARD = "STANDARD"

    #: A constant which can be used with the audit_type property of a AuditEventAggregationDimensions.
    #: This constant has a value of "FINE_GRAINED"
    AUDIT_TYPE_FINE_GRAINED = "FINE_GRAINED"

    #: A constant which can be used with the audit_type property of a AuditEventAggregationDimensions.
    #: This constant has a value of "XS"
    AUDIT_TYPE_XS = "XS"

    #: A constant which can be used with the audit_type property of a AuditEventAggregationDimensions.
    #: This constant has a value of "DATABASE_VAULT"
    AUDIT_TYPE_DATABASE_VAULT = "DATABASE_VAULT"

    #: A constant which can be used with the audit_type property of a AuditEventAggregationDimensions.
    #: This constant has a value of "LABEL_SECURITY"
    AUDIT_TYPE_LABEL_SECURITY = "LABEL_SECURITY"

    #: A constant which can be used with the audit_type property of a AuditEventAggregationDimensions.
    #: This constant has a value of "RMAN"
    AUDIT_TYPE_RMAN = "RMAN"

    #: A constant which can be used with the audit_type property of a AuditEventAggregationDimensions.
    #: This constant has a value of "DATAPUMP"
    AUDIT_TYPE_DATAPUMP = "DATAPUMP"

    #: A constant which can be used with the audit_type property of a AuditEventAggregationDimensions.
    #: This constant has a value of "DIRECT_PATH_API"
    AUDIT_TYPE_DIRECT_PATH_API = "DIRECT_PATH_API"

    def __init__(self, **kwargs):
        """
        Initializes a new AuditEventAggregationDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param audit_event_time:
            The value to assign to the audit_event_time property of this AuditEventAggregationDimensions.
        :type audit_event_time: list[datetime]

        :param db_user_name:
            The value to assign to the db_user_name property of this AuditEventAggregationDimensions.
        :type db_user_name: list[str]

        :param target_id:
            The value to assign to the target_id property of this AuditEventAggregationDimensions.
        :type target_id: list[str]

        :param target_name:
            The value to assign to the target_name property of this AuditEventAggregationDimensions.
        :type target_name: list[str]

        :param target_class:
            The value to assign to the target_class property of this AuditEventAggregationDimensions.
            Allowed values for items in this list are: "DATABASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type target_class: list[str]

        :param object_type:
            The value to assign to the object_type property of this AuditEventAggregationDimensions.
        :type object_type: list[str]

        :param client_hostname:
            The value to assign to the client_hostname property of this AuditEventAggregationDimensions.
        :type client_hostname: list[str]

        :param client_program:
            The value to assign to the client_program property of this AuditEventAggregationDimensions.
        :type client_program: list[str]

        :param client_id:
            The value to assign to the client_id property of this AuditEventAggregationDimensions.
        :type client_id: list[str]

        :param audit_type:
            The value to assign to the audit_type property of this AuditEventAggregationDimensions.
            Allowed values for items in this list are: "STANDARD", "FINE_GRAINED", "XS", "DATABASE_VAULT", "LABEL_SECURITY", "RMAN", "DATAPUMP", "DIRECT_PATH_API", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type audit_type: list[str]

        :param event_name:
            The value to assign to the event_name property of this AuditEventAggregationDimensions.
        :type event_name: list[str]

        """
        self.swagger_types = {
            'audit_event_time': 'list[datetime]',
            'db_user_name': 'list[str]',
            'target_id': 'list[str]',
            'target_name': 'list[str]',
            'target_class': 'list[str]',
            'object_type': 'list[str]',
            'client_hostname': 'list[str]',
            'client_program': 'list[str]',
            'client_id': 'list[str]',
            'audit_type': 'list[str]',
            'event_name': 'list[str]'
        }

        self.attribute_map = {
            'audit_event_time': 'auditEventTime',
            'db_user_name': 'dbUserName',
            'target_id': 'targetId',
            'target_name': 'targetName',
            'target_class': 'targetClass',
            'object_type': 'objectType',
            'client_hostname': 'clientHostname',
            'client_program': 'clientProgram',
            'client_id': 'clientId',
            'audit_type': 'auditType',
            'event_name': 'eventName'
        }

        self._audit_event_time = None
        self._db_user_name = None
        self._target_id = None
        self._target_name = None
        self._target_class = None
        self._object_type = None
        self._client_hostname = None
        self._client_program = None
        self._client_id = None
        self._audit_type = None
        self._event_name = None

    @property
    def audit_event_time(self):
        """
        Gets the audit_event_time of this AuditEventAggregationDimensions.
        Time of audit event occurrence in the target database.


        :return: The audit_event_time of this AuditEventAggregationDimensions.
        :rtype: list[datetime]
        """
        return self._audit_event_time

    @audit_event_time.setter
    def audit_event_time(self, audit_event_time):
        """
        Sets the audit_event_time of this AuditEventAggregationDimensions.
        Time of audit event occurrence in the target database.


        :param audit_event_time: The audit_event_time of this AuditEventAggregationDimensions.
        :type: list[datetime]
        """
        self._audit_event_time = audit_event_time

    @property
    def db_user_name(self):
        """
        Gets the db_user_name of this AuditEventAggregationDimensions.
        Name of the database user whose actions were audited.


        :return: The db_user_name of this AuditEventAggregationDimensions.
        :rtype: list[str]
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        """
        Sets the db_user_name of this AuditEventAggregationDimensions.
        Name of the database user whose actions were audited.


        :param db_user_name: The db_user_name of this AuditEventAggregationDimensions.
        :type: list[str]
        """
        self._db_user_name = db_user_name

    @property
    def target_id(self):
        """
        Gets the target_id of this AuditEventAggregationDimensions.
        The OCID of the target database that was audited.


        :return: The target_id of this AuditEventAggregationDimensions.
        :rtype: list[str]
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this AuditEventAggregationDimensions.
        The OCID of the target database that was audited.


        :param target_id: The target_id of this AuditEventAggregationDimensions.
        :type: list[str]
        """
        self._target_id = target_id

    @property
    def target_name(self):
        """
        Gets the target_name of this AuditEventAggregationDimensions.
        The name of the target database that was audited.


        :return: The target_name of this AuditEventAggregationDimensions.
        :rtype: list[str]
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """
        Sets the target_name of this AuditEventAggregationDimensions.
        The name of the target database that was audited.


        :param target_name: The target_name of this AuditEventAggregationDimensions.
        :type: list[str]
        """
        self._target_name = target_name

    @property
    def target_class(self):
        """
        Gets the target_class of this AuditEventAggregationDimensions.
        Class of the target that was audited.

        Allowed values for items in this list are: "DATABASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The target_class of this AuditEventAggregationDimensions.
        :rtype: list[str]
        """
        return self._target_class

    @target_class.setter
    def target_class(self, target_class):
        """
        Sets the target_class of this AuditEventAggregationDimensions.
        Class of the target that was audited.


        :param target_class: The target_class of this AuditEventAggregationDimensions.
        :type: list[str]
        """
        allowed_values = ["DATABASE"]
        if target_class:
            target_class[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in target_class]
        self._target_class = target_class

    @property
    def object_type(self):
        """
        Gets the object_type of this AuditEventAggregationDimensions.
        Type of object in the source database affected by the action. i.e PL/SQL, SYNONYM, PACKAGE BODY.


        :return: The object_type of this AuditEventAggregationDimensions.
        :rtype: list[str]
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AuditEventAggregationDimensions.
        Type of object in the source database affected by the action. i.e PL/SQL, SYNONYM, PACKAGE BODY.


        :param object_type: The object_type of this AuditEventAggregationDimensions.
        :type: list[str]
        """
        self._object_type = object_type

    @property
    def client_hostname(self):
        """
        Gets the client_hostname of this AuditEventAggregationDimensions.
        Name of the host machine from which the session was spawned.


        :return: The client_hostname of this AuditEventAggregationDimensions.
        :rtype: list[str]
        """
        return self._client_hostname

    @client_hostname.setter
    def client_hostname(self, client_hostname):
        """
        Sets the client_hostname of this AuditEventAggregationDimensions.
        Name of the host machine from which the session was spawned.


        :param client_hostname: The client_hostname of this AuditEventAggregationDimensions.
        :type: list[str]
        """
        self._client_hostname = client_hostname

    @property
    def client_program(self):
        """
        Gets the client_program of this AuditEventAggregationDimensions.
        The application from which the audit event was generated. Examples SQL Plus or SQL Developer.


        :return: The client_program of this AuditEventAggregationDimensions.
        :rtype: list[str]
        """
        return self._client_program

    @client_program.setter
    def client_program(self, client_program):
        """
        Sets the client_program of this AuditEventAggregationDimensions.
        The application from which the audit event was generated. Examples SQL Plus or SQL Developer.


        :param client_program: The client_program of this AuditEventAggregationDimensions.
        :type: list[str]
        """
        self._client_program = client_program

    @property
    def client_id(self):
        """
        Gets the client_id of this AuditEventAggregationDimensions.
        The client identifier in each Oracle session.


        :return: The client_id of this AuditEventAggregationDimensions.
        :rtype: list[str]
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this AuditEventAggregationDimensions.
        The client identifier in each Oracle session.


        :param client_id: The client_id of this AuditEventAggregationDimensions.
        :type: list[str]
        """
        self._client_id = client_id

    @property
    def audit_type(self):
        """
        Gets the audit_type of this AuditEventAggregationDimensions.
        Type of auditing.

        Allowed values for items in this list are: "STANDARD", "FINE_GRAINED", "XS", "DATABASE_VAULT", "LABEL_SECURITY", "RMAN", "DATAPUMP", "DIRECT_PATH_API", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The audit_type of this AuditEventAggregationDimensions.
        :rtype: list[str]
        """
        return self._audit_type

    @audit_type.setter
    def audit_type(self, audit_type):
        """
        Sets the audit_type of this AuditEventAggregationDimensions.
        Type of auditing.


        :param audit_type: The audit_type of this AuditEventAggregationDimensions.
        :type: list[str]
        """
        allowed_values = ["STANDARD", "FINE_GRAINED", "XS", "DATABASE_VAULT", "LABEL_SECURITY", "RMAN", "DATAPUMP", "DIRECT_PATH_API"]
        if audit_type:
            audit_type[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in audit_type]
        self._audit_type = audit_type

    @property
    def event_name(self):
        """
        Gets the event_name of this AuditEventAggregationDimensions.
        Name of the detail action executed by the user on the target database. i.e ALTER SEQUENCE, CREATE TRIGGER, CREATE INDEX.


        :return: The event_name of this AuditEventAggregationDimensions.
        :rtype: list[str]
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this AuditEventAggregationDimensions.
        Name of the detail action executed by the user on the target database. i.e ALTER SEQUENCE, CREATE TRIGGER, CREATE INDEX.


        :param event_name: The event_name of this AuditEventAggregationDimensions.
        :type: list[str]
        """
        self._event_name = event_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
