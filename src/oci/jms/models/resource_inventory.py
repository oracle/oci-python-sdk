# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceInventory(object):
    """
    Inventory of JMS resources in a compartment during a specified time period.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceInventory object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param active_fleet_count:
            The value to assign to the active_fleet_count property of this ResourceInventory.
        :type active_fleet_count: int

        :param managed_instance_count:
            The value to assign to the managed_instance_count property of this ResourceInventory.
        :type managed_instance_count: int

        :param jre_count:
            The value to assign to the jre_count property of this ResourceInventory.
        :type jre_count: int

        :param installation_count:
            The value to assign to the installation_count property of this ResourceInventory.
        :type installation_count: int

        :param application_count:
            The value to assign to the application_count property of this ResourceInventory.
        :type application_count: int

        """
        self.swagger_types = {
            'active_fleet_count': 'int',
            'managed_instance_count': 'int',
            'jre_count': 'int',
            'installation_count': 'int',
            'application_count': 'int'
        }

        self.attribute_map = {
            'active_fleet_count': 'activeFleetCount',
            'managed_instance_count': 'managedInstanceCount',
            'jre_count': 'jreCount',
            'installation_count': 'installationCount',
            'application_count': 'applicationCount'
        }

        self._active_fleet_count = None
        self._managed_instance_count = None
        self._jre_count = None
        self._installation_count = None
        self._application_count = None

    @property
    def active_fleet_count(self):
        """
        **[Required]** Gets the active_fleet_count of this ResourceInventory.
        The number of _active_ fleets.


        :return: The active_fleet_count of this ResourceInventory.
        :rtype: int
        """
        return self._active_fleet_count

    @active_fleet_count.setter
    def active_fleet_count(self, active_fleet_count):
        """
        Sets the active_fleet_count of this ResourceInventory.
        The number of _active_ fleets.


        :param active_fleet_count: The active_fleet_count of this ResourceInventory.
        :type: int
        """
        self._active_fleet_count = active_fleet_count

    @property
    def managed_instance_count(self):
        """
        **[Required]** Gets the managed_instance_count of this ResourceInventory.
        The number of managed instances.


        :return: The managed_instance_count of this ResourceInventory.
        :rtype: int
        """
        return self._managed_instance_count

    @managed_instance_count.setter
    def managed_instance_count(self, managed_instance_count):
        """
        Sets the managed_instance_count of this ResourceInventory.
        The number of managed instances.


        :param managed_instance_count: The managed_instance_count of this ResourceInventory.
        :type: int
        """
        self._managed_instance_count = managed_instance_count

    @property
    def jre_count(self):
        """
        **[Required]** Gets the jre_count of this ResourceInventory.
        The number of Java Runtimes.


        :return: The jre_count of this ResourceInventory.
        :rtype: int
        """
        return self._jre_count

    @jre_count.setter
    def jre_count(self, jre_count):
        """
        Sets the jre_count of this ResourceInventory.
        The number of Java Runtimes.


        :param jre_count: The jre_count of this ResourceInventory.
        :type: int
        """
        self._jre_count = jre_count

    @property
    def installation_count(self):
        """
        **[Required]** Gets the installation_count of this ResourceInventory.
        The number of Java installations.


        :return: The installation_count of this ResourceInventory.
        :rtype: int
        """
        return self._installation_count

    @installation_count.setter
    def installation_count(self, installation_count):
        """
        Sets the installation_count of this ResourceInventory.
        The number of Java installations.


        :param installation_count: The installation_count of this ResourceInventory.
        :type: int
        """
        self._installation_count = installation_count

    @property
    def application_count(self):
        """
        **[Required]** Gets the application_count of this ResourceInventory.
        The number of applications.


        :return: The application_count of this ResourceInventory.
        :rtype: int
        """
        return self._application_count

    @application_count.setter
    def application_count(self, application_count):
        """
        Sets the application_count of this ResourceInventory.
        The number of applications.


        :param application_count: The application_count of this ResourceInventory.
        :type: int
        """
        self._application_count = application_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
