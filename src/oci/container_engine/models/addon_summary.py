# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddonSummary(object):
    """
    The properties that define an addon summary.
    """

    #: A constant which can be used with the lifecycle_state property of a AddonSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AddonSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AddonSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AddonSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AddonSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AddonSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a AddonSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AddonSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AddonSummary.
        :type name: str

        :param version:
            The value to assign to the version property of this AddonSummary.
        :type version: str

        :param current_installed_version:
            The value to assign to the current_installed_version property of this AddonSummary.
        :type current_installed_version: str

        :param time_created:
            The value to assign to the time_created property of this AddonSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AddonSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "UPDATING", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param addon_error:
            The value to assign to the addon_error property of this AddonSummary.
        :type addon_error: oci.container_engine.models.AddonError

        """
        self.swagger_types = {
            'name': 'str',
            'version': 'str',
            'current_installed_version': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'addon_error': 'AddonError'
        }

        self.attribute_map = {
            'name': 'name',
            'version': 'version',
            'current_installed_version': 'currentInstalledVersion',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'addon_error': 'addonError'
        }

        self._name = None
        self._version = None
        self._current_installed_version = None
        self._time_created = None
        self._lifecycle_state = None
        self._addon_error = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AddonSummary.
        The name of the addon.


        :return: The name of this AddonSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AddonSummary.
        The name of the addon.


        :param name: The name of this AddonSummary.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """
        Gets the version of this AddonSummary.
        selected addon version, or null indicates autoUpdate


        :return: The version of this AddonSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this AddonSummary.
        selected addon version, or null indicates autoUpdate


        :param version: The version of this AddonSummary.
        :type: str
        """
        self._version = version

    @property
    def current_installed_version(self):
        """
        Gets the current_installed_version of this AddonSummary.
        current installed version of the addon


        :return: The current_installed_version of this AddonSummary.
        :rtype: str
        """
        return self._current_installed_version

    @current_installed_version.setter
    def current_installed_version(self, current_installed_version):
        """
        Sets the current_installed_version of this AddonSummary.
        current installed version of the addon


        :param current_installed_version: The current_installed_version of this AddonSummary.
        :type: str
        """
        self._current_installed_version = current_installed_version

    @property
    def time_created(self):
        """
        Gets the time_created of this AddonSummary.
        The time the cluster was created.


        :return: The time_created of this AddonSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AddonSummary.
        The time the cluster was created.


        :param time_created: The time_created of this AddonSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AddonSummary.
        The state of the addon.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "UPDATING", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AddonSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AddonSummary.
        The state of the addon.


        :param lifecycle_state: The lifecycle_state of this AddonSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "UPDATING", "NEEDS_ATTENTION", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def addon_error(self):
        """
        Gets the addon_error of this AddonSummary.
        The error info of the addon.


        :return: The addon_error of this AddonSummary.
        :rtype: oci.container_engine.models.AddonError
        """
        return self._addon_error

    @addon_error.setter
    def addon_error(self, addon_error):
        """
        Sets the addon_error of this AddonSummary.
        The error info of the addon.


        :param addon_error: The addon_error of this AddonSummary.
        :type: oci.container_engine.models.AddonError
        """
        self._addon_error = addon_error

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
