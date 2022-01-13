# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnnotationAnalyticsAggregation(object):
    """
    Aggregation entities are required by the API consistency guidelines for API Consistency Guidelines#AnalyticsAPIs.  These are used to summarize annotations for a given dataset and will be used to populate UI elements.  Aggregations need to have the fields that identify the exact scope that they're summarizing.  Any filters applied to the list API, have to show up in the aggregation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnnotationAnalyticsAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param count:
            The value to assign to the count property of this AnnotationAnalyticsAggregation.
        :type count: float

        :param dataset_id:
            The value to assign to the dataset_id property of this AnnotationAnalyticsAggregation.
        :type dataset_id: str

        :param dimensions:
            The value to assign to the dimensions property of this AnnotationAnalyticsAggregation.
        :type dimensions: oci.data_labeling_service_dataplane.models.AnnotationAggregationDimensions

        :param updated_by:
            The value to assign to the updated_by property of this AnnotationAnalyticsAggregation.
        :type updated_by: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AnnotationAnalyticsAggregation.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AnnotationAnalyticsAggregation.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'count': 'float',
            'dataset_id': 'str',
            'dimensions': 'AnnotationAggregationDimensions',
            'updated_by': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'count': 'count',
            'dataset_id': 'datasetId',
            'dimensions': 'dimensions',
            'updated_by': 'updatedBy',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState'
        }

        self._count = None
        self._dataset_id = None
        self._dimensions = None
        self._updated_by = None
        self._compartment_id = None
        self._lifecycle_state = None

    @property
    def count(self):
        """
        **[Required]** Gets the count of this AnnotationAnalyticsAggregation.
        The count of the matching results.


        :return: The count of this AnnotationAnalyticsAggregation.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this AnnotationAnalyticsAggregation.
        The count of the matching results.


        :param count: The count of this AnnotationAnalyticsAggregation.
        :type: float
        """
        self._count = count

    @property
    def dataset_id(self):
        """
        **[Required]** Gets the dataset_id of this AnnotationAnalyticsAggregation.
        The OCID of the dataset the annotations belong to.


        :return: The dataset_id of this AnnotationAnalyticsAggregation.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """
        Sets the dataset_id of this AnnotationAnalyticsAggregation.
        The OCID of the dataset the annotations belong to.


        :param dataset_id: The dataset_id of this AnnotationAnalyticsAggregation.
        :type: str
        """
        self._dataset_id = dataset_id

    @property
    def dimensions(self):
        """
        Gets the dimensions of this AnnotationAnalyticsAggregation.

        :return: The dimensions of this AnnotationAnalyticsAggregation.
        :rtype: oci.data_labeling_service_dataplane.models.AnnotationAggregationDimensions
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this AnnotationAnalyticsAggregation.

        :param dimensions: The dimensions of this AnnotationAnalyticsAggregation.
        :type: oci.data_labeling_service_dataplane.models.AnnotationAggregationDimensions
        """
        self._dimensions = dimensions

    @property
    def updated_by(self):
        """
        Gets the updated_by of this AnnotationAnalyticsAggregation.
        The OCID of the principal which updated the annotation.


        :return: The updated_by of this AnnotationAnalyticsAggregation.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """
        Sets the updated_by of this AnnotationAnalyticsAggregation.
        The OCID of the principal which updated the annotation.


        :param updated_by: The updated_by of this AnnotationAnalyticsAggregation.
        :type: str
        """
        self._updated_by = updated_by

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AnnotationAnalyticsAggregation.
        The OCID of the compartment containing the annotations.


        :return: The compartment_id of this AnnotationAnalyticsAggregation.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AnnotationAnalyticsAggregation.
        The OCID of the compartment containing the annotations.


        :param compartment_id: The compartment_id of this AnnotationAnalyticsAggregation.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AnnotationAnalyticsAggregation.
        Describes the lifecycle state.


        :return: The lifecycle_state of this AnnotationAnalyticsAggregation.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AnnotationAnalyticsAggregation.
        Describes the lifecycle state.


        :param lifecycle_state: The lifecycle_state of this AnnotationAnalyticsAggregation.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
