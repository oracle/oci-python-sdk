# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngestStreamDistributionChannelResult(object):
    """
    The Ingest Workflow Job information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IngestStreamDistributionChannelResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param media_workflow_job_id:
            The value to assign to the media_workflow_job_id property of this IngestStreamDistributionChannelResult.
        :type media_workflow_job_id: str

        """
        self.swagger_types = {
            'media_workflow_job_id': 'str'
        }

        self.attribute_map = {
            'media_workflow_job_id': 'mediaWorkflowJobId'
        }

        self._media_workflow_job_id = None

    @property
    def media_workflow_job_id(self):
        """
        **[Required]** Gets the media_workflow_job_id of this IngestStreamDistributionChannelResult.
        Identifier of the Ingest Workflow Job created.


        :return: The media_workflow_job_id of this IngestStreamDistributionChannelResult.
        :rtype: str
        """
        return self._media_workflow_job_id

    @media_workflow_job_id.setter
    def media_workflow_job_id(self, media_workflow_job_id):
        """
        Sets the media_workflow_job_id of this IngestStreamDistributionChannelResult.
        Identifier of the Ingest Workflow Job created.


        :param media_workflow_job_id: The media_workflow_job_id of this IngestStreamDistributionChannelResult.
        :type: str
        """
        self._media_workflow_job_id = media_workflow_job_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
