# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstanceSummary(object):
    """
    An OCI Compute instance that is being managed
    """

    #: A constant which can be used with the status property of a ManagedInstanceSummary.
    #: This constant has a value of "NORMAL"
    STATUS_NORMAL = "NORMAL"

    #: A constant which can be used with the status property of a ManagedInstanceSummary.
    #: This constant has a value of "UNREACHABLE"
    STATUS_UNREACHABLE = "UNREACHABLE"

    #: A constant which can be used with the status property of a ManagedInstanceSummary.
    #: This constant has a value of "ERROR"
    STATUS_ERROR = "ERROR"

    #: A constant which can be used with the status property of a ManagedInstanceSummary.
    #: This constant has a value of "WARNING"
    STATUS_WARNING = "WARNING"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this ManagedInstanceSummary.
        :type display_name: str

        :param id:
            The value to assign to the id property of this ManagedInstanceSummary.
        :type id: str

        :param last_checkin:
            The value to assign to the last_checkin property of this ManagedInstanceSummary.
        :type last_checkin: str

        :param last_boot:
            The value to assign to the last_boot property of this ManagedInstanceSummary.
        :type last_boot: str

        :param updates_available:
            The value to assign to the updates_available property of this ManagedInstanceSummary.
        :type updates_available: int

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagedInstanceSummary.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this ManagedInstanceSummary.
        :type description: str

        :param status:
            The value to assign to the status property of this ManagedInstanceSummary.
            Allowed values for this property are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'id': 'str',
            'last_checkin': 'str',
            'last_boot': 'str',
            'updates_available': 'int',
            'compartment_id': 'str',
            'description': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'id': 'id',
            'last_checkin': 'lastCheckin',
            'last_boot': 'lastBoot',
            'updates_available': 'updatesAvailable',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'status': 'status'
        }

        self._display_name = None
        self._id = None
        self._last_checkin = None
        self._last_boot = None
        self._updates_available = None
        self._compartment_id = None
        self._description = None
        self._status = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ManagedInstanceSummary.
        user settable name


        :return: The display_name of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagedInstanceSummary.
        user settable name


        :param display_name: The display_name of this ManagedInstanceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagedInstanceSummary.
        OCID for the managed instance


        :return: The id of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagedInstanceSummary.
        OCID for the managed instance


        :param id: The id of this ManagedInstanceSummary.
        :type: str
        """
        self._id = id

    @property
    def last_checkin(self):
        """
        Gets the last_checkin of this ManagedInstanceSummary.
        Time at which the instance last checked in


        :return: The last_checkin of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._last_checkin

    @last_checkin.setter
    def last_checkin(self, last_checkin):
        """
        Sets the last_checkin of this ManagedInstanceSummary.
        Time at which the instance last checked in


        :param last_checkin: The last_checkin of this ManagedInstanceSummary.
        :type: str
        """
        self._last_checkin = last_checkin

    @property
    def last_boot(self):
        """
        Gets the last_boot of this ManagedInstanceSummary.
        Time at which the instance last booted


        :return: The last_boot of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._last_boot

    @last_boot.setter
    def last_boot(self, last_boot):
        """
        Sets the last_boot of this ManagedInstanceSummary.
        Time at which the instance last booted


        :param last_boot: The last_boot of this ManagedInstanceSummary.
        :type: str
        """
        self._last_boot = last_boot

    @property
    def updates_available(self):
        """
        Gets the updates_available of this ManagedInstanceSummary.
        Number of updates available to be installed


        :return: The updates_available of this ManagedInstanceSummary.
        :rtype: int
        """
        return self._updates_available

    @updates_available.setter
    def updates_available(self, updates_available):
        """
        Sets the updates_available of this ManagedInstanceSummary.
        Number of updates available to be installed


        :param updates_available: The updates_available of this ManagedInstanceSummary.
        :type: int
        """
        self._updates_available = updates_available

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagedInstanceSummary.
        OCID for the Compartment


        :return: The compartment_id of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagedInstanceSummary.
        OCID for the Compartment


        :param compartment_id: The compartment_id of this ManagedInstanceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this ManagedInstanceSummary.
        Information specified by the user about the managed instance


        :return: The description of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManagedInstanceSummary.
        Information specified by the user about the managed instance


        :param description: The description of this ManagedInstanceSummary.
        :type: str
        """
        self._description = description

    @property
    def status(self):
        """
        Gets the status of this ManagedInstanceSummary.
        status of the managed instance.

        Allowed values for this property are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ManagedInstanceSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ManagedInstanceSummary.
        status of the managed instance.


        :param status: The status of this ManagedInstanceSummary.
        :type: str
        """
        allowed_values = ["NORMAL", "UNREACHABLE", "ERROR", "WARNING"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
