# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplyDiscoveryJobResultsDetails(object):
    """
    Details to apply the discovery results to a sensitive data model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApplyDiscoveryJobResultsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param discovery_job_id:
            The value to assign to the discovery_job_id property of this ApplyDiscoveryJobResultsDetails.
        :type discovery_job_id: str

        """
        self.swagger_types = {
            'discovery_job_id': 'str'
        }

        self.attribute_map = {
            'discovery_job_id': 'discoveryJobId'
        }

        self._discovery_job_id = None

    @property
    def discovery_job_id(self):
        """
        **[Required]** Gets the discovery_job_id of this ApplyDiscoveryJobResultsDetails.
        The OCID of the discovery job.


        :return: The discovery_job_id of this ApplyDiscoveryJobResultsDetails.
        :rtype: str
        """
        return self._discovery_job_id

    @discovery_job_id.setter
    def discovery_job_id(self, discovery_job_id):
        """
        Sets the discovery_job_id of this ApplyDiscoveryJobResultsDetails.
        The OCID of the discovery job.


        :param discovery_job_id: The discovery_job_id of this ApplyDiscoveryJobResultsDetails.
        :type: str
        """
        self._discovery_job_id = discovery_job_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
