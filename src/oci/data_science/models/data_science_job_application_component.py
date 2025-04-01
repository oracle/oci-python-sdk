# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .application_component import ApplicationComponent
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataScienceJobApplicationComponent(ApplicationComponent):
    """
    Data Science Job application component
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataScienceJobApplicationComponent object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.DataScienceJobApplicationComponent.type` attribute
        of this class is ``DATA_SCIENCE_JOB`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DataScienceJobApplicationComponent.
            Allowed values for this property are: "DATA_SCIENCE_PIPELINE", "DATA_SCIENCE_JOB", "DATA_SCIENCE_MODEL", "DATA_FLOW_APPLICATION", "GENERIC_OCI_RESOURCE"
        :type type: str

        :param name:
            The value to assign to the name property of this DataScienceJobApplicationComponent.
        :type name: str

        :param component_name:
            The value to assign to the component_name property of this DataScienceJobApplicationComponent.
        :type component_name: str

        :param job_id:
            The value to assign to the job_id property of this DataScienceJobApplicationComponent.
        :type job_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'component_name': 'str',
            'job_id': 'str'
        }
        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'component_name': 'componentName',
            'job_id': 'jobId'
        }
        self._type = None
        self._name = None
        self._component_name = None
        self._job_id = None
        self._type = 'DATA_SCIENCE_JOB'

    @property
    def job_id(self):
        """
        **[Required]** Gets the job_id of this DataScienceJobApplicationComponent.
        OCID of Data Science Job


        :return: The job_id of this DataScienceJobApplicationComponent.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this DataScienceJobApplicationComponent.
        OCID of Data Science Job


        :param job_id: The job_id of this DataScienceJobApplicationComponent.
        :type: str
        """
        self._job_id = job_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
