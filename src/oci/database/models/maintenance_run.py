# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaintenanceRun(object):
    """
    Details of a maintenance run.
    """

    #: A constant which can be used with the lifecycle_state property of a MaintenanceRun.
    #: This constant has a value of "SCHEDULED"
    LIFECYCLE_STATE_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceRun.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceRun.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceRun.
    #: This constant has a value of "SKIPPED"
    LIFECYCLE_STATE_SKIPPED = "SKIPPED"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceRun.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceRun.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceRun.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MaintenanceRun.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the target_resource_type property of a MaintenanceRun.
    #: This constant has a value of "AUTONOMOUS_EXADATA_INFRASTRUCTURE"
    TARGET_RESOURCE_TYPE_AUTONOMOUS_EXADATA_INFRASTRUCTURE = "AUTONOMOUS_EXADATA_INFRASTRUCTURE"

    #: A constant which can be used with the target_resource_type property of a MaintenanceRun.
    #: This constant has a value of "AUTONOMOUS_CONTAINER_DATABASE"
    TARGET_RESOURCE_TYPE_AUTONOMOUS_CONTAINER_DATABASE = "AUTONOMOUS_CONTAINER_DATABASE"

    #: A constant which can be used with the target_resource_type property of a MaintenanceRun.
    #: This constant has a value of "EXADATA_DB_SYSTEM"
    TARGET_RESOURCE_TYPE_EXADATA_DB_SYSTEM = "EXADATA_DB_SYSTEM"

    #: A constant which can be used with the target_resource_type property of a MaintenanceRun.
    #: This constant has a value of "CLOUD_EXADATA_INFRASTRUCTURE"
    TARGET_RESOURCE_TYPE_CLOUD_EXADATA_INFRASTRUCTURE = "CLOUD_EXADATA_INFRASTRUCTURE"

    #: A constant which can be used with the target_resource_type property of a MaintenanceRun.
    #: This constant has a value of "EXACC_INFRASTRUCTURE"
    TARGET_RESOURCE_TYPE_EXACC_INFRASTRUCTURE = "EXACC_INFRASTRUCTURE"

    #: A constant which can be used with the maintenance_type property of a MaintenanceRun.
    #: This constant has a value of "PLANNED"
    MAINTENANCE_TYPE_PLANNED = "PLANNED"

    #: A constant which can be used with the maintenance_type property of a MaintenanceRun.
    #: This constant has a value of "UNPLANNED"
    MAINTENANCE_TYPE_UNPLANNED = "UNPLANNED"

    #: A constant which can be used with the maintenance_subtype property of a MaintenanceRun.
    #: This constant has a value of "QUARTERLY"
    MAINTENANCE_SUBTYPE_QUARTERLY = "QUARTERLY"

    #: A constant which can be used with the maintenance_subtype property of a MaintenanceRun.
    #: This constant has a value of "HARDWARE"
    MAINTENANCE_SUBTYPE_HARDWARE = "HARDWARE"

    #: A constant which can be used with the maintenance_subtype property of a MaintenanceRun.
    #: This constant has a value of "CRITICAL"
    MAINTENANCE_SUBTYPE_CRITICAL = "CRITICAL"

    def __init__(self, **kwargs):
        """
        Initializes a new MaintenanceRun object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MaintenanceRun.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MaintenanceRun.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this MaintenanceRun.
        :type display_name: str

        :param description:
            The value to assign to the description property of this MaintenanceRun.
        :type description: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MaintenanceRun.
            Allowed values for this property are: "SCHEDULED", "IN_PROGRESS", "SUCCEEDED", "SKIPPED", "FAILED", "UPDATING", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MaintenanceRun.
        :type lifecycle_details: str

        :param time_scheduled:
            The value to assign to the time_scheduled property of this MaintenanceRun.
        :type time_scheduled: datetime

        :param time_started:
            The value to assign to the time_started property of this MaintenanceRun.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this MaintenanceRun.
        :type time_ended: datetime

        :param target_resource_type:
            The value to assign to the target_resource_type property of this MaintenanceRun.
            Allowed values for this property are: "AUTONOMOUS_EXADATA_INFRASTRUCTURE", "AUTONOMOUS_CONTAINER_DATABASE", "EXADATA_DB_SYSTEM", "CLOUD_EXADATA_INFRASTRUCTURE", "EXACC_INFRASTRUCTURE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type target_resource_type: str

        :param target_resource_id:
            The value to assign to the target_resource_id property of this MaintenanceRun.
        :type target_resource_id: str

        :param maintenance_type:
            The value to assign to the maintenance_type property of this MaintenanceRun.
            Allowed values for this property are: "PLANNED", "UNPLANNED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type maintenance_type: str

        :param patch_id:
            The value to assign to the patch_id property of this MaintenanceRun.
        :type patch_id: str

        :param maintenance_subtype:
            The value to assign to the maintenance_subtype property of this MaintenanceRun.
            Allowed values for this property are: "QUARTERLY", "HARDWARE", "CRITICAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type maintenance_subtype: str

        :param peer_maintenance_run_id:
            The value to assign to the peer_maintenance_run_id property of this MaintenanceRun.
        :type peer_maintenance_run_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_scheduled': 'datetime',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'target_resource_type': 'str',
            'target_resource_id': 'str',
            'maintenance_type': 'str',
            'patch_id': 'str',
            'maintenance_subtype': 'str',
            'peer_maintenance_run_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_scheduled': 'timeScheduled',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'target_resource_type': 'targetResourceType',
            'target_resource_id': 'targetResourceId',
            'maintenance_type': 'maintenanceType',
            'patch_id': 'patchId',
            'maintenance_subtype': 'maintenanceSubtype',
            'peer_maintenance_run_id': 'peerMaintenanceRunId'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_scheduled = None
        self._time_started = None
        self._time_ended = None
        self._target_resource_type = None
        self._target_resource_id = None
        self._maintenance_type = None
        self._patch_id = None
        self._maintenance_subtype = None
        self._peer_maintenance_run_id = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MaintenanceRun.
        The OCID of the maintenance run.


        :return: The id of this MaintenanceRun.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MaintenanceRun.
        The OCID of the maintenance run.


        :param id: The id of this MaintenanceRun.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MaintenanceRun.
        The OCID of the compartment.


        :return: The compartment_id of this MaintenanceRun.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MaintenanceRun.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this MaintenanceRun.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this MaintenanceRun.
        The user-friendly name for the maintenance run.


        :return: The display_name of this MaintenanceRun.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MaintenanceRun.
        The user-friendly name for the maintenance run.


        :param display_name: The display_name of this MaintenanceRun.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this MaintenanceRun.
        Description of the maintenance run.


        :return: The description of this MaintenanceRun.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MaintenanceRun.
        Description of the maintenance run.


        :param description: The description of this MaintenanceRun.
        :type: str
        """
        self._description = description

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MaintenanceRun.
        The current state of the maintenance run.

        Allowed values for this property are: "SCHEDULED", "IN_PROGRESS", "SUCCEEDED", "SKIPPED", "FAILED", "UPDATING", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MaintenanceRun.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MaintenanceRun.
        The current state of the maintenance run.


        :param lifecycle_state: The lifecycle_state of this MaintenanceRun.
        :type: str
        """
        allowed_values = ["SCHEDULED", "IN_PROGRESS", "SUCCEEDED", "SKIPPED", "FAILED", "UPDATING", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this MaintenanceRun.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this MaintenanceRun.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this MaintenanceRun.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this MaintenanceRun.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_scheduled(self):
        """
        **[Required]** Gets the time_scheduled of this MaintenanceRun.
        The date and time the maintenance run is scheduled to occur.


        :return: The time_scheduled of this MaintenanceRun.
        :rtype: datetime
        """
        return self._time_scheduled

    @time_scheduled.setter
    def time_scheduled(self, time_scheduled):
        """
        Sets the time_scheduled of this MaintenanceRun.
        The date and time the maintenance run is scheduled to occur.


        :param time_scheduled: The time_scheduled of this MaintenanceRun.
        :type: datetime
        """
        self._time_scheduled = time_scheduled

    @property
    def time_started(self):
        """
        Gets the time_started of this MaintenanceRun.
        The date and time the maintenance run starts.


        :return: The time_started of this MaintenanceRun.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this MaintenanceRun.
        The date and time the maintenance run starts.


        :param time_started: The time_started of this MaintenanceRun.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this MaintenanceRun.
        The date and time the maintenance run was completed.


        :return: The time_ended of this MaintenanceRun.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this MaintenanceRun.
        The date and time the maintenance run was completed.


        :param time_ended: The time_ended of this MaintenanceRun.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def target_resource_type(self):
        """
        Gets the target_resource_type of this MaintenanceRun.
        The type of the target resource on which the maintenance run occurs.

        Allowed values for this property are: "AUTONOMOUS_EXADATA_INFRASTRUCTURE", "AUTONOMOUS_CONTAINER_DATABASE", "EXADATA_DB_SYSTEM", "CLOUD_EXADATA_INFRASTRUCTURE", "EXACC_INFRASTRUCTURE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The target_resource_type of this MaintenanceRun.
        :rtype: str
        """
        return self._target_resource_type

    @target_resource_type.setter
    def target_resource_type(self, target_resource_type):
        """
        Sets the target_resource_type of this MaintenanceRun.
        The type of the target resource on which the maintenance run occurs.


        :param target_resource_type: The target_resource_type of this MaintenanceRun.
        :type: str
        """
        allowed_values = ["AUTONOMOUS_EXADATA_INFRASTRUCTURE", "AUTONOMOUS_CONTAINER_DATABASE", "EXADATA_DB_SYSTEM", "CLOUD_EXADATA_INFRASTRUCTURE", "EXACC_INFRASTRUCTURE"]
        if not value_allowed_none_or_none_sentinel(target_resource_type, allowed_values):
            target_resource_type = 'UNKNOWN_ENUM_VALUE'
        self._target_resource_type = target_resource_type

    @property
    def target_resource_id(self):
        """
        Gets the target_resource_id of this MaintenanceRun.
        The ID of the target resource on which the maintenance run occurs.


        :return: The target_resource_id of this MaintenanceRun.
        :rtype: str
        """
        return self._target_resource_id

    @target_resource_id.setter
    def target_resource_id(self, target_resource_id):
        """
        Sets the target_resource_id of this MaintenanceRun.
        The ID of the target resource on which the maintenance run occurs.


        :param target_resource_id: The target_resource_id of this MaintenanceRun.
        :type: str
        """
        self._target_resource_id = target_resource_id

    @property
    def maintenance_type(self):
        """
        Gets the maintenance_type of this MaintenanceRun.
        Maintenance type.

        Allowed values for this property are: "PLANNED", "UNPLANNED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The maintenance_type of this MaintenanceRun.
        :rtype: str
        """
        return self._maintenance_type

    @maintenance_type.setter
    def maintenance_type(self, maintenance_type):
        """
        Sets the maintenance_type of this MaintenanceRun.
        Maintenance type.


        :param maintenance_type: The maintenance_type of this MaintenanceRun.
        :type: str
        """
        allowed_values = ["PLANNED", "UNPLANNED"]
        if not value_allowed_none_or_none_sentinel(maintenance_type, allowed_values):
            maintenance_type = 'UNKNOWN_ENUM_VALUE'
        self._maintenance_type = maintenance_type

    @property
    def patch_id(self):
        """
        Gets the patch_id of this MaintenanceRun.
        The unique identifier of the patch. The identifier string includes the patch type, the Oracle Database version, and the patch creation date (using the format YYMMDD). For example, the identifier `ru_patch_19.9.0.0_201030` is used for an RU patch for Oracle Database 19.9.0.0 that was released October 30, 2020.


        :return: The patch_id of this MaintenanceRun.
        :rtype: str
        """
        return self._patch_id

    @patch_id.setter
    def patch_id(self, patch_id):
        """
        Sets the patch_id of this MaintenanceRun.
        The unique identifier of the patch. The identifier string includes the patch type, the Oracle Database version, and the patch creation date (using the format YYMMDD). For example, the identifier `ru_patch_19.9.0.0_201030` is used for an RU patch for Oracle Database 19.9.0.0 that was released October 30, 2020.


        :param patch_id: The patch_id of this MaintenanceRun.
        :type: str
        """
        self._patch_id = patch_id

    @property
    def maintenance_subtype(self):
        """
        Gets the maintenance_subtype of this MaintenanceRun.
        Maintenance sub-type.

        Allowed values for this property are: "QUARTERLY", "HARDWARE", "CRITICAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The maintenance_subtype of this MaintenanceRun.
        :rtype: str
        """
        return self._maintenance_subtype

    @maintenance_subtype.setter
    def maintenance_subtype(self, maintenance_subtype):
        """
        Sets the maintenance_subtype of this MaintenanceRun.
        Maintenance sub-type.


        :param maintenance_subtype: The maintenance_subtype of this MaintenanceRun.
        :type: str
        """
        allowed_values = ["QUARTERLY", "HARDWARE", "CRITICAL"]
        if not value_allowed_none_or_none_sentinel(maintenance_subtype, allowed_values):
            maintenance_subtype = 'UNKNOWN_ENUM_VALUE'
        self._maintenance_subtype = maintenance_subtype

    @property
    def peer_maintenance_run_id(self):
        """
        Gets the peer_maintenance_run_id of this MaintenanceRun.
        The `OCID`__ of the maintenance run for the Autonomous Data Guard association's peer container database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The peer_maintenance_run_id of this MaintenanceRun.
        :rtype: str
        """
        return self._peer_maintenance_run_id

    @peer_maintenance_run_id.setter
    def peer_maintenance_run_id(self, peer_maintenance_run_id):
        """
        Sets the peer_maintenance_run_id of this MaintenanceRun.
        The `OCID`__ of the maintenance run for the Autonomous Data Guard association's peer container database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param peer_maintenance_run_id: The peer_maintenance_run_id of this MaintenanceRun.
        :type: str
        """
        self._peer_maintenance_run_id = peer_maintenance_run_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
