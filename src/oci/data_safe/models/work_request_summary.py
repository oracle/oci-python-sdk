# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestSummary(object):
    """
    Summary of a work request.
    """

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "ENABLE_DATA_SAFE_CONFIGURATION"
    OPERATION_TYPE_ENABLE_DATA_SAFE_CONFIGURATION = "ENABLE_DATA_SAFE_CONFIGURATION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_PRIVATE_ENDPOINT"
    OPERATION_TYPE_CREATE_PRIVATE_ENDPOINT = "CREATE_PRIVATE_ENDPOINT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_PRIVATE_ENDPOINT"
    OPERATION_TYPE_UPDATE_PRIVATE_ENDPOINT = "UPDATE_PRIVATE_ENDPOINT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_PRIVATE_ENDPOINT"
    OPERATION_TYPE_DELETE_PRIVATE_ENDPOINT = "DELETE_PRIVATE_ENDPOINT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_PRIVATE_ENDPOINT_COMPARTMENT"
    OPERATION_TYPE_CHANGE_PRIVATE_ENDPOINT_COMPARTMENT = "CHANGE_PRIVATE_ENDPOINT_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_ONPREM_CONNECTOR"
    OPERATION_TYPE_CREATE_ONPREM_CONNECTOR = "CREATE_ONPREM_CONNECTOR"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_ONPREM_CONNECTOR"
    OPERATION_TYPE_UPDATE_ONPREM_CONNECTOR = "UPDATE_ONPREM_CONNECTOR"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_ONPREM_CONNECTOR"
    OPERATION_TYPE_DELETE_ONPREM_CONNECTOR = "DELETE_ONPREM_CONNECTOR"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_ONPREM_CONNECTOR_WALLET"
    OPERATION_TYPE_UPDATE_ONPREM_CONNECTOR_WALLET = "UPDATE_ONPREM_CONNECTOR_WALLET"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_ONPREM_CONNECTOR_COMPARTMENT"
    OPERATION_TYPE_CHANGE_ONPREM_CONNECTOR_COMPARTMENT = "CHANGE_ONPREM_CONNECTOR_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "PROVISION_POLICY"
    OPERATION_TYPE_PROVISION_POLICY = "PROVISION_POLICY"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "RETRIEVE_POLICY"
    OPERATION_TYPE_RETRIEVE_POLICY = "RETRIEVE_POLICY"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_POLICY"
    OPERATION_TYPE_UPDATE_POLICY = "UPDATE_POLICY"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_POLICY_COMPARTMENT"
    OPERATION_TYPE_CHANGE_POLICY_COMPARTMENT = "CHANGE_POLICY_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_TARGET_DATABASE"
    OPERATION_TYPE_CREATE_TARGET_DATABASE = "CREATE_TARGET_DATABASE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_TARGET_DATABASE"
    OPERATION_TYPE_UPDATE_TARGET_DATABASE = "UPDATE_TARGET_DATABASE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "ACTIVATE_TARGET_DATABASE"
    OPERATION_TYPE_ACTIVATE_TARGET_DATABASE = "ACTIVATE_TARGET_DATABASE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DEACTIVATE_TARGET_DATABASE"
    OPERATION_TYPE_DEACTIVATE_TARGET_DATABASE = "DEACTIVATE_TARGET_DATABASE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_TARGET_DATABASE"
    OPERATION_TYPE_DELETE_TARGET_DATABASE = "DELETE_TARGET_DATABASE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_TARGET_DATABASE_COMPARTMENT"
    OPERATION_TYPE_CHANGE_TARGET_DATABASE_COMPARTMENT = "CHANGE_TARGET_DATABASE_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_USER_ASSESSMENT"
    OPERATION_TYPE_CREATE_USER_ASSESSMENT = "CREATE_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "ASSESS_USER_ASSESSMENT"
    OPERATION_TYPE_ASSESS_USER_ASSESSMENT = "ASSESS_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SNAPSHOT_USER_ASSESSMENT"
    OPERATION_TYPE_CREATE_SNAPSHOT_USER_ASSESSMENT = "CREATE_SNAPSHOT_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SCHEDULE_USER_ASSESSMENT"
    OPERATION_TYPE_CREATE_SCHEDULE_USER_ASSESSMENT = "CREATE_SCHEDULE_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "COMPARE_WITH_BASELINE_USER_ASSESSMENT"
    OPERATION_TYPE_COMPARE_WITH_BASELINE_USER_ASSESSMENT = "COMPARE_WITH_BASELINE_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_USER_ASSESSMENT"
    OPERATION_TYPE_DELETE_USER_ASSESSMENT = "DELETE_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_USER_ASSESSMENT"
    OPERATION_TYPE_UPDATE_USER_ASSESSMENT = "UPDATE_USER_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_USER_ASSESSMENT_COMPARTMENT"
    OPERATION_TYPE_CHANGE_USER_ASSESSMENT_COMPARTMENT = "CHANGE_USER_ASSESSMENT_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "SET_USER_ASSESSMENT_BASELINE"
    OPERATION_TYPE_SET_USER_ASSESSMENT_BASELINE = "SET_USER_ASSESSMENT_BASELINE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UNSET_USER_ASSESSMENT_BASELINE"
    OPERATION_TYPE_UNSET_USER_ASSESSMENT_BASELINE = "UNSET_USER_ASSESSMENT_BASELINE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "GENERATE_USER_ASSESSMENT_REPORT"
    OPERATION_TYPE_GENERATE_USER_ASSESSMENT_REPORT = "GENERATE_USER_ASSESSMENT_REPORT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SECURITY_ASSESSMENT"
    OPERATION_TYPE_CREATE_SECURITY_ASSESSMENT = "CREATE_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SECURITY_ASSESSMENT_NOW"
    OPERATION_TYPE_CREATE_SECURITY_ASSESSMENT_NOW = "CREATE_SECURITY_ASSESSMENT_NOW"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "ASSESS_SECURITY_ASSESSMENT"
    OPERATION_TYPE_ASSESS_SECURITY_ASSESSMENT = "ASSESS_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SNAPSHOT_SECURITY_ASSESSMENT"
    OPERATION_TYPE_CREATE_SNAPSHOT_SECURITY_ASSESSMENT = "CREATE_SNAPSHOT_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SCHEDULE_SECURITY_ASSESSMENT"
    OPERATION_TYPE_CREATE_SCHEDULE_SECURITY_ASSESSMENT = "CREATE_SCHEDULE_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "COMPARE_WITH_BASELINE_SECURITY_ASSESSMENT"
    OPERATION_TYPE_COMPARE_WITH_BASELINE_SECURITY_ASSESSMENT = "COMPARE_WITH_BASELINE_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_SECURITY_ASSESSMENT"
    OPERATION_TYPE_DELETE_SECURITY_ASSESSMENT = "DELETE_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_SECURITY_ASSESSMENT"
    OPERATION_TYPE_UPDATE_SECURITY_ASSESSMENT = "UPDATE_SECURITY_ASSESSMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_SECURITY_ASSESSMENT_COMPARTMENT"
    OPERATION_TYPE_CHANGE_SECURITY_ASSESSMENT_COMPARTMENT = "CHANGE_SECURITY_ASSESSMENT_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "SET_SECURITY_ASSESSMENT_BASELINE"
    OPERATION_TYPE_SET_SECURITY_ASSESSMENT_BASELINE = "SET_SECURITY_ASSESSMENT_BASELINE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UNSET_SECURITY_ASSESSMENT_BASELINE"
    OPERATION_TYPE_UNSET_SECURITY_ASSESSMENT_BASELINE = "UNSET_SECURITY_ASSESSMENT_BASELINE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "GENERATE_SECURITY_ASSESSMENT_REPORT"
    OPERATION_TYPE_GENERATE_SECURITY_ASSESSMENT_REPORT = "GENERATE_SECURITY_ASSESSMENT_REPORT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CALCULATE_VOLUME"
    OPERATION_TYPE_CALCULATE_VOLUME = "CALCULATE_VOLUME"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CALCULATE_COLLECTED_VOLUME"
    OPERATION_TYPE_CALCULATE_COLLECTED_VOLUME = "CALCULATE_COLLECTED_VOLUME"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "AUDIT_TRAIL"
    OPERATION_TYPE_AUDIT_TRAIL = "AUDIT_TRAIL"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_AUDIT_TRAIL"
    OPERATION_TYPE_DELETE_AUDIT_TRAIL = "DELETE_AUDIT_TRAIL"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DISCOVER_AUDIT_TRAILS"
    OPERATION_TYPE_DISCOVER_AUDIT_TRAILS = "DISCOVER_AUDIT_TRAILS"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_AUDIT_TRAIL"
    OPERATION_TYPE_UPDATE_AUDIT_TRAIL = "UPDATE_AUDIT_TRAIL"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_AUDIT_PROFILE"
    OPERATION_TYPE_UPDATE_AUDIT_PROFILE = "UPDATE_AUDIT_PROFILE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "AUDIT_CHANGE_COMPARTMENT"
    OPERATION_TYPE_AUDIT_CHANGE_COMPARTMENT = "AUDIT_CHANGE_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_REPORT_DEFINITION"
    OPERATION_TYPE_CREATE_REPORT_DEFINITION = "CREATE_REPORT_DEFINITION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_REPORT_DEFINITION"
    OPERATION_TYPE_UPDATE_REPORT_DEFINITION = "UPDATE_REPORT_DEFINITION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_REPORT_DEFINITION_COMPARTMENT"
    OPERATION_TYPE_CHANGE_REPORT_DEFINITION_COMPARTMENT = "CHANGE_REPORT_DEFINITION_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_REPORT_DEFINITION"
    OPERATION_TYPE_DELETE_REPORT_DEFINITION = "DELETE_REPORT_DEFINITION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "GENERATE_REPORT"
    OPERATION_TYPE_GENERATE_REPORT = "GENERATE_REPORT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_REPORT_COMPARTMENT"
    OPERATION_TYPE_CHANGE_REPORT_COMPARTMENT = "CHANGE_REPORT_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_ARCHIVE_RETRIEVAL"
    OPERATION_TYPE_DELETE_ARCHIVE_RETRIEVAL = "DELETE_ARCHIVE_RETRIEVAL"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_ARCHIVE_RETRIEVAL"
    OPERATION_TYPE_CREATE_ARCHIVE_RETRIEVAL = "CREATE_ARCHIVE_RETRIEVAL"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_ARCHIVE_RETRIEVAL"
    OPERATION_TYPE_UPDATE_ARCHIVE_RETRIEVAL = "UPDATE_ARCHIVE_RETRIEVAL"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_ARCHIVE_RETRIEVAL_COMPARTMENT"
    OPERATION_TYPE_CHANGE_ARCHIVE_RETRIEVAL_COMPARTMENT = "CHANGE_ARCHIVE_RETRIEVAL_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_ALERT"
    OPERATION_TYPE_UPDATE_ALERT = "UPDATE_ALERT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "TARGET_ALERT_POLICY_ASSOCIATION"
    OPERATION_TYPE_TARGET_ALERT_POLICY_ASSOCIATION = "TARGET_ALERT_POLICY_ASSOCIATION"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SENSITIVE_DATA_MODEL"
    OPERATION_TYPE_CREATE_SENSITIVE_DATA_MODEL = "CREATE_SENSITIVE_DATA_MODEL"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_SENSITIVE_DATA_MODEL"
    OPERATION_TYPE_UPDATE_SENSITIVE_DATA_MODEL = "UPDATE_SENSITIVE_DATA_MODEL"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_SENSITIVE_DATA_MODEL"
    OPERATION_TYPE_DELETE_SENSITIVE_DATA_MODEL = "DELETE_SENSITIVE_DATA_MODEL"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPLOAD_SENSITIVE_DATA_MODEL"
    OPERATION_TYPE_UPLOAD_SENSITIVE_DATA_MODEL = "UPLOAD_SENSITIVE_DATA_MODEL"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "GENERATE_SENSITIVE_DATA_MODEL_FOR_DOWNLOAD"
    OPERATION_TYPE_GENERATE_SENSITIVE_DATA_MODEL_FOR_DOWNLOAD = "GENERATE_SENSITIVE_DATA_MODEL_FOR_DOWNLOAD"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SENSITIVE_COLUMN"
    OPERATION_TYPE_CREATE_SENSITIVE_COLUMN = "CREATE_SENSITIVE_COLUMN"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_SENSITIVE_COLUMN"
    OPERATION_TYPE_UPDATE_SENSITIVE_COLUMN = "UPDATE_SENSITIVE_COLUMN"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "PATCH_SENSITIVE_COLUMNS"
    OPERATION_TYPE_PATCH_SENSITIVE_COLUMNS = "PATCH_SENSITIVE_COLUMNS"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_DISCOVERY_JOB"
    OPERATION_TYPE_CREATE_DISCOVERY_JOB = "CREATE_DISCOVERY_JOB"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_DISCOVERY_JOB"
    OPERATION_TYPE_DELETE_DISCOVERY_JOB = "DELETE_DISCOVERY_JOB"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "PATCH_DISCOVERY_JOB_RESULT"
    OPERATION_TYPE_PATCH_DISCOVERY_JOB_RESULT = "PATCH_DISCOVERY_JOB_RESULT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "APPLY_DISCOVERY_JOB_RESULT"
    OPERATION_TYPE_APPLY_DISCOVERY_JOB_RESULT = "APPLY_DISCOVERY_JOB_RESULT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "GENERATE_DISCOVERY_REPORT"
    OPERATION_TYPE_GENERATE_DISCOVERY_REPORT = "GENERATE_DISCOVERY_REPORT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SENSITIVE_TYPE"
    OPERATION_TYPE_CREATE_SENSITIVE_TYPE = "CREATE_SENSITIVE_TYPE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_SENSITIVE_TYPE"
    OPERATION_TYPE_UPDATE_SENSITIVE_TYPE = "UPDATE_SENSITIVE_TYPE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_MASKING_POLICY"
    OPERATION_TYPE_CREATE_MASKING_POLICY = "CREATE_MASKING_POLICY"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_MASKING_POLICY"
    OPERATION_TYPE_UPDATE_MASKING_POLICY = "UPDATE_MASKING_POLICY"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_MASKING_POLICY"
    OPERATION_TYPE_DELETE_MASKING_POLICY = "DELETE_MASKING_POLICY"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPLOAD_MASKING_POLICY"
    OPERATION_TYPE_UPLOAD_MASKING_POLICY = "UPLOAD_MASKING_POLICY"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "GENERATE_MASKING_POLICY_FOR_DOWNLOAD"
    OPERATION_TYPE_GENERATE_MASKING_POLICY_FOR_DOWNLOAD = "GENERATE_MASKING_POLICY_FOR_DOWNLOAD"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_MASKING_COLUMN"
    OPERATION_TYPE_CREATE_MASKING_COLUMN = "CREATE_MASKING_COLUMN"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_MASKING_COLUMN"
    OPERATION_TYPE_UPDATE_MASKING_COLUMN = "UPDATE_MASKING_COLUMN"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "PATCH_MASKING_COLUMNS"
    OPERATION_TYPE_PATCH_MASKING_COLUMNS = "PATCH_MASKING_COLUMNS"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "GENERATE_MASKING_REPORT"
    OPERATION_TYPE_GENERATE_MASKING_REPORT = "GENERATE_MASKING_REPORT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_LIBRARY_MASKING_FORMAT"
    OPERATION_TYPE_CREATE_LIBRARY_MASKING_FORMAT = "CREATE_LIBRARY_MASKING_FORMAT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_LIBRARY_MASKING_FORMAT"
    OPERATION_TYPE_UPDATE_LIBRARY_MASKING_FORMAT = "UPDATE_LIBRARY_MASKING_FORMAT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "ADD_COLUMNS_FROM_SDM"
    OPERATION_TYPE_ADD_COLUMNS_FROM_SDM = "ADD_COLUMNS_FROM_SDM"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "MASKING_JOB"
    OPERATION_TYPE_MASKING_JOB = "MASKING_JOB"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SCHEDULE"
    OPERATION_TYPE_CREATE_SCHEDULE = "CREATE_SCHEDULE"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "REMOVE_SCHEDULE_REPORT"
    OPERATION_TYPE_REMOVE_SCHEDULE_REPORT = "REMOVE_SCHEDULE_REPORT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_ALL_ALERT"
    OPERATION_TYPE_UPDATE_ALL_ALERT = "UPDATE_ALL_ALERT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "PATCH_TARGET_ALERT_POLICY_ASSOCIATION"
    OPERATION_TYPE_PATCH_TARGET_ALERT_POLICY_ASSOCIATION = "PATCH_TARGET_ALERT_POLICY_ASSOCIATION"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "SUSPENDING"
    STATUS_SUSPENDING = "SUSPENDING"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "SUSPENDED"
    STATUS_SUSPENDED = "SUSPENDED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequestSummary.
            Allowed values for this property are: "ENABLE_DATA_SAFE_CONFIGURATION", "CREATE_PRIVATE_ENDPOINT", "UPDATE_PRIVATE_ENDPOINT", "DELETE_PRIVATE_ENDPOINT", "CHANGE_PRIVATE_ENDPOINT_COMPARTMENT", "CREATE_ONPREM_CONNECTOR", "UPDATE_ONPREM_CONNECTOR", "DELETE_ONPREM_CONNECTOR", "UPDATE_ONPREM_CONNECTOR_WALLET", "CHANGE_ONPREM_CONNECTOR_COMPARTMENT", "PROVISION_POLICY", "RETRIEVE_POLICY", "UPDATE_POLICY", "CHANGE_POLICY_COMPARTMENT", "CREATE_TARGET_DATABASE", "UPDATE_TARGET_DATABASE", "ACTIVATE_TARGET_DATABASE", "DEACTIVATE_TARGET_DATABASE", "DELETE_TARGET_DATABASE", "CHANGE_TARGET_DATABASE_COMPARTMENT", "CREATE_USER_ASSESSMENT", "ASSESS_USER_ASSESSMENT", "CREATE_SNAPSHOT_USER_ASSESSMENT", "CREATE_SCHEDULE_USER_ASSESSMENT", "COMPARE_WITH_BASELINE_USER_ASSESSMENT", "DELETE_USER_ASSESSMENT", "UPDATE_USER_ASSESSMENT", "CHANGE_USER_ASSESSMENT_COMPARTMENT", "SET_USER_ASSESSMENT_BASELINE", "UNSET_USER_ASSESSMENT_BASELINE", "GENERATE_USER_ASSESSMENT_REPORT", "CREATE_SECURITY_ASSESSMENT", "CREATE_SECURITY_ASSESSMENT_NOW", "ASSESS_SECURITY_ASSESSMENT", "CREATE_SNAPSHOT_SECURITY_ASSESSMENT", "CREATE_SCHEDULE_SECURITY_ASSESSMENT", "COMPARE_WITH_BASELINE_SECURITY_ASSESSMENT", "DELETE_SECURITY_ASSESSMENT", "UPDATE_SECURITY_ASSESSMENT", "CHANGE_SECURITY_ASSESSMENT_COMPARTMENT", "SET_SECURITY_ASSESSMENT_BASELINE", "UNSET_SECURITY_ASSESSMENT_BASELINE", "GENERATE_SECURITY_ASSESSMENT_REPORT", "CALCULATE_VOLUME", "CALCULATE_COLLECTED_VOLUME", "AUDIT_TRAIL", "DELETE_AUDIT_TRAIL", "DISCOVER_AUDIT_TRAILS", "UPDATE_AUDIT_TRAIL", "UPDATE_AUDIT_PROFILE", "AUDIT_CHANGE_COMPARTMENT", "CREATE_REPORT_DEFINITION", "UPDATE_REPORT_DEFINITION", "CHANGE_REPORT_DEFINITION_COMPARTMENT", "DELETE_REPORT_DEFINITION", "GENERATE_REPORT", "CHANGE_REPORT_COMPARTMENT", "DELETE_ARCHIVE_RETRIEVAL", "CREATE_ARCHIVE_RETRIEVAL", "UPDATE_ARCHIVE_RETRIEVAL", "CHANGE_ARCHIVE_RETRIEVAL_COMPARTMENT", "UPDATE_ALERT", "TARGET_ALERT_POLICY_ASSOCIATION", "CREATE_SENSITIVE_DATA_MODEL", "UPDATE_SENSITIVE_DATA_MODEL", "DELETE_SENSITIVE_DATA_MODEL", "UPLOAD_SENSITIVE_DATA_MODEL", "GENERATE_SENSITIVE_DATA_MODEL_FOR_DOWNLOAD", "CREATE_SENSITIVE_COLUMN", "UPDATE_SENSITIVE_COLUMN", "PATCH_SENSITIVE_COLUMNS", "CREATE_DISCOVERY_JOB", "DELETE_DISCOVERY_JOB", "PATCH_DISCOVERY_JOB_RESULT", "APPLY_DISCOVERY_JOB_RESULT", "GENERATE_DISCOVERY_REPORT", "CREATE_SENSITIVE_TYPE", "UPDATE_SENSITIVE_TYPE", "CREATE_MASKING_POLICY", "UPDATE_MASKING_POLICY", "DELETE_MASKING_POLICY", "UPLOAD_MASKING_POLICY", "GENERATE_MASKING_POLICY_FOR_DOWNLOAD", "CREATE_MASKING_COLUMN", "UPDATE_MASKING_COLUMN", "PATCH_MASKING_COLUMNS", "GENERATE_MASKING_REPORT", "CREATE_LIBRARY_MASKING_FORMAT", "UPDATE_LIBRARY_MASKING_FORMAT", "ADD_COLUMNS_FROM_SDM", "MASKING_JOB", "CREATE_SCHEDULE", "REMOVE_SCHEDULE_REPORT", "UPDATE_ALL_ALERT", "PATCH_TARGET_ALERT_POLICY_ASSOCIATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this WorkRequestSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "SUSPENDING", "SUSPENDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param id:
            The value to assign to the id property of this WorkRequestSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequestSummary.
        :type compartment_id: str

        :param resources:
            The value to assign to the resources property of this WorkRequestSummary.
        :type resources: list[oci.data_safe.models.WorkRequestResource]

        :param percent_complete:
            The value to assign to the percent_complete property of this WorkRequestSummary.
        :type percent_complete: float

        :param time_accepted:
            The value to assign to the time_accepted property of this WorkRequestSummary.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this WorkRequestSummary.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this WorkRequestSummary.
        :type time_finished: datetime

        """
        self.swagger_types = {
            'operation_type': 'str',
            'status': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'resources': 'list[WorkRequestResource]',
            'percent_complete': 'float',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime'
        }

        self.attribute_map = {
            'operation_type': 'operationType',
            'status': 'status',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'resources': 'resources',
            'percent_complete': 'percentComplete',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished'
        }

        self._operation_type = None
        self._status = None
        self._id = None
        self._compartment_id = None
        self._resources = None
        self._percent_complete = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this WorkRequestSummary.
        The asynchronous operation tracked by this work request.

        Allowed values for this property are: "ENABLE_DATA_SAFE_CONFIGURATION", "CREATE_PRIVATE_ENDPOINT", "UPDATE_PRIVATE_ENDPOINT", "DELETE_PRIVATE_ENDPOINT", "CHANGE_PRIVATE_ENDPOINT_COMPARTMENT", "CREATE_ONPREM_CONNECTOR", "UPDATE_ONPREM_CONNECTOR", "DELETE_ONPREM_CONNECTOR", "UPDATE_ONPREM_CONNECTOR_WALLET", "CHANGE_ONPREM_CONNECTOR_COMPARTMENT", "PROVISION_POLICY", "RETRIEVE_POLICY", "UPDATE_POLICY", "CHANGE_POLICY_COMPARTMENT", "CREATE_TARGET_DATABASE", "UPDATE_TARGET_DATABASE", "ACTIVATE_TARGET_DATABASE", "DEACTIVATE_TARGET_DATABASE", "DELETE_TARGET_DATABASE", "CHANGE_TARGET_DATABASE_COMPARTMENT", "CREATE_USER_ASSESSMENT", "ASSESS_USER_ASSESSMENT", "CREATE_SNAPSHOT_USER_ASSESSMENT", "CREATE_SCHEDULE_USER_ASSESSMENT", "COMPARE_WITH_BASELINE_USER_ASSESSMENT", "DELETE_USER_ASSESSMENT", "UPDATE_USER_ASSESSMENT", "CHANGE_USER_ASSESSMENT_COMPARTMENT", "SET_USER_ASSESSMENT_BASELINE", "UNSET_USER_ASSESSMENT_BASELINE", "GENERATE_USER_ASSESSMENT_REPORT", "CREATE_SECURITY_ASSESSMENT", "CREATE_SECURITY_ASSESSMENT_NOW", "ASSESS_SECURITY_ASSESSMENT", "CREATE_SNAPSHOT_SECURITY_ASSESSMENT", "CREATE_SCHEDULE_SECURITY_ASSESSMENT", "COMPARE_WITH_BASELINE_SECURITY_ASSESSMENT", "DELETE_SECURITY_ASSESSMENT", "UPDATE_SECURITY_ASSESSMENT", "CHANGE_SECURITY_ASSESSMENT_COMPARTMENT", "SET_SECURITY_ASSESSMENT_BASELINE", "UNSET_SECURITY_ASSESSMENT_BASELINE", "GENERATE_SECURITY_ASSESSMENT_REPORT", "CALCULATE_VOLUME", "CALCULATE_COLLECTED_VOLUME", "AUDIT_TRAIL", "DELETE_AUDIT_TRAIL", "DISCOVER_AUDIT_TRAILS", "UPDATE_AUDIT_TRAIL", "UPDATE_AUDIT_PROFILE", "AUDIT_CHANGE_COMPARTMENT", "CREATE_REPORT_DEFINITION", "UPDATE_REPORT_DEFINITION", "CHANGE_REPORT_DEFINITION_COMPARTMENT", "DELETE_REPORT_DEFINITION", "GENERATE_REPORT", "CHANGE_REPORT_COMPARTMENT", "DELETE_ARCHIVE_RETRIEVAL", "CREATE_ARCHIVE_RETRIEVAL", "UPDATE_ARCHIVE_RETRIEVAL", "CHANGE_ARCHIVE_RETRIEVAL_COMPARTMENT", "UPDATE_ALERT", "TARGET_ALERT_POLICY_ASSOCIATION", "CREATE_SENSITIVE_DATA_MODEL", "UPDATE_SENSITIVE_DATA_MODEL", "DELETE_SENSITIVE_DATA_MODEL", "UPLOAD_SENSITIVE_DATA_MODEL", "GENERATE_SENSITIVE_DATA_MODEL_FOR_DOWNLOAD", "CREATE_SENSITIVE_COLUMN", "UPDATE_SENSITIVE_COLUMN", "PATCH_SENSITIVE_COLUMNS", "CREATE_DISCOVERY_JOB", "DELETE_DISCOVERY_JOB", "PATCH_DISCOVERY_JOB_RESULT", "APPLY_DISCOVERY_JOB_RESULT", "GENERATE_DISCOVERY_REPORT", "CREATE_SENSITIVE_TYPE", "UPDATE_SENSITIVE_TYPE", "CREATE_MASKING_POLICY", "UPDATE_MASKING_POLICY", "DELETE_MASKING_POLICY", "UPLOAD_MASKING_POLICY", "GENERATE_MASKING_POLICY_FOR_DOWNLOAD", "CREATE_MASKING_COLUMN", "UPDATE_MASKING_COLUMN", "PATCH_MASKING_COLUMNS", "GENERATE_MASKING_REPORT", "CREATE_LIBRARY_MASKING_FORMAT", "UPDATE_LIBRARY_MASKING_FORMAT", "ADD_COLUMNS_FROM_SDM", "MASKING_JOB", "CREATE_SCHEDULE", "REMOVE_SCHEDULE_REPORT", "UPDATE_ALL_ALERT", "PATCH_TARGET_ALERT_POLICY_ASSOCIATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this WorkRequestSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequestSummary.
        The asynchronous operation tracked by this work request.


        :param operation_type: The operation_type of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["ENABLE_DATA_SAFE_CONFIGURATION", "CREATE_PRIVATE_ENDPOINT", "UPDATE_PRIVATE_ENDPOINT", "DELETE_PRIVATE_ENDPOINT", "CHANGE_PRIVATE_ENDPOINT_COMPARTMENT", "CREATE_ONPREM_CONNECTOR", "UPDATE_ONPREM_CONNECTOR", "DELETE_ONPREM_CONNECTOR", "UPDATE_ONPREM_CONNECTOR_WALLET", "CHANGE_ONPREM_CONNECTOR_COMPARTMENT", "PROVISION_POLICY", "RETRIEVE_POLICY", "UPDATE_POLICY", "CHANGE_POLICY_COMPARTMENT", "CREATE_TARGET_DATABASE", "UPDATE_TARGET_DATABASE", "ACTIVATE_TARGET_DATABASE", "DEACTIVATE_TARGET_DATABASE", "DELETE_TARGET_DATABASE", "CHANGE_TARGET_DATABASE_COMPARTMENT", "CREATE_USER_ASSESSMENT", "ASSESS_USER_ASSESSMENT", "CREATE_SNAPSHOT_USER_ASSESSMENT", "CREATE_SCHEDULE_USER_ASSESSMENT", "COMPARE_WITH_BASELINE_USER_ASSESSMENT", "DELETE_USER_ASSESSMENT", "UPDATE_USER_ASSESSMENT", "CHANGE_USER_ASSESSMENT_COMPARTMENT", "SET_USER_ASSESSMENT_BASELINE", "UNSET_USER_ASSESSMENT_BASELINE", "GENERATE_USER_ASSESSMENT_REPORT", "CREATE_SECURITY_ASSESSMENT", "CREATE_SECURITY_ASSESSMENT_NOW", "ASSESS_SECURITY_ASSESSMENT", "CREATE_SNAPSHOT_SECURITY_ASSESSMENT", "CREATE_SCHEDULE_SECURITY_ASSESSMENT", "COMPARE_WITH_BASELINE_SECURITY_ASSESSMENT", "DELETE_SECURITY_ASSESSMENT", "UPDATE_SECURITY_ASSESSMENT", "CHANGE_SECURITY_ASSESSMENT_COMPARTMENT", "SET_SECURITY_ASSESSMENT_BASELINE", "UNSET_SECURITY_ASSESSMENT_BASELINE", "GENERATE_SECURITY_ASSESSMENT_REPORT", "CALCULATE_VOLUME", "CALCULATE_COLLECTED_VOLUME", "AUDIT_TRAIL", "DELETE_AUDIT_TRAIL", "DISCOVER_AUDIT_TRAILS", "UPDATE_AUDIT_TRAIL", "UPDATE_AUDIT_PROFILE", "AUDIT_CHANGE_COMPARTMENT", "CREATE_REPORT_DEFINITION", "UPDATE_REPORT_DEFINITION", "CHANGE_REPORT_DEFINITION_COMPARTMENT", "DELETE_REPORT_DEFINITION", "GENERATE_REPORT", "CHANGE_REPORT_COMPARTMENT", "DELETE_ARCHIVE_RETRIEVAL", "CREATE_ARCHIVE_RETRIEVAL", "UPDATE_ARCHIVE_RETRIEVAL", "CHANGE_ARCHIVE_RETRIEVAL_COMPARTMENT", "UPDATE_ALERT", "TARGET_ALERT_POLICY_ASSOCIATION", "CREATE_SENSITIVE_DATA_MODEL", "UPDATE_SENSITIVE_DATA_MODEL", "DELETE_SENSITIVE_DATA_MODEL", "UPLOAD_SENSITIVE_DATA_MODEL", "GENERATE_SENSITIVE_DATA_MODEL_FOR_DOWNLOAD", "CREATE_SENSITIVE_COLUMN", "UPDATE_SENSITIVE_COLUMN", "PATCH_SENSITIVE_COLUMNS", "CREATE_DISCOVERY_JOB", "DELETE_DISCOVERY_JOB", "PATCH_DISCOVERY_JOB_RESULT", "APPLY_DISCOVERY_JOB_RESULT", "GENERATE_DISCOVERY_REPORT", "CREATE_SENSITIVE_TYPE", "UPDATE_SENSITIVE_TYPE", "CREATE_MASKING_POLICY", "UPDATE_MASKING_POLICY", "DELETE_MASKING_POLICY", "UPLOAD_MASKING_POLICY", "GENERATE_MASKING_POLICY_FOR_DOWNLOAD", "CREATE_MASKING_COLUMN", "UPDATE_MASKING_COLUMN", "PATCH_MASKING_COLUMNS", "GENERATE_MASKING_REPORT", "CREATE_LIBRARY_MASKING_FORMAT", "UPDATE_LIBRARY_MASKING_FORMAT", "ADD_COLUMNS_FROM_SDM", "MASKING_JOB", "CREATE_SCHEDULE", "REMOVE_SCHEDULE_REPORT", "UPDATE_ALL_ALERT", "PATCH_TARGET_ALERT_POLICY_ASSOCIATION"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequestSummary.
        The current status of the work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "SUSPENDING", "SUSPENDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequestSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequestSummary.
        The current status of the work request.


        :param status: The status of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "SUSPENDING", "SUSPENDED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequestSummary.
        The OCID of the work request.


        :return: The id of this WorkRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequestSummary.
        The OCID of the work request.


        :param id: The id of this WorkRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequestSummary.
        The OCID of the compartment that contains the work request.


        :return: The compartment_id of this WorkRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequestSummary.
        The OCID of the compartment that contains the work request.


        :param compartment_id: The compartment_id of this WorkRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this WorkRequestSummary.
        The resources that are affected by the work request.


        :return: The resources of this WorkRequestSummary.
        :rtype: list[oci.data_safe.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequestSummary.
        The resources that are affected by the work request.


        :param resources: The resources of this WorkRequestSummary.
        :type: list[oci.data_safe.models.WorkRequestResource]
        """
        self._resources = resources

    @property
    def percent_complete(self):
        """
        **[Required]** Gets the percent_complete of this WorkRequestSummary.
        Progress of the work request in percentage.


        :return: The percent_complete of this WorkRequestSummary.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequestSummary.
        Progress of the work request in percentage.


        :param percent_complete: The percent_complete of this WorkRequestSummary.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this WorkRequestSummary.
        The date and time the work request was accepted, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_accepted of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequestSummary.
        The date and time the work request was accepted, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_accepted: The time_accepted of this WorkRequestSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this WorkRequestSummary.
        The date and time the work request transitioned from ACCEPTED to IN_PROGRESS, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_started of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequestSummary.
        The date and time the work request transitioned from ACCEPTED to IN_PROGRESS, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_started: The time_started of this WorkRequestSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequestSummary.
        The date and time the work request reached a terminal state, either FAILED or SUCCEEDED, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_finished of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequestSummary.
        The date and time the work request reached a terminal state, either FAILED or SUCCEEDED, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_finished: The time_finished of this WorkRequestSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
