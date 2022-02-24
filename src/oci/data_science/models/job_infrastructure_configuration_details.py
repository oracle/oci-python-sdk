# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobInfrastructureConfigurationDetails(object):
    """
    The job infrastructure configuration details (shape, block storage, etc.)
    """

    #: A constant which can be used with the job_infrastructure_type property of a JobInfrastructureConfigurationDetails.
    #: This constant has a value of "STANDALONE"
    JOB_INFRASTRUCTURE_TYPE_STANDALONE = "STANDALONE"

    #: A constant which can be used with the job_infrastructure_type property of a JobInfrastructureConfigurationDetails.
    #: This constant has a value of "ME_STANDALONE"
    JOB_INFRASTRUCTURE_TYPE_ME_STANDALONE = "ME_STANDALONE"

    def __init__(self, **kwargs):
        """
        Initializes a new JobInfrastructureConfigurationDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_science.models.ManagedEgressStandaloneJobInfrastructureConfigurationDetails`
        * :class:`~oci.data_science.models.StandaloneJobInfrastructureConfigurationDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param job_infrastructure_type:
            The value to assign to the job_infrastructure_type property of this JobInfrastructureConfigurationDetails.
            Allowed values for this property are: "STANDALONE", "ME_STANDALONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type job_infrastructure_type: str

        """
        self.swagger_types = {
            'job_infrastructure_type': 'str'
        }

        self.attribute_map = {
            'job_infrastructure_type': 'jobInfrastructureType'
        }

        self._job_infrastructure_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['jobInfrastructureType']

        if type == 'ME_STANDALONE':
            return 'ManagedEgressStandaloneJobInfrastructureConfigurationDetails'

        if type == 'STANDALONE':
            return 'StandaloneJobInfrastructureConfigurationDetails'
        else:
            return 'JobInfrastructureConfigurationDetails'

    @property
    def job_infrastructure_type(self):
        """
        **[Required]** Gets the job_infrastructure_type of this JobInfrastructureConfigurationDetails.
        The infrastructure type used for job run.

        Allowed values for this property are: "STANDALONE", "ME_STANDALONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The job_infrastructure_type of this JobInfrastructureConfigurationDetails.
        :rtype: str
        """
        return self._job_infrastructure_type

    @job_infrastructure_type.setter
    def job_infrastructure_type(self, job_infrastructure_type):
        """
        Sets the job_infrastructure_type of this JobInfrastructureConfigurationDetails.
        The infrastructure type used for job run.


        :param job_infrastructure_type: The job_infrastructure_type of this JobInfrastructureConfigurationDetails.
        :type: str
        """
        allowed_values = ["STANDALONE", "ME_STANDALONE"]
        if not value_allowed_none_or_none_sentinel(job_infrastructure_type, allowed_values):
            job_infrastructure_type = 'UNKNOWN_ENUM_VALUE'
        self._job_infrastructure_type = job_infrastructure_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
