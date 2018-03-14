# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportSet(object):

    def __init__(self, **kwargs):
        """
        Initializes a new ExportSet object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this ExportSet.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExportSet.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ExportSet.
        :type display_name: str

        :param id:
            The value to assign to the id property of this ExportSet.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExportSet.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param max_fs_stat_bytes:
            The value to assign to the max_fs_stat_bytes property of this ExportSet.
        :type max_fs_stat_bytes: int

        :param max_fs_stat_files:
            The value to assign to the max_fs_stat_files property of this ExportSet.
        :type max_fs_stat_files: int

        :param time_created:
            The value to assign to the time_created property of this ExportSet.
        :type time_created: datetime

        :param vcn_id:
            The value to assign to the vcn_id property of this ExportSet.
        :type vcn_id: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'max_fs_stat_bytes': 'int',
            'max_fs_stat_files': 'int',
            'time_created': 'datetime',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'max_fs_stat_bytes': 'maxFsStatBytes',
            'max_fs_stat_files': 'maxFsStatFiles',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._max_fs_stat_bytes = None
        self._max_fs_stat_files = None
        self._time_created = None
        self._vcn_id = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this ExportSet.
        The availability domain the export set is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this ExportSet.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ExportSet.
        The availability domain the export set is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this ExportSet.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExportSet.
        The OCID of the compartment that contains the export set.


        :return: The compartment_id of this ExportSet.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExportSet.
        The OCID of the compartment that contains the export set.


        :param compartment_id: The compartment_id of this ExportSet.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExportSet.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My export set`


        :return: The display_name of this ExportSet.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExportSet.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My export set`


        :param display_name: The display_name of this ExportSet.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExportSet.
        The OCID of the export set.


        :return: The id of this ExportSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExportSet.
        The OCID of the export set.


        :param id: The id of this ExportSet.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExportSet.
        The current state of the export set.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExportSet.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExportSet.
        The current state of the export set.


        :param lifecycle_state: The lifecycle_state of this ExportSet.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def max_fs_stat_bytes(self):
        """
        Gets the max_fs_stat_bytes of this ExportSet.
        Controls the maximum `tbytes`, `fbytes`, and `abytes`,
        values reported by `NFS FSSTAT` calls through any associated
        mount targets. This is an advanced feature. For most
        applications, use the default value. The
        `tbytes` value reported by `FSSTAT` will be
        `maxFsStatBytes`. The value of `fbytes` and `abytes` will be
        `maxFsStatBytes` minus the metered size of the file
        system. If the metered size is larger than `maxFsStatBytes`,
        then `fbytes` and `abytes` will both be '0'.


        :return: The max_fs_stat_bytes of this ExportSet.
        :rtype: int
        """
        return self._max_fs_stat_bytes

    @max_fs_stat_bytes.setter
    def max_fs_stat_bytes(self, max_fs_stat_bytes):
        """
        Sets the max_fs_stat_bytes of this ExportSet.
        Controls the maximum `tbytes`, `fbytes`, and `abytes`,
        values reported by `NFS FSSTAT` calls through any associated
        mount targets. This is an advanced feature. For most
        applications, use the default value. The
        `tbytes` value reported by `FSSTAT` will be
        `maxFsStatBytes`. The value of `fbytes` and `abytes` will be
        `maxFsStatBytes` minus the metered size of the file
        system. If the metered size is larger than `maxFsStatBytes`,
        then `fbytes` and `abytes` will both be '0'.


        :param max_fs_stat_bytes: The max_fs_stat_bytes of this ExportSet.
        :type: int
        """
        self._max_fs_stat_bytes = max_fs_stat_bytes

    @property
    def max_fs_stat_files(self):
        """
        Gets the max_fs_stat_files of this ExportSet.
        Controls the maximum `ffiles`, `ffiles`, and `afiles`
        values reported by `NFS FSSTAT` calls through any associated
        mount targets. This is an advanced feature. For most
        applications, use the default value. The
        `tfiles` value reported by `FSSTAT` will be
        `maxFsStatFiles`. The value of `ffiles` and `afiles` will be
        `maxFsStatFiles` minus the metered size of the file
        system. If the metered size is larger than `maxFsStatFiles`,
        then `ffiles` and `afiles` will both be '0'.


        :return: The max_fs_stat_files of this ExportSet.
        :rtype: int
        """
        return self._max_fs_stat_files

    @max_fs_stat_files.setter
    def max_fs_stat_files(self, max_fs_stat_files):
        """
        Sets the max_fs_stat_files of this ExportSet.
        Controls the maximum `ffiles`, `ffiles`, and `afiles`
        values reported by `NFS FSSTAT` calls through any associated
        mount targets. This is an advanced feature. For most
        applications, use the default value. The
        `tfiles` value reported by `FSSTAT` will be
        `maxFsStatFiles`. The value of `ffiles` and `afiles` will be
        `maxFsStatFiles` minus the metered size of the file
        system. If the metered size is larger than `maxFsStatFiles`,
        then `ffiles` and `afiles` will both be '0'.


        :param max_fs_stat_files: The max_fs_stat_files of this ExportSet.
        :type: int
        """
        self._max_fs_stat_files = max_fs_stat_files

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ExportSet.
        The date and time the export set was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this ExportSet.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExportSet.
        The date and time the export set was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this ExportSet.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this ExportSet.
        The OCID of the virtual cloud network (VCN) the export set is in.


        :return: The vcn_id of this ExportSet.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this ExportSet.
        The OCID of the virtual cloud network (VCN) the export set is in.


        :param vcn_id: The vcn_id of this ExportSet.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
