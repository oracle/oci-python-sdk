# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MountTargetSummary(object):
    """
    Summary information for the specified mount target.
    """

    #: A constant which can be used with the lifecycle_state property of a MountTargetSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MountTargetSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MountTargetSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MountTargetSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MountTargetSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new MountTargetSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this MountTargetSummary.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MountTargetSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this MountTargetSummary.
        :type display_name: str

        :param export_set_id:
            The value to assign to the export_set_id property of this MountTargetSummary.
        :type export_set_id: str

        :param id:
            The value to assign to the id property of this MountTargetSummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MountTargetSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param private_ip_ids:
            The value to assign to the private_ip_ids property of this MountTargetSummary.
        :type private_ip_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this MountTargetSummary.
        :type subnet_id: str

        :param time_created:
            The value to assign to the time_created property of this MountTargetSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'export_set_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'private_ip_ids': 'list[str]',
            'subnet_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'export_set_id': 'exportSetId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'private_ip_ids': 'privateIpIds',
            'subnet_id': 'subnetId',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._export_set_id = None
        self._id = None
        self._lifecycle_state = None
        self._private_ip_ids = None
        self._subnet_id = None
        self._time_created = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this MountTargetSummary.
        The availability domain the mount target is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this MountTargetSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this MountTargetSummary.
        The availability domain the mount target is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this MountTargetSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MountTargetSummary.
        The OCID of the compartment that contains the mount target.


        :return: The compartment_id of this MountTargetSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MountTargetSummary.
        The OCID of the compartment that contains the mount target.


        :param compartment_id: The compartment_id of this MountTargetSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this MountTargetSummary.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My mount target`


        :return: The display_name of this MountTargetSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MountTargetSummary.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My mount target`


        :param display_name: The display_name of this MountTargetSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def export_set_id(self):
        """
        Gets the export_set_id of this MountTargetSummary.
        The OCID of the associated export set. Controls what file
        systems will be exported using Network File System (NFS) protocol on
        this mount target.


        :return: The export_set_id of this MountTargetSummary.
        :rtype: str
        """
        return self._export_set_id

    @export_set_id.setter
    def export_set_id(self, export_set_id):
        """
        Sets the export_set_id of this MountTargetSummary.
        The OCID of the associated export set. Controls what file
        systems will be exported using Network File System (NFS) protocol on
        this mount target.


        :param export_set_id: The export_set_id of this MountTargetSummary.
        :type: str
        """
        self._export_set_id = export_set_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MountTargetSummary.
        The OCID of the mount target.


        :return: The id of this MountTargetSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MountTargetSummary.
        The OCID of the mount target.


        :param id: The id of this MountTargetSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MountTargetSummary.
        The current state of the mount target.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MountTargetSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MountTargetSummary.
        The current state of the mount target.


        :param lifecycle_state: The lifecycle_state of this MountTargetSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def private_ip_ids(self):
        """
        **[Required]** Gets the private_ip_ids of this MountTargetSummary.
        The OCIDs of the private IP addresses associated with this mount target.


        :return: The private_ip_ids of this MountTargetSummary.
        :rtype: list[str]
        """
        return self._private_ip_ids

    @private_ip_ids.setter
    def private_ip_ids(self, private_ip_ids):
        """
        Sets the private_ip_ids of this MountTargetSummary.
        The OCIDs of the private IP addresses associated with this mount target.


        :param private_ip_ids: The private_ip_ids of this MountTargetSummary.
        :type: list[str]
        """
        self._private_ip_ids = private_ip_ids

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this MountTargetSummary.
        The OCID of the subnet the mount target is in.


        :return: The subnet_id of this MountTargetSummary.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this MountTargetSummary.
        The OCID of the subnet the mount target is in.


        :param subnet_id: The subnet_id of this MountTargetSummary.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MountTargetSummary.
        The date and time the mount target was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this MountTargetSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MountTargetSummary.
        The date and time the mount target was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this MountTargetSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
