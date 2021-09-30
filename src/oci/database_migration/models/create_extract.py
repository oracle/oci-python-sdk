# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateExtract(object):
    """
    Parameters for GoldenGate Extract processes.
    """

    #: A constant which can be used with the performance_profile property of a CreateExtract.
    #: This constant has a value of "LOW"
    PERFORMANCE_PROFILE_LOW = "LOW"

    #: A constant which can be used with the performance_profile property of a CreateExtract.
    #: This constant has a value of "MEDIUM"
    PERFORMANCE_PROFILE_MEDIUM = "MEDIUM"

    #: A constant which can be used with the performance_profile property of a CreateExtract.
    #: This constant has a value of "HIGH"
    PERFORMANCE_PROFILE_HIGH = "HIGH"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateExtract object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param performance_profile:
            The value to assign to the performance_profile property of this CreateExtract.
            Allowed values for this property are: "LOW", "MEDIUM", "HIGH"
        :type performance_profile: str

        :param long_trans_duration:
            The value to assign to the long_trans_duration property of this CreateExtract.
        :type long_trans_duration: int

        """
        self.swagger_types = {
            'performance_profile': 'str',
            'long_trans_duration': 'int'
        }

        self.attribute_map = {
            'performance_profile': 'performanceProfile',
            'long_trans_duration': 'longTransDuration'
        }

        self._performance_profile = None
        self._long_trans_duration = None

    @property
    def performance_profile(self):
        """
        Gets the performance_profile of this CreateExtract.
        Extract performance.

        Allowed values for this property are: "LOW", "MEDIUM", "HIGH"


        :return: The performance_profile of this CreateExtract.
        :rtype: str
        """
        return self._performance_profile

    @performance_profile.setter
    def performance_profile(self, performance_profile):
        """
        Sets the performance_profile of this CreateExtract.
        Extract performance.


        :param performance_profile: The performance_profile of this CreateExtract.
        :type: str
        """
        allowed_values = ["LOW", "MEDIUM", "HIGH"]
        if not value_allowed_none_or_none_sentinel(performance_profile, allowed_values):
            raise ValueError(
                "Invalid value for `performance_profile`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._performance_profile = performance_profile

    @property
    def long_trans_duration(self):
        """
        Gets the long_trans_duration of this CreateExtract.
        Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is long-running.
        If not specified, Extract will not generate a warning on long-running transactions.


        :return: The long_trans_duration of this CreateExtract.
        :rtype: int
        """
        return self._long_trans_duration

    @long_trans_duration.setter
    def long_trans_duration(self, long_trans_duration):
        """
        Sets the long_trans_duration of this CreateExtract.
        Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is long-running.
        If not specified, Extract will not generate a warning on long-running transactions.


        :param long_trans_duration: The long_trans_duration of this CreateExtract.
        :type: int
        """
        self._long_trans_duration = long_trans_duration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
