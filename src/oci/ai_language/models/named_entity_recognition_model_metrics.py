# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NamedEntityRecognitionModelMetrics(object):
    """
    Model level named entity recognition metrics
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NamedEntityRecognitionModelMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param micro_f1:
            The value to assign to the micro_f1 property of this NamedEntityRecognitionModelMetrics.
        :type micro_f1: float

        :param micro_precision:
            The value to assign to the micro_precision property of this NamedEntityRecognitionModelMetrics.
        :type micro_precision: float

        :param micro_recall:
            The value to assign to the micro_recall property of this NamedEntityRecognitionModelMetrics.
        :type micro_recall: float

        :param macro_f1:
            The value to assign to the macro_f1 property of this NamedEntityRecognitionModelMetrics.
        :type macro_f1: float

        :param macro_precision:
            The value to assign to the macro_precision property of this NamedEntityRecognitionModelMetrics.
        :type macro_precision: float

        :param macro_recall:
            The value to assign to the macro_recall property of this NamedEntityRecognitionModelMetrics.
        :type macro_recall: float

        :param weighted_f1:
            The value to assign to the weighted_f1 property of this NamedEntityRecognitionModelMetrics.
        :type weighted_f1: float

        :param weighted_precision:
            The value to assign to the weighted_precision property of this NamedEntityRecognitionModelMetrics.
        :type weighted_precision: float

        :param weighted_recall:
            The value to assign to the weighted_recall property of this NamedEntityRecognitionModelMetrics.
        :type weighted_recall: float

        """
        self.swagger_types = {
            'micro_f1': 'float',
            'micro_precision': 'float',
            'micro_recall': 'float',
            'macro_f1': 'float',
            'macro_precision': 'float',
            'macro_recall': 'float',
            'weighted_f1': 'float',
            'weighted_precision': 'float',
            'weighted_recall': 'float'
        }

        self.attribute_map = {
            'micro_f1': 'microF1',
            'micro_precision': 'microPrecision',
            'micro_recall': 'microRecall',
            'macro_f1': 'macroF1',
            'macro_precision': 'macroPrecision',
            'macro_recall': 'macroRecall',
            'weighted_f1': 'weightedF1',
            'weighted_precision': 'weightedPrecision',
            'weighted_recall': 'weightedRecall'
        }

        self._micro_f1 = None
        self._micro_precision = None
        self._micro_recall = None
        self._macro_f1 = None
        self._macro_precision = None
        self._macro_recall = None
        self._weighted_f1 = None
        self._weighted_precision = None
        self._weighted_recall = None

    @property
    def micro_f1(self):
        """
        **[Required]** Gets the micro_f1 of this NamedEntityRecognitionModelMetrics.
        F1-score, is a measure of a model\u2019s accuracy on a dataset


        :return: The micro_f1 of this NamedEntityRecognitionModelMetrics.
        :rtype: float
        """
        return self._micro_f1

    @micro_f1.setter
    def micro_f1(self, micro_f1):
        """
        Sets the micro_f1 of this NamedEntityRecognitionModelMetrics.
        F1-score, is a measure of a model\u2019s accuracy on a dataset


        :param micro_f1: The micro_f1 of this NamedEntityRecognitionModelMetrics.
        :type: float
        """
        self._micro_f1 = micro_f1

    @property
    def micro_precision(self):
        """
        **[Required]** Gets the micro_precision of this NamedEntityRecognitionModelMetrics.
        Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)


        :return: The micro_precision of this NamedEntityRecognitionModelMetrics.
        :rtype: float
        """
        return self._micro_precision

    @micro_precision.setter
    def micro_precision(self, micro_precision):
        """
        Sets the micro_precision of this NamedEntityRecognitionModelMetrics.
        Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)


        :param micro_precision: The micro_precision of this NamedEntityRecognitionModelMetrics.
        :type: float
        """
        self._micro_precision = micro_precision

    @property
    def micro_recall(self):
        """
        **[Required]** Gets the micro_recall of this NamedEntityRecognitionModelMetrics.
        Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.


        :return: The micro_recall of this NamedEntityRecognitionModelMetrics.
        :rtype: float
        """
        return self._micro_recall

    @micro_recall.setter
    def micro_recall(self, micro_recall):
        """
        Sets the micro_recall of this NamedEntityRecognitionModelMetrics.
        Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.


        :param micro_recall: The micro_recall of this NamedEntityRecognitionModelMetrics.
        :type: float
        """
        self._micro_recall = micro_recall

    @property
    def macro_f1(self):
        """
        **[Required]** Gets the macro_f1 of this NamedEntityRecognitionModelMetrics.
        F1-score, is a measure of a model\u2019s accuracy on a dataset


        :return: The macro_f1 of this NamedEntityRecognitionModelMetrics.
        :rtype: float
        """
        return self._macro_f1

    @macro_f1.setter
    def macro_f1(self, macro_f1):
        """
        Sets the macro_f1 of this NamedEntityRecognitionModelMetrics.
        F1-score, is a measure of a model\u2019s accuracy on a dataset


        :param macro_f1: The macro_f1 of this NamedEntityRecognitionModelMetrics.
        :type: float
        """
        self._macro_f1 = macro_f1

    @property
    def macro_precision(self):
        """
        Gets the macro_precision of this NamedEntityRecognitionModelMetrics.
        Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)


        :return: The macro_precision of this NamedEntityRecognitionModelMetrics.
        :rtype: float
        """
        return self._macro_precision

    @macro_precision.setter
    def macro_precision(self, macro_precision):
        """
        Sets the macro_precision of this NamedEntityRecognitionModelMetrics.
        Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)


        :param macro_precision: The macro_precision of this NamedEntityRecognitionModelMetrics.
        :type: float
        """
        self._macro_precision = macro_precision

    @property
    def macro_recall(self):
        """
        Gets the macro_recall of this NamedEntityRecognitionModelMetrics.
        Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.


        :return: The macro_recall of this NamedEntityRecognitionModelMetrics.
        :rtype: float
        """
        return self._macro_recall

    @macro_recall.setter
    def macro_recall(self, macro_recall):
        """
        Sets the macro_recall of this NamedEntityRecognitionModelMetrics.
        Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.


        :param macro_recall: The macro_recall of this NamedEntityRecognitionModelMetrics.
        :type: float
        """
        self._macro_recall = macro_recall

    @property
    def weighted_f1(self):
        """
        Gets the weighted_f1 of this NamedEntityRecognitionModelMetrics.
        F1-score, is a measure of a model\u2019s accuracy on a dataset


        :return: The weighted_f1 of this NamedEntityRecognitionModelMetrics.
        :rtype: float
        """
        return self._weighted_f1

    @weighted_f1.setter
    def weighted_f1(self, weighted_f1):
        """
        Sets the weighted_f1 of this NamedEntityRecognitionModelMetrics.
        F1-score, is a measure of a model\u2019s accuracy on a dataset


        :param weighted_f1: The weighted_f1 of this NamedEntityRecognitionModelMetrics.
        :type: float
        """
        self._weighted_f1 = weighted_f1

    @property
    def weighted_precision(self):
        """
        Gets the weighted_precision of this NamedEntityRecognitionModelMetrics.
        Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)


        :return: The weighted_precision of this NamedEntityRecognitionModelMetrics.
        :rtype: float
        """
        return self._weighted_precision

    @weighted_precision.setter
    def weighted_precision(self, weighted_precision):
        """
        Sets the weighted_precision of this NamedEntityRecognitionModelMetrics.
        Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true positives plus the number of false positives)


        :param weighted_precision: The weighted_precision of this NamedEntityRecognitionModelMetrics.
        :type: float
        """
        self._weighted_precision = weighted_precision

    @property
    def weighted_recall(self):
        """
        Gets the weighted_recall of this NamedEntityRecognitionModelMetrics.
        Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.


        :return: The weighted_recall of this NamedEntityRecognitionModelMetrics.
        :rtype: float
        """
        return self._weighted_recall

    @weighted_recall.setter
    def weighted_recall(self, weighted_recall):
        """
        Sets the weighted_recall of this NamedEntityRecognitionModelMetrics.
        Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.


        :param weighted_recall: The weighted_recall of this NamedEntityRecognitionModelMetrics.
        :type: float
        """
        self._weighted_recall = weighted_recall

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
