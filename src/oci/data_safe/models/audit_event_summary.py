# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuditEventSummary(object):
    """
    The resource represents the audit events collected from the target database by Oracle Data Safe.
    """

    #: A constant which can be used with the database_type property of a AuditEventSummary.
    #: This constant has a value of "DATABASE_CLOUD_SERVICE"
    DATABASE_TYPE_DATABASE_CLOUD_SERVICE = "DATABASE_CLOUD_SERVICE"

    #: A constant which can be used with the database_type property of a AuditEventSummary.
    #: This constant has a value of "AUTONOMOUS_DATABASE"
    DATABASE_TYPE_AUTONOMOUS_DATABASE = "AUTONOMOUS_DATABASE"

    #: A constant which can be used with the database_type property of a AuditEventSummary.
    #: This constant has a value of "INSTALLED_DATABASE"
    DATABASE_TYPE_INSTALLED_DATABASE = "INSTALLED_DATABASE"

    #: A constant which can be used with the target_class property of a AuditEventSummary.
    #: This constant has a value of "DATABASE"
    TARGET_CLASS_DATABASE = "DATABASE"

    #: A constant which can be used with the operation_status property of a AuditEventSummary.
    #: This constant has a value of "SUCCESS"
    OPERATION_STATUS_SUCCESS = "SUCCESS"

    #: A constant which can be used with the operation_status property of a AuditEventSummary.
    #: This constant has a value of "FAILURE"
    OPERATION_STATUS_FAILURE = "FAILURE"

    #: A constant which can be used with the audit_location property of a AuditEventSummary.
    #: This constant has a value of "AUDIT_TABLE"
    AUDIT_LOCATION_AUDIT_TABLE = "AUDIT_TABLE"

    #: A constant which can be used with the audit_type property of a AuditEventSummary.
    #: This constant has a value of "STANDARD"
    AUDIT_TYPE_STANDARD = "STANDARD"

    #: A constant which can be used with the audit_type property of a AuditEventSummary.
    #: This constant has a value of "FINE_GRAINED"
    AUDIT_TYPE_FINE_GRAINED = "FINE_GRAINED"

    #: A constant which can be used with the audit_type property of a AuditEventSummary.
    #: This constant has a value of "XS"
    AUDIT_TYPE_XS = "XS"

    #: A constant which can be used with the audit_type property of a AuditEventSummary.
    #: This constant has a value of "DATABASE_VAULT"
    AUDIT_TYPE_DATABASE_VAULT = "DATABASE_VAULT"

    #: A constant which can be used with the audit_type property of a AuditEventSummary.
    #: This constant has a value of "LABEL_SECURITY"
    AUDIT_TYPE_LABEL_SECURITY = "LABEL_SECURITY"

    #: A constant which can be used with the audit_type property of a AuditEventSummary.
    #: This constant has a value of "RMAN"
    AUDIT_TYPE_RMAN = "RMAN"

    #: A constant which can be used with the audit_type property of a AuditEventSummary.
    #: This constant has a value of "DATAPUMP"
    AUDIT_TYPE_DATAPUMP = "DATAPUMP"

    #: A constant which can be used with the audit_type property of a AuditEventSummary.
    #: This constant has a value of "DIRECT_PATH_API"
    AUDIT_TYPE_DIRECT_PATH_API = "DIRECT_PATH_API"

    def __init__(self, **kwargs):
        """
        Initializes a new AuditEventSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AuditEventSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AuditEventSummary.
        :type compartment_id: str

        :param db_user_name:
            The value to assign to the db_user_name property of this AuditEventSummary.
        :type db_user_name: str

        :param target_id:
            The value to assign to the target_id property of this AuditEventSummary.
        :type target_id: str

        :param target_name:
            The value to assign to the target_name property of this AuditEventSummary.
        :type target_name: str

        :param database_type:
            The value to assign to the database_type property of this AuditEventSummary.
            Allowed values for this property are: "DATABASE_CLOUD_SERVICE", "AUTONOMOUS_DATABASE", "INSTALLED_DATABASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param target_class:
            The value to assign to the target_class property of this AuditEventSummary.
            Allowed values for this property are: "DATABASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type target_class: str

        :param audit_event_time:
            The value to assign to the audit_event_time property of this AuditEventSummary.
        :type audit_event_time: datetime

        :param time_collected:
            The value to assign to the time_collected property of this AuditEventSummary.
        :type time_collected: datetime

        :param os_user_name:
            The value to assign to the os_user_name property of this AuditEventSummary.
        :type os_user_name: str

        :param operation:
            The value to assign to the operation property of this AuditEventSummary.
        :type operation: str

        :param operation_status:
            The value to assign to the operation_status property of this AuditEventSummary.
            Allowed values for this property are: "SUCCESS", "FAILURE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_status: str

        :param event_name:
            The value to assign to the event_name property of this AuditEventSummary.
        :type event_name: str

        :param error_code:
            The value to assign to the error_code property of this AuditEventSummary.
        :type error_code: str

        :param error_message:
            The value to assign to the error_message property of this AuditEventSummary.
        :type error_message: str

        :param object_type:
            The value to assign to the object_type property of this AuditEventSummary.
        :type object_type: str

        :param object_name:
            The value to assign to the object_name property of this AuditEventSummary.
        :type object_name: str

        :param object_owner:
            The value to assign to the object_owner property of this AuditEventSummary.
        :type object_owner: str

        :param client_hostname:
            The value to assign to the client_hostname property of this AuditEventSummary.
        :type client_hostname: str

        :param client_ip:
            The value to assign to the client_ip property of this AuditEventSummary.
        :type client_ip: str

        :param audit_trail_id:
            The value to assign to the audit_trail_id property of this AuditEventSummary.
        :type audit_trail_id: str

        :param is_alerted:
            The value to assign to the is_alerted property of this AuditEventSummary.
        :type is_alerted: bool

        :param action_taken:
            The value to assign to the action_taken property of this AuditEventSummary.
        :type action_taken: str

        :param client_program:
            The value to assign to the client_program property of this AuditEventSummary.
        :type client_program: str

        :param command_text:
            The value to assign to the command_text property of this AuditEventSummary.
        :type command_text: str

        :param command_param:
            The value to assign to the command_param property of this AuditEventSummary.
        :type command_param: str

        :param extended_event_attributes:
            The value to assign to the extended_event_attributes property of this AuditEventSummary.
        :type extended_event_attributes: str

        :param audit_location:
            The value to assign to the audit_location property of this AuditEventSummary.
            Allowed values for this property are: "AUDIT_TABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type audit_location: str

        :param os_terminal:
            The value to assign to the os_terminal property of this AuditEventSummary.
        :type os_terminal: str

        :param client_id:
            The value to assign to the client_id property of this AuditEventSummary.
        :type client_id: str

        :param audit_policies:
            The value to assign to the audit_policies property of this AuditEventSummary.
        :type audit_policies: str

        :param audit_type:
            The value to assign to the audit_type property of this AuditEventSummary.
            Allowed values for this property are: "STANDARD", "FINE_GRAINED", "XS", "DATABASE_VAULT", "LABEL_SECURITY", "RMAN", "DATAPUMP", "DIRECT_PATH_API", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type audit_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AuditEventSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AuditEventSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'db_user_name': 'str',
            'target_id': 'str',
            'target_name': 'str',
            'database_type': 'str',
            'target_class': 'str',
            'audit_event_time': 'datetime',
            'time_collected': 'datetime',
            'os_user_name': 'str',
            'operation': 'str',
            'operation_status': 'str',
            'event_name': 'str',
            'error_code': 'str',
            'error_message': 'str',
            'object_type': 'str',
            'object_name': 'str',
            'object_owner': 'str',
            'client_hostname': 'str',
            'client_ip': 'str',
            'audit_trail_id': 'str',
            'is_alerted': 'bool',
            'action_taken': 'str',
            'client_program': 'str',
            'command_text': 'str',
            'command_param': 'str',
            'extended_event_attributes': 'str',
            'audit_location': 'str',
            'os_terminal': 'str',
            'client_id': 'str',
            'audit_policies': 'str',
            'audit_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'db_user_name': 'dbUserName',
            'target_id': 'targetId',
            'target_name': 'targetName',
            'database_type': 'databaseType',
            'target_class': 'targetClass',
            'audit_event_time': 'auditEventTime',
            'time_collected': 'timeCollected',
            'os_user_name': 'osUserName',
            'operation': 'operation',
            'operation_status': 'operationStatus',
            'event_name': 'eventName',
            'error_code': 'errorCode',
            'error_message': 'errorMessage',
            'object_type': 'objectType',
            'object_name': 'objectName',
            'object_owner': 'objectOwner',
            'client_hostname': 'clientHostname',
            'client_ip': 'clientIp',
            'audit_trail_id': 'auditTrailId',
            'is_alerted': 'isAlerted',
            'action_taken': 'actionTaken',
            'client_program': 'clientProgram',
            'command_text': 'commandText',
            'command_param': 'commandParam',
            'extended_event_attributes': 'extendedEventAttributes',
            'audit_location': 'auditLocation',
            'os_terminal': 'osTerminal',
            'client_id': 'clientId',
            'audit_policies': 'auditPolicies',
            'audit_type': 'auditType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._db_user_name = None
        self._target_id = None
        self._target_name = None
        self._database_type = None
        self._target_class = None
        self._audit_event_time = None
        self._time_collected = None
        self._os_user_name = None
        self._operation = None
        self._operation_status = None
        self._event_name = None
        self._error_code = None
        self._error_message = None
        self._object_type = None
        self._object_name = None
        self._object_owner = None
        self._client_hostname = None
        self._client_ip = None
        self._audit_trail_id = None
        self._is_alerted = None
        self._action_taken = None
        self._client_program = None
        self._command_text = None
        self._command_param = None
        self._extended_event_attributes = None
        self._audit_location = None
        self._os_terminal = None
        self._client_id = None
        self._audit_policies = None
        self._audit_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AuditEventSummary.
        The OCID of the audit event.


        :return: The id of this AuditEventSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuditEventSummary.
        The OCID of the audit event.


        :param id: The id of this AuditEventSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AuditEventSummary.
        The OCID of the compartment containing the audit event. This is the same audited target database resource comparment.


        :return: The compartment_id of this AuditEventSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AuditEventSummary.
        The OCID of the compartment containing the audit event. This is the same audited target database resource comparment.


        :param compartment_id: The compartment_id of this AuditEventSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_user_name(self):
        """
        Gets the db_user_name of this AuditEventSummary.
        Name of the database user whose actions were audited.


        :return: The db_user_name of this AuditEventSummary.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        """
        Sets the db_user_name of this AuditEventSummary.
        Name of the database user whose actions were audited.


        :param db_user_name: The db_user_name of this AuditEventSummary.
        :type: str
        """
        self._db_user_name = db_user_name

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this AuditEventSummary.
        The OCID of the target database that was audited.


        :return: The target_id of this AuditEventSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this AuditEventSummary.
        The OCID of the target database that was audited.


        :param target_id: The target_id of this AuditEventSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def target_name(self):
        """
        **[Required]** Gets the target_name of this AuditEventSummary.
        The name of the target database that was audited.


        :return: The target_name of this AuditEventSummary.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """
        Sets the target_name of this AuditEventSummary.
        The name of the target database that was audited.


        :param target_name: The target_name of this AuditEventSummary.
        :type: str
        """
        self._target_name = target_name

    @property
    def database_type(self):
        """
        **[Required]** Gets the database_type of this AuditEventSummary.
        The type of the target database that was audited. Allowed values are
          - DATABASE_CLOUD_SERVICE - Represents Oracle Database Cloud Services.
          - AUTONOMOUS_DATABASE - Represents Oracle Autonomous Databases.
          - INSTALLED_DATABASE - Represents databases running on-premises or on compute instances.

        Allowed values for this property are: "DATABASE_CLOUD_SERVICE", "AUTONOMOUS_DATABASE", "INSTALLED_DATABASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this AuditEventSummary.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this AuditEventSummary.
        The type of the target database that was audited. Allowed values are
          - DATABASE_CLOUD_SERVICE - Represents Oracle Database Cloud Services.
          - AUTONOMOUS_DATABASE - Represents Oracle Autonomous Databases.
          - INSTALLED_DATABASE - Represents databases running on-premises or on compute instances.


        :param database_type: The database_type of this AuditEventSummary.
        :type: str
        """
        allowed_values = ["DATABASE_CLOUD_SERVICE", "AUTONOMOUS_DATABASE", "INSTALLED_DATABASE"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def target_class(self):
        """
        Gets the target_class of this AuditEventSummary.
        Class of the target that was audited.

        Allowed values for this property are: "DATABASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The target_class of this AuditEventSummary.
        :rtype: str
        """
        return self._target_class

    @target_class.setter
    def target_class(self, target_class):
        """
        Sets the target_class of this AuditEventSummary.
        Class of the target that was audited.


        :param target_class: The target_class of this AuditEventSummary.
        :type: str
        """
        allowed_values = ["DATABASE"]
        if not value_allowed_none_or_none_sentinel(target_class, allowed_values):
            target_class = 'UNKNOWN_ENUM_VALUE'
        self._target_class = target_class

    @property
    def audit_event_time(self):
        """
        **[Required]** Gets the audit_event_time of this AuditEventSummary.
        Time of audit event occurrence in the target database.


        :return: The audit_event_time of this AuditEventSummary.
        :rtype: datetime
        """
        return self._audit_event_time

    @audit_event_time.setter
    def audit_event_time(self, audit_event_time):
        """
        Sets the audit_event_time of this AuditEventSummary.
        Time of audit event occurrence in the target database.


        :param audit_event_time: The audit_event_time of this AuditEventSummary.
        :type: datetime
        """
        self._audit_event_time = audit_event_time

    @property
    def time_collected(self):
        """
        **[Required]** Gets the time_collected of this AuditEventSummary.
        Timestamp when this audit event was collected from the target database by Data Safe.


        :return: The time_collected of this AuditEventSummary.
        :rtype: datetime
        """
        return self._time_collected

    @time_collected.setter
    def time_collected(self, time_collected):
        """
        Sets the time_collected of this AuditEventSummary.
        Timestamp when this audit event was collected from the target database by Data Safe.


        :param time_collected: The time_collected of this AuditEventSummary.
        :type: datetime
        """
        self._time_collected = time_collected

    @property
    def os_user_name(self):
        """
        Gets the os_user_name of this AuditEventSummary.
        Name of the operating system user for the database session.


        :return: The os_user_name of this AuditEventSummary.
        :rtype: str
        """
        return self._os_user_name

    @os_user_name.setter
    def os_user_name(self, os_user_name):
        """
        Sets the os_user_name of this AuditEventSummary.
        Name of the operating system user for the database session.


        :param os_user_name: The os_user_name of this AuditEventSummary.
        :type: str
        """
        self._os_user_name = os_user_name

    @property
    def operation(self):
        """
        Gets the operation of this AuditEventSummary.
        Name of the action executed by the user on the target database. i.e ALTER, CREATE, DROP.


        :return: The operation of this AuditEventSummary.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this AuditEventSummary.
        Name of the action executed by the user on the target database. i.e ALTER, CREATE, DROP.


        :param operation: The operation of this AuditEventSummary.
        :type: str
        """
        self._operation = operation

    @property
    def operation_status(self):
        """
        Gets the operation_status of this AuditEventSummary.
        Indicates whether the operation was a success or a failure.

        Allowed values for this property are: "SUCCESS", "FAILURE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_status of this AuditEventSummary.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        """
        Sets the operation_status of this AuditEventSummary.
        Indicates whether the operation was a success or a failure.


        :param operation_status: The operation_status of this AuditEventSummary.
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILURE"]
        if not value_allowed_none_or_none_sentinel(operation_status, allowed_values):
            operation_status = 'UNKNOWN_ENUM_VALUE'
        self._operation_status = operation_status

    @property
    def event_name(self):
        """
        Gets the event_name of this AuditEventSummary.
        Name of the detail action executed by the user on the target database. i.e ALTER SEQUENCE, CREATE TRIGGER, CREATE INDEX.


        :return: The event_name of this AuditEventSummary.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this AuditEventSummary.
        Name of the detail action executed by the user on the target database. i.e ALTER SEQUENCE, CREATE TRIGGER, CREATE INDEX.


        :param event_name: The event_name of this AuditEventSummary.
        :type: str
        """
        self._event_name = event_name

    @property
    def error_code(self):
        """
        Gets the error_code of this AuditEventSummary.
        Oracle Error code generated by the action. Zero indicates the action was successful.


        :return: The error_code of this AuditEventSummary.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this AuditEventSummary.
        Oracle Error code generated by the action. Zero indicates the action was successful.


        :param error_code: The error_code of this AuditEventSummary.
        :type: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """
        Gets the error_message of this AuditEventSummary.
        Detailed message on why the Error occurred.


        :return: The error_message of this AuditEventSummary.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this AuditEventSummary.
        Detailed message on why the Error occurred.


        :param error_message: The error_message of this AuditEventSummary.
        :type: str
        """
        self._error_message = error_message

    @property
    def object_type(self):
        """
        Gets the object_type of this AuditEventSummary.
        Type of object in the source database affected by the action. i.e PL/SQL, SYNONYM, PACKAGE BODY.


        :return: The object_type of this AuditEventSummary.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AuditEventSummary.
        Type of object in the source database affected by the action. i.e PL/SQL, SYNONYM, PACKAGE BODY.


        :param object_type: The object_type of this AuditEventSummary.
        :type: str
        """
        self._object_type = object_type

    @property
    def object_name(self):
        """
        Gets the object_name of this AuditEventSummary.
        Name of the object affected by the action.


        :return: The object_name of this AuditEventSummary.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this AuditEventSummary.
        Name of the object affected by the action.


        :param object_name: The object_name of this AuditEventSummary.
        :type: str
        """
        self._object_name = object_name

    @property
    def object_owner(self):
        """
        Gets the object_owner of this AuditEventSummary.
        Schema name of object affected but the action.


        :return: The object_owner of this AuditEventSummary.
        :rtype: str
        """
        return self._object_owner

    @object_owner.setter
    def object_owner(self, object_owner):
        """
        Sets the object_owner of this AuditEventSummary.
        Schema name of object affected but the action.


        :param object_owner: The object_owner of this AuditEventSummary.
        :type: str
        """
        self._object_owner = object_owner

    @property
    def client_hostname(self):
        """
        Gets the client_hostname of this AuditEventSummary.
        Name of the host machine from which the session was spawned.


        :return: The client_hostname of this AuditEventSummary.
        :rtype: str
        """
        return self._client_hostname

    @client_hostname.setter
    def client_hostname(self, client_hostname):
        """
        Sets the client_hostname of this AuditEventSummary.
        Name of the host machine from which the session was spawned.


        :param client_hostname: The client_hostname of this AuditEventSummary.
        :type: str
        """
        self._client_hostname = client_hostname

    @property
    def client_ip(self):
        """
        Gets the client_ip of this AuditEventSummary.
        IP address of the host from which the session was spawned.


        :return: The client_ip of this AuditEventSummary.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """
        Sets the client_ip of this AuditEventSummary.
        IP address of the host from which the session was spawned.


        :param client_ip: The client_ip of this AuditEventSummary.
        :type: str
        """
        self._client_ip = client_ip

    @property
    def audit_trail_id(self):
        """
        Gets the audit_trail_id of this AuditEventSummary.
        The OCID of the audit trail that generated this audit event.


        :return: The audit_trail_id of this AuditEventSummary.
        :rtype: str
        """
        return self._audit_trail_id

    @audit_trail_id.setter
    def audit_trail_id(self, audit_trail_id):
        """
        Sets the audit_trail_id of this AuditEventSummary.
        The OCID of the audit trail that generated this audit event.


        :param audit_trail_id: The audit_trail_id of this AuditEventSummary.
        :type: str
        """
        self._audit_trail_id = audit_trail_id

    @property
    def is_alerted(self):
        """
        **[Required]** Gets the is_alerted of this AuditEventSummary.
        Indicates whether an alert was raised for this audit event.


        :return: The is_alerted of this AuditEventSummary.
        :rtype: bool
        """
        return self._is_alerted

    @is_alerted.setter
    def is_alerted(self, is_alerted):
        """
        Sets the is_alerted of this AuditEventSummary.
        Indicates whether an alert was raised for this audit event.


        :param is_alerted: The is_alerted of this AuditEventSummary.
        :type: bool
        """
        self._is_alerted = is_alerted

    @property
    def action_taken(self):
        """
        Gets the action_taken of this AuditEventSummary.
        The action taken for this audit event.


        :return: The action_taken of this AuditEventSummary.
        :rtype: str
        """
        return self._action_taken

    @action_taken.setter
    def action_taken(self, action_taken):
        """
        Sets the action_taken of this AuditEventSummary.
        The action taken for this audit event.


        :param action_taken: The action_taken of this AuditEventSummary.
        :type: str
        """
        self._action_taken = action_taken

    @property
    def client_program(self):
        """
        Gets the client_program of this AuditEventSummary.
        The application from which the audit event was generated. Examples SQL Plus or SQL Developer.


        :return: The client_program of this AuditEventSummary.
        :rtype: str
        """
        return self._client_program

    @client_program.setter
    def client_program(self, client_program):
        """
        Sets the client_program of this AuditEventSummary.
        The application from which the audit event was generated. Examples SQL Plus or SQL Developer.


        :param client_program: The client_program of this AuditEventSummary.
        :type: str
        """
        self._client_program = client_program

    @property
    def command_text(self):
        """
        Gets the command_text of this AuditEventSummary.
        The SQL associated with the audit event.


        :return: The command_text of this AuditEventSummary.
        :rtype: str
        """
        return self._command_text

    @command_text.setter
    def command_text(self, command_text):
        """
        Sets the command_text of this AuditEventSummary.
        The SQL associated with the audit event.


        :param command_text: The command_text of this AuditEventSummary.
        :type: str
        """
        self._command_text = command_text

    @property
    def command_param(self):
        """
        Gets the command_param of this AuditEventSummary.
        List of bind variables associated with the command text.


        :return: The command_param of this AuditEventSummary.
        :rtype: str
        """
        return self._command_param

    @command_param.setter
    def command_param(self, command_param):
        """
        Sets the command_param of this AuditEventSummary.
        List of bind variables associated with the command text.


        :param command_param: The command_param of this AuditEventSummary.
        :type: str
        """
        self._command_param = command_param

    @property
    def extended_event_attributes(self):
        """
        Gets the extended_event_attributes of this AuditEventSummary.
        List of all other attributes of the audit event seperated by a colon other than the one returned in audit record.


        :return: The extended_event_attributes of this AuditEventSummary.
        :rtype: str
        """
        return self._extended_event_attributes

    @extended_event_attributes.setter
    def extended_event_attributes(self, extended_event_attributes):
        """
        Sets the extended_event_attributes of this AuditEventSummary.
        List of all other attributes of the audit event seperated by a colon other than the one returned in audit record.


        :param extended_event_attributes: The extended_event_attributes of this AuditEventSummary.
        :type: str
        """
        self._extended_event_attributes = extended_event_attributes

    @property
    def audit_location(self):
        """
        Gets the audit_location of this AuditEventSummary.
        The location of the audit. Currently the value is audit table.

        Allowed values for this property are: "AUDIT_TABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The audit_location of this AuditEventSummary.
        :rtype: str
        """
        return self._audit_location

    @audit_location.setter
    def audit_location(self, audit_location):
        """
        Sets the audit_location of this AuditEventSummary.
        The location of the audit. Currently the value is audit table.


        :param audit_location: The audit_location of this AuditEventSummary.
        :type: str
        """
        allowed_values = ["AUDIT_TABLE"]
        if not value_allowed_none_or_none_sentinel(audit_location, allowed_values):
            audit_location = 'UNKNOWN_ENUM_VALUE'
        self._audit_location = audit_location

    @property
    def os_terminal(self):
        """
        Gets the os_terminal of this AuditEventSummary.
        The operating system terminal of the user session.


        :return: The os_terminal of this AuditEventSummary.
        :rtype: str
        """
        return self._os_terminal

    @os_terminal.setter
    def os_terminal(self, os_terminal):
        """
        Sets the os_terminal of this AuditEventSummary.
        The operating system terminal of the user session.


        :param os_terminal: The os_terminal of this AuditEventSummary.
        :type: str
        """
        self._os_terminal = os_terminal

    @property
    def client_id(self):
        """
        Gets the client_id of this AuditEventSummary.
        The client identifier in each Oracle session.


        :return: The client_id of this AuditEventSummary.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this AuditEventSummary.
        The client identifier in each Oracle session.


        :param client_id: The client_id of this AuditEventSummary.
        :type: str
        """
        self._client_id = client_id

    @property
    def audit_policies(self):
        """
        Gets the audit_policies of this AuditEventSummary.
        Comma-seperated list of audit policies that caused the current audit event.


        :return: The audit_policies of this AuditEventSummary.
        :rtype: str
        """
        return self._audit_policies

    @audit_policies.setter
    def audit_policies(self, audit_policies):
        """
        Sets the audit_policies of this AuditEventSummary.
        Comma-seperated list of audit policies that caused the current audit event.


        :param audit_policies: The audit_policies of this AuditEventSummary.
        :type: str
        """
        self._audit_policies = audit_policies

    @property
    def audit_type(self):
        """
        Gets the audit_type of this AuditEventSummary.
        Type of auditing.

        Allowed values for this property are: "STANDARD", "FINE_GRAINED", "XS", "DATABASE_VAULT", "LABEL_SECURITY", "RMAN", "DATAPUMP", "DIRECT_PATH_API", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The audit_type of this AuditEventSummary.
        :rtype: str
        """
        return self._audit_type

    @audit_type.setter
    def audit_type(self, audit_type):
        """
        Sets the audit_type of this AuditEventSummary.
        Type of auditing.


        :param audit_type: The audit_type of this AuditEventSummary.
        :type: str
        """
        allowed_values = ["STANDARD", "FINE_GRAINED", "XS", "DATABASE_VAULT", "LABEL_SECURITY", "RMAN", "DATAPUMP", "DIRECT_PATH_API"]
        if not value_allowed_none_or_none_sentinel(audit_type, allowed_values):
            audit_type = 'UNKNOWN_ENUM_VALUE'
        self._audit_type = audit_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AuditEventSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AuditEventSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AuditEventSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AuditEventSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AuditEventSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AuditEventSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AuditEventSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AuditEventSummary.
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
