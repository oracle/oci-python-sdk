# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobConfigurationDetails(object):
    """
    The job configuration details
    """

    #: A constant which can be used with the job_type property of a JobConfigurationDetails.
    #: This constant has a value of "DEFAULT"
    JOB_TYPE_DEFAULT = "DEFAULT"

    def __init__(self, **kwargs):
        """
        Initializes a new JobConfigurationDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_science.models.DefaultJobConfigurationDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param job_type:
            The value to assign to the job_type property of this JobConfigurationDetails.
            Allowed values for this property are: "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type job_type: str

        """
        self.swagger_types = {
            'job_type': 'str'
        }

        self.attribute_map = {
            'job_type': 'jobType'
        }

        self._job_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['jobType']

        if type == 'DEFAULT':
            return 'DefaultJobConfigurationDetails'
        else:
            return 'JobConfigurationDetails'

    @property
    def job_type(self):
        """
        **[Required]** Gets the job_type of this JobConfigurationDetails.
        The type of job.

        Allowed values for this property are: "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The job_type of this JobConfigurationDetails.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """
        Sets the job_type of this JobConfigurationDetails.
        The type of job.


        :param job_type: The job_type of this JobConfigurationDetails.
        :type: str
        """
        allowed_values = ["DEFAULT"]
        if not value_allowed_none_or_none_sentinel(job_type, allowed_values):
            job_type = 'UNKNOWN_ENUM_VALUE'
        self._job_type = job_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
