# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .evaluation_results import EvaluationResults
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TextClassificationEvaluationResults(EvaluationResults):
    """
    Text Classification model testing and evaluation results
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TextClassificationEvaluationResults object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_language.models.TextClassificationEvaluationResults.model_type` attribute
        of this class is ``TEXT_CLASSIFICATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this TextClassificationEvaluationResults.
        :type model_type: str

        :param metrics:
            The value to assign to the metrics property of this TextClassificationEvaluationResults.
        :type metrics: oci.ai_language.models.TextClassificationModelMetrics

        :param class_metrics:
            The value to assign to the class_metrics property of this TextClassificationEvaluationResults.
        :type class_metrics: list[oci.ai_language.models.ClassMetrics]

        :param confusion_matrix:
            The value to assign to the confusion_matrix property of this TextClassificationEvaluationResults.
        :type confusion_matrix: dict(str, ConfusionMatrixDetails)

        :param labels:
            The value to assign to the labels property of this TextClassificationEvaluationResults.
        :type labels: list[str]

        """
        self.swagger_types = {
            'model_type': 'str',
            'metrics': 'TextClassificationModelMetrics',
            'class_metrics': 'list[ClassMetrics]',
            'confusion_matrix': 'dict(str, ConfusionMatrixDetails)',
            'labels': 'list[str]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'metrics': 'metrics',
            'class_metrics': 'classMetrics',
            'confusion_matrix': 'confusionMatrix',
            'labels': 'labels'
        }

        self._model_type = None
        self._metrics = None
        self._class_metrics = None
        self._confusion_matrix = None
        self._labels = None
        self._model_type = 'TEXT_CLASSIFICATION'

    @property
    def metrics(self):
        """
        Gets the metrics of this TextClassificationEvaluationResults.

        :return: The metrics of this TextClassificationEvaluationResults.
        :rtype: oci.ai_language.models.TextClassificationModelMetrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this TextClassificationEvaluationResults.

        :param metrics: The metrics of this TextClassificationEvaluationResults.
        :type: oci.ai_language.models.TextClassificationModelMetrics
        """
        self._metrics = metrics

    @property
    def class_metrics(self):
        """
        Gets the class_metrics of this TextClassificationEvaluationResults.
        List of text classification metrics


        :return: The class_metrics of this TextClassificationEvaluationResults.
        :rtype: list[oci.ai_language.models.ClassMetrics]
        """
        return self._class_metrics

    @class_metrics.setter
    def class_metrics(self, class_metrics):
        """
        Sets the class_metrics of this TextClassificationEvaluationResults.
        List of text classification metrics


        :param class_metrics: The class_metrics of this TextClassificationEvaluationResults.
        :type: list[oci.ai_language.models.ClassMetrics]
        """
        self._class_metrics = class_metrics

    @property
    def confusion_matrix(self):
        """
        Gets the confusion_matrix of this TextClassificationEvaluationResults.
        class level confusion matrix


        :return: The confusion_matrix of this TextClassificationEvaluationResults.
        :rtype: dict(str, ConfusionMatrixDetails)
        """
        return self._confusion_matrix

    @confusion_matrix.setter
    def confusion_matrix(self, confusion_matrix):
        """
        Sets the confusion_matrix of this TextClassificationEvaluationResults.
        class level confusion matrix


        :param confusion_matrix: The confusion_matrix of this TextClassificationEvaluationResults.
        :type: dict(str, ConfusionMatrixDetails)
        """
        self._confusion_matrix = confusion_matrix

    @property
    def labels(self):
        """
        Gets the labels of this TextClassificationEvaluationResults.
        labels


        :return: The labels of this TextClassificationEvaluationResults.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this TextClassificationEvaluationResults.
        labels


        :param labels: The labels of this TextClassificationEvaluationResults.
        :type: list[str]
        """
        self._labels = labels

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
