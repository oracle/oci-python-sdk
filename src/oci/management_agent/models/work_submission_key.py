# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkSubmissionKey(object):
    """
    Work Submission Identifier
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkSubmissionKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param work_submission_key:
            The value to assign to the work_submission_key property of this WorkSubmissionKey.
        :type work_submission_key: str

        """
        self.swagger_types = {
            'work_submission_key': 'str'
        }

        self.attribute_map = {
            'work_submission_key': 'workSubmissionKey'
        }

        self._work_submission_key = None

    @property
    def work_submission_key(self):
        """
        **[Required]** Gets the work_submission_key of this WorkSubmissionKey.
        Work Submission Identifier


        :return: The work_submission_key of this WorkSubmissionKey.
        :rtype: str
        """
        return self._work_submission_key

    @work_submission_key.setter
    def work_submission_key(self, work_submission_key):
        """
        Sets the work_submission_key of this WorkSubmissionKey.
        Work Submission Identifier


        :param work_submission_key: The work_submission_key of this WorkSubmissionKey.
        :type: str
        """
        self._work_submission_key = work_submission_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
