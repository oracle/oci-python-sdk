# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceConfiguration(object):
    """
    Properties related to a resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param spark_version:
            The value to assign to the spark_version property of this ResourceConfiguration.
        :type spark_version: str

        :param driver_shape:
            The value to assign to the driver_shape property of this ResourceConfiguration.
        :type driver_shape: str

        :param executor_shape:
            The value to assign to the executor_shape property of this ResourceConfiguration.
        :type executor_shape: str

        :param total_executors:
            The value to assign to the total_executors property of this ResourceConfiguration.
        :type total_executors: int

        """
        self.swagger_types = {
            'spark_version': 'str',
            'driver_shape': 'str',
            'executor_shape': 'str',
            'total_executors': 'int'
        }

        self.attribute_map = {
            'spark_version': 'sparkVersion',
            'driver_shape': 'driverShape',
            'executor_shape': 'executorShape',
            'total_executors': 'totalExecutors'
        }

        self._spark_version = None
        self._driver_shape = None
        self._executor_shape = None
        self._total_executors = None

    @property
    def spark_version(self):
        """
        **[Required]** Gets the spark_version of this ResourceConfiguration.
        The version of the spark used while creating an Oracle Cloud Infrastructure Data Flow application.


        :return: The spark_version of this ResourceConfiguration.
        :rtype: str
        """
        return self._spark_version

    @spark_version.setter
    def spark_version(self, spark_version):
        """
        Sets the spark_version of this ResourceConfiguration.
        The version of the spark used while creating an Oracle Cloud Infrastructure Data Flow application.


        :param spark_version: The spark_version of this ResourceConfiguration.
        :type: str
        """
        self._spark_version = spark_version

    @property
    def driver_shape(self):
        """
        **[Required]** Gets the driver_shape of this ResourceConfiguration.
        The VM shape of the driver used while creating an Oracle Cloud Infrastructure Data Flow application. It sets the driver cores and memory.


        :return: The driver_shape of this ResourceConfiguration.
        :rtype: str
        """
        return self._driver_shape

    @driver_shape.setter
    def driver_shape(self, driver_shape):
        """
        Sets the driver_shape of this ResourceConfiguration.
        The VM shape of the driver used while creating an Oracle Cloud Infrastructure Data Flow application. It sets the driver cores and memory.


        :param driver_shape: The driver_shape of this ResourceConfiguration.
        :type: str
        """
        self._driver_shape = driver_shape

    @property
    def executor_shape(self):
        """
        **[Required]** Gets the executor_shape of this ResourceConfiguration.
        The shape of the executor used while creating an Oracle Cloud Infrastructure Data Flow application. It sets the executor cores and memory.


        :return: The executor_shape of this ResourceConfiguration.
        :rtype: str
        """
        return self._executor_shape

    @executor_shape.setter
    def executor_shape(self, executor_shape):
        """
        Sets the executor_shape of this ResourceConfiguration.
        The shape of the executor used while creating an Oracle Cloud Infrastructure Data Flow application. It sets the executor cores and memory.


        :param executor_shape: The executor_shape of this ResourceConfiguration.
        :type: str
        """
        self._executor_shape = executor_shape

    @property
    def total_executors(self):
        """
        **[Required]** Gets the total_executors of this ResourceConfiguration.
        Number of executor VMs requested while creating an Oracle Cloud Infrastructure Data Flow application.


        :return: The total_executors of this ResourceConfiguration.
        :rtype: int
        """
        return self._total_executors

    @total_executors.setter
    def total_executors(self, total_executors):
        """
        Sets the total_executors of this ResourceConfiguration.
        Number of executor VMs requested while creating an Oracle Cloud Infrastructure Data Flow application.


        :param total_executors: The total_executors of this ResourceConfiguration.
        :type: int
        """
        self._total_executors = total_executors

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
