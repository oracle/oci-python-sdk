# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsEmBridgeSummary(object):
    """
    Enterprise manager bridge summary.
    """

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsEmBridgeSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsEmBridgeSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsEmBridgeSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsEmBridgeSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the last_import_processing_status property of a LogAnalyticsEmBridgeSummary.
    #: This constant has a value of "NOT_STARTED"
    LAST_IMPORT_PROCESSING_STATUS_NOT_STARTED = "NOT_STARTED"

    #: A constant which can be used with the last_import_processing_status property of a LogAnalyticsEmBridgeSummary.
    #: This constant has a value of "SUCCESS"
    LAST_IMPORT_PROCESSING_STATUS_SUCCESS = "SUCCESS"

    #: A constant which can be used with the last_import_processing_status property of a LogAnalyticsEmBridgeSummary.
    #: This constant has a value of "IN_PROGRESS"
    LAST_IMPORT_PROCESSING_STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the last_import_processing_status property of a LogAnalyticsEmBridgeSummary.
    #: This constant has a value of "FAILED"
    LAST_IMPORT_PROCESSING_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the last_import_processing_status property of a LogAnalyticsEmBridgeSummary.
    #: This constant has a value of "PARTIAL_SUCCESS"
    LAST_IMPORT_PROCESSING_STATUS_PARTIAL_SUCCESS = "PARTIAL_SUCCESS"

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsEmBridgeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this LogAnalyticsEmBridgeSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this LogAnalyticsEmBridgeSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this LogAnalyticsEmBridgeSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LogAnalyticsEmBridgeSummary.
        :type compartment_id: str

        :param em_entities_compartment_id:
            The value to assign to the em_entities_compartment_id property of this LogAnalyticsEmBridgeSummary.
        :type em_entities_compartment_id: str

        :param bucket_name:
            The value to assign to the bucket_name property of this LogAnalyticsEmBridgeSummary.
        :type bucket_name: str

        :param time_created:
            The value to assign to the time_created property of this LogAnalyticsEmBridgeSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this LogAnalyticsEmBridgeSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LogAnalyticsEmBridgeSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this LogAnalyticsEmBridgeSummary.
        :type lifecycle_details: str

        :param last_import_processing_status:
            The value to assign to the last_import_processing_status property of this LogAnalyticsEmBridgeSummary.
            Allowed values for this property are: "NOT_STARTED", "SUCCESS", "IN_PROGRESS", "FAILED", "PARTIAL_SUCCESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type last_import_processing_status: str

        :param last_import_processing_details:
            The value to assign to the last_import_processing_details property of this LogAnalyticsEmBridgeSummary.
        :type last_import_processing_details: str

        :param time_import_last_processed:
            The value to assign to the time_import_last_processed property of this LogAnalyticsEmBridgeSummary.
        :type time_import_last_processed: datetime

        :param time_em_data_last_extracted:
            The value to assign to the time_em_data_last_extracted property of this LogAnalyticsEmBridgeSummary.
        :type time_em_data_last_extracted: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LogAnalyticsEmBridgeSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this LogAnalyticsEmBridgeSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'em_entities_compartment_id': 'str',
            'bucket_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'last_import_processing_status': 'str',
            'last_import_processing_details': 'str',
            'time_import_last_processed': 'datetime',
            'time_em_data_last_extracted': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'em_entities_compartment_id': 'emEntitiesCompartmentId',
            'bucket_name': 'bucketName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'last_import_processing_status': 'lastImportProcessingStatus',
            'last_import_processing_details': 'lastImportProcessingDetails',
            'time_import_last_processed': 'timeImportLastProcessed',
            'time_em_data_last_extracted': 'timeEmDataLastExtracted',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._em_entities_compartment_id = None
        self._bucket_name = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._last_import_processing_status = None
        self._last_import_processing_details = None
        self._time_import_last_processed = None
        self._time_em_data_last_extracted = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this LogAnalyticsEmBridgeSummary.
        The enterprise manager bridge OCID.


        :return: The id of this LogAnalyticsEmBridgeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LogAnalyticsEmBridgeSummary.
        The enterprise manager bridge OCID.


        :param id: The id of this LogAnalyticsEmBridgeSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this LogAnalyticsEmBridgeSummary.
        Log analytics enterprise manager bridge display name.


        :return: The display_name of this LogAnalyticsEmBridgeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LogAnalyticsEmBridgeSummary.
        Log analytics enterprise manager bridge display name.


        :param display_name: The display_name of this LogAnalyticsEmBridgeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsEmBridgeSummary.
        A description for log analytics enterprise manager bridge.


        :return: The description of this LogAnalyticsEmBridgeSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsEmBridgeSummary.
        A description for log analytics enterprise manager bridge.


        :param description: The description of this LogAnalyticsEmBridgeSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LogAnalyticsEmBridgeSummary.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this LogAnalyticsEmBridgeSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LogAnalyticsEmBridgeSummary.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this LogAnalyticsEmBridgeSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def em_entities_compartment_id(self):
        """
        **[Required]** Gets the em_entities_compartment_id of this LogAnalyticsEmBridgeSummary.
        Compartment for entities created from enterprise manager.


        :return: The em_entities_compartment_id of this LogAnalyticsEmBridgeSummary.
        :rtype: str
        """
        return self._em_entities_compartment_id

    @em_entities_compartment_id.setter
    def em_entities_compartment_id(self, em_entities_compartment_id):
        """
        Sets the em_entities_compartment_id of this LogAnalyticsEmBridgeSummary.
        Compartment for entities created from enterprise manager.


        :param em_entities_compartment_id: The em_entities_compartment_id of this LogAnalyticsEmBridgeSummary.
        :type: str
        """
        self._em_entities_compartment_id = em_entities_compartment_id

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this LogAnalyticsEmBridgeSummary.
        Object store bucket name where enterprise manager harvested entities will be uploaded.


        :return: The bucket_name of this LogAnalyticsEmBridgeSummary.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this LogAnalyticsEmBridgeSummary.
        Object store bucket name where enterprise manager harvested entities will be uploaded.


        :param bucket_name: The bucket_name of this LogAnalyticsEmBridgeSummary.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this LogAnalyticsEmBridgeSummary.
        The date and time the resource was created, in the format defined by RFC3339.


        :return: The time_created of this LogAnalyticsEmBridgeSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LogAnalyticsEmBridgeSummary.
        The date and time the resource was created, in the format defined by RFC3339.


        :param time_created: The time_created of this LogAnalyticsEmBridgeSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this LogAnalyticsEmBridgeSummary.
        The date and time the resource was last updated, in the format defined by RFC3339.


        :return: The time_updated of this LogAnalyticsEmBridgeSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this LogAnalyticsEmBridgeSummary.
        The date and time the resource was last updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this LogAnalyticsEmBridgeSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this LogAnalyticsEmBridgeSummary.
        The current state of the enterprise manager bridge.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LogAnalyticsEmBridgeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LogAnalyticsEmBridgeSummary.
        The current state of the enterprise manager bridge.


        :param lifecycle_state: The lifecycle_state of this LogAnalyticsEmBridgeSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this LogAnalyticsEmBridgeSummary.
        lifecycleDetails has additional information regarding substeps such as verifying connection to object store.


        :return: The lifecycle_details of this LogAnalyticsEmBridgeSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this LogAnalyticsEmBridgeSummary.
        lifecycleDetails has additional information regarding substeps such as verifying connection to object store.


        :param lifecycle_details: The lifecycle_details of this LogAnalyticsEmBridgeSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def last_import_processing_status(self):
        """
        **[Required]** Gets the last_import_processing_status of this LogAnalyticsEmBridgeSummary.
        The status from last processing status of enterprise manager upload.

        Allowed values for this property are: "NOT_STARTED", "SUCCESS", "IN_PROGRESS", "FAILED", "PARTIAL_SUCCESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The last_import_processing_status of this LogAnalyticsEmBridgeSummary.
        :rtype: str
        """
        return self._last_import_processing_status

    @last_import_processing_status.setter
    def last_import_processing_status(self, last_import_processing_status):
        """
        Sets the last_import_processing_status of this LogAnalyticsEmBridgeSummary.
        The status from last processing status of enterprise manager upload.


        :param last_import_processing_status: The last_import_processing_status of this LogAnalyticsEmBridgeSummary.
        :type: str
        """
        allowed_values = ["NOT_STARTED", "SUCCESS", "IN_PROGRESS", "FAILED", "PARTIAL_SUCCESS"]
        if not value_allowed_none_or_none_sentinel(last_import_processing_status, allowed_values):
            last_import_processing_status = 'UNKNOWN_ENUM_VALUE'
        self._last_import_processing_status = last_import_processing_status

    @property
    def last_import_processing_details(self):
        """
        Gets the last_import_processing_details of this LogAnalyticsEmBridgeSummary.
        Processing status details of enterprise manager upload. This provides additional details
        for failed status


        :return: The last_import_processing_details of this LogAnalyticsEmBridgeSummary.
        :rtype: str
        """
        return self._last_import_processing_details

    @last_import_processing_details.setter
    def last_import_processing_details(self, last_import_processing_details):
        """
        Sets the last_import_processing_details of this LogAnalyticsEmBridgeSummary.
        Processing status details of enterprise manager upload. This provides additional details
        for failed status


        :param last_import_processing_details: The last_import_processing_details of this LogAnalyticsEmBridgeSummary.
        :type: str
        """
        self._last_import_processing_details = last_import_processing_details

    @property
    def time_import_last_processed(self):
        """
        Gets the time_import_last_processed of this LogAnalyticsEmBridgeSummary.
        The last time of enterprise manager upload was processed. This is in the format defined by RFC3339


        :return: The time_import_last_processed of this LogAnalyticsEmBridgeSummary.
        :rtype: datetime
        """
        return self._time_import_last_processed

    @time_import_last_processed.setter
    def time_import_last_processed(self, time_import_last_processed):
        """
        Sets the time_import_last_processed of this LogAnalyticsEmBridgeSummary.
        The last time of enterprise manager upload was processed. This is in the format defined by RFC3339


        :param time_import_last_processed: The time_import_last_processed of this LogAnalyticsEmBridgeSummary.
        :type: datetime
        """
        self._time_import_last_processed = time_import_last_processed

    @property
    def time_em_data_last_extracted(self):
        """
        Gets the time_em_data_last_extracted of this LogAnalyticsEmBridgeSummary.
        The timestamp of last enterprise manager upload to OCI Object Store. This is in the format defined by RFC3339


        :return: The time_em_data_last_extracted of this LogAnalyticsEmBridgeSummary.
        :rtype: datetime
        """
        return self._time_em_data_last_extracted

    @time_em_data_last_extracted.setter
    def time_em_data_last_extracted(self, time_em_data_last_extracted):
        """
        Sets the time_em_data_last_extracted of this LogAnalyticsEmBridgeSummary.
        The timestamp of last enterprise manager upload to OCI Object Store. This is in the format defined by RFC3339


        :param time_em_data_last_extracted: The time_em_data_last_extracted of this LogAnalyticsEmBridgeSummary.
        :type: datetime
        """
        self._time_em_data_last_extracted = time_em_data_last_extracted

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this LogAnalyticsEmBridgeSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this LogAnalyticsEmBridgeSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this LogAnalyticsEmBridgeSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this LogAnalyticsEmBridgeSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this LogAnalyticsEmBridgeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this LogAnalyticsEmBridgeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this LogAnalyticsEmBridgeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this LogAnalyticsEmBridgeSummary.
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
