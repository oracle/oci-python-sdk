# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplyJobPlanResolution(object):
    """
    Deprecated. Use the property `executionPlanStrategy` in `jobOperationDetails` instead.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApplyJobPlanResolution object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plan_job_id:
            The value to assign to the plan_job_id property of this ApplyJobPlanResolution.
        :type plan_job_id: str

        :param is_use_latest_job_id:
            The value to assign to the is_use_latest_job_id property of this ApplyJobPlanResolution.
        :type is_use_latest_job_id: bool

        :param is_auto_approved:
            The value to assign to the is_auto_approved property of this ApplyJobPlanResolution.
        :type is_auto_approved: bool

        """
        self.swagger_types = {
            'plan_job_id': 'str',
            'is_use_latest_job_id': 'bool',
            'is_auto_approved': 'bool'
        }

        self.attribute_map = {
            'plan_job_id': 'planJobId',
            'is_use_latest_job_id': 'isUseLatestJobId',
            'is_auto_approved': 'isAutoApproved'
        }

        self._plan_job_id = None
        self._is_use_latest_job_id = None
        self._is_auto_approved = None

    @property
    def plan_job_id(self):
        """
        Gets the plan_job_id of this ApplyJobPlanResolution.
        The `OCID`__ that specifies the most recently executed plan job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The plan_job_id of this ApplyJobPlanResolution.
        :rtype: str
        """
        return self._plan_job_id

    @plan_job_id.setter
    def plan_job_id(self, plan_job_id):
        """
        Sets the plan_job_id of this ApplyJobPlanResolution.
        The `OCID`__ that specifies the most recently executed plan job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param plan_job_id: The plan_job_id of this ApplyJobPlanResolution.
        :type: str
        """
        self._plan_job_id = plan_job_id

    @property
    def is_use_latest_job_id(self):
        """
        Gets the is_use_latest_job_id of this ApplyJobPlanResolution.
        Specifies whether to use the `OCID`__ of the most recently run plan job.
        `True` if using the latest job `OCID`__. Must be a plan job that completed successfully.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The is_use_latest_job_id of this ApplyJobPlanResolution.
        :rtype: bool
        """
        return self._is_use_latest_job_id

    @is_use_latest_job_id.setter
    def is_use_latest_job_id(self, is_use_latest_job_id):
        """
        Sets the is_use_latest_job_id of this ApplyJobPlanResolution.
        Specifies whether to use the `OCID`__ of the most recently run plan job.
        `True` if using the latest job `OCID`__. Must be a plan job that completed successfully.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param is_use_latest_job_id: The is_use_latest_job_id of this ApplyJobPlanResolution.
        :type: bool
        """
        self._is_use_latest_job_id = is_use_latest_job_id

    @property
    def is_auto_approved(self):
        """
        Gets the is_auto_approved of this ApplyJobPlanResolution.
        Specifies whether to use the configuration directly, without reference to a Plan job.
        `True` if using the configuration directly. Note that it is not necessary
        for a Plan job to have run successfully.


        :return: The is_auto_approved of this ApplyJobPlanResolution.
        :rtype: bool
        """
        return self._is_auto_approved

    @is_auto_approved.setter
    def is_auto_approved(self, is_auto_approved):
        """
        Sets the is_auto_approved of this ApplyJobPlanResolution.
        Specifies whether to use the configuration directly, without reference to a Plan job.
        `True` if using the configuration directly. Note that it is not necessary
        for a Plan job to have run successfully.


        :param is_auto_approved: The is_auto_approved of this ApplyJobPlanResolution.
        :type: bool
        """
        self._is_auto_approved = is_auto_approved

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
