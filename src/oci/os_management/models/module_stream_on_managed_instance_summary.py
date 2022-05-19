# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModuleStreamOnManagedInstanceSummary(object):
    """
    Summary information pertaining to a module stream on a managed instance
    """

    #: A constant which can be used with the status property of a ModuleStreamOnManagedInstanceSummary.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a ModuleStreamOnManagedInstanceSummary.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a ModuleStreamOnManagedInstanceSummary.
    #: This constant has a value of "ACTIVE"
    STATUS_ACTIVE = "ACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new ModuleStreamOnManagedInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param module_name:
            The value to assign to the module_name property of this ModuleStreamOnManagedInstanceSummary.
        :type module_name: str

        :param stream_name:
            The value to assign to the stream_name property of this ModuleStreamOnManagedInstanceSummary.
        :type stream_name: str

        :param status:
            The value to assign to the status property of this ModuleStreamOnManagedInstanceSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param profiles:
            The value to assign to the profiles property of this ModuleStreamOnManagedInstanceSummary.
        :type profiles: list[oci.os_management.models.ModuleStreamProfileOnManagedInstanceSummary]

        :param software_source_id:
            The value to assign to the software_source_id property of this ModuleStreamOnManagedInstanceSummary.
        :type software_source_id: str

        :param time_modified:
            The value to assign to the time_modified property of this ModuleStreamOnManagedInstanceSummary.
        :type time_modified: datetime

        """
        self.swagger_types = {
            'module_name': 'str',
            'stream_name': 'str',
            'status': 'str',
            'profiles': 'list[ModuleStreamProfileOnManagedInstanceSummary]',
            'software_source_id': 'str',
            'time_modified': 'datetime'
        }

        self.attribute_map = {
            'module_name': 'moduleName',
            'stream_name': 'streamName',
            'status': 'status',
            'profiles': 'profiles',
            'software_source_id': 'softwareSourceId',
            'time_modified': 'timeModified'
        }

        self._module_name = None
        self._stream_name = None
        self._status = None
        self._profiles = None
        self._software_source_id = None
        self._time_modified = None

    @property
    def module_name(self):
        """
        **[Required]** Gets the module_name of this ModuleStreamOnManagedInstanceSummary.
        The name of the module that contains the stream.


        :return: The module_name of this ModuleStreamOnManagedInstanceSummary.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this ModuleStreamOnManagedInstanceSummary.
        The name of the module that contains the stream.


        :param module_name: The module_name of this ModuleStreamOnManagedInstanceSummary.
        :type: str
        """
        self._module_name = module_name

    @property
    def stream_name(self):
        """
        **[Required]** Gets the stream_name of this ModuleStreamOnManagedInstanceSummary.
        The name of the stream.


        :return: The stream_name of this ModuleStreamOnManagedInstanceSummary.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this ModuleStreamOnManagedInstanceSummary.
        The name of the stream.


        :param stream_name: The stream_name of this ModuleStreamOnManagedInstanceSummary.
        :type: str
        """
        self._stream_name = stream_name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ModuleStreamOnManagedInstanceSummary.
        The status of the stream

        A stream with the \"ENABLED\" status can be used as a source for installing
        profiles.  Streams with this status are also \"ACTIVE\".

        A stream with the \"DISABLED\" status cannot be the source for installing
        profiles.  To install profiles and packages from this stream, it must be
        enabled.

        A stream with the \"ACTIVE\" status can be used as a source for installing
        profiles.  The packages that comprise the stream are also used when a
        matching package is installed directly.  In general, a stream can have
        this status if it is the default stream for the module and no stream has
        been explicitly enabled.

        Allowed values for this property are: "ENABLED", "DISABLED", "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ModuleStreamOnManagedInstanceSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ModuleStreamOnManagedInstanceSummary.
        The status of the stream

        A stream with the \"ENABLED\" status can be used as a source for installing
        profiles.  Streams with this status are also \"ACTIVE\".

        A stream with the \"DISABLED\" status cannot be the source for installing
        profiles.  To install profiles and packages from this stream, it must be
        enabled.

        A stream with the \"ACTIVE\" status can be used as a source for installing
        profiles.  The packages that comprise the stream are also used when a
        matching package is installed directly.  In general, a stream can have
        this status if it is the default stream for the module and no stream has
        been explicitly enabled.


        :param status: The status of this ModuleStreamOnManagedInstanceSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "ACTIVE"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def profiles(self):
        """
        Gets the profiles of this ModuleStreamOnManagedInstanceSummary.
        The set of profiles that the module stream contains.


        :return: The profiles of this ModuleStreamOnManagedInstanceSummary.
        :rtype: list[oci.os_management.models.ModuleStreamProfileOnManagedInstanceSummary]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """
        Sets the profiles of this ModuleStreamOnManagedInstanceSummary.
        The set of profiles that the module stream contains.


        :param profiles: The profiles of this ModuleStreamOnManagedInstanceSummary.
        :type: list[oci.os_management.models.ModuleStreamProfileOnManagedInstanceSummary]
        """
        self._profiles = profiles

    @property
    def software_source_id(self):
        """
        Gets the software_source_id of this ModuleStreamOnManagedInstanceSummary.
        The OCID of the software source that provides this module stream.


        :return: The software_source_id of this ModuleStreamOnManagedInstanceSummary.
        :rtype: str
        """
        return self._software_source_id

    @software_source_id.setter
    def software_source_id(self, software_source_id):
        """
        Sets the software_source_id of this ModuleStreamOnManagedInstanceSummary.
        The OCID of the software source that provides this module stream.


        :param software_source_id: The software_source_id of this ModuleStreamOnManagedInstanceSummary.
        :type: str
        """
        self._software_source_id = software_source_id

    @property
    def time_modified(self):
        """
        Gets the time_modified of this ModuleStreamOnManagedInstanceSummary.
        The date and time of the last status change for this profile, as
        described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_modified of this ModuleStreamOnManagedInstanceSummary.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this ModuleStreamOnManagedInstanceSummary.
        The date and time of the last status change for this profile, as
        described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_modified: The time_modified of this ModuleStreamOnManagedInstanceSummary.
        :type: datetime
        """
        self._time_modified = time_modified

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
