# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EvaluatedMetric(object):
    """
    One of the metrics that will be evaluated by profiles using this profile level.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EvaluatedMetric object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this EvaluatedMetric.
        :type name: str

        :param statistic:
            The value to assign to the statistic property of this EvaluatedMetric.
        :type statistic: str

        :param threshold:
            The value to assign to the threshold property of this EvaluatedMetric.
        :type threshold: float

        :param target:
            The value to assign to the target property of this EvaluatedMetric.
        :type target: float

        """
        self.swagger_types = {
            'name': 'str',
            'statistic': 'str',
            'threshold': 'float',
            'target': 'float'
        }

        self.attribute_map = {
            'name': 'name',
            'statistic': 'statistic',
            'threshold': 'threshold',
            'target': 'target'
        }

        self._name = None
        self._statistic = None
        self._threshold = None
        self._target = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this EvaluatedMetric.
        The name of the metric (e.g., `CpuUtilization`).


        :return: The name of this EvaluatedMetric.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EvaluatedMetric.
        The name of the metric (e.g., `CpuUtilization`).


        :param name: The name of this EvaluatedMetric.
        :type: str
        """
        self._name = name

    @property
    def statistic(self):
        """
        **[Required]** Gets the statistic of this EvaluatedMetric.
        The name of the statistic (e.g., `p95`).


        :return: The statistic of this EvaluatedMetric.
        :rtype: str
        """
        return self._statistic

    @statistic.setter
    def statistic(self, statistic):
        """
        Sets the statistic of this EvaluatedMetric.
        The name of the statistic (e.g., `p95`).


        :param statistic: The statistic of this EvaluatedMetric.
        :type: str
        """
        self._statistic = statistic

    @property
    def threshold(self):
        """
        **[Required]** Gets the threshold of this EvaluatedMetric.
        The threshold that must be crossed for the recommendation to appear.


        :return: The threshold of this EvaluatedMetric.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """
        Sets the threshold of this EvaluatedMetric.
        The threshold that must be crossed for the recommendation to appear.


        :param threshold: The threshold of this EvaluatedMetric.
        :type: float
        """
        self._threshold = threshold

    @property
    def target(self):
        """
        Gets the target of this EvaluatedMetric.
        Optional. The metric value that the recommendation will target.


        :return: The target of this EvaluatedMetric.
        :rtype: float
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this EvaluatedMetric.
        Optional. The metric value that the recommendation will target.


        :param target: The target of this EvaluatedMetric.
        :type: float
        """
        self._target = target

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
