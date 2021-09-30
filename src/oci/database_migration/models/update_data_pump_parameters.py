# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDataPumpParameters(object):
    """
    Optional parameters for Data Pump Export and Import. Refer to `Configuring Optional Initial Load Advanced Settings`__
    If an empty object is specified, the stored Data Pump Parameter details will be removed.

    __ https://docs-uat.us.oracle.com/en/cloud/paas/database-migration/dmsus/working-migration-resources.html#GUID-24BD3054-FDF8-48FF-8492-636C1D4B71ED
    """

    #: A constant which can be used with the estimate property of a UpdateDataPumpParameters.
    #: This constant has a value of "BLOCKS"
    ESTIMATE_BLOCKS = "BLOCKS"

    #: A constant which can be used with the estimate property of a UpdateDataPumpParameters.
    #: This constant has a value of "STATISTICS"
    ESTIMATE_STATISTICS = "STATISTICS"

    #: A constant which can be used with the table_exists_action property of a UpdateDataPumpParameters.
    #: This constant has a value of "TRUNCATE"
    TABLE_EXISTS_ACTION_TRUNCATE = "TRUNCATE"

    #: A constant which can be used with the table_exists_action property of a UpdateDataPumpParameters.
    #: This constant has a value of "REPLACE"
    TABLE_EXISTS_ACTION_REPLACE = "REPLACE"

    #: A constant which can be used with the table_exists_action property of a UpdateDataPumpParameters.
    #: This constant has a value of "APPEND"
    TABLE_EXISTS_ACTION_APPEND = "APPEND"

    #: A constant which can be used with the table_exists_action property of a UpdateDataPumpParameters.
    #: This constant has a value of "SKIP"
    TABLE_EXISTS_ACTION_SKIP = "SKIP"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDataPumpParameters object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_cluster:
            The value to assign to the is_cluster property of this UpdateDataPumpParameters.
        :type is_cluster: bool

        :param estimate:
            The value to assign to the estimate property of this UpdateDataPumpParameters.
            Allowed values for this property are: "BLOCKS", "STATISTICS"
        :type estimate: str

        :param table_exists_action:
            The value to assign to the table_exists_action property of this UpdateDataPumpParameters.
            Allowed values for this property are: "TRUNCATE", "REPLACE", "APPEND", "SKIP"
        :type table_exists_action: str

        :param exclude_parameters:
            The value to assign to the exclude_parameters property of this UpdateDataPumpParameters.
        :type exclude_parameters: list[oci.database_migration.models.DataPumpExcludeParameters]

        :param import_parallelism_degree:
            The value to assign to the import_parallelism_degree property of this UpdateDataPumpParameters.
        :type import_parallelism_degree: int

        :param export_parallelism_degree:
            The value to assign to the export_parallelism_degree property of this UpdateDataPumpParameters.
        :type export_parallelism_degree: int

        """
        self.swagger_types = {
            'is_cluster': 'bool',
            'estimate': 'str',
            'table_exists_action': 'str',
            'exclude_parameters': 'list[DataPumpExcludeParameters]',
            'import_parallelism_degree': 'int',
            'export_parallelism_degree': 'int'
        }

        self.attribute_map = {
            'is_cluster': 'isCluster',
            'estimate': 'estimate',
            'table_exists_action': 'tableExistsAction',
            'exclude_parameters': 'excludeParameters',
            'import_parallelism_degree': 'importParallelismDegree',
            'export_parallelism_degree': 'exportParallelismDegree'
        }

        self._is_cluster = None
        self._estimate = None
        self._table_exists_action = None
        self._exclude_parameters = None
        self._import_parallelism_degree = None
        self._export_parallelism_degree = None

    @property
    def is_cluster(self):
        """
        Gets the is_cluster of this UpdateDataPumpParameters.
        Set to false to force Data Pump worker processes to run on one instance.


        :return: The is_cluster of this UpdateDataPumpParameters.
        :rtype: bool
        """
        return self._is_cluster

    @is_cluster.setter
    def is_cluster(self, is_cluster):
        """
        Sets the is_cluster of this UpdateDataPumpParameters.
        Set to false to force Data Pump worker processes to run on one instance.


        :param is_cluster: The is_cluster of this UpdateDataPumpParameters.
        :type: bool
        """
        self._is_cluster = is_cluster

    @property
    def estimate(self):
        """
        Gets the estimate of this UpdateDataPumpParameters.
        Estimate size of dumps that will be generated.

        Allowed values for this property are: "BLOCKS", "STATISTICS"


        :return: The estimate of this UpdateDataPumpParameters.
        :rtype: str
        """
        return self._estimate

    @estimate.setter
    def estimate(self, estimate):
        """
        Sets the estimate of this UpdateDataPumpParameters.
        Estimate size of dumps that will be generated.


        :param estimate: The estimate of this UpdateDataPumpParameters.
        :type: str
        """
        allowed_values = ["BLOCKS", "STATISTICS"]
        if not value_allowed_none_or_none_sentinel(estimate, allowed_values):
            raise ValueError(
                "Invalid value for `estimate`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._estimate = estimate

    @property
    def table_exists_action(self):
        """
        Gets the table_exists_action of this UpdateDataPumpParameters.
        IMPORT: Specifies the action to be performed when data is loaded into a preexisting table.

        Allowed values for this property are: "TRUNCATE", "REPLACE", "APPEND", "SKIP"


        :return: The table_exists_action of this UpdateDataPumpParameters.
        :rtype: str
        """
        return self._table_exists_action

    @table_exists_action.setter
    def table_exists_action(self, table_exists_action):
        """
        Sets the table_exists_action of this UpdateDataPumpParameters.
        IMPORT: Specifies the action to be performed when data is loaded into a preexisting table.


        :param table_exists_action: The table_exists_action of this UpdateDataPumpParameters.
        :type: str
        """
        allowed_values = ["TRUNCATE", "REPLACE", "APPEND", "SKIP"]
        if not value_allowed_none_or_none_sentinel(table_exists_action, allowed_values):
            raise ValueError(
                "Invalid value for `table_exists_action`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._table_exists_action = table_exists_action

    @property
    def exclude_parameters(self):
        """
        Gets the exclude_parameters of this UpdateDataPumpParameters.
        Exclude paratemers for Export and Import. If specified, the stored list will be replaced.


        :return: The exclude_parameters of this UpdateDataPumpParameters.
        :rtype: list[oci.database_migration.models.DataPumpExcludeParameters]
        """
        return self._exclude_parameters

    @exclude_parameters.setter
    def exclude_parameters(self, exclude_parameters):
        """
        Sets the exclude_parameters of this UpdateDataPumpParameters.
        Exclude paratemers for Export and Import. If specified, the stored list will be replaced.


        :param exclude_parameters: The exclude_parameters of this UpdateDataPumpParameters.
        :type: list[oci.database_migration.models.DataPumpExcludeParameters]
        """
        self._exclude_parameters = exclude_parameters

    @property
    def import_parallelism_degree(self):
        """
        Gets the import_parallelism_degree of this UpdateDataPumpParameters.
        Maximum number of worker processes that can be used for a Data Pump Import job.
        For an Autonomous Database, ODMS will automatically query its CPU core count and set this property.


        :return: The import_parallelism_degree of this UpdateDataPumpParameters.
        :rtype: int
        """
        return self._import_parallelism_degree

    @import_parallelism_degree.setter
    def import_parallelism_degree(self, import_parallelism_degree):
        """
        Sets the import_parallelism_degree of this UpdateDataPumpParameters.
        Maximum number of worker processes that can be used for a Data Pump Import job.
        For an Autonomous Database, ODMS will automatically query its CPU core count and set this property.


        :param import_parallelism_degree: The import_parallelism_degree of this UpdateDataPumpParameters.
        :type: int
        """
        self._import_parallelism_degree = import_parallelism_degree

    @property
    def export_parallelism_degree(self):
        """
        Gets the export_parallelism_degree of this UpdateDataPumpParameters.
        Maximum number of worker processes that can be used for a Data Pump Export job.


        :return: The export_parallelism_degree of this UpdateDataPumpParameters.
        :rtype: int
        """
        return self._export_parallelism_degree

    @export_parallelism_degree.setter
    def export_parallelism_degree(self, export_parallelism_degree):
        """
        Sets the export_parallelism_degree of this UpdateDataPumpParameters.
        Maximum number of worker processes that can be used for a Data Pump Export job.


        :param export_parallelism_degree: The export_parallelism_degree of this UpdateDataPumpParameters.
        :type: int
        """
        self._export_parallelism_degree = export_parallelism_degree

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
