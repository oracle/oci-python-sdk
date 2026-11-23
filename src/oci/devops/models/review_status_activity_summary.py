# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.

from .pull_request_activity_summary import PullRequestActivitySummary
from oci.decorators import init_model_state_from_kwargs
from oci.util import formatted_flat_dict, value_allowed_none_or_none_sentinel


@init_model_state_from_kwargs
class ReviewStatusActivitySummary(PullRequestActivitySummary):
    """Activity describing a pull request review-status change."""

    STATUS_DRAFT = "DRAFT"

    def __init__(self, **kwargs):
        self.swagger_types = {
            'id': 'str', 'principal': 'PrincipalDetails', 'pull_request_id': 'str',
            'time_occurred': 'datetime', 'activity_type': 'str', 'status': 'str'
        }
        self.attribute_map = {
            'id': 'id', 'principal': 'principal', 'pull_request_id': 'pullRequestId',
            'time_occurred': 'timeOccurred', 'activity_type': 'activityType', 'status': 'status'
        }
        self._id = self._principal = self._pull_request_id = self._time_occurred = None
        self._activity_type = 'REVIEW_STATUS'
        self._status = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if not value_allowed_none_or_none_sentinel(status, ["DRAFT"]):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)
