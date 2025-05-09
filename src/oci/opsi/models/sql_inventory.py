# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlInventory(object):
    """
    Inventory details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlInventory object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total_sqls:
            The value to assign to the total_sqls property of this SqlInventory.
        :type total_sqls: int

        :param total_databases:
            The value to assign to the total_databases property of this SqlInventory.
        :type total_databases: int

        :param sqls_analyzed:
            The value to assign to the sqls_analyzed property of this SqlInventory.
        :type sqls_analyzed: int

        """
        self.swagger_types = {
            'total_sqls': 'int',
            'total_databases': 'int',
            'sqls_analyzed': 'int'
        }
        self.attribute_map = {
            'total_sqls': 'totalSqls',
            'total_databases': 'totalDatabases',
            'sqls_analyzed': 'sqlsAnalyzed'
        }
        self._total_sqls = None
        self._total_databases = None
        self._sqls_analyzed = None

    @property
    def total_sqls(self):
        """
        **[Required]** Gets the total_sqls of this SqlInventory.
        Total number of sqls. Example `2000`


        :return: The total_sqls of this SqlInventory.
        :rtype: int
        """
        return self._total_sqls

    @total_sqls.setter
    def total_sqls(self, total_sqls):
        """
        Sets the total_sqls of this SqlInventory.
        Total number of sqls. Example `2000`


        :param total_sqls: The total_sqls of this SqlInventory.
        :type: int
        """
        self._total_sqls = total_sqls

    @property
    def total_databases(self):
        """
        **[Required]** Gets the total_databases of this SqlInventory.
        Total number of Databases. Example `400`


        :return: The total_databases of this SqlInventory.
        :rtype: int
        """
        return self._total_databases

    @total_databases.setter
    def total_databases(self, total_databases):
        """
        Sets the total_databases of this SqlInventory.
        Total number of Databases. Example `400`


        :param total_databases: The total_databases of this SqlInventory.
        :type: int
        """
        self._total_databases = total_databases

    @property
    def sqls_analyzed(self):
        """
        **[Required]** Gets the sqls_analyzed of this SqlInventory.
        Total number of sqls analyzed by the query. Example `120`


        :return: The sqls_analyzed of this SqlInventory.
        :rtype: int
        """
        return self._sqls_analyzed

    @sqls_analyzed.setter
    def sqls_analyzed(self, sqls_analyzed):
        """
        Sets the sqls_analyzed of this SqlInventory.
        Total number of sqls analyzed by the query. Example `120`


        :param sqls_analyzed: The sqls_analyzed of this SqlInventory.
        :type: int
        """
        self._sqls_analyzed = sqls_analyzed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
