# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .affected_resource import AffectedResource
from .announcement import Announcement
from .announcement_summary import AnnouncementSummary
from .announcement_user_status_details import AnnouncementUserStatusDetails
from .announcements_collection import AnnouncementsCollection
from .announcements_preferences import AnnouncementsPreferences
from .announcements_preferences_summary import AnnouncementsPreferencesSummary
from .base_announcement import BaseAnnouncement
from .base_announcements_preferences import BaseAnnouncementsPreferences
from .base_create_announcements_preferences_details import BaseCreateAnnouncementsPreferencesDetails
from .create_announcements_preferences_details import CreateAnnouncementsPreferencesDetails
from .model_property import ModelProperty
from .update_announcements_preferences_details import UpdateAnnouncementsPreferencesDetails

# Maps type names to classes for announcements_service services.
announcements_service_type_mapping = {
    "AffectedResource": AffectedResource,
    "Announcement": Announcement,
    "AnnouncementSummary": AnnouncementSummary,
    "AnnouncementUserStatusDetails": AnnouncementUserStatusDetails,
    "AnnouncementsCollection": AnnouncementsCollection,
    "AnnouncementsPreferences": AnnouncementsPreferences,
    "AnnouncementsPreferencesSummary": AnnouncementsPreferencesSummary,
    "BaseAnnouncement": BaseAnnouncement,
    "BaseAnnouncementsPreferences": BaseAnnouncementsPreferences,
    "BaseCreateAnnouncementsPreferencesDetails": BaseCreateAnnouncementsPreferencesDetails,
    "CreateAnnouncementsPreferencesDetails": CreateAnnouncementsPreferencesDetails,
    "ModelProperty": ModelProperty,
    "UpdateAnnouncementsPreferencesDetails": UpdateAnnouncementsPreferencesDetails
}
