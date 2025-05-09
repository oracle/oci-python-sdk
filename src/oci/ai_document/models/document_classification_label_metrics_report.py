# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221109


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DocumentClassificationLabelMetricsReport(object):
    """
    Label Metrics report for Document Classification Model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DocumentClassificationLabelMetricsReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label:
            The value to assign to the label property of this DocumentClassificationLabelMetricsReport.
        :type label: str

        :param mean_average_precision:
            The value to assign to the mean_average_precision property of this DocumentClassificationLabelMetricsReport.
        :type mean_average_precision: float

        :param confidence_entries:
            The value to assign to the confidence_entries property of this DocumentClassificationLabelMetricsReport.
        :type confidence_entries: list[oci.ai_document.models.DocumentClassificationConfidenceEntry]

        """
        self.swagger_types = {
            'label': 'str',
            'mean_average_precision': 'float',
            'confidence_entries': 'list[DocumentClassificationConfidenceEntry]'
        }
        self.attribute_map = {
            'label': 'label',
            'mean_average_precision': 'meanAveragePrecision',
            'confidence_entries': 'confidenceEntries'
        }
        self._label = None
        self._mean_average_precision = None
        self._confidence_entries = None

    @property
    def label(self):
        """
        Gets the label of this DocumentClassificationLabelMetricsReport.
        Label name


        :return: The label of this DocumentClassificationLabelMetricsReport.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this DocumentClassificationLabelMetricsReport.
        Label name


        :param label: The label of this DocumentClassificationLabelMetricsReport.
        :type: str
        """
        self._label = label

    @property
    def mean_average_precision(self):
        """
        **[Required]** Gets the mean_average_precision of this DocumentClassificationLabelMetricsReport.
        Mean average precision under different thresholds


        :return: The mean_average_precision of this DocumentClassificationLabelMetricsReport.
        :rtype: float
        """
        return self._mean_average_precision

    @mean_average_precision.setter
    def mean_average_precision(self, mean_average_precision):
        """
        Sets the mean_average_precision of this DocumentClassificationLabelMetricsReport.
        Mean average precision under different thresholds


        :param mean_average_precision: The mean_average_precision of this DocumentClassificationLabelMetricsReport.
        :type: float
        """
        self._mean_average_precision = mean_average_precision

    @property
    def confidence_entries(self):
        """
        **[Required]** Gets the confidence_entries of this DocumentClassificationLabelMetricsReport.
        List of document classification confidence report.


        :return: The confidence_entries of this DocumentClassificationLabelMetricsReport.
        :rtype: list[oci.ai_document.models.DocumentClassificationConfidenceEntry]
        """
        return self._confidence_entries

    @confidence_entries.setter
    def confidence_entries(self, confidence_entries):
        """
        Sets the confidence_entries of this DocumentClassificationLabelMetricsReport.
        List of document classification confidence report.


        :param confidence_entries: The confidence_entries of this DocumentClassificationLabelMetricsReport.
        :type: list[oci.ai_document.models.DocumentClassificationConfidenceEntry]
        """
        self._confidence_entries = confidence_entries

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
