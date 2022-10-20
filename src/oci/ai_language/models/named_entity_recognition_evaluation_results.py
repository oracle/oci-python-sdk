# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .evaluation_results import EvaluationResults
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NamedEntityRecognitionEvaluationResults(EvaluationResults):
    """
    Named entity recognition model testing and evaluation results
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NamedEntityRecognitionEvaluationResults object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_language.models.NamedEntityRecognitionEvaluationResults.model_type` attribute
        of this class is ``NAMED_ENTITY_RECOGNITION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this NamedEntityRecognitionEvaluationResults.
        :type model_type: str

        :param metrics:
            The value to assign to the metrics property of this NamedEntityRecognitionEvaluationResults.
        :type metrics: oci.ai_language.models.NamedEntityRecognitionModelMetrics

        :param entity_metrics:
            The value to assign to the entity_metrics property of this NamedEntityRecognitionEvaluationResults.
        :type entity_metrics: list[oci.ai_language.models.EntityMetrics]

        :param confusion_matrix:
            The value to assign to the confusion_matrix property of this NamedEntityRecognitionEvaluationResults.
        :type confusion_matrix: dict(str, ConfusionMatrixDetails)

        :param labels:
            The value to assign to the labels property of this NamedEntityRecognitionEvaluationResults.
        :type labels: list[str]

        """
        self.swagger_types = {
            'model_type': 'str',
            'metrics': 'NamedEntityRecognitionModelMetrics',
            'entity_metrics': 'list[EntityMetrics]',
            'confusion_matrix': 'dict(str, ConfusionMatrixDetails)',
            'labels': 'list[str]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'metrics': 'metrics',
            'entity_metrics': 'entityMetrics',
            'confusion_matrix': 'confusionMatrix',
            'labels': 'labels'
        }

        self._model_type = None
        self._metrics = None
        self._entity_metrics = None
        self._confusion_matrix = None
        self._labels = None
        self._model_type = 'NAMED_ENTITY_RECOGNITION'

    @property
    def metrics(self):
        """
        Gets the metrics of this NamedEntityRecognitionEvaluationResults.

        :return: The metrics of this NamedEntityRecognitionEvaluationResults.
        :rtype: oci.ai_language.models.NamedEntityRecognitionModelMetrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this NamedEntityRecognitionEvaluationResults.

        :param metrics: The metrics of this NamedEntityRecognitionEvaluationResults.
        :type: oci.ai_language.models.NamedEntityRecognitionModelMetrics
        """
        self._metrics = metrics

    @property
    def entity_metrics(self):
        """
        Gets the entity_metrics of this NamedEntityRecognitionEvaluationResults.
        List of entity metrics


        :return: The entity_metrics of this NamedEntityRecognitionEvaluationResults.
        :rtype: list[oci.ai_language.models.EntityMetrics]
        """
        return self._entity_metrics

    @entity_metrics.setter
    def entity_metrics(self, entity_metrics):
        """
        Sets the entity_metrics of this NamedEntityRecognitionEvaluationResults.
        List of entity metrics


        :param entity_metrics: The entity_metrics of this NamedEntityRecognitionEvaluationResults.
        :type: list[oci.ai_language.models.EntityMetrics]
        """
        self._entity_metrics = entity_metrics

    @property
    def confusion_matrix(self):
        """
        Gets the confusion_matrix of this NamedEntityRecognitionEvaluationResults.
        class level confusion matrix


        :return: The confusion_matrix of this NamedEntityRecognitionEvaluationResults.
        :rtype: dict(str, ConfusionMatrixDetails)
        """
        return self._confusion_matrix

    @confusion_matrix.setter
    def confusion_matrix(self, confusion_matrix):
        """
        Sets the confusion_matrix of this NamedEntityRecognitionEvaluationResults.
        class level confusion matrix


        :param confusion_matrix: The confusion_matrix of this NamedEntityRecognitionEvaluationResults.
        :type: dict(str, ConfusionMatrixDetails)
        """
        self._confusion_matrix = confusion_matrix

    @property
    def labels(self):
        """
        Gets the labels of this NamedEntityRecognitionEvaluationResults.
        labels


        :return: The labels of this NamedEntityRecognitionEvaluationResults.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this NamedEntityRecognitionEvaluationResults.
        labels


        :param labels: The labels of this NamedEntityRecognitionEvaluationResults.
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
