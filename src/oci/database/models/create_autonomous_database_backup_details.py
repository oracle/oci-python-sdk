# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutonomousDatabaseBackupDetails(object):
    """
    Details to create an Oracle Autonomous Database backup.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutonomousDatabaseBackupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateAutonomousDatabaseBackupDetails.
        :type display_name: str

        :param autonomous_database_id:
            The value to assign to the autonomous_database_id property of this CreateAutonomousDatabaseBackupDetails.
        :type autonomous_database_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'autonomous_database_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'autonomous_database_id': 'autonomousDatabaseId'
        }

        self._display_name = None
        self._autonomous_database_id = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateAutonomousDatabaseBackupDetails.
        The user-friendly name for the backup. The name does not have to be unique.


        :return: The display_name of this CreateAutonomousDatabaseBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAutonomousDatabaseBackupDetails.
        The user-friendly name for the backup. The name does not have to be unique.


        :param display_name: The display_name of this CreateAutonomousDatabaseBackupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def autonomous_database_id(self):
        """
        **[Required]** Gets the autonomous_database_id of this CreateAutonomousDatabaseBackupDetails.
        The `OCID`__ of the Autonomous Database backup.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The autonomous_database_id of this CreateAutonomousDatabaseBackupDetails.
        :rtype: str
        """
        return self._autonomous_database_id

    @autonomous_database_id.setter
    def autonomous_database_id(self, autonomous_database_id):
        """
        Sets the autonomous_database_id of this CreateAutonomousDatabaseBackupDetails.
        The `OCID`__ of the Autonomous Database backup.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param autonomous_database_id: The autonomous_database_id of this CreateAutonomousDatabaseBackupDetails.
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
