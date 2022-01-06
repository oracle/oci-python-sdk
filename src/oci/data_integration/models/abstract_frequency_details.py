# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AbstractFrequencyDetails(object):
    """
    The model that holds the frequency details.
    """

    #: A constant which can be used with the model_type property of a AbstractFrequencyDetails.
    #: This constant has a value of "HOURLY"
    MODEL_TYPE_HOURLY = "HOURLY"

    #: A constant which can be used with the model_type property of a AbstractFrequencyDetails.
    #: This constant has a value of "DAILY"
    MODEL_TYPE_DAILY = "DAILY"

    #: A constant which can be used with the model_type property of a AbstractFrequencyDetails.
    #: This constant has a value of "MONTHLY"
    MODEL_TYPE_MONTHLY = "MONTHLY"

    #: A constant which can be used with the model_type property of a AbstractFrequencyDetails.
    #: This constant has a value of "WEEKLY"
    MODEL_TYPE_WEEKLY = "WEEKLY"

    #: A constant which can be used with the model_type property of a AbstractFrequencyDetails.
    #: This constant has a value of "MONTHLY_RULE"
    MODEL_TYPE_MONTHLY_RULE = "MONTHLY_RULE"

    #: A constant which can be used with the model_type property of a AbstractFrequencyDetails.
    #: This constant has a value of "CUSTOM"
    MODEL_TYPE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the frequency property of a AbstractFrequencyDetails.
    #: This constant has a value of "HOURLY"
    FREQUENCY_HOURLY = "HOURLY"

    #: A constant which can be used with the frequency property of a AbstractFrequencyDetails.
    #: This constant has a value of "DAILY"
    FREQUENCY_DAILY = "DAILY"

    #: A constant which can be used with the frequency property of a AbstractFrequencyDetails.
    #: This constant has a value of "MONTHLY"
    FREQUENCY_MONTHLY = "MONTHLY"

    #: A constant which can be used with the frequency property of a AbstractFrequencyDetails.
    #: This constant has a value of "WEEKLY"
    FREQUENCY_WEEKLY = "WEEKLY"

    #: A constant which can be used with the frequency property of a AbstractFrequencyDetails.
    #: This constant has a value of "CUSTOM"
    FREQUENCY_CUSTOM = "CUSTOM"

    def __init__(self, **kwargs):
        """
        Initializes a new AbstractFrequencyDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.MonthlyFrequencyDetails`
        * :class:`~oci.data_integration.models.CustomFrequencyDetails`
        * :class:`~oci.data_integration.models.DailyFrequencyDetails`
        * :class:`~oci.data_integration.models.WeeklyFrequencyDetails`
        * :class:`~oci.data_integration.models.MonthlyRuleFrequencyDetails`
        * :class:`~oci.data_integration.models.HourlyFrequencyDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this AbstractFrequencyDetails.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "WEEKLY", "MONTHLY_RULE", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param frequency:
            The value to assign to the frequency property of this AbstractFrequencyDetails.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "WEEKLY", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type frequency: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'frequency': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'frequency': 'frequency'
        }

        self._model_type = None
        self._frequency = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'MONTHLY':
            return 'MonthlyFrequencyDetails'

        if type == 'CUSTOM':
            return 'CustomFrequencyDetails'

        if type == 'DAILY':
            return 'DailyFrequencyDetails'

        if type == 'WEEKLY':
            return 'WeeklyFrequencyDetails'

        if type == 'MONTHLY_RULE':
            return 'MonthlyRuleFrequencyDetails'

        if type == 'HOURLY':
            return 'HourlyFrequencyDetails'
        else:
            return 'AbstractFrequencyDetails'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this AbstractFrequencyDetails.
        The type of the model

        Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "WEEKLY", "MONTHLY_RULE", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this AbstractFrequencyDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this AbstractFrequencyDetails.
        The type of the model


        :param model_type: The model_type of this AbstractFrequencyDetails.
        :type: str
        """
        allowed_values = ["HOURLY", "DAILY", "MONTHLY", "WEEKLY", "MONTHLY_RULE", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def frequency(self):
        """
        Gets the frequency of this AbstractFrequencyDetails.
        the frequency of the schedule.

        Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "WEEKLY", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The frequency of this AbstractFrequencyDetails.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """
        Sets the frequency of this AbstractFrequencyDetails.
        the frequency of the schedule.


        :param frequency: The frequency of this AbstractFrequencyDetails.
        :type: str
        """
        allowed_values = ["HOURLY", "DAILY", "MONTHLY", "WEEKLY", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(frequency, allowed_values):
            frequency = 'UNKNOWN_ENUM_VALUE'
        self._frequency = frequency

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
