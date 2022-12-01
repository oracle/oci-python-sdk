# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_details import DatabaseDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseDetails(DatabaseDetails):
    """
    The details of the Oracle Autonomous Database to be registered as a target database in Data Safe.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.AutonomousDatabaseDetails.database_type` attribute
        of this class is ``AUTONOMOUS_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_type:
            The value to assign to the database_type property of this AutonomousDatabaseDetails.
            Allowed values for this property are: "DATABASE_CLOUD_SERVICE", "AUTONOMOUS_DATABASE", "INSTALLED_DATABASE"
        :type database_type: str

        :param infrastructure_type:
            The value to assign to the infrastructure_type property of this AutonomousDatabaseDetails.
            Allowed values for this property are: "ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD"
        :type infrastructure_type: str

        :param autonomous_database_id:
            The value to assign to the autonomous_database_id property of this AutonomousDatabaseDetails.
        :type autonomous_database_id: str

        """
        self.swagger_types = {
            'database_type': 'str',
            'infrastructure_type': 'str',
            'autonomous_database_id': 'str'
        }

        self.attribute_map = {
            'database_type': 'databaseType',
            'infrastructure_type': 'infrastructureType',
            'autonomous_database_id': 'autonomousDatabaseId'
        }

        self._database_type = None
        self._infrastructure_type = None
        self._autonomous_database_id = None
        self._database_type = 'AUTONOMOUS_DATABASE'

    @property
    def autonomous_database_id(self):
        """
        **[Required]** Gets the autonomous_database_id of this AutonomousDatabaseDetails.
        The OCID of the autonomous database registered as a target database in Data Safe.


        :return: The autonomous_database_id of this AutonomousDatabaseDetails.
        :rtype: str
        """
        return self._autonomous_database_id

    @autonomous_database_id.setter
    def autonomous_database_id(self, autonomous_database_id):
        """
        Sets the autonomous_database_id of this AutonomousDatabaseDetails.
        The OCID of the autonomous database registered as a target database in Data Safe.


        :param autonomous_database_id: The autonomous_database_id of this AutonomousDatabaseDetails.
        :type: str
        """
        self._autonomous_database_id = autonomous_database_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
