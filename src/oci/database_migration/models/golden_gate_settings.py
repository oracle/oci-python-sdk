# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GoldenGateSettings(object):
    """
    Optional settings for Oracle GoldenGate processes
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GoldenGateSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param extract:
            The value to assign to the extract property of this GoldenGateSettings.
        :type extract: oci.database_migration.models.Extract

        :param replicat:
            The value to assign to the replicat property of this GoldenGateSettings.
        :type replicat: oci.database_migration.models.Replicat

        :param acceptable_lag:
            The value to assign to the acceptable_lag property of this GoldenGateSettings.
        :type acceptable_lag: int

        """
        self.swagger_types = {
            'extract': 'Extract',
            'replicat': 'Replicat',
            'acceptable_lag': 'int'
        }

        self.attribute_map = {
            'extract': 'extract',
            'replicat': 'replicat',
            'acceptable_lag': 'acceptableLag'
        }

        self._extract = None
        self._replicat = None
        self._acceptable_lag = None

    @property
    def extract(self):
        """
        Gets the extract of this GoldenGateSettings.

        :return: The extract of this GoldenGateSettings.
        :rtype: oci.database_migration.models.Extract
        """
        return self._extract

    @extract.setter
    def extract(self, extract):
        """
        Sets the extract of this GoldenGateSettings.

        :param extract: The extract of this GoldenGateSettings.
        :type: oci.database_migration.models.Extract
        """
        self._extract = extract

    @property
    def replicat(self):
        """
        Gets the replicat of this GoldenGateSettings.

        :return: The replicat of this GoldenGateSettings.
        :rtype: oci.database_migration.models.Replicat
        """
        return self._replicat

    @replicat.setter
    def replicat(self, replicat):
        """
        Sets the replicat of this GoldenGateSettings.

        :param replicat: The replicat of this GoldenGateSettings.
        :type: oci.database_migration.models.Replicat
        """
        self._replicat = replicat

    @property
    def acceptable_lag(self):
        """
        Gets the acceptable_lag of this GoldenGateSettings.
        ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.


        :return: The acceptable_lag of this GoldenGateSettings.
        :rtype: int
        """
        return self._acceptable_lag

    @acceptable_lag.setter
    def acceptable_lag(self, acceptable_lag):
        """
        Sets the acceptable_lag of this GoldenGateSettings.
        ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.


        :param acceptable_lag: The acceptable_lag of this GoldenGateSettings.
        :type: int
        """
        self._acceptable_lag = acceptable_lag

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
