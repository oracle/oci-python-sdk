# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InitialRecordGenerationConfiguration(object):
    """
    The initial generate records configuration It generates records from the dataset's source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InitialRecordGenerationConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param limit:
            The value to assign to the limit property of this InitialRecordGenerationConfiguration.
        :type limit: float

        """
        self.swagger_types = {
            'limit': 'float'
        }

        self.attribute_map = {
            'limit': 'limit'
        }

        self._limit = None

    @property
    def limit(self):
        """
        Gets the limit of this InitialRecordGenerationConfiguration.
        The maximum number of records to generate.


        :return: The limit of this InitialRecordGenerationConfiguration.
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this InitialRecordGenerationConfiguration.
        The maximum number of records to generate.


        :param limit: The limit of this InitialRecordGenerationConfiguration.
        :type: float
        """
        self._limit = limit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
