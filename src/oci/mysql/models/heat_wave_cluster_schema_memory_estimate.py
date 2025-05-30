# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190415


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HeatWaveClusterSchemaMemoryEstimate(object):
    """
    Schema with estimated memory footprints for each MySQL user table
    of the schema when loaded to HeatWave cluster memory.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HeatWaveClusterSchemaMemoryEstimate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param schema_name:
            The value to assign to the schema_name property of this HeatWaveClusterSchemaMemoryEstimate.
        :type schema_name: str

        :param per_table_estimates:
            The value to assign to the per_table_estimates property of this HeatWaveClusterSchemaMemoryEstimate.
        :type per_table_estimates: list[oci.mysql.models.HeatWaveClusterTableMemoryEstimate]

        """
        self.swagger_types = {
            'schema_name': 'str',
            'per_table_estimates': 'list[HeatWaveClusterTableMemoryEstimate]'
        }
        self.attribute_map = {
            'schema_name': 'schemaName',
            'per_table_estimates': 'perTableEstimates'
        }
        self._schema_name = None
        self._per_table_estimates = None

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this HeatWaveClusterSchemaMemoryEstimate.
        The name of the schema.


        :return: The schema_name of this HeatWaveClusterSchemaMemoryEstimate.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this HeatWaveClusterSchemaMemoryEstimate.
        The name of the schema.


        :param schema_name: The schema_name of this HeatWaveClusterSchemaMemoryEstimate.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def per_table_estimates(self):
        """
        **[Required]** Gets the per_table_estimates of this HeatWaveClusterSchemaMemoryEstimate.
        Estimated memory footprints for MySQL user tables of the schema
        when loaded to HeatWave cluster memory.


        :return: The per_table_estimates of this HeatWaveClusterSchemaMemoryEstimate.
        :rtype: list[oci.mysql.models.HeatWaveClusterTableMemoryEstimate]
        """
        return self._per_table_estimates

    @per_table_estimates.setter
    def per_table_estimates(self, per_table_estimates):
        """
        Sets the per_table_estimates of this HeatWaveClusterSchemaMemoryEstimate.
        Estimated memory footprints for MySQL user tables of the schema
        when loaded to HeatWave cluster memory.


        :param per_table_estimates: The per_table_estimates of this HeatWaveClusterSchemaMemoryEstimate.
        :type: list[oci.mysql.models.HeatWaveClusterTableMemoryEstimate]
        """
        self._per_table_estimates = per_table_estimates

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
