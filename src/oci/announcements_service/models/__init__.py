# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .affected_resource import AffectedResource
from .announcement import Announcement
from .announcement_summary import AnnouncementSummary
from .announcement_user_status_details import AnnouncementUserStatusDetails
from .announcements_collection import AnnouncementsCollection
from .base_announcement import BaseAnnouncement

# Maps type names to classes for announcements_service services.
announcements_service_type_mapping = {
    "AffectedResource": AffectedResource,
    "Announcement": Announcement,
    "AnnouncementSummary": AnnouncementSummary,
    "AnnouncementUserStatusDetails": AnnouncementUserStatusDetails,
    "AnnouncementsCollection": AnnouncementsCollection,
    "BaseAnnouncement": BaseAnnouncement
}
