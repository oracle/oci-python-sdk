# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .wait_criteria import WaitCriteria
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AbsoluteWaitCriteria(WaitCriteria):
    """
    Specifies the absolute wait criteria. You can specify fixed length of wait duration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AbsoluteWaitCriteria object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.AbsoluteWaitCriteria.wait_type` attribute
        of this class is ``ABSOLUTE_WAIT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param wait_type:
            The value to assign to the wait_type property of this AbsoluteWaitCriteria.
            Allowed values for this property are: "ABSOLUTE_WAIT"
        :type wait_type: str

        :param wait_duration:
            The value to assign to the wait_duration property of this AbsoluteWaitCriteria.
        :type wait_duration: str

        """
        self.swagger_types = {
            'wait_type': 'str',
            'wait_duration': 'str'
        }

        self.attribute_map = {
            'wait_type': 'waitType',
            'wait_duration': 'waitDuration'
        }

        self._wait_type = None
        self._wait_duration = None
        self._wait_type = 'ABSOLUTE_WAIT'

    @property
    def wait_duration(self):
        """
        **[Required]** Gets the wait_duration of this AbsoluteWaitCriteria.
        The absolute wait duration. An ISO 8601 formatted duration string. Minimum waitDuration should be 5 seconds. Maximum waitDuration can be up to 2 days.


        :return: The wait_duration of this AbsoluteWaitCriteria.
        :rtype: str
        """
        return self._wait_duration

    @wait_duration.setter
    def wait_duration(self, wait_duration):
        """
        Sets the wait_duration of this AbsoluteWaitCriteria.
        The absolute wait duration. An ISO 8601 formatted duration string. Minimum waitDuration should be 5 seconds. Maximum waitDuration can be up to 2 days.


        :param wait_duration: The wait_duration of this AbsoluteWaitCriteria.
        :type: str
        """
        self._wait_duration = wait_duration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
