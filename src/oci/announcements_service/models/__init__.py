# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
