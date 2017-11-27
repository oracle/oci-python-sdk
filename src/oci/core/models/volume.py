# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Volume(object):

    def __init__(self, **kwargs):
        """
        Initializes a new Volume object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this Volume.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Volume.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this Volume.
        :type display_name: str

        :param id:
            The value to assign to the id property of this Volume.
        :type id: str

        :param is_hydrated:
            The value to assign to the is_hydrated property of this Volume.
        :type is_hydrated: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Volume.
            Allowed values for this property are: "PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this Volume.
        :type size_in_gbs: int

        :param size_in_mbs:
            The value to assign to the size_in_mbs property of this Volume.
        :type size_in_mbs: int

        :param source_details:
            The value to assign to the source_details property of this Volume.
        :type source_details: VolumeSourceDetails

        :param time_created:
            The value to assign to the time_created property of this Volume.
        :type time_created: datetime

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'is_hydrated': 'bool',
            'lifecycle_state': 'str',
            'size_in_gbs': 'int',
            'size_in_mbs': 'int',
            'source_details': 'VolumeSourceDetails',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'is_hydrated': 'isHydrated',
            'lifecycle_state': 'lifecycleState',
            'size_in_gbs': 'sizeInGBs',
            'size_in_mbs': 'sizeInMBs',
            'source_details': 'sourceDetails',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._is_hydrated = None
        self._lifecycle_state = None
        self._size_in_gbs = None
        self._size_in_mbs = None
        self._source_details = None
        self._time_created = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this Volume.
        The Availability Domain of the volume.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this Volume.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Volume.
        The Availability Domain of the volume.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this Volume.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Volume.
        The OCID of the compartment that contains the volume.


        :return: The compartment_id of this Volume.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Volume.
        The OCID of the compartment that contains the volume.


        :param compartment_id: The compartment_id of this Volume.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Volume.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Volume.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Volume.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Volume.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this Volume.
        The OCID of the volume.


        :return: The id of this Volume.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Volume.
        The OCID of the volume.


        :param id: The id of this Volume.
        :type: str
        """
        self._id = id

    @property
    def is_hydrated(self):
        """
        Gets the is_hydrated of this Volume.
        Specifies whether the cloned volume's data has finished copying from the source volume or backup.


        :return: The is_hydrated of this Volume.
        :rtype: bool
        """
        return self._is_hydrated

    @is_hydrated.setter
    def is_hydrated(self, is_hydrated):
        """
        Sets the is_hydrated of this Volume.
        Specifies whether the cloned volume's data has finished copying from the source volume or backup.


        :param is_hydrated: The is_hydrated of this Volume.
        :type: bool
        """
        self._is_hydrated = is_hydrated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Volume.
        The current state of a volume.

        Allowed values for this property are: "PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Volume.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Volume.
        The current state of a volume.


        :param lifecycle_state: The lifecycle_state of this Volume.
        :type: str
        """
        allowed_values = ["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def size_in_gbs(self):
        """
        Gets the size_in_gbs of this Volume.
        The size of the volume in GBs.


        :return: The size_in_gbs of this Volume.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this Volume.
        The size of the volume in GBs.


        :param size_in_gbs: The size_in_gbs of this Volume.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    @property
    def size_in_mbs(self):
        """
        Gets the size_in_mbs of this Volume.
        The size of the volume in MBs. This field is deprecated. Use sizeInGBs instead.


        :return: The size_in_mbs of this Volume.
        :rtype: int
        """
        return self._size_in_mbs

    @size_in_mbs.setter
    def size_in_mbs(self, size_in_mbs):
        """
        Sets the size_in_mbs of this Volume.
        The size of the volume in MBs. This field is deprecated. Use sizeInGBs instead.


        :param size_in_mbs: The size_in_mbs of this Volume.
        :type: int
        """
        self._size_in_mbs = size_in_mbs

    @property
    def source_details(self):
        """
        Gets the source_details of this Volume.
        The volume source, either an existing volume in the same Availability Domain or a volume backup.
        If null, an empty volume is created.


        :return: The source_details of this Volume.
        :rtype: VolumeSourceDetails
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this Volume.
        The volume source, either an existing volume in the same Availability Domain or a volume backup.
        If null, an empty volume is created.


        :param source_details: The source_details of this Volume.
        :type: VolumeSourceDetails
        """
        self._source_details = source_details

    @property
    def time_created(self):
        """
        Gets the time_created of this Volume.
        The date and time the volume was created. Format defined by RFC3339.


        :return: The time_created of this Volume.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Volume.
        The date and time the volume was created. Format defined by RFC3339.


        :param time_created: The time_created of this Volume.
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
