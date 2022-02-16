# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_read_attribute import AbstractReadAttribute
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BiccReadAttributes(AbstractReadAttribute):
    """
    Properties to configure reading from an Oracle Database.
    """

    #: A constant which can be used with the extract_strategy property of a BiccReadAttributes.
    #: This constant has a value of "FULL"
    EXTRACT_STRATEGY_FULL = "FULL"

    #: A constant which can be used with the extract_strategy property of a BiccReadAttributes.
    #: This constant has a value of "INCREMENTAL"
    EXTRACT_STRATEGY_INCREMENTAL = "INCREMENTAL"

    def __init__(self, **kwargs):
        """
        Initializes a new BiccReadAttributes object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.BiccReadAttributes.model_type` attribute
        of this class is ``BICC_READ_ATTRIBUTE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this BiccReadAttributes.
            Allowed values for this property are: "ORACLEREADATTRIBUTE", "ORACLE_READ_ATTRIBUTE", "BICC_READ_ATTRIBUTE"
        :type model_type: str

        :param fetch_size:
            The value to assign to the fetch_size property of this BiccReadAttributes.
        :type fetch_size: int

        :param extract_strategy:
            The value to assign to the extract_strategy property of this BiccReadAttributes.
            Allowed values for this property are: "FULL", "INCREMENTAL"
        :type extract_strategy: str

        :param external_storage:
            The value to assign to the external_storage property of this BiccReadAttributes.
        :type external_storage: oci.data_connectivity.models.ExternalStorage

        :param initial_extract_date:
            The value to assign to the initial_extract_date property of this BiccReadAttributes.
        :type initial_extract_date: datetime

        :param last_extract_date:
            The value to assign to the last_extract_date property of this BiccReadAttributes.
        :type last_extract_date: datetime

        """
        self.swagger_types = {
            'model_type': 'str',
            'fetch_size': 'int',
            'extract_strategy': 'str',
            'external_storage': 'ExternalStorage',
            'initial_extract_date': 'datetime',
            'last_extract_date': 'datetime'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'fetch_size': 'fetchSize',
            'extract_strategy': 'extractStrategy',
            'external_storage': 'externalStorage',
            'initial_extract_date': 'initialExtractDate',
            'last_extract_date': 'lastExtractDate'
        }

        self._model_type = None
        self._fetch_size = None
        self._extract_strategy = None
        self._external_storage = None
        self._initial_extract_date = None
        self._last_extract_date = None
        self._model_type = 'BICC_READ_ATTRIBUTE'

    @property
    def fetch_size(self):
        """
        Gets the fetch_size of this BiccReadAttributes.
        The fetch size for reading.


        :return: The fetch_size of this BiccReadAttributes.
        :rtype: int
        """
        return self._fetch_size

    @fetch_size.setter
    def fetch_size(self, fetch_size):
        """
        Sets the fetch_size of this BiccReadAttributes.
        The fetch size for reading.


        :param fetch_size: The fetch_size of this BiccReadAttributes.
        :type: int
        """
        self._fetch_size = fetch_size

    @property
    def extract_strategy(self):
        """
        Gets the extract_strategy of this BiccReadAttributes.
        Extraction Strategy - FULL|INCREMENTAL

        Allowed values for this property are: "FULL", "INCREMENTAL"


        :return: The extract_strategy of this BiccReadAttributes.
        :rtype: str
        """
        return self._extract_strategy

    @extract_strategy.setter
    def extract_strategy(self, extract_strategy):
        """
        Sets the extract_strategy of this BiccReadAttributes.
        Extraction Strategy - FULL|INCREMENTAL


        :param extract_strategy: The extract_strategy of this BiccReadAttributes.
        :type: str
        """
        allowed_values = ["FULL", "INCREMENTAL"]
        if not value_allowed_none_or_none_sentinel(extract_strategy, allowed_values):
            raise ValueError(
                "Invalid value for `extract_strategy`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._extract_strategy = extract_strategy

    @property
    def external_storage(self):
        """
        Gets the external_storage of this BiccReadAttributes.

        :return: The external_storage of this BiccReadAttributes.
        :rtype: oci.data_connectivity.models.ExternalStorage
        """
        return self._external_storage

    @external_storage.setter
    def external_storage(self, external_storage):
        """
        Sets the external_storage of this BiccReadAttributes.

        :param external_storage: The external_storage of this BiccReadAttributes.
        :type: oci.data_connectivity.models.ExternalStorage
        """
        self._external_storage = external_storage

    @property
    def initial_extract_date(self):
        """
        Gets the initial_extract_date of this BiccReadAttributes.
        Date from where extract should start


        :return: The initial_extract_date of this BiccReadAttributes.
        :rtype: datetime
        """
        return self._initial_extract_date

    @initial_extract_date.setter
    def initial_extract_date(self, initial_extract_date):
        """
        Sets the initial_extract_date of this BiccReadAttributes.
        Date from where extract should start


        :param initial_extract_date: The initial_extract_date of this BiccReadAttributes.
        :type: datetime
        """
        self._initial_extract_date = initial_extract_date

    @property
    def last_extract_date(self):
        """
        Gets the last_extract_date of this BiccReadAttributes.
        Date last extracted


        :return: The last_extract_date of this BiccReadAttributes.
        :rtype: datetime
        """
        return self._last_extract_date

    @last_extract_date.setter
    def last_extract_date(self, last_extract_date):
        """
        Sets the last_extract_date of this BiccReadAttributes.
        Date last extracted


        :param last_extract_date: The last_extract_date of this BiccReadAttributes.
        :type: datetime
        """
        self._last_extract_date = last_extract_date

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
