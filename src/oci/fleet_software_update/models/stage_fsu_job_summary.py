# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .fsu_job_summary import FsuJobSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StageFsuJobSummary(FsuJobSummary):
    """
    Summary of Stage Exadata Fleet Update Job resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StageFsuJobSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.StageFsuJobSummary.type` attribute
        of this class is ``STAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this StageFsuJobSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this StageFsuJobSummary.
        :type display_name: str

        :param type:
            The value to assign to the type property of this StageFsuJobSummary.
            Allowed values for this property are: "STAGE", "PRECHECK", "APPLY", "ROLLBACK_AND_REMOVE_TARGET", "CLEANUP"
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this StageFsuJobSummary.
        :type compartment_id: str

        :param fsu_action_id:
            The value to assign to the fsu_action_id property of this StageFsuJobSummary.
        :type fsu_action_id: str

        :param progress:
            The value to assign to the progress property of this StageFsuJobSummary.
        :type progress: oci.fleet_software_update.models.JobProgress

        :param time_created:
            The value to assign to the time_created property of this StageFsuJobSummary.
        :type time_created: datetime

        :param time_started:
            The value to assign to the time_started property of this StageFsuJobSummary.
        :type time_started: datetime

        :param time_updated:
            The value to assign to the time_updated property of this StageFsuJobSummary.
        :type time_updated: datetime

        :param time_finished:
            The value to assign to the time_finished property of this StageFsuJobSummary.
        :type time_finished: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this StageFsuJobSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "UNKNOWN", "TERMINATED", "FAILED", "NEEDS_ATTENTION", "SUCCEEDED", "WAITING", "CANCELING", "CANCELED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this StageFsuJobSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this StageFsuJobSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this StageFsuJobSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this StageFsuJobSummary.
        :type system_tags: dict(str, dict(str, object))

        :param fsu_collection_id:
            The value to assign to the fsu_collection_id property of this StageFsuJobSummary.
        :type fsu_collection_id: str

        :param fsu_cycle_id:
            The value to assign to the fsu_cycle_id property of this StageFsuJobSummary.
        :type fsu_cycle_id: str

        :param target_id:
            The value to assign to the target_id property of this StageFsuJobSummary.
        :type target_id: str

        :param schedule:
            The value to assign to the schedule property of this StageFsuJobSummary.
        :type schedule: oci.fleet_software_update.models.ScheduleDetails

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'type': 'str',
            'compartment_id': 'str',
            'fsu_action_id': 'str',
            'progress': 'JobProgress',
            'time_created': 'datetime',
            'time_started': 'datetime',
            'time_updated': 'datetime',
            'time_finished': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'fsu_collection_id': 'str',
            'fsu_cycle_id': 'str',
            'target_id': 'str',
            'schedule': 'ScheduleDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'type': 'type',
            'compartment_id': 'compartmentId',
            'fsu_action_id': 'fsuActionId',
            'progress': 'progress',
            'time_created': 'timeCreated',
            'time_started': 'timeStarted',
            'time_updated': 'timeUpdated',
            'time_finished': 'timeFinished',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'fsu_collection_id': 'fsuCollectionId',
            'fsu_cycle_id': 'fsuCycleId',
            'target_id': 'targetId',
            'schedule': 'schedule'
        }

        self._id = None
        self._display_name = None
        self._type = None
        self._compartment_id = None
        self._fsu_action_id = None
        self._progress = None
        self._time_created = None
        self._time_started = None
        self._time_updated = None
        self._time_finished = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._fsu_collection_id = None
        self._fsu_cycle_id = None
        self._target_id = None
        self._schedule = None
        self._type = 'STAGE'

    @property
    def fsu_collection_id(self):
        """
        Gets the fsu_collection_id of this StageFsuJobSummary.
        OCID of the Exadata Fleet Update Collection that the job is executing on.


        :return: The fsu_collection_id of this StageFsuJobSummary.
        :rtype: str
        """
        return self._fsu_collection_id

    @fsu_collection_id.setter
    def fsu_collection_id(self, fsu_collection_id):
        """
        Sets the fsu_collection_id of this StageFsuJobSummary.
        OCID of the Exadata Fleet Update Collection that the job is executing on.


        :param fsu_collection_id: The fsu_collection_id of this StageFsuJobSummary.
        :type: str
        """
        self._fsu_collection_id = fsu_collection_id

    @property
    def fsu_cycle_id(self):
        """
        Gets the fsu_cycle_id of this StageFsuJobSummary.
        OCID of the Exadata Fleet Update Cycle that this job is part of.


        :return: The fsu_cycle_id of this StageFsuJobSummary.
        :rtype: str
        """
        return self._fsu_cycle_id

    @fsu_cycle_id.setter
    def fsu_cycle_id(self, fsu_cycle_id):
        """
        Sets the fsu_cycle_id of this StageFsuJobSummary.
        OCID of the Exadata Fleet Update Cycle that this job is part of.


        :param fsu_cycle_id: The fsu_cycle_id of this StageFsuJobSummary.
        :type: str
        """
        self._fsu_cycle_id = fsu_cycle_id

    @property
    def target_id(self):
        """
        Gets the target_id of this StageFsuJobSummary.
        OCID of Target resource on which the job is executing the action.


        :return: The target_id of this StageFsuJobSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this StageFsuJobSummary.
        OCID of Target resource on which the job is executing the action.


        :param target_id: The target_id of this StageFsuJobSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def schedule(self):
        """
        Gets the schedule of this StageFsuJobSummary.

        :return: The schedule of this StageFsuJobSummary.
        :rtype: oci.fleet_software_update.models.ScheduleDetails
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this StageFsuJobSummary.

        :param schedule: The schedule of this StageFsuJobSummary.
        :type: oci.fleet_software_update.models.ScheduleDetails
        """
        self._schedule = schedule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
