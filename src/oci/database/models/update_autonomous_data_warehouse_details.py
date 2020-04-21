# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAutonomousDataWarehouseDetails(object):
    """
    **Deprecated.** See :func:`update_autonomous_database_details` for reference information about updating an Autonomous Data Warehouse.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAutonomousDataWarehouseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this UpdateAutonomousDataWarehouseDetails.
        :type cpu_core_count: int

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this UpdateAutonomousDataWarehouseDetails.
        :type data_storage_size_in_tbs: int

        :param display_name:
            The value to assign to the display_name property of this UpdateAutonomousDataWarehouseDetails.
        :type display_name: str

        :param admin_password:
            The value to assign to the admin_password property of this UpdateAutonomousDataWarehouseDetails.
        :type admin_password: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAutonomousDataWarehouseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAutonomousDataWarehouseDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'cpu_core_count': 'int',
            'data_storage_size_in_tbs': 'int',
            'display_name': 'str',
            'admin_password': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'cpu_core_count': 'cpuCoreCount',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'display_name': 'displayName',
            'admin_password': 'adminPassword',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._cpu_core_count = None
        self._data_storage_size_in_tbs = None
        self._display_name = None
        self._admin_password = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this UpdateAutonomousDataWarehouseDetails.
        The number of CPU cores to be made available to the database.


        :return: The cpu_core_count of this UpdateAutonomousDataWarehouseDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this UpdateAutonomousDataWarehouseDetails.
        The number of CPU cores to be made available to the database.


        :param cpu_core_count: The cpu_core_count of this UpdateAutonomousDataWarehouseDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def data_storage_size_in_tbs(self):
        """
        Gets the data_storage_size_in_tbs of this UpdateAutonomousDataWarehouseDetails.
        Size, in terabytes, of the data volume that will be attached to the database.


        :return: The data_storage_size_in_tbs of this UpdateAutonomousDataWarehouseDetails.
        :rtype: int
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this UpdateAutonomousDataWarehouseDetails.
        Size, in terabytes, of the data volume that will be attached to the database.


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this UpdateAutonomousDataWarehouseDetails.
        :type: int
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAutonomousDataWarehouseDetails.
        The user-friendly name for the Autonomous Data Warehouse. The name does not have to be unique.


        :return: The display_name of this UpdateAutonomousDataWarehouseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAutonomousDataWarehouseDetails.
        The user-friendly name for the Autonomous Data Warehouse. The name does not have to be unique.


        :param display_name: The display_name of this UpdateAutonomousDataWarehouseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def admin_password(self):
        """
        Gets the admin_password of this UpdateAutonomousDataWarehouseDetails.
        The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing. It must be different from the last four passwords and it must not be a password used within the last 24 hours.


        :return: The admin_password of this UpdateAutonomousDataWarehouseDetails.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this UpdateAutonomousDataWarehouseDetails.
        The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing. It must be different from the last four passwords and it must not be a password used within the last 24 hours.


        :param admin_password: The admin_password of this UpdateAutonomousDataWarehouseDetails.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAutonomousDataWarehouseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateAutonomousDataWarehouseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAutonomousDataWarehouseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateAutonomousDataWarehouseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAutonomousDataWarehouseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateAutonomousDataWarehouseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAutonomousDataWarehouseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateAutonomousDataWarehouseDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
