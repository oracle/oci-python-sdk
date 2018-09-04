# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutonomousDataWarehouseBackupDetails(object):
    """
    Details to create an Oracle Autonomous Data Warehouse backup.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutonomousDataWarehouseBackupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param autonomous_data_warehouse_id:
            The value to assign to the autonomous_data_warehouse_id property of this CreateAutonomousDataWarehouseBackupDetails.
        :type autonomous_data_warehouse_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateAutonomousDataWarehouseBackupDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'autonomous_data_warehouse_id': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'autonomous_data_warehouse_id': 'autonomousDataWarehouseId',
            'display_name': 'displayName'
        }

        self._autonomous_data_warehouse_id = None
        self._display_name = None

    @property
    def autonomous_data_warehouse_id(self):
        """
        **[Required]** Gets the autonomous_data_warehouse_id of this CreateAutonomousDataWarehouseBackupDetails.
        The `OCID`__ of the Autonomous Data Warehouse backup.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The autonomous_data_warehouse_id of this CreateAutonomousDataWarehouseBackupDetails.
        :rtype: str
        """
        return self._autonomous_data_warehouse_id

    @autonomous_data_warehouse_id.setter
    def autonomous_data_warehouse_id(self, autonomous_data_warehouse_id):
        """
        Sets the autonomous_data_warehouse_id of this CreateAutonomousDataWarehouseBackupDetails.
        The `OCID`__ of the Autonomous Data Warehouse backup.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param autonomous_data_warehouse_id: The autonomous_data_warehouse_id of this CreateAutonomousDataWarehouseBackupDetails.
        :type: str
        """
        self._autonomous_data_warehouse_id = autonomous_data_warehouse_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateAutonomousDataWarehouseBackupDetails.
        The user-friendly name for the backup. The name does not have to be unique.


        :return: The display_name of this CreateAutonomousDataWarehouseBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAutonomousDataWarehouseBackupDetails.
        The user-friendly name for the backup. The name does not have to be unique.


        :param display_name: The display_name of this CreateAutonomousDataWarehouseBackupDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
