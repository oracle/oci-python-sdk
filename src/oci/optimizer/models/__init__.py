# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .action import Action
from .bulk_apply_recommendations_details import BulkApplyRecommendationsDetails
from .category import Category
from .category_collection import CategoryCollection
from .category_summary import CategorySummary
from .create_profile_details import CreateProfileDetails
from .enrollment_status import EnrollmentStatus
from .enrollment_status_collection import EnrollmentStatusCollection
from .enrollment_status_summary import EnrollmentStatusSummary
from .history_collection import HistoryCollection
from .history_summary import HistorySummary
from .level_configuration import LevelConfiguration
from .levels_configuration import LevelsConfiguration
from .profile import Profile
from .profile_collection import ProfileCollection
from .profile_summary import ProfileSummary
from .recommendation import Recommendation
from .recommendation_collection import RecommendationCollection
from .recommendation_count import RecommendationCount
from .recommendation_summary import RecommendationSummary
from .resource_action import ResourceAction
from .resource_action_collection import ResourceActionCollection
from .resource_action_summary import ResourceActionSummary
from .resource_count import ResourceCount
from .supported_level import SupportedLevel
from .supported_levels import SupportedLevels
from .update_enrollment_status_details import UpdateEnrollmentStatusDetails
from .update_profile_details import UpdateProfileDetails
from .update_recommendation_details import UpdateRecommendationDetails
from .update_resource_action_details import UpdateResourceActionDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource

# Maps type names to classes for optimizer services.
optimizer_type_mapping = {
    "Action": Action,
    "BulkApplyRecommendationsDetails": BulkApplyRecommendationsDetails,
    "Category": Category,
    "CategoryCollection": CategoryCollection,
    "CategorySummary": CategorySummary,
    "CreateProfileDetails": CreateProfileDetails,
    "EnrollmentStatus": EnrollmentStatus,
    "EnrollmentStatusCollection": EnrollmentStatusCollection,
    "EnrollmentStatusSummary": EnrollmentStatusSummary,
    "HistoryCollection": HistoryCollection,
    "HistorySummary": HistorySummary,
    "LevelConfiguration": LevelConfiguration,
    "LevelsConfiguration": LevelsConfiguration,
    "Profile": Profile,
    "ProfileCollection": ProfileCollection,
    "ProfileSummary": ProfileSummary,
    "Recommendation": Recommendation,
    "RecommendationCollection": RecommendationCollection,
    "RecommendationCount": RecommendationCount,
    "RecommendationSummary": RecommendationSummary,
    "ResourceAction": ResourceAction,
    "ResourceActionCollection": ResourceActionCollection,
    "ResourceActionSummary": ResourceActionSummary,
    "ResourceCount": ResourceCount,
    "SupportedLevel": SupportedLevel,
    "SupportedLevels": SupportedLevels,
    "UpdateEnrollmentStatusDetails": UpdateEnrollmentStatusDetails,
    "UpdateProfileDetails": UpdateProfileDetails,
    "UpdateRecommendationDetails": UpdateRecommendationDetails,
    "UpdateResourceActionDetails": UpdateResourceActionDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource
}
