# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TestStrategy(object):
    """
    Possible strategy as testing and validation(optional) dataset.
    """

    #: A constant which can be used with the strategy_type property of a TestStrategy.
    #: This constant has a value of "TEST_AND_VALIDATION_DATASET"
    STRATEGY_TYPE_TEST_AND_VALIDATION_DATASET = "TEST_AND_VALIDATION_DATASET"

    def __init__(self, **kwargs):
        """
        Initializes a new TestStrategy object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_language.models.TestAndValidationDatasetStrategy`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param strategy_type:
            The value to assign to the strategy_type property of this TestStrategy.
            Allowed values for this property are: "TEST_AND_VALIDATION_DATASET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type strategy_type: str

        """
        self.swagger_types = {
            'strategy_type': 'str'
        }

        self.attribute_map = {
            'strategy_type': 'strategyType'
        }

        self._strategy_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['strategyType']

        if type == 'TEST_AND_VALIDATION_DATASET':
            return 'TestAndValidationDatasetStrategy'
        else:
            return 'TestStrategy'

    @property
    def strategy_type(self):
        """
        **[Required]** Gets the strategy_type of this TestStrategy.
        This information will define the test strategy
        different datasets for test and validation(optional) dataset.

        Allowed values for this property are: "TEST_AND_VALIDATION_DATASET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The strategy_type of this TestStrategy.
        :rtype: str
        """
        return self._strategy_type

    @strategy_type.setter
    def strategy_type(self, strategy_type):
        """
        Sets the strategy_type of this TestStrategy.
        This information will define the test strategy
        different datasets for test and validation(optional) dataset.


        :param strategy_type: The strategy_type of this TestStrategy.
        :type: str
        """
        allowed_values = ["TEST_AND_VALIDATION_DATASET"]
        if not value_allowed_none_or_none_sentinel(strategy_type, allowed_values):
            strategy_type = 'UNKNOWN_ENUM_VALUE'
        self._strategy_type = strategy_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
