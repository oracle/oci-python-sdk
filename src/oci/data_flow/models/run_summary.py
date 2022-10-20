# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RunSummary(object):
    """
    A summary of the run.
    """

    #: A constant which can be used with the language property of a RunSummary.
    #: This constant has a value of "SCALA"
    LANGUAGE_SCALA = "SCALA"

    #: A constant which can be used with the language property of a RunSummary.
    #: This constant has a value of "JAVA"
    LANGUAGE_JAVA = "JAVA"

    #: A constant which can be used with the language property of a RunSummary.
    #: This constant has a value of "PYTHON"
    LANGUAGE_PYTHON = "PYTHON"

    #: A constant which can be used with the language property of a RunSummary.
    #: This constant has a value of "SQL"
    LANGUAGE_SQL = "SQL"

    #: A constant which can be used with the lifecycle_state property of a RunSummary.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a RunSummary.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a RunSummary.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a RunSummary.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a RunSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a RunSummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a RunSummary.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a RunSummary.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the type property of a RunSummary.
    #: This constant has a value of "BATCH"
    TYPE_BATCH = "BATCH"

    #: A constant which can be used with the type property of a RunSummary.
    #: This constant has a value of "STREAMING"
    TYPE_STREAMING = "STREAMING"

    #: A constant which can be used with the type property of a RunSummary.
    #: This constant has a value of "SESSION"
    TYPE_SESSION = "SESSION"

    def __init__(self, **kwargs):
        """
        Initializes a new RunSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param application_id:
            The value to assign to the application_id property of this RunSummary.
        :type application_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RunSummary.
        :type compartment_id: str

        :param data_read_in_bytes:
            The value to assign to the data_read_in_bytes property of this RunSummary.
        :type data_read_in_bytes: int

        :param data_written_in_bytes:
            The value to assign to the data_written_in_bytes property of this RunSummary.
        :type data_written_in_bytes: int

        :param defined_tags:
            The value to assign to the defined_tags property of this RunSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this RunSummary.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RunSummary.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this RunSummary.
        :type id: str

        :param language:
            The value to assign to the language property of this RunSummary.
            Allowed values for this property are: "SCALA", "JAVA", "PYTHON", "SQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type language: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this RunSummary.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RunSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "CANCELING", "CANCELED", "FAILED", "SUCCEEDED", "STOPPING", "STOPPED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param opc_request_id:
            The value to assign to the opc_request_id property of this RunSummary.
        :type opc_request_id: str

        :param owner_principal_id:
            The value to assign to the owner_principal_id property of this RunSummary.
        :type owner_principal_id: str

        :param owner_user_name:
            The value to assign to the owner_user_name property of this RunSummary.
        :type owner_user_name: str

        :param run_duration_in_milliseconds:
            The value to assign to the run_duration_in_milliseconds property of this RunSummary.
        :type run_duration_in_milliseconds: int

        :param total_o_cpu:
            The value to assign to the total_o_cpu property of this RunSummary.
        :type total_o_cpu: int

        :param time_created:
            The value to assign to the time_created property of this RunSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RunSummary.
        :type time_updated: datetime

        :param type:
            The value to assign to the type property of this RunSummary.
            Allowed values for this property are: "BATCH", "STREAMING", "SESSION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'application_id': 'str',
            'compartment_id': 'str',
            'data_read_in_bytes': 'int',
            'data_written_in_bytes': 'int',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'language': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'opc_request_id': 'str',
            'owner_principal_id': 'str',
            'owner_user_name': 'str',
            'run_duration_in_milliseconds': 'int',
            'total_o_cpu': 'int',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'type': 'str'
        }

        self.attribute_map = {
            'application_id': 'applicationId',
            'compartment_id': 'compartmentId',
            'data_read_in_bytes': 'dataReadInBytes',
            'data_written_in_bytes': 'dataWrittenInBytes',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'language': 'language',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'opc_request_id': 'opcRequestId',
            'owner_principal_id': 'ownerPrincipalId',
            'owner_user_name': 'ownerUserName',
            'run_duration_in_milliseconds': 'runDurationInMilliseconds',
            'total_o_cpu': 'totalOCpu',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'type': 'type'
        }

        self._application_id = None
        self._compartment_id = None
        self._data_read_in_bytes = None
        self._data_written_in_bytes = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._language = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._opc_request_id = None
        self._owner_principal_id = None
        self._owner_user_name = None
        self._run_duration_in_milliseconds = None
        self._total_o_cpu = None
        self._time_created = None
        self._time_updated = None
        self._type = None

    @property
    def application_id(self):
        """
        **[Required]** Gets the application_id of this RunSummary.
        The application ID.


        :return: The application_id of this RunSummary.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """
        Sets the application_id of this RunSummary.
        The application ID.


        :param application_id: The application_id of this RunSummary.
        :type: str
        """
        self._application_id = application_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RunSummary.
        The OCID of a compartment.


        :return: The compartment_id of this RunSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RunSummary.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this RunSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def data_read_in_bytes(self):
        """
        Gets the data_read_in_bytes of this RunSummary.
        The data read by the run in bytes.


        :return: The data_read_in_bytes of this RunSummary.
        :rtype: int
        """
        return self._data_read_in_bytes

    @data_read_in_bytes.setter
    def data_read_in_bytes(self, data_read_in_bytes):
        """
        Sets the data_read_in_bytes of this RunSummary.
        The data read by the run in bytes.


        :param data_read_in_bytes: The data_read_in_bytes of this RunSummary.
        :type: int
        """
        self._data_read_in_bytes = data_read_in_bytes

    @property
    def data_written_in_bytes(self):
        """
        Gets the data_written_in_bytes of this RunSummary.
        The data written by the run in bytes.


        :return: The data_written_in_bytes of this RunSummary.
        :rtype: int
        """
        return self._data_written_in_bytes

    @data_written_in_bytes.setter
    def data_written_in_bytes(self, data_written_in_bytes):
        """
        Sets the data_written_in_bytes of this RunSummary.
        The data written by the run in bytes.


        :param data_written_in_bytes: The data_written_in_bytes of this RunSummary.
        :type: int
        """
        self._data_written_in_bytes = data_written_in_bytes

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this RunSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this RunSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RunSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this RunSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this RunSummary.
        A user-friendly name. This name is not necessarily unique.


        :return: The display_name of this RunSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RunSummary.
        A user-friendly name. This name is not necessarily unique.


        :param display_name: The display_name of this RunSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this RunSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this RunSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RunSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this RunSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RunSummary.
        The ID of a run.


        :return: The id of this RunSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RunSummary.
        The ID of a run.


        :param id: The id of this RunSummary.
        :type: str
        """
        self._id = id

    @property
    def language(self):
        """
        **[Required]** Gets the language of this RunSummary.
        The Spark language.

        Allowed values for this property are: "SCALA", "JAVA", "PYTHON", "SQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The language of this RunSummary.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this RunSummary.
        The Spark language.


        :param language: The language of this RunSummary.
        :type: str
        """
        allowed_values = ["SCALA", "JAVA", "PYTHON", "SQL"]
        if not value_allowed_none_or_none_sentinel(language, allowed_values):
            language = 'UNKNOWN_ENUM_VALUE'
        self._language = language

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this RunSummary.
        The detailed messages about the lifecycle state.


        :return: The lifecycle_details of this RunSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this RunSummary.
        The detailed messages about the lifecycle state.


        :param lifecycle_details: The lifecycle_details of this RunSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this RunSummary.
        The current state of this run.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "CANCELING", "CANCELED", "FAILED", "SUCCEEDED", "STOPPING", "STOPPED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RunSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RunSummary.
        The current state of this run.


        :param lifecycle_state: The lifecycle_state of this RunSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "CANCELING", "CANCELED", "FAILED", "SUCCEEDED", "STOPPING", "STOPPED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def opc_request_id(self):
        """
        Gets the opc_request_id of this RunSummary.
        Unique Oracle assigned identifier for the request.
        If you need to contact Oracle about a particular request, please provide the request ID.


        :return: The opc_request_id of this RunSummary.
        :rtype: str
        """
        return self._opc_request_id

    @opc_request_id.setter
    def opc_request_id(self, opc_request_id):
        """
        Sets the opc_request_id of this RunSummary.
        Unique Oracle assigned identifier for the request.
        If you need to contact Oracle about a particular request, please provide the request ID.


        :param opc_request_id: The opc_request_id of this RunSummary.
        :type: str
        """
        self._opc_request_id = opc_request_id

    @property
    def owner_principal_id(self):
        """
        Gets the owner_principal_id of this RunSummary.
        The OCID of the user who created the resource.


        :return: The owner_principal_id of this RunSummary.
        :rtype: str
        """
        return self._owner_principal_id

    @owner_principal_id.setter
    def owner_principal_id(self, owner_principal_id):
        """
        Sets the owner_principal_id of this RunSummary.
        The OCID of the user who created the resource.


        :param owner_principal_id: The owner_principal_id of this RunSummary.
        :type: str
        """
        self._owner_principal_id = owner_principal_id

    @property
    def owner_user_name(self):
        """
        Gets the owner_user_name of this RunSummary.
        The username of the user who created the resource.  If the username of the owner does not exist,
        `null` will be returned and the caller should refer to the ownerPrincipalId value instead.


        :return: The owner_user_name of this RunSummary.
        :rtype: str
        """
        return self._owner_user_name

    @owner_user_name.setter
    def owner_user_name(self, owner_user_name):
        """
        Sets the owner_user_name of this RunSummary.
        The username of the user who created the resource.  If the username of the owner does not exist,
        `null` will be returned and the caller should refer to the ownerPrincipalId value instead.


        :param owner_user_name: The owner_user_name of this RunSummary.
        :type: str
        """
        self._owner_user_name = owner_user_name

    @property
    def run_duration_in_milliseconds(self):
        """
        Gets the run_duration_in_milliseconds of this RunSummary.
        The duration of the run in milliseconds.


        :return: The run_duration_in_milliseconds of this RunSummary.
        :rtype: int
        """
        return self._run_duration_in_milliseconds

    @run_duration_in_milliseconds.setter
    def run_duration_in_milliseconds(self, run_duration_in_milliseconds):
        """
        Sets the run_duration_in_milliseconds of this RunSummary.
        The duration of the run in milliseconds.


        :param run_duration_in_milliseconds: The run_duration_in_milliseconds of this RunSummary.
        :type: int
        """
        self._run_duration_in_milliseconds = run_duration_in_milliseconds

    @property
    def total_o_cpu(self):
        """
        Gets the total_o_cpu of this RunSummary.
        The total number of oCPU requested by the run.


        :return: The total_o_cpu of this RunSummary.
        :rtype: int
        """
        return self._total_o_cpu

    @total_o_cpu.setter
    def total_o_cpu(self, total_o_cpu):
        """
        Sets the total_o_cpu of this RunSummary.
        The total number of oCPU requested by the run.


        :param total_o_cpu: The total_o_cpu of this RunSummary.
        :type: int
        """
        self._total_o_cpu = total_o_cpu

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this RunSummary.
        The date and time a application was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this RunSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RunSummary.
        The date and time a application was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this RunSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this RunSummary.
        The date and time a application was updated, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this RunSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RunSummary.
        The date and time a application was updated, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this RunSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def type(self):
        """
        Gets the type of this RunSummary.
        The Spark application processing type.

        Allowed values for this property are: "BATCH", "STREAMING", "SESSION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this RunSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RunSummary.
        The Spark application processing type.


        :param type: The type of this RunSummary.
        :type: str
        """
        allowed_values = ["BATCH", "STREAMING", "SESSION"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
