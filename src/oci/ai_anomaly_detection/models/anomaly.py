# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Anomaly(object):
    """
    An object to hold value information for each anomaly point
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Anomaly object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param signal_name:
            The value to assign to the signal_name property of this Anomaly.
        :type signal_name: str

        :param actual_value:
            The value to assign to the actual_value property of this Anomaly.
        :type actual_value: float

        :param estimated_value:
            The value to assign to the estimated_value property of this Anomaly.
        :type estimated_value: float

        :param imputed_value:
            The value to assign to the imputed_value property of this Anomaly.
        :type imputed_value: float

        :param anomaly_score:
            The value to assign to the anomaly_score property of this Anomaly.
        :type anomaly_score: float

        """
        self.swagger_types = {
            'signal_name': 'str',
            'actual_value': 'float',
            'estimated_value': 'float',
            'imputed_value': 'float',
            'anomaly_score': 'float'
        }

        self.attribute_map = {
            'signal_name': 'signalName',
            'actual_value': 'actualValue',
            'estimated_value': 'estimatedValue',
            'imputed_value': 'imputedValue',
            'anomaly_score': 'anomalyScore'
        }

        self._signal_name = None
        self._actual_value = None
        self._estimated_value = None
        self._imputed_value = None
        self._anomaly_score = None

    @property
    def signal_name(self):
        """
        **[Required]** Gets the signal_name of this Anomaly.
        Name of a signal where current anomaly point belongs to


        :return: The signal_name of this Anomaly.
        :rtype: str
        """
        return self._signal_name

    @signal_name.setter
    def signal_name(self, signal_name):
        """
        Sets the signal_name of this Anomaly.
        Name of a signal where current anomaly point belongs to


        :param signal_name: The signal_name of this Anomaly.
        :type: str
        """
        self._signal_name = signal_name

    @property
    def actual_value(self):
        """
        **[Required]** Gets the actual_value of this Anomaly.
        The actual value for the anomaly point at given signal and timestamp/row


        :return: The actual_value of this Anomaly.
        :rtype: float
        """
        return self._actual_value

    @actual_value.setter
    def actual_value(self, actual_value):
        """
        Sets the actual_value of this Anomaly.
        The actual value for the anomaly point at given signal and timestamp/row


        :param actual_value: The actual_value of this Anomaly.
        :type: float
        """
        self._actual_value = actual_value

    @property
    def estimated_value(self):
        """
        **[Required]** Gets the estimated_value of this Anomaly.
        The estimated value for the anomaly point at given signal and timestamp/row


        :return: The estimated_value of this Anomaly.
        :rtype: float
        """
        return self._estimated_value

    @estimated_value.setter
    def estimated_value(self, estimated_value):
        """
        Sets the estimated_value of this Anomaly.
        The estimated value for the anomaly point at given signal and timestamp/row


        :param estimated_value: The estimated_value of this Anomaly.
        :type: float
        """
        self._estimated_value = estimated_value

    @property
    def imputed_value(self):
        """
        Gets the imputed_value of this Anomaly.
        The value imputed by one of IDP step for missing values in origin data


        :return: The imputed_value of this Anomaly.
        :rtype: float
        """
        return self._imputed_value

    @imputed_value.setter
    def imputed_value(self, imputed_value):
        """
        Sets the imputed_value of this Anomaly.
        The value imputed by one of IDP step for missing values in origin data


        :param imputed_value: The imputed_value of this Anomaly.
        :type: float
        """
        self._imputed_value = imputed_value

    @property
    def anomaly_score(self):
        """
        **[Required]** Gets the anomaly_score of this Anomaly.
        A significant score ranged from 0 to 1 to each anomaly point


        :return: The anomaly_score of this Anomaly.
        :rtype: float
        """
        return self._anomaly_score

    @anomaly_score.setter
    def anomaly_score(self, anomaly_score):
        """
        Sets the anomaly_score of this Anomaly.
        A significant score ranged from 0 to 1 to each anomaly point


        :param anomaly_score: The anomaly_score of this Anomaly.
        :type: float
        """
        self._anomaly_score = anomaly_score

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
