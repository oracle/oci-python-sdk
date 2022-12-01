# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaskingReport(object):
    """
    A masking report contains information about a completed masking request. It includes details such as the target database masked,
    masking policy used, masking start and finish time, total number of schemas, tables, columns and values masked, masked columns, and the masking formats used.
    """

    #: A constant which can be used with the lifecycle_state property of a MaskingReport.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MaskingReport.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MaskingReport.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MaskingReport.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MaskingReport.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MaskingReport.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a MaskingReport.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new MaskingReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MaskingReport.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MaskingReport.
        :type compartment_id: str

        :param masking_work_request_id:
            The value to assign to the masking_work_request_id property of this MaskingReport.
        :type masking_work_request_id: str

        :param masking_policy_id:
            The value to assign to the masking_policy_id property of this MaskingReport.
        :type masking_policy_id: str

        :param target_id:
            The value to assign to the target_id property of this MaskingReport.
        :type target_id: str

        :param total_masked_sensitive_types:
            The value to assign to the total_masked_sensitive_types property of this MaskingReport.
        :type total_masked_sensitive_types: int

        :param total_masked_schemas:
            The value to assign to the total_masked_schemas property of this MaskingReport.
        :type total_masked_schemas: int

        :param total_masked_objects:
            The value to assign to the total_masked_objects property of this MaskingReport.
        :type total_masked_objects: int

        :param total_masked_columns:
            The value to assign to the total_masked_columns property of this MaskingReport.
        :type total_masked_columns: int

        :param total_masked_values:
            The value to assign to the total_masked_values property of this MaskingReport.
        :type total_masked_values: int

        :param time_masking_started:
            The value to assign to the time_masking_started property of this MaskingReport.
        :type time_masking_started: datetime

        :param time_masking_finished:
            The value to assign to the time_masking_finished property of this MaskingReport.
        :type time_masking_finished: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MaskingReport.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this MaskingReport.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'masking_work_request_id': 'str',
            'masking_policy_id': 'str',
            'target_id': 'str',
            'total_masked_sensitive_types': 'int',
            'total_masked_schemas': 'int',
            'total_masked_objects': 'int',
            'total_masked_columns': 'int',
            'total_masked_values': 'int',
            'time_masking_started': 'datetime',
            'time_masking_finished': 'datetime',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'masking_work_request_id': 'maskingWorkRequestId',
            'masking_policy_id': 'maskingPolicyId',
            'target_id': 'targetId',
            'total_masked_sensitive_types': 'totalMaskedSensitiveTypes',
            'total_masked_schemas': 'totalMaskedSchemas',
            'total_masked_objects': 'totalMaskedObjects',
            'total_masked_columns': 'totalMaskedColumns',
            'total_masked_values': 'totalMaskedValues',
            'time_masking_started': 'timeMaskingStarted',
            'time_masking_finished': 'timeMaskingFinished',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._compartment_id = None
        self._masking_work_request_id = None
        self._masking_policy_id = None
        self._target_id = None
        self._total_masked_sensitive_types = None
        self._total_masked_schemas = None
        self._total_masked_objects = None
        self._total_masked_columns = None
        self._total_masked_values = None
        self._time_masking_started = None
        self._time_masking_finished = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MaskingReport.
        The OCID of the masking report.


        :return: The id of this MaskingReport.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MaskingReport.
        The OCID of the masking report.


        :param id: The id of this MaskingReport.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MaskingReport.
        The OCID of the compartment that contains the masking report.


        :return: The compartment_id of this MaskingReport.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MaskingReport.
        The OCID of the compartment that contains the masking report.


        :param compartment_id: The compartment_id of this MaskingReport.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def masking_work_request_id(self):
        """
        **[Required]** Gets the masking_work_request_id of this MaskingReport.
        The OCID of the masking work request that resulted in this masking report.


        :return: The masking_work_request_id of this MaskingReport.
        :rtype: str
        """
        return self._masking_work_request_id

    @masking_work_request_id.setter
    def masking_work_request_id(self, masking_work_request_id):
        """
        Sets the masking_work_request_id of this MaskingReport.
        The OCID of the masking work request that resulted in this masking report.


        :param masking_work_request_id: The masking_work_request_id of this MaskingReport.
        :type: str
        """
        self._masking_work_request_id = masking_work_request_id

    @property
    def masking_policy_id(self):
        """
        **[Required]** Gets the masking_policy_id of this MaskingReport.
        The OCID of the masking policy used.


        :return: The masking_policy_id of this MaskingReport.
        :rtype: str
        """
        return self._masking_policy_id

    @masking_policy_id.setter
    def masking_policy_id(self, masking_policy_id):
        """
        Sets the masking_policy_id of this MaskingReport.
        The OCID of the masking policy used.


        :param masking_policy_id: The masking_policy_id of this MaskingReport.
        :type: str
        """
        self._masking_policy_id = masking_policy_id

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this MaskingReport.
        The OCID of the target database masked.


        :return: The target_id of this MaskingReport.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this MaskingReport.
        The OCID of the target database masked.


        :param target_id: The target_id of this MaskingReport.
        :type: str
        """
        self._target_id = target_id

    @property
    def total_masked_sensitive_types(self):
        """
        **[Required]** Gets the total_masked_sensitive_types of this MaskingReport.
        The total number of unique sensitive types associated with the masked columns.


        :return: The total_masked_sensitive_types of this MaskingReport.
        :rtype: int
        """
        return self._total_masked_sensitive_types

    @total_masked_sensitive_types.setter
    def total_masked_sensitive_types(self, total_masked_sensitive_types):
        """
        Sets the total_masked_sensitive_types of this MaskingReport.
        The total number of unique sensitive types associated with the masked columns.


        :param total_masked_sensitive_types: The total_masked_sensitive_types of this MaskingReport.
        :type: int
        """
        self._total_masked_sensitive_types = total_masked_sensitive_types

    @property
    def total_masked_schemas(self):
        """
        **[Required]** Gets the total_masked_schemas of this MaskingReport.
        The total number of unique schemas that contain the masked columns.


        :return: The total_masked_schemas of this MaskingReport.
        :rtype: int
        """
        return self._total_masked_schemas

    @total_masked_schemas.setter
    def total_masked_schemas(self, total_masked_schemas):
        """
        Sets the total_masked_schemas of this MaskingReport.
        The total number of unique schemas that contain the masked columns.


        :param total_masked_schemas: The total_masked_schemas of this MaskingReport.
        :type: int
        """
        self._total_masked_schemas = total_masked_schemas

    @property
    def total_masked_objects(self):
        """
        **[Required]** Gets the total_masked_objects of this MaskingReport.
        The total number of unique objects (tables and editioning views) that contain the masked columns.


        :return: The total_masked_objects of this MaskingReport.
        :rtype: int
        """
        return self._total_masked_objects

    @total_masked_objects.setter
    def total_masked_objects(self, total_masked_objects):
        """
        Sets the total_masked_objects of this MaskingReport.
        The total number of unique objects (tables and editioning views) that contain the masked columns.


        :param total_masked_objects: The total_masked_objects of this MaskingReport.
        :type: int
        """
        self._total_masked_objects = total_masked_objects

    @property
    def total_masked_columns(self):
        """
        **[Required]** Gets the total_masked_columns of this MaskingReport.
        The total number of masked columns.


        :return: The total_masked_columns of this MaskingReport.
        :rtype: int
        """
        return self._total_masked_columns

    @total_masked_columns.setter
    def total_masked_columns(self, total_masked_columns):
        """
        Sets the total_masked_columns of this MaskingReport.
        The total number of masked columns.


        :param total_masked_columns: The total_masked_columns of this MaskingReport.
        :type: int
        """
        self._total_masked_columns = total_masked_columns

    @property
    def total_masked_values(self):
        """
        **[Required]** Gets the total_masked_values of this MaskingReport.
        The total number of masked values.


        :return: The total_masked_values of this MaskingReport.
        :rtype: int
        """
        return self._total_masked_values

    @total_masked_values.setter
    def total_masked_values(self, total_masked_values):
        """
        Sets the total_masked_values of this MaskingReport.
        The total number of masked values.


        :param total_masked_values: The total_masked_values of this MaskingReport.
        :type: int
        """
        self._total_masked_values = total_masked_values

    @property
    def time_masking_started(self):
        """
        **[Required]** Gets the time_masking_started of this MaskingReport.
        The date and time data masking started, in the format defined by `RFC3339`__

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_masking_started of this MaskingReport.
        :rtype: datetime
        """
        return self._time_masking_started

    @time_masking_started.setter
    def time_masking_started(self, time_masking_started):
        """
        Sets the time_masking_started of this MaskingReport.
        The date and time data masking started, in the format defined by `RFC3339`__

        __ https://tools.ietf.org/html/rfc3339


        :param time_masking_started: The time_masking_started of this MaskingReport.
        :type: datetime
        """
        self._time_masking_started = time_masking_started

    @property
    def time_masking_finished(self):
        """
        **[Required]** Gets the time_masking_finished of this MaskingReport.
        The date and time data masking finished, in the format defined by `RFC3339`__

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_masking_finished of this MaskingReport.
        :rtype: datetime
        """
        return self._time_masking_finished

    @time_masking_finished.setter
    def time_masking_finished(self, time_masking_finished):
        """
        Sets the time_masking_finished of this MaskingReport.
        The date and time data masking finished, in the format defined by `RFC3339`__

        __ https://tools.ietf.org/html/rfc3339


        :param time_masking_finished: The time_masking_finished of this MaskingReport.
        :type: datetime
        """
        self._time_masking_finished = time_masking_finished

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MaskingReport.
        The current state of the masking report.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MaskingReport.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MaskingReport.
        The current state of the masking report.


        :param lifecycle_state: The lifecycle_state of this MaskingReport.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this MaskingReport.
        The date and time the masking report was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this MaskingReport.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MaskingReport.
        The date and time the masking report was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this MaskingReport.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
