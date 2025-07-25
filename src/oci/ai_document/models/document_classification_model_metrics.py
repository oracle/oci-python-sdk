# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221109

from .model_metrics import ModelMetrics
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DocumentClassificationModelMetrics(ModelMetrics):
    """
    Metrics for Document Classification Model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DocumentClassificationModelMetrics object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_document.models.DocumentClassificationModelMetrics.model_type` attribute
        of this class is ``DOCUMENT_CLASSIFICATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DocumentClassificationModelMetrics.
            Allowed values for this property are: "KEY_VALUE_EXTRACTION", "DOCUMENT_CLASSIFICATION", "PRE_TRAINED_TEXT_EXTRACTION", "PRE_TRAINED_TABLE_EXTRACTION", "PRE_TRAINED_KEY_VALUE_EXTRACTION", "PRE_TRAINED_DOCUMENT_CLASSIFICATION", "PRE_TRAINED_DOCUMENT_ELEMENTS_EXTRACTION"
        :type model_type: str

        :param dataset_summary:
            The value to assign to the dataset_summary property of this DocumentClassificationModelMetrics.
        :type dataset_summary: oci.ai_document.models.DatasetSummary

        :param label_metrics_report:
            The value to assign to the label_metrics_report property of this DocumentClassificationModelMetrics.
        :type label_metrics_report: list[oci.ai_document.models.DocumentClassificationLabelMetricsReport]

        :param overall_metrics_report:
            The value to assign to the overall_metrics_report property of this DocumentClassificationModelMetrics.
        :type overall_metrics_report: oci.ai_document.models.DocumentClassificationOverallMetricsReport

        """
        self.swagger_types = {
            'model_type': 'str',
            'dataset_summary': 'DatasetSummary',
            'label_metrics_report': 'list[DocumentClassificationLabelMetricsReport]',
            'overall_metrics_report': 'DocumentClassificationOverallMetricsReport'
        }
        self.attribute_map = {
            'model_type': 'modelType',
            'dataset_summary': 'datasetSummary',
            'label_metrics_report': 'labelMetricsReport',
            'overall_metrics_report': 'overallMetricsReport'
        }
        self._model_type = None
        self._dataset_summary = None
        self._label_metrics_report = None
        self._overall_metrics_report = None
        self._model_type = 'DOCUMENT_CLASSIFICATION'

    @property
    def label_metrics_report(self):
        """
        **[Required]** Gets the label_metrics_report of this DocumentClassificationModelMetrics.
        List of metrics entries per label.


        :return: The label_metrics_report of this DocumentClassificationModelMetrics.
        :rtype: list[oci.ai_document.models.DocumentClassificationLabelMetricsReport]
        """
        return self._label_metrics_report

    @label_metrics_report.setter
    def label_metrics_report(self, label_metrics_report):
        """
        Sets the label_metrics_report of this DocumentClassificationModelMetrics.
        List of metrics entries per label.


        :param label_metrics_report: The label_metrics_report of this DocumentClassificationModelMetrics.
        :type: list[oci.ai_document.models.DocumentClassificationLabelMetricsReport]
        """
        self._label_metrics_report = label_metrics_report

    @property
    def overall_metrics_report(self):
        """
        **[Required]** Gets the overall_metrics_report of this DocumentClassificationModelMetrics.

        :return: The overall_metrics_report of this DocumentClassificationModelMetrics.
        :rtype: oci.ai_document.models.DocumentClassificationOverallMetricsReport
        """
        return self._overall_metrics_report

    @overall_metrics_report.setter
    def overall_metrics_report(self, overall_metrics_report):
        """
        Sets the overall_metrics_report of this DocumentClassificationModelMetrics.

        :param overall_metrics_report: The overall_metrics_report of this DocumentClassificationModelMetrics.
        :type: oci.ai_document.models.DocumentClassificationOverallMetricsReport
        """
        self._overall_metrics_report = overall_metrics_report

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
